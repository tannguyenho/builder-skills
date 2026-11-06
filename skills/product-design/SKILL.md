---
name: product-design
description: >-
  Thiết kế, thẩm định và lên kế hoạch cho một startup/sản phẩm mới từ con số 0:
  nghiên cứu thị trường, phân tích đối thủ, mô hình kinh doanh, nhận diện thương hiệu,
  định nghĩa sản phẩm (MVP), dự phóng tài chính và thí nghiệm thẩm định. Dùng khi user
  có ý tưởng startup muốn khám phá, muốn thẩm định một ý tưởng kinh doanh, cần business
  plan hoặc Lean Canvas, hỏi về quy mô thị trường hay bức tranh cạnh tranh, muốn định vị
  thương hiệu hoặc chiến lược go-to-market. Ví dụ: "mình có ý tưởng làm...", "ý tưởng này
  có đáng làm không", "thẩm định giúp mình ý tưởng startup", "làm lean canvas",
  "I have an idea for...", "is this idea worth pursuing", "validate my startup idea".
  Cũng dùng để làm tiếp từ checkpoint của phiên trước (PROGRESS.md).
---

# Product Design — thiết kế & thẩm định startup

Một skill nhiều phase, có cấu trúc, đưa ý tưởng startup từ khái niệm thô đến một bản thiết kế đã được thẩm định. Skill tạo ra trọn bộ tài liệu markdown sắp xếp theo từng mảng, có sẵn cơ chế theo dõi tiến độ để công việc không bị mất khi phiên làm việc bị ngắt.

## Cách hoạt động

Quy trình gồm 8 phase đánh số chạy tuần tự, cộng thêm bước Kiểm tra sơ bộ (**Pre-Flight Check**, Phase 0.5) và một cổng Khám phá khách hàng (**Customer Discovery**, Phase 3.7). Mỗi phase tạo ra file đầu ra và cập nhật file theo dõi tiến độ. Nếu phiên bị ngắt, làm tiếp từ checkpoint cuối cùng đã hoàn thành.

```
PRE-FLIGHT → INTAKE → BRAINSTORM → RESEARCH → [Research Gate] → CUSTOMER DISCOVERY → [Interview Gate] → STRATEGY → BRAND → PRODUCT → FINANCIAL → VALIDATION
```

### Chế độ

**Full Mode (mặc định):** Chạy mọi phase theo thứ tự, gồm cả Pre-Flight và Customer Discovery. Phù hợp nhất khi muốn thiết kế startup thật kỹ từ đầu.

**Fast Track Mode:** Khi user nói muốn "thẩm định nhanh", "đánh giá nhanh" ("quick validation", "rapid assessment") hoặc tương tự, hoặc khi rõ ràng là thời gian/ngân sách có hạn, chạy bản rút gọn:
1. Phase 0.5 (Pre-Flight Check) — luôn chạy, mất 5 phút
2. Phase 1 (Intake) — rút xuống 1 vòng câu hỏi; ghi lại mọi cuộc trò chuyện với khách hàng mà founder đã có trước đó
3. Phase 2 (Brainstorm) — 3 biến thể thay vì 5-8
4. Phase 3 (Research) — chỉ Wave 1 + Wave 2 (bỏ phần đào sâu tiếng nói khách hàng và phân phối)
5. Phase 3.5 (Research Gate) — checkpoint go/no-go
6. Phase 3.7 (Customer Discovery) — nếu founder đã có 5+ cuộc trò chuyện trước đó thì ghi lại; nếu chưa, chạy ít nhất 3 cuộc phỏng vấn trước khi đi tiếp
7. Phase 4 (Strategy) — chỉ Lean Canvas
8. Bỏ Phase 5 (Brand) và Phase 6 (Product)
9. Phase 7 (Financial) — chỉ mô hình doanh thu, Stage A (dựa trên giả định), không làm dự phóng đầy đủ
10. Phase 8 (Validation) — chỉ Scorecard + 3 thí nghiệm hàng đầu

Fast Track tạo ra ít file hơn nhưng vẫn cho founder một tín hiệu go/no-go rõ ràng, có bằng chứng. Ghi chú trong PROGRESS.md là đã dùng Fast Track mode, để phiên sau có thể mở rộng sang full mode nếu ý tưởng qua được bước thẩm định.

### Ngôn ngữ

Ngôn ngữ đầu ra mặc định là **tiếng Việt**. Nếu user viết bằng ngôn ngữ khác hoặc yêu cầu rõ một ngôn ngữ, dùng ngôn ngữ đó cho toàn bộ đầu ra.

---

> **Tham khảo:** Đọc `references/output-guidelines.md` một lần lúc bắt đầu. File này định nghĩa header/footer chuẩn cho mỗi file (tiêu đề, ngày, phase, độ tin cậy, cờ cảnh báo), cách tham chiếu chéo giữa các phase, ví dụ đầu ra tốt và kém, và cách xử lý khi pivot giữa chừng.

## Phase 0: Kiểm tra để làm tiếp (Resume Check)

Trước mọi việc khác, kiểm tra xem có file `PROGRESS.md` trong thư mục làm việc (hoặc thư mục con của dự án) không. Nếu có, đọc nó và làm tiếp từ phase dở dang gần nhất. Nói với user: "Mình tìm thấy tiến độ từ phiên trước. Bạn đã xong [các phase]. Giờ làm tiếp từ [phase tiếp theo]."

Nếu không có file tiến độ, bắt đầu từ Phase 1.

---

## Phase 0.5: Kiểm tra sơ bộ (Pre-Flight Check)

Trước khi đầu tư thời gian vào toàn bộ quy trình, chạy một bước kiểm tra nhanh — 2-3 lượt tìm kiếm có mục tiêu, tối đa 5 phút. Mục đích là phát hiện ngay những tín hiệu loại trừ để founder biết từ đầu.

**Chạy ba bước kiểm tra sau:**

**1. Kiểm tra giải pháp thống trị** — Đã có giải pháp được đầu tư mạnh, được dùng rộng rãi cho đúng vấn đề này chưa? Tìm: `"{problem domain} software"`, `"{problem} tool site:producthunt.com"`, `"{problem} app reviews"`. Nếu có một người dẫn đầu thị trường rõ ràng với 10k+ khách hàng, gắn cờ ngay — đây không phải lý do để dừng, nhưng founder cần biết thực tế cạnh tranh trước khi bắt đầu.

**2. Kiểm tra tiền lệ thất bại** — Đã có công ty nào thử đúng ý tưởng này và thất bại công khai chưa? Tìm: `"{startup idea} startup failed"`, `"{problem} startup shutdown"`, `"why {product category} failed"`. Thất bại trước đó không phải lý do loại bỏ — đó là bài học. Nhưng những thất bại trước đó mà mình không biết thì là bãi mìn.

**3. Rào cản pháp lý "chết ngay"** — Có lý do pháp lý hiển nhiên nào khiến ý tưởng này không thể tồn tại không? (Vd quy định tài chính cụ thể, luật bảo vệ dữ liệu ở khu vực mục tiêu, yêu cầu giấy phép.) Một lượt tìm nhanh giúp tránh việc cắm đầu xây về phía bức tường.

**Đầu ra:** Một tin nhắn ngắn cho founder (tối đa 3-5 gạch đầu dòng) về những gì tìm được. Dùng định dạng sau:

```
## Kiểm tra sơ bộ (Pre-Flight Check)

✅ Không thấy đối thủ thống trị — thị trường có vẻ còn mở.
⚠️  [CompanyX] đã thử cách tương tự năm 2021 và đóng cửa năm 2023.
    Lý do chính: [một câu]. Nên tìm hiểu trước khi đi tiếp.
✅ Chưa thấy rào cản pháp lý rõ ràng nào cho [thị trường mục tiêu].

→ Sẵn sàng chuyển sang intake. Những điều trên là bối cảnh, không phải phán quyết.
```

Giữ thật ngắn. Đây là lời báo trước, không phải phân tích đầy đủ. Lúc này thư mục dự án và PROGRESS.md chưa tồn tại — trình bày kết quả trong cuộc trò chuyện, rồi lưu vào `{project-name}/00-intake/preflight.md` ở bước đầu ra của Phase 1, khi thư mục dự án đã được tạo.

---

## Phase 1: Phỏng vấn đầu vào (Intake Interview)

Chất lượng của mọi thứ phía sau phụ thuộc vào lượng bối cảnh bạn khai thác được lúc này. Đừng vội — một buổi intake kỹ lưỡng tiết kiệm hàng giờ đi sai hướng về sau.

> **Tham khảo:** Đọc `references/intake-questions.md` để có bộ câu hỏi đầy đủ (ý tưởng, founder, thị trường, kinh doanh, ràng buộc), các câu hỏi khó giúp lộ ra điểm mù, và kỹ thuật phỏng vấn.

Phủ đủ cả năm nhóm câu hỏi cộng với các câu hỏi khó — chúng đặt tông cho toàn bộ quy trình và cho thấy đây là một đánh giá trung thực, không phải buổi cổ vũ. Hỏi 3-5 câu mỗi lần theo mạch trò chuyện, hỏi sâu khi câu trả lời còn mơ hồ, và sau 2-3 vòng thì tóm tắt những gì bạn đã hiểu rồi nhờ user xác nhận hoặc sửa.

### Đầu ra

Lưu bản intake đã tổng hợp vào `{project-name}/00-intake/brief.md`, với mọi thông tin thu được được sắp xếp rõ ràng. Tên dự án lấy từ ý tưởng startup (kebab-case, vd `pet-health-tracker`).

Tạo `PROGRESS.md` ở thư mục gốc dự án, gồm: tên dự án, ngày bắt đầu, ngôn ngữ, checklist mọi phase kể cả Pre-Flight (0.5) và Customer Discovery (3.7) — đánh dấu Pre-Flight và Phase 1 đã xong — và một mục Ghi chú (Notes) cho trạng thái phiên. Đồng thời lưu kết quả Pre-Flight từ Phase 0.5 vào `00-intake/preflight.md` vì giờ thư mục đã tồn tại.

---

## Phase 2: Brainstorm

Trước khi lao vào nghiên cứu, hãy khám phá không gian ý tưởng. Việc này giúp tránh hội tụ quá sớm vào phiên bản đầu tiên của ý tưởng.

### Quy trình

1. **Mở rộng (Diverge)** — Tạo 5-8 biến thể của ý tưởng cốt lõi. Đẩy ranh giới:
   - Nếu thị trường mục tiêu hoàn toàn khác thì sao?
   - Nếu mô hình kinh doanh bị đảo ngược thì sao?
   - Nếu giải một phiên bản nhỏ hơn/lớn hơn của vấn đề thì sao?
   - Có vấn đề lân cận nào có thể giải thay thế không?
   - "Phiên bản 10x" trông thế nào so với "phiên bản đơn giản nhất có thể"?

2. **Phân tích (Analyze)** — Với mỗi biến thể, ghi lại:
   - Điều gì hấp dẫn ở nó
   - Điều gì rủi ro hoặc khó
   - Nó thay đổi bức tranh cạnh tranh ra sao

3. **Hội tụ (Converge)** — Trình bày các biến thể cho user. Giúp họ xác định yếu tố nào chạm đến họ. Mục tiêu không phải chọn một biến thể — mà là làm giàu ý tưởng gốc bằng những insight từ việc khám phá.

4. **Tinh chỉnh (Refine)** — Dựa trên phản hồi của user, chốt lại ý tưởng đã tinh chỉnh. Cập nhật brief nếu ý tưởng thay đổi đáng kể.

### Đầu ra

Lưu vào `{project-name}/00-intake/brainstorm.md`. Cập nhật PROGRESS.md.

---

## Phase 2.5: Đánh giá độ sâu nghiên cứu (Research Depth Assessment)

Sau intake (và brainstorm nếu có), đánh giá độ phức tạp của thị trường và trình bày đề xuất Độ sâu nghiên cứu (**Research Depth**) cho user.

> **Tham khảo:** Đọc `references/research-scaling.md` để có ma trận chấm điểm độ phức tạp, định nghĩa các tier, cấu hình wave, và mẫu trao đổi với user.

### Quy trình

1. Chấm ba yếu tố từ intake: độ rộng thị trường (1-3), số đối thủ đã biết (1-3), phạm vi địa lý (1-3)
2. Cộng điểm (khoảng 3-9) và quy ra tier: Light (3-4), Standard (5-7), Deep (8-9)
3. Trình bày bảng Research Depth cho user (xem `research-scaling.md` để có mẫu chính xác)
4. Chờ user trả lời: **light**, **deep**, hoặc **ok** để chấp nhận đề xuất
5. Ghi tier đã chọn vào PROGRESS.md

Tier được chọn quyết định số agent mỗi wave và số vòng tìm kiếm mỗi agent ở Phase 3. Xem `research-scaling.md` để có cấu hình wave chính xác cho từng tier.

---

## Phase 3: Nghiên cứu thị trường (Market Research)

Đây là phase tốn tài nguyên nhất. Nó dùng 4 wave nghiên cứu web chạy tuần tự, wave sau xây trên kết quả của wave trước.

### Nhận diện môi trường

Kiểm tra xem tool `Agent` có sẵn không (Claude Code) hay không (Claude.ai, môi trường khác):

- **Có tool Agent:** Tạo subagent chạy song song trong mỗi wave, như mô tả bên dưới. Cách này nhanh hơn (~3-5 phút mỗi wave).
- **KHÔNG có tool Agent (Claude.ai, web):** Tự thực hiện nghiên cứu, tuần tự. Với mỗi wave, theo đúng các template agent trong file tham khảo, nhưng chạy từng lượt tìm kiếm một trong cuộc trò chuyện chính. Phủ cùng các chủ đề và áp dụng cùng nguyên tắc nghiên cứu — chất lượng đầu ra phải như nhau, chỉ là lâu hơn. KHÔNG được bỏ wave nào hay giảm độ sâu tìm kiếm vì chạy tuần tự.

### Khả năng tìm kiếm web

Phase 3 cần WebSearch. Trong Claude Code, tool này luôn có — nếu user chưa cho phép trước, hệ thống sẽ hỏi họ ở mỗi lượt tìm. Nếu user từ chối, hoặc ở môi trường hoàn toàn không có WebSearch, chuyển sang **Chế độ nghiên cứu dựa trên kiến thức (Knowledge-Based Research Mode)**: dùng dữ liệu huấn luyện của bạn, đánh dấu rõ mọi phát hiện bằng **[Knowledge-Based — not live data, verify independently]** (dựa trên kiến thức — không phải dữ liệu trực tiếp, cần tự kiểm chứng), hạ mức độ tin cậy xuống một bậc, và khuyên founder tự kiểm chứng các khẳng định quan trọng. Ghi chế độ này vào PROGRESS.md để phiên sau biết nghiên cứu không lấy từ web.

> **Tham khảo** — Đọc file tương ứng cho từng wave:
> - `references/research-principles.md` — Quy tắc xuyên suốt (chất lượng nguồn, đối chiếu chéo, định lượng, xử lý khi tìm kiếm thất bại). Đọc file này TRƯỚC TIÊN.
> - `references/research-wave-1-market.md` — Template agent cho Wave 1 (quy mô thị trường, xu hướng, pháp lý)
> - `references/research-wave-2-competitors.md` — Template agent cho Wave 2 (đối thủ trực tiếp, gián tiếp, phân tích GTM)
> - `references/research-wave-3-customers.md` — Template agent cho Wave 3 (tiếng nói khách hàng, nhu cầu, đối tượng)
> - `references/research-wave-4-distribution.md` — Template agent cho Wave 4 (kênh phân phối, thâm nhập theo địa lý)
> - `references/research-synthesis.md` — Cách tổng hợp phát hiện thô thành sản phẩm bàn giao cuối cùng
>
> Chỉ đọc file nguyên tắc + file của wave đang chạy. Đừng nạp tất cả file wave cùng lúc.

### Nguyên tắc nghiên cứu

- Mỗi agent thực hiện **tối thiểu 5-8 lượt tìm kiếm web**, mỗi vòng đào sâu hơn
- Đối chiếu chéo mọi phát hiện quan trọng qua 2-3 nguồn độc lập
- Xếp hạng chất lượng nguồn (Tier 1: báo cáo của hãng phân tích, Tier 2: báo công nghệ, Tier 3: blog/mạng xã hội)
- Định lượng mọi thứ — "$4.2B với CAGR 12.3%" chứ không phải "thị trường đang tăng trưởng"
- Ghi ngày cho mọi dữ liệu và gắn cờ những gì cũ hơn 18 tháng
- Ghi nhận mâu thuẫn giữa các nguồn thay vì chọn một

### Các wave nghiên cứu

Brief đầy đủ của agent, chiến lược tìm kiếm và nơi lưu đầu ra nằm trong các file tham khảo của từng wave — đọc file tương ứng khi tạo mỗi wave:

- **Wave 1: Bức tranh thị trường** (3 agent) — A1 Quy mô thị trường & kinh tế học, A2 Xu hướng ngành & thời điểm, A3 Pháp lý & tuân thủ *(bỏ A3 nếu không có rủi ro pháp lý)*
- **Wave 2: Phân tích cạnh tranh** (3 agent) — B1 Đào sâu đối thủ trực tiếp, B2 Đối thủ gián tiếp & sản phẩm thay thế, B3 Go-to-Market của đối thủ
- **Wave 3: Khách hàng & nhu cầu** (3 agent) — C1 Tiếng nói khách hàng & nỗi đau, C2 Tín hiệu nhu cầu & thẩm định thị trường, C3 Phác hoạ đối tượng mục tiêu
- **Wave 4: Phân phối & đối tác** (2 agent) — D1 Kênh phân phối, D2 Địa lý & thâm nhập thị trường

Mỗi wave phải xong trước khi wave sau bắt đầu. Chuyển các phát hiện chính sang làm bối cảnh (phát hiện Wave 1 cho agent Wave 2, danh sách đối thủ và phát hiện GTM cho Wave 3, v.v.). Các agent chạy song song trong một wave, hoặc thành các khối nghiên cứu tuần tự nếu không có tool Agent.

### Thô → Tổng hợp

Mọi agent lưu phát hiện thô vào `{project-name}/01-discovery/raw/`. Sau khi mọi wave xong, tổng hợp thành 4 sản phẩm bàn giao hoàn chỉnh.

Tổng hợp là suy luận, không phải định dạng — đây là nơi nghiên cứu thô trở thành quyết định. Trước khi viết gì, hãy nghĩ thật kỹ xem các mảnh ghép khớp với nhau thế nào: nguồn nào mâu thuẫn và nên tin nguồn nào, bằng chứng thực sự ủng hộ điều gì so với điều founder mong muốn, và tất cả có ý nghĩa gì với *chính* startup này. Đây là phần tư duy có đòn bẩy cao nhất trong toàn bộ quy trình và mọi phase phía sau đều thừa hưởng chất lượng của nó, nên nếu model hỗ trợ extended thinking thì đây là chỗ nên dùng. Một bản tổng hợp yếu tạo ra tài liệu gọn gàng chỉ nhắc lại đầu vào; một bản tổng hợp mạnh đi đến những kết luận không hiển nhiên mà một nhà phân tích sắc sảo sẽ rút ra từ cùng bằng chứng.

Bản tổng hợp phải:
- Nối các điểm giữa các mảng nghiên cứu (khoảng trống cạnh tranh → nỗi đau khách hàng → cơ hội định vị)
- Làm nổi bật mâu thuẫn và giải thích nên tin dữ liệu nào
- Đánh giá độ tin cậy cho từng khẳng định chính (Cao / Trung bình / Thấp)
- Rút ra hàm ý chiến lược rõ ràng, không chỉ liệt kê sự kiện

### File đầu ra

- `{project-name}/01-discovery/market-analysis.md` — Quy mô thị trường (TAM/SAM/SOM), tăng trưởng, độ trưởng thành, tóm tắt pháp lý, đánh giá thời điểm
- `{project-name}/01-discovery/competitor-landscape.md` — Hồ sơ đối thủ, **ma trận so sánh có cấu trúc** (bảng với các cột: Tên, Sản phẩm, Giá, Đối tượng, Vốn gọi được, Traction, Điểm mạnh chính, Điểm yếu chính), bản đồ định vị, rủi ro nền tảng, phân tích điểm yếu dễ tấn công
- `{project-name}/01-discovery/target-audience.md` — Persona, thứ bậc nỗi đau, jobs-to-be-done, bản đồ ngôn ngữ, hành vi mua, kênh
- `{project-name}/01-discovery/industry-trends.md` — Xu hướng công nghệ, tín hiệu đầu tư, chuyển dịch hành vi, quỹ đạo pháp lý, hàm ý chiến lược
- `{project-name}/01-discovery/confidence-dashboard.md` — Tóm tắt chất lượng dữ liệu của toàn bộ nghiên cứu. Với mỗi khẳng định chính, liệt kê: khẳng định, tier của nguồn (1/2/3), số nguồn xác nhận, mức độ tin cậy (Cao/Trung bình/Thấp), và tuổi dữ liệu. Nó cho founder biết họ đang đứng trên nền vững hay trên lớp băng mỏng.

Cập nhật PROGRESS.md.

---

## Phase 3.5a: Kiểm chứng nghiên cứu (Research Verification)

Sau khi tổng hợp xong và mọi file bàn giao đã được viết, chạy một lượt kiểm chứng để bắt các điểm không nhất quán.

> **Tham khảo:** Đọc `references/verification-agent.md` để có quy trình kiểm chứng đầy đủ, các bước kiểm tra chung và kiểm tra riêng cho skill.

### Quy trình

1. Tạo agent **V1: Verification** — agent này đọc mọi file bàn giao trong `01-discovery/` và kiểm tra: khẳng định chưa gắn nhãn, mâu thuẫn nội bộ, độ nhất quán của mức độ tin cậy, khoảng trống dữ liệu bị bỏ sót, thiếu cờ cảnh báo, dữ liệu cũ, và xác nhận giả do trùng nguồn
2. V1 cũng chạy các bước kiểm tra riêng của product-design: tính nhất quán giữa các phase (chiến lược phản ánh dữ liệu thị trường, sản phẩm phản ánh nỗi đau khách hàng, tài chính phản ánh mô hình kinh doanh, thẩm định bao phủ các rủi ro đã xác định)
3. V1 tạo ra `{project-name}/01-discovery/verification-report.md`
4. **Nếu có vấn đề Critical:** Dừng lại và trình bày vấn đề cho user. Hỏi: sửa trước, hay đi tiếp như hiện tại?
5. **Nếu chỉ có Warning/Info:** Hiện tóm tắt một dòng rồi đi tiếp tới Research Gate

Trên Claude.ai hoặc khi không có tool Agent, tự chạy các bước kiểm chứng trong cuộc trò chuyện chính theo đúng quy trình.

---

## Phase 3.5: Research Gate (checkpoint Go/No-Go)

Trước khi đầu tư thời gian từ Strategy đến Validation, dừng lại và trình bày cho founder một đánh giá trung thực dựa trên kết quả nghiên cứu. Đây là điểm ra quyết định, không phải thủ tục.

Suy luận kỹ trước khi viết kết luận. Cân những tín hiệu mạnh nhất với các cờ đỏ thay vì lấy trung bình thành một câu "còn tuỳ" chung chung — một lỗi chí mạng có thể nặng hơn năm tín hiệu hứa hẹn, và một tín hiệu đặc biệt xuất sắc có thể đủ lý do đi tiếp dù còn vài chỗ thô. Founder sắp bỏ thời gian và tiền thật dựa trên cách bạn đọc bằng chứng, nên hãy nghĩ thật kỹ xem dữ liệu thực sự ủng hộ điều gì.

Trình bày một bản tóm tắt ngắn: "Đây là những gì nghiên cứu tìm được." Bao gồm quy mô thị trường, mức độ cạnh tranh, tín hiệu nhu cầu khách hàng, và thời điểm. Sau đó đưa ra khuyến nghị rõ ràng:
- **Đèn xanh** — Dữ liệu ủng hộ việc đi tiếp. Nêu các tín hiệu mạnh nhất.
- **Đèn vàng** — Tín hiệu lẫn lộn. Chỉ rõ điều gì đáng lo và điều gì cần đúng thì mới thành công.
- **Đèn đỏ** — Dữ liệu phản đối hướng đi này. Gợi ý pivot nếu nghiên cứu cho thấy cơ hội lân cận.

Hỏi founder: "Dựa trên kết quả này, bạn muốn đi tiếp sang chiến lược đầy đủ, pivot ý tưởng, hay dừng ở đây?" Tôn trọng quyết định của họ, nhưng đảm bảo đó là quyết định có đủ thông tin. Lưu đánh giá của cổng này vào `{project-name}/01-discovery/research-gate.md`.

---

## Phase 3.7: Khám phá khách hàng — Phỏng vấn (Customer Discovery)

Nghiên cứu cho biết thị trường trông thế nào từ bên ngoài. Phỏng vấn khách hàng cho biết vấn đề được cảm nhận thế nào từ bên trong. Đây là bước thẩm định cho tín hiệu mạnh nhất trong toàn bộ quy trình — và là bước duy nhất cần thời gian thực trên lịch (thường 1-2 tuần).

> **Tham khảo:** Đọc `references/customer-interview.md` để có quy trình phỏng vấn đầy đủ, cấu trúc câu hỏi, mẫu ghi chép và hướng dẫn tổng hợp.

### Khi nào chạy phase này

Chạy phase này sau khi Research Gate bật đèn xanh hoặc vàng cho ý tưởng. Nếu cổng trả về đèn đỏ và founder chọn dừng, bỏ qua phase này.

Vì phỏng vấn làm gián đoạn mạch làm việc của phiên, đưa cho founder một lựa chọn rõ ràng:

- **Phỏng vấn ngay (khuyến nghị)** — dừng ở đây, thực hiện phỏng vấn trong những ngày tới, rồi làm tiếp từ checkpoint này (PROGRESS.md giữ trạng thái).
- **Hoãn lại và đi tiếp** — chuyển sang Strategy chỉ với dữ liệu nghiên cứu. Nói thẳng hệ quả: dự phóng tài chính giữ ở Stage A (dựa trên giả định), Bảng đánh giá cuối (Final Assessment Dashboard) sẽ hiện "Phỏng vấn khách hàng: 0 cuộc · đã hoãn", và phỏng vấn trở thành thí nghiệm #1 trong validation playbook ở Phase 8. Một chiến lược xây dựng mà không tiếp xúc khách hàng là giả thuyết, không phải hướng đi đã được thẩm định — nói điều này thẳng thắn, rồi tôn trọng quyết định của founder mà không nhắc đi nhắc lại.

**Ngoại lệ — Fast Track Mode:** Nếu founder báo đã có 5+ cuộc trò chuyện với khách hàng trong intake, ghi lại các cuộc trò chuyện đó theo mẫu phỏng vấn và đi tiếp. Gắn cờ mọi khẳng định là `[Founder-reported]`. Nếu ít hơn 5 cuộc, khuyên chạy phỏng vấn mới — tối thiểu 5 ở Full Mode, tối thiểu 3 ở Fast Track.

### Quy trình

1. **Xác định người cần phỏng vấn** — Dùng persona chính từ `01-discovery/target-audience.md`, định nghĩa chính xác chân dung. Tối thiểu 5 cuộc phỏng vấn.
2. **Thực hiện phỏng vấn** — Theo quy trình trong `references/customer-interview.md`. Nhắm 25-30 phút mỗi cuộc, tập trung vào vấn đề, không chào hàng sản phẩm.
3. **Ghi chép từng cuộc phỏng vấn** — Lưu vào `{project-name}/00-intake/interviews/interview-{N}.md` theo mẫu trong file tham khảo.
4. **Tổng hợp** — Sau mọi cuộc phỏng vấn, viết `{project-name}/00-intake/interview-synthesis.md` gồm: tỉ lệ xác nhận vấn đề, tín hiệu hành vi (ai đã trả tiền/tự chế cách xoay xở), các cụm từ then chốt, và rà soát giả định.

### Interview Gate: Đi tiếp hay Đánh giá lại

Sau khi tổng hợp, trình bày phát hiện ngắn gọn cho founder và áp dụng cổng này:

**Đi tiếp sang Phase 4 nếu:**
- 4+ trên 5 người được phỏng vấn xác nhận vấn đề cốt lõi rõ ràng mà không cần gợi ý
- Ít nhất 2 người có tín hiệu hành vi (đã trả tiền cho thứ gì đó, đã tự chế cách xoay xở, đã chủ động tìm kiếm)
- Ngôn ngữ mô tả vấn đề nhất quán giữa các cuộc phỏng vấn

**Dừng lại và đánh giá lại nếu:**
- 3 hoặc ít hơn trên 5 người xác nhận vấn đề (quy đổi theo tỉ lệ nếu phỏng vấn nhiều hơn)
- Ai cũng nói "hay đấy" nhưng không có tín hiệu hành vi nào
- Vấn đề họ mô tả không khớp với giải pháp đề xuất

Trình bày bản tổng hợp và kết quả cổng cho founder. Nếu kết quả là cần đánh giá lại, gợi ý pivot cụ thể nếu các cuộc phỏng vấn chỉ ra một vấn đề lân cận đáng giải. Để founder quyết định: pivot ý tưởng, thu hẹp đối tượng, hay dừng.

Cập nhật PROGRESS.md với kết quả Interview Gate.

---

## Phase 4: Chiến lược (Strategy)

Có nghiên cứu trong tay rồi, giờ định nghĩa nền tảng chiến lược. Mỗi tài liệu cần tham chiếu phát hiện cụ thể từ Phase 3 — chiến lược tách rời khỏi nghiên cứu chỉ là đoán mò.

> **Tham khảo:** Đọc `references/frameworks.md` để có định nghĩa chuẩn của Lean Canvas, Positioning theo April Dunford, Value Proposition Canvas, và RICE/MoSCoW. Đọc `references/output-specs.md` (mục Phase 4) để biết cấu trúc bắt buộc của từng file.

Tạo trong `02-strategy/`:
- `lean-canvas.md` — Lean Canvas đầy đủ 9 ô
- `value-proposition.md` — value proposition canvas (jobs, pains, gains), tuyên bố giá trị một câu, bằng chứng (proof points)
- `business-model.md` — mô hình doanh thu, unit economics, khả năng mở rộng, phụ thuộc và đối tác
- `positioning.md` — năm thành phần của April Dunford
- `go-to-market.md` — chiến lược ra mắt, kế hoạch 100 khách hàng đầu tiên, các kênh tăng trưởng đã xếp hạng, cột mốc

Cập nhật PROGRESS.md.

---

## Phase 5: Thương hiệu (Brand)

> **Checkpoint:** Trước khi bắt đầu, trình bày ngắn gọn tóm tắt chiến lược cho founder: định vị, thị trường mục tiêu, mô hình kinh doanh. Hỏi: "Như vậy đã đúng tầm nhìn của bạn chưa? Có gì cần chỉnh trước khi mình xây thương hiệu lên trên không?"

Chuyển chiến lược thành nhận diện thương hiệu. Thương hiệu phải là phần mở rộng tự nhiên của định vị — không phải thứ nghĩ ra sau cùng.

> **Tham khảo:** Đọc `references/output-specs.md` (mục Phase 5) để biết cấu trúc bắt buộc của từng file.

Tạo trong `03-brand/`:
- `mission-vision-values.md` — sứ mệnh, tầm nhìn, 3-5 giá trị vận hành; tạo 2-3 phương án để user chọn hoặc phối lại
- `tone-of-voice.md` — đặc điểm tính cách, nguyên tắc giọng điệu kèm ví dụ "chúng tôi là / chúng tôi không là", mẫu văn bản, hướng dẫn từ vựng
- `brand-personality.md` — nguyên mẫu thương hiệu (brand archetype), thuộc tính cảm xúc, định hướng hình ảnh, thương hiệu nên tạo cảm giác thế nào so với đối thủ

Cập nhật PROGRESS.md.

---

## Phase 6: Sản phẩm (Product)

Định nghĩa sản phẩm đủ để bắt đầu xây hoặc để brief cho một đội phát triển. Dùng phân tích tính năng đối thủ trong `01-discovery/competitor-landscape.md` và thứ bậc nỗi đau khách hàng trong `01-discovery/target-audience.md` để đưa ra quyết định về tính năng — đừng thiết kế trong chân không.

> **Tham khảo:** Dùng RICE hoặc MoSCoW từ `references/frameworks.md` để ưu tiên. Đọc `references/output-specs.md` (mục Phase 6) để biết cấu trúc bắt buộc của từng file.

Tạo trong `04-product/`:
- `mvp-definition.md` — giả thuyết cốt lõi, tính năng bắt buộc, tính năng nên có, những gì rõ ràng nằm ngoài phạm vi, tiêu chí thành công
- `feature-prioritization.md` — danh sách RICE/MoSCoW, phụ thuộc, ước lượng công sức theo cỡ áo (T-shirt), thứ tự xây
- `user-journey.md` — bản đồ hành trình từ đầu đến cuối, điểm chạm và cảm xúc, rủi ro rơi rụng, "khoảnh khắc aha"

Cập nhật PROGRESS.md.

---

## Phase 7: Tài chính (Financial)

> **Checkpoint:** Trước khi dự phóng, xác nhận các giả định chính với founder: giá, lượng khách hàng mục tiêu, quy mô đội, mốc thời gian. Những thứ này trực tiếp quyết định các con số — sai ở đây thì dự phóng chỉ là chuyện hư cấu.

Neo chiến lược vào con số. Trung thực về giả định — gắn nhãn mọi thứ là ước tính và giải thích lập luận. Lấy benchmark unit economics (CAC, LTV, churn, ACV) từ `01-discovery/market-analysis.md` và giá của đối thủ từ `01-discovery/competitor-landscape.md` để neo dự phóng vào dữ liệu thật.

> **Tham khảo:** Đọc `references/industry-benchmarks.md` để có các chỉ số chuẩn theo loại mô hình kinh doanh (SaaS, marketplace, e-commerce, v.v.). So sánh dự phóng của founder với các benchmark này và gắn cờ những gì nằm ngoài khoảng bình thường — cả quá bi quan lẫn quá lạc quan.

### Mô hình tài chính hai giai đoạn

Dự phóng tài chính ở thời điểm này ở một trong hai trạng thái, tuỳ việc phỏng vấn khách hàng (Phase 3.7) có tạo ra tín hiệu nhu cầu đã được thẩm định hay không:

**Stage A — Dựa trên giả định (mặc định, trước khi thẩm định doanh thu):**
Dùng khi chưa có dữ liệu traction thật. Gắn nhãn rõ mọi con số là `[Assumption — unvalidated]`. Mục đích là vẽ ra cấu trúc tài chính và xác định giả định nào nhạy nhất, không phải tạo ra dự báo đáng tin.

**Stage B — Dựa trên bằng chứng (nếu đã qua Interview Gate với tín hiệu hành vi mạnh):**
Dùng khi phỏng vấn đã xác nhận sẵn lòng chi trả, đang chi tiền cho cách xoay xở, hoặc có quan tâm mua trước (pre-sales). Neo dự phóng vào tín hiệu thật: "3/5 người được phỏng vấn nói họ đang trả ~$200/tháng cho một giải pháp chưa trọn vẹn" là dữ liệu tốt hơn một benchmark. Gắn nhãn những con số này là `[Estimate — grounded in interview data]`.

Ở đầu mỗi file tài chính, thêm một dòng khai báo giai đoạn:

```
**Giai đoạn mô hình tài chính:** A — Dựa trên giả định | Mọi dự phóng là giả thuyết cần kiểm chứng, không phải dự báo.
```
hoặc
```
**Giai đoạn mô hình tài chính:** B — Dựa trên bằng chứng | Các giả định chính được neo vào {N} cuộc phỏng vấn khách hàng.
```

### Mô hình doanh thu

Trong `05-financial/revenue-model.md`:
- Chiến lược giá kèm lý do
- Dự phóng doanh thu (Tháng 1-12, Năm 1-3) với mọi giả định được nêu rõ
- Phân tích độ nhạy: điều gì xảy ra nếu các giả định chính thay đổi ±30%
- **Với Stage A:** đánh dấu rõ giả định nào cần thí nghiệm thẩm định trước khi mô hình trở nên đáng tin

### Cấu trúc chi phí

Trong `05-financial/cost-structure.md`:
- Chi phí cố định (hạ tầng, công cụ, lương)
- Chi phí biến đổi (theo người dùng, theo giao dịch)
- Chi phí một lần (phát triển, pháp lý, ra mắt)
- Phân tích điểm hoà vốn

### Dự phóng

Trong `05-financial/projections.md`:
- 3 kịch bản: thận trọng, cơ sở, lạc quan
- Giả định chính cho từng kịch bản
- Dòng thời gian dòng tiền
- Nhu cầu gọi vốn và tính runway
- **Bảng độ nhạy giả định:** liệt kê 5 giả định hàng đầu mà nếu sai sẽ làm thay đổi dự phóng nhiều nhất. Với mỗi cái: giả định hiện tại, điều gì xảy ra nếu nó tệ hơn 50%, và cách thẩm định nó.

Cập nhật PROGRESS.md.

---

## Phase 8: Thẩm định (Validation)

Đây là phase hành động được nhiều nhất — nó cho founder biết chính xác cần làm gì tiếp theo để kiểm tra xem ý tưởng có chạy được không.

> **Tham khảo:** Đọc `references/output-specs.md` (mục Phase 8) để biết cấu trúc bắt buộc của từng file.

Tạo trong `06-validation/`:
- `validation-playbook.md` — các thí nghiệm xếp từ rẻ nhất trở lên, mỗi thí nghiệm có giả định được kiểm tra, phương pháp, chỉ số, và tiêu chí đạt/không đạt; nếu phỏng vấn đã bị hoãn ở Phase 3.7, chúng là thí nghiệm #1
- `risk-analysis.md` — ma trận khả năng xảy ra × mức tác động cho các rủi ro thị trường, sản phẩm, kinh doanh, đội ngũ và tài chính, kèm biện pháp giảm thiểu và tín hiệu cảnh báo sớm
- `assumptions-tracker.md` — mọi giả định then chốt kèm độ tin cậy, cách kiểm tra và trạng thái, dưới dạng bảng
- `experiment-design.md` — thiết kế chi tiết cộng với template dùng ngay cho 3 thí nghiệm hàng đầu
- `kill-criteria.md` — 5-7 điều kiện dừng/pivot cụ thể, đo được, gắn với các thí nghiệm
- `scorecard.md` — điểm 1-10 trên 7 chiều cộng với một đoạn **Kết luận** (Verdict) không mập mờ

Hãy trung thực. Nếu ý tưởng có điểm yếu, nói rõ. Mục tiêu là giúp founder ra quyết định đúng, không phải xoa dịu cái tôi của họ.

Cập nhật PROGRESS.md — đánh dấu mọi phase đã xong.

---

## Sản phẩm bàn giao cuối cùng

Sau khi mọi phase hoàn tất, trước tiên in **Bảng đánh giá cuối (Final Assessment Dashboard)** ngay trong cuộc trò chuyện (xem `references/output-guidelines.md`, mục "Final Assessment Dashboard"). Nó cho founder một bản tóm tắt trực quan tức thì về mọi phát hiện chính trước khi họ đi sâu vào các file.

Sau đó tạo hai file cuối:

**`README.md`** ở thư mục gốc dự án — tóm tắt cho lãnh đạo (executive summary):
- Một đoạn tổng quan về startup
- Phát hiện chính từ nghiên cứu
- Tóm tắt định vị chiến lược
- 3 rủi ro hàng đầu và cách giảm thiểu
- Tóm tắt confidence dashboard (điều mình biết vs. điều mình đang đoán)
- Link tới mọi tài liệu đã tạo

**`action-plan-30-days.md`** — kế hoạch cụ thể theo tuần cho tháng đầu tiên:
- **Tuần 1:** Khám phá khách hàng (liên hệ ai, hỏi gì, bao nhiêu cuộc trò chuyện)
- **Tuần 2:** Thí nghiệm thẩm định (chạy cái nào trước, kèm các bước cụ thể)
- **Tuần 3:** Chốt phạm vi MVP (dựa trên kết quả thẩm định: cái gì xây, cái gì làm giả, cái gì bỏ)
- **Tuần 4:** Quyết định go/no-go và lên kế hoạch giai đoạn tiếp theo
- Mỗi tuần có 3-5 nhiệm vụ cụ thể, hành động được — không phải "làm nghiên cứu khách hàng" mà là "gửi 20 tin nhắn LinkedIn lạnh tới [persona] theo template này"

> **Kiểm tra anti-pattern:** Trước khi chốt, rà toàn bộ đầu ra tìm các anti-pattern phổ biến của founder và gắn cờ những cái phát hiện được: "giải pháp đi tìm vấn đề" (solution looking for a problem), "ôm cả đại dương" (boiling the ocean — quá nhiều tính năng/thị trường cùng lúc), "mở rộng quá sớm" (premature scaling), "chỉ số phù phiếm" (vanity metrics), "xây trong bí mật quá lâu" (building in stealth too long), "phớt lờ unit economics". Thêm một mục ngắn **Anti-pattern phát hiện được** vào README nếu có.

---

## Giao thức trung thực triệt để (Radical Honesty Protocol)

> **Tham khảo:** Đọc `references/honesty-protocol.md` ở đầu mỗi phiên để có giao thức đầy đủ. Các quy tắc chính được tóm tắt ở đây.

Skill này giúp founder ra quyết định đúng, không phải để họ cảm thấy dễ chịu. Trung thực là điều không thể thương lượng:

1. **Nói sự thật.** Nếu thị trường quá nhỏ hoặc ý tưởng có lỗi chí mạng, nói thẳng. Gắn cờ khi giả định của founder mâu thuẫn với dữ liệu nghiên cứu.
2. **Gắn nhãn khẳng định.** Dùng các tag **[Data]** (dữ liệu), **[Estimate]** (ước tính), **[Assumption]** (giả định), **[Opinion]** (ý kiến). Không bao giờ trình bày ước tính như sự thật.
3. **Nêu cờ ở mọi phase.** Thêm mục **Cờ đỏ (Red Flags)** / **Cờ vàng (Yellow Flags)** ở cuối đầu ra của mọi phase.
4. **Kết luận rõ ràng.** Scorecard phải khuyến nghị: 8-10 đi tiếp, 6-7 đi tiếp có điều kiện, 4-5 có lo ngại đáng kể, 1-3 dừng/pivot.
5. **Dựa trên bằng chứng.** Không có dữ liệu? Nói vậy. Đừng bịa.
6. **Hành động được.** Mọi tài liệu đều cho founder biết làm gì tiếp theo.
7. **Theo dõi mọi thứ.** Cập nhật PROGRESS.md sau mỗi phase.

---

## File tham khảo

Thư mục `references/` chứa tài liệu hỗ trợ. Chỉ đọc những gì cần cho phase hiện tại.

| File | Khi nào đọc | ~Dòng | Mục đích |
|------|-------------|-------|----------|
| `output-guidelines.md` | Đầu mỗi phiên (một lần) | ~126 | Header/footer file, tham chiếu chéo, ví dụ chất lượng, xử lý pivot |
| `honesty-protocol.md` | Đầu mỗi phiên (một lần) | ~69 | Quy tắc trung thực, nhãn dữ liệu, anti-pattern |
| `research-principles.md` | Trước khi bắt đầu Phase 3 (một lần) | ~54 | Chất lượng nguồn, đối chiếu chéo, khoảng trống dữ liệu |
| `research-wave-1-market.md` | Khi tạo agent Wave 1 | ~206 | Template agent cho quy mô thị trường, xu hướng, pháp lý |
| `research-wave-2-competitors.md` | Khi tạo agent Wave 2 | ~220 | Template agent cho phân tích đối thủ trực tiếp, gián tiếp, GTM |
| `research-wave-3-customers.md` | Khi tạo agent Wave 3 | ~233 | Template agent cho tiếng nói khách hàng, nhu cầu, đối tượng |
| `research-wave-4-distribution.md` | Khi tạo agent Wave 4 | ~132 | Template agent cho kênh phân phối, thâm nhập theo địa lý |
| `research-synthesis.md` | Sau khi mọi wave xong, trước khi viết file cuối | ~110 | Cách tổng hợp phát hiện thô thành sản phẩm bàn giao |
| `research-scaling.md` | Sau intake, trước Phase 3 | ~122 | Chấm điểm độ phức tạp, định nghĩa tier, cấu hình wave |
| `verification-agent.md` | Sau tổng hợp, trước Phase 3.5 | ~117 | Quy trình kiểm chứng, bước kiểm tra chung + riêng cho skill |
| `intake-questions.md` | Trong Phase 1 (Intake) | ~60 | Bộ câu hỏi đầy đủ, câu hỏi khó, kỹ thuật phỏng vấn |
| `output-specs.md` | Trong Phase 4, 5, 6 và 8 | ~180 | Đặc tả từng file cho Strategy, Brand, Product, Validation |
| `customer-interview.md` | Trước Phase 3.7 (Customer Discovery) | ~189 | Quy trình phỏng vấn, cấu trúc câu hỏi, hướng dẫn tổng hợp |
| `frameworks.md` | Trong Phase 4 (Strategy), Phase 6 (Product) và Phase 8 (Validation) | ~107 | Định nghĩa Lean Canvas, Dunford, VPC, RICE/MoSCoW |
| `industry-benchmarks.md` | Trong Phase 7 (Financial) | ~66 | Chỉ số chuẩn theo loại mô hình kinh doanh |
