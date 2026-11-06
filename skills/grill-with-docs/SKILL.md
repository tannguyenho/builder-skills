---
name: grill-with-docs
description: >-
  Phỏng vấn vặn hỏi không khoan nhượng để làm sắc một kế hoạch hoặc thiết kế,
  đồng thời chủ động xây dựng domain model của dự án và ghi tài liệu ngay trong
  lúc làm: thuật ngữ vào GLOSSARY.md, quyết định khó đảo ngược vào ADR
  (docs/adr/). Dùng khi user muốn grill một thiết kế kèm ghi docs; khi một skill
  khác cần phiên grilling + domain modeling; hoặc khi chỉ cần phần domain
  modeling (thử thách thuật ngữ, viết/sửa GLOSSARY.md, ghi/sửa ADR). Câu kích
  hoạt: "grill with docs", "vặn hỏi rồi ghi glossary/ADR", "chốt thuật ngữ
  domain", "ghi ADR cho quyết định này", "update the glossary".
---

# Grill With Docs

Skill này gồm hai phần chạy cùng nhau trong một phiên:

- **Phần 1 — Grilling**: phỏng vấn user theo từng vòng cho tới khi hai bên hiểu chung.
- **Phần 2 — Domain modeling**: trong lúc phỏng vấn, thử thách thuật ngữ và ghi `GLOSSARY.md` cùng ADR ngay khi mọi thứ vừa được chốt.

Khi một skill khác gọi skill này chỉ để làm domain modeling (vd ghi/sửa `GLOSSARY.md` hoặc ADR), chỉ cần áp dụng Phần 2.

## Phần 1 — Grilling

Phỏng vấn user không khoan nhượng cho đến khi hai bên đạt được hiểu biết chung. Hình dung việc này như một **cây thiết kế** (**design tree**): mỗi quyết định lại rẽ nhánh ra những quyết định phụ thuộc vào nó.

Đi qua cây theo từng **vòng** (**round**). **Biên** (**frontier**) là mọi quyết định mà các điều kiện tiên quyết đã được chốt: những câu hỏi bạn có thể hỏi _ngay bây giờ_ mà không phải đoán trước những câu trả lời bạn chưa được nghe. Hỏi toàn bộ biên trong một vòng: đánh số từng câu hỏi và đưa ra câu trả lời bạn đề xuất. Sau đó chờ user trả lời rồi mới sang vòng tiếp theo.

Định dạng một vòng như sau:

```
❓ **Q1** - **<tiêu đề câu hỏi>**: <nội dung câu hỏi, có thể gồm nhiều đoạn, kèm nhiều lựa chọn>

➡️ <câu trả lời bạn đề xuất>

---

❓ **Q2** - **<tiêu đề câu hỏi>**: <nội dung câu hỏi, có thể gồm nhiều đoạn, kèm nhiều lựa chọn>

➡️ <câu trả lời bạn đề xuất>
```

Diễn đạt mỗi câu hỏi sao cho trả lời "có" nghĩa là chấp nhận câu trả lời bạn đề xuất.

Mỗi vòng user trả lời sẽ định hình lại cây: các quyết định đã chốt đẩy biên ra xa hơn và mở khoá những câu hỏi phụ thuộc vào chúng. Tính lại biên và hỏi vòng tiếp theo. Một câu hỏi mà câu trả lời phụ thuộc vào một câu hỏi khác vẫn còn mở trong vòng này thì thuộc về một vòng _sau_, không phải vòng này.

Tìm _sự kiện_ (fact) là việc của bạn, không bao giờ là việc của user. Khi một câu hỏi ở biên cần một sự kiện từ môi trường (filesystem, tool, v.v.), hãy giao cho một sub-agent với context window mới để đi tìm; đừng hỏi user bất cứ điều gì bạn có thể tự tra được. Đừng đứng chờ: một lượt khám phá đang chạy là một điều kiện tiên quyết chưa chốt, nên chỉ những câu hỏi phụ thuộc vào nó mới phải chờ sub-agent báo về; các câu còn lại của biên thì hỏi ngay. _Quyết định_ là của user: đưa từng quyết định cho họ và chờ.

Phiên kết thúc khi biên trống: mọi nhánh của cây thiết kế đã được đi qua, không còn điều gì bị ngầm giả định. Không hành động dựa trên kết quả cho đến khi user xác nhận rằng hai bên đã hiểu chung.

## Phần 2 — Domain Modeling

Chủ động xây dựng và làm sắc domain model của dự án trong lúc thiết kế. Đây là kỷ luật *chủ động*: thử thách các thuật ngữ, nghĩ ra kịch bản biên (edge case), và ghi glossary cùng các quyết định xuống ngay khi chúng vừa định hình. (Chỉ *đọc* `GLOSSARY.md` để lấy từ vựng thì không phải là phần này: đó là thói quen một dòng mà skill nào cũng làm được. Phần này dành cho lúc bạn đang thay đổi model, không chỉ dùng nó.)

### Cấu trúc file

Hầu hết repo chỉ có một context:

```
/
├── GLOSSARY.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

Nếu có file `GLOSSARY-MAP.md` ở thư mục gốc, repo có nhiều context. File map chỉ ra mỗi context nằm ở đâu:

```
/
├── GLOSSARY-MAP.md
├── docs/
│   └── adr/                          ← quyết định áp dụng toàn hệ thống
├── src/
│   ├── ordering/
│   │   ├── GLOSSARY.md
│   │   └── docs/adr/                 ← quyết định riêng của context
│   └── billing/
│       ├── GLOSSARY.md
│       └── docs/adr/
```

Tạo file một cách lười biếng (lazily): chỉ khi bạn có thứ cần ghi. Nếu chưa có `GLOSSARY.md`, tạo nó khi thuật ngữ đầu tiên được chốt. Nếu chưa có `docs/adr/`, tạo nó khi cần ADR đầu tiên.

### Trong phiên

#### Đối chiếu với glossary

Khi user dùng một thuật ngữ mâu thuẫn với ngôn ngữ đã có trong `GLOSSARY.md`, chỉ ra ngay lập tức. "Glossary của bạn định nghĩa 'cancellation' là X, nhưng có vẻ bạn đang muốn nói Y. Vậy là cái nào?"

#### Làm rõ ngôn từ mơ hồ

Khi user dùng thuật ngữ mơ hồ hoặc bị dùng cho quá nhiều nghĩa, đề xuất một thuật ngữ chuẩn (canonical) chính xác. "Bạn đang nói 'account': ý bạn là Customer hay User? Đó là hai thứ khác nhau."

#### Bàn bằng kịch bản cụ thể

Khi đang bàn về các quan hệ trong domain, thử thách chúng bằng các kịch bản cụ thể. Nghĩ ra những kịch bản dò vào edge case và buộc user phải nói chính xác ranh giới giữa các khái niệm.

#### Đối chiếu với code

Khi user phát biểu một thứ hoạt động thế nào, kiểm tra xem code có khớp không. Nếu thấy mâu thuẫn, nêu ra: "Code của bạn huỷ toàn bộ Order, nhưng bạn vừa nói có thể huỷ một phần. Cái nào đúng?"

#### Cập nhật GLOSSARY.md ngay tại chỗ

Khi một thuật ngữ được chốt, cập nhật `GLOSSARY.md` ngay lúc đó. Đừng dồn lại: ghi lại ngay khi chúng xảy ra. Dùng định dạng trong [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md).

`GLOSSARY.md` phải hoàn toàn không chứa chi tiết cài đặt (implementation). Đừng coi `GLOSSARY.md` là spec, nháp, hay nơi chứa các quyết định cài đặt. Nó là glossary và không gì khác.

#### Đề xuất ADR một cách dè dặt

Chỉ đề xuất tạo ADR khi cả ba điều sau đều đúng:

1. **Khó đảo ngược**: cái giá của việc đổi ý sau này là đáng kể
2. **Gây bất ngờ nếu thiếu bối cảnh**: người đọc sau này sẽ thắc mắc "sao họ lại làm thế này?"
3. **Là kết quả của một sự đánh đổi thật sự**: đã có những phương án thay thế thực sự và bạn chọn một phương án vì những lý do cụ thể

Nếu thiếu bất kỳ điều nào trong ba điều trên, bỏ qua ADR. Dùng định dạng trong [ADR-FORMAT.md](./ADR-FORMAT.md).
