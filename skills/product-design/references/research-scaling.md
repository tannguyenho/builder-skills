# Quy trình điều chỉnh quy mô nghiên cứu (Research Scaling Protocol)

Điều chỉnh động giúp thay đổi độ sâu nghiên cứu theo độ phức tạp của thị trường và mong muốn của user. Đánh giá sau intake, trước khi bắt đầu nghiên cứu.

## Điểm độ phức tạp

Đánh giá ba yếu tố từ dữ liệu intake:

| Yếu tố | Thấp (1) | Trung bình (2) | Cao (3) |
|--------|---------|------------|----------|
| **Độ rộng thị trường** | Siêu ngách, ít người chơi, phân khúc được định nghĩa rõ | Thị trường xác định, cạnh tranh vừa phải | Thị trường rộng, nhiều phân khúc, người chơi đa dạng |
| **Số đối thủ đã biết** | Xác định được 0-2 | Xác định được 3-5 | Xác định được 6+ |
| **Phạm vi địa lý** | Một quốc gia | Khu vực (vd châu Âu, Bắc Mỹ) | Toàn cầu hoặc nhiều khu vực |

**Điểm độ phức tạp** = tổng ba yếu tố (khoảng: 3-9)

## Các tier độ sâu nghiên cứu

| Tier | Khoảng điểm | Kích hoạt thủ công | Mô tả |
|------|-----------|----------------|-------------|
| **Light** | 3-4 | User nói "light", "nhanh", "quick" hoặc "fast research" | Quét nhanh, ít agent hơn, 2-3 vòng tìm kiếm |
| **Standard** | 5-7 | Mặc định (không cần ghi đè) | Hành vi hiện tại, độ sâu cân bằng |
| **Deep** | 8-9 | User nói "deep", "kỹ", "thorough" hoặc "deep research" | Nhiều agent hơn, 5-6 vòng tìm kiếm, phủ thêm nội dung |

**Ghi đè thủ công luôn thắng.** Nếu user yêu cầu "light" cho một thị trường điểm 9, dùng Light. Nếu họ yêu cầu "deep" cho thị trường điểm 3, dùng Deep.

## Trao đổi với user

Sau khi tính điểm, hiển thị cho user:

```
## Độ sâu nghiên cứu (Research Depth)

Dựa trên intake của bạn, mình đã đánh giá độ phức tạp của việc nghiên cứu:

| Yếu tố             | Đánh giá            | Điểm  |
|--------------------|---------------------|-------|
| Độ rộng thị trường | {mô tả}             | {1-3} |
| Số đối thủ đã biết | Xác định được {N}   | {1-3} |
| Phạm vi địa lý     | {mô tả}             | {1-3} |

**Điểm độ phức tạp: {X}/9 — độ sâu đề xuất: {Light/Standard/Deep}**

Bạn có thể ghi đè. Ý nghĩa của từng mức:

| Độ sâu       | Số agent | Lượt tìm mỗi agent | Phù hợp nhất cho                               |
|--------------|----------|--------------------|-----------------------------------------------|
| **Light**    | {N}      | 2-3 vòng           | Quét nhanh, thị trường ngách, quyết định gấp về thời gian |
| **Standard** | {N}      | 3-4 vòng           | Đa số trường hợp, cân bằng giữa độ sâu và tốc độ |
| **Deep**     | {N}      | 5-6 vòng           | Thị trường đông đúc, quyết định hệ trọng, due diligence kỹ lưỡng |

→ Gõ **light**, **deep**, hoặc **ok** để chấp nhận đề xuất.
```

Số agent hiển thị phải phản ánh con số thực của skill này (xem Cấu hình wave bên dưới).

## Cấu hình wave: product-design

### Light (điểm 3-4 hoặc user ghi đè)

**Wave 1: Bức tranh thị trường** (2 agent)
- A1: Quy mô thị trường & kinh tế học (giữ nguyên)
- A2: Xu hướng ngành, thời điểm & pháp lý (gộp A2+A3 thành một agent)

**Wave 2: Phân tích cạnh tranh** (2 agent)
- B1: Đào sâu đối thủ trực tiếp (giữ nguyên)
- B2: Đối thủ gián tiếp & GTM (gộp B2+B3 thành một agent)

**Wave 3: Khách hàng & nhu cầu** (2 agent)
- C1: Tiếng nói khách hàng & nỗi đau (giữ nguyên)
- C2: Tín hiệu nhu cầu & phác hoạ đối tượng (gộp C2+C3 thành một agent)

**Wave 4: Phân phối** (1 agent)
- D1: Phân phối & thâm nhập theo địa lý (gộp D1+D2 thành một agent)
- Bỏ hẳn Wave 4 nếu thị trường là địa phương/một quốc gia

**Tổng: 6-7 agent** (so với 11 ở Standard), 2-3 vòng tìm kiếm mỗi agent

### Standard (điểm 5-7, mặc định)

Không thay đổi cấu trúc wave hiện tại:
- Wave 1: 3 agent (A1, A2, A3)
- Wave 2: 3 agent (B1, B2, B3)
- Wave 3: 3 agent (C1, C2, C3)
- Wave 4: 2 agent (D1, D2)

**Tổng: 11 agent**, 3-4 vòng tìm kiếm mỗi agent

### Deep (điểm 8-9 hoặc user ghi đè)

**Wave 1: Bức tranh thị trường** (4 agent)
- A1: Quy mô thị trường & kinh tế học (giữ nguyên)
- A2: Xu hướng ngành & thời điểm (giữ nguyên)
- A3: Pháp lý & tuân thủ (giữ nguyên)
- A4: Thị trường lân cận & mở rộng (MỚI: nghiên cứu các ngành dọc lân cận, khoảng trống thị trường, hướng mở rộng)

**Wave 2: Phân tích cạnh tranh** (4 agent)
- B1: Đào sâu đối thủ trực tiếp (giữ nguyên)
- B2: Đối thủ gián tiếp & sản phẩm thay thế (giữ nguyên)
- B3: Go-to-Market của đối thủ (giữ nguyên)
- B4: Đối thủ mới nổi & đang ẩn mình (MỚI: tìm các startup đang stealth, sản phẩm mới ra mắt, sản phẩm chưa ra mắt trong lĩnh vực)

**Wave 3: Khách hàng & nhu cầu** (4 agent)
- C1: Tiếng nói khách hàng & nỗi đau (giữ nguyên)
- C2: Tín hiệu nhu cầu & thẩm định thị trường (giữ nguyên)
- C3: Phác hoạ đối tượng mục tiêu (giữ nguyên)
- C4: Đào sâu về giá (MỚI: thông tin giá chi tiết, phân tích WTP, nghiên cứu độ nhạy giá)

**Wave 4: Phân phối & đối tác** (3 agent)
- D1: Đào sâu kênh phân phối (giữ nguyên)
- D2: Địa lý & thâm nhập thị trường (giữ nguyên)
- D3: Lập bản đồ đối tác chiến lược (MỚI: đối tác tiềm năng, cơ hội tích hợp, đối tác kênh)

**Tổng: 15 agent**, 5-6 vòng tìm kiếm mỗi agent

## PROGRESS.md

Ghi tier đã chọn vào PROGRESS.md:

```markdown
- **Độ sâu nghiên cứu:** {Light/Standard/Deep} (điểm: {X}/9, {ghi đè: theo yêu cầu user / tự động})
```
