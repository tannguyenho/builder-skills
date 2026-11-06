---
name: retro
description: >-
  Làm retrospective (nhìn lại) một phiên code: đọc lại log phiên, tìm cơ hội cải
  thiện môi trường của coding agent (điều hướng, automated check, coding
  standards, AGENTS.md, tool economy, thông tin truy cập được) và đề xuất theo
  mức độ nghiêm trọng. Dùng khi user nói "retro phiên này", "nhìn lại phiên
  vừa rồi", "rút kinh nghiệm cho agent", "run a retro", "retrospective on this
  session".
disable-model-invocation: true
---

# Retro

User đã yêu cầu một buổi **retrospective** (nhìn lại). Bạn đang đề xuất các cải tiến cho **môi trường** (**environment**) của coding agent để những lần chạy sau tốt hơn.

## Các bước

1. Gọi Skill tool với `writing-for-agents` để lấy hướng dẫn văn phong.

2. Đọc nguồn gốc (primary source) của phiên mà user chỉ định. Việc này có thể nghĩa là tìm trong các log phiên trên máy này. Nếu user không chỉ định phiên nào, mặc định là phiên hiện tại.

3. Tìm các ứng viên cải tiến theo những nhóm sau.

- **Điều hướng (Navigation)**: agent tìm đúng file dễ hay khó? Có phụ thuộc ẩn giữa các file không? Một **navigation pointer** (con trỏ điều hướng) có giúp dễ hơn không? _Dùng khi_ phiên mất nhiều thời gian để tìm một mẩu thông tin.
- **Kiểm tra tự động (Automated checks)**: có kiểm tra tự động nào bắt được lỗi agent đã mắc không? Lint, typing, test, linter cho filesystem? Đọc lệnh kiểm tra sẵn có của repo trước (script `lint`/`check` trong `package.json`/build tool, workflow CI), để nếu một kiểm tra đã tồn tại nhưng chưa được nối vào hoặc đang hỏng âm thầm thì đó mới là phát hiện, chứ không phải phát minh lại. Một repo không có **guardrail** (rào chắn) nào (không pre-commit hook, không job CI chạy lệnh lint/typecheck/test) tự nó đã là một phát hiện: repo không lint là một cơ hội bị bỏ lỡ thường trực, không phải một mặc định trung tính. _Dùng khi_ agent mắc một lỗi mà kiểm tra tự động lẽ ra bắt được, hoặc repo không có guardrail nào.
- **Chuẩn code (Coding standards)**: có nên cho **reviewer agent** (agent review) một quy tắc mới để cưỡng chế không? Có nên bỏ hoặc làm rõ một quy tắc hiện có không? Phân loại vi phạm trước: vi phạm **cơ học** (**mechanical** — một pattern cú pháp cố định, một API bị cấm, một dạng import, một quy tắc vị trí file) thì làm kiểm tra tất định, dứt khoát: một custom rule trong linter của chính repo, một pre-commit hook mới, hoặc một job CI mới, chọn cái nào rẻ nhất theo ngôn ngữ và guardrail hiện có của repo. Mặc định là xây kiểm tra thay vì viết quy tắc. Dành `CODING_STANDARDS.md` cho những chỗ thật sự cần **phán đoán** (**judgement call** — nhất quán giữa nhiều file, "khớp với style xung quanh", bất cứ thứ gì không guardrail nào thay thế được). _Dùng khi_ reviewer agent không bắt được một lỗi.
- **AGENTS.md toàn cục (Global AGENTS.md)**: có chỉ dẫn điều khiển (steering instruction) nào nên được chuyển sang coding standards (hoặc kiểm tra tự động) không? _Dùng khi_ file AGENTS.md đặc biệt lớn — trong repo HOẶC ở phạm vi toàn cục của user.
- **Tiết kiệm tool (Tool economy)**: agent có gọi tool tốn kém mà có thể tinh gọn được không? Có tooling tuỳ chỉnh nào (CLI, MCP) đặc biệt tốn token không? _Dùng khi_ agent đã gọi một tool tốn kém.
- **Chỉ dẫn vô tác dụng (No-ops)**: tìm những chỉ dẫn trong các file steering không làm thay đổi hành vi của agent. _Dùng khi_ các file steering lớn và cồng kềnh.
- **Truy cập thông tin (Information access)**: tìm cơ hội tăng khả năng truy cập thông tin của agent. Tee log của dev server, quyền chỉ-đọc vào dịch vụ bên thứ ba. _Dùng khi_ một mẩu thông tin quan trọng không có sẵn cho agent.

4. Trình bày các ứng viên này cho user, theo thứ tự mức độ nghiêm trọng.

## Tham chiếu

### Cài đặt và Review (Implementation vs Review)

Hãy nhớ rằng mọi công việc đều đi qua hai giai đoạn: cài đặt và review. Agent cài đặt chịu **áp lực context** (**context pressure**) lớn nhất. Nó chịu trách nhiệm khám phá, viết code và debug lỗi.

Agent review chịu áp lực context ít nhất — nó nhận một diff, nên không cần khám phá. Nó thường không cần viết code hay debug.

Điều này có nghĩa là agent review nên chịu trách nhiệm áp đặt coding standards, chứ không phải agent cài đặt.

### Các file

Bạn có quyền truy cập vài loại file trong repo:

- `CLAUDE.md`/`AGENTS.md`: các file này được đẩy vào context window của mọi agent làm việc trong repo. Chúng nên được dùng cực kỳ dè sẻn, thường chỉ cho **navigation pointer** tới các file khác.
- `CODING_STANDARDS.md`: file này được đọc trong lúc review, không phải lúc cài đặt. Thêm **navigation pointer** tới các thư mục docs nếu file standards dài quá 1.000 dòng.
- Docs: dùng docs làm file tham chiếu, được các file khác trỏ tới. Tìm docs đã có trước khi viết docs mới.
- Skill: dùng skill cho docs (vì description của skill đi vào context window của agent), hoặc cho các lệnh do user gọi. Làm theo lời khuyên trong skill `writing-for-agents`.
