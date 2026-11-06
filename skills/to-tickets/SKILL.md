---
name: to-tickets
description: >-
  Chia một kế hoạch, spec hoặc cuộc hội thoại hiện tại thành một bộ ticket
  tracer-bullet (lát cắt dọc), mỗi ticket khai báo các ticket chặn nó, rồi đăng
  lên tracker đã cấu hình (cạnh chặn ghi bằng chữ, mỗi ticket một file nếu là
  tracker cục bộ; hoặc dùng liên kết chặn gốc nếu là tracker thật). Dùng khi
  user muốn chia spec/kế hoạch thành việc cụ thể cho agent nhận. Câu kích hoạt:
  "chia spec này thành ticket", "tách thành issue", "lên ticket cho kế hoạch
  này", "to-tickets", "break this into tickets", "split the spec into issues".
disable-model-invocation: true
---

# To Tickets

Chia một kế hoạch, spec hoặc cuộc hội thoại thành một bộ **ticket**: các lát cắt dọc kiểu **tracer bullet**, mỗi ticket khai báo những ticket **chặn** (**block**) nó.

Lẽ ra bạn đã được cung cấp thông tin về issue tracker và bộ label triage. Nếu chưa, bảo user chạy `/setup-agent`.

## Quy trình

### 1. Thu thập ngữ cảnh

Làm việc từ những gì đã có trong ngữ cảnh hội thoại. Nếu user truyền một tham chiếu (đường dẫn spec, số hoặc URL issue) làm tham số, hãy lấy nó về và đọc toàn bộ phần thân cùng bình luận.

### 2. Khảo sát codebase (tuỳ chọn)

Nếu bạn chưa khảo sát codebase, hãy làm để nắm trạng thái hiện tại của code. Tiêu đề và mô tả ticket nên dùng từ vựng trong glossary domain của dự án, và tôn trọng các ADR thuộc khu vực bạn đụng tới.

Tìm cơ hội **prefactor** code để việc triển khai dễ hơn. "Làm cho thay đổi trở nên dễ, rồi thực hiện thay đổi dễ đó." (**"Make the change easy, then make the easy change."**)

### 3. Phác các lát cắt dọc

Chia công việc thành các ticket **tracer bullet**.

<vertical-slice-rules>

- Mỗi lát cắt đi một đường hẹp nhưng HOÀN CHỈNH xuyên qua mọi lớp (schema, API, UI, test): cắt dọc, KHÔNG phải cắt ngang một lớp
- Một lát cắt đã hoàn thành có thể demo hoặc kiểm chứng độc lập
- Mỗi lát cắt có kích cỡ vừa một context window mới
- Mọi việc prefactor phải làm trước

</vertical-slice-rules>

Gán cho mỗi ticket các **cạnh chặn** (**blocking edges**): những ticket khác phải xong trước khi nó có thể bắt đầu. Ticket không có gì chặn thì bắt đầu được ngay.

**Refactor diện rộng là ngoại lệ của việc cắt dọc.** Một **refactor diện rộng** (**wide refactor**) là một thay đổi máy móc (đổi tên một cột, đổi kiểu một symbol dùng chung) mà **bán kính ảnh hưởng** (**blast radius**) lan ra toàn codebase, nên chỉ một lần sửa đã làm gãy hàng nghìn chỗ gọi cùng lúc và không lát cắt dọc nào có thể merge mà vẫn xanh. Đừng ép nó vào một tracer bullet; hãy sắp xếp theo kiểu **expand–contract**. Đầu tiên expand: thêm dạng mới bên cạnh dạng cũ để không gì bị gãy. Sau đó chuyển các chỗ gọi sang theo từng đợt có kích cỡ theo bán kính ảnh hưởng (theo package, theo thư mục), mỗi đợt là một ticket riêng bị chặn bởi bước expand, giữ CI xanh từ đợt này sang đợt khác vì dạng cũ vẫn còn. Cuối cùng contract: xoá dạng cũ khi không còn chỗ gọi nào, trong một ticket bị chặn bởi mọi đợt chuyển đổi. Khi ngay cả từng đợt cũng không thể tự xanh, vẫn giữ trình tự nhưng cho chúng dùng chung một nhánh tích hợp, tất cả cùng chặn một ticket cuối "tích hợp và kiểm chứng"; chỉ ở đó mới hứa hẹn xanh.

### 4. Hỏi lại user

Trình bày cách chia đề xuất dưới dạng danh sách đánh số. Với mỗi ticket, hiển thị:

- **Tiêu đề**: tên ngắn, mô tả rõ
- **Bị chặn bởi**: những ticket nào (nếu có) phải xong trước
- **Mang lại gì**: hành vi end-to-end mà ticket này làm cho chạy được

Hỏi user:

- Độ chi tiết đã hợp lý chưa? (quá thô / quá vụn)
- Các cạnh chặn đã đúng chưa: mỗi ticket có chỉ phụ thuộc vào những ticket thật sự chặn nó không?
- Có ticket nào nên gộp lại hoặc tách nhỏ hơn không?

Lặp lại cho tới khi user duyệt cách chia.

### 5. Đăng ticket lên tracker đã cấu hình

Đăng các ticket đã được duyệt. **Cách đăng** tuỳ vào tracker mà `/setup-agent` đã cấu hình; ticket thì như nhau, chỉ hình dạng của cạnh chặn là thay đổi:

- **File cục bộ** → ghi mỗi ticket một file tại `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, đánh số từ `01` theo thứ tự phụ thuộc (ticket chặn đứng trước). Dòng "Blocked by" của mỗi file liệt kê số/tiêu đề mà nó phụ thuộc. Dùng template file theo ticket bên dưới: mỗi file một ticket, không bao giờ gộp chung vào một file.
- **Issue tracker thật (GitHub, Linear, …)** → đăng mỗi ticket một issue theo thứ tự phụ thuộc (ticket chặn đứng trước) để cạnh chặn của mỗi ticket có thể tham chiếu tới định danh thật. Dùng quan hệ chặn gốc của nền tảng nếu có; nếu không, ghi "Blocked by" của mỗi ticket là các issue chặn nó. Nếu nguồn là một issue có sẵn, biến mỗi ticket thành sub-issue của nó (theo thao tác trong tài liệu tracker). Gắn label triage `ready-for-agent` trừ khi được dặn khác; các ticket này vốn được thiết kế để agent nhận làm được.

Làm theo **frontier**: bất kỳ ticket nào có mọi ticket chặn đã xong. Với một chuỗi thuần tuyến tính thì nghĩa là từ trên xuống dưới.

KHÔNG đóng hay sửa bất kỳ issue cha nào.

<local-ticket-template>

# <NN>: <Tiêu đề ticket>

**Cần làm:** hành vi end-to-end mà ticket này làm cho chạy được, nhìn từ góc độ user, không phải danh sách triển khai từng lớp.

**Blocked by:** số/tiêu đề các ticket chặn ticket này, hoặc "Không có (bắt đầu được ngay)".

**Status:** ready-for-agent

- [ ] Tiêu chí nghiệm thu 1
- [ ] Tiêu chí nghiệm thu 2

</local-ticket-template>

<issue-template>

## Issue cha

Tham chiếu tới issue cha trên tracker (nếu nguồn là một issue có sẵn, nếu không thì bỏ mục này).

## Cần làm

Hành vi end-to-end mà ticket này làm cho chạy được, nhìn từ góc độ user, không phải triển khai từng lớp.

## Tiêu chí nghiệm thu

- [ ] Tiêu chí 1
- [ ] Tiêu chí 2

## Bị chặn bởi

- Tham chiếu tới từng ticket chặn, hoặc "Không có (bắt đầu được ngay)". Bỏ mục này khi các ticket chặn đã được đặt bằng cạnh chặn gốc.

</issue-template>

Ở dạng nào cũng vậy, tránh đường dẫn file hay đoạn code cụ thể: chúng lỗi thời nhanh. Ngoại lệ: nếu một prototype đã tạo ra một đoạn code thể hiện quyết định chính xác hơn văn xuôi (state machine, reducer, schema, hình dạng type), hãy chèn nó vào và ghi chú ngắn rằng nó đến từ prototype. Cắt gọn chỉ còn phần chứa quyết định, không phải một bản demo chạy được, chỉ những phần quan trọng.
