# Wave 2: Phân tích cạnh tranh (3 agent)

Đọc `research-principles.md` trước. Các agent Wave 2 nhận phát hiện từ Wave 1 làm bối cảnh — chuyển cho chúng bản tóm tắt quy mô thị trường, các người chơi chính đã xác định, và các xu hướng liên quan.

---

## Agent B1: Đào sâu đối thủ trực tiếp (Direct Competitor Deep-Dives)

```
Nhiệm vụ nghiên cứu: Phân tích sâu các đối thủ trực tiếp cho {mô tả sản phẩm}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.
Bối cảnh thị trường từ Wave 1: {tóm tắt ngắn về quy mô thị trường, các người chơi chính đã tìm thấy}

QUY TRÌNH NGHIÊN CỨU — cho từng đối thủ (nhắm 5-8 đối thủ trực tiếp):

VÒNG 1 — Xác định đối thủ (3-4 lượt tìm):
- "{problem} software/app/tool {current year}"
- "best {product category} tools {current year}"
- "{known competitor 1} vs {known competitor 2} alternatives"
- "G2 {product category} grid"
- "{product category} Product Hunt"

VÒNG 2 — Đào sâu từng đối thủ (2-3 lượt tìm mỗi đối thủ):
- Vào thẳng website của họ: ghi lại giá, tính năng, định vị
- "{competitor name} review" trên G2, Capterra, TrustRadius
- "{competitor name} funding crunchbase" HOẶC "{competitor name} investors"
- "{competitor name} employees linkedin" (để có tín hiệu về quy mô đội)
- "{competitor name} complaints" HOẶC "{competitor name} problems reddit"

VÒNG 3 — Động lực cạnh tranh (2 lượt tìm):
- "{product category} market share"
- Các bài so sánh "{competitor 1} vs {competitor 2}"

Với TỪNG đối thủ, dựng một hồ sơ đầy đủ:

MẪU HỒ SƠ ĐỐI THỦ:
## {Tên đối thủ}
- **Website:** {url}
- **Thành lập:** {năm}
- **Trụ sở:** {địa điểm}
- **Quy mô đội:** {ước tính từ LinkedIn/Crunchbase}
- **Vốn:** {tổng vốn đã gọi, vòng gần nhất, nhà đầu tư}
- **Giai đoạn:** bootstrap / seed / Series A / Series B+ / đã niêm yết

### Sản phẩm
- **Sản phẩm cốt lõi:** {họ bán gì}
- **Tính năng chính:** {5 tính năng hàng đầu}
- **Tín hiệu về tech stack:** {mọi thông tin công khai về công nghệ của họ}
- **Tích hợp:** {họ kết nối với những gì}

### Giá
- **Mô hình:** {subscription / theo người dùng / theo mức dùng / freemium}
- **Các gói:** {liệt kê từng gói với giá và nội dung bao gồm}
- **Gói miễn phí:** có/không, gồm những gì
- **Enterprise:** giá tuỳ chỉnh? do đội sales dẫn dắt?

### Vị thế thị trường
- **Khách hàng mục tiêu:** {họ phục vụ ai}
- **Định vị:** {họ tự mô tả mình thế nào — ghi lại nguyên văn tagline}
- **Điểm khác biệt chính:** {điều họ tuyên bố khiến họ độc đáo}

### Tín hiệu traction
- **Review trên G2/Capterra:** {số lượng và điểm trung bình}
- **Product Hunt:** {số upvote nếu đã ra mắt ở đó}
- **Mạng xã hội:** {số người theo dõi trên LinkedIn, Twitter}
- **Tin tuyển dụng:** {số lượng và loại — nặng về kỹ sư = đang xây; nặng về sales = đang mở rộng}
- **Khách hàng tiêu biểu:** {logo hoặc case study trên site của họ}

### Điểm mạnh (dựa trên review và định vị)
- {điểm mạnh 1}
- {điểm mạnh 2}

### Điểm yếu (dựa trên review tiêu cực, tính năng còn thiếu, phàn nàn)
- {điểm yếu 1}
- {điểm yếu 2}

### Mức đe doạ với startup của chúng ta: Thấp / Trung bình / Cao
- {tại sao}

---

Sau tất cả hồ sơ, thêm:

## Tóm tắt bức tranh cạnh tranh
- **Mức độ tập trung thị trường:** phân mảnh / đang hợp nhất / bị 1-2 người chơi thống trị
- **Khoảng trống trên thị trường:** {điều mà không đối thủ nào làm tốt}
- **Cơ hội định vị:** {chỗ chúng ta có thể khác biệt}
- **Đánh giá hào phòng thủ cạnh tranh (moat):** {thị trường này khó công phá đến mức nào}

## Khoảng trống dữ liệu
- [Các đối thủ bạn nghi là có tồn tại nhưng không tìm được thông tin]
- [Các điểm dữ liệu còn thiếu cho từng đối thủ cụ thể]

Lưu vào: {project-name}/01-discovery/raw/direct-competitors.md
```

---

## Agent B2: Đối thủ gián tiếp & sản phẩm thay thế (Indirect Competitors & Substitutes)

```
Nhiệm vụ nghiên cứu: Đối thủ gián tiếp, sản phẩm thay thế, và các cách tiếp cận khác cho {vấn đề}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.
Đối thủ trực tiếp đã tìm thấy: {danh sách từ Agent B1 nếu có, nếu không thì "sẽ xác định sau"}

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Các cách tiếp cận thay thế (2-3 lượt tìm):
- "how do {customer type} currently handle {problem}"
- "{problem} without software"
- "{problem} excel template" HOẶC "{problem} manual process"
- "{problem} outsource"

VÒNG 2 — Sản phẩm lân cận (2-3 lượt tìm):
- "{adjacent category} that also does {related function}"
- "{large platform} {related feature}" (vd "Salesforce reporting" nếu bạn đang xây công cụ analytics)
- "open source {product category}"

VÒNG 3 — Rủi ro nền tảng (1-2 lượt tìm):
- "{major platform} adding {our feature}"
- "{major platform} AI features {current year}"

ĐỊNH DẠNG ĐẦU RA:
# Đối thủ gián tiếp & sản phẩm thay thế

## Giải pháp hiện trạng (người ta đang làm gì hôm nay khi không có công cụ chuyên dụng)
Với mỗi giải pháp:
- Nó là gì
- Phổ biến đến mức nào
- Tại sao người ta vẫn dùng (chi phí, quen thuộc, "đủ dùng")
- Nó gãy ở đâu (nỗi đau tạo ra cơ hội cho chúng ta)

## Sản phẩm lân cận
Với mỗi sản phẩm:
- Tên sản phẩm và chức năng chính của nó
- Nó giải một phần vấn đề của chúng ta như thế nào
- Nó còn thiếu gì (điểm chen vào — wedge — của chúng ta)
- Rủi ro: họ có thể thêm tính năng của chúng ta không?

## Đánh giá rủi ro nền tảng
- Những nền tảng lớn nào có thể nuốt chức năng của chúng ta?
- Khả năng đó cao đến đâu? (dựa trên tín hiệu roadmap, thương vụ thâu tóm, phát ngôn công khai)
- Ước tính mốc thời gian
- Chiến lược giảm thiểu

## Lựa chọn mã nguồn mở & miễn phí
- Những gì đang có
- Chất lượng và mức độ được dùng
- Tại sao người ta lại trả tiền cho giải pháp của chúng ta thay vì vậy

## Phân tích chi phí chuyển đổi
- Điều gì giữ người dùng ở lại với giải pháp hiện tại?
- Điều gì sẽ khiến họ chuyển?
- Ước tính công sức để chuyển sang sản phẩm của chúng ta

## Khoảng trống dữ liệu
- [Liệt kê những gì không tìm được]

Lưu vào: {project-name}/01-discovery/raw/indirect-competitors.md
```

---

## Agent B3: Phân tích Go-to-Market của đối thủ (Competitor Go-to-Market Analysis)

```
Nhiệm vụ nghiên cứu: Các đối thủ trong {nhóm sản phẩm} thu hút và giữ chân khách hàng như thế nào
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.
Các đối thủ chính: {liệt kê 3-5 đối thủ hàng đầu từ Agent B1}

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Kênh marketing (2-3 lượt tìm mỗi đối thủ):
- Xem website đối thủ để tìm blog, tài nguyên, webinar, case study
- "{competitor name} marketing strategy"
- Tìm quảng cáo của đối thủ (Google Ads Transparency, Facebook Ad Library)
- Xem hoạt động mạng xã hội và tần suất đăng nội dung của họ

VÒNG 2 — Cách bán hàng (2 lượt tìm):
- "{competitor name} sales team" linkedin
- "{product category} sales cycle length"
- Tìm xem: tự đăng ký (self-serve) vs. yêu cầu demo vs. "liên hệ sales"

VÒNG 3 — Nội dung & SEO (2 lượt tìm):
- "{product category} blog" — ai đang xếp hạng cho các từ khoá chính?
- Xem đối thủ trên Similarweb hoặc công cụ tương tự để ước tính traffic

ĐỊNH DẠNG ĐẦU RA:
# Phân tích Go-to-Market của đối thủ

Với từng đối thủ:
## {Tên đối thủ} — Phân tích GTM
- **Kênh thu hút chính:** {SEO / quảng cáo trả phí / outbound sales / đối tác / cộng đồng / PLG}
- **Cách bán hàng:** {self-serve / có sales hỗ trợ / enterprise sales}
- **Chiến lược nội dung:** {tần suất blog, chủ đề, đánh giá chất lượng}
- **Hiện diện mạng xã hội:** {nền tảng nào, tần suất đăng, mức tương tác}
- **Quảng cáo trả phí:** {có thấy quảng cáo không? kênh nào? thông điệp gì?}
- **Chiêu đối tác:** {tích hợp, co-marketing, đối tác kênh}
- **Giá như một công cụ GTM:** {freemium? dùng thử miễn phí? hoàn tiền?}

## Bản đồ cơ hội kênh
| Kênh | Mức bão hoà của đối thủ | Cơ hội của chúng ta | CAC ước tính |
|---------|----------------------|-----------------|---------------|
| SEO/Nội dung | Cao/Trung bình/Thấp | ... | ... |
| Tìm kiếm trả phí | ... | ... | ... |
| Mạng xã hội/Cộng đồng | ... | ... | ... |
| Outbound Sales | ... | ... | ... |
| Đối tác | ... | ... | ... |
| Product-Led Growth | ... | ... | ... |

## Điểm rút ra chính
- Điều gì đang hiệu quả với đối thủ?
- Kênh nào chưa được khai thác hết?
- Chúng ta có thể thắng ở đâu với ngân sách hạn chế?

## Khoảng trống dữ liệu
- [Liệt kê những gì không tìm được]

Lưu vào: {project-name}/01-discovery/raw/competitor-gtm.md
```
