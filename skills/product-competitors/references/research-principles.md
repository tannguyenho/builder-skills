# Nguyên tắc nghiên cứu

Các nguyên tắc này áp dụng cho TẤT CẢ agent nghiên cứu trong mọi đợt. Agent nào cũng phải tuân theo.

## Nghiên cứu sâu theo vòng lặp

Mỗi agent thực hiện **tối thiểu 5-8 lượt tìm kiếm web**, chia thành các vòng nối tiếp, càng về sau càng đào sâu:
- Vòng 1: Truy vấn tổng quan rộng
- Vòng 2: Đào sâu vào các phát hiện cụ thể từ Vòng 1
- Vòng 3: Đối chiếu chéo và xác thực
- Vòng 4: Kiểm tra thực tế và các trường hợp biên

KHÔNG dừng sau một truy vấn duy nhất. Lượt tìm đầu tiên cho bạn bề mặt — các lượt tìm tiếp theo mới cho bạn insight.

## Các bậc chất lượng nguồn

Xếp hạng mọi phát hiện theo độ tin cậy của nguồn:

| Bậc | Loại nguồn | Dùng cho |
|------|-----------|---------|
| **Tier 1** | Báo cáo ngành (Gartner, Forrester, McKinsey, IBISWorld), hồ sơ SEC, dữ liệu chính phủ, dữ liệu tổng hợp của G2/Capterra | Số liệu cứng, thị phần, chỉ số đã kiểm chứng |
| **Tier 2** | Báo công nghệ uy tín (TechCrunch, Bloomberg, WSJ), thông cáo báo chí của công ty, Crunchbase, tài liệu trình bày cho nhà đầu tư | Dữ liệu gọi vốn, tin tức công ty, ý kiến chuyên gia |
| **Tier 3** | Bài blog, thread Reddit, review cá nhân, mạng xã hội | Cảm nhận, tiếng nói khách hàng, bằng chứng mang tính giai thoại |

Với phân tích cạnh tranh, nguồn Tier 3 có giá trị hơn bình thường — review cá nhân và bài diễn đàn cho thấy trải nghiệm thật của khách hàng mà marketing bóng bẩy che đi. Nhưng đừng dùng chúng cho số liệu cứng.

## Đối chiếu chéo

Không bao giờ tin một nguồn duy nhất cho các nhận định quan trọng. Với mỗi phát hiện then chốt:
- Tìm 2-3 nguồn độc lập
- Nếu các nguồn khớp nhau: ghi nhận sự hội tụ và trích dẫn tất cả
- Nếu các nguồn lệch nhau: ghi cả hai con số, giải thích chỗ chênh lệch, và nói rõ bạn tin nguồn nào hơn và vì sao

## Định lượng

Nhận định mơ hồ là vô giá trị. Luôn cố lấy con số:
- Tệ: "Họ là một tay chơi lớn"
- Tốt: "ARR $12M, hơn 2.500 khách hàng, Series B ($28M từ Accel)"
- Tệ: "Giá của họ cao"
- Tốt: "$49/seat/tháng cho gói Pro, $99/seat/tháng cho Enterprise, so với trung vị thị trường $35/seat/tháng"

## Ghi ngày

Luôn ghi lại thời điểm dữ liệu được công bố. Đánh dấu mọi thứ cũ hơn 12 tháng là có thể đã lỗi thời. Bối cảnh đối thủ thay đổi rất nhanh — một vòng gọi vốn, một cú pivot hay một thương vụ mua lại có thể thay đổi mọi thứ chỉ trong vài tuần.

## Xử lý khi nghiên cứu thất bại

Đôi khi WebSearch không tìm được thứ bạn cần:

1. **Thử truy vấn khác.** Diễn đạt lại, dùng từ đồng nghĩa, thử góc khác. Ít nhất 3 biến thể trước khi kết luận là thiếu dữ liệu.
2. **Dùng dữ liệu đại diện (proxy).** Nếu không tìm được doanh thu của đối thủ, ước tính từ quy mô đội, số vốn gọi được, giá × số khách hàng ước tính. Trình bày cách tính.
3. **Khai báo rõ chỗ thiếu.** Ghi: "DATA GAP: Không tìm được dữ liệu đáng tin về [X]. Proxy gần nhất: [Y]. Độ tin cậy: Thấp."
4. **Không bao giờ bịa đặt.** Một câu "chưa rõ" trung thực có giá trị hơn vô cùng so với một con số bịa ra.
5. **Gợi ý cách lấp chỗ thiếu.** Chỉ ra báo cáo cụ thể, hoặc khuyên liên hệ trực tiếp khách hàng của đối thủ.
