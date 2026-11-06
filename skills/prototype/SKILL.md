---
name: prototype
description: >-
  Dựng một prototype dùng xong bỏ để trả lời một câu hỏi thiết kế. Hai dạng:
  (1) logic/state model — một file HTML tự chứa có nút bấm và kịch bản dẫn dắt để
  người không biết code cũng "bấm thử" được; (2) giao diện — nhiều biến thể UI
  khác hẳn nhau trên cùng một route, chuyển qua lại bằng thanh nổi ở đáy màn
  hình. Dùng khi user muốn kiểm tra state model/logic có hợp lý không, hoặc muốn
  xem vài phương án giao diện trước khi chốt. Câu kích hoạt: "làm prototype",
  "dựng thử vài phương án UI", "cho mình bấm thử luồng trạng thái này",
  "prototype this", "show me a few UI variants".
---

# Prototype

Prototype là **code dùng xong bỏ để trả lời một câu hỏi**. Câu hỏi quyết định hình dạng của prototype.

## Chọn nhánh

Xác định câu hỏi đang cần trả lời, dựa vào lời user, code xung quanh, hoặc hỏi user nếu họ đang có mặt:

- **"Logic / state model này có ổn không?"** → [LOGIC.md](LOGIC.md). Dựng một file HTML duy nhất, chia sẻ được (nút bấm tự do cùng các tab kịch bản dẫn dắt), đẩy state machine qua những trường hợp khó suy luận trên giấy, và người không biết code cũng tự điều khiển được.
- **"Cái này nên trông thế nào?"** → [UI.md](UI.md). Sinh vài biến thể UI khác hẳn nhau trên cùng một route, chuyển qua lại bằng một search param trên URL và một thanh nổi ở đáy màn hình.

Hai nhánh tạo ra hai sản phẩm rất khác nhau, nên chọn sai là phí trắng cả prototype. Nếu câu hỏi thật sự mơ hồ và không hỏi được user, mặc định chọn nhánh khớp hơn với code xung quanh (module backend → logic; một page hay component → UI) và ghi rõ giả định đó ở đầu prototype.

## Quy tắc chung cho cả hai nhánh

1. **Dùng xong bỏ ngay từ đầu, và đánh dấu rõ như vậy.** Đặt code prototype gần nơi nó sẽ thực sự được dùng (cạnh module hoặc page mà nó làm thử) để ngữ cảnh rõ ràng, nhưng đặt tên sao cho người đọc lướt cũng thấy đây là prototype, không phải code production. Với route UI dùng xong bỏ, theo đúng quy ước routing mà dự án đang dùng; không tự nghĩ ra cấu trúc cấp cao mới.
2. **Chạy cực dễ.** Prototype UI khởi động bằng một lệnh trong task runner của dự án: `pnpm <name>`, `python <path>`, `bun <path>`… Demo logic là một file HTML user chỉ cần bấm đúp. Dù dạng nào cũng không phải nghĩ mới chạy được.
3. **Mặc định không lưu dữ liệu.** State nằm trong bộ nhớ. Lưu trữ là thứ prototype đang _kiểm tra_, không phải thứ nó dựa vào. Nếu câu hỏi đụng tới database một cách rõ ràng, dùng một DB nháp hoặc file local với tên ghi rõ kiểu "PROTOTYPE, xoá tôi đi".
4. **Bỏ qua phần trau chuốt.** Không test, không xử lý lỗi ngoài mức đủ để prototype _chạy được_, không trừu tượng hoá. Mục tiêu là học được điều gì đó thật nhanh.
5. **Hiện rõ state.** Sau mỗi thao tác (logic) hoặc mỗi lần đổi biến thể (UI), in hoặc hiển thị toàn bộ state liên quan để user thấy cái gì vừa thay đổi.
6. **Lưu lại khi xong.** Đưa mọi quyết định đã được kiểm chứng vào code thật, rồi lưu chính prototype làm **nguồn gốc** (**primary source**): commit nó lên một nhánh dùng xong bỏ, không vào main, và để lại một con trỏ ngữ cảnh (**context pointer**) tới nhánh đó trên issue triển khai. Lưu cả câu trả lời (kết luận và câu hỏi nó đã giải quyết) trong issue hoặc một commit. Nhánh main chỉ giữ quyết định đã được kiểm chứng.
