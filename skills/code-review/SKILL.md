---
name: code-review
description: >-
  Review các thay đổi kể từ một mốc cố định (commit, branch, tag hoặc
  merge-base) theo hai trục: Standards (code có theo chuẩn code đã ghi trong
  repo không?) và Spec (code có đúng điều issue/spec gốc yêu cầu không?). Chạy
  hai review song song bằng sub-agent và báo cáo cạnh nhau. Dùng khi user muốn
  review một branch, một PR, thay đổi đang làm dở, hoặc nói "review từ X tới
  giờ", "review branch này", "review PR này", "review since X", "review this
  branch".
---

# Code Review

Review hai trục trên diff giữa `HEAD` và một mốc cố định do user đưa ra:

- **Standards** (chuẩn code): code có tuân theo các chuẩn code đã được ghi lại trong repo này không?
- **Spec** (đặc tả): code có hiện thực trung thành issue / spec gốc không?

Hai trục chạy dưới dạng **sub-agent song song** để chúng không làm bẩn context của nhau, sau đó skill này tổng hợp các phát hiện của chúng. Khởi động mọi sub-agent với một context window mới.

Issue tracker lẽ ra đã được cung cấp cho bạn. Nếu chưa, bảo user chạy `/setup-agent`.

## Quy trình

### 1. Chốt mốc cố định

Bất cứ thứ gì user nói chính là mốc cố định (một commit SHA, tên branch, tag, `main`, `HEAD~5`, v.v.). Nếu họ không nêu, hãy hỏi.

Ghi lại lệnh diff một lần: `git diff <fixed-point>...HEAD` (ba chấm, để so sánh với merge-base). Đồng thời ghi lại danh sách commit qua `git log <fixed-point>..HEAD --oneline`.

Trước khi đi tiếp, xác nhận mốc cố định resolve được (`git rev-parse <fixed-point>`) và diff không rỗng. Một ref sai hoặc diff rỗng phải fail ở đây, chứ không phải bên trong hai sub-agent song song.

### 2. Xác định nguồn spec

Tìm spec gốc theo thứ tự sau:

1. Tham chiếu issue trong commit message (`#123`, `Closes #45`, GitLab `!67`, v.v.), lấy về theo quy trình trong tài liệu tracker.
2. Một đường dẫn user truyền vào làm tham số.
3. Một file spec trong `docs/`, `specs/`, hoặc `.scratch/` khớp với tên branch hoặc tính năng.
4. Nếu không tìm thấy gì, hỏi user spec ở đâu. Nếu họ nói không có, sub-agent **Spec** sẽ bỏ qua và báo "không có spec".

### 3. Xác định nguồn chuẩn code

Tìm trong repo mọi file ghi lại cách viết code. Khi có `CODING_STANDARDS.md` hoặc `CONTRIBUTING.md`, file đó bắt buộc phải nằm trong danh sách.

Ngoài những gì repo ghi lại, trục Standards luôn mang theo **bộ smell nền** (**smell baseline**) bên dưới: một tập cố định các code smell của Fowler (_Refactoring_, chương 3), áp dụng cả khi repo không ghi lại chuẩn nào. Hai quy tắc ràng buộc bộ này:

- **Repo được ưu tiên.** Một chuẩn đã ghi lại của repo luôn thắng; chỗ nào repo chấp nhận một điều mà bộ nền sẽ đánh dấu, hãy bỏ qua smell đó.
- **Luôn là phán đoán.** Mỗi smell là một heuristic có gắn nhãn ("có thể là Feature Envy"), không bao giờ là vi phạm cứng. Như mọi chuẩn khác ở đây, bỏ qua bất cứ thứ gì tooling đã cưỡng chế.

Mỗi smell đọc theo dạng *nó là gì* → *cách sửa*; đối chiếu với diff:

- **Mysterious Name** (tên bí ẩn): một hàm, biến hoặc type mà tên không cho thấy nó làm gì hay chứa gì. → đổi tên; nếu không nghĩ ra được tên trung thực, thiết kế đang mù mờ.
- **Duplicated Code** (code trùng lặp): cùng một hình dạng logic xuất hiện ở nhiều hunk hoặc nhiều file trong thay đổi. → tách hình dạng chung ra, gọi nó từ cả hai nơi.
- **Feature Envy** (thèm tính năng nhà khác): một method thò vào dữ liệu của object khác nhiều hơn dữ liệu của chính nó. → chuyển method sang chỗ dữ liệu mà nó thèm.
- **Data Clumps** (cụm dữ liệu): cùng vài field hoặc param cứ đi cùng nhau (một type đang chờ được sinh ra). → gói chúng thành một type, truyền type đó.
- **Primitive Obsession** (ám ảnh kiểu nguyên thuỷ): một primitive hoặc string đứng thay cho một khái niệm domain đáng có type riêng. → cho khái niệm đó một type nhỏ riêng.
- **Repeated Switches** (switch lặp lại): cùng một `switch`/chuỗi `if` trên cùng một type xuất hiện lặp lại trong thay đổi. → thay bằng đa hình (polymorphism), hoặc một map dùng chung cho cả hai chỗ.
- **Shotgun Surgery** (phẫu thuật súng hoa cải): một thay đổi logic buộc phải sửa rải rác nhiều file trong diff. → gom những gì thay đổi cùng nhau vào một module.
- **Divergent Change** (thay đổi phân kỳ): một file hoặc module bị sửa vì nhiều lý do không liên quan. → tách ra để mỗi module chỉ thay đổi vì một lý do.
- **Speculative Generality** (tổng quát hoá phỏng đoán): abstraction, tham số hoặc hook được thêm cho những nhu cầu mà spec không có. → xoá nó; inline lại cho tới khi nhu cầu thật xuất hiện.
- **Message Chains** (chuỗi lời gọi): đường đi dài kiểu `a.b().c().d()` mà bên gọi lẽ ra không nên phụ thuộc. → giấu đường đi đó sau một method trên object đầu tiên.
- **Middle Man** (người trung gian): một class hoặc hàm hầu như chỉ chuyển tiếp lời gọi. → cắt bỏ nó, gọi thẳng tới đích thật.
- **Refused Bequest** (từ chối di sản): một subclass hoặc implementer bỏ qua hoặc override phần lớn những gì nó kế thừa. → bỏ kế thừa, dùng composition.

### 4. Tạo cả hai sub-agent song song

Gọi cả hai sub-agent cùng lúc, ở foreground, và tổng hợp các báo cáo chúng trả về.

**Prompt cho sub-agent Standards** cần có:

- Lệnh diff đầy đủ và danh sách commit.
- Danh sách các file nguồn chuẩn code bạn tìm được ở bước 3, **cộng với bộ smell nền ở bước 3** dán nguyên văn đầy đủ (sub-agent không có cách nào khác để biết nó).
- Yêu cầu: "Báo cáo, theo từng file/hunk khi phù hợp, (a) mọi chỗ diff vi phạm một chuẩn đã ghi lại: dẫn nguồn chuẩn (file + quy tắc); và (b) mọi smell trong bộ nền mà bạn phát hiện: gọi tên nó và trích hunk. Phân biệt vi phạm cứng với phán đoán: vi phạm chuẩn đã ghi lại có thể là cứng, nhưng smell trong bộ nền luôn là phán đoán, và chuẩn đã ghi lại của repo được ưu tiên hơn bộ nền. Bỏ qua bất cứ thứ gì tooling đã cưỡng chế. Dưới 400 từ."

**Prompt cho sub-agent Spec** cần có:

- Lệnh diff và danh sách commit.
- Đường dẫn hoặc nội dung đã lấy về của spec.
- Yêu cầu: "Báo cáo: (a) các yêu cầu spec đưa ra mà còn thiếu hoặc mới làm một phần; (b) hành vi trong diff không được yêu cầu (phình phạm vi — scope creep); (c) các yêu cầu trông như đã được hiện thực nhưng cách hiện thực có vẻ sai. Trích dòng spec cho mỗi phát hiện. Dưới 400 từ."

Nếu không có spec, bỏ qua sub-agent Spec và ghi chú điều này trong báo cáo cuối.

### 5. Tổng hợp

Trình bày hai báo cáo dưới các heading `## Standards (chuẩn code)` và `## Spec (đặc tả)`, giữ nguyên văn hoặc chỉnh sửa nhẹ. **Không** gộp hay xếp hạng lại các phát hiện, vì hai trục được tách riêng có chủ đích (xem _Vì sao hai trục_).

Kết thúc bằng một dòng tóm tắt: tổng số phát hiện theo từng trục, và vấn đề nặng nhất _trong mỗi trục_ (nếu có). Đừng chọn một vấn đề nặng nhất chung cho cả hai trục: đó chính là kiểu xếp hạng lại mà việc tách trục muốn ngăn chặn.

## Vì sao hai trục

Một thay đổi có thể đạt trục này nhưng trượt trục kia:

- Code theo đúng mọi chuẩn nhưng hiện thực sai thứ → **Standards đạt, Spec trượt.**
- Code làm đúng chính xác điều issue yêu cầu nhưng phá vỡ quy ước của dự án → **Spec đạt, Standards trượt.**

Báo cáo riêng hai trục giúp trục này không che lấp trục kia.
