# Issue tracker: GitHub

Issue và spec của repo này nằm trên GitHub Issues. Dùng CLI `gh` cho mọi thao tác.

## Quy ước

- **Tạo issue**: `gh issue create --title "..." --body "..."`. Dùng heredoc cho phần thân nhiều dòng.
- **Đọc issue**: `gh issue view <number> --json number,title,body,labels,comments`.
- **Liệt kê issue**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` kèm bộ lọc `--label` và `--state` phù hợp.
- **Biến issue thành sub-issue của một issue cha**: `gh issue create --parent <parent> ...`, hoặc sau đó chạy `gh issue edit <parent> --add-sub-issue <child>` (`gh` 2.94+). Với `gh` cũ hơn: `gh api --method POST repos/<owner>/<repo>/issues/<parent>/sub_issues -F sub_issue_id=<child-db-id>` (database id, giống mục **Chặn** bên dưới). Nếu không có sub-issue, ghi `Part of #<parent>` ở đầu phần thân của issue con.
- **Chặn (blocking)**: dùng **quan hệ phụ thuộc issue gốc** (**native issue dependencies**) của GitHub, cách biểu diễn chuẩn và hiển thị được trên UI. Thêm cạnh chặn bằng `gh issue create --blocked-by <n>,<n> ...` hoặc `gh issue edit <child> --add-blocked-by <blocker>` (`gh` 2.94+). Với `gh` cũ hơn: `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`, trong đó `<blocker-db-id>` là **database id** dạng số của issue chặn (`gh api repos/<owner>/<repo>/issues/<n> --jq .id`, _không phải_ `#number` hay `node_id`). Nơi không có tính năng phụ thuộc, dùng phương án dự phòng là một dòng `Blocked by: #<n>, #<n>` ở đầu phần thân issue con. Ticket được gỡ chặn khi mọi issue chặn nó đều đã đóng.
- **Đếm số issue chặn còn mở**: `gh api repos/<owner>/<repo>/issues/<n> --jq .issue_dependencies_summary.blocked_by` (chỉ tính issue chặn còn mở; 0 nghĩa là bắt đầu được). `gh issue view <n> --json blockedBy` liệt kê cả issue chặn đã đóng, nên phải lọc: `--jq '[.blockedBy.nodes[] | select(.state == "OPEN")] | length'`.
- **Bình luận vào issue**: `gh issue comment <number> --body "..."`
- **Gắn / gỡ label**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Đóng**: đăng lời giải thích bằng `gh issue comment <number> --body "..."`, rồi `gh issue close <number>`. Với issue đã đóng sẵn, `gh issue close --comment` sẽ bỏ mất bình luận mà vẫn thoát với mã 0.

Suy ra repo từ `git remote -v`; `gh` tự làm việc này khi chạy bên trong một bản clone.

Chỉ tạo issue vào repo của chính user. Không bao giờ tạo issue vào repo phát hành bộ skill này (`tannguyenho/builder-skills`, hay repo gốc `mattpocock/skills`) trừ khi user là chủ repo đó. Trong một bản fork, `gh` có thể mặc định trỏ về repo cha upstream, nên trước lần `gh issue create` đầu tiên của phiên, kiểm tra repo đích bằng `gh repo view --json nameWithOwner` và xác nhận với user nếu đó không phải repo của họ.

## Pull request là một kênh triage

**PR là kênh nhận yêu cầu (PRs as a request surface): no.** _(Đặt thành `yes` nếu repo này coi PR từ bên ngoài là yêu cầu tính năng; `/triage` đọc cờ này.)_

Khi đặt thành `yes`, PR đi qua cùng bộ label và trạng thái như issue, dùng các lệnh `gh pr` tương ứng:

- **Đọc PR**: `gh pr view <number>`, rồi `gh pr view <number> --comments` (khi không chạy trong TTY, `--comments` chỉ in bình luận, không in phần thân), và `gh pr diff <number>` để xem diff.
- **Liệt kê PR bên ngoài cần triage**: `gh api --paginate 'repos/{owner}/{repo}/pulls?state=open' --jq '.[] | select(.author_association | IN("OWNER","MEMBER","COLLABORATOR") | not) | {number, title, author: .user.login, author_association, labels: [.labels[].name]}'`.
- **Bình luận / gắn label / đóng**: `gh pr comment`, `gh pr edit --add-label`/`--remove-label`, `gh pr close`.

GitHub dùng chung một dải số cho cả issue và PR, nên một `#42` trơn có thể là một trong hai: xác định bằng `gh pr view 42`, không được thì chuyển sang `gh issue view 42`.

## Khi một skill bảo "đăng lên issue tracker"

Tạo một GitHub issue.

## Khi một skill bảo "lấy ticket liên quan"

Đọc như mục **Đọc issue** ở trên.

## Thao tác wayfinding

Dùng bởi `/wayfinder`. **Bản đồ** (**map**) là một issue duy nhất, với các issue **con** (**child**) làm ticket.

- **Map**: một issue duy nhất gắn label `wayfinder:map`, phần thân gồm Đích đến / Ghi chú / Các quyết định đã chốt / Chưa xác định rõ. `gh issue create --label wayfinder:map`.
- **Ticket con**: một issue được nối với map dưới dạng GitHub sub-issue (xem **Biến issue thành sub-issue của một issue cha**). Nơi chưa bật sub-issue, thêm ticket con vào một task list trong phần thân map và ghi `Part of #<map>` ở đầu phần thân ticket con. Label: `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Khi đã được nhận, ticket được assign cho dev đang dẫn dắt.
- **Chặn**: xem mục **Chặn** trong phần Quy ước.
- **Truy vấn frontier**: liệt kê các issue con còn mở của map (`gh issue list --state open`, giới hạn trong sub-issue / task list của map), loại những issue còn bị chặn bởi issue đang mở (xem **Đếm số issue chặn còn mở**, hoặc có issue đang mở trong dòng `Blocked by`) hoặc đã có người được assign; issue đứng đầu theo thứ tự trong map được chọn.
- **Nhận (claim)**: `gh issue edit <n> --add-assignee @me`, là thao tác ghi đầu tiên của phiên.
- **Giải quyết (resolve)**: `gh issue comment <n> --body "<answer>"`, rồi `gh issue close <n>`, rồi nối một con trỏ ngữ cảnh (ý chính + link) vào mục **Các quyết định đã chốt** của map.
