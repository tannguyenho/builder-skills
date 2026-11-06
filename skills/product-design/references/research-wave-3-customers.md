# Wave 3: Khách hàng & nhu cầu (3 agent)

Đọc `research-principles.md` trước. Các agent Wave 3 nhận phát hiện về đối thủ từ Wave 2 làm bối cảnh.

---

## Agent C1: Tiếng nói khách hàng & nỗi đau (Customer Voice & Pain Points)

```
Nhiệm vụ nghiên cứu: Nghiên cứu khách hàng chuyên sâu — tiếng nói thật về {vấn đề}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.
Khách hàng mục tiêu: {mô tả khách hàng}
Các đối thủ chính đã tìm thấy: {danh sách từ Wave 2}

Mục tiêu là nghe người thật nói về vấn đề này bằng chính lời của họ. Điều này trực tiếp định hướng định vị, viết copy và quyết định sản phẩm.

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Đào sâu Reddit (3-4 lượt tìm):
- "site:reddit.com {problem keywords}"
- "site:reddit.com {industry} frustration"
- "site:reddit.com {existing solution} complaints"
- Duyệt các bài hàng đầu trong các subreddit liên quan: r/{industry}, r/{role}, r/{related topic}
Với mỗi thread liên quan: ghi lại bài gốc, các bình luận hàng đầu và số upvote (upvote = sự đồng tình).

VÒNG 2 — Diễn đàn chuyên môn (2-3 lượt tìm):
- "site:news.ycombinator.com {problem keywords}"
- "{problem} forum discussion"
- "{industry} community {problem}"
- Xem các diễn đàn riêng của ngành (vd Stack Overflow cho devtools, Bogleheads cho tài chính)

VÒNG 3 — Khai thác review (2-3 lượt tìm):
- "{existing solution} reviews" trên G2, Capterra, TrustRadius
- Tập trung vào review 1-3 sao — chúng lộ ra nhu cầu chưa được đáp ứng
- "{existing solution} worst thing about"

VÒNG 4 — Cảm nhận trên mạng xã hội (1-2 lượt tìm):
- "site:twitter.com {problem keywords}" HOẶC "site:linkedin.com {problem keywords}"
- "{problem} rant" HOẶC "{problem} hate"

ĐỊNH DẠNG ĐẦU RA:
# Nghiên cứu tiếng nói khách hàng: {vấn đề}

## Trích dẫn nguyên văn (Top 20)
Ghi lại nguyên văn các câu nói thể hiện nỗi đau. Với mỗi câu:
- Trích dẫn (nguyên văn)
- Nguồn (Reddit, G2, v.v. — kèm link thread/review nếu được)
- Bối cảnh (người này là ai? vai trò/ngành gì?)
- Số upvote/tín hiệu đồng tình
- Nhóm nỗi đau (xem bên dưới)

## Nhóm nỗi đau (gom từ các trích dẫn)
Với mỗi nhóm:
- Tên nỗi đau (vd "Tốn thời gian cho quy trình thủ công")
- Tần suất: nó xuất hiện thường xuyên đến đâu trên mọi nguồn?
- Cường độ: phiền nhẹ hay vấn đề "cháy nhà"?
- Các cách xoay xở hiện tại mà mọi người nhắc tới
- Các trích dẫn đại diện tốt nhất cho nỗi đau này

## Jobs-to-Be-Done (rút ra từ tiếng nói khách hàng)
- Job chức năng: họ đang cố hoàn thành điều gì?
- Job xã hội: họ muốn được người khác nhìn nhận thế nào?
- Job cảm xúc: họ muốn cảm thấy thế nào?

## Bản đồ ngôn ngữ (Language Map)
Các từ và cụm từ khách hàng thực sự dùng để mô tả:
- Vấn đề: [liệt kê nguyên văn]
- Kết quả mong muốn: [liệt kê nguyên văn]
- Sự bực bội của họ: [liệt kê nguyên văn]
Ngôn ngữ này nên được dùng nguyên văn trong định vị và copy — nó chạm đến khách hàng vì phản chiếu chính lời của họ.

## Nhu cầu chưa được đáp ứng (những thứ người ta hỏi mà chưa tồn tại)
- [Nhu cầu 1 — bằng chứng từ trích dẫn]
- [Nhu cầu 2 — bằng chứng từ trích dẫn]

## Khoảng trống dữ liệu
- [Các cộng đồng không truy cập hoặc không tìm được]
- [Các phân khúc khách hàng không có dữ liệu tiếng nói]

Lưu vào: {project-name}/01-discovery/raw/customer-voice.md
```

---

## Agent C2: Tín hiệu nhu cầu & thẩm định thị trường (Demand Signals & Market Validation)

```
Nhiệm vụ nghiên cứu: Tín hiệu nhu cầu định lượng cho {nhóm sản phẩm}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Nhu cầu tìm kiếm (2-3 lượt tìm):
- Google Trends cho: "{product category}", "{problem} solution", "{competitor name}"
- "{product category} search volume"
- "keyword research {product category}"
Ghi lại: chiều hướng xu hướng (tăng/đi ngang/giảm), tính mùa vụ, điểm nóng theo địa lý.

VÒNG 2 — Tín hiệu ra mắt sản phẩm (2 lượt tìm):
- Tìm trên Product Hunt các sản phẩm tương tự — upvote, bình luận, phản hồi của maker
- Tìm trên Indie Hackers những người đang xây trong lĩnh vực này — số doanh thu nếu được chia sẻ
- Xem các beta list / công cụ landing page để tìm sản phẩm chưa ra mắt trong lĩnh vực

VÒNG 3 — Thông tin về giá (3-4 lượt tìm):
- Vào thẳng trang giá của 5 đối thủ hàng đầu
- "{product category} pricing comparison {current year}"
- "{product category} how much do companies spend"
- "{customer type} software budget survey"
Ghi lại: các gói giá chính xác của từng đối thủ trong một bảng so sánh.

VÒNG 4 — Tín hiệu sẵn lòng chi trả (1-2 lượt tìm):
- "{product category} survey willingness to pay"
- "{problem} worth paying for"
- Xem các subreddit và diễn đàn để tìm thảo luận về giá của các công cụ tương tự

ĐỊNH DẠNG ĐẦU RA:
# Tín hiệu nhu cầu: {nhóm sản phẩm}

## Nhu cầu tìm kiếm
- Tóm tắt Google Trends: [tăng / ổn định / giảm trong khoảng thời gian nào]
- Tháng cao điểm (nếu có mùa vụ): [các tháng]
- Điểm nóng theo địa lý: [khu vực/quốc gia có mức quan tâm cao nhất]
- Truy vấn liên quan đang tăng: [liệt kê — chúng lộ ra cơ hội lân cận]

## Tín hiệu ra mắt sản phẩm
| Sản phẩm | Nền tảng | Ngày | Upvote/Đón nhận | Điểm rút ra chính |
|---------|----------|------|-------------------|-------------|
| ... | ... | ... | ... | ... |

## Bức tranh giá
| Đối thủ | Gói miễn phí | Starter | Pro | Enterprise | Mô hình |
|-----------|-----------|---------|-----|-----------|-------|
| ... | ... | ... | ... | ... | ... |

- Mức giá trung vị: $X/tháng
- Khoảng giá: $X - $Y/tháng
- Mô hình phổ biến nhất: [subscription / theo người dùng / theo mức dùng]
- Xu hướng giá: [đua xuống đáy? gói cao cấp đang tăng? tính theo mức dùng đang lên?]

## Đánh giá mức sẵn lòng chi trả (WTP)
- Bằng chứng cho WTP mạnh: [liệt kê]
- Bằng chứng cho WTP yếu: [liệt kê]
- Khoảng giá đề xuất cho startup của chúng ta: $X - $Y/tháng
- Lý do: [tại sao chọn khoảng này, dựa trên benchmark đối thủ và giá trị mang lại]

## Điểm thẩm định thị trường
- Nhu cầu tìm kiếm: Mạnh / Vừa / Yếu
- Hoạt động cạnh tranh: Cao / Trung bình / Thấp (cao = thị trường đã được chứng minh; thấp = chưa được chứng minh)
- Chi tiêu của khách hàng: Đang tăng / Ổn định / Đang giảm
- Tín hiệu nhu cầu tổng thể: [đánh giá]

## Khoảng trống dữ liệu
- [Từ khoá không có dữ liệu xu hướng]
- [Đối thủ giấu giá]

Lưu vào: {project-name}/01-discovery/raw/demand-signals.md
```

---

## Agent C3: Phác hoạ đối tượng mục tiêu (Target Audience Profiling)

```
Nhiệm vụ nghiên cứu: Nghiên cứu chuyên sâu đối tượng mục tiêu cho {mô tả khách hàng}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Dữ liệu nhân khẩu học & đặc điểm doanh nghiệp (2-3 lượt tìm):
- "{customer type} demographics statistics"
- "how many {customer type} in {geography}"
- "{customer type} company size distribution"
Ghi lại: quy mô tổng thể, dữ liệu phân khúc, phân bố địa lý.

VÒNG 2 — Mô thức hành vi (2-3 lượt tìm):
- "{customer type} software adoption habits"
- "{customer type} buying process for {product category}"
- "how do {customer type} discover new tools"
Ghi lại: họ tìm hiểu ở đâu, ai ảnh hưởng tới họ, quy trình ra quyết định.

VÒNG 3 — Một ngày của họ (2 lượt tìm):
- "{role} daily challenges"
- "{role} workflow {industry}"
Ghi lại: một ngày của họ trông thế nào, sản phẩm của chúng ta nằm ở đâu trong quy trình làm việc của họ.

VÒNG 4 — Ra quyết định (1-2 lượt tìm):
- "{product category} buying criteria"
- "who decides on {product category} at {company type}"
Ghi lại: ai là người mua, người ảnh hưởng, người cản? Chu kỳ bán hàng điển hình là bao lâu?

ĐỊNH DẠNG ĐẦU RA:
# Hồ sơ đối tượng mục tiêu: {mô tả khách hàng}

## Persona chính
- **Tên:** {tên đại diện hư cấu}
- **Vai trò:** {chức danh}
- **Công ty:** {loại công ty, quy mô, ngành}
- **Nhân khẩu học:** {độ tuổi, địa điểm, học vấn}
- **Mục tiêu:** {điều họ đang cố đạt được}
- **Nỗi bực bội:** {nỗi đau cụ thể liên quan tới vấn đề của chúng ta}
- **Công cụ hiện tại:** {hôm nay họ dùng gì}
- **Câu nói:** {một trích dẫn đại diện từ nghiên cứu tiếng nói khách hàng}

## Hành vi mua
- **Cách họ khám phá công cụ:** {kênh, nguồn}
- **Ai tham gia quyết định:** {người mua, người ảnh hưởng, người duyệt, người cản}
- **Tiêu chí quyết định:** {5 yếu tố hàng đầu đã xếp hạng}
- **Ngân sách điển hình:** {họ chi bao nhiêu cho công cụ tương tự}
- **Độ dài chu kỳ bán hàng:** {ngày/tuần/tháng}
- **Phản đối thường gặp:** {vì sao họ có thể từ chối}

## Persona phụ (nếu có)
[Cấu trúc giống persona chính]

## Anti-persona (ai KHÔNG phải khách hàng của chúng ta)
- {mô tả những ai chúng ta KHÔNG nên nhắm tới và tại sao}

## Tiếp cận họ ở đâu
| Kênh | Mật độ | Chi phí | Ghi chú |
|---------|---------|------|-------|
| {subreddit cụ thể} | ... | Miễn phí | ... |
| {nhóm LinkedIn cụ thể} | ... | ... | ... |
| {hội nghị cụ thể} | ... | ... | ... |
| {newsletter cụ thể} | ... | ... | ... |
| {podcast cụ thể} | ... | ... | ... |
| {cộng đồng cụ thể} | ... | ... | ... |

## Khoảng trống dữ liệu
- [Phân khúc đối tượng không có dữ liệu]
- [Dữ liệu hành vi không tìm được]

Lưu vào: {project-name}/01-discovery/raw/target-audience.md
```
