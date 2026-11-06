---
name: product-competitors
description: >-
  Phân tích đối thủ cạnh tranh chuyên sâu (competitive intelligence) cho bất kỳ
  thị trường nào. Phân tích sản phẩm, giá, cảm nhận khách hàng, chiến lược GTM
  và tín hiệu tăng trưởng của đối thủ bằng dữ liệu web thật. Tạo ra battle card,
  bức tranh giá (pricing landscape) và ma trận tính năng. Dùng khi user muốn hiểu
  bối cảnh cạnh tranh, phân tích đối thủ, so sánh sản phẩm trong một thị trường,
  hoặc tìm xem mình đang cạnh tranh với ai. Kích hoạt với các câu như "đối thủ
  của mình là ai", "phân tích đối thủ", "nghiên cứu đối thủ", "so sánh giá đối
  thủ", "ai khác đang làm mảng này", "lợi thế cạnh tranh", "who are my
  competitors", "competitive analysis", "competitor research", "battle cards",
  "pricing comparison", "competitor pricing", "market players", "competitive
  intelligence", "competitive landscape", "who else is in this space",
  "competitive moat", hoặc mọi yêu cầu lập hồ sơ, so sánh, vẽ bản đồ đối thủ
  trong một nhóm sản phẩm. Chạy độc lập — không cần đã chạy product-design trước.
---

# Product Competitors

Phân tích đối thủ cạnh tranh chuyên sâu, vượt xa mức hồ sơ bề mặt. Tạo ra battle card dùng được ngay, phân tích bức tranh giá và bản đồ điểm yếu chiến lược bằng dữ liệu web thật.

## Cách hoạt động

```
INTAKE → RESEARCH (3 đợt nối tiếp) → SYNTHESIS → BATTLE CARDS
```

Quy trình tập trung: hiểu sản phẩm, nghiên cứu sâu đối thủ theo 3 chiều, tổng hợp kết quả, rồi tạo đầu ra dùng được ngay. Thời gian chạy thường: 15-25 phút trên Claude Code (agent chạy song song), 30-45 phút trên Claude.ai (chạy tuần tự).

### Ngôn ngữ

Ngôn ngữ đầu ra mặc định là **tiếng Việt**. Nếu user viết bằng ngôn ngữ khác hoặc yêu cầu rõ một ngôn ngữ, dùng ngôn ngữ đó cho mọi đầu ra.

---

## Giai đoạn 0: Kiểm tra để làm tiếp (Resume Check)

Trước mọi việc khác, kiểm tra xem trong thư mục làm việc hoặc một thư mục con của project có file `PROGRESS.md` do skill này tạo không (trường tên skill ghi `product-competitors`). Nếu có, đọc nó và làm tiếp từ giai đoạn chưa xong gần nhất. Báo user: "Mình thấy tiến độ từ phiên trước. Bạn đã xong [các giai đoạn]. Mình sẽ làm tiếp từ [giai đoạn kế tiếp]."

Nếu không có file tiến độ — hoặc file tìm thấy thuộc về skill khác — bắt đầu từ Giai đoạn 1.

---

## Giai đoạn 1: Thu thập thông tin (Intake)

Ngắn gọn và tập trung — 1-2 lượt hỏi, không phải một buổi phỏng vấn dài. Mục tiêu chỉ là đủ bối cảnh để chạy nghiên cứu có trọng tâm.

### Kiểm tra kết quả product-design có sẵn

Trước khi hỏi, kiểm tra xem project này đã chạy xong một phiên `product-design` chưa. Tìm các file sau trong thư mục làm việc hoặc thư mục con:

- `01-discovery/competitor-landscape.md` — hồ sơ và phân tích đối thủ
- `01-discovery/market-analysis.md` — quy mô thị trường, xu hướng, quy định pháp lý
- `01-discovery/target-audience.md` — chân dung khách hàng (persona), nỗi đau (pain point)
- `00-intake/brief.md` — mô tả sản phẩm và bối cảnh

Nếu các file này tồn tại, đọc chúng và dùng dữ liệu làm điểm xuất phát:
- Lấy mô tả sản phẩm, thị trường mục tiêu và các đối thủ đã biết từ brief
- Dùng danh sách đối thủ trong `competitor-landscape.md` làm điểm bắt đầu để phân tích sâu hơn (product-design chỉ lập hồ sơ bề mặt cho 5-8 đối thủ — skill này đào sâu hơn nhiều vào từng đối thủ)
- Lấy quy mô và xu hướng thị trường từ `market-analysis.md` để đặt bối cảnh cạnh tranh
- Dùng pain point của khách hàng trong `target-audience.md` để tập trung phần khai thác cảm nhận khách hàng (sentiment mining) vào những gì quan trọng nhất

Báo user: "Mình thấy dữ liệu từ một phiên product-design trước. Mình sẽ dùng nó làm điểm xuất phát và phân tích đối thủ sâu hơn."

Bỏ qua hoàn toàn phần phỏng vấn intake nếu các file product-design đã cung cấp đủ bối cảnh. Chuyển thẳng sang nghiên cứu.

### Cần hỏi gì (nếu chưa có dữ liệu trước đó)

**Lượt 1 — Thông tin cơ bản:**
- Sản phẩm/ý tưởng của bạn là gì? (một câu là đủ)
- Nó giải quyết vấn đề gì và cho ai?
- Bạn đang ở thị trường/nhóm sản phẩm (category) nào?
- Bạn đã biết đối thủ nào chưa? (tên, URL)

**Lượt 2 — Làm rõ thêm (chỉ khi cần):**
- Bạn nhắm tới khu vực địa lý/thị trường nào?
- Mô hình giá hoặc khoảng giá của bạn là gì?
- Bạn coi điểm khác biệt chính của mình là gì?

Đừng hỏi quá nhiều. Nếu user mô tả rõ ngay từ đầu, chuyển thẳng sang nghiên cứu. Chính phần phân tích cạnh tranh sẽ làm lộ ra những gì quan trọng.

### Đầu ra

Lưu vào `{project-name}/intake.md` — tóm tắt ngắn về sản phẩm, thị trường và các đối thủ đã biết. Nếu dựa trên dữ liệu product-design, ghi lại các file nguồn đã dùng. Tên project lấy từ sản phẩm/thị trường (kebab-case, vd `ai-email-assistant`).

Tạo `{project-name}/PROGRESS.md` gồm: tên project, tên skill (`product-competitors`), ngày bắt đầu, ngôn ngữ, chế độ nghiên cứu (Live / Knowledge-Based) và checklist các giai đoạn. Cập nhật file sau mỗi giai đoạn hoàn thành. Nếu PROGRESS.md đã có từ phiên trước, làm tiếp từ giai đoạn chưa xong gần nhất.

---

## Giai đoạn 1.5: Đánh giá độ sâu nghiên cứu

Sau intake, đánh giá độ phức tạp của thị trường và trình bày đề xuất Độ sâu nghiên cứu (Research Depth) cho user.

> **Tham khảo:** Đọc `references/research-scaling.md` để lấy ma trận chấm điểm độ phức tạp, định nghĩa các mức, cấu hình từng đợt nghiên cứu và mẫu thông báo cho user.

### Quy trình

1. Chấm điểm ba yếu tố từ intake: độ rộng thị trường (1-3), số đối thủ đã biết (1-3), phạm vi địa lý (1-3)
2. Cộng điểm (khoảng 3-9) và quy ra mức: Light (3-4), Standard (5-7), Deep (8-9)
3. Trình bày bảng Độ sâu nghiên cứu cho user (xem mẫu chính xác trong `research-scaling.md`)
4. Chờ user trả lời: **light**, **deep**, hoặc **ok** để chấp nhận đề xuất
5. Ghi mức đã chọn vào PROGRESS.md

Mức đã chọn quyết định số agent mỗi đợt và số vòng tìm kiếm mỗi agent ở Giai đoạn 2. Xem cấu hình chính xác từng đợt theo mức trong `research-scaling.md`.

---

## Giai đoạn 2: Nghiên cứu

Ba đợt nghiên cứu (wave) chạy nối tiếp nhau, mỗi đợt tiếp cận bối cảnh cạnh tranh từ một góc khác — các agent trong cùng một đợt chạy song song. Gộp lại, chúng cho một cái nhìn 360 độ.

### Nhận biết môi trường

Kiểm tra xem tool `Agent` có sẵn không:

- **Có tool Agent (Claude Code):** Tạo tất cả agent trong mỗi đợt chạy song song. Cách này nhanh hơn.
- **KHÔNG có tool Agent (Claude.ai, web):** Chạy nghiên cứu tuần tự, theo đúng các mẫu (template). Độ sâu như nhau, chỉ chậm hơn.

### Tìm kiếm web

Skill này cần WebSearch để có dữ liệu thật. Nếu WebSearch không có hoặc bị từ chối, chuyển sang **Chế độ Knowledge-Based**: dùng dữ liệu huấn luyện, đánh dấu mọi phát hiện bằng **[Knowledge-Based — cần tự kiểm chứng]**, và hạ mức độ tin cậy xuống một bậc.

> **Tham khảo:** Đọc `references/research-principles.md` trước khi bắt đầu bất kỳ đợt nào. File này định nghĩa các bậc chất lượng nguồn, quy tắc đối chiếu chéo, và cách xử lý chỗ thiếu dữ liệu.

### Đợt 1: Hồ sơ đối thủ + Thông tin giá

> **Tham khảo:** Đọc `references/research-wave-1-profiles-pricing.md` để lấy mẫu cho agent.

Hai agent (hoặc hai khối việc tuần tự):

**A1: Đào sâu đối thủ (Competitor Deep-Dives)** — Xác định và lập hồ sơ 5-8 đối thủ trực tiếp cùng 2-3 giải pháp liền kề (nền tảng rộng hơn, cách làm thủ công, công cụ từ các nhóm sản phẩm lân cận tranh cùng một ngân sách). Với mỗi đối thủ: sản phẩm, tính năng, quy mô đội, vốn gọi được, tín hiệu traction, điểm mạnh, điểm yếu. Đừng dừng ở trang marketing của họ — xem cả review, tin tuyển dụng và dữ liệu gọi vốn.

**A2: Thông tin giá (Pricing Intelligence)** — Với mỗi đối thủ: phân tích ngược mô hình giá. Không chỉ "giá $49/tháng" mà là: thước đo giá trị (value metric) là gì (theo seat? theo mức dùng? giá cố định?), các gói (tier) khác nhau thế nào, họ dùng tâm lý giá nào (neo giá — anchoring, gói mồi — decoy, giá lẻ — charm pricing), chi phí chuyển đổi (switching cost) là gì (kỹ thuật, hợp đồng, cảm xúc). Lập bảng so sánh từng gói.

### Đợt 2: Khai thác cảm nhận khách hàng

> **Tham khảo:** Đọc `references/research-wave-2-sentiment-mining.md` để lấy mẫu cho agent.

Hai agent (hoặc hai khối việc tuần tự):

**B1: Khai thác review (Review Mining)** — Khai thác review trên G2, Capterra, TrustRadius, Product Hunt và App Store cho từng đối thủ. Rút ra các mẫu lặp lại: người dùng khen gì? Phàn nàn gì? Xin thêm tính năng gì? Sắp xếp theo đối thủ và theo chủ đề nỗi đau. Kèm trích dẫn nguyên văn.

**B2: Khai thác diễn đàn & cộng đồng (Forum & Community Mining)** — Khai thác Reddit, Indie Hackers, Hacker News, Quora và các cộng đồng ngách. Tìm: phàn nàn về công cụ hiện có, các thread kiểu "bạn dùng gì cho X?", câu chuyện chuyển đổi (migration), thảo luận về cách lách (workaround). Xây một **bản đồ ngôn ngữ (language map)** — đúng những từ khách hàng dùng để mô tả vấn đề và mong muốn của họ. Xác định **tín hiệu rời bỏ (churn signal)** — vì sao người dùng rời bỏ từng đối thủ.

### Đợt 3: GTM & Tín hiệu chiến lược

> **Tham khảo:** Đọc `references/research-wave-3-gtm-signals.md` để lấy mẫu cho agent.

Hai agent (hoặc hai khối việc tuần tự):

**C1: Phân tích Go-to-Market** — Với mỗi đối thủ: kênh thu hút khách chính, cách bán (self-serve hay sales-led), chiến lược nội dung (tần suất blog, chủ đề, chất lượng), hiện diện mạng xã hội, tín hiệu quảng cáo trả phí, các nước đi về đối tác. Xây một **bản đồ cơ hội theo kênh (channel opportunity map)** cho thấy mức bão hoà đối thủ so với mức cơ hội trên từng kênh.

**C2: Tín hiệu chiến lược & tăng trưởng** — Quỹ đạo gọi vốn (các vòng, nhà đầu tư, thời điểm), mẫu tuyển dụng (nhiều kỹ sư = đang xây; nhiều sales = đang mở rộng; nhiều support = đang chật vật), dấu chân nội dung/SEO (họ lên top cho từ khoá nào, khoảng trống ở đâu), tín hiệu lộ trình sản phẩm từ changelog và phát ngôn công khai. Xác định **trụ cột nội dung (content pillar)** mà mỗi đối thủ đang nắm và những chủ đề chưa ai làm tốt.

---

### Điểm dừng sau nghiên cứu

Sau khi cả ba đợt xong, trước khi tổng hợp, trình bày ngắn gọn cho user những gì nghiên cứu tìm được: đã lập hồ sơ bao nhiêu đối thủ, các chủ đề nỗi đau hàng đầu của khách hàng, các tín hiệu chiến lược đáng chú ý nhất (gọi vốn, tuyển dụng, mẫu GTM). Hỏi: "Kết quả này có khớp với kỳ vọng của bạn không? Có đối thủ nào cần thêm hay bỏ trước khi mình tổng hợp không?"

Gói gọn trong một tin nhắn — đây là bước kiểm tra nhanh cho thống nhất, không phải một báo cáo đầy đủ.

---

## Giai đoạn 3: Tổng hợp (Synthesis)

> **Tham khảo:** Đọc `references/research-synthesis.md` để lấy quy trình tổng hợp và mẫu battle card.

Sau điểm dừng, tổng hợp các phát hiện thô thành sản phẩm chiến lược. Bước này tạo ra giá trị thật — không phải báo cáo lại, mà là ghép mẫu (pattern-matching) xuyên suốt các nguồn dữ liệu.

### Cách tổng hợp

Tổng hợp là nơi dữ liệu đối thủ thô trở thành chiến lược — đó là suy luận, không phải định dạng lại. Trước khi viết, hãy nghĩ kỹ xem các phát hiện ăn khớp với nhau thế nào: một khoảng trống về giá chẳng mấy ý nghĩa cho tới khi bạn nối nó với một lời phàn nàn lặp lại của khách hàng và một tín hiệu tuyển dụng. Đây là phần suy nghĩ có đòn bẩy cao nhất trong cả phân tích, nên nếu model hỗ trợ extended thinking, hãy dồn nó vào đây. Sau đó làm cẩn thận qua các bước:

1. Đọc tất cả file thô trước khi viết bất cứ gì
2. Nối các phát hiện giữa các đợt: khoảng trống giá + phàn nàn của khách + tín hiệu tuyển dụng = cơ hội chiến lược
3. Chỉ ra mâu thuẫn giữa các nguồn và giải thích nên tin nguồn nào
4. Chấm độ tin cậy cho mỗi nhận định lớn (Cao / Trung bình / Thấp)
5. Làm rõ hàm ý chiến lược — không chỉ dữ kiện, mà dữ kiện đó có nghĩa là gì
6. Gom mọi chỗ thiếu dữ liệu từ các file thô vào một mục riêng "Chỗ thiếu dữ liệu & Giới hạn nghiên cứu" trong competitors-report — phân tích nào cũng có điểm mù, nói rõ chúng ra giúp tránh tự tin sai chỗ
7. Đưa cả các giải pháp liền kề vào (nền tảng rộng hơn, cách làm thủ công, công cụ từ nhóm sản phẩm lân cận) — khách hàng không chỉ chọn giữa các đối thủ trực tiếp, họ chọn giữa các phương án "tạm đủ dùng" từ các mảng lân cận

### Các file đầu ra

Mọi file sản phẩm phải mở đầu bằng header chuẩn: `# {Tiêu đề}: {product}` rồi tới `*Skill: product-competitors | Ngày tạo: {date}*`. Mọi file sản phẩm phải kết thúc bằng các mục Red Flags, Yellow Flags và Nguồn (Sources).

**`{project-name}/competitors-report.md`** — Sản phẩm chính:
- Tóm tắt điều hành (tổng quan bối cảnh cạnh tranh trong 5 câu)
- Đánh giá mức độ tập trung thị trường (phân mảnh / đang hợp nhất / bị thống trị)
- Phát hiện chính theo từng chiều nghiên cứu
- Cơ hội chiến lược (nên cạnh tranh ở đâu)
- Rủi ro chiến lược (nên tránh ở đâu)
- Đánh giá hào cạnh tranh (moat) (hiệu ứng mạng, chi phí chuyển đổi, hào dữ liệu, thương hiệu, quy mô)
- Chỗ thiếu dữ liệu & giới hạn nghiên cứu (bắt buộc — gom từ tất cả file thô)
- Red flags và yellow flags

**`{project-name}/competitive-matrix.md`** — Bảng so sánh tính năng:
- Tính năng ở hàng, đối thủ ở cột
- Đánh giá: mạnh / đạt / yếu / không có
- Làm nổi bật các khoảng trống mà chưa đối thủ nào phục vụ tốt
- Có cả sản phẩm của bạn (hoặc để chỗ trống nếu chưa ra mắt)

**`{project-name}/pricing-landscape.md`** — Phân tích giá riêng:
- So sánh từng gói giữa tất cả đối thủ
- Phân tích value metric (mỗi bên tính tiền theo cái gì và vì sao)
- Phân tích tâm lý giá (neo giá, gói mồi, chiến lược freemium)
- Bản đồ định vị giá (trục: giá so với độ sâu tính năng)
- Khoảng trống về giá — nơi còn chỗ để định vị
- Ma trận chi phí chuyển đổi (theo từng đối thủ: kỹ thuật, hợp đồng, cảm xúc)

**`{project-name}/battle-cards/{competitor-name}.md`** — Mỗi đối thủ một file:
- Định dạng một trang: họ là ai, điểm mạnh, điểm yếu
- Cách thắng họ (luận điểm cụ thể khi trao đổi)
- Khi nào họ thắng bạn (hãy thành thật)
- Phản đối thường gặp của khách và cách trả lời
- Điểm yếu then chốt có thể khai thác
- Tín hiệu rời bỏ (vì sao khách của họ bỏ đi)

### Dữ liệu thô

Giữ các file nghiên cứu thô trong `{project-name}/raw/` để tham khảo:
- `competitor-profiles.md`
- `pricing-intelligence.md`
- `review-mining.md`
- `forum-mining.md`
- `gtm-analysis.md`
- `strategic-signals.md`

---

## Giai đoạn 3.5: Kiểm chứng nghiên cứu

Sau khi tổng hợp xong và mọi file sản phẩm đã được ghi, chạy một lượt kiểm chứng.

> **Tham khảo:** Đọc `references/verification-agent.md` để lấy toàn bộ quy trình kiểm chứng, các kiểm tra chung và các kiểm tra riêng cho skill này.

### Quy trình

1. Tạo agent **V1: Kiểm chứng (Verification)** — agent đọc tất cả file sản phẩm và kiểm tra: nhận định không gắn nhãn, mâu thuẫn nội bộ, độ nhất quán của mức tin cậy, thiếu mục chỗ thiếu dữ liệu, thiếu flag, dữ liệu cũ, và việc dùng trùng một nguồn như thể đối chiếu độc lập
2. V1 cũng chạy các kiểm tra riêng của product-competitors: battle card nhất quán với báo cáo, ma trận khớp với hồ sơ, bức tranh giá nhất quán với hồ sơ, các sản phẩm ăn khớp với nhau
3. V1 tạo ra `{project-name}/verification-report.md`
4. **Nếu có vấn đề Nghiêm trọng (Critical):** Dừng lại và trình bày cho user. Hỏi: sửa trước, hay cứ tiếp tục như hiện tại?
5. **Nếu chỉ có Cảnh báo/Thông tin (Warnings/Info):** Hiển thị tóm tắt một dòng

Trên Claude.ai hoặc khi không có tool Agent, tự chạy các kiểm tra này trong cuộc hội thoại chính theo đúng quy trình.

---

## Quy tắc trung thực (Honesty Protocol)

> **Tham khảo:** Đọc `references/honesty-protocol.md` để lấy toàn bộ quy tắc và chi tiết các anti-pattern.

Thông tin cạnh tranh chỉ hữu ích khi trung thực. Các quy tắc lõi áp dụng (gắn nhãn nhận định, định lượng, khai báo chỗ thiếu), cộng thêm các quy tắc riêng cho phân tích cạnh tranh:

1. **Không cổ vũ suông.** Nếu đối thủ khách quan giỏi hơn ở điểm nào, nói thẳng. Battle card mà lờ đi điểm mạnh của đối thủ thì vô dụng trong các cuộc bán hàng thật.
2. **Gắn nhãn nhận định.** Dùng các nhãn **[Data]**, **[Estimate]**, **[Assumption]**, **[Opinion]**. Không bao giờ trình bày phỏng đoán như sự thật.
3. **Định lượng.** "ARR $12M, tăng 40% so với cùng kỳ năm trước" chứ không phải "họ đang tăng nhanh".
4. **Ghi ngày cho mọi thứ.** Đánh dấu dữ liệu cũ hơn 12 tháng.
5. **Khai báo chỗ thiếu.** "DATA GAP: Không tìm được dữ liệu đáng tin về [X]" luôn tốt hơn bịa đặt.
6. **Nêu rõ red flag.** Nếu bối cảnh cạnh tranh trông khốc liệt, nói thẳng.
7. **Chống thiên kiến xác nhận (confirmation bias).** Khi nghiên cứu xác nhận đúng điều founder vốn đã tin, hãy đào sâu thêm. Tìm bằng chứng ngược lại.

Xem `references/honesty-protocol.md` để có đầy đủ bảng anti-pattern (6 mục) và quy tắc chi tiết.

---

## Các file tham khảo

Chỉ đọc những gì cần cho giai đoạn hiện tại.

| File | Khi nào đọc | ~Số dòng | Mục đích |
|------|-------------|--------|---------|
| `honesty-protocol.md` | Đầu phiên | ~72 | Toàn bộ quy tắc trung thực kèm anti-pattern |
| `research-principles.md` | Trước khi bắt đầu Giai đoạn 2 | ~54 | Chất lượng nguồn, đối chiếu chéo, chỗ thiếu dữ liệu |
| `research-wave-1-profiles-pricing.md` | Khi chạy Đợt 1 | ~186 | Mẫu agent cho hồ sơ + giá |
| `research-wave-2-sentiment-mining.md` | Khi chạy Đợt 2 | ~198 | Mẫu agent cho khai thác review + diễn đàn |
| `research-wave-3-gtm-signals.md` | Khi chạy Đợt 3 | ~199 | Mẫu agent cho GTM + tín hiệu chiến lược |
| `research-synthesis.md` | Sau khi xong mọi đợt | ~237 | Cách tổng hợp + mẫu battle card |
| `research-scaling.md` | Sau intake, trước Giai đoạn 2 | ~106 | Chấm điểm độ phức tạp, định nghĩa mức, cấu hình từng đợt |
| `verification-agent.md` | Sau khi tổng hợp | ~126 | Quy trình kiểm chứng, kiểm tra chung + kiểm tra riêng của skill |
