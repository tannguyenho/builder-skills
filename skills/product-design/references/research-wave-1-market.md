# Wave 1: Bức tranh thị trường (3 agent)

Đọc `research-principles.md` trước để nắm các quy tắc xuyên suốt về chất lượng nguồn, đối chiếu chéo và định lượng.

---

## Agent A1: Quy mô thị trường & kinh tế học (Market Sizing & Economics)

```
Nhiệm vụ nghiên cứu: Định cỡ thị trường chuyên sâu cho {ngành/nhóm sản phẩm}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.
Thị trường mục tiêu: {khu vực địa lý}, {phân khúc khách hàng}

QUY TRÌNH NGHIÊN CỨU — thực hiện các lượt tìm theo thứ tự, lượt sau xây trên lượt trước:

VÒNG 1 — Tổng quan thị trường rộng (2-3 lượt tìm):
- "{broad category} market size {current year}"
- "{broad category} market report {current year}"
- "{industry} industry overview statistics"
Ghi lại: Số liệu TAM, tốc độ tăng trưởng, người chơi chính. Ghi chú báo cáo nào được trích dẫn nhiều nhất.

VÒNG 2 — Đào sâu phân khúc (2-3 lượt tìm):
- "{specific segment} market size {geography}"
- "{specific segment} spending trends"
- "{customer type} budget for {product category}"
Ghi lại: Số liệu SAM, tăng trưởng riêng của phân khúc, mô hình chi tiêu trên mỗi khách hàng.

VÒNG 3 — Nghiên cứu unit economics (2-3 lượt tìm):
- "{product category} average contract value"
- "{product category} customer acquisition cost benchmarks"
- "{product category} churn rate benchmarks"
- "{product category} pricing survey"
Ghi lại: Benchmark của ngành cho ACV, CAC, LTV, churn. Những số này làm nền cho mô hình tài chính về sau.

VÒNG 4 — Kiểm tra thực tế (1-2 lượt tìm):
- "{product category} market challenges {current year}"
- "why {product category} startups fail"
Ghi lại: Lực cản, tín hiệu bão hoà, các kiểu thất bại phổ biến.

ĐỊNH DẠNG ĐẦU RA:
# Quy mô thị trường: {ngành}

## TAM (Total Addressable Market — tổng thị trường có thể nhắm tới)
- Số liệu: $X (Nguồn, Ngày)
- Số liệu: $Y (Nguồn, Ngày) — [ghi chú nếu khác và tại sao]
- Tốc độ tăng trưởng: CAGR X% (Nguồn)

## SAM (Serviceable Addressable Market — thị trường có thể phục vụ)
- Phân khúc: {phân khúc cụ thể}
- Số liệu: $X (Nguồn, Ngày)
- Lập luận: [SAM được suy ra từ TAM như thế nào]

## SOM (Serviceable Obtainable Market — thị trường có thể giành được)
- Mức giành được thực tế ở Năm 1: $X
- Lập luận: [dựa trên quỹ đạo của các công ty tương đương]

## Benchmark unit economics
- Giá trị hợp đồng trung bình: $X/tháng hoặc $X/năm
- Chi phí thu hút khách hàng (CAC): $X
- Giá trị vòng đời (LTV): $X
- Tỉ lệ churn: X%/tháng hoặc X%/năm
- [Ghi chú benchmark là cho đúng phân khúc này hay cho ngành rộng hơn]

## Lực cản & rủi ro thị trường
- [Liệt kê các thách thức cụ thể kèm nguồn]

## Đánh giá chất lượng nguồn
- [Xếp từng nguồn chính vào Tier 1/2/3 và ghi chú mọi khoảng trống dữ liệu]

## Khoảng trống dữ liệu
- [Liệt kê những gì không tìm được, kèm cách gợi ý để lấp khoảng trống]

Lưu vào: {project-name}/01-discovery/raw/market-size.md
```

---

## Agent A2: Xu hướng ngành & thời điểm (Industry Trends & Timing)

```
Nhiệm vụ nghiên cứu: Xu hướng ngành, tín hiệu thời điểm và quỹ đạo tương lai của {ngành}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.

QUY TRÌNH NGHIÊN CỨU — thực hiện các lượt tìm theo thứ tự:

VÒNG 1 — Xu hướng công nghệ (2-3 lượt tìm):
- "{industry} technology trends {current year}"
- "AI impact on {industry}"
- "{industry} innovation report {current year}"
Ghi lại: Công nghệ nào đang định hình lại lĩnh vực. Đường cong chấp nhận. Mức độ trưởng thành.

VÒNG 2 — Hoạt động đầu tư & M&A (2-3 lượt tìm):
- "{industry} startup funding {current year}"
- "{industry} acquisitions {current year}"
- "{product category} venture capital deals"
Tìm trên Crunchbase, các bản tóm tắt của PitchBook, các bài tổng hợp gọi vốn của TechCrunch.
Ghi lại: Quy mô thương vụ, công ty đi thâu tóm (tín hiệu cho thấy ông lớn thấy giá trị ở đâu), đầu tư đang tăng tốc hay chậm lại.

VÒNG 3 — Chuyển dịch hành vi (2 lượt tìm):
- "{customer type} changing expectations {industry}"
- "remote work impact on {industry}" HOẶC "{customer type} digital adoption"
Ghi lại: Hành vi khách hàng đang thay đổi thế nào. Kỳ vọng mới. Chuyển dịch giữa các thế hệ.

VÒNG 4 — Dự đoán của chuyên gia (1-2 lượt tìm):
- "{industry} predictions {current year + 1}"
- "{industry} future outlook analyst"
Ghi lại: Các nhà phân tích đáng tin nghĩ lĩnh vực này đang đi về đâu. Quan điểm đồng thuận vs. quan điểm ngược dòng.

ĐỊNH DẠNG ĐẦU RA:
# Xu hướng ngành: {ngành}

## Xu hướng công nghệ
Với mỗi xu hướng:
- Tên và mô tả xu hướng
- Giai đoạn chấp nhận hiện tại (sớm/đang tăng/trưởng thành/suy giảm)
- Tác động tới startup của chúng ta (cơ hội/đe doạ/trung tính)
- Mốc thời gian: khi nào nó thành phổ biến?
- Nguồn và ngày

## Hoạt động đầu tư
- Tổng vốn vào lĩnh vực (12 tháng gần nhất): $X qua N thương vụ
- Các vòng gọi vốn đáng chú ý: [công ty, số tiền, giai đoạn, ngày]
- Các thương vụ thâu tóm đáng chú ý: [bên mua → bên bị mua, số tiền, ngày, lý do chiến lược]
- Xu hướng đầu tư: tăng tốc / ổn định / chậm lại
- Điều này báo hiệu gì cho startup của chúng ta

## Chuyển dịch hành vi
- [Chuyển dịch cụ thể kèm dữ liệu]
- [Điều này ảnh hưởng thế nào tới nhu cầu cho sản phẩm của chúng ta]

## Dự đoán của chuyên gia
- [Dự đoán, nguồn, đánh giá độ uy tín]

## Đánh giá thời điểm
- Bây giờ có phải thời điểm tốt để vào thị trường này không? Tại sao có hoặc không?
- Điều gì sẽ làm thời điểm tốt hơn hoặc tệ hơn?

## Khoảng trống dữ liệu
- [Liệt kê những gì không tìm được]

Lưu vào: {project-name}/01-discovery/raw/trends.md
```

---

## Agent A3: Bức tranh pháp lý & tuân thủ (Regulatory & Compliance Landscape)

Bỏ agent này nếu startup không có rủi ro pháp lý rõ ràng. Khi phân vân, cứ chạy — phát hiện yêu cầu pháp lý sớm vẫn tốt hơn muộn.

```
Nhiệm vụ nghiên cứu: Bức tranh pháp lý của {ngành} tại {khu vực địa lý}
Bối cảnh: Chúng ta đang thiết kế một startup {mô tả một câu}.

QUY TRÌNH NGHIÊN CỨU:

VÒNG 1 — Quy định hiện hành (2-3 lượt tìm):
- "{industry} regulations {geography} {current year}"
- "{product type} compliance requirements"
- "{industry} licensing requirements {geography}"

VÒNG 2 — Dữ liệu & quyền riêng tư (2 lượt tìm):
- "{industry} data privacy requirements"
- "GDPR CCPA impact on {industry}" HOẶC "{industry} data handling regulations"

VÒNG 3 — Thay đổi sắp tới (1-2 lượt tìm):
- "{industry} new regulations {current year}"
- "{industry} regulatory changes pending legislation"

VÒNG 4 — Thực thi & tiền lệ (1 lượt tìm):
- "{industry} regulatory enforcement actions" HOẶC "{industry} compliance fines"

ĐỊNH DẠNG ĐẦU RA:
# Bức tranh pháp lý: {ngành} tại {khu vực địa lý}

## Quy định hiện hành
Với mỗi quy định:
- Tên và phạm vi tài phán
- Nó yêu cầu gì
- Áp dụng cho ai (có áp dụng cho chúng ta lúc ra mắt không? Khi mở rộng quy mô?)
- Ước tính chi phí tuân thủ
- Thời gian để đạt tuân thủ

## Dữ liệu & quyền riêng tư
- Các khung quy định áp dụng (GDPR, CCPA, HIPAA, v.v.)
- Yêu cầu xử lý dữ liệu riêng của ngành này
- Tác động tới kiến trúc sản phẩm

## Thay đổi sắp tới
- Dự luật đang chờ hoặc quy định đang được đề xuất
- Mốc thời gian dự kiến
- Tác động tiềm năng

## Ước tính chi phí tuân thủ
- Mức tuân thủ tối thiểu khả thi: $X (những gì cần lúc ra mắt)
- Tuân thủ đầy đủ: $X (những gì cần khi mở rộng quy mô)
- Chứng nhận cần có: [SOC 2, ISO 27001, HIPAA, v.v.]

## Đánh giá rủi ro
- Mức rủi ro pháp lý: Thấp / Trung bình / Cao
- Các rủi ro pháp lý chính cho riêng startup này

## Khoảng trống dữ liệu
- [Liệt kê những gì không tìm được]

Lưu vào: {project-name}/01-discovery/raw/regulatory.md
```
