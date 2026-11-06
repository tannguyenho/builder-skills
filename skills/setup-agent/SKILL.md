---
name: setup-agent
description: >-
  Cấu hình repo cho bộ skill engineering: chọn issue tracker (GitHub, GitLab,
  markdown cục bộ hoặc công cụ khác), bộ label triage, và cách bố trí tài liệu
  domain (GLOSSARY.md, ADR). Ghi kết quả vào docs/agents/ và khối "## Agent
  skills" trong CLAUDE.md/AGENTS.md. Chạy một lần trước khi dùng các skill
  engineering khác như to-spec, to-tickets, triage, wayfinder. Dùng khi user nói
  "setup agent", "cấu hình repo cho agent", "thiết lập issue tracker cho skill",
  "chạy /setup-agent", "set up the engineering skills", "configure issue
  tracker for agents".
disable-model-invocation: true
---

# Setup Agent

Dựng phần cấu hình theo từng repo mà các skill engineering mặc định là đã có:

- **Issue tracker**: issue nằm ở đâu (mặc định là GitHub; markdown cục bộ cũng được hỗ trợ sẵn)
- **Label triage**: chuỗi label dùng cho năm vai trò triage chuẩn
- **Tài liệu domain**: `GLOSSARY.md` và ADR nằm ở đâu, cùng các quy tắc đọc chúng dành cho skill sử dụng

Đây là skill dẫn dắt bằng prompt, không phải một script chạy cố định. Hãy khảo sát, trình bày những gì tìm thấy, xác nhận với user, rồi mới ghi file.

## Quy trình

### 1. Khảo sát

Xem repo hiện tại để nắm trạng thái ban đầu. Đọc những gì đang có; đừng giả định:

- `git remote -v` và `.git/config`: đây có phải repo GitHub không? Repo nào?
- `AGENTS.md` và `CLAUDE.md` ở gốc repo: có file nào tồn tại không? Đã có mục `## Agent skills` trong file nào chưa?
- `GLOSSARY.md` và `GLOSSARY-MAP.md` ở gốc repo, cùng các file kiểu cũ `CONTEXT.md` / `CONTEXT-MAP.md`. Nếu có file kiểu cũ, đề nghị `git mv` sang tên `GLOSSARY` tương ứng và sửa lại các tên đó trong `docs/agents/domain.md`.
- `docs/adr/` và mọi thư mục `src/*/docs/adr/`
- `docs/agents/`: kết quả từ lần chạy trước của skill này đã tồn tại chưa?
- `.scratch/`: dấu hiệu repo đang dùng quy ước issue tracker bằng markdown cục bộ
- Skill `triage` đã được cài chưa? (có thư mục skill `triage` nằm cạnh skill này, hoặc `triage` có trong danh sách skill khả dụng của bạn.) Điều này quyết định Mục B có chạy hay không.
- Dấu hiệu monorepo: có `pnpm-workspace.yaml`, trường `workspaces` trong `package.json`, hoặc `packages/*` có nội dung và mỗi package có `src/` riêng. Những dấu hiệu này chỉ xuất hiện ở repo thật sự lớn, nhiều package; không có chúng nghĩa là repo một context (**single-context**), tức gần như mọi repo.

### 2. Trình bày kết quả và hỏi

Tóm tắt những gì đã có và những gì còn thiếu. Sau đó đi lần lượt từng mục. Mỗi mục một câu trả lời, xong rồi mới sang mục tiếp.

Mở đầu mỗi mục bằng phương án được khuyến nghị để user có thể đồng ý chỉ bằng một từ. Chỉ thêm một dòng giải thích khi lựa chọn thật sự rẽ nhánh; bỏ hẳn mục nào mà bước khảo sát đã trả lời rồi (Mục B khi `triage` chưa được cài, Mục C khi không phải monorepo).

**Mục A: Issue tracker.**

> Giải thích: "Issue tracker" là nơi chứa issue của repo này. Các skill như `to-tickets`, `triage` và `to-spec` đọc và ghi vào đó. Chúng cần biết nên gọi `gh issue create`, ghi một file markdown trong `.scratch/`, hay làm theo một quy trình khác do bạn mô tả. Hãy chọn đúng nơi bạn thực sự theo dõi công việc của repo này.

Lập trường mặc định: bộ skill này được thiết kế cho GitHub. Nếu có `git remote` trỏ tới GitHub, đề xuất GitHub. Nếu `git remote` trỏ tới GitLab (`gitlab.com` hoặc host tự dựng), đề xuất GitLab. Nếu không (hoặc nếu user muốn khác), đưa ra các lựa chọn:

- **GitHub**: issue nằm trong GitHub Issues của repo (dùng CLI `gh`)
- **GitLab**: issue nằm trong GitLab Issues của repo (dùng CLI [`glab`](https://gitlab.com/gitlab-org/cli))
- **Markdown cục bộ**: issue là các file trong `.scratch/<feature>/` ngay trong repo (hợp với dự án làm một mình hoặc repo không có remote)
- **Khác** (Jira, Linear, v.v.): nhờ user mô tả quy trình trong một đoạn văn; skill sẽ ghi lại nguyên văn dạng văn xuôi tự do

Ghi lựa chọn vào `docs/agents/issue-tracker.md`. Template GitHub và GitLab có một cờ "PR là kênh nhận yêu cầu" (**PRs as a request surface**), mặc định **tắt**. Cứ để tắt và đừng nhắc tới: user nào muốn đưa PR từ bên ngoài vào hàng đợi triage có thể tự bật cờ này trong file sau.

Tracker GitHub hoặc GitLab cần một repo truy cập được. Khi user chọn một trong hai mà chưa có `git remote` nào trỏ tới host đó, hỏi user URL repo rồi nối vào (`git init` nếu cần, `git remote add origin <url>`) trước khi đi tiếp. Coi là xong khi `gh repo view` / `glab repo view` in ra được project từ bên trong thư mục này; nếu không được, dừng lại và nói cho user biết còn thiếu gì.

**Mục B: Bộ label triage.** Bỏ qua hẳn mục này nếu skill `triage` chưa được cài (bước khảo sát đã cho biết), vì skill chưa cài thì không cần label.

Nếu đã cài, hỏi đúng một câu:

> Bạn có muốn giữ bộ label triage mặc định không? (khuyến nghị: **có**)

Mặc định là năm vai trò chuẩn, chuỗi label của mỗi vai trò trùng với tên của nó: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Nếu trả lời **có**, ghi nguyên như vậy. Chỉ khi user nói không, thường vì tracker của họ đã dùng tên khác (vd `bug:triage` thay cho `needs-triage`), mới thu thập các tên thay thế để `triage` dùng label đang có thay vì tạo label trùng.

**Mục C: Tài liệu domain.** Mặc định là **single-context** (một `GLOSSARY.md` + `docs/adr/` ở gốc repo). Cách này hợp với gần như mọi repo; cứ ghi mà không cần hỏi.

Chỉ đề xuất **multi-context** (một `GLOSSARY-MAP.md` ở gốc trỏ tới các file `GLOSSARY.md` riêng cho từng context) khi bước khảo sát tìm thấy dấu hiệu monorepo. Khi đó xác nhận với user họ muốn bố cục nào.

### 3. Xác nhận và chỉnh sửa

Cho user xem bản nháp của:

- Khối `## Agent skills` sẽ thêm vào file `CLAUDE.md` / `AGENTS.md` được chọn để sửa (xem quy tắc chọn ở bước 4)
- Nội dung `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, và `docs/agents/triage-labels.md` (file cuối chỉ khi `triage` đã được cài)

Để user chỉnh sửa trước khi ghi.

### 4. Ghi file

**Chọn file để sửa:**

- Nếu có `CLAUDE.md`, sửa file đó.
- Nếu không mà có `AGENTS.md`, sửa file đó.
- Nếu không có file nào, hỏi user muốn tạo file nào; đừng tự chọn thay họ.

Không bao giờ tạo `AGENTS.md` khi đã có `CLAUDE.md` (hoặc ngược lại); luôn sửa file đang có sẵn.

Nếu file được chọn đã có khối `## Agent skills`, cập nhật nội dung ngay tại chỗ thay vì nối thêm một khối trùng. Đừng ghi đè những chỉnh sửa của user ở các mục xung quanh.

Khối cần ghi:

```markdown
## Agent skills

### Issue tracker

[tóm tắt một dòng nơi theo dõi issue]. Xem `docs/agents/issue-tracker.md`.

### Triage labels

[tóm tắt một dòng về bộ label]. Xem `docs/agents/triage-labels.md`.

### Domain docs

[tóm tắt một dòng về bố cục: "single-context" hoặc "multi-context"]. Xem `docs/agents/domain.md`.
```

Chỉ thêm khối con `### Triage labels`, và chỉ ghi `docs/agents/triage-labels.md`, khi `triage` đã được cài và Mục B đã chạy. Nếu không, bỏ cả hai.

Khi Mục B đã chạy trên GitHub hoặc GitLab, tạo mọi label đã cấu hình mà tracker còn thiếu (`gh label create` / `glab label create`).

Sau đó ghi các file tài liệu, lấy các template mẫu trong thư mục skill này làm điểm xuất phát:

- [issue-tracker-github.md](./issue-tracker-github.md): issue tracker GitHub
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md): issue tracker GitLab
- [issue-tracker-local.md](./issue-tracker-local.md): issue tracker bằng markdown cục bộ
- [triage-labels.md](./triage-labels.md): bảng ánh xạ label (chỉ khi `triage` đã được cài)
- [domain.md](./domain.md): quy tắc đọc tài liệu domain + bố cục

Với issue tracker "khác", tự viết `docs/agents/issue-tracker.md` từ đầu dựa trên mô tả của user.

### 5. Hoàn tất

Báo user rằng việc thiết lập đã xong và những skill engineering nào từ giờ sẽ đọc các file này. Nhắc rằng sau này họ có thể sửa trực tiếp `docs/agents/*.md`; chỉ cần chạy lại `/setup-agent` khi muốn đổi issue tracker hoặc làm lại từ đầu.
