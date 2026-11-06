# Quy tắc điều chỉnh quy mô nghiên cứu (Research Scaling Protocol)

Điều chỉnh động độ sâu nghiên cứu theo độ phức tạp của thị trường và mong muốn của user. Đánh giá sau intake, trước khi bắt đầu nghiên cứu.

## Điểm phức tạp

Đánh giá ba yếu tố từ dữ liệu intake:

| Yếu tố | Thấp (1) | Trung bình (2) | Cao (3) |
|--------|---------|------------|----------|
| **Độ rộng thị trường** | Siêu ngách, ít người chơi, phân khúc rõ ràng | Thị trường xác định, cạnh tranh vừa phải | Thị trường rộng, nhiều phân khúc, người chơi đa dạng |
| **Số đối thủ đã biết** | Xác định được 0-2 | Xác định được 3-5 | Xác định được 6+ |
| **Phạm vi địa lý** | Một quốc gia | Khu vực (vd Châu Âu, Bắc Mỹ) | Toàn cầu hoặc nhiều khu vực |

**Điểm phức tạp** = tổng điểm ba yếu tố (khoảng: 3-9)

## Các mức độ sâu nghiên cứu

| Mức | Khoảng điểm | Kích hoạt thủ công | Mô tả |
|------|-----------|----------------|-------------|
| **Light** | 3-4 | User nói "light", "quick", "fast research" (hoặc "nhanh", "sơ bộ") | Quét nhanh, ít agent hơn, 2-3 vòng tìm kiếm |
| **Standard** | 5-7 | Mặc định (không cần chỉnh) | Hành vi hiện tại, độ sâu cân bằng |
| **Deep** | 8-9 | User nói "deep", "thorough", "deep research" (hoặc "kỹ", "chuyên sâu") | Nhiều agent hơn, 5-6 vòng tìm kiếm, phủ thêm |

**Lựa chọn thủ công luôn thắng.** Nếu user yêu cầu "light" cho một thị trường 9 điểm, dùng Light. Nếu họ yêu cầu "deep" cho một thị trường 3 điểm, dùng Deep.

## Thông báo cho user

Sau khi tính điểm, hiển thị cho user:

```
## Độ sâu nghiên cứu

Dựa trên thông tin intake, mình đã đánh giá độ phức tạp nghiên cứu:

| Yếu tố              | Đánh giá            | Điểm  |
|---------------------|---------------------|-------|
| Độ rộng thị trường  | {mô tả}             | {1-3} |
| Số đối thủ đã biết  | Xác định được {N}   | {1-3} |
| Phạm vi địa lý      | {mô tả}             | {1-3} |

**Điểm phức tạp: {X}/9 — độ sâu đề xuất: {Light/Standard/Deep}**

Bạn có thể chọn khác. Ý nghĩa của từng mức:

| Độ sâu       | Agent  | Số vòng tìm mỗi agent | Phù hợp cho                                   |
|--------------|--------|-----------------------|-----------------------------------------------|
| **Light**    | {N}    | 2-3 vòng              | Quét nhanh, thị trường ngách, quyết định gấp  |
| **Standard** | {N}    | 3-4 vòng              | Đa số trường hợp, cân bằng độ sâu và tốc độ   |
| **Deep**     | {N}    | 5-6 vòng              | Thị trường đông đúc, quyết định quan trọng, thẩm định kỹ |

→ Gõ **light**, **deep**, hoặc **ok** để chấp nhận đề xuất.
```

Số agent hiển thị phải phản ánh đúng con số thực của skill này (xem Cấu hình từng đợt bên dưới).

## Cấu hình từng đợt: product-competitors

### Light (điểm 3-4 hoặc user chọn)

**Đợt 1: Hồ sơ đối thủ + Giá** (1 agent)
- A1: Hồ sơ đối thủ & Giá (gộp A1+A2 thành một agent, làm hồ sơ và giá cùng lúc)

**Đợt 2: Cảm nhận khách hàng** (1 agent)
- B1: Khai thác review & cộng đồng (gộp B1+B2 thành một agent, làm review và diễn đàn cùng lúc)

**Đợt 3: GTM & Tín hiệu chiến lược** (1 agent)
- C1: GTM & Tín hiệu tăng trưởng (gộp C1+C2 thành một agent, làm GTM và tín hiệu chiến lược cùng lúc)

**Tổng: 3 agent** (so với 6 ở Standard), 2-3 vòng tìm kiếm mỗi agent

### Standard (điểm 5-7, mặc định)

Giữ nguyên cấu trúc đợt hiện tại:
- Đợt 1: 2 agent (A1, A2)
- Đợt 2: 2 agent (B1, B2)
- Đợt 3: 2 agent (C1, C2)

**Tổng: 6 agent**, 3-4 vòng tìm kiếm mỗi agent

### Deep (điểm 8-9 hoặc user chọn)

**Đợt 1: Hồ sơ đối thủ + Giá** (3 agent)
- A1: Đào sâu đối thủ (giữ nguyên)
- A2: Thông tin giá (giữ nguyên)
- A3: Hồ sơ đối thủ liền kề (MỚI: lập hồ sơ 3-5 đối thủ liền kề/mới nổi không nằm trong nhóm trực tiếp, gồm cả sản phẩm mới ra mắt và startup đang hoạt động kín — stealth)

**Đợt 2: Cảm nhận khách hàng** (3 agent)
- B1: Khai thác review (giữ nguyên)
- B2: Khai thác diễn đàn & cộng đồng (giữ nguyên)
- B3: Cảm nhận trên mạng xã hội (MỚI: khai thác Twitter/X, LinkedIn và YouTube để tìm các lần nhắc tới đối thủ, mẫu cảm nhận và ý kiến của người có ảnh hưởng)

**Đợt 3: GTM & Tín hiệu chiến lược** (3 agent)
- C1: Phân tích Go-to-Market (giữ nguyên)
- C2: Tín hiệu chiến lược & tăng trưởng (giữ nguyên)
- C3: Tech stack & Phân tích sản phẩm (MỚI: phân tích lựa chọn công nghệ, hệ sinh thái API, độ sâu tích hợp và hào kỹ thuật của đối thủ)

**Tổng: 9 agent**, 5-6 vòng tìm kiếm mỗi agent

## PROGRESS.md

Ghi mức đã chọn vào PROGRESS.md:

```markdown
- **Độ sâu nghiên cứu:** {Light/Standard/Deep} (điểm: {X}/9, {chọn bởi: user yêu cầu / tự động})
```
