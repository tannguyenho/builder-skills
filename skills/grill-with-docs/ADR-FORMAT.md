# Định dạng ADR

ADR nằm trong `docs/adr/` và đánh số tuần tự: `0001-slug.md`, `0002-slug.md`, v.v.

Tạo thư mục `docs/adr/` một cách lười biếng (lazily): chỉ khi cần ADR đầu tiên.

## Template

```md
# {Tiêu đề ngắn của quyết định}

{1-3 câu: bối cảnh là gì, chúng ta đã quyết định gì, và vì sao.}
```

Vậy thôi. Một ADR có thể chỉ là một đoạn văn. Giá trị nằm ở việc ghi lại *rằng* một quyết định đã được đưa ra và *vì sao*, không nằm ở việc điền đủ các mục.

## Các mục tuỳ chọn

Chỉ thêm các mục này khi chúng thực sự có giá trị. Đa số ADR không cần.

- Frontmatter **Status** (`proposed | accepted | deprecated | superseded by ADR-NNNN`): hữu ích khi các quyết định được xem xét lại
- **Các phương án đã cân nhắc** (**Considered Options**): chỉ khi những phương án bị loại đáng để nhớ
- **Hệ quả** (**Consequences**): chỉ khi cần nêu ra những tác động dây chuyền không hiển nhiên

## Đánh số

Quét `docs/adr/` để tìm số lớn nhất hiện có và cộng thêm một.

## Khi nào nên đề xuất ADR

Cả ba điều sau phải cùng đúng:

1. **Khó đảo ngược**: cái giá của việc đổi ý sau này là đáng kể
2. **Gây bất ngờ nếu thiếu bối cảnh**: người đọc sau này nhìn code sẽ thắc mắc "rốt cuộc sao họ lại làm thế này?"
3. **Là kết quả của một sự đánh đổi thật sự**: đã có những phương án thay thế thực sự và bạn chọn một phương án vì những lý do cụ thể

Nếu một quyết định dễ đảo ngược, bỏ qua: bạn sẽ chỉ việc đảo nó lại. Nếu nó không gây bất ngờ, sẽ chẳng ai thắc mắc vì sao. Nếu không có phương án thay thế thực sự, thì chẳng có gì để ghi ngoài "chúng tôi đã làm điều hiển nhiên".

### Những gì đủ điều kiện

- **Hình dạng kiến trúc.** "Chúng ta dùng monorepo." "Write model dùng event sourcing, read model được project sang Postgres."
- **Pattern tích hợp giữa các context.** "Ordering và Billing giao tiếp qua domain event, không qua HTTP đồng bộ."
- **Lựa chọn công nghệ kéo theo lock-in.** Database, message bus, auth provider, nơi deploy. Không phải mọi thư viện: chỉ những thứ mà thay ra sẽ mất cả quý.
- **Quyết định về ranh giới và phạm vi.** "Dữ liệu Customer thuộc về context Customer; các context khác chỉ tham chiếu nó bằng ID." Những cái "không" rõ ràng cũng giá trị như những cái "có".
- **Cố ý đi lệch khỏi con đường hiển nhiên.** "Chúng ta viết SQL thủ công thay vì dùng ORM vì X." Bất cứ điều gì mà một người đọc hợp lý sẽ giả định điều ngược lại. Những ADR này ngăn kỹ sư tiếp theo "sửa" một thứ vốn được làm có chủ đích.
- **Ràng buộc không nhìn thấy trong code.** "Không được dùng AWS vì yêu cầu compliance." "Thời gian phản hồi phải dưới 200ms vì hợp đồng API với đối tác."
- **Phương án bị loại khi lý do loại không hiển nhiên.** Nếu bạn đã cân nhắc GraphQL và chọn REST vì những lý do tinh tế, hãy ghi lại; nếu không, sáu tháng nữa sẽ lại có người đề xuất GraphQL.
