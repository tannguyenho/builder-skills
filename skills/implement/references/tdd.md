# Phát triển hướng kiểm thử (Test-Driven Development)

TDD là vòng lặp red → green. Tài liệu này là phần tham chiếu giúp vòng lặp đó tạo ra những test đáng giữ: thế nào là một test tốt, test đặt ở đâu, các anti-pattern, và các quy tắc của vòng lặp. Mọi phần đều áp dụng cho mọi chu kỳ: tra cứu chúng trước và trong vòng lặp, không phải sau.

Khi khám phá codebase, đọc `GLOSSARY.md` (nếu có) để tên test và từ vựng của interface khớp với ngôn ngữ domain của dự án, và tôn trọng các ADR trong khu vực bạn đang động vào.

## Thế nào là một test tốt

Test kiểm chứng hành vi qua public interface, không qua chi tiết cài đặt. Code có thể thay đổi hoàn toàn; test thì không nên phải đổi. Một test tốt đọc như một bản đặc tả: "user can checkout with valid cart" cho bạn biết chính xác năng lực nào đang tồn tại, và nó sống sót qua các lần refactor vì nó không quan tâm tới cấu trúc bên trong.

Xem phần [Test tốt và test tồi](#test-tốt-và-test-tồi) bên dưới để có ví dụ, và phần [Khi nào nên mock](#khi-nào-nên-mock) cho hướng dẫn về mock.

## Seam: test đặt ở đâu

**Seam** là ranh giới public mà bạn test tại đó: interface nơi bạn quan sát hành vi mà không thò tay vào bên trong. Test nằm ở seam, không bao giờ nhắm vào phần bên trong.

**Chỉ test ở các seam đã thống nhất trước.** Trước khi viết bất kỳ test nào, ghi ra các seam sẽ được test và xác nhận chúng với user. Không viết test nào ở một seam chưa được xác nhận. Bạn không thể test mọi thứ, nên thống nhất seam từ đầu là cách để công sức test rơi vào các luồng quan trọng và logic phức tạp, thay vì vào từng edge case.

Hỏi: "Public interface là gì, và nên test ở những seam nào?" Với mỗi seam đề xuất, kèm một dòng ghi chú: nó bắt được gì và bỏ lọt gì.

Khi chính hình dạng của interface đó còn đang được bàn (module sâu tới đâu, seam nên đặt ở đâu, interface nên lộ ra những gì), hãy gọi Skill tool với "codebase-design" để lấy bộ từ vựng. Đó là nguồn chung của các thuật ngữ module, interface, depth, seam, adapter, leverage và locality, và nó là tài liệu tham chiếu để tra cứu, không phải một phiên để chạy.

## Anti-pattern

- **Dính vào cài đặt (Implementation-coupled)**: mock các collaborator nội bộ, test method private, hoặc kiểm chứng qua đường vòng (query database thay vì dùng interface). Dấu hiệu: test vỡ khi bạn refactor dù hành vi không đổi.
- **Lặp lại chính nó (Tautological)**: assertion tính lại giá trị mong đợi theo đúng cách code tính (`expect(add(a, b)).toBe(a + b)`, một snapshot tự tay suy ra theo cùng cách, một hằng số được assert bằng chính nó), nên test pass theo cấu trúc và không bao giờ có thể bất đồng với code. Giá trị mong đợi phải đến từ một nguồn sự thật độc lập: một literal đã biết là đúng, một ví dụ tính tay, hoặc spec.
- **Cắt lát ngang (Horizontal slicing)**: viết hết test trước, rồi mới viết hết phần cài đặt. Test viết hàng loạt kiểm chứng hành vi _tưởng tượng_: bạn test _hình dạng_ của mọi thứ thay vì hành vi mà người dùng thấy, các test trở nên trơ trước thay đổi thật, và bạn cam kết cấu trúc test trước khi hiểu phần cài đặt. Thay vào đó hãy làm theo **lát dọc** (**vertical slices**): một test → một phần cài đặt → lặp lại, mỗi test là một **viên đạn vạch đường** (**tracer bullet**) phản hồi theo những gì chu kỳ trước dạy bạn.

## Quy tắc của vòng lặp

- **Red trước green.** Viết test fail trước, rồi chỉ viết vừa đủ code để nó pass. Đừng đoán trước các test tương lai hay thêm tính năng phỏng đoán.
- **Mỗi lần một lát.** Mỗi chu kỳ: một seam, một test, một phần cài đặt tối thiểu.
- **Refactor không thuộc vòng lặp.** Nó thuộc về giai đoạn review (xem skill `code-review`), không thuộc chu kỳ cài đặt red → green.

## Test tốt và test tồi

### Test tốt

**Kiểu tích hợp (Integration-style)**: Test qua interface thật, không qua mock của các phần bên trong.

```typescript
// TỐT: Test hành vi quan sát được
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Đặc điểm:

- Test hành vi mà người dùng/bên gọi quan tâm
- Chỉ dùng public API
- Sống sót qua refactor nội bộ
- Mô tả CÁI GÌ, không phải NHƯ THẾ NÀO
- Mỗi test một assertion logic

### Test tồi

**Test chi tiết cài đặt**: Dính vào cấu trúc bên trong.

```typescript
// TỒI: Test chi tiết cài đặt
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Dấu hiệu đáng ngờ:

- Mock các collaborator nội bộ
- Test method private
- Assert theo số lần gọi/thứ tự gọi
- Test vỡ khi refactor mà hành vi không đổi
- Tên test mô tả NHƯ THẾ NÀO thay vì CÁI GÌ
- Kiểm chứng bằng đường bên ngoài thay vì qua interface

```typescript
// TỒI: Đi vòng qua interface để kiểm chứng
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// TỐT: Kiểm chứng qua interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

**Test lặp lại chính nó (Tautological)**: Giá trị mong đợi nhắc lại phần cài đặt, nên test pass theo cấu trúc.

```typescript
// TỒI: Giá trị mong đợi được tính lại theo đúng cách code tính
test("calculateTotal sums line items", () => {
  const items = [{ price: 10 }, { price: 5 }];
  const expected = items.reduce((sum, i) => sum + i.price, 0);
  expect(calculateTotal(items)).toBe(expected);
});

// TỐT: Giá trị mong đợi là một literal độc lập, đã biết
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```

## Khi nào nên mock

Chỉ mock ở **ranh giới hệ thống** (**system boundaries**):

- API bên ngoài (thanh toán, email, v.v.)
- Database (đôi khi — ưu tiên dùng test DB)
- Thời gian/tính ngẫu nhiên
- File system (đôi khi)

Không mock:

- Class/module của chính bạn
- Collaborator nội bộ
- Bất cứ thứ gì bạn kiểm soát được

### Thiết kế để dễ mock

Ở ranh giới hệ thống, thiết kế interface sao cho dễ mock:

**1. Dùng dependency injection**

Truyền dependency bên ngoài vào thay vì tạo chúng bên trong:

```typescript
// Dễ mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Khó mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. Ưu tiên interface kiểu SDK thay vì hàm fetch chung chung**

Tạo hàm riêng cho từng thao tác bên ngoài thay vì một hàm chung có logic điều kiện:

```typescript
// TỐT: Mỗi hàm có thể mock độc lập
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// TỒI: Muốn mock thì phải viết logic điều kiện bên trong mock
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

Cách làm kiểu SDK nghĩa là:
- Mỗi mock trả về một hình dạng cụ thể
- Không có logic điều kiện trong phần setup test
- Dễ thấy một test đang chạm tới những endpoint nào
- An toàn kiểu (type safety) cho từng endpoint
