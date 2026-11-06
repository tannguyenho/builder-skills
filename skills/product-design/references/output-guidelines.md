# Hướng dẫn đầu ra (Output Guidelines)

## Header chuẩn của file

Mọi file đầu ra nên bắt đầu bằng một header thống nhất:

```markdown
# [Tiêu đề tài liệu]

**Phase:** [Số và tên phase]
**Dự án:** [project-name]
**Ngày:** [ngày tạo]
**Độ tin cậy:** [Độ tin cậy tổng thể: Cao / Trung bình / Thấp]

---
```

Nhờ vậy founder dễ điều hướng giữa các sản phẩm bàn giao và hiểu ngay mức độ đáng tin của từng tài liệu.

## Footer chuẩn của file

Mọi file đầu ra nên kết thúc bằng:

```markdown
---

## Cờ cảnh báo (Flags)

**Cờ đỏ (Red Flags):**
- [Liệt kê các cờ đỏ, hoặc "Không phát hiện"]

**Cờ vàng (Yellow Flags):**
- [Liệt kê các cờ vàng, hoặc "Không phát hiện"]

## Nguồn
- [Các nguồn chính được tham chiếu trong tài liệu này, kèm xếp hạng tier]
```

## Tham chiếu chéo giữa các phase

Khi một tài liệu tham chiếu phát hiện từ phase khác, dùng trích dẫn rõ ràng:

**Tốt:**
> "Persona mục tiêu (xem `01-discovery/target-audience.md`, Persona 1: CFO doanh nghiệp vừa) có ngân sách công cụ trung bình $2,000/tháng [Data, Gartner 2025]."

**Kém:**
> "Như đã nói ở trên, khách hàng mục tiêu có ngân sách cho việc này."

Luôn gồm:
- Đường dẫn file được tham chiếu
- Phát hiện cụ thể (không tham chiếu mơ hồ)
- Nhãn dữ liệu ([Data], [Estimate], v.v.)

## Ví dụ về chất lượng

### Đầu ra tốt vs. kém

**Phân tích thị trường — Kém:**
> "Thị trường mở ra những cơ hội tăng trưởng thú vị. Có vài đối thủ nhưng không quá đông đúc. Thời điểm có vẻ thuận lợi."

**Phân tích thị trường — Tốt:**
> "Thị trường tự động hoá hoá đơn toàn cầu đạt $4.2B [Data, MarketsAndMarkets 2025], tăng trưởng CAGR 12.3% [Data, Grand View Research 2025]. Tuy nhiên, phân khúc SMB — mục tiêu của chúng ta — chỉ chiếm $340M [Estimate, suy ra từ tỉ trọng SMB 8.1% theo báo cáo của Ardent Partners]. Ba đối thủ được đầu tư mạnh (Tipalti gọi được $270M, Stampli $68M, Vic.ai $52M) đã phục vụ phân khúc này [Data, Crunchbase]. **[Yellow Flag]** Thị trường có thể quá nhỏ cho một người mới vào cạnh tranh trực diện; cần một định vị ngách."

**Scorecard — Kém:**
> | Quy mô thị trường | 7 | Quy mô thị trường tốt |

**Scorecard — Tốt:**
> | Quy mô thị trường | 5 | TAM là $4.2B nhưng phân khúc phục vụ được (tự động hoá hoá đơn cho SMB) chỉ ~$340M [Estimate]. Với mức thâm nhập 5% là $17M ARR — khả thi cho một doanh nghiệp bootstrap nhưng dưới ngưỡng thường thấy của VC. [Yellow Flag] |

## Bảng đánh giá cuối (Final Assessment Dashboard)

Sau khi cả 8 phase hoàn tất và trước khi viết README.md, in một dashboard tóm tắt ngay trong cuộc trò chuyện (không ghi vào file). Nó cho founder thấy ngay thành quả trực quan của toàn bộ quy trình.

Lấy từng giá trị từ đầu ra thực tế của các phase. Không bịa hay làm tròn ước chừng. Nếu một giá trị chưa được xác định, ghi "Chưa đánh giá".

```
═══════════════════════════════════════════════
        PRODUCT DESIGN — ĐÁNH GIÁ CUỐI
═══════════════════════════════════════════════

 Ý tưởng:           [biến thể được chọn từ brainstorm Phase 2]
 Founder Fit:       [Mạnh / Trung bình / Yếu]
 Thị trường:        [$X TAM] · [% tăng trưởng] · [giai đoạn trưởng thành]
 Đối thủ:           [tìm thấy N] · [tóm tắt bức tranh gọi vốn]
 Phỏng vấn KH:      [N cuộc đã làm] · [vấn đề được xác nhận bởi N/N]
 Định vị:           [Rõ ràng / Đang hình thành / Chưa rõ]
 Mô hình KD:        [SaaS / Marketplace / Open Core / v.v.]
 Giai đoạn TC:      [A — Dựa trên giả định / B — Dựa trên bằng chứng]
 Phạm vi MVP:       [N tính năng cốt lõi] · [ước lượng thời gian xây]
 Tính khả thi MH:   [Khả thi / Rủi ro / Hỏng]
 Rủi ro lớn nhất:   [rủi ro lớn nhất trong một dòng]

 ĐIỂM:              [X / 10]
 KẾT LUẬN:          [GO / CONDITIONAL / NO-GO]

 Số file đã tạo:    [N]
 Thư mục:           [path]
═══════════════════════════════════════════════
```

**Định nghĩa các trường:**

- **Phỏng vấn KH (khách hàng)**: Số cuộc phỏng vấn đã làm ở Phase 3.7 và tỉ lệ xác nhận vấn đề (vd "5 cuộc đã làm · xác nhận bởi 4/5"). Nếu là Fast Track với các cuộc trò chuyện do founder tự báo, ghi chú "[Founder-reported]". Nếu founder đã hoãn phỏng vấn, ghi "0 cuộc đã làm · đã hoãn".
- **Giai đoạn TC (tài chính)**: A = Dựa trên giả định (không có dữ liệu traction thật), B = Dựa trên bằng chứng (dự phóng neo vào tín hiệu phỏng vấn hoặc dữ liệu traction thật).
- **Ý tưởng**: Biến thể cụ thể được chọn sau brainstorm, không phải đầu vào thô ban đầu.
- **Founder Fit** (độ phù hợp của founder): Từ đánh giá intake ở Phase 1. Mạnh = có lợi thế không công bằng (unfair advantage) rõ ràng. Trung bình = có nền tảng liên quan ở mức nào đó. Yếu = không có lợi thế về lĩnh vực.
- **Thị trường**: TAM từ nghiên cứu Phase 3, tốc độ tăng trưởng, và độ trưởng thành (mới nổi/đang tăng trưởng/trưởng thành/suy giảm).
- **Đối thủ**: Số đối thủ trực tiếp tìm thấy ở Phase 3, cộng một cụm từ tóm tắt bức tranh gọi vốn (vd "3 đã gọi vốn, 2 bootstrap" hoặc "bị 1 ông lớn thống trị").
- **Định vị**: Từ chiến lược Phase 4. Rõ ràng = có góc khác biệt hiển nhiên. Đang hình thành = có thể khác biệt nhưng chưa được chứng minh. Chưa rõ = chưa tìm được góc nào rõ ràng.
- **Mô hình KD (kinh doanh)**: Mô hình được chọn trong chiến lược Phase 4.
- **Phạm vi MVP**: Số tính năng cốt lõi từ định nghĩa sản phẩm Phase 6, cộng ước lượng thô thời gian xây.
- **Tính khả thi MH (mô hình)**: Một nhận định tổng hợp từ tài chính Phase 7. Khả thi = unit economics chạy được với giả định hợp lý. Rủi ro = unit economics phụ thuộc vào giả định lạc quan. Hỏng = unit economics không chạy được trong bất kỳ kịch bản hợp lý nào.
- **Rủi ro lớn nhất**: Rủi ro có tác động lớn nhất từ ma trận rủi ro Phase 8.
- **Điểm / Kết luận**: Từ validation scorecard Phase 8. GO (8-10), CONDITIONAL (6-7), NO-GO (1-5).

In dashboard này trong cuộc trò chuyện sau khi mọi file đã được viết. Rồi tiếp tục viết README.md và action-plan-30-days.md như mô tả trong file skill chính.

---

## Xử lý pivot

Nếu founder muốn đổi hướng sau khi xem kết quả nghiên cứu hoặc chiến lược (thị trường mục tiêu khác, mô hình kinh doanh khác, định vị khác):

1. **Đừng làm lại từ đầu.** Phần lớn nghiên cứu và phân tích có thể vẫn dùng được.
2. **Cập nhật brief** (`00-intake/brief.md`) với mục "Ghi chú pivot" ghi lại điều gì đã thay đổi và tại sao.
3. **Chỉ chạy lại các phase bị ảnh hưởng.** Nếu pivot liên quan đến thị trường mục tiêu, chạy lại Phase 3 (các wave nghiên cứu khách hàng) và Phase 4 (chiến lược). Nếu liên quan đến mô hình kinh doanh, chạy lại Phase 4 và Phase 7.
4. **Đánh dấu các phase chạy lại** trong PROGRESS.md: `- [x] Phase 4: Strategy — chạy lại sau pivot {date}`
5. **Giữ phiên bản cũ.** Đổi tên đầu ra trước đó thành `{filename}.pre-pivot.md` trước khi tạo phiên bản mới. Việc này giữ lại dấu vết quyết định.
