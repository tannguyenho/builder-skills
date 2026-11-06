# Viết agent brief

Agent brief là một bình luận có cấu trúc, đăng lên GitHub issue hoặc PR khi nó chuyển sang `ready-for-agent`. Đây là bản đặc tả có thẩm quyền mà một agent AFK sẽ làm theo. Phần thân gốc và cuộc thảo luận chỉ là ngữ cảnh: agent brief mới là hợp đồng.

Brief nêu **agent cần làm gì**, áp dụng cho cả hai loại: với issue, đó là xây thay đổi từ con số không; với PR, đó là những gì còn lại cần làm *trên diff đang có*: hoàn thiện nó, lấp chỗ hở, xử lý các góp ý review. Nguyên tắc như nhau ở cả hai; ví dụ PR bên dưới cho thấy điểm khác biệt.

## Nguyên tắc

### Bền vững hơn là chính xác

Issue có thể nằm ở `ready-for-agent` hàng ngày hoặc hàng tuần. Codebase sẽ thay đổi trong thời gian đó. Hãy viết brief sao cho nó vẫn hữu ích kể cả khi file bị đổi tên, di chuyển hay refactor.

- **Nên** mô tả interface, type và hợp đồng hành vi
- **Nên** nêu tên type, chữ ký hàm hoặc hình dạng config cụ thể mà agent cần tìm hoặc sửa
- **Không nên** nhắc đường dẫn file: chúng lỗi thời
- **Không nên** nhắc số dòng
- **Không nên** giả định cấu trúc triển khai hiện tại sẽ giữ nguyên

### Mô tả hành vi, không mô tả thủ tục

Mô tả hệ thống cần làm **gì**, không phải triển khai **thế nào**. Agent sẽ khảo sát codebase từ đầu và tự đưa ra quyết định triển khai.

- **Tốt:** "Type `SkillConfig` nên nhận thêm trường tuỳ chọn `schedule` có kiểu `CronExpression`"
- **Tệ:** "Mở src/types/skill.ts và thêm trường schedule ở dòng 42"
- **Tốt:** "Khi user chạy `/triage` không kèm tham số, họ sẽ thấy tóm tắt các issue cần chú ý"
- **Tệ:** "Thêm một câu lệnh switch vào hàm handler chính"

### Tiêu chí nghiệm thu đầy đủ

Agent cần biết khi nào là xong. Mọi agent brief phải có tiêu chí nghiệm thu cụ thể, kiểm thử được. Mỗi tiêu chí phải kiểm chứng được một cách độc lập.

- **Tốt:** "Chạy `gh issue list --label needs-triage` trả về các issue đã qua bước phân loại ban đầu"
- **Tệ:** "Triage phải chạy đúng"

### Ranh giới phạm vi rõ ràng

Nêu rõ cái gì nằm ngoài phạm vi. Điều này ngăn agent làm thừa (**gold-plating**) hoặc tự giả định về các tính năng lân cận.

## Template

```markdown
## Agent Brief

**Phân loại:** bug / enhancement
**Tóm tắt:** mô tả một dòng điều cần xảy ra

**Hành vi hiện tại:**
Mô tả những gì đang xảy ra. Với bug, đây là hành vi bị hỏng.
Với enhancement, đây là hiện trạng mà tính năng sẽ xây tiếp lên.

**Hành vi mong muốn:**
Mô tả những gì sẽ xảy ra sau khi agent làm xong.
Nêu cụ thể các trường hợp biên và tình huống lỗi.

**Interface chính:**
- `TypeName`: cần thay đổi gì và vì sao
- Kiểu trả về của `functionName()`: hiện trả về gì so với cần trả về gì
- Hình dạng config: mọi tuỳ chọn cấu hình mới cần có

**Tiêu chí nghiệm thu:**
- [ ] Tiêu chí cụ thể, kiểm thử được 1
- [ ] Tiêu chí cụ thể, kiểm thử được 2
- [ ] Tiêu chí cụ thể, kiểm thử được 3

**Ngoài phạm vi:**
- Thứ KHÔNG được thay đổi hay xử lý trong issue này
- Tính năng lân cận có vẻ liên quan nhưng là việc riêng
```

## Ví dụ

### Agent brief tốt (bug)

```markdown
## Agent Brief

**Phân loại:** bug
**Tóm tắt:** Cắt ngắn description của skill bị đứt giữa từ, tạo ra output hỏng

**Hành vi hiện tại:**
Khi description của skill vượt quá 1024 ký tự, nó bị cắt đúng tại ký tự
thứ 1024 bất kể ranh giới từ. Kết quả là description kết thúc giữa chừng
một từ (vd "Use when the user wants to confi").

**Hành vi mong muốn:**
Việc cắt phải dừng ở ranh giới từ cuối cùng trước 1024 ký tự
và thêm "..." để báo là đã bị cắt.

**Interface chính:**
- Trường `description` của type `SkillMetadata`: không cần đổi type,
  nhưng logic kiểm tra/xử lý điền giá trị cho nó phải tôn trọng
  ranh giới từ
- Mọi hàm đọc frontmatter của SKILL.md và trích ra description

**Tiêu chí nghiệm thu:**
- [ ] Description dưới 1024 ký tự giữ nguyên
- [ ] Description trên 1024 ký tự bị cắt tại ranh giới từ cuối cùng
      trước 1024 ký tự
- [ ] Description đã bị cắt kết thúc bằng "..."
- [ ] Tổng độ dài tính cả "..." không vượt quá 1024 ký tự

**Ngoài phạm vi:**
- Thay đổi chính giới hạn 1024 ký tự
- Hỗ trợ description nhiều dòng
```

### Agent brief tốt (enhancement)

```markdown
## Agent Brief

**Phân loại:** enhancement
**Tóm tắt:** Thêm hỗ trợ thư mục `.out-of-scope/` để theo dõi các yêu cầu tính năng bị từ chối

**Hành vi hiện tại:**
Khi một yêu cầu tính năng bị từ chối, issue được đóng với label `wontfix`
và một bình luận. Không có bản ghi lâu dài nào về quyết định hay lập luận.
Các yêu cầu tương tự sau này buộc maintainer phải nhớ lại hoặc đi tìm
cuộc thảo luận trước đó.

**Hành vi mong muốn:**
Yêu cầu tính năng bị từ chối được ghi lại trong các file `.out-of-scope/<concept>.md`,
lưu quyết định, lập luận và link tới mọi issue đã yêu cầu tính năng đó.
Khi triage issue mới, các file này được kiểm tra xem có khớp không.

**Interface chính:**
- Định dạng file markdown trong `.out-of-scope/`: mỗi file có một heading
  `# Tên khái niệm`, một dòng `**Quyết định:**`, một dòng `**Lý do:**`,
  và một danh sách `**Các yêu cầu trước đây:**` kèm link issue
- Quy trình triage phải đọc mọi file `.out-of-scope/*.md` từ sớm
  và so khớp issue mới với chúng theo độ tương đồng khái niệm

**Tiêu chí nghiệm thu:**
- [ ] Đóng một tính năng với wontfix sẽ tạo/cập nhật một file trong `.out-of-scope/`
- [ ] File chứa quyết định, lập luận và link tới issue đã đóng
- [ ] Nếu đã có file `.out-of-scope/` khớp, issue mới được nối vào danh sách
      "Các yêu cầu trước đây" của nó thay vì tạo file trùng
- [ ] Trong lúc triage, các file `.out-of-scope/` đang có được kiểm tra và nêu ra
      khi một issue mới khớp với một lần từ chối trước

**Ngoài phạm vi:**
- So khớp tự động (con người xác nhận việc khớp)
- Mở lại các tính năng đã từng bị từ chối
- Báo cáo bug (chỉ enhancement bị từ chối mới vào `.out-of-scope/`)
```

### Agent brief tốt (PR)

Với PR, "Hành vi hiện tại" mô tả trạng thái của diff, và brief yêu cầu agent hoàn thiện hoặc sửa nó thay vì xây từ đầu.

```markdown
## Agent Brief

**Phân loại:** enhancement
**Tóm tắt:** Hoàn thiện flag output `--json` của người đóng góp cho `triage list`

**Hành vi hiện tại:**
PR thêm flag `--json` để serialize danh sách issue ra JSON. Luồng chính chạy
được và diff khớp với cấu trúc lệnh của dự án. Còn hai chỗ hở: lỗi vẫn được
in ra dạng chữ cho người đọc (không phải JSON), và flag mới chưa có test.

**Hành vi mong muốn:**
Với `--json`, mọi output (kể cả lỗi) đều là JSON hợp lệ trên stdout,
và exit code của lệnh không đổi. Output dạng chữ cho người đọc hiện có
giữ nguyên khi không có flag.

**Interface chính:**
- Nhánh xử lý lỗi của lệnh phải xuất `{ "error": string }` khi có `--json`
  thay vì thông báo lỗi dạng chữ
- Dùng lại serializer mà PR đã thêm; không tạo thêm cái thứ hai

**Tiêu chí nghiệm thu:**
- [ ] `triage list --json` xuất JSON hợp lệ cho cả trường hợp thành công lẫn lỗi
- [ ] Exit code khớp với lệnh không dùng JSON
- [ ] Có test cho output thành công của `--json` và một trường hợp lỗi
- [ ] Output mặc định (không JSON) giống hệt từng byte như trước

**Ngoài phạm vi:**
- Thêm `--json` cho bất kỳ lệnh nào khác
- Thay đổi hình dạng JSON của payload thành công mà PR đã định nghĩa
```

### Agent brief tệ

```markdown
## Agent Brief

**Tóm tắt:** Sửa bug triage

**Cần làm:**
Cái phần triage bị hỏng rồi. Xem file chính rồi sửa đi.
Hàm quanh dòng 150 có vấn đề.

**File cần sửa:**
- src/triage/handler.ts (dòng 150)
- src/types.ts (dòng 42)
```

Brief này tệ vì:
- Không có phân loại
- Mô tả mơ hồ ("cái phần triage bị hỏng")
- Nhắc đường dẫn file và số dòng, thứ sẽ lỗi thời
- Không có tiêu chí nghiệm thu
- Không có ranh giới phạm vi
- Không mô tả hành vi hiện tại so với hành vi mong muốn
