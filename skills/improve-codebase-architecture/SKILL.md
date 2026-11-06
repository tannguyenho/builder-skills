---
name: improve-codebase-architecture
description: >-
  Quét codebase tìm cơ hội làm sâu module (deepening), trình bày thành một báo
  cáo HTML trực quan, rồi chất vấn kỹ (grill) ứng viên mà user chọn. Gọi bằng
  tay, vd "/improve-codebase-architecture", "rà kiến trúc codebase này", "review
  the codebase architecture".
disable-model-invocation: true
---

# Cải thiện kiến trúc codebase

Chỉ ra những điểm ma sát kiến trúc và đề xuất **cơ hội làm sâu** (**deepening opportunities**): các refactor biến shallow module thành deep module. Mục tiêu là khả năng test và khả năng để AI dễ đọc hiểu, dễ đi lại trong code (AI-navigability).

Lệnh này _dựa trên_ domain model của dự án và được xây trên một bộ từ vựng thiết kế chung:

- Gọi Skill tool với "codebase-design" để lấy bộ từ vựng kiến trúc (**module**, **interface**, **depth**, **seam**, **adapter**, **leverage**, **locality**) và các nguyên tắc của nó (phép thử xoá bỏ, "interface là bề mặt test", "một adapter = seam giả định, hai adapter = seam thật"). Dùng đúng các thuật ngữ này trong mọi đề xuất, và đừng trôi sang "component", "service", "API" hay "boundary".
- Ngôn ngữ domain trong `GLOSSARY.md` cho ta tên gọi của những seam tốt; các ADR trong `docs/adr/` ghi lại những quyết định mà lệnh này không được lật lại.

## Quy trình

### 1. Khám phá

**Khoanh vùng trước khi quét: YAGNI.** Làm sâu một module có lời vì nó làm cho các thay đổi về sau trên module đó dễ hơn, nên hãy ưu tiên những phần codebase vừa thay đổi gần đây. Quyết định *nhìn vào đâu* trước khi nhìn:

- Nếu user đã chỉ hướng (một module, một subsystem, một điểm đau), đi theo hướng đó và bỏ qua phần suy luận bên dưới.
- Nếu không, lần ngược một đoạn dài lịch sử commit (`git log --oneline`) để tìm các điểm nóng (hot spot) của codebase, những file và khu vực cứ xuất hiện lặp lại, và để những đường dẫn đó kéo sự chú ý của bạn trước. Nếu thay đổi rải rác, không có điểm nóng rõ ràng, hãy mở rộng phạm vi.

Đọc bảng thuật ngữ domain của dự án (`GLOSSARY.md`) và mọi ADR thuộc khu vực bạn sắp động vào trước tiên.

Sau đó khởi chạy một sub-agent với context window mới để đi khắp codebase. Đừng bám theo heuristic cứng nhắc; hãy khám phá một cách tự nhiên và ghi lại những chỗ bạn thấy ma sát:

- Chỗ nào để hiểu một khái niệm phải nhảy qua lại giữa nhiều module nhỏ?
- Chỗ nào module **shallow**, với interface gần phức tạp bằng implementation?
- Chỗ nào các hàm thuần (pure function) được tách ra chỉ để dễ test, nhưng bug thật lại nằm ở cách chúng được gọi (không có **locality**)?
- Chỗ nào các module ghép nối chặt rò rỉ qua seam của nhau?
- Phần nào của codebase chưa có test, hoặc khó test qua interface hiện tại?

Áp dụng **phép thử xoá bỏ** (**deletion test**) cho mọi thứ bạn nghi là shallow: xoá nó đi thì độ phức tạp dồn tụ lại, hay chỉ dời chỗ? Câu trả lời "có, dồn tụ lại" là tín hiệu bạn đang tìm.

### 2. Trình bày ứng viên thành báo cáo HTML

Ghi một file HTML tự đủ vào thư mục tạm của hệ điều hành để không có gì rơi vào repo. Xác định thư mục tạm từ `$TMPDIR`, nếu không có thì dùng `/tmp` (hoặc `%TEMP%` trên Windows), và ghi ra `<tmpdir>/architecture-review-<timestamp>.html` để mỗi lần chạy có một file mới. Mở file cho user (`xdg-open <path>` trên Linux, `open <path>` trên macOS, `start <path>` trên Windows) và báo cho họ đường dẫn tuyệt đối.

Báo cáo dùng **Tailwind qua CDN** cho bố cục và styling, và **Mermaid qua CDN** cho sơ đồ ở những chỗ mà một graph/flow/sequence truyền đạt cấu trúc một cách chắc chắn. Trộn Mermaid với hình vẽ CSS/SVG làm tay: dùng Mermaid khi quan hệ có dạng đồ thị (call graph, dependency, sequence), và dùng div/SVG dựng tay khi bạn muốn thứ gì đó mang tính biên tập hơn (mass diagram, mặt cắt, hiệu ứng thu gọn). Mỗi ứng viên có một **hình minh hoạ trước/sau**. Hãy trực quan.

Với mỗi ứng viên, dựng một thẻ (card) gồm:

- **File**: những file/module liên quan
- **Vấn đề**: vì sao kiến trúc hiện tại đang gây ma sát
- **Giải pháp**: mô tả bằng lời đời thường những gì sẽ thay đổi
- **Lợi ích**: giải thích theo locality và leverage, và test sẽ tốt lên thế nào
- **Sơ đồ Trước / Sau**: đặt cạnh nhau, vẽ riêng cho trường hợp này, minh hoạ độ nông và việc làm sâu
- **Mức khuyến nghị**: một trong `Khuyến nghị mạnh` (Strong), `Đáng tìm hiểu` (Worth exploring), `Phỏng đoán` (Speculative), hiển thị dạng badge

Kết thúc báo cáo bằng mục **Khuyến nghị hàng đầu**: bạn sẽ xử lý ứng viên nào trước và vì sao.

**Dùng từ vựng của GLOSSARY.md cho domain, và từ vựng của skill `codebase-design` cho kiến trúc.** Nếu `GLOSSARY.md` định nghĩa "Order", hãy nói về "module Order intake", chứ không phải "FooBarHandler", và cũng không phải "Order service".

**Xung đột với ADR**: nếu một ứng viên đi ngược một ADR hiện có, chỉ đưa nó ra khi ma sát đủ thật để đáng xem lại ADR đó. Đánh dấu rõ trong thẻ (vd một khung cảnh báo: _"trái với ADR-0007, nhưng đáng mở lại vì…"_). Đừng liệt kê mọi refactor lý thuyết mà một ADR đã cấm.

Xem [HTML-REPORT.md](HTML-REPORT.md) để có khung HTML đầy đủ, các mẫu sơ đồ và hướng dẫn styling.

CHƯA đề xuất interface ở bước này. Sau khi ghi file xong, hỏi user: "Bạn muốn tìm hiểu kỹ ứng viên nào trong số này?"

### 3. Vòng chất vấn (grilling)

Khi user chọn một ứng viên, gọi Skill tool với "grill-me" để cùng họ đi qua cây quyết định: các ràng buộc, dependency, hình dạng của module sau khi làm sâu, những gì nằm sau seam, test nào còn giữ lại được.

Các tác động phụ diễn ra ngay tại chỗ khi quyết định dần rõ ràng; gọi Skill tool với "grill-with-docs" (phần quản lý `GLOSSARY.md` và ADR) để giữ domain model luôn cập nhật trong lúc làm:

- **Đặt tên cho module sau khi làm sâu theo một khái niệm chưa có trong `GLOSSARY.md`?** Thêm thuật ngữ đó vào `GLOSSARY.md`. Nếu file chưa tồn tại thì đến lúc này mới tạo.
- **Làm rõ một thuật ngữ còn mơ hồ trong lúc trao đổi?** Cập nhật `GLOSSARY.md` ngay lúc đó.
- **User bác bỏ ứng viên với một lý do quan trọng?** Đề nghị ghi một ADR, theo cách hỏi: _"Bạn có muốn mình ghi lại điều này thành một ADR để các lần rà kiến trúc sau không đề xuất lại nó nữa không?"_ Chỉ đề nghị khi người khám phá sau này thực sự cần lý do đó để khỏi đề xuất lại cùng một thứ; bỏ qua những lý do nhất thời ("giờ chưa đáng làm") và những lý do hiển nhiên.
- **Muốn khám phá các interface thay thế cho module sau khi làm sâu?** Gọi Skill tool với "codebase-design" và dùng mẫu sub-agent song song "design it twice" của nó.
