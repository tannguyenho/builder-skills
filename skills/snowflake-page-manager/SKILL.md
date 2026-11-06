---
name: snowflake-page-manager
description: "Tổ chức page trong file Snowflake. Dùng khi user muốn sắp xếp lại page trong file Snowflake, hoặc kiểm tra cấu trúc page đúng chuẩn chưa."
---

# Page Manager — Snowflake

Skill này dùng để tổ chức **page** trong file Snowflake, nhóm component theo Base/Component/Screen để dễ tìm trong Assets panel.

> ⚠️ **Phạm vi: chỉ thao tác trên danh sách Page** (tạo page mới còn thiếu, đổi tên, sắp xếp lại thứ tự page theo cấu trúc chuẩn bên dưới).
> **KHÔNG** di chuyển, cắt/dán, hay đổi parent của bất kỳ component/frame/instance nào đang có sẵn trong file — nội dung bên trong mỗi page giữ nguyên, không được gom hay kéo component thật từ page này sang page khác.
> Tên `→ [Component]` bên dưới chỉ là **tên gợi ý cho page** (đại diện cho nhóm component nào nên nằm ở page nào theo quy ước đặt tên) — không phải chỉ thị để di chuyển nội dung.

```
🖼️ COVER
---
📦 BASE
    → [Base Component 1]
    → [Base Component 2]
---
🍀 COMPONENT
    → [Component 1]
    → [Component 2]
---
🖥️ SCREEN
    → [Screen 1]
    → [Screen 2]
```

- `📦 BASE`: page nhóm — mỗi component `Base / ...` (và element của nó) nằm ở 1 sub-page riêng trong nhóm này
- `🍀 COMPONENT`: page nhóm — mỗi component không phải Base nằm ở 1 sub-page riêng trong nhóm này, sắp xếp A-Z
- `🖥️ SCREEN`: page nhóm — chứa các màn hình/flow hoàn chỉnh, lắp ráp từ nhiều component (không phải bản thân component)
- Sub-page prefix `→ ` (mũi tên, không phải `->`), tên Title Case
- Emoji: OK ở tên page nhóm, **cấm** ở tên component
- `---` = page trống ngăn cách giữa các nhóm
- Đây là **cấu trúc chung** (3 nhóm page + sub-page prefix `→`) — tên page/component cụ thể tuỳ theo từng file, không phải tên cố định phải dùng lại

Ví dụ minh hoạ (tên chỉ để tham khảo, không phải chuẩn bắt buộc):
```
📦 BASE
    → Card
    → Entrypoint
🍀 COMPONENT
    → Chatbot
    → Menu
🖥️ SCREEN
    → Home
    → Destination
```