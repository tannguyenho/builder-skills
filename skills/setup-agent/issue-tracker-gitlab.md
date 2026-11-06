# Issue tracker: GitLab

Issue và spec của repo này nằm trên GitLab Issues. Dùng CLI [`glab`](https://gitlab.com/gitlab-org/cli) cho mọi thao tác.

## Quy ước

- **Tạo issue**: `glab issue create --title "..." --description "..."`. Dùng heredoc cho phần mô tả nhiều dòng. Truyền `--description -` để mở trình soạn thảo.
- **Đọc issue**: `glab issue view <number> --comments`. Dùng `-F json` để có output máy đọc được.
- **Liệt kê issue**: `glab issue list -O json` kèm bộ lọc `--label` phù hợp.
- **Bình luận vào issue**: `glab issue note <number> --message "..."`. GitLab gọi bình luận là "note".
- **Gắn / gỡ label**: `glab issue update <number> --label "..."` / `--unlabel "..."`. Nhiều label có thể ngăn cách bằng dấu phẩy hoặc lặp lại flag.
- **Đóng**: `glab issue close <number>`. `glab issue close` không nhận bình luận khi đóng, nên hãy đăng lời giải thích trước bằng `glab issue note <number> --message "..."`, rồi mới đóng.
- **Merge request**: GitLab gọi PR là "merge request". Dùng `glab mr create`, `glab mr view`, `glab mr note`, v.v., cùng dạng với `gh pr ...`, chỉ thay `pr` bằng `mr` và `comment`/`--body` bằng `note`/`--message`.

Suy ra repo từ `git remote -v`; `glab` tự làm việc này khi chạy bên trong một bản clone.

## Merge request là một kênh triage

**MR là kênh nhận yêu cầu (MRs as a request surface): no.** _(Đặt thành `yes` nếu repo này coi merge request từ bên ngoài là yêu cầu tính năng; `/triage` đọc cờ này.)_

Khi đặt thành `yes`, MR đi qua cùng bộ label và trạng thái như issue, dùng các lệnh `glab mr` tương ứng:

- **Đọc MR**: `glab mr view <number> --comments` và `glab mr diff <number>` để xem diff.
- **Liệt kê MR bên ngoài cần triage**: `glab mr list -O json`, rồi chỉ giữ những MR mà tác giả không phải member/owner của project (MR của người đóng góp, không phải việc đang dở của maintainer).
- **Bình luận / gắn label / đóng**: `glab mr note`, `glab mr update --label`/`--unlabel`, `glab mr close`.

Khác với GitHub, GitLab đánh số issue và MR riêng, nên `#42` không còn mơ hồ một khi bạn biết maintainer đang nói tới kênh nào.

## Khi một skill bảo "đăng lên issue tracker"

Tạo một GitLab issue.

## Khi một skill bảo "lấy ticket liên quan"

Chạy `glab issue view <number> --comments`.

## Thao tác wayfinding

Dùng bởi `/wayfinder`. **Bản đồ** (**map**) là một issue duy nhất, với các issue **con** (**child**) làm ticket.

- **Map**: một issue duy nhất gắn label `wayfinder:map`, phần thân gồm Đích đến / Ghi chú / Các quyết định đã chốt / Chưa xác định rõ. `glab issue create --label wayfinder:map`. (Ở các gói GitLab có epic gốc, có thể dùng một epic để chứa map; issue gắn label thì chạy được ở mọi nơi.)
- **Ticket con**: một issue có `Part of #<map>` ở đầu phần mô tả, được nối với map (`glab issue create --linked-issues <map> --link-type relates_to`), và gắn label `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Khi đã được nhận, ticket được assign cho dev đang dẫn dắt.
- **Chặn (blocking)**: dùng **liên kết chặn gốc** (**native blocking link**) của GitLab, cách biểu diễn chuẩn và hiển thị được trên UI. Thêm bằng quick action `/blocked_by #<n>`, đăng dưới dạng note (`glab issue note <child> --message "/blocked_by #<blocker>"`). Liên kết chặn gốc là tính năng của gói Premium/Ultimate; ở gói miễn phí (hoặc nơi không có), dùng phương án dự phòng là một dòng `Blocked by: #<n>, #<n>` ở đầu phần mô tả. Ticket được gỡ chặn khi mọi issue chặn nó đều đã đóng.
- **Truy vấn frontier**: liệt kê các ticket con của map bằng `glab api projects/:id/issues/<map>/links`, giữ các issue còn mở có label `wayfinder:<type>`; loại những issue còn bị chặn bởi issue đang mở: một liên kết `blocked_by` gốc tới issue đang mở (`glab api projects/:id/issues/<child-iid>/links`), hoặc có issue đang mở trong dòng `Blocked by`, hoặc đã có người được assign; issue đứng đầu theo thứ tự trong map được chọn.
- **Nhận (claim)**: `glab issue update <n> --assignee @me`, là thao tác ghi đầu tiên của phiên.
- **Giải quyết (resolve)**: `glab issue note <n> --message "<answer>"`, rồi `glab issue close <n>`, rồi nối một con trỏ ngữ cảnh (ý chính + link) vào mục **Các quyết định đã chốt** của map.
