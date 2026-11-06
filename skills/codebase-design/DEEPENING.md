# Làm sâu module (Deepening)

Cách làm sâu một cụm shallow module một cách an toàn, dựa trên các dependency của nó. Giả định bạn đã nắm bộ từ vựng trong [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**.

## Phân loại dependency

Khi đánh giá một ứng viên để làm sâu, hãy phân loại các dependency của nó. Loại dependency quyết định cách test module đã được làm sâu qua seam của nó.

### 1. Trong tiến trình (In-process)

Tính toán thuần, state trong bộ nhớ, không I/O. Luôn làm sâu được: gộp các module lại và test trực tiếp qua interface mới. Không cần adapter.

### 2. Có bản thay thế cục bộ (Local-substitutable)

Dependency có bản thay thế chạy cục bộ khi test (PGLite cho Postgres, filesystem in-memory). Làm sâu được nếu bản thay thế đó tồn tại. Module đã làm sâu được test với bản thay thế chạy ngay trong bộ test. Seam là seam nội bộ; không có port ở interface bên ngoài của module.

### 3. Ở xa nhưng do mình sở hữu (Ports & Adapters)

Các service của chính bạn nằm bên kia ranh giới mạng (microservice, API nội bộ). Định nghĩa một **port** (interface) tại seam. Deep module sở hữu logic; phần truyền tải (transport) được inject vào dưới dạng **adapter**. Test dùng adapter in-memory. Production dùng adapter HTTP/gRPC/queue.

Mẫu khuyến nghị: *"Định nghĩa một port tại seam, viết một adapter HTTP cho production và một adapter in-memory để test, để logic nằm trong một deep module dù nó được triển khai qua mạng."*

### 4. Bên ngoài thật sự (Mock)

Dịch vụ bên thứ ba (Stripe, Twilio, v.v.) mà bạn không kiểm soát. Module đã làm sâu nhận dependency bên ngoài dưới dạng một port được inject vào; test cung cấp một adapter mock.

## Kỷ luật seam

- **Một adapter nghĩa là seam giả định. Hai adapter nghĩa là seam thật.** Đừng tạo port trừ khi có ít nhất hai adapter có lý do tồn tại (thường là production + test). Một seam chỉ có một adapter thì chỉ là thêm một lớp gián tiếp.
- **Seam nội bộ và seam bên ngoài.** Một deep module có thể có seam nội bộ (riêng tư trong implementation, dùng cho test của chính nó) bên cạnh seam bên ngoài tại interface. Đừng phơi seam nội bộ ra interface chỉ vì test có dùng đến.

## Chiến lược test: thay thế, đừng chồng lớp

- Unit test cũ trên các shallow module trở thành thừa khi đã có test tại interface của module đã làm sâu; hãy xoá chúng.
- Viết test mới tại interface của module đã làm sâu. **Interface là bề mặt test**.
- Test khẳng định (assert) trên kết quả quan sát được qua interface, không phải trên state nội bộ.
- Test phải sống sót qua các lần refactor nội bộ, vì chúng mô tả hành vi, không mô tả implementation. Nếu một test phải đổi khi implementation đổi, nó đang test vượt qua interface.
