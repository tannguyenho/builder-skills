---
name: triage
description: >-
  Đưa issue và PR từ bên ngoài đi qua một máy trạng thái gồm các vai trò triage:
  phân loại, kiểm chứng, tra hỏi (grill) khi cần, và viết brief sẵn sàng cho
  agent. Dùng khi maintainer muốn xem issue nào cần chú ý, đánh giá một issue/PR
  cụ thể, chuyển trạng thái issue, hoặc tìm việc sẵn sàng cho agent. Câu kích
  hoạt: "triage", "có issue nào cần mình xem không", "xem giúp #42", "chuyển #42
  sang ready-for-agent", "show me anything that needs my attention", "what's
  ready for agents to pick up?".
disable-model-invocation: true
---

# Triage

Đưa issue trên issue tracker của dự án đi qua một máy trạng thái nhỏ gồm các vai trò triage.

Nếu repo này coi pull request từ bên ngoài là một kênh nhận yêu cầu (xem cấu hình issue tracker), triage cũng bao gồm cả chúng: **một PR là một issue có đính kèm code**, dùng cùng vai trò, cùng trạng thái và cùng máy trạng thái, với vài điểm khác biệt được đánh dấu "với PR" bên dưới. Xác định một `#42` trơn là issue hay PR theo cấu hình tracker.

Mọi bình luận hay issue đăng lên issue tracker trong quá trình triage **bắt buộc** phải mở đầu bằng dòng lưu ý này:

```
> *Nội dung này do AI tạo ra trong quá trình triage.*
```

## Tài liệu tham khảo

- [AGENT-BRIEF.md](AGENT-BRIEF.md): cách viết agent brief bền vững
- [OUT-OF-SCOPE.md](OUT-OF-SCOPE.md): cách knowledge base `.out-of-scope/` hoạt động

## Vai trò

Hai vai trò **phân loại** (**category**):

- `bug`: có gì đó bị hỏng
- `enhancement`: tính năng mới hoặc cải tiến

Năm vai trò **trạng thái** (**state**):

- `needs-triage`: maintainer cần đánh giá
- `needs-info`: đang chờ người báo cáo bổ sung thông tin
- `ready-for-agent`: đã đặc tả đầy đủ, sẵn sàng cho agent AFK
- `ready-for-human`: cần người làm
- `wontfix`: sẽ không xử lý

Với PR, các trạng thái này được hiểu theo code đính kèm: `ready-for-agent` nghĩa là đã đính kèm brief và một agent nên làm bước tiếp theo trên diff; `ready-for-human` nghĩa là đã sẵn sàng để người merge.

Mỗi issue đã triage nên mang đúng một vai trò phân loại và một vai trò trạng thái. Nếu các vai trò trạng thái mâu thuẫn nhau, nêu ra và hỏi maintainer trước khi làm bất cứ việc gì khác.

Đây là tên vai trò chuẩn. Chuỗi label thực tế trong issue tracker có thể khác. Lẽ ra bạn đã được cung cấp bảng ánh xạ. Nếu chưa, bảo user chạy `/setup-agent`.

Chuyển trạng thái: một issue chưa có label thường đi tới `needs-triage` trước; từ đó nó chuyển sang `needs-info`, `ready-for-agent`, `ready-for-human` hoặc `wontfix`. `needs-info` quay về `needs-triage` khi người báo cáo trả lời. Maintainer có thể ghi đè bất cứ lúc nào; hãy nêu ra những lần chuyển trạng thái trông bất thường và hỏi trước khi tiếp tục.

## Cách gọi skill

Maintainer gọi `/triage` và mô tả điều họ muốn bằng ngôn ngữ tự nhiên. Hãy hiểu yêu cầu và hành động. Ví dụ:

- "Cho mình xem những gì cần mình chú ý"
- "Xem #42 nào" (issue hoặc PR)
- "Chuyển #42 sang ready-for-agent"
- "Có gì sẵn sàng cho agent nhận chưa?"

## Hiển thị những gì cần chú ý

Truy vấn issue tracker và trình bày ba nhóm, cũ nhất trước:

1. **Chưa có label**: chưa từng được triage.
2. **`needs-triage`**: đang đánh giá dở.
3. **`needs-info` có hoạt động của người báo cáo kể từ ghi chú triage gần nhất**: cần đánh giá lại.

Khi PR nằm trong phạm vi, đưa PR từ bên ngoài vào các nhóm này và gắn thẻ mỗi dòng `[PR]` hoặc `[issue]`. Bước tìm kiếm chỉ đưa ra PR *từ bên ngoài* (cấu hình tracker định nghĩa thế nào là bên ngoài), nên PR đang làm dở của một collaborator không phải việc triage. Bộ lọc này chỉ áp dụng cho bước tìm kiếm; một PR được gọi tên cụ thể thì luôn được triage bất kể tác giả là ai.

Hiển thị số lượng và một dòng tóm tắt cho mỗi mục. Để maintainer chọn.

## Triage một issue hoặc PR cụ thể

1. **Thu thập ngữ cảnh.** Đọc toàn bộ issue hoặc PR (phần thân, bình luận, label, tác giả, ngày; với PR thì cả diff). Phân tích mọi ghi chú triage trước đó để không hỏi lại những câu đã được giải đáp. Khảo sát codebase bằng từ vựng trong glossary domain của dự án, tôn trọng các ADR trong khu vực đó. Chạy hai bước kiểm tra trên codebase: (a) **trùng lặp** (**redundancy**): tìm xem hành vi được yêu cầu đã được triển khai chưa, tìm theo khái niệm domain (không chỉ theo câu chữ của yêu cầu), và báo lại bạn đã tìm ở đâu. Nếu tìm thấy, đó là `wontfix` vì đã triển khai rồi (bước 5). (b) **từng bị từ chối** (**prior rejection**): đọc `.out-of-scope/*.md` và nêu ra bất kỳ file nào giống yêu cầu này.

2. **Đề xuất.** Nói với maintainer đề xuất của bạn về phân loại và trạng thái kèm lập luận, cùng một tóm tắt ngắn về codebase liên quan tới yêu cầu (bao gồm việc nó đã được triển khai hay chưa). Chờ chỉ đạo.

3. **Kiểm chứng điều được khẳng định.** Trước khi tra hỏi, kiểm tra xem điều được khẳng định có đứng vững không. Với bug, tái hiện nó theo các bước của người báo cáo. Với PR, xác nhận diff làm đúng như nó nói: checkout về, chạy các test hoặc lệnh liên quan. Báo lại kết quả: đã xác nhận (kèm luồng code), thất bại, hoặc không đủ chi tiết (một tín hiệu mạnh cho `needs-info`). Một lần kiểm chứng đã xác nhận giúp agent brief mạnh hơn nhiều.

4. **Tra hỏi (nếu cần).** Nếu yêu cầu cần được làm rõ thêm, gọi skill `grill-with-docs` và tra hỏi cho tới khi yêu cầu thành hình, mỗi lần một loạt câu hỏi, mài sắc các thuật ngữ domain và cập nhật `GLOSSARY.md`/ADR ngay tại chỗ khi quyết định được chốt.

5. **Áp dụng kết quả:**
   - `ready-for-agent`: đăng một bình luận agent brief ([AGENT-BRIEF.md](AGENT-BRIEF.md)).
   - `ready-for-human`: cùng cấu trúc với agent brief, nhưng ghi rõ vì sao không thể giao cho agent (cần phán đoán, cần quyền truy cập bên ngoài, quyết định thiết kế, test thủ công).
   - `needs-info`: đăng ghi chú triage (template bên dưới).
   - Với `wontfix`, đóng issue, kèm bình luận tuỳ theo *lý do*:
     - **Đã triển khai rồi**: thay đổi đã tồn tại trong codebase. Chỉ ra nó nằm ở đâu; **không** ghi vào `.out-of-scope/` (knowledge base đó dành cho yêu cầu *bị từ chối*, không phải yêu cầu đã làm).
     - **Từ chối (bug)**: giải thích lịch sự, rồi đóng.
     - **Từ chối (enhancement)**: ghi vào `.out-of-scope/`, gắn link tới đó trong một bình luận, rồi đóng ([OUT-OF-SCOPE.md](OUT-OF-SCOPE.md)).
   - `needs-triage`: gắn vai trò. Bình luận tuỳ chọn nếu đã có tiến triển một phần.

## Ghi đè trạng thái nhanh

Nếu maintainer nói "chuyển #42 sang ready-for-agent", tin họ và gắn vai trò trực tiếp. Xác nhận những gì bạn sắp làm (đổi vai trò, bình luận, đóng), rồi hành động. Bỏ qua bước tra hỏi. Nếu chuyển sang `ready-for-agent` mà chưa qua phiên tra hỏi nào, hỏi xem họ có muốn viết agent brief không.

## Template needs-info

```markdown
## Ghi chú triage

**Những gì đã xác định được:**

- ý 1
- ý 2

**Những gì vẫn cần từ bạn (@reporter):**

- câu hỏi 1
- câu hỏi 2
```

Ghi lại mọi thứ đã được giải đáp trong lúc tra hỏi vào phần "đã xác định được" để công sức không bị mất. Câu hỏi phải cụ thể và làm theo được, không phải kiểu "vui lòng cung cấp thêm thông tin".

## Tiếp tục một phiên trước

Nếu issue hoặc PR đã có ghi chú triage từ trước, đọc chúng, kiểm tra xem người báo cáo đã trả lời câu hỏi nào còn treo chưa, và trình bày bức tranh cập nhật trước khi tiếp tục. Đừng hỏi lại những câu đã được giải đáp.
