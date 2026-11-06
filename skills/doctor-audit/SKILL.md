---
name: doctor-audit
description: >-
  Khám tổng quát bộ skill builder-skills: (1) đồng bộ các skill dịch với phiên
  bản mới nhất của repo gốc (mattpocock/skills, ferdinandobons/startup-skill) —
  chỉ dịch phần thay đổi và giữ các chỉnh sửa riêng; (2) test: kiểm tra tĩnh bằng
  script và chạy thử khô từng skill bằng subagent; (3) đề xuất lược bớt phần
  thừa và cải thiện cho từng skill, rồi chỉ áp dụng những gì user chọn. Chạy
  trong bản clone của repo builder-skills. Gọi bằng /doctor-audit, có thể kèm
  tên skill hoặc chế độ: "sync", "test", "review".
disable-model-invocation: true
---

# Doctor Audit

Bộ skill này một phần là bản dịch của hai repo gốc vẫn đang được cập nhật. Không có quy trình khám định kỳ thì bản tiếng Việt sẽ lệch dần khỏi bản gốc, và mỗi skill sẽ phình dần những đoạn không còn tác dụng. Skill này làm ba việc theo thứ tự: **đồng bộ → test → đề xuất**, rồi chỉ sửa những gì user đồng ý.

Tài nguyên trong skill:

- [scripts/audit.py](scripts/audit.py): script kiểm tra, chỉ dùng thư viện chuẩn Python. `check` kiểm tra tĩnh; `upstream` so với repo gốc; `mark-synced` ghi commit đã đồng bộ.
- [references/upstream.json](references/upstream.json): **khoá phiên bản**. Ghi mỗi skill dịch từ đường dẫn nào, commit nào của repo gốc, và những chỗ **cố ý khác bản gốc** (`adaptations`) mà khi đồng bộ phải giữ.
- [references/translation-rules.md](references/translation-rules.md): quy tắc dịch và đổi tên. Đọc trước khi dịch bất kỳ thay đổi nào.
- [references/review-criteria.md](references/review-criteria.md): tiêu chí chấm từng skill ở Bước 4.

Mọi lệnh dưới đây chạy từ gốc repo. Dùng `python3` (trên macOS thường không có `python`); máy chỉ có `python` thì thay tương ứng.

## Phạm vi lần chạy

Đọc tham số user gõ kèm lệnh:

- Không tham số: chạy đủ năm bước cho mọi skill.
- Chế độ `sync`, `test`, `review` (ghép được, vd `test review`): chỉ chạy các bước tương ứng (Bước 2, 3, 4). Bước 1 luôn chạy. Bước 4 hoặc 2 có chạy thì Bước 5 chạy sau đó. Ba từ này luôn hiểu là chế độ, không phải tên skill.
- Tên skill (vd `/doctor-audit implement pr`): giới hạn Bước 3–4 vào các skill đó. Bước 2 vẫn so cả repo gốc, vì một thay đổi ở gốc có thể chạm nhiều skill cùng lúc.
- Lần chạy nào cũng kết thúc bằng một báo cáo theo mẫu ở Bước 4. Bước nào không chạy thì ghi "Không chạy" vào mục của bước đó, để người đọc phân biệt "đã kiểm tra, không có gì" với "chưa kiểm tra".

## Bước 1: Kiểm tra điều kiện

1. Xác nhận đang ở gốc repo builder-skills: `.claude-plugin/plugin.json` có `"name": "builder-skills"`. Nếu không phải, dừng lại và bảo user mở Claude trong bản clone của repo. Skill này sửa chính mã nguồn của bộ skill, nên chạy từ bản cài plugin thì không có gì để sửa.
2. `git status --short`: nếu có thay đổi chưa commit, báo user và hỏi có làm tiếp không (nên commit hoặc stash trước). Lý do: các thay đổi của lần khám sẽ trộn lẫn với việc dở dang, rất khó review.
3. Đọc `CLAUDE.md` của repo. Quy ước ở đó (tiếng Việt, không tiền tố `uxf-`, không đưa link nội bộ, chạy `package_skill.py`, tăng version) áp dụng cho mọi thay đổi bên dưới.

## Bước 2: Đồng bộ với repo gốc

1. Clone **đủ lịch sử** của từng repo trong `upstreams` của `upstream.json` vào thư mục tạm, ngoài repo. Dùng `--filter=blob:none`, không dùng `--depth`, vì script cần commit cũ để tính diff:

   ```bash
   git clone --filter=blob:none https://github.com/mattpocock/skills <tmp>/mp
   git clone --filter=blob:none https://github.com/ferdinandobons/startup-skill <tmp>/su
   ```

2. Chạy so sánh:

   ```bash
   python3 skills/doctor-audit/scripts/audit.py upstream --clone mattpocock/skills=<tmp>/mp --clone ferdinandobons/startup-skill=<tmp>/su
   ```

   Kết quả có bốn loại dòng: ✅ không đổi, 🔄 skill có file gốc thay đổi, 🆕 skill gốc mới chưa dịch, ❌ đường dẫn gốc đã mất.

3. Với mỗi skill 🔄:
   1. Đọc diff gốc: `git -C <clone> diff <synced_commit> HEAD -- <paths>`.
   2. Đọc bản tiếng Việt hiện tại và mục `adaptations` của skill đó trong `upstream.json`.
   3. **Dịch đúng phần thay đổi** vào bản tiếng Việt, theo [translation-rules.md](references/translation-rules.md). Đừng dịch lại cả file: dịch lại toàn bộ sẽ xoá mất các chỉnh sửa riêng và làm diff không review được.
   4. Nếu thay đổi gốc đụng vào một `adaptation` (vd gốc sửa đúng đoạn đã gộp, hay thêm lời gọi tới skill không có trong bộ này), dừng lại và hỏi user cách xử lý. Đừng tự chọn.
   5. Skill gộp từ nhiều nguồn (`grill-me`, `grill-with-docs`, `implement`, `implement-spec`): một thay đổi ở `grilling` hay `tdd` phải được đưa vào **mọi** skill chứa nó. `references/tdd.md` của `implement` và `implement-spec` phải giữ giống hệt nhau.

   Có trên 3 skill 🔄 thì giao cho subagent chạy song song, mỗi subagent một nhóm skill. Đưa cho mỗi subagent: đường dẫn clone, commit cũ/mới, danh sách skill, và đường dẫn tới `translation-rules.md` và `upstream.json`. Subagent báo lại các file đã sửa và mọi chỗ phải tự quyết.

4. Với skill 🆕: liệt kê kèm một dòng mô tả lấy từ `description` gốc. Hỏi user muốn dịch skill nào, và skill nào cho vào `ignored_skills`. Skill được chọn thì dịch theo [translation-rules.md](references/translation-rules.md), thêm vào `upstream.json`, README và `THIRD_PARTY_NOTICES.md`.
5. Với dòng ❌: dùng `git -C <clone> log --follow --diff-filter=RD -- <path>` để tìm xem đường dẫn bị đổi tên hay bị xoá, rồi đề xuất cách cập nhật `paths` hoặc gỡ skill. Hỏi user trước khi gỡ.
6. Đồng bộ xong một repo thì ghi commit mới:

   ```bash
   python3 skills/doctor-audit/scripts/audit.py mark-synced <owner/repo> <commit HEAD của clone>
   ```

   Chỉ ghi khi **mọi** skill 🔄 của repo đó đã được xử lý. Ghi sớm thì lần sau script sẽ không còn thấy phần chưa dịch.

## Bước 3: Test

**3a. Kiểm tra tĩnh.** Chạy `python3 skills/doctor-audit/scripts/audit.py check [tên-skill ...]`. Script này đã bao gồm phần kiểm tra của `scripts/package_skill.py`, nên không cần chạy thêm lệnh đó ở đây (lệnh đó còn ghi ra `dist/`). Script kiểm tra:

- frontmatter: `name` trùng tên thư mục, có `description`, `description` không quá 1024 ký tự (cảnh báo khi trên 900);
- link và file được nhắc tới phải tồn tại;
- skill được nhắc tới phải có trong repo;
- skill được skill khác gọi thì không được có `disable-model-invocation`;
- file không ai nhắc tới;
- đoạn văn còn tiếng Anh;
- email, token, link Figma/Drive (repo public);
- skill phải có trong bảng của README;
- file trùng y hệt, hoặc cùng tên mà gần giống nhau, giữa các skill.

Sửa hết lỗi ❌. Không ổn thì báo user, đừng bỏ qua. Cảnh báo ⚠️ thì đưa vào báo cáo ở Bước 4.

**3b. Chạy thử khô (dry-run).** Kiểm tra tĩnh không biết skill có làm được việc hay không. Chọn các skill vừa đồng bộ ở Bước 2, các skill có ⚠️, và các skill user nêu tên. Nếu chạy cho mọi skill, báo trước cho user là sẽ tốn nhiều token.

Với mỗi skill được chọn, giao một subagent mới, kèm:

- đường dẫn tới thư mục skill;
- một yêu cầu thực tế mà user sẽ gõ để gọi skill đó;
- dặn subagent **đi qua từng bước của skill trên giấy**: không sửa repo, không gọi dịch vụ ngoài.

Subagent báo lại theo ba mục:

- (a) bước nào chưa rõ hoặc có hai cách hiểu;
- (b) bước nào cần thông tin hay công cụ mà skill không nói lấy ở đâu;
- (c) chỗ nào phải đoán.

Giao song song, tối đa khoảng 5 subagent một lượt. Không có công cụ subagent (vd trên claude.ai) thì tự đi qua từng skill trên giấy, báo theo đúng ba mục trên. Cách này kém khách quan hơn vì bạn đã đọc skill trước, nên cố đọc như người mới.

## Bước 4: Đề xuất lược bớt và cải thiện

Chấm từng skill theo [review-criteria.md](references/review-criteria.md). Dùng thêm kết quả của Bước 3 và các file trùng mà script đã báo. Nhiều skill thì chia nhóm cho subagent, mỗi subagent đọc đầy đủ skill trong nhóm mình rồi trả về đề xuất theo đúng mẫu bên dưới.

Mỗi đề xuất phải **chỉ ra đúng vị trí** (file và đoạn), nêu **vì sao**, và nêu **được gì** (bớt bao nhiêu dòng, hoặc agent làm đúng hơn ở chỗ nào). Đề xuất chung chung kiểu "nên viết gọn hơn" thì không dùng được. Khi nào xếp vào "Cần user quyết": xem [review-criteria.md](references/review-criteria.md).

Ghi báo cáo vào `docs/audit/<YYYY-MM-DD>.md` (tạo thư mục nếu chưa có; file đã tồn tại thì thêm hậu tố `-2`, `-3`…, đừng ghi đè). Theo mẫu dưới đây; đề xuất đánh số liên tục trong cả báo cáo để user chọn theo số:

```markdown
# Doctor audit — <ngày>

## Tóm tắt
- Đồng bộ: <repo>: <commit cũ> → <commit mới>, <n> skill cập nhật, <n> skill gốc mới
- Kiểm tra tĩnh: <n> lỗi đã sửa, <n> cảnh báo
- Chạy thử khô: <n> skill, <n> chỗ chưa rõ
- Đề xuất: <n> lược bớt, <n> cải thiện, <n> cần user quyết

## Đã đồng bộ
| Skill | File gốc thay đổi | Đã làm |
(hoặc "Không chạy" / "Không có commit mới")

## Kiểm tra tĩnh
<các ❌ đã sửa, các ⚠️ còn lại, file trùng/gần trùng — hoặc "Không chạy">

## Chạy thử khô
### `<tên-skill>` — yêu cầu thử: "<câu user gõ>"
- (a)/(b)/(c) <chỗ chưa rõ>

## Đề xuất theo skill
### `<tên-skill>`
1. ✂️ **Lược bớt** — `<file>` § <đoạn>: <vì sao thừa>. Được gì: bớt ~<n> dòng. [*Khác bản gốc*]
2. 🔧 **Cải thiện** — `<file>` § <đoạn>: <vấn đề> → <đề xuất cụ thể>. Được gì: <…>. [*Khác bản gốc* | *Lỗi có sẵn ở bản gốc*]
3. ❓ **Cần user quyết** — <câu hỏi, kèm các phương án>.

## Không cần làm gì
<các skill ✅>
```

Trình bày báo cáo cho user dạng danh sách đánh số, nhóm theo skill. Hỏi user muốn áp dụng đề xuất nào (vd "áp 1, 3, 5–8", "tất cả trừ 4"). **Chưa được đồng ý thì không sửa skill nào.** Đề xuất là ý kiến của Claude, user mới là người quyết bộ skill của team trông thế nào.

## Bước 5: Áp dụng và hoàn tất

1. Áp dụng các đề xuất user đã chọn. Đề xuất nào chạm vào skill dịch thì xem lại `adaptations`. Nếu thay đổi là cố ý khác bản gốc, ghi thêm một dòng vào `adaptations`, để lần đồng bộ sau không ghi đè mất.
2. Chạy lại `python3 skills/doctor-audit/scripts/audit.py check` và `python3 scripts/package_skill.py`, rồi xoá `dist/`.
3. Cập nhật bảng skill và hướng dẫn trong `README.md` nếu skill đổi chức năng, đổi tên, hoặc có skill mới.
4. Tăng `version` trong `.claude-plugin/plugin.json`: chỉ sửa nhỏ hoặc đồng bộ thì tăng số cuối (`0.6.0` → `0.6.1`); thêm hay bớt skill thì tăng số giữa.
5. Tóm tắt cho user: đã đồng bộ gì, đã sửa gì, còn gì để lại. Hỏi user có muốn commit và push không, và push lên nhánh nào. Báo cáo trong `docs/audit/` commit cùng nếu user muốn giữ lịch sử khám.
