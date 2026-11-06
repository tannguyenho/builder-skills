---
name: implement
description: >-
  Hiện thực (implement) một phần việc dựa trên spec hoặc bộ ticket: code theo
  TDD ở các seam đã thống nhất, chạy typecheck và test, review bằng skill
  code-review rồi commit vào branch hiện tại. Dùng khi user nói "implement
  ticket này", "code theo spec này", "làm ticket #12", "implement this spec",
  "build this ticket".
disable-model-invocation: true
---

# Implement

Hiện thực phần việc mà user mô tả trong spec hoặc ticket.

Nếu user đưa một tham chiếu ticket, lấy ticket đó từ issue tracker và nêu tiêu đề của nó trước khi bắt đầu. Nếu tham chiếu không rõ ràng, hãy hỏi.

Đọc [references/tdd.md](references/tdd.md) và làm theo TDD ở những chỗ có thể, tại các seam đã thống nhất trước.

Chạy typecheck thường xuyên, chạy từng file test riêng lẻ thường xuyên, và chạy toàn bộ test suite một lần ở cuối.

Khi xong, gọi Skill tool với "code-review" để review công việc.

Commit công việc vào branch hiện tại.
