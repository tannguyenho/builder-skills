---
name: implement-spec
description: >-
  Hiện thực trọn một spec (kết quả của /to-spec và /to-tickets) thành code:
  coi các ticket là task graph, chạy song song nhiều implementer subagent
  (mỗi ticket một worktree, làm theo TDD), gộp vào một integration branch,
  rồi review bằng code-review. Dùng khi user nói "implement cả spec này",
  "chạy hết các ticket của spec", "implement spec", "build the whole spec".
disable-model-invocation: true
---

# Implement Spec

Bạn đã được cung cấp một spec. Spec này phải có các ticket đi kèm, mô tả cách hiện thực spec.

Issue tracker lẽ ra đã được cung cấp cho bạn. Nếu chưa, bảo user chạy `/setup-agent`.

Mục tiêu là toàn bộ spec được hiện thực trên một **integration branch** duy nhất, với mọi ticket được giải quyết theo cách issue tracker dùng để đóng việc.

Các ticket không phải là một danh sách các bước. Chúng là một **task graph** với quan hệ chặn (blocking) giữa nhau. Điều đó có nghĩa là luôn có một **biên** (**frontier**) gồm những ticket đã sẵn sàng để nhận làm.

Khởi động mọi subagent với một context window mới.

Giao tiếp tới và từ subagent nên thưa thớt. Giao tiếp chủ yếu qua **context pointer** (con trỏ ngữ cảnh): tới spec, ticket, ghi chú nghiên cứu, và các commit trước đó. Đừng lặp lại thông tin đã có sẵn qua các pointer.

Tài liệu TDD mà implementer subagent phải làm theo nằm ở `references/tdd.md` trong thư mục của skill này. Subagent không tự biết skill này nằm ở đâu, nên hãy đưa cho nó **đường dẫn tuyệt đối**: thư mục gốc của skill này (đường dẫn "Base directory for this skill" hiện ra khi skill được nạp) + `/references/tdd.md`.

**Implementer subagent** nên được chạy ở chế độ nền (background) khi có thể để tối đa hoá tính song song.

## Các bước

1. Đọc spec và các ticket để hiểu task graph.

2. (tuỳ chọn) Dùng một **exploration subagent** (subagent khám phá) để làm mọi việc khám phá mà các ticket cần — các file liên quan trong codebase hoặc tài liệu bên ngoài. Bảo đảm exploration subagent có thể lưu file — nó nên lưu ghi chú markdown vào một thư mục nằm ngoài repo, mà mọi subagent sau này đều truy cập được. Nhờ đó **implementer subagent** tập trung vào việc hiện thực thay vì khám phá.

3. Tạo integration branch. Nếu issue tracker đóng việc thông qua PR, hoặc user yêu cầu, mở một draft PR sau lần merge đầu tiên ở bước 5 (một branch chưa có commit nào đi trước main thì không mở PR được), đánh dấu là đóng spec và các ticket.

4. Dùng một **implementer subagent** mới cho mỗi ticket, mỗi subagent trong worktree riêng trên branch riêng. Mỗi implementer subagent:
   - xác nhận worktree của mình dựa trên integration branch trước khi bắt đầu, và reset về đó nếu không phải;
   - đọc file `references/tdd.md` của skill này (theo đường dẫn tuyệt đối bạn đưa) và làm theo TDD để xây ticket;
   - merge đầu mút (tip) của integration branch vào branch của mình trước khi báo xong

5. Khi một **implementer subagent** hoàn thành, merge công việc của nó vào integration branch bằng một **merger subagent** (subagent merge).

6. Nếu việc này làm thay đổi **biên** các ticket sẵn sàng, khởi động thêm **implementer subagent** để làm các ticket mới. Cách này cho phép song song tối đa.

7. Khi mọi ticket đã xong, gọi Skill tool với `code-review` trên integration branch. Sửa mọi vấn đề mà code review nêu ra trong một **implementer subagent** mới duy nhất.

8. Nếu đã có draft PR, đánh dấu nó sẵn sàng để review. Nếu không, giải quyết từng ticket theo cách issue tracker đóng việc, và báo cáo integration branch.

9. Dọn dẹp toàn bộ worktree của các **implementer subagent**.
