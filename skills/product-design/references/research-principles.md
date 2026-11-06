# Nguyên tắc nghiên cứu (Research Principles)

Các nguyên tắc này áp dụng cho TẤT CẢ agent nghiên cứu ở mọi wave. Agent nào cũng phải tuân theo.

## Nghiên cứu sâu theo vòng lặp

Mỗi agent thực hiện **tối thiểu 5-8 lượt tìm kiếm web**, chia thành các vòng tuần tự, vòng sau đào sâu hơn:
- Vòng 1: Truy vấn tổng quan rộng
- Vòng 2: Đào sâu vào các phát hiện cụ thể từ Vòng 1
- Vòng 3: Đối chiếu chéo và kiểm chứng
- Vòng 4: Kiểm tra thực tế và các trường hợp biên

KHÔNG dừng sau một truy vấn duy nhất. Lượt tìm đầu tiên cho bạn bề mặt — các lượt tìm tiếp theo mới cho bạn insight.

## Các tier chất lượng nguồn

Xếp hạng mọi phát hiện theo độ tin cậy của nguồn:

| Tier | Loại nguồn | Dùng cho |
|------|-----------|---------|
| **Tier 1** | Báo cáo ngành (Gartner, Forrester, McKinsey, IBISWorld), hồ sơ SEC, dữ liệu chính phủ, bài báo học thuật | Số liệu cứng, quy mô thị trường, tốc độ tăng trưởng |
| **Tier 2** | Báo công nghệ uy tín (TechCrunch, Bloomberg, WSJ), thông cáo báo chí của công ty, tài liệu trình bày nhà đầu tư | Dữ liệu gọi vốn, tin tức công ty, ý kiến chuyên gia |
| **Tier 3** | Bài blog, bài quan điểm, mạng xã hội | Cảm nhận, tiếng nói khách hàng, bằng chứng giai thoại |

Một nguồn Tier 3 nói "thị trường là $5B" thì không đáng tin. Một báo cáo Tier 1 nói điều tương tự thì đáng tin.

## Đối chiếu chéo

Không bao giờ tin một nguồn duy nhất cho các khẳng định quan trọng. Với mỗi phát hiện chính:
- Tìm 2-3 nguồn độc lập
- Nếu các nguồn khớp nhau: ghi nhận sự hội tụ và trích dẫn tất cả
- Nếu các nguồn lệch nhau: ghi cả hai con số, giải thích chỗ chênh lệch, và nói bạn tin nguồn nào hơn và tại sao

## Định lượng

Khẳng định mơ hồ là vô giá trị. Luôn cố tìm con số:
- Kém: "Thị trường đang tăng trưởng nhanh"
- Tốt: "Thị trường $4.2B tăng trưởng CAGR 12.3% (Grand View Research, 2025)"
- Kém: "Nhiều công ty dùng cái này"
- Tốt: "67% công ty quy mô vừa cho biết đang dùng ít nhất một công cụ tự động hoá AP (Ardent Partners, 2025)"

## Ghi ngày

Luôn ghi thời điểm dữ liệu được công bố. Gắn cờ mọi thứ cũ hơn 18 tháng là có thể đã lỗi thời. Thị trường có thể thay đổi đáng kể trong khoảng đó, nhất là ngành công nghệ.

## Xử lý khi nghiên cứu thất bại

Đôi khi WebSearch không tìm được thứ bạn cần. Khi đó:

1. **Thử truy vấn khác.** Diễn đạt lại, dùng từ đồng nghĩa, thử góc khác. Ít nhất 3 biến thể trước khi kết luận là có khoảng trống.
2. **Dùng dữ liệu đại diện (proxy).** Nếu không tìm được quy mô thị trường cho đúng phân khúc của bạn, tìm thị trường rộng hơn và ước tính tỉ trọng của phân khúc. Trình bày cách tính.
3. **Khai báo khoảng trống rõ ràng.** Ghi: "KHOẢNG TRỐNG DỮ LIỆU: Không tìm được dữ liệu đáng tin về [X]. Proxy gần nhất: [Y]. Độ tin cậy: Thấp."
4. **Không bao giờ bịa.** Nếu không có dữ liệu, nói vậy. Một câu "chưa biết" trung thực có giá trị hơn vô cùng so với một con số bịa ra.
5. **Gợi ý cách lấp khoảng trống.** Chỉ ra các báo cáo cụ thể có thể có dữ liệu (kể cả khi phải trả phí), hoặc đề xuất nghiên cứu sơ cấp mà founder có thể tự làm.
