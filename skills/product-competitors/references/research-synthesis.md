# Tổng hợp & Battle Card

Sau khi TẤT CẢ các đợt hoàn thành (6 agent), tổng hợp các phát hiện thô thành sản phẩm hoàn chỉnh. Bước này tạo ra giá trị phân tích thật — nó nối các điểm giữa các nguồn dữ liệu để làm lộ ra những cơ hội mà từng mảnh nghiên cứu riêng lẻ không tự cho thấy được.

## Quy trình tổng hợp

### Trước khi viết

1. Đọc TẤT CẢ file thô trong `{project-name}/raw/` trước khi viết bất cứ gì
2. Tìm các mẫu xuyên suốt các nguồn — chủ đề nào lặp lại?
3. Chỉ ra mâu thuẫn giữa các nguồn và giải thích bạn tin nguồn nào hơn
4. Nối các điểm: khoảng trống giá + phàn nàn của khách + tín hiệu tuyển dụng = cơ hội

### Các kết nối giữa các đợt cần tìm

Đây là các insight giá trị cao có được khi kết hợp dữ liệu:

- **Phàn nàn + Giá = Cơ hội:** Khách hàng phàn nàn về một tính năng VÀ đối thủ tính giá cao cho nó → cạnh tranh bằng giá trị tốt hơn với giá thấp hơn
- **Tuyển dụng + Hướng đi sản phẩm = Mối đe doạ:** Đối thủ đang tuyển kỹ sư AI + changelog gần đây nhắc tới AI → họ đang nhắm vào mảng đó
- **Tín hiệu rời bỏ + Chi phí chuyển đổi = Điểm chen vào (wedge):** Người dùng muốn rời đi nhưng khó mang dữ liệu đi → biến việc chuyển đổi dễ dàng thành điểm khác biệt
- **Khoảng trống nội dung + Lượng tìm kiếm = Quick win:** Chưa ai lên top cho một từ khoá có lượng tìm kiếm cao → chiếm nó sớm
- **Mẫu review + Tính năng còn thiếu = Tính năng MVP:** Nhiều đối thủ cùng thiếu thứ khách hàng muốn → xây nó trước
- **Vốn + Quy mô đội = Kiểm tra thực tế:** Đối thủ nhiều vốn với hơn 100 kỹ sư → đừng cạnh tranh bằng tính năng, hãy cạnh tranh bằng sự tập trung

### Chấm độ tin cậy

Chấm cho mọi nhận định lớn:
- **Cao:** Nhiều nguồn Tier 1/2 khớp nhau, dữ liệu gần đây
- **Trung bình:** Có bằng chứng nhưng còn khoảng trống, hoặc các nguồn lệch nhau một phần
- **Thấp:** Ít dữ liệu, chủ yếu là suy ra, hoặc dữ liệu cũ hơn 12 tháng

---

## File đầu ra: competitors-report.md

Cấu trúc:

```markdown
# Báo cáo phân tích cạnh tranh: {market/product}
*Skill: product-competitors | Ngày tạo: {date}*

## Tóm tắt điều hành
{Tối đa 5 câu: mức độ tập trung thị trường, phát hiện chính, cơ hội lớn nhất, rủi ro lớn nhất, đánh giá tổng thể}

## Mức độ tập trung thị trường
- **Cấu trúc:** phân mảnh / đang hợp nhất / bị thống trị
- **Số người chơi đang hoạt động:** {count}
- **Mức tập trung vốn:** {tiền đang đổ vào hay đang cạn?}
- **Rào cản gia nhập:** thấp / trung bình / cao — {vì sao}

## Tổng quan các người chơi chính
| Đối thủ | Giai đoạn | Vốn | Điểm mạnh | Điểm yếu | Đe doạ |
|-----------|-------|---------|----------|----------|--------|
| ... | ... | ... | ... | ... | C/TB/T |

## Giải pháp liền kề & Sản phẩm thay thế
{Nền tảng rộng hơn, cách làm thủ công và công cụ từ các nhóm sản phẩm lân cận tranh cùng một ngân sách hoặc cùng một việc (job). Gồm: chúng giải việc gì, vì sao người mua cân nhắc chúng, và chúng so với đối thủ trực tiếp thế nào.}

## Cơ hội chiến lược
Với mỗi cơ hội:
### Cơ hội: {name}
- **Là gì:** {mô tả}
- **Bằng chứng:** {các điểm dữ liệu từ nghiên cứu}
- **Độ tin cậy:** Cao / Trung bình / Thấp
- **Cách khai thác:** {khuyến nghị cụ thể}

## Rủi ro chiến lược
Với mỗi rủi ro:
### Rủi ro: {name}
- **Là gì:** {mô tả}
- **Bằng chứng:** {các điểm dữ liệu}
- **Mức nghiêm trọng:** Cao / Trung bình / Thấp
- **Giảm thiểu:** {cách tự bảo vệ}

## Đánh giá hào cạnh tranh (moat)
Đánh giá thị trường theo 5 chiều moat:
| Loại moat | Có trên thị trường? | Ai có | Độ mạnh |
|----------|-------------------|-----------|----------|
| Hiệu ứng mạng (network effects) | có / không | {who} | mạnh / yếu |
| Chi phí chuyển đổi (switching costs) | có / không | {who} | mạnh / yếu |
| Hào dữ liệu (data moat) | có / không | {who} | mạnh / yếu |
| Thương hiệu/niềm tin | có / không | {who} | mạnh / yếu |
| Lợi thế quy mô (economies of scale) | có / không | {who} | mạnh / yếu |

{Đoạn giải thích điều này có ý nghĩa gì với một người mới gia nhập}

## Chỗ thiếu dữ liệu & Giới hạn nghiên cứu
Gom mọi chỗ thiếu dữ liệu từ các file nghiên cứu thô vào một mục duy nhất. Với mỗi chỗ thiếu:
- Dữ liệu nào đang thiếu
- Vì sao nó quan trọng cho việc ra quyết định
- Cách lấp nó (hành động cụ thể founder có thể làm)

Mục này là bắt buộc — phân tích cạnh tranh nào cũng có điểm mù. Nói rõ chúng ra giúp tạo niềm tin và tránh tự tin sai chỗ.

## Red Flags
- {flag 1 — những điều founder nên lo ngại}
- {flag 2}

## Yellow Flags
- {flag 1 — những điều cần theo dõi}
- {flag 2}
```

---

## File đầu ra: competitive-matrix.md

```markdown
# Ma trận tính năng cạnh tranh: {market}

## So sánh tính năng
| Tính năng | {Sản phẩm của bạn} | {Đối thủ 1} | {Đối thủ 2} | {Đối thủ 3} | {Đối thủ 4} |
|---------|---------------|----------|----------|----------|----------|
| {tính năng 1} | {rating} | {rating} | ... | ... | ... |
| {tính năng 2} | ... | ... | ... | ... | ... |

Thang đánh giá: Mạnh / Đạt / Yếu / Không có / Chưa rõ

## Phân tích khoảng trống
Những tính năng chưa đối thủ nào làm xuất sắc (tất cả đều Yếu hoặc Không có):
- {khoảng trống 1} — {hàm ý về cơ hội}
- {khoảng trống 2} — {hàm ý về cơ hội}

## Cơ hội tạo khác biệt
Dựa trên ma trận, các hướng tạo khác biệt rõ ràng nhất:
1. {cơ hội — xây gì và vì sao}
2. {cơ hội}
3. {cơ hội}
```

---

## File đầu ra: pricing-landscape.md

```markdown
# Bức tranh giá: {market}

## Tổng quan giá thị trường
- **Value metric phổ biến nhất:** {đa số tính tiền theo cái gì}
- **Khoảng giá:** {thấp nhất — cao nhất cho các gói tương đương}
- **Mức giá trung vị:** {cho gói tiêu chuẩn}
- **Mức phổ biến của gói miễn phí:** {X trên Y đối thủ có gói free}

## So sánh từng gói
| | {Đối thủ 1} | {Đối thủ 2} | {Đối thủ 3} | {Đối thủ 4} |
|---|----------|----------|----------|----------|
| Gói miễn phí | {gồm những gì} | ... | ... | ... |
| Gói khởi đầu | ${price} — {giới hạn} | ... | ... | ... |
| Gói giữa | ${price} — {giới hạn} | ... | ... | ... |
| Gói cao nhất | ${price} — {giới hạn} | ... | ... | ... |
| Enterprise | {giá thoả thuận?} | ... | ... | ... |

## Phân tích value metric
| Đối thủ | Value metric | Vì sao hiệu quả/không hiệu quả | Tác động khi mở rộng |
|-----------|-------------|---------------------|-------------------|
| ... | theo seat | {phân tích} | {chi phí tăng thế nào} |

## Tâm lý giá đang được dùng
| Chiến thuật | Ai dùng | Cách dùng |
|--------|---------|-----|
| Neo giá (anchoring) | {who} | {chi tiết} |
| Gói mồi (decoy tier) | {who} | {chi tiết} |
| Giá lẻ (charm pricing) | {who} | {chi tiết} |
| Ràng buộc theo năm | {who} | {% giảm giá} |

## Ma trận chi phí chuyển đổi
| Đối thủ | Chi phí kỹ thuật | Chi phí hợp đồng | Chi phí cảm xúc | Tổng thể |
|-----------|---------------|-----------------|----------------|---------|
| ... | C/TB/T | C/TB/T | C/TB/T | C/TB/T |

## Khoảng trống về giá
{Nơi còn chỗ để định vị về giá — phân khúc chưa được phục vụ, mô hình chưa ai thử, mức giá chưa ai chiếm}

## Khuyến nghị
- **Nếu cạnh tranh bằng giá:** {chiến lược}
- **Nếu cạnh tranh bằng giá trị:** {chiến lược}
- **Nếu cạnh tranh bằng mô hình:** {cách định giá khác mà chưa đối thủ nào dùng}
```

---

## Kiểm chứng sau tổng hợp

Sau khi viết xong mọi sản phẩm và battle card, chạy quy trình Agent Kiểm chứng. Xem toàn bộ quy trình ở `references/verification-agent.md`. Bước kiểm chứng rà soát mọi sản phẩm để tìm nhận định không gắn nhãn, mâu thuẫn nội bộ, độ nhất quán của mức tin cậy, và độ ăn khớp riêng của product-competitors (battle card nhất quán với báo cáo, ma trận khớp với hồ sơ, bức tranh giá nhất quán với hồ sơ, cơ hội/rủi ro truy được nguồn gốc giữa các sản phẩm).

---

## File đầu ra: battle-cards/{competitor-name}.md

Mỗi đối thủ một battle card. Giữ mỗi card trong MỘT trang — đây là công cụ tra cứu dùng nhanh, không phải tài liệu nghiên cứu sâu.

```markdown
# Battle Card: {Tên đối thủ}
*Cập nhật lần cuối: {date}*

## Nhìn nhanh
- **Họ làm gì:** {một câu}
- **Năm thành lập:** {year} | **Vốn:** {total} | **Đội:** ~{size}
- **Giá:** {range} | **Mô hình:** {value metric}
- **Phù hợp nhất cho:** {khách hàng lý tưởng của họ}

## Điểm mạnh của họ (hãy thành thật)
- {điểm mạnh 1 — kèm bằng chứng}
- {điểm mạnh 2}
- {điểm mạnh 3}

## Điểm yếu của họ (cơ hội của bạn)
- {điểm yếu 1 — kèm bằng chứng từ review/diễn đàn}
- {điểm yếu 2}
- {điểm yếu 3}

## Cách thắng họ
Luận điểm cụ thể khi khách hàng tiềm năng đang cân nhắc cả hai:
- **Khi khách nói "{phản đối}",** trả lời: {phản biện kèm bằng chứng}
- **Khi khách nói "{phản đối}",** trả lời: {phản biện}
- **Mở đầu bằng:** {điểm khác biệt mạnh nhất của bạn so với riêng đối thủ này}

## Khi nào họ thắng bạn
Thành thật về những lúc đối thủ là lựa chọn tốt hơn:
- {tình huống 1 — vd "Đội enterprise cần SSO và audit log"}
- {tình huống 2}

## Phàn nàn hàng đầu của khách hàng họ
"{trích dẫn nguyên văn từ review}" — {nguồn}
Điều này quan trọng vì: {hàm ý chiến lược}

## Điểm yếu then chốt
{Điểm yếu lớn nhất duy nhất bạn có thể khai thác — kèm bằng chứng}

## Tín hiệu rời bỏ
Vì sao khách hàng của họ rời đi:
- {lý do 1} — tần suất: thường gặp / thỉnh thoảng
- {lý do 2}

## Cần để ý
{Đối thủ này nhiều khả năng sẽ làm gì tiếp theo, dựa trên các tín hiệu chiến lược}
```
