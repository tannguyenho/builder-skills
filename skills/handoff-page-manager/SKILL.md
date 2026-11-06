---
name: handoff-page-manager
description: "Tổ chức page trong file handoff (file bàn giao design cho dev) theo cấu trúc CHANGE LOG / USER FLOW / UI GUIDELINE / DESIGN QA / COVER. Dùng khi user muốn sắp xếp lại page trong file handoff, tạo page còn thiếu, hoặc kiểm tra cấu trúc page handoff đúng chuẩn chưa."
---

# Page Manager — Handoff

Skill này dùng để tổ chức **page** trong file handoff — file bàn giao design cho dev, gom flow theo nhóm nghiệp vụ kèm changelog, UI guideline và design QA.

> ⚠️ **Phạm vi: chỉ thao tác trên danh sách Page** (tạo page còn thiếu, đổi tên, sắp xếp lại thứ tự page theo cấu trúc chuẩn bên dưới).
> **KHÔNG** di chuyển, cắt/dán hay đổi parent của bất kỳ frame/section nào đang có sẵn trong file — nội dung bên trong mỗi page giữ nguyên.

```
📋 CHANGE LOG
---
🦶 USER FLOW
---
📐 UI GUIDELINE
---
🚧 DESIGN QA
---
🖼️ COVER
```

- `📋 CHANGE LOG`: page đầu tiên — ghi nhận thay đổi của file theo từng đợt bàn giao (ngày, nội dung thay đổi, page bị ảnh hưởng)
- `🦶 USER FLOW`: page nhóm — chứa toàn bộ flow nghiệp vụ, chia thành các nhóm nghiệp vụ bên trong
- `📐 UI GUIDELINE`: page nhóm — chứa pattern/guideline UI dùng chung cho nhiều flow, mỗi guideline 1 sub-page `→ [Tên]` (Title Case nếu tên tiếng Anh)
- `🚧 DESIGN QA`: page — kết quả QA design trước handoff (checklist, lỗi phát hiện, trạng thái fix)
- `🖼️ COVER`: page cuối cùng — bìa file (khác DS/Snowflake để cover ở đầu file; thumbnail vẫn set thủ công trong Figma)
- Tên nhóm/flow giữ nguyên ngôn ngữ nghiệp vụ của dự án, không bắt buộc tiếng Anh
- Prefix sub-page `→ ` (mũi tên, không phải `->`)
- `---` = page trống ngăn cách giữa các nhóm

Ví dụ minh hoạ (tên chỉ để tham khảo, không phải chuẩn bắt buộc):
```
📋 CHANGE LOG
🦶 USER FLOW
    🔹 3. Nhóm nghiệp vụ Trong chuyến đi (In-trip)
        → 3.1 - Thu thập đánh giá khách hàng
        → 3.2 - Gợi ý cảnh báo trong chuyến đi (thời tiết, máy bay)
        → 3.3 - Import hoá đơn đặt chờ (Chưa làm trong phase này)
        → 3.5 - Gợi ý nhà hàng từ ảnh chụp món ăn 🍜
        → 3.6 - Up-sell & Cross-sell (Chưa làm trong phase này)
        → 3.7 - Trợ lý ẩm thực (Dịch Menu) 🍜
📐 UI GUIDELINE
    → Digital Menu
    → Gather information form
🚧 DESIGN QA
🖼️ COVER
```