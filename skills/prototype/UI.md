# Prototype giao diện

Sinh **vài biến thể UI khác hẳn nhau** trên cùng một route, chuyển qua lại bằng một thanh nổi ở đáy màn hình. User lật qua các biến thể trên trình duyệt, chọn một (hoặc lấy mỗi cái một ít), rồi bỏ phần còn lại.

Nếu câu hỏi là về logic/state chứ không phải giao diện trông thế nào thì nhánh này sai. Dùng [LOGIC.md](LOGIC.md).

## Khi nào đúng là dạng này

- "Trang này nên trông thế nào?"
- "Mình muốn xem vài phương án cho dashboard này trước khi chốt."
- "Thử một layout khác cho màn hình cài đặt."
- Bất cứ lúc nào user sẽ mất cả ngày phân vân giữa ba bản mockup mơ hồ trong đầu.

## Hai dạng con: rất nên chọn dạng A

Prototype UI dễ đánh giá hơn nhiều khi nó **nằm sát phần còn lại của app**: header thật, sidebar thật, dữ liệu thật, mật độ thật. Một route dùng xong bỏ đứng một mình là chân không: biến thể nào trông cũng ổn khi đứng riêng. Mặc định chọn dạng A mỗi khi có một page sẵn có hợp lý để chứa các biến thể. Chỉ dùng dạng B nếu prototype thực sự không có chỗ nào gần để ở.

### Dạng A: điều chỉnh một page sẵn có (nên chọn)

Route đã tồn tại. Các biến thể được render **trên cùng route đó**, chọn bằng search param `?variant=` trên URL. Phần lấy dữ liệu, param và auth hiện có giữ nguyên. Chỉ phần render được đổi. Đây là mặc định; chọn nó trừ khi có lý do cụ thể để không.

Nếu prototype là cho một thứ chưa có page nhưng *đương nhiên sẽ nằm trong một page* (một khu mới của dashboard, một card mới trong màn hình cài đặt, một bước mới trong một luồng sẵn có), thì vẫn là dạng A. Gắn các biến thể vào bên trong page chủ.

### Dạng B: một page mới (phương án cuối)

Chỉ dùng khi thứ đang làm prototype thực sự không có page sẵn có nào để nằm trong (vd một bề mặt cấp cao hoàn toàn mới, hoặc một luồng không nhúng hợp lý vào đâu được).

Tạo một **route dùng xong bỏ** theo đúng quy ước routing mà dự án đang dùng. Không tự nghĩ ra cấu trúc cấp cao mới. Đặt tên sao cho nhìn là biết prototype (vd có chữ `prototype` trong đường dẫn hoặc tên file). Cùng kiểu `?variant=`.

Trước khi chốt dạng B, tự kiểm tra: có thật là không có page sẵn có nào để nhúng vào? Một route trống che giấu những vấn đề thiết kế mà một route đầy dữ liệu sẽ phơi ra.

Ở cả hai dạng, thanh nổi ở đáy giống hệt nhau.

## Quy trình

### 1. Nêu câu hỏi và chọn N

Mặc định **3 biến thể**. Quá 5 thì chúng không còn khác hẳn nhau mà thành nhiễu, nên dừng ở 5.

Ghi kế hoạch thành một dòng, ở vị trí prototype hoặc comment đầu file:

> "Ba biến thể của trang cài đặt, chuyển bằng `?variant=`, trên route `/settings` sẵn có."

Cách này dùng được dù user có ở đó để phản biện hay không.

### 2. Sinh các biến thể khác hẳn nhau

Phác từng biến thể. Mỗi biến thể phải bám:

- Mục đích của page và dữ liệu nó có quyền truy cập.
- Thư viện component / hệ thống style của dự án (TailwindCSS, shadcn, MUI, CSS thuần, bất kể là gì).
- Một tên component export rõ ràng, vd `VariantA`, `VariantB`, `VariantC`.

Biến thể phải **khác nhau về cấu trúc**: khác layout, khác phân cấp thông tin, khác thao tác chính, không chỉ khác màu. Ba lưới card chỉnh nhẹ không phải prototype UI, đó là giấy dán tường. Nếu hai bản phác ra quá giống nhau, làm lại một bản với chỉ dẫn rõ "không dùng lưới card".

### 3. Nối chúng lại

Tạo một component chuyển đổi duy nhất trên route:

```tsx
// pseudo-code, chỉnh theo framework của dự án
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

Với dạng A (page sẵn có): giữ toàn bộ phần lấy dữ liệu hiện có phía trên switcher; chỉ cây render là đổi theo biến thể.

Với dạng B (page mới): route dùng xong bỏ dưới `/prototype/<name>` gắn cùng switcher đó.

### 4. Dựng thanh chuyển nổi

Một thanh nhỏ cố định ở giữa đáy màn hình, gồm ba phần:

- **Mũi tên trái**: chuyển về biến thể trước (quay vòng).
- **Nhãn biến thể**: hiện key biến thể hiện tại và, nếu biến thể export tên, cả tên đó. Vd `B (Layout có sidebar)`.
- **Mũi tên phải**: chuyển tới (quay vòng).

Hành vi:

- Bấm mũi tên sẽ cập nhật search param trên URL (dùng router của framework, vd `router.replace` trên Next, `navigate` trên React Router…) để biến thể chia sẻ được và giữ nguyên khi tải lại.
- Bàn phím: phím `←` và `→` cũng chuyển biến thể. Không bắt phím mũi tên khi đang focus vào `<input>`, `<textarea>` hoặc `[contenteditable]`.
- Tách biệt rõ về thị giác với page (vd viên thuốc tương phản cao, bóng nhẹ) để nhìn là biết nó không thuộc thiết kế đang được đánh giá.
- Ẩn ở bản build production: chặn bằng `process.env.NODE_ENV !== 'production'` hoặc kiểm tra tương đương, để lỡ merge nhầm prototype cũng không đẩy thanh này tới người dùng.

Đặt switcher trong một component dùng chung để cả hai dạng tái sử dụng. Đặt nó ở chỗ dự án để UI dùng chung.

### 5. Bàn giao

Đưa ra URL (và các key `?variant=`). User sẽ lật qua khi rảnh. Phản hồi đáng giá thường là **"mình muốn header của B với sidebar của C"**, đó mới là thiết kế họ thực sự muốn.

### 6. Lưu câu trả lời và dọn dẹp

Khi đã có biến thể thắng, lưu câu trả lời (biến thể nào và vì sao), rồi lưu prototype theo cách [SKILL](SKILL.md) mô tả. Đưa biến thể thắng vào code thật và chuyển phần còn lại sang nhánh dùng xong bỏ, không để trong main:

- **Dạng A**: đưa biến thể thắng vào page sẵn có; bỏ các biến thể thua và switcher khỏi main.
- **Dạng B**: nâng biến thể thắng thành route thật; bỏ route dùng xong bỏ và switcher khỏi main.

Bộ biến thể đầy đủ là nguồn gốc, nên nó nằm trên nhánh dùng xong bỏ chứ không vào thùng rác, vì component biến thể và switcher để lại trong main sẽ mục rất nhanh và làm người đọc sau rối.

## Anti-pattern

- **Biến thể chỉ khác màu hoặc chữ.** Đó là chỉnh sửa nhỏ, không phải prototype. Biến thể thật phải bất đồng về cấu trúc.
- **Dùng chung quá nhiều code giữa các biến thể.** Một `<Header>` dùng chung thì được; một `<Layout>` dùng chung thì mất ý nghĩa. Mỗi biến thể phải được tự do bỏ layout.
- **Nối biến thể vào thao tác ghi dữ liệu thật.** Prototype chỉ đọc là được. Nếu biến thể cần ghi, trỏ nó vào một stub: câu hỏi là "cái này nên trông thế nào", không phải "backend có chạy không".
- **Đưa thẳng prototype lên production.** Code biến thể được viết trong ràng buộc của prototype (không test, xử lý lỗi tối thiểu). Viết lại cho đàng hoàng khi đưa vào code thật.
