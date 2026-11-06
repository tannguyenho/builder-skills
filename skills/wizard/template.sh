#!/usr/bin/env bash
#
# Wizard dẫn một người đi qua một quy trình làm tay, từng bước một.
# Được tạo bởi skill /wizard.
#
# Mọi thứ phía trên dấu mốc "STAGES" là thư viện wizard: không sửa tay.
# Viết các stage cho từng bước ở bên dưới dấu mốc.

set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────
# Thư viện wizard: UX dễ chịu, nhất quán, giống hệt nhau ở mọi wizard.
# ──────────────────────────────────────────────────────────────────────────

if [[ -t 1 ]] && command -v tput >/dev/null 2>&1 && [[ "$(tput colors 2>/dev/null || echo 0)" -ge 8 ]]; then
  BOLD=$(tput bold); DIM=$(tput dim); RESET=$(tput sgr0)
  BLUE=$(tput setaf 4); GREEN=$(tput setaf 2); YELLOW=$(tput setaf 3)
else
  BOLD=""; DIM=""; RESET=""; BLUE=""; GREEN=""; YELLOW=""
fi

# Người viết đặt giá trị này ở đầu phần stages.
TOTAL_STAGES=0

_STAGE_INDEX=0
ENV_FILE="${ENV_FILE:-.env}"
WRITTEN_ENV=()    # các KEY đã ghi vào ENV_FILE trong lần chạy này
WRITTEN_SECRET=() # các NAME secret đã đặt trong lần chạy này
SKIPPED=()        # những việc không làm được (vd thiếu gh)

# _clear xoá terminal để chỉ bước hiện tại hiện trên màn hình. Không làm gì khi
# output không phải terminal, để log khi pipe vẫn đọc được.
_clear() {
  [[ -t 1 ]] || return 0
  if command -v tput >/dev/null 2>&1 && tput clear 2>/dev/null; then return 0; fi
  printf '\033[2J\033[3J\033[H'
}

# banner "Tiêu đề" hiện khung mở đầu: wizard này làm gì.
banner() {
  _clear
  printf '\n%s%s  %s%s\n' "$BOLD" "$BLUE" "$1" "$RESET"
  printf '%s  %s bước%s\n\n' "$DIM" "$TOTAL_STAGES" "$RESET"
  printf '%s  Bạn thao tác trên trình duyệt; wizard này nói chính xác cần làm gì và\n' "$DIM"
  printf '  lưu lại các giá trị bạn copy về. Dừng bất cứ lúc nào bằng Ctrl-C và chạy lại\n'
  printf '  sau, vì nó nhớ các giá trị đã lưu.%s\n' "$RESET"
  pause "Sẵn sàng bắt đầu chưa?"
}

# stage "Tên" xoá màn hình, rồi thông báo một stage và hiện tiến độ.
# Xoá màn hình để chỉ giữ bước hiện tại.
stage() {
  _clear
  _STAGE_INDEX=$((_STAGE_INDEX + 1))
  printf '\n%s%s▸ Bước %s/%s · %s%s\n' \
    "$BOLD" "$BLUE" "$_STAGE_INDEX" "$TOTAL_STAGES" "$1" "$RESET"
}

# say "..." in một dòng hướng dẫn thường.
say()  { printf '  %s\n' "$1"; }
# step "..." là một thao tác (kiểu có đánh số) người dùng làm trên trình duyệt.
step() { printf '  %s•%s %s\n' "$BLUE" "$RESET" "$1"; }
note() { printf '  %s%s%s\n' "$DIM" "$1" "$RESET"; }
warn() { printf '  %s⚠ %s%s\n' "$YELLOW" "$1" "$RESET"; }

# open_url URL mở URL trong trình duyệt của người dùng, đa nền tảng kể cả WSL.
open_url() {
  local url="$1"
  printf '  %s↗ đang mở%s %s\n' "$GREEN" "$RESET" "$url"
  { if   command -v wslview     >/dev/null 2>&1; then wslview "$url"
    elif command -v explorer.exe >/dev/null 2>&1; then explorer.exe "$url"
    elif command -v xdg-open    >/dev/null 2>&1; then xdg-open "$url"
    elif command -v open        >/dev/null 2>&1; then open "$url"
    else false; fi
  } >/dev/null 2>&1 || warn "không mở được trình duyệt, hãy tự truy cập: $url"
}

# pause "msg" chờ người dùng xác nhận đã làm xong phần thao tác tay.
pause() {
  printf '  %s%s%s ' "$DIM" "${1:-Nhấn Enter để tiếp tục}" "$RESET"
  read -r _ || true
}

# confirm "câu hỏi" là cổng y/N; trả về thành công nếu trả lời có.
confirm() {
  local reply=""
  printf '  %s? %s [y/N] ' "$YELLOW" "$1"
  read -r reply || true
  [[ "$reply" =~ ^[Yy] ]]
}

# _existing KEY: giá trị hiện tại của KEY trong ENV_FILE, nếu có, đã gỡ dấu nháy
# đơn do write_env thêm vào hoặc gỡ nháy kép của một giá trị dotenv thông thường.
_existing() {
  [[ -f "$ENV_FILE" ]] || return 1
  local line value sq="'\\''"; line=$(grep -E "^${1}=" "$ENV_FILE" | tail -n1) || return 1
  value="${line#*=}"
  if [[ "$value" == \'*\' ]]; then value="${value:1:${#value}-2}"; value="${value//"$sq"/\'}"
  elif [[ "$value" == \"*\" ]]; then
    value="${value:1:${#value}-2}"
    [[ "$value" == *[\\\$\"]* ]] && return 1   # có escape, $ hoặc ": không giải mã an toàn được; hỏi lại
  fi
  printf '%s' "$value"
}

# ask KEY "Câu hỏi" đọc một giá trị vào $KEY. Ở những lần chạy lại, đưa giá trị
# đang có trong .env làm mặc định (Enter để giữ). Nhập hiện chữ (không bí mật),
# chỉnh sửa bằng Readline. Thất bại khi gặp EOF mà không có gì nhập vào.
ask() {
  local key="$1" prompt="$2" current input s=$'\001' e=$'\002' p rc=0
  current=$(_existing "$key" || true)
  # Readline cần mã màu được bọc trong \001..\002 để đặt con trỏ đúng chỗ.
  p="  $s$BOLD$e$prompt$s$RESET$e "
  [[ -n "$current" ]] && p+="$s$DIM$e[Enter để giữ giá trị hiện tại]$s$RESET$e "
  read -e -r -p "$p" input || rc=1
  if (( rc )) && [[ -z "$input" ]]; then return 1; fi
  [[ -z "$input" && -n "$current" ]] && input="$current"
  printf -v "$key" '%s' "$input"
}

# ask_secret KEY "Câu hỏi" giống ask, nhưng chữ nhập vào bị ẩn.
ask_secret() {
  local key="$1" prompt="$2" current input rc=0
  current=$(_existing "$key" || true)
  if [[ -n "$current" ]]; then
    printf '  %s%s%s %s[Enter để giữ giá trị hiện tại]%s ' "$BOLD" "$prompt" "$RESET" "$DIM" "$RESET"
  else
    printf '  %s%s%s ' "$BOLD" "$prompt" "$RESET"
  fi
  read -rs input || rc=1
  printf '\n'
  if (( rc )) && [[ -z "$input" ]]; then return 1; fi
  [[ -z "$input" && -n "$current" ]] && input="$current"
  printf -v "$key" '%s' "$input"
}

# write_env KEY VALUE upsert KEY='VALUE' vào ENV_FILE (thay dòng cũ nếu có)
# và đặt $KEY. Chạy nhiều lần vẫn cho cùng kết quả. Tạo ENV_FILE với mode 0600;
# ghi xuyên qua symlink và giữ nguyên mode của file đã có.
write_env() {
  local key="$1" value="$2" tmp sq="'\\''"
  [[ -e "$ENV_FILE" ]] || (umask 077 && : > "$ENV_FILE")
  tmp=$(mktemp)
  grep -vE "^${key}=" "$ENV_FILE" > "$tmp" || true
  printf "%s='%s'\n" "$key" "${value//\'/$sq}" >> "$tmp"
  cat "$tmp" > "$ENV_FILE"
  rm -f "$tmp"
  printf -v "$key" '%s' "$value"
  WRITTEN_ENV+=("$key")
  printf '  %s✓ đã ghi%s %s → %s\n' "$GREEN" "$RESET" "$key" "$ENV_FILE"
}

# set_secret NAME VALUE đặt một secret GitHub Actions cho repo qua gh. Nếu gh
# không có hoặc chưa đăng nhập thì chuyển sang cảnh báo (và ghi nhận lại).
set_secret() {
  local name="$1" value="$2"
  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    if printf '%s' "$value" | gh secret set "$name" >/dev/null 2>&1; then
      WRITTEN_SECRET+=("$name")
      printf '  %s✓ đã đặt%s GitHub secret %s\n' "$GREEN" "$RESET" "$name"
      return
    fi
  fi
  SKIPPED+=("GitHub secret $name (tự đặt bằng tay: gh secret set $name)")
  warn "bỏ qua GitHub secret $name: gh chưa sẵn sàng; đặt sau"
}

# set_var NAME VALUE đặt một variable GitHub Actions cho repo (không bí mật).
set_var() {
  local name="$1" value="$2"
  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    if gh variable set "$name" --body "$value" >/dev/null 2>&1; then
      printf '  %s✓ đã đặt%s GitHub variable %s\n' "$GREEN" "$RESET" "$name"
      return
    fi
  fi
  SKIPPED+=("GitHub variable $name")
  warn "bỏ qua GitHub variable $name, gh chưa sẵn sàng; đặt sau"
}

# finish xoá màn hình, rồi hiện bản tổng kết mọi thứ đã cấu hình.
finish() {
  _clear
  printf '\n%s%s  ✓ Thiết lập xong%s\n' "$BOLD" "$GREEN" "$RESET"
  (( ${#WRITTEN_ENV[@]} ))    && note "đã ghi ${#WRITTEN_ENV[@]} giá trị vào $ENV_FILE: ${WRITTEN_ENV[*]}"
  (( ${#WRITTEN_SECRET[@]} )) && note "đã đặt ${#WRITTEN_SECRET[@]} GitHub secret: ${WRITTEN_SECRET[*]}"
  if (( ${#SKIPPED[@]} )); then
    printf '\n'; warn "còn phải làm tay:"
    for s in "${SKIPPED[@]}"; do note "  - $s"; done
  fi
  printf '\n'
}

# ──────────────────────────────────────────────────────────────────────────
# STAGES: viết phần này. Mỗi bước người dùng làm là một stage().
# Thay ví dụ bên dưới. Đặt TOTAL_STAGES khớp với số stage bạn viết.
# Giữ mọi stage bên trong run_wizard và giữ nguyên dòng cuối: nhờ vậy bash
# phân tích cả file trước lời nhắc đầu tiên, nên sửa file giữa chừng không làm hỏng lần chạy.
# ──────────────────────────────────────────────────────────────────────────

run_wizard() {

TOTAL_STAGES=1

banner "Thiết lập Stripe"

# ── Stage ví dụ: thay bằng các bước thật của bạn ──────────────────────────
stage "Stripe: API key"
say "Mình sẽ lấy test key của Stripe và lưu lại cho môi trường dev local + CI."
open_url "https://dashboard.stripe.com/test/apikeys"
step "Ở trang API keys, copy Publishable key (bắt đầu bằng pk_test_)."
ask STRIPE_PUBLISHABLE_KEY "Dán publishable key:"
step "Bấm 'Reveal test key' ở dòng Secret key, rồi copy nó."
ask_secret STRIPE_SECRET_KEY "Dán secret key:"
write_env STRIPE_PUBLISHABLE_KEY "$STRIPE_PUBLISHABLE_KEY"
write_env STRIPE_SECRET_KEY "$STRIPE_SECRET_KEY"
set_secret STRIPE_SECRET_KEY "$STRIPE_SECRET_KEY"   # CI cần cái này
# ──────────────────────────────────────────────────────────────────────────

finish
}

run_wizard "$@"; exit
