# Đặc tả đầu ra theo phase (Phase Output Specifications)

Yêu cầu từng file cho các phase Strategy, Brand, Product và Validation. Đọc mục của phase bạn đang chạy — các đặc tả này định nghĩa mỗi sản phẩm bàn giao phải chứa gì.

**Nội dung:** Phase 4 — Strategy · Phase 5 — Brand · Phase 6 — Product · Phase 8 — Validation

---

## Phase 4 — Strategy (`02-strategy/`)

### lean-canvas.md

Dựng một Lean Canvas đầy đủ (mô hình kinh doanh 1 trang):
- Vấn đề (Problem — top 3)
- Phân khúc khách hàng (Customer Segments)
- Tuyên bố giá trị độc nhất (Unique Value Proposition)
- Giải pháp (Solution)
- Kênh (Channels)
- Dòng doanh thu (Revenue Streams)
- Cấu trúc chi phí (Cost Structure)
- Chỉ số chính (Key Metrics)
- Lợi thế không công bằng (Unfair Advantage)

### value-proposition.md

- Value proposition canvas (jobs-to-be-done, pains, gains)
- Sản phẩm xử lý từng nỗi đau (pain) và tạo ra từng lợi ích (gain) như thế nào
- Tuyên bố giá trị một câu
- Bằng chứng (proof points) và tín hiệu tạo uy tín

### business-model.md

- Mô hình doanh thu (tiền vào bằng cách nào, các gói giá)
- Unit economics (CAC, LTV, biên lợi nhuận — kể cả ước tính thô)
- Các cân nhắc về khả năng mở rộng
- Phụ thuộc và đối tác chính

### positioning.md

Dùng framework định vị của April Dunford:
- Lựa chọn thay thế cạnh tranh (Competitive alternatives — điều gì xảy ra nếu bạn không tồn tại)
- Thuộc tính độc nhất (Unique attributes — bạn có gì mà các lựa chọn thay thế không có)
- Giá trị (Value — các thuộc tính đó mang lại điều gì cho khách hàng)
- Thị trường mục tiêu (Target market — ai quan tâm nhất)
- Hạng mục thị trường (Market category — bối cảnh khiến giá trị trở nên hiển nhiên)

### go-to-market.md

- Chiến lược ra mắt (ở đâu, thế nào, tới ai trước)
- Kế hoạch 100 khách hàng đầu tiên
- Các kênh tăng trưởng xếp theo tác động và chi phí kỳ vọng
- Đối tác và các nước đi trong hệ sinh thái
- Dòng thời gian kèm cột mốc

---

## Phase 5 — Brand (`03-brand/`)

### mission-vision-values.md

- **Sứ mệnh (Mission)** — Vì sao công ty tồn tại (thì hiện tại, hướng hành động)
- **Tầm nhìn (Vision)** — Thế giới bạn đang hướng tới (truyền cảm hứng nhưng đáng tin)
- **Giá trị (Values)** — 3-5 giá trị cốt lõi kèm giải thích ngắn về ý nghĩa của chúng trong thực tế (không phải khẩu hiệu sáo rỗng — giá trị phải giúp ra quyết định)

Tạo 2-3 phương án cho sứ mệnh và tầm nhìn để user chọn hoặc phối lại.

### tone-of-voice.md

- Đặc điểm tính cách thương hiệu (3-4 tính từ kèm định nghĩa)
- Nguyên tắc giọng điệu kèm ví dụ "chúng tôi là / chúng tôi không là"
- Mẫu văn bản: thương hiệu nghe thế nào trong các bối cảnh khác nhau (tiêu đề trang chủ, thông báo lỗi, bài đăng mạng xã hội, email gửi khách hàng)
- Hướng dẫn từ vựng: từ nên dùng vs. từ nên tránh

### brand-personality.md

- Phân tích nguyên mẫu thương hiệu (brand archetype — nguyên mẫu nào phù hợp và tại sao)
- Thuộc tính cảm xúc
- Gợi ý định hướng hình ảnh (không phải thiết kế hoàn chỉnh, mà là tính từ và tham khảo)
- Thương hiệu nên tạo cảm giác thế nào so với đối thủ

---

## Phase 6 — Product (`04-product/`)

### mvp-definition.md

- Giả thuyết cốt lõi mà MVP kiểm tra
- Tính năng bắt buộc (bộ tối thiểu để kiểm tra giả thuyết)
- Tính năng nên có (cho v1.1, không phải v1.0)
- Rõ ràng nằm ngoài phạm vi (ngăn phình phạm vi — scope creep)
- Tiêu chí thành công: kết quả nào sẽ thẩm định được MVP

### feature-prioritization.md

- Danh sách tính năng với ưu tiên theo RICE hoặc MoSCoW
- Phụ thuộc giữa các tính năng
- Ước lượng công sức (theo cỡ áo — T-shirt sizing: S/M/L/XL)
- Thứ tự xây đề xuất

### user-journey.md

- Bản đồ hành trình người dùng từ đầu đến cuối (từ lúc khám phá đến lúc dùng thường xuyên)
- Điểm chạm chính và cảm xúc ở từng giai đoạn
- Rủi ro rơi rụng và ý tưởng giảm thiểu
- "Khoảnh khắc aha" — khi nào người dùng lần đầu trải nghiệm giá trị?

---

## Phase 8 — Validation (`06-validation/`)

### validation-playbook.md

- Danh sách thí nghiệm theo thứ tự, từ rẻ/nhanh nhất đến đắt nhất
- Với mỗi thí nghiệm:
  - Nó kiểm tra giả định nào
  - Cách chạy (từng bước)
  - Đo gì
  - Kết quả nào xác nhận vs. bác bỏ giả định
  - Ước tính thời gian và chi phí
- Ví dụ: thử nghiệm landing page, fake door test, concierge MVP, phỏng vấn khách hàng, thử nghiệm chiến dịch quảng cáo, wizard of oz, bán trước (pre-sales)
- Nếu phỏng vấn khách hàng đã bị hoãn ở Phase 3.7, chúng là thí nghiệm #1 — không có ngoại lệ

Điều chỉnh thí nghiệm theo đúng ý tưởng cụ thể — một B2B SaaS cần cách thẩm định khác với một marketplace tiêu dùng.

### risk-analysis.md

- Ma trận rủi ro (khả năng xảy ra × mức tác động) cho:
  - Rủi ro thị trường (không có nhu cầu, thời điểm, pháp lý)
  - Rủi ro sản phẩm (không xây được, không chạy được)
  - Rủi ro kinh doanh (không kiếm tiền được, không mở rộng được)
  - Rủi ro đội ngũ (thiếu kỹ năng, xung đột giữa các founder)
  - Rủi ro tài chính (runway, CAC quá cao)
- Với mỗi rủi ro ưu tiên cao: chiến lược giảm thiểu và tín hiệu cảnh báo sớm

### assumptions-tracker.md

- Mọi giả định then chốt mà business plan dựa vào
- Mức độ tin cậy hiện tại (cao/trung bình/thấp)
- Cách kiểm tra từng giả định
- Trạng thái: chưa kiểm tra / đang kiểm tra / đã xác nhận / đã bị bác bỏ

Định dạng thành bảng để dễ đọc lướt và cập nhật.

### experiment-design.md

- Thiết kế chi tiết cho 3 thí nghiệm được đề xuất hàng đầu
- Giả thuyết, phương pháp, chỉ số, tiêu chí thành công, dòng thời gian
- Template founder có thể dùng ngay (kịch bản phỏng vấn, câu hỏi khảo sát, dàn ý copy cho landing page)

### kill-criteria.md

Định nghĩa 5-7 điều kiện cụ thể, đo được mà khi xảy ra thì founder nên dừng hoặc pivot. Gắn mỗi điều kiện với một thí nghiệm thẩm định. Cụ thể: "Nếu ít hơn 3/10 người được phỏng vấn nói sẽ trả $X" chứ không phải "nếu không có nhu cầu." Điều này bảo vệ founder khỏi tư duy chi phí chìm (sunk cost).

### scorecard.md

Tạo một bảng điểm tóm tắt:

| Chiều đánh giá | Điểm (1-10) | Lý do |
|-----------|-------------|-----------|
| Mức nghiêm trọng của vấn đề | | |
| Quy mô thị trường | | |
| Lợi thế cạnh tranh | | |
| Tính khả thi | | |
| Độ rõ ràng của mô hình kinh doanh | | |
| Độ phù hợp founder-thị trường | | |
| Thời điểm | | |
| **Tổng thể** | | |

Hãy trung thực. Nếu ý tưởng có điểm yếu, nói rõ. Mục tiêu là giúp founder ra quyết định đúng, không phải xoa dịu cái tôi của họ. Thêm một đoạn **Kết luận** (Verdict) rõ ràng sau bảng, với khuyến nghị không mập mờ (xem thang chấm điểm trong Giao thức trung thực triệt để).
