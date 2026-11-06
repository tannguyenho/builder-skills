# Issue tracker: Markdown cục bộ

Issue và spec của repo này là các file markdown trong `.scratch/`.

## Quy ước

- Mỗi feature một thư mục: `.scratch/<feature-slug>/`
- Spec nằm ở `.scratch/<feature-slug>/spec.md`
- Các issue triển khai là mỗi ticket một file tại `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, đánh số từ `01`, không bao giờ gộp chung vào một file tickets duy nhất
- Trạng thái triage được ghi bằng một dòng `Status:` gần đầu mỗi file issue (xem `triage-labels.md` để biết chuỗi của từng vai trò)
- Bình luận và lịch sử trao đổi được nối vào cuối file, dưới heading `## Bình luận`

## Khi một skill bảo "đăng lên issue tracker"

Tạo một file mới trong `.scratch/<feature-slug>/` (tạo thư mục nếu cần).

## Khi một skill bảo "lấy ticket liên quan"

Đọc file tại đường dẫn được nhắc tới. Thường thì user sẽ đưa thẳng đường dẫn hoặc số issue.

## Thao tác wayfinding

Dùng bởi `/wayfinder`. **Bản đồ** (**map**) là một file, kèm mỗi ticket một file **con** (**child**).

- **Map**: `.scratch/<effort>/map.md` (phần thân gồm Đích đến / Ghi chú / Các quyết định đã chốt / Chưa xác định rõ).
- **Ticket con**: `.scratch/<effort>/issues/NN-<slug>.md`, đánh số từ `01`, câu hỏi nằm trong phần thân. Một dòng `Type:` ghi loại ticket (`research`/`prototype`/`grilling`/`task`); một dòng `Status:` ghi `claimed`/`resolved`.
- **Chặn (blocking)**: một dòng `Blocked by: NN, NN` gần đầu file. Ticket được gỡ chặn khi mọi file nó liệt kê đều đã `resolved`.
- **Frontier**: quét `.scratch/<effort>/issues/` tìm các file còn mở, không bị chặn và chưa ai nhận; file có số nhỏ nhất được chọn.
- **Nhận (claim)**: đặt `Status: claimed` và lưu lại trước khi làm bất cứ việc gì.
- **Giải quyết (resolve)**: nối câu trả lời dưới heading `## Câu trả lời`, đặt `Status: resolved`, rồi nối một con trỏ ngữ cảnh (ý chính + link) vào mục **Các quyết định đã chốt** trong `map.md`.
