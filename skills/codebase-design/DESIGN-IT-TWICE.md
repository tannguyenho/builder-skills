# Thiết kế hai lần (Design It Twice)

Khi user muốn khám phá các interface thay thế cho một ứng viên làm sâu đã chọn, hãy dùng mẫu sub-agent song song này. Dựa trên "Design It Twice" (Ousterhout): ý tưởng đầu tiên của bạn khó mà là ý tưởng tốt nhất.

Dùng bộ từ vựng trong [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**, **leverage**.

## Quy trình

### 1. Phác hoạ không gian vấn đề

Trước khi khởi chạy sub-agent, hãy viết một phần giải thích về không gian vấn đề cho ứng viên đã chọn, dành cho user đọc:

- Các ràng buộc mà bất kỳ interface mới nào cũng phải thoả mãn
- Các dependency nó sẽ dựa vào, và mỗi cái thuộc loại nào (xem [DEEPENING.md](DEEPENING.md))
- Một đoạn code phác hoạ sơ bộ để neo các ràng buộc lại, không phải một đề xuất, chỉ là cách làm cho ràng buộc trở nên cụ thể

Cho user xem phần này, rồi chuyển ngay sang Bước 2. User đọc và suy nghĩ trong lúc các sub-agent làm việc song song.

### 2. Khởi chạy sub-agent

Khởi chạy song song từ 3 sub-agent trở lên, mỗi cái có một context window mới. Mỗi sub-agent phải tạo ra một interface **khác hẳn** cho module được làm sâu.

Prompt cho mỗi sub-agent một bản brief kỹ thuật riêng (đường dẫn file, chi tiết về độ ghép nối, loại dependency theo [DEEPENING.md](DEEPENING.md), những gì nằm sau seam). Bản brief này độc lập với phần giải thích không gian vấn đề cho user ở Bước 1. Giao cho mỗi agent một ràng buộc thiết kế khác nhau:

- Agent 1: "Thu nhỏ interface tối đa: nhắm tới tối đa 1–3 điểm vào. Tối đa hoá leverage trên mỗi điểm vào."
- Agent 2: "Tối đa hoá tính linh hoạt: hỗ trợ nhiều trường hợp sử dụng và khả năng mở rộng."
- Agent 3: "Tối ưu cho bên gọi phổ biến nhất: làm cho trường hợp mặc định trở nên cực kỳ đơn giản."
- Agent 4 (nếu phù hợp): "Thiết kế quanh ports & adapters cho các dependency đi qua seam."

Đưa cả bộ từ vựng của [SKILL.md](SKILL.md) lẫn bộ từ vựng của GLOSSARY.md vào brief để mỗi sub-agent đặt tên nhất quán với ngôn ngữ kiến trúc và ngôn ngữ domain của dự án.

Mỗi sub-agent trả về:

1. Interface (kiểu, method, tham số, cùng các bất biến, thứ tự, kiểu lỗi)
2. Ví dụ sử dụng cho thấy bên gọi dùng nó thế nào
3. Implementation giấu những gì phía sau seam
4. Chiến lược dependency và các adapter (xem [DEEPENING.md](DEEPENING.md))
5. Đánh đổi: chỗ nào leverage cao, chỗ nào mỏng

### 3. Trình bày và so sánh

Trình bày lần lượt từng thiết kế để user thấm từng cái, rồi so sánh chúng bằng văn xuôi. Đối chiếu theo **depth** (leverage tại interface), **locality** (thay đổi dồn về đâu) và **vị trí đặt seam**.

Sau khi so sánh, đưa ra khuyến nghị của riêng bạn: thiết kế nào bạn thấy mạnh nhất và vì sao. Nếu các phần từ những thiết kế khác nhau kết hợp tốt, hãy đề xuất một bản lai. Hãy có chính kiến: user muốn một nhận định rõ ràng, không phải một thực đơn.
