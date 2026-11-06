# Định dạng GLOSSARY.md

## Cấu trúc

```md
# {Tên context}

{Mô tả một hoặc hai câu: context này là gì và vì sao nó tồn tại.}

## Ngôn ngữ

**Order**:
{Mô tả thuật ngữ trong một hoặc hai câu}
_Tránh dùng_: Purchase, transaction

**Invoice**:
Yêu cầu thanh toán gửi cho khách hàng sau khi giao hàng.
_Tránh dùng_: Bill, payment request

**Customer**:
Một người hoặc tổ chức đặt hàng.
_Tránh dùng_: Client, buyer, account
```

## Quy tắc

- **Có chính kiến.** Khi có nhiều từ cho cùng một khái niệm, chọn từ tốt nhất và liệt kê các từ còn lại dưới `_Tránh dùng_`.
- **Định nghĩa thật gọn.** Tối đa một hoặc hai câu. Định nghĩa nó LÀ gì, không phải nó LÀM gì.
- **Chỉ đưa vào những thuật ngữ riêng của context dự án này.** Các khái niệm lập trình chung (timeout, kiểu lỗi, pattern tiện ích) không thuộc về đây, kể cả khi dự án dùng chúng rất nhiều. Trước khi thêm một thuật ngữ, hãy tự hỏi: đây là khái niệm riêng của context này, hay là khái niệm lập trình chung? Chỉ loại thứ nhất mới được đưa vào.
- **Nhóm thuật ngữ dưới các heading con** khi tự nhiên hình thành các cụm. Nếu mọi thuật ngữ thuộc về một mảng thống nhất duy nhất, một danh sách phẳng là được.

## Repo một context và nhiều context

**Một context (hầu hết repo):** Một file `GLOSSARY.md` ở thư mục gốc repo.

**Nhiều context:** Một file `GLOSSARY-MAP.md` ở thư mục gốc repo liệt kê các context, chúng nằm ở đâu, và chúng liên quan với nhau thế nào:

```md
# Bản đồ Glossary

## Các context

- [Ordering](./src/ordering/GLOSSARY.md): nhận và theo dõi đơn hàng của khách
- [Billing](./src/billing/GLOSSARY.md): tạo hoá đơn và xử lý thanh toán
- [Fulfillment](./src/fulfillment/GLOSSARY.md): quản lý việc lấy hàng trong kho và vận chuyển

## Quan hệ

- **Ordering → Fulfillment**: Ordering phát event `OrderPlaced`; Fulfillment tiêu thụ chúng để bắt đầu lấy hàng
- **Fulfillment → Billing**: Fulfillment phát event `ShipmentDispatched`; Billing tiêu thụ chúng để tạo hoá đơn
- **Ordering ↔ Billing**: Dùng chung type `CustomerId` và `Money`
```

Skill tự suy ra cấu trúc nào đang áp dụng:

- Nếu có `GLOSSARY-MAP.md`, đọc nó để tìm các context
- Nếu chỉ có một `GLOSSARY.md` ở gốc, đó là một context
- Nếu không có cả hai, tạo `GLOSSARY.md` ở gốc một cách lười biếng khi thuật ngữ đầu tiên được chốt

Khi có nhiều context, suy ra chủ đề hiện tại liên quan tới context nào. Nếu không rõ, hãy hỏi.
