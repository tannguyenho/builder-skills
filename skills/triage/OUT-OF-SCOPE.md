# Knowledge base ngoài phạm vi

Thư mục `.out-of-scope/` trong repo lưu bản ghi lâu dài về các yêu cầu tính năng đã bị từ chối. Nó phục vụ hai mục đích:

1. **Ký ức tổ chức** (**institutional memory**): vì sao một tính năng bị từ chối, để lập luận không bị mất khi issue bị đóng
2. **Chống trùng lặp** (**deduplication**): khi một issue mới khớp với một lần từ chối trước, skill có thể đưa ra quyết định cũ thay vì tranh luận lại từ đầu

## Cấu trúc thư mục

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

Mỗi **khái niệm** (**concept**) một file, không phải mỗi issue một file. Nhiều issue yêu cầu cùng một thứ được gom vào một file.

## Định dạng file

File nên được viết theo văn phong thoải mái, dễ đọc, giống một tài liệu thiết kế ngắn hơn là một bản ghi cơ sở dữ liệu. Dùng đoạn văn, code mẫu và ví dụ để lập luận rõ ràng và hữu ích cho người lần đầu đọc tới.

```markdown
# Dark Mode

Dự án này không hỗ trợ dark mode hay theme do người dùng tuỳ chỉnh.

## Vì sao nằm ngoài phạm vi

Pipeline render giả định một bảng màu duy nhất được định nghĩa trong
`ThemeConfig`. Hỗ trợ nhiều theme sẽ cần:

- Một theme context provider bọc toàn bộ cây component
- Cơ chế phân giải style theo theme cho từng component
- Một lớp lưu trữ cho lựa chọn theme của người dùng

Đây là một thay đổi kiến trúc lớn, không khớp với trọng tâm của dự án là
soạn nội dung. Theme là việc của các bên dùng lại phía sau, những người
nhúng hoặc phân phối lại output.

```ts
// Interface ThemeConfig hiện tại không được thiết kế để chuyển đổi lúc runtime:
interface ThemeConfig {
  colors: ColorPalette; // một bảng màu duy nhất, phân giải lúc build
  fonts: FontStack;
}
```

## Các yêu cầu trước đây

- #42: "Add dark mode support"
- #87: "Night theme for accessibility"
- #134: "Dark theme option"
```

### Đặt tên file

Dùng tên ngắn, mô tả rõ, dạng kebab-case cho khái niệm: `dark-mode.md`, `plugin-system.md`, `graphql-api.md`. Tên phải đủ dễ nhận ra để người lướt qua thư mục hiểu được cái gì đã bị từ chối mà không cần mở file.

### Viết lý do

Lý do phải có thực chất: không phải "chúng tôi không muốn cái này" mà là vì sao. Lý do tốt thường dựa vào:

- Phạm vi hoặc triết lý dự án ("Dự án này tập trung vào X; theme là việc của phía sau")
- Ràng buộc kỹ thuật ("Hỗ trợ điều này sẽ cần Y, vốn xung đột với kiến trúc Z của chúng tôi")
- Quyết định chiến lược ("Chúng tôi chọn dùng A thay vì B vì...")

Lý do phải bền vững. Tránh dựa vào hoàn cảnh tạm thời ("giờ đang bận quá"); đó không phải từ chối thật, mà là hoãn lại.

## Khi nào kiểm tra `.out-of-scope/`

Trong lúc triage (Bước 1: Thu thập ngữ cảnh), đọc mọi file trong `.out-of-scope/`. Khi đánh giá một issue mới:

- Kiểm tra xem yêu cầu có khớp với một khái niệm ngoài phạm vi đã có không
- So khớp theo độ tương đồng khái niệm, không theo từ khoá: "night theme" khớp với `dark-mode.md`
- Nếu khớp, nêu ra cho maintainer: "Yêu cầu này giống với `.out-of-scope/dark-mode.md`. Trước đây mình đã từ chối vì [lý do]. Bạn vẫn thấy như vậy chứ?"

Maintainer có thể:

- **Xác nhận**: issue mới được thêm vào danh sách "Các yêu cầu trước đây" của file đang có, rồi đóng
- **Cân nhắc lại**: file ngoài phạm vi bị xoá hoặc cập nhật, và issue đi tiếp qua quy trình triage bình thường
- **Không đồng ý**: các issue có liên quan nhưng khác nhau, tiếp tục triage bình thường

## Khi nào ghi vào `.out-of-scope/`

Chỉ khi một **enhancement** (không phải bug) bị *từ chối* với `wontfix`. Điều này áp dụng cho PR enhancement y hệt như cho issue: một PR bị từ chối được ghi lại ở đây để cùng yêu cầu đó không quay lại dưới dạng code mới.

**Không** ghi vào đây khi một thứ bị đóng với `wontfix` vì nó **đã được triển khai rồi**. Đó là tính năng đã xây, không phải bị từ chối; ghi lại nó sẽ làm hỏng bước kiểm tra trùng lặp bằng những lần từ chối giả. Thay vào đó, bình luận khi đóng chỉ ra tính năng đó đang nằm ở đâu.

Quy trình:

1. Maintainer quyết định một yêu cầu tính năng nằm ngoài phạm vi
2. Kiểm tra xem đã có file `.out-of-scope/` nào khớp chưa
3. Nếu có: thêm issue mới vào danh sách "Các yêu cầu trước đây"
4. Nếu chưa: tạo file mới với tên khái niệm, quyết định, lý do và yêu cầu đầu tiên
5. Đăng bình luận lên issue giải thích quyết định và nhắc tới file `.out-of-scope/`
6. Đóng issue với label `wontfix`

## Cập nhật hoặc xoá file ngoài phạm vi

Nếu maintainer đổi ý về một khái niệm đã từng bị từ chối:

- Xoá file `.out-of-scope/` đó
- Skill không cần mở lại các issue cũ; chúng là bản ghi lịch sử
- Issue mới đã khơi lại việc cân nhắc sẽ đi tiếp qua quy trình triage bình thường
