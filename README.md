# builder-skills

Bộ skill của **UX Foundation** cho Claude (Claude Code, app Claude desktop, claude.ai). Mỗi skill là một quy trình được đóng gói sẵn: Claude đọc hướng dẫn trong skill và làm theo, nên cả team chạy cùng một cách, cùng một chuẩn.

Bộ skill đi theo vòng đời một sản phẩm: **chuẩn bị** môi trường → **nghĩ sản phẩm** → **dựng Figma** → **viết tài liệu** → **code** → **cải thiện agent**. Toàn bộ bằng tiếng Việt; một phần được dịch và chỉnh từ [mattpocock/skills](https://github.com/mattpocock/skills) và [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) (xem [Nguồn & giấy phép](#4-nguồn--giấy-phép)).

**Cách gọi:** cột *Gọi* ghi `🙋 tay` nghĩa là skill chỉ chạy khi bạn gõ lệnh slash (vd `/builder-skills:to-spec`), vì nó làm việc lớn hoặc ghi ra ngoài; `🤖 tự động` nghĩa là Claude tự gọi khi câu bạn nói khớp mô tả, bạn vẫn gõ lệnh slash được. Cài bằng plugin thì lệnh có tiền tố `builder-skills:`; chép tay thì gõ thẳng `/<tên-skill>`.

## Danh sách skill

### ⚙️ Setup — chuẩn bị môi trường

| Skill | Dùng để | Gọi |
| --- | --- | --- |
| [`setup-agent`](skills/setup-agent/SKILL.md) | Cấu hình repo cho các skill doc/coding: chọn issue tracker (GitHub, GitLab hay file local), bộ label triage, bố cục tài liệu domain. Ghi khối `## Agent skills` vào `CLAUDE.md`/`AGENTS.md`. **Chạy một lần trước** khi dùng `to-spec`, `to-tickets`, `triage`, `wayfinder`, `implement-spec`, `code-review` | 🙋 tay |
| [`init-figma-design`](skills/init-figma-design/SKILL.md) | Dựng kiến trúc Figma cho app mới (Team → Folder → File) và ghi link vào `ARCHITECTURE.md` | 🤖 tự động |

### 🚀 Start product — khởi động sản phẩm

| Skill | Dùng để | Gọi |
| --- | --- | --- |
| [`product-design`](skills/product-design/SKILL.md) | Thiết kế và thẩm định một ý tưởng sản phẩm từ đầu: nghiên cứu thị trường, đối thủ, khách hàng, kênh phân phối, mô hình kinh doanh, thương hiệu, dự phóng tài chính, thí nghiệm kiểm chứng. Lưu checkpoint để làm tiếp | 🤖 tự động |
| [`product-competitors`](skills/product-competitors/SKILL.md) | Phân tích đối thủ sâu bằng dữ liệu web thật: sản phẩm, giá, cảm nhận khách hàng, GTM, tín hiệu tăng trưởng. Ra battle card, bảng giá, ma trận tính năng | 🤖 tự động |
| [`wayfinder`](skills/wayfinder/SKILL.md) | Lên kế hoạch cho một khối việc quá lớn so với một phiên agent: vẽ "bản đồ" các ticket quyết định trên issue tracker rồi giải từng cái đến khi rõ đường | 🙋 tay |

### 🎨 Figma — sắp xếp file Figma

| Skill | Dùng để | Gọi |
| --- | --- | --- |
| [`ds-page-manager`](skills/ds-page-manager/SKILL.md) | Sắp xếp page trong file **Design System** theo Category (FOUNDATION, ACTIONS, DATA ENTRY…) | 🤖 tự động |
| [`snowflake-page-manager`](skills/snowflake-page-manager/SKILL.md) | Sắp xếp page trong file **Snowflake** theo BASE / COMPONENT / SCREEN | 🤖 tự động |
| [`handoff-page-manager`](skills/handoff-page-manager/SKILL.md) | Sắp xếp page trong file **Handoff** theo CHANGE LOG / USER FLOW / UI GUIDELINE / DESIGN QA / COVER | 🤖 tự động |

### 📝 Doc — chốt ý tưởng thành tài liệu

| Skill | Dùng để | Gọi |
| --- | --- | --- |
| [`grill-me`](skills/grill-me/SKILL.md) | Claude vặn hỏi bạn liên tục về một kế hoạch/ý tưởng, từng vòng câu hỏi có đề xuất sẵn, đến khi hai bên hiểu giống nhau | 🤖 tự động |
| [`grill-with-docs`](skills/grill-with-docs/SKILL.md) | Như `grill-me`, đồng thời ghi tài liệu ngay trong lúc hỏi: thuật ngữ vào `GLOSSARY.md`, quyết định khó đảo ngược vào ADR (`docs/adr/`) | 🤖 tự động |
| [`to-spec`](skills/to-spec/SKILL.md) | Tổng hợp cuộc trò chuyện hiện tại thành một spec và đăng lên issue tracker (không phỏng vấn thêm) | 🙋 tay |
| [`to-tickets`](skills/to-tickets/SKILL.md) | Chia spec/kế hoạch thành các ticket lát dọc (tracer bullet), mỗi ticket ghi rõ bị chặn bởi ticket nào | 🙋 tay |
| [`triage`](skills/triage/SKILL.md) | Đưa issue và PR bên ngoài qua các trạng thái triage: phân loại, xác minh, hỏi thêm nếu cần, viết brief sẵn cho agent | 🙋 tay |

### 💻 Coding — viết và review code

| Skill | Dùng để | Gọi |
| --- | --- | --- |
| [`implement`](skills/implement/SKILL.md) | Làm một phần việc theo spec/ticket bằng TDD, chạy typecheck và test, tự `code-review` rồi commit | 🙋 tay |
| [`implement-spec`](skills/implement-spec/SKILL.md) | Làm trọn một spec đã có ticket: chạy nhiều subagent song song theo đồ thị ticket, gộp về một nhánh tích hợp, review cuối | 🙋 tay |
| [`code-review`](skills/code-review/SKILL.md) | Review thay đổi từ một mốc (commit, nhánh, tag) theo hai trục song song: **Standards** (đúng chuẩn code của repo?) và **Spec** (đúng điều issue/spec yêu cầu?) | 🤖 tự động |
| [`codebase-design`](skills/codebase-design/SKILL.md) | Bộ từ vựng thiết kế "deep module": interface, seam, adapter, depth… Dùng khi thiết kế/cải thiện interface của một module, làm code dễ test và dễ cho AI đọc | 🤖 tự động |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | Quét codebase tìm chỗ nên "làm sâu" module, xuất báo cáo HTML trực quan, rồi cùng bạn đào sâu phương án bạn chọn | 🙋 tay |
| [`pr`](skills/pr/SKILL.md) | Viết mô tả PR: tóm tắt, bằng chứng, rủi ro khi merge, phạm vi ảnh hưởng | 🤖 tự động |

### 🤖 Agent — cải thiện cách agent làm việc

| Skill | Dùng để | Gọi |
| --- | --- | --- |
| [`retro`](skills/retro/SKILL.md) | Retrospective một phiên code: tìm chỗ cải thiện môi trường của agent (điều hướng file, check tự động, chuẩn code, `CLAUDE.md`, tool…) | 🙋 tay |
| [`wizard`](skills/wizard/SKILL.md) | Sinh một script bash tương tác dẫn người làm từng bước mà chỉ người làm được (tạo credential, CI secret, bấm dashboard bên thứ ba, migration một lần) | 🤖 tự động |
| [`writing-for-agents`](skills/writing-for-agents/SKILL.md) | Cách viết tài liệu cho agent đọc: skill, `CLAUDE.md`, `AGENTS.md` | 🤖 tự động |

### Luồng dùng gợi ý

```
⚙️  setup-agent  (một lần cho mỗi repo)        init-figma-design  (một lần cho mỗi app)
        │                                               │
🚀  product-design ─ product-competitors              🎨  ds- / snowflake- / handoff-page-manager
        │
📝  grill-me / grill-with-docs  →  to-spec  →  to-tickets        (việc quá lớn: wayfinder)
        │                                        ▲
        │                              triage (issue từ bên ngoài)
        ▼
💻  implement (một ticket)  hoặc  implement-spec (cả spec)  →  code-review  →  pr
        │
🤖  retro  →  sửa CLAUDE.md / chuẩn code / check tự động  (dùng writing-for-agents)
```

Kiến trúc dài hạn: chạy `improve-codebase-architecture` định kỳ; `codebase-design` được các skill khác tự gọi khi cần bàn về interface.

---

## 1. Cài đặt

Chọn **một** trong ba cách. Đừng cài cùng một skill bằng hai cách, vì Claude sẽ thấy hai bản và có thể chọn nhầm bản cũ.

### Cách A — Plugin cho Claude Code / app Claude desktop (khuyên dùng)

Cài một lần, sau này cập nhật bằng một lệnh. Chạy trong terminal:

```bash
claude plugin marketplace add tannguyenho/builder-skills
```

```bash
claude plugin install builder-skills@tannguyenho
```

Hoặc gõ trong phiên `claude` tương tác: `/plugin marketplace add tannguyenho/builder-skills` rồi `/plugin install builder-skills@tannguyenho`.

Plugin cài ở phạm vi user nên dùng được cả trong terminal lẫn tab **Code** của app Claude desktop. Mở phiên mới để Claude nạp skill.

**Cập nhật** khi repo có skill mới hoặc bản sửa (lệnh 1 tải bản mới của repo, lệnh 2 cài bản đó), rồi mở phiên mới:

```bash
claude plugin marketplace update tannguyenho
```

```bash
claude plugin update builder-skills@tannguyenho
```

> **Tránh trùng skill:** nếu trước đây bạn đã có các skill này dưới tên cũ (`uxf-init-design`, `uxf-ds-page-manager`, `uxf-snowflake-page-manager`, `uxf-handoff-page-manager`) — chép tay trong `~/.claude/skills/` hoặc tải lên claude.ai — hãy xoá bản cũ sau khi cài plugin. Skill tải lên claude.ai được đồng bộ về app desktop, nên phải xoá trong phần **Skills** ở Settings của claude.ai.
>
> Nếu đã cài bộ gốc tiếng Anh (plugin `mattpocock-skills` hoặc `startup-skill`), nên gỡ hoặc tắt để Claude không phải chọn giữa hai bản cùng chức năng.

### Cách B — Chép tay vào thư mục skills

Dùng khi muốn sửa thử skill ngay trên máy.

```bash
git clone https://github.com/tannguyenho/builder-skills.git
```

Rồi chép thư mục skill cần dùng vào một trong hai nơi:

- `~/.claude/skills/<tên-skill>/` — dùng cho mọi dự án (Windows: `C:\Users\<bạn>\.claude\skills\`).
- `<dự án>/.claude/skills/<tên-skill>/` — chỉ dùng trong dự án đó, commit cùng dự án để cả team có.

Cách này không tự cập nhật: muốn bản mới thì `git pull` rồi chép lại.

### Cách C — claude.ai (web / app chat)

claude.ai nhận skill dạng file `.skill` (zip của thư mục skill). Đóng gói:

```bash
python scripts/package_skill.py
```

Lệnh trên đóng gói mọi skill vào `dist/<tên-skill>.skill`; muốn một skill thì thêm tên, vd `python scripts/package_skill.py ds-page-manager`. Tải file lên trong phần **Skills** ở Settings của claude.ai.

> Lưu ý: `init-figma-design` cần trình duyệt để tạo Team/Folder trên Figma, nên chạy tốt nhất ở **tab Code của app Claude desktop**. Trên claude.ai chỉ dùng được phần ghi link có sẵn vào `ARCHITECTURE.md`. Ba skill `*-page-manager` chạy được ở mọi nơi có kết nối Figma.
>
> Nhóm **Doc**, **Coding** và `setup-agent`, `wayfinder`, `retro`, `wizard` cần đọc/ghi file, chạy git và CLI (`gh`, `glab`) trong repo, nên dùng trong **Claude Code** (terminal hoặc tab Code). Trên claude.ai dùng tốt `grill-me`, `product-design`, `product-competitors`, `writing-for-agents`.

---

## 2. Hướng dẫn dùng theo nhóm

### 2.1 ⚙️ Setup

#### `setup-agent` — cấu hình repo cho agent

Chạy **một lần cho mỗi repo** trước khi dùng nhóm Doc và Coding. Gõ `/builder-skills:setup-agent` trong thư mục repo. Skill sẽ hỏi rồi ghi:

- **Issue tracker**: GitHub Issues, GitLab Issues, hay file markdown ngay trong repo (`.scratch/<feature>/`). Dùng GitHub/GitLab thì cần CLI `gh`/`glab` đã đăng nhập và repo đã có remote.
- **Label triage**: ánh xạ 4 vai trò `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human` sang label thật trong repo của bạn.
- **Bố cục domain doc**: mặc định một `GLOSSARY.md` + `docs/adr/` ở gốc repo; monorepo thì có thể mỗi context một `GLOSSARY.md`.

Kết quả: khối `## Agent skills` trong `CLAUDE.md`/`AGENTS.md` và các file `docs/agents/*.md`. Các skill khác đọc khối này để biết đăng spec/ticket ở đâu. Chạy lại bất kỳ lúc nào để sửa.


#### `init-figma-design` — dựng kiến trúc Figma

**Skill làm gì**

Tạo "khung nhà" Figma cho một app và ghi toàn bộ link vào file `ARCHITECTURE.md` ở gốc dự án, để designer, dev và AI agent đều biết design nằm ở đâu:

```
Figma
├── Team "0. Design system"            ← dùng chung cho mọi app
│   └── Folder "[Design System] <App>"
│       └── File "[Design System] Version 0.0.0"
└── Team "<N>. <App>"                  ← mỗi app một team
    ├── Folder "[Library] Snowflake"   → ❄️ [Snowflake] <App>
    ├── Folder "[Concept] Sandbox"     → 🖼️ [Concept] <App>
    └── Folder "[Handoff] App"         → ✅ [Handoff] <App>
```

**Cần chuẩn bị**

| Thứ cần có | Vì sao | Cách có |
| --- | --- | --- |
| App **Claude desktop → tab Code** (hoặc extension **Claude in Chrome**) | Figma chỉ cho tạo Team/Folder qua giao diện web | Tải app Claude desktop; Browser pane có sẵn (bật/tắt bằng Ctrl+Shift+B) |
| **Figma MCP** đã kết nối | Đọc danh sách team, tạo file nhanh | App desktop: Settings → Connectors → Figma. CLI: `/mcp` |
| Tài khoản Figma có gói **Education** | Gói Starter chỉ cho **1 folder mỗi team**, không đủ cho cấu trúc trên | Xác minh Education trên Figma, hoặc dùng gói trả phí |
| Đăng nhập Figma trong Browser pane **cùng tài khoản** với Figma MCP | File/folder tạo bằng tài khoản khác thì MCP không ghi được | Tự đăng nhập trong Browser pane khi skill nhắc |

Nếu bạn **đã có sẵn** đủ team/folder/file và chỉ cần ghi link thì không cần trình duyệt hay MCP.

**Chạy**

1. Mở dự án của app trong Claude (thư mục sẽ chứa `ARCHITECTURE.md`).
2. Gõ: `init design cho app <Tên app>` (hoặc gọi thẳng `/builder-skills:init-figma-design` nếu cài bằng plugin, `/init-figma-design` nếu chép tay).
3. Skill sẽ:
   1. **Kiểm tra môi trường** và báo bảng ✅/❌ (trình duyệt, Figma MCP, đúng tài khoản).
   2. **Hỏi bạn đã có sẵn team/folder/file chưa**: tạo mới hết, đã có đủ (chỉ dán link), hoặc có một phần.
   3. **Gửi bản xác nhận** những gì sẽ tạo mới / dùng lại. Chưa đồng ý thì không tạo gì.
   4. Tạo hoặc bổ sung `ARCHITECTURE.md`, rồi tạo lần lượt Team → Folder → File trên Figma. Mỗi mục tạo xong được ghi link ngay.
   5. Kiểm tra lại và báo cáo kèm link.

**Những bước bạn phải tự làm**

- **Đăng nhập Figma** trong Browser pane. Claude không gõ mật khẩu thay bạn.
- **Tích ô đồng ý điều khoản** ở trang chọn gói Education của mỗi team mới. Claude dừng ở trang đó, chờ bạn tích rồi mới bấm "Complete upgrade".

**Bị ngắt giữa chừng?**

Cứ chạy lại skill. Mục nào trong `ARCHITECTURE.md` còn ghi `Link figma điền tại đây` là mục chưa làm; skill chỉ làm tiếp những mục đó và không tạo trùng.

**Kết quả mẫu**

```markdown
<!-- Design Figma Architecture Start -->
## 🎨 Design Figma Architecture

### Team

| Team | Link |
| --- | --- |
| 0. Design system | https://www.figma.com/files/team/<teamId> |
| 1. My App | https://www.figma.com/files/team/<teamId> |

### My App

#### Bảng Folder My App
...
#### Bảng File My App
...
<!-- Design Figma Architecture End -->
```

### 2.2 🚀 Start product

#### `product-design` — thiết kế và thẩm định ý tưởng sản phẩm

Nói tự nhiên, ví dụ *"mình có ý tưởng app đặt lịch cắt tóc, có đáng làm không?"*, *"làm lean canvas cho ý tưởng này"*, *"ước tính TAM/SAM/SOM"*. Skill đi qua các giai đoạn và ghi kết quả thành file trong một thư mục dự án:

```
KIỂM TRA TRƯỚC → PHỎNG VẤN ĐẦU VÀO → BRAINSTORM → NGHIÊN CỨU → [cổng Go/No-Go] → PHỎNG VẤN KHÁCH HÀNG
   → CHIẾN LƯỢC → THƯƠNG HIỆU → SẢN PHẨM → TÀI CHÍNH → KIỂM CHỨNG
```

- **Hai chế độ**: *đầy đủ* (mặc định) hoặc *nhanh* (nói "thẩm định nhanh"): ít bước hơn nhưng vẫn ra tín hiệu go/no-go có bằng chứng.
- **Nghiên cứu cần WebSearch.** Không có web thì skill chuyển sang chế độ dựa trên kiến thức có sẵn và gắn nhãn rõ "không phải dữ liệu live", hạ mức tin cậy.
- **Trung thực thẳng thắn**: mọi số liệu được gắn nhãn dữ liệu thật / ước tính / giả định; có bước xác minh lại nghiên cứu và chỉ ra anti-pattern (giải pháp đi tìm vấn đề, scale sớm…).
- **Kết quả cuối**: bảng tổng kết trong chat, `README.md` tóm tắt cho dự án và `action-plan-30-days.md` (kế hoạch 4 tuần cụ thể).
- **Bị ngắt giữa chừng?** Tiến độ lưu trong `PROGRESS.md`; gọi lại skill để làm tiếp từ giai đoạn chưa xong.

#### `product-competitors` — phân tích đối thủ

Nói *"đối thủ của mình là ai"*, *"so sánh giá các tool quản lý spa"*, *"làm battle card với X"*. Chạy độc lập, không cần `product-design` trước (có thì dùng lại kết quả). Skill nghiên cứu theo 3 đợt (hồ sơ & giá → cảm nhận khách hàng trên review/diễn đàn → GTM & tín hiệu tăng trưởng), rồi ra: bảng giá, ma trận tính năng, battle card cho từng đối thủ, bản đồ điểm yếu chiến lược. Độ sâu có 3 mức: nói "nhanh"/"sơ bộ" hoặc "kỹ"/"chuyên sâu".

#### `wayfinder` — tìm đường cho khối việc lớn

Dùng khi việc quá lớn để một phiên agent ôm hết (vd "chuyển cả app sang kiến trúc mới"). Gõ `/builder-skills:wayfinder`. Skill tạo một **bản đồ** (issue cha) trên issue tracker, chia thành các ticket quyết định thuộc 4 loại: nghiên cứu, prototype, chất vấn (grilling, dùng `grill-with-docs`), và việc cụ thể. Sau đó giải từng ticket theo thứ tự cho đến khi đường tới **đích đến** (một spec, một quyết định hay một thay đổi) rõ ràng. Cần chạy `setup-agent` trước.

### 2.3 🎨 Figma — ba skill `*-page-manager`

Ba skill cùng một cách làm, mỗi skill áp chuẩn cho một loại file:

| Skill | Áp cho file | Cấu trúc page chuẩn |
| --- | --- | --- |
| `ds-page-manager` | `[Design System] Version x.y.z` | `🖼️ Cover` → các nhóm Category viết HOA kèm emoji (`🎨 FOUNDATION`, `⚡ ACTIONS`, `✏️ DATA ENTRY`, `📊 DATA DISPLAY`, `🧩 PATTERNS`, `📐 TEMPLATES`), mỗi component một sub-page `→ Tên` |
| `snowflake-page-manager` | `❄️ [Snowflake] <App>` | `🖼️ COVER` → `📦 BASE` → `🍀 COMPONENT` (A–Z) → `🖥️ SCREEN`, mỗi mục một sub-page `→ Tên` |
| `handoff-page-manager` | `✅ [Handoff] <App>` | `📋 CHANGE LOG` → `🦶 USER FLOW` → `📐 UI GUIDELINE` → `🚧 DESIGN QA` → `🖼️ COVER` (cover nằm **cuối**) |

Quy ước chung của cả ba:

- Sub-page bắt đầu bằng `→ ` (mũi tên thật, không phải `->`).
- Page tên `---` để trống, làm vạch ngăn giữa các nhóm.
- Emoji chỉ dùng ở tên page nhóm, **không** dùng trong tên component.

#### Cần chuẩn bị

- **Figma MCP** đã kết nối, bằng tài khoản có quyền sửa file (ghế Full). App desktop: Settings → Connectors → Figma.
- Link file Figma cần sắp xếp. Nếu dự án đã chạy `init-figma-design`, link nằm sẵn trong `ARCHITECTURE.md`.

#### Chạy

Mở dự án trong Claude rồi nói, kèm link file nếu có, ví dụ:

- `Sắp xếp page cho file DS <link>`
- `Kiểm tra cấu trúc page file Snowflake của app này đúng chuẩn chưa`
- `Tạo các page còn thiếu cho file handoff <link>`

Hoặc gọi thẳng `/builder-skills:ds-page-manager`, `/builder-skills:snowflake-page-manager`, `/builder-skills:handoff-page-manager`.

#### Skill sẽ và không làm gì

- **Có:** tạo page còn thiếu, đổi tên page, sắp xếp lại thứ tự page theo chuẩn.
- **Không:** di chuyển, cắt/dán hay đổi chỗ bất kỳ component, frame, instance nào. Nội dung trong mỗi page giữ nguyên. Tên `→ …` trong chuẩn chỉ là tên gợi ý cho page, không phải lệnh chuyển component sang đó.

### 2.4 📝 Doc

Nhóm này biến ý tưởng mơ hồ thành tài liệu đủ rõ để giao cho người hoặc agent làm.

1. **Chốt ý tưởng**: nói *"grill me về kế hoạch này"* để chạy `grill-me`. Claude hỏi theo từng **vòng**, đánh số câu hỏi, kèm đáp án đề xuất (trả lời "yes" là chấp nhận đề xuất). Claude tự tra sự thật trong code/tài liệu; bạn chỉ quyết định. Muốn ghi luôn thuật ngữ và quyết định quan trọng thì dùng `grill-with-docs`: nó cập nhật `GLOSSARY.md` và viết ADR ngay khi một điều được chốt.
2. **Viết spec**: khi đã bàn đủ, gõ `/builder-skills:to-spec`. Skill không hỏi thêm, chỉ tổng hợp cuộc trò chuyện thành spec và đăng lên issue tracker.
3. **Chia ticket**: `/builder-skills:to-tickets` chia spec thành các lát dọc (mỗi lát chạy được từ đầu đến cuối, nhỏ nhất có thể), ghi rõ ticket nào chặn ticket nào.
4. **Issue từ bên ngoài**: `/builder-skills:triage` đưa issue/PR mới qua các trạng thái `needs-triage` → `needs-info` / `ready-for-agent` / `ready-for-human`, viết **Agent Brief** cho việc giao được cho agent, và ghi lại lý do khi từ chối một đề xuất.

`to-spec`, `to-tickets`, `triage` cần chạy `setup-agent` trước.

### 2.5 💻 Coding

- **Một ticket**: `/builder-skills:implement <ticket hoặc mô tả>`. Claude làm theo TDD (viết test fail trước, rồi code vừa đủ cho pass), chạy typecheck và test, gọi `code-review`, rồi commit vào nhánh hiện tại.
- **Cả một spec**: `/builder-skills:implement-spec <spec>`. Claude điều phối: mỗi ticket một subagent trong worktree riêng, chạy song song theo đồ thị chặn giữa các ticket, gộp về một **nhánh tích hợp**, review và sửa lần cuối. Hợp với spec đã có ticket từ `to-tickets`.
- **Review**: nói *"review thay đổi từ main"* hoặc *"review nhánh này"*. `code-review` chạy hai subagent song song: một bên so với chuẩn code của repo (`CODING_STANDARDS.md`, `CONTRIBUTING.md`…), một bên so với issue/spec gốc, rồi báo cáo cạnh nhau.
- **Mô tả PR**: nói *"viết mô tả PR"*; `pr` soạn phần tóm tắt, bằng chứng đã chạy, rủi ro khi merge và phạm vi ảnh hưởng.
- **Kiến trúc**: `/builder-skills:improve-codebase-architecture` quét repo, xuất báo cáo HTML liệt kê các chỗ nên gom/làm sâu module kèm mức khuyến nghị; chọn một chỗ để Claude cùng bạn đào sâu. `codebase-design` là bộ từ vựng chung (module, interface, seam, adapter…) mà các skill khác dùng; nó tự bật khi bạn bàn về thiết kế interface.

> Plugin này và Claude Code đều có lệnh `/code-review`. Muốn chắc chắn gọi bản của bộ này thì gõ `/builder-skills:code-review`.

### 2.6 🤖 Agent

- **Sau một phiên code**: `/builder-skills:retro` đọc lại phiên (mặc định là phiên hiện tại) và đề xuất, theo thứ tự nghiêm trọng, cách cải thiện môi trường cho agent: thêm con trỏ điều hướng, thêm lint/test/hook tự động, bổ sung chuẩn code cho bước review, rút gọn `CLAUDE.md`, giảm tool tốn token…
- **Việc chỉ người làm được** (tạo API key, thêm CI secret, bấm qua dashboard bên thứ ba, migration một lần): nói *"tạo wizard hướng dẫn mình setup Stripe"*. `wizard` sinh một script bash tương tác, dẫn từng bước, mở sẵn link, hỏi và ghi giá trị vào `.env`/secret.
- **Viết skill hoặc `CLAUDE.md`**: `writing-for-agents` tự bật khi bạn tạo/sửa skill hay `CLAUDE.md`/`AGENTS.md`, giúp tài liệu gọn, đúng chỗ và agent làm theo được.

---

## 3. Build skill mới trong repo này

### Cấu trúc repo

```
builder-skills/
├── .claude-plugin/
│   ├── marketplace.json     ← khai báo marketplace "tannguyenho"
│   └── plugin.json          ← plugin "builder-skills", nạp mọi skill trong skills/
├── skills/
│   └── <tên-skill>/
│       ├── SKILL.md         ← bắt buộc
│       ├── assets/          ← mẫu, template mà skill dùng (tuỳ chọn)
│       ├── references/      ← tài liệu dài, chỉ đọc khi cần (tuỳ chọn)
│       └── scripts/         ← script skill gọi tới (tuỳ chọn)
└── scripts/package_skill.py ← đóng gói .skill cho claude.ai
```

Plugin tự nạp mọi thư mục trong `skills/`, nên thêm skill mới **không cần sửa** `plugin.json`.

### Quy trình

1. **Tạo thư mục** `skills/<tên-skill>/`. Tên viết thường, nối bằng gạch ngang, **không** thêm tiền tố `uxf-` (vd `handoff-page-manager`). Khi cài bằng plugin, Claude tự gắn tiền tố `builder-skills:` nên không cần thêm gì để phân biệt.
2. **Viết `SKILL.md`**. Cách nhanh nhất: mở Claude trong repo này và nói *"tạo skill mới tên … để …"*. Claude sẽ dùng skill `skill-creator` để soạn, chạy thử và chỉnh. Khung tối thiểu:

   ```markdown
   ---
   name: ten-skill
   description: >-
     Skill làm gì + KHI NÀO dùng. Liệt kê các câu user hay nói để kích hoạt
     ("…", "…"), kể cả khi user không nhắc tên skill.
   ---

   # Tiêu đề

   Mục tiêu, các bước, nguyên tắc an toàn…
   ```

   - `name` phải trùng tên thư mục.
   - `description` quyết định Claude có tự gọi skill hay không: ghi rõ *làm gì* và *khi nào dùng*.
   - Giữ `SKILL.md` gọn (dưới ~500 dòng). Phần dài đưa vào `references/` và ghi trong `SKILL.md` khi nào cần đọc.
   - Giải thích *vì sao* cho mỗi quy tắc quan trọng, để Claude xử lý được cả trường hợp skill không nói tới.
3. **Chạy thử trên máy** trước khi push. Mở Claude với plugin lấy thẳng từ thư mục repo:

   ```bash
   claude --plugin-dir .
   ```

   Rồi gõ đúng câu mà user thật sẽ nói, xem skill có được gọi và làm đúng không.
4. **Kiểm tra định dạng / đóng gói**:

   ```bash
   python scripts/package_skill.py <tên-skill>
   ```

   Script báo lỗi nếu thiếu frontmatter hoặc `name` không khớp tên thư mục.
5. **Cập nhật README**: thêm một dòng vào bảng skill ở đầu file, và một mục hướng dẫn dùng nếu skill cần chuẩn bị gì.
6. **Tăng `version`** trong `.claude-plugin/plugin.json` (vd `0.1.0` → `0.2.0` khi thêm skill, `0.1.1` khi sửa nhỏ), rồi commit và push. Mọi người lấy bản mới bằng `claude plugin marketplace update tannguyenho` rồi `claude plugin update builder-skills@tannguyenho`.

### Lưu ý khi viết skill

- Repo này **public**: không đưa vào skill token, mật khẩu, email, link Figma/Drive nội bộ của khách hàng.
- Thao tác thật trên dịch vụ ngoài (tạo team, gửi tin, xoá file…) phải có bước **xin xác nhận user** trước khi làm.
- Những việc Claude không được làm thay (đăng nhập, đồng ý điều khoản, thanh toán) phải ghi rõ là user tự làm.

---

## 4. Nguồn & giấy phép

Các skill sau được dịch sang tiếng Việt và chỉnh cho bộ này (đổi tên, gộp skill phụ thuộc để mỗi skill tự chạy được), từ hai dự án giấy phép MIT:

| Dự án gốc | Skill trong bộ này |
| --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `setup-agent` (gốc `setup-matt-pocock-skills`), `wayfinder`, `grill-me` (gộp `grilling`), `grill-with-docs` (gộp `grilling` + `domain-modeling`), `to-spec`, `to-tickets`, `triage`, `implement`, `implement-spec` (kèm `tdd`), `code-review`, `codebase-design`, `improve-codebase-architecture`, `pr`, `retro`, `wizard`, `writing-for-agents` |
| [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) | `product-design` (gốc `startup-design`), `product-competitors` (gốc `startup-competitors`) |

Thông báo bản quyền gốc nằm trong [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Khi bản gốc cập nhật, dịch lại phần thay đổi rồi tăng `version` như mọi lần sửa skill.
