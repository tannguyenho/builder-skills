---
name: wizard
description: >-
  Tạo một wizard bash tương tác dẫn người dùng đi qua những bước chỉ họ mới làm
  được. Dùng khi cấp phát hạ tầng, thiết lập credential hoặc secret cho CI, đi
  qua một dashboard bên thứ ba lạ lẫm, hoặc chạy một lần migration hay chuyển
  đổi (cutover). Không dùng cho những bước agent tự làm được. Câu kích hoạt:
  "làm wizard hướng dẫn mình setup", "tạo script từng bước để lấy API key",
  "make a setup wizard", "walk me through setting up the secrets".
---

# Wizard

**Wizard** là một script bash dẫn một người, từng bước một, đi qua một quy trình làm tay vừa mất công làm bằng tay vừa mất công giải thích lại cho AI mỗi lần. Nó mở từng URL, nói chính xác cần bấm gì và copy gì, thu lại các giá trị, ghi chúng vào đúng chỗ (`.env`, GitHub secrets), xác nhận ở mọi giai đoạn, và cho thấy còn bao nhiêu stage nữa. Nó có thể cấu hình dịch vụ bên thứ ba, chạy một lần migration, hoặc chuyển dự án từ trạng thái này sang trạng thái khác.

Phần UX dễ chịu đã được giải quyết sẵn bởi [template.sh](template.sh): tiến độ theo từng stage, cổng xác nhận, mở URL đa nền tảng (kể cả WSL), nhập secret ẩn, upsert `.env` chạy lại vẫn an toàn (idempotent), ghi `gh secret`/`gh variable`, và bản tổng kết cuối. **Việc của bạn chỉ là khoanh phạm vi quy trình và viết các stage của nó.** Phần thư viện phía trên dấu mốc `STAGES` giống hệt nhau ở mọi wizard; chính sự nhất quán đó là mục đích: không bao giờ sửa tay phần này.

Wizard mặc định là đồ dùng một lần: làm cho một lần chạy, lưu ở đường dẫn nháp hoặc `scripts/`, xoá khi xong việc. Chỉ commit khi user muốn có một đường thiết lập lặp lại được, cần nằm trong repo.

## Quy trình

### 1. Khoanh phạm vi quy trình

Xác định mọi bước làm tay mà người dùng phải thực hiện và mọi giá trị được thu lại trong quá trình. Đọc repo trước, đừng hỏi suông:

- Với việc thiết lập: `.env`, `.env.example`, `.env.*`, `README`, `docker-compose*`, cấu hình framework, và `.github/workflows/*` (mỗi tham chiếu `secrets.*` / `vars.*` là một giá trị wizard phải tạo ra).
- Với migration hoặc chuyển đổi: trạng thái hiện tại, trạng thái đích, và các hành động không đảo ngược được ở giữa.

Sau đó cho user xem danh sách stage theo thứ tự cùng các giá trị mỗi stage tạo ra, và xác nhận: họ có thể thêm, bớt hoặc đổi thứ tự.

**Xong khi:** mọi stage đã được đặt tên theo thứ tự, và với mỗi giá trị được thu lại bạn biết (a) người dùng lấy nó ở đâu, (b) nó được ghi vào đâu (`.env`, một GitHub secret, cả hai, hoặc không đâu cả; có stage chỉ là hành động thuần), và (c) nó là bí mật (nhập ẩn) hay công khai.

### 2. Vạch hành trình của từng stage

Với mỗi stage, viết đường đi chính xác mà người dùng sẽ theo: mở URL nào, làm gì ở đó, giá trị hiện ở đâu, nó điền vào biến nào: vd "Dashboard → Developers → API keys → Reveal test key → copy". Chỗ nào bạn không thực sự biết UI hiện tại hoặc câu lệnh chính xác, hãy nói ra và hỏi user hoặc tra tài liệu: không bao giờ bịa ra những bước có thể không tồn tại.

**Xong khi:** mọi stage đều dẫn tới hướng dẫn cụ thể mà một người lạ cũng làm theo được.

### 3. Viết wizard

Copy `template.sh` tới đường dẫn đích. Thay stage ví dụ bằng mỗi bước một `stage`, theo thứ tự phụ thuộc. Dùng các helper của thư viện: `stage`, `say`/`step`, `open_url`, `ask`/`ask_secret`, `write_env`, `set_secret`/`set_var`, `pause`/`confirm`. Đặt `TOTAL_STAGES` bằng số stage bạn đã viết.

Giữ đúng chuẩn mà template đặt ra: mở URL trước khi hỏi giá trị của nó, dùng `ask_secret` cho mọi thứ bí mật, `write_env` mọi giá trị cần lưu, chỉ `set_secret` những giá trị CI thực sự cần, và `confirm` trước mọi hành động không đảo ngược được. Mỗi `stage` xoá màn hình để chỉ bước hiện tại hiển thị: giữ mỗi stage cho một việc tập trung để không có gì người dùng cần bị trôi khỏi màn hình. Không động vào phần thư viện phía trên dấu mốc.

Template đã dịch sẵn chữ hiển thị sang tiếng Việt; viết các chuỗi `say`/`step`/`ask` của stage cũng bằng tiếng Việt cho đồng bộ.

### 4. Kiểm tra và bàn giao

- `bash -n <script>`; chạy `shellcheck` nếu có.
- `chmod +x <script>`.
- Đừng tự chạy nó từ đầu đến cuối: nó mở trình duyệt và chờ người dùng nhập. Thay vào đó hãy lần theo nó một cách tĩnh: mọi giá trị ở bước 1 đều được thu lại và nằm đúng chỗ bước 1 đã nói, và mọi tên `set_secret` khớp chính xác với một tham chiếu `secrets.*` trong CI.
- Nói cho user cách chạy. Nếu đó là đường thiết lập lặp lại được, hãy commit nó và link từ README để người sau chạy script thay vì đi hỏi AI.
