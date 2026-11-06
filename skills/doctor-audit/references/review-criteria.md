# Tiêu chí chấm skill (Bước 4)

Mục tiêu của một skill: agent đọc xong làm đúng việc, với ít chữ nhất có thể. Mỗi dòng trong skill tốn context của agent mỗi lần skill được gọi, nên dòng nào không làm thay đổi hành vi của agent là dòng thừa. Đọc từng skill **đầy đủ**, kể cả `references/`, rồi chấm theo các mục dưới đây.

## ✂️ Lược bớt

- **Câu không thay đổi hành vi (no-op):** lời khuyên chung mà agent vốn đã làm ("viết code sạch", "cẩn thận"), câu khích lệ, câu nhắc lại tiêu đề. Phép thử: xoá câu đó đi, agent có làm khác không? Không thì nó thừa.
- **Lặp trong cùng skill:** một quy tắc được nói lại ở nhiều bước. Giữ một chỗ, chỗ còn lại chỉ trỏ tới nó.
- **Lặp giữa các skill:** file giống hoặc gần giống nhau ở nhiều skill (script đã báo file trùng y hệt; tự tìm thêm loại gần giống, vd `honesty-protocol.md`, `research-principles.md` ở cả `product-design` và `product-competitors`). Mỗi skill phải đóng gói được riêng lẻ cho claude.ai, nên lặp đôi khi là bắt buộc. Khi đó đề xuất giữ hai bản **giống hệt nhau** để dễ đồng bộ, thay vì để mỗi bản lệch một kiểu.
- **Nội dung lỗi thời:** nhắc tới skill, lệnh, tool hay tính năng không còn tồn tại; số dòng hoặc bảng mục lục không còn khớp file.
- **SKILL.md quá dài:** phần chỉ cần ở một nhánh hiếm gặp thì chuyển sang `references/`, kèm một dòng nói khi nào đọc.

Riêng **skill dịch**, lược một đoạn có trong bản gốc là tạo thêm một `adaptation`. Lần đồng bộ sau phải giữ chỗ lược đó, nên chỉ đề xuất khi được nhiều. Đánh dấu rõ là "khác bản gốc" trong đề xuất.

## 🔧 Cải thiện

- **Description:** có nói rõ *làm gì* và *khi nào dùng* không? Có câu kích hoạt tiếng Việt mà user thật sẽ gõ không? Skill tự gọi mà description mơ hồ thì Claude sẽ không gọi. Skill gọi tay mà description quá rộng thì vô hại, nhưng vẫn nên gọn.
- **Bước chưa rõ:** lấy từ kết quả chạy thử khô ở Bước 3b. Mỗi chỗ subagent phải đoán là một đề xuất.
- **Thiếu "vì sao":** quy tắc quan trọng không kèm lý do thì agent không xử lý được tình huống skill không nói tới. Đề xuất thêm một mệnh đề lý do, không thêm chữ HOA.
- **Thiếu điểm dừng hay bước xin xác nhận:** thao tác ghi ra ngoài (tạo issue, push, gọi API, xoá file) phải có bước hỏi user trước, hoặc skill phải chỉ chạy khi user gõ lệnh.
- **Phụ thuộc:** gọi skill khác mà skill đó chặn tự gọi; giả định công cụ (`gh`, `glab`, Figma MCP, WebSearch) mà không nói phải làm gì khi thiếu.
- **Chất lượng tiếng Việt:** câu dịch sát từng chữ, đọc gượng; một thuật ngữ mà dịch nhiều kiểu trong cùng skill hay giữa các skill; đoạn còn sót tiếng Anh.
- **Việc lặp lại nên thành script:** nếu skill bắt agent tự làm một việc máy móc nhiều bước mỗi lần chạy, đề xuất đóng gói thành script trong `scripts/`.

## ❓ Cần user quyết

Đưa vào đây khi đề xuất phụ thuộc vào cách team làm việc chứ không phải chất lượng skill. Ví dụ:

- bỏ hẳn một skill ít dùng;
- đổi một skill gọi tay sang tự động (hoặc ngược lại);
- gộp hai skill gần nhau (`grill-me` và `grill-with-docs`);
- đổi mặc định (ngôn ngữ đầu ra, issue tracker).

## Cách viết một đề xuất

Mỗi đề xuất có bốn phần:

- **vị trí**: file và heading hoặc đoạn;
- **vấn đề**;
- **đề xuất cụ thể**: nên kèm câu thay thế nếu ngắn;
- **được gì**: bớt bao nhiêu dòng, hoặc agent làm đúng hơn ở chỗ nào.

Sắp xếp trong mỗi skill theo mức tác động, cao trước. Skill không có gì đáng sửa thì ghi vào mục "Không cần làm gì". Đừng nặn ra đề xuất cho đủ số.
