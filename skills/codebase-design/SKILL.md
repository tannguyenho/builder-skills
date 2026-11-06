---
name: codebase-design
description: >-
  Bộ từ vựng chung để thiết kế deep module (module sâu): nhiều hành vi sau một
  interface nhỏ, đặt ở một seam gọn, test được qua chính interface đó. Dùng khi
  user muốn thiết kế hoặc cải thiện interface của một module, tìm cơ hội làm sâu
  module, quyết định đặt seam ở đâu, làm code dễ test hơn hoặc dễ cho AI đọc hiểu
  hơn, hoặc khi một skill khác cần bộ từ vựng deep module. Câu kích hoạt: "thiết
  kế lại interface module này", "seam nên đặt ở đâu", "làm sao cho dễ test hơn",
  "design this module's interface", "where should the seam go", "make this more
  testable".
---

# Thiết kế codebase

Thiết kế **deep module** (module sâu): nhiều hành vi nằm sau một interface nhỏ, đặt ở một seam gọn, test được qua interface đó. Dùng ngôn ngữ và các nguyên tắc này ở bất cứ đâu code đang được thiết kế hoặc tái cấu trúc. Mục tiêu là đòn bẩy (leverage) cho bên gọi, tính tập trung (locality) cho người bảo trì, và khả năng test cho tất cả mọi người.

## Bảng thuật ngữ

Dùng đúng các thuật ngữ này: đừng thay bằng "component", "service", "API" hay "boundary". Ngôn ngữ nhất quán chính là toàn bộ mục đích.

**Module**: bất cứ thứ gì có một interface và một implementation. Cố ý không gắn với quy mô: một hàm, một class, một package, hay một lát cắt xuyên nhiều tầng. _Tránh dùng_: unit, component, service.

**Interface**: mọi thứ bên gọi phải biết để dùng module đúng cách: type signature, nhưng còn cả các bất biến (invariant), ràng buộc về thứ tự, các kiểu lỗi, cấu hình bắt buộc và đặc tính hiệu năng. _Tránh dùng_: API, signature (quá hẹp, chỉ nói về bề mặt ở mức kiểu dữ liệu).

**Implementation**: phần bên trong module, phần thân code của nó. Khác với **Adapter**: một thứ có thể là adapter nhỏ nhưng implementation lớn (một Postgres repo) hoặc adapter lớn nhưng implementation nhỏ (một bản fake in-memory). Dùng "adapter" khi chủ đề là seam; còn lại dùng "implementation".

**Depth** (độ sâu): đòn bẩy tại interface. Lượng hành vi mà bên gọi (hoặc test) khai thác được trên mỗi đơn vị interface họ phải học. Module là **deep** (sâu) khi có nhiều hành vi nằm sau một interface nhỏ, là **shallow** (nông) khi interface gần phức tạp bằng implementation.

**Seam** _(Michael Feathers)_: một vị trí mà bạn có thể thay đổi hành vi mà không phải sửa code ngay tại chỗ đó; là *vị trí* nơi interface của module nằm. Đặt seam ở đâu là một quyết định thiết kế riêng, tách biệt với việc đặt gì phía sau nó. _Tránh dùng_: boundary (bị quá tải nghĩa với bounded context của DDD).

**Adapter**: một thứ cụ thể đáp ứng một interface tại một seam. Mô tả *vai trò* (nó lấp vào khe nào), không phải bản chất (bên trong có gì).

**Leverage** (đòn bẩy): thứ bên gọi nhận được từ depth. Nhiều năng lực hơn trên mỗi đơn vị interface họ phải học. Một implementation hoàn vốn qua N chỗ gọi và M test.

**Locality** (tính tập trung): thứ người bảo trì nhận được từ depth. Thay đổi, bug, hiểu biết và việc kiểm chứng dồn về một chỗ thay vì rải khắp các bên gọi. Sửa một lần, đúng ở mọi nơi.

## Sâu và nông

**Deep module** = interface nhỏ + nhiều implementation:

```
┌─────────────────────┐
│   Small Interface   │  ← Ít method, tham số đơn giản
├─────────────────────┤
│                     │
│  Deep Implementation│  ← Logic phức tạp được giấu đi
│                     │
└─────────────────────┘
```

**Shallow module** = interface lớn + ít implementation (nên tránh):

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Nhiều method, tham số phức tạp
├─────────────────────────────────┤
│  Thin Implementation            │  ← Chỉ chuyển tiếp lời gọi
└─────────────────────────────────┘
```

Khi thiết kế một interface, hãy hỏi:

- Có giảm được số method không?
- Có đơn giản hoá được tham số không?
- Có giấu thêm được độ phức tạp vào bên trong không?

## Nguyên tắc

- **Depth là thuộc tính của interface, không phải của implementation.** Một deep module bên trong vẫn có thể ghép từ nhiều phần nhỏ, mock được, thay được; chỉ là chúng không thuộc interface. Một module có thể có **seam nội bộ** (**internal seam**, riêng tư trong implementation, dùng cho test của chính nó) bên cạnh **seam bên ngoài** (**external seam**) tại interface.
- **Phép thử xoá bỏ (deletion test).** Hãy tưởng tượng xoá module đi. Nếu độ phức tạp biến mất, nó chỉ là lớp chuyển tiếp (pass-through). Nếu độ phức tạp xuất hiện lại ở N bên gọi, nó đang làm đúng việc của mình.
- **Interface là bề mặt test.** Bên gọi và test đi qua cùng một seam. Nếu bạn muốn test *vượt qua* interface, có lẽ module đang có hình dạng sai.
- **Một adapter nghĩa là seam giả định. Hai adapter nghĩa là seam thật.** Đừng tạo seam trừ khi thực sự có thứ gì đó thay đổi qua nó.

## Thiết kế để dễ test

Interface tốt khiến việc test trở nên tự nhiên:

1. **Nhận dependency từ ngoài vào, đừng tự tạo ra.**

   ```typescript
   // Testable
   function processOrder(order, paymentGateway) {}

   // Hard to test
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **Trả về kết quả, đừng tạo side effect.**

   ```typescript
   // Testable
   function calculateDiscount(cart): Discount {}

   // Hard to test
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **Bề mặt nhỏ.** Ít method hơn = cần ít test hơn. Ít tham số hơn = khâu chuẩn bị test đơn giản hơn.

## Quan hệ giữa các khái niệm

- Một **Module** có đúng một **Interface** (bề mặt nó trình ra cho bên gọi và test).
- **Depth** là thuộc tính của một **Module**, đo theo **Interface** của nó.
- **Seam** là nơi **Interface** của một **Module** nằm.
- **Adapter** nằm tại một **Seam** và đáp ứng **Interface**.
- **Depth** sinh ra **Leverage** cho bên gọi và **Locality** cho người bảo trì.

## Các cách hiểu bị loại bỏ

- **Depth là tỉ lệ số dòng implementation trên số dòng interface** (Ousterhout): khuyến khích độn thêm implementation. Ở đây ta dùng depth-theo-đòn-bẩy.
- **"Interface" là từ khoá `interface` của TypeScript hoặc các public method của class**: quá hẹp: interface ở đây gồm mọi sự thật mà bên gọi phải biết.
- **"Boundary"**: bị quá tải nghĩa với bounded context của DDD. Hãy nói **seam** hoặc **interface**.

## Đi sâu hơn

- **Làm sâu một cụm module dựa trên các dependency của nó**, xem [DEEPENING.md](DEEPENING.md): phân loại dependency, kỷ luật seam, và cách test "thay thế, đừng chồng lớp".
- **Khám phá các interface thay thế**, xem [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md): chạy song song nhiều sub-agent để thiết kế interface theo nhiều cách khác hẳn nhau, rồi so sánh theo depth, locality và vị trí đặt seam.
