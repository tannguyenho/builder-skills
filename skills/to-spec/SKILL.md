---
name: to-spec
description: >-
  Biến cuộc hội thoại hiện tại thành một spec và đăng lên issue tracker của dự
  án: không phỏng vấn thêm, chỉ tổng hợp những gì đã bàn. Dùng khi user đã thảo
  luận xong một tính năng và muốn chốt lại thành spec/PRD để agent triển khai.
  Câu kích hoạt: "viết spec từ cuộc trao đổi này", "chốt thành spec", "tạo PRD
  rồi đăng lên tracker", "to-spec", "turn this into a spec", "write up a spec
  and publish it".
disable-model-invocation: true
---

Skill này lấy ngữ cảnh của cuộc hội thoại hiện tại cùng hiểu biết về codebase để tạo ra một spec. KHÔNG phỏng vấn user; chỉ tổng hợp những gì bạn đã biết.

Lẽ ra bạn đã được cung cấp thông tin về issue tracker và bộ label triage. Nếu chưa, bảo user chạy `/setup-agent`.

## Quy trình

1. Khảo sát repo để nắm trạng thái hiện tại của codebase, nếu bạn chưa làm. Dùng từ vựng trong glossary domain của dự án xuyên suốt spec, và tôn trọng mọi ADR thuộc khu vực bạn đụng tới.

2. Phác ra các **seam** mà bạn sẽ dùng để test tính năng. Ưu tiên seam đã có hơn seam mới. Dùng seam ở mức cao nhất có thể. Nếu cần seam mới, đề xuất chúng ở điểm cao nhất bạn có thể. Càng ít seam trong toàn codebase càng tốt - con số lý tưởng là một.

Hỏi lại user xem các seam này có đúng với kỳ vọng của họ không.

3. Viết spec theo template bên dưới, rồi đăng lên issue tracker của dự án. Gắn label triage `ready-for-agent` - không cần triage thêm.

<spec-template>

## Mô tả vấn đề

Vấn đề mà user đang gặp, nhìn từ góc độ của user.

## Giải pháp

Giải pháp cho vấn đề, nhìn từ góc độ của user.

## User story

Một danh sách user story DÀI, có đánh số. Mỗi user story theo định dạng:

1. Là một <vai trò>, tôi muốn <tính năng>, để <lợi ích>

<user-story-example>
1. Là một khách hàng dùng ngân hàng trên điện thoại, tôi muốn xem số dư các tài khoản của mình, để đưa ra quyết định chi tiêu sáng suốt hơn
</user-story-example>

Danh sách user story này phải cực kỳ đầy đủ và bao quát mọi khía cạnh của tính năng.

## Quyết định triển khai

Danh sách các quyết định triển khai đã được đưa ra. Có thể gồm:

- Các module sẽ được xây mới/sửa đổi
- Interface của các module đó sẽ được sửa đổi
- Các làm rõ kỹ thuật từ developer
- Các quyết định kiến trúc
- Thay đổi schema
- API contract
- Các tương tác cụ thể

KHÔNG đưa vào đường dẫn file hay đoạn code cụ thể. Chúng có thể lỗi thời rất nhanh.

Ngoại lệ: nếu một prototype đã tạo ra một đoạn code thể hiện quyết định chính xác hơn văn xuôi (state machine, reducer, schema, hình dạng type), hãy chèn nó ngay trong quyết định liên quan và ghi chú ngắn rằng nó đến từ prototype. Cắt gọn chỉ còn phần chứa quyết định, không phải một bản demo chạy được, chỉ những phần quan trọng.

## Quyết định về test

Danh sách các quyết định về test đã được đưa ra. Gồm:

- Mô tả thế nào là một test tốt (chỉ test hành vi bên ngoài, không test chi tiết triển khai)
- Những module nào sẽ được test
- Tiền lệ cho các test (tức các loại test tương tự đã có trong codebase)

## Ngoài phạm vi

Mô tả những gì nằm ngoài phạm vi của spec này.

## Ghi chú thêm

Mọi ghi chú thêm về tính năng.

</spec-template>
