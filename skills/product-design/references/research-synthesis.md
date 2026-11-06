# Quy trình tổng hợp nghiên cứu (Research Synthesis Protocol)

Sau khi TẤT CẢ wave hoàn tất (10-11 agent, tuỳ việc A3/Pháp lý có bị bỏ hay không), tổng hợp các phát hiện thô thành sản phẩm bàn giao hoàn chỉnh. Bước này tạo ra giá trị phân tích thực sự — không phải sao chép, mà là kết nối.

## Cách tổng hợp

Đây là việc suy luận, không phải chép lại. Đọc hết mọi thứ trước, rồi nghĩ thật kỹ xem tất cả có nghĩa gì trước khi viết bất kỳ sản phẩm bàn giao nào — những mối liên kết bạn rút ra ở đây chính là giá trị phân tích mà founder đang trả công. Đi qua các bước sau một cách có chủ đích thay vì vội vàng điền vào template:

1. **Đọc mọi file thô** trong `01-discovery/raw/` trước khi viết bất cứ gì.
2. **Tìm mô thức** xuyên suốt các nguồn: chủ đề nào lặp lại? Điều gì làm bạn bất ngờ?
3. **Xác định mâu thuẫn** giữa các nguồn và giải thích bạn tin nguồn nào hơn và tại sao.
4. **Nối các điểm** giữa các mảng nghiên cứu: khoảng trống cạnh tranh liên quan thế nào tới nỗi đau khách hàng? Xu hướng thị trường ảnh hưởng thế nào tới go-to-market?
5. **Làm nổi bật hàm ý chiến lược** — đừng chỉ báo cáo sự kiện; nói rõ chúng có ý nghĩa gì với startup này.
6. **Đánh giá độ tin cậy** cho từng phát hiện chính: Cao (nhiều nguồn Tier 1 khớp nhau), Trung bình (có bằng chứng nhưng còn khoảng trống), Thấp (dữ liệu hạn chế, chủ yếu là suy luận).
7. **Gom các khoảng trống dữ liệu** từ mọi file thô và trình bày rõ ràng — chúng trở thành đầu vào cho Phase 8 (Validation).

## File đầu ra

### `01-discovery/market-analysis.md`
Tổng hợp từ: `raw/market-size.md`, `raw/trends.md`, `raw/regulatory.md`, `raw/geographic.md`

Cấu trúc:
- **Tóm tắt điều hành** (tổng quan 5 câu về cơ hội thị trường)
- **Quy mô thị trường** với phân rã TAM/SAM/SOM và mức độ tin cậy
- **Quỹ đạo tăng trưởng** với các động lực chính và lực cản
- **Đánh giá độ trưởng thành của thị trường** (mới nổi / đang tăng trưởng / trưởng thành / suy giảm)
- **Benchmark unit economics** (lấy từ phần định cỡ thị trường, được Phase 7 dùng)
- **Tóm tắt pháp lý** (yêu cầu chính, chi phí tuân thủ, mốc thời gian)
- **Phân tích địa lý** (thị trường đầu cầu, lộ trình mở rộng)
- **Đánh giá thời điểm:** tại sao là bây giờ? Có những lực đẩy và lực cản nào?
- **Khoảng trống dữ liệu** gom từ mọi nghiên cứu liên quan tới thị trường

### `01-discovery/competitor-landscape.md`
Tổng hợp từ: `raw/direct-competitors.md`, `raw/indirect-competitors.md`, `raw/competitor-gtm.md`

Cấu trúc:
- **Tổng quan cạnh tranh** (đông đúc đến đâu, mức độ tập trung thị trường, mức đe doạ tổng thể)
- **Ma trận so sánh đối thủ** (bảng tính năng × đối thủ)
- **Bản đồ định vị** (mô tả các đối thủ tự định vị thế nào, khoảng trống ở đâu)
- **Tóm tắt GTM của đối thủ** (kênh thu hút nào hiệu quả, kênh nào đã bão hoà)
- **Đánh giá rủi ro nền tảng** (nền tảng nào có thể nuốt chức năng của chúng ta)
- **Phân tích chi phí chuyển đổi** (điều gì giữ người dùng ở lại với giải pháp hiện tại)
- **Khuyến nghị chiến lược:** cạnh tranh ở đâu, tránh ở đâu, khác biệt hoá thế nào
- **Phân tích điểm yếu:** đối thủ nào yếu nhất và tại sao — chúng ta có thể thắng ở đâu?
- **Khoảng trống dữ liệu**

### `01-discovery/target-audience.md`
Tổng hợp từ: `raw/customer-voice.md`, `raw/target-audience.md`, `raw/demand-signals.md`

Cấu trúc:
- **Persona chính** (sống động, có dữ liệu hậu thuẫn, kèm trích dẫn đại diện)
- **Persona phụ** (nếu có)
- **Anti-persona** (ai KHÔNG nên nhắm tới)
- **Thứ bậc nỗi đau của khách hàng** (xếp theo tần suất × cường độ, từ tiếng nói khách hàng)
- **Khung jobs-to-be-done** (chức năng, xã hội, cảm xúc)
- **Bản đồ ngôn ngữ** (nguyên văn từ ngữ khách hàng dùng — đưa thẳng vào việc viết copy)
- **Hành vi mua** (quy trình quyết định, tiêu chí, độ dài chu kỳ, phản đối)
- **Tiếp cận họ ở đâu** (các kênh đã xếp hạng kèm mật độ và chi phí)
- **Thẩm định nhu cầu** (xu hướng tìm kiếm, bằng chứng WTP, điểm thẩm định thị trường)
- **Khoảng trống dữ liệu**

### `01-discovery/industry-trends.md`
Tổng hợp từ: `raw/trends.md`, `raw/regulatory.md`, `raw/demand-signals.md`

Cấu trúc:
- **Xu hướng vĩ mô** ảnh hưởng tới ngành (kèm mốc thời gian và đánh giá tác động)
- **Chuyển dịch công nghệ** và đường cong chấp nhận của chúng
- **Tín hiệu đầu tư và M&A** (dòng tiền thông minh đang làm gì)
- **Chuyển dịch hành vi** của khách hàng mục tiêu
- **Quỹ đạo pháp lý** (hướng đang đi, không chỉ trạng thái hiện tại)
- **Điều này có ý nghĩa gì với startup của chúng ta** — hàm ý chiến lược rõ ràng
- **Bảng điểm thời điểm:** bây giờ có đúng lúc không? Đánh giá: lực đẩy vs. lực cản
- **Khoảng trống dữ liệu**

### `01-discovery/confidence-dashboard.md`
Tổng hợp từ: TẤT CẢ file thô của mọi wave.

Cấu trúc:
- **Tổng quan** — Bao nhiêu phần của phân tích đứng trên nền vững vs. trên lớp băng mỏng
- Bảng **độ tin cậy theo từng khẳng định**:

| Khẳng định | Tier nguồn | Số nguồn xác nhận | Độ tin cậy | Tuổi dữ liệu |
|-------|-----------|------------------------|------------|----------|
| {khẳng định chính từ nghiên cứu} | 1/2/3 | {số lượng} | Cao/Trung bình/Thấp | {ngày hoặc khoảng thời gian} |

- **Phát hiện có độ tin cậy cao nhất** — Các khẳng định được nhiều nguồn Tier 1 hậu thuẫn
- **Phát hiện có độ tin cậy thấp nhất** — Các khẳng định dựa trên một nguồn duy nhất, dữ liệu suy luận, hoặc thông tin cũ
- **Ẩn số then chốt** — Những điều chúng ta chưa biết mà có thể làm thay đổi chiến lược
- **Khuyến nghị** — Founder nên kiểm chứng điều gì trước, và bằng cách nào

File này giúp founder hiểu chỗ nào họ đang đứng trên nền vững và chỗ nào đang ra quyết định dựa trên dữ liệu yếu. Nó là lớp "meta" nằm trên 4 sản phẩm bàn giao còn lại.

---

## Liên kết giữa các tài liệu

Sau khi viết xong cả 4 file, thêm một mục "Liên kết chiến lược" ở cuối mỗi file, nối tới insight từ các tài liệu khác. Ví dụ:

- Trong market-analysis.md: "Sự tăng trưởng của [xu hướng X] (xem industry-trends.md) mở ra cơ hội ở [phân khúc Y] mà [đối thủ Z] (xem competitor-landscape.md) chưa xử lý."
- Trong target-audience.md: "Độ nhạy giá tìm thấy ở đây khớp với khoảng $X-Y từ phân tích giá của đối thủ (xem competitor-landscape.md)."

Các liên kết này giúp Phase 4 (Strategy) xây trên nghiên cứu cụ thể thay vì những khẳng định trừu tượng.

## Kiểm chứng sau tổng hợp

Sau khi viết xong mọi sản phẩm bàn giao, chạy quy trình Verification Agent. Xem `references/verification-agent.md` để có quy trình đầy đủ. Bước kiểm chứng rà mọi sản phẩm bàn giao để tìm khẳng định chưa gắn nhãn, mâu thuẫn nội bộ, độ nhất quán của mức độ tin cậy, và tính mạch lạc giữa các phase riêng của product-design (chiến lược phản ánh dữ liệu thị trường, sản phẩm phản ánh nỗi đau khách hàng, tài chính phản ánh mô hình kinh doanh, thẩm định bao phủ các rủi ro đã xác định).

## Dọn dẹp

Giữ lại thư mục `raw/` để tham khảo. Ghi chú trong PROGRESS.md rằng các file nghiên cứu thô có ở `01-discovery/raw/`.
