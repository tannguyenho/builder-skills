---
name: ds-page-manager
description: "Tổ chức page trong file Design System (DS). Dùng khi user muốn sắp xếp lại page trong file DS, hoặc kiểm tra cấu trúc page DS đúng chuẩn chưa"
---

# Page Manager — Design System

Skill này dùng để tổ chức **page** trong file Design System (DS), nhóm component theo Category để dễ tìm trong Assets panel.

> ⚠️ **Phạm vi: chỉ thao tác trên danh sách Page** (tạo page mới còn thiếu, đổi tên, sắp xếp lại thứ tự page theo cấu trúc chuẩn bên dưới).
> **KHÔNG** di chuyển, cắt/dán, hay đổi parent của bất kỳ component/frame/instance nào đang có sẵn trong file — nội dung bên trong mỗi page giữ nguyên, không được gom hay kéo component thật từ page này sang page khác.
> Tên `→ Component` bên dưới chỉ là **tên gợi ý cho page** (đại diện cho nhóm component nào nên nằm ở page nào theo quy ước đặt tên) — không phải chỉ thị để di chuyển nội dung.

```
🖼️ Cover
---
🎨 FOUNDATION
    → Assets
    → Colors
    → Typography
---
⚡ ACTIONS
    → Button
---
✏️ DATA ENTRY
    → Calendar
    → Checkbox / Radio / Toggle
    → Dropdown Input
    → Text Field
---
📊 DATA DISPLAY
    → Avatar
    → Badge
---
🧩 PATTERNS
    → Empty State
    → Search & Filter
    → Form
---
📐 TEMPLATES
    → Dashboard
    → List & Detail
```

- `🖼️ Cover`: page đầu tiên của file
- Mỗi **Category** là 1 page riêng — tên ALL CAPS + emoji đại diện (vd `🎨 FOUNDATION`, `⚡ ACTIONS`, `✏️ DATA ENTRY`, `📊 DATA DISPLAY`) — **không** gộp toàn bộ component vào 1 page chung
- Component thuộc Category nằm dưới dạng sub-page, prefix `→ ` (mũi tên, không phải `->`), tên Title Case
- `---`: page trống làm divider giữa các nhóm Category
- Emoji ở tên Category (page): OK — Emoji ở tên component: **KHÔNG**
- `🧩 PATTERNS`: cụm component ghép lại để giải một nhu cầu lặp lại (trạng thái rỗng, tìm kiếm & lọc, form). Đặt sau các nhóm component
- `📐 TEMPLATES`: khung cả trang (vị trí header, vùng nội dung, nút chính), dựng từ component và pattern. Luôn là nhóm cuối cùng của file
- Category mới đặt tên theo đúng mục đích, kèm emoji phù hợp, chèn vào giữa các divider `---`