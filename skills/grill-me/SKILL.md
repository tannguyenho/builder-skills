---
name: grill-me
description: >-
  Phỏng vấn, vặn hỏi user không khoan nhượng về một kế hoạch, quyết định hoặc
  ý tưởng cho tới khi hai bên hiểu chung, đi theo từng vòng câu hỏi có đánh số
  kèm câu trả lời đề xuất. Dùng khi user muốn thử thách (stress-test) suy nghĩ
  của mình, hoặc nói các câu kiểu "grill me", "vặn hỏi kế hoạch này",
  "phản biện ý tưởng này", "hỏi xoáy giúp mình", "stress-test this plan",
  "grill this idea".
---

# Grill Me

Phỏng vấn user không khoan nhượng cho đến khi hai bên đạt được hiểu biết chung. Hình dung việc này như một **cây thiết kế** (**design tree**): mỗi quyết định lại rẽ nhánh ra những quyết định phụ thuộc vào nó.

Đi qua cây theo từng **vòng** (**round**). **Biên** (**frontier**) là mọi quyết định mà các điều kiện tiên quyết đã được chốt: những câu hỏi bạn có thể hỏi _ngay bây giờ_ mà không phải đoán trước những câu trả lời bạn chưa được nghe. Hỏi toàn bộ biên trong một vòng: đánh số từng câu hỏi và đưa ra câu trả lời bạn đề xuất. Sau đó chờ user trả lời rồi mới sang vòng tiếp theo.

Định dạng một vòng như sau:

```
❓ **Q1** - **<tiêu đề câu hỏi>**: <nội dung câu hỏi, có thể gồm nhiều đoạn, kèm nhiều lựa chọn>

➡️ <câu trả lời bạn đề xuất>

---

❓ **Q2** - **<tiêu đề câu hỏi>**: <nội dung câu hỏi, có thể gồm nhiều đoạn, kèm nhiều lựa chọn>

➡️ <câu trả lời bạn đề xuất>
```

Diễn đạt mỗi câu hỏi sao cho trả lời "có" nghĩa là chấp nhận câu trả lời bạn đề xuất.

Mỗi vòng user trả lời sẽ định hình lại cây: các quyết định đã chốt đẩy biên ra xa hơn và mở khoá những câu hỏi phụ thuộc vào chúng. Tính lại biên và hỏi vòng tiếp theo. Một câu hỏi mà câu trả lời phụ thuộc vào một câu hỏi khác vẫn còn mở trong vòng này thì thuộc về một vòng _sau_, không phải vòng này.

Tìm _sự kiện_ (fact) là việc của bạn, không bao giờ là việc của user. Khi một câu hỏi ở biên cần một sự kiện từ môi trường (filesystem, tool, v.v.), hãy giao cho một sub-agent với context window mới để đi tìm; đừng hỏi user bất cứ điều gì bạn có thể tự tra được. Đừng đứng chờ: một lượt khám phá đang chạy là một điều kiện tiên quyết chưa chốt, nên chỉ những câu hỏi phụ thuộc vào nó mới phải chờ sub-agent báo về; các câu còn lại của biên thì hỏi ngay. _Quyết định_ là của user: đưa từng quyết định cho họ và chờ.

Phiên kết thúc khi biên trống: mọi nhánh của cây thiết kế đã được đi qua, không còn điều gì bị ngầm giả định. Không hành động dựa trên kết quả cho đến khi user xác nhận rằng hai bên đã hiểu chung.
