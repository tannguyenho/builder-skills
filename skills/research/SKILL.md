---
name: research
description: >-
  Nghiên cứu một câu hỏi dựa trên nguồn gốc đáng tin cậy (tài liệu chính thức,
  mã nguồn, spec, API của bên sở hữu) rồi ghi kết quả thành một file Markdown
  trong repo, có trích nguồn cho từng ý. Chạy bằng agent nền để bạn vẫn làm việc
  tiếp. Dùng khi user muốn tìm hiểu một chủ đề, thu thập thông tin về tài liệu
  hay API, hoặc giao phần đọc tài liệu cho agent nền. Câu kích hoạt: "nghiên cứu
  giúp mình…", "tìm hiểu xem API X có…", "tra tài liệu chính thức về…",
  "research this", "look up the docs for".
---

# Research

Khởi động một **agent nền** (**background agent**) để làm phần nghiên cứu, để bạn vẫn làm việc tiếp trong lúc nó đọc. Cho agent bắt đầu với một context window mới.

Việc của agent đó:

1. Tìm hiểu câu hỏi dựa trên **nguồn gốc** (**primary sources**: tài liệu chính thức, mã nguồn, spec, API của chính bên sở hữu), không dựa trên bài viết lại của người khác. Lần theo mỗi khẳng định về đúng nguồn sở hữu nó.
2. Ghi kết quả vào một file Markdown duy nhất, trích nguồn cho từng khẳng định.
3. Lưu file ở nơi repo vẫn đang để các ghi chú kiểu này; làm theo quy ước sẵn có, và nếu chưa có quy ước thì đặt ở chỗ hợp lý rồi nói rõ đã lưu ở đâu.
