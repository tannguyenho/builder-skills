# Tài liệu domain

Cách các skill engineering đọc và dùng tài liệu domain của repo này khi khảo sát codebase.

## Trước khi khảo sát, hãy đọc

- **`GLOSSARY.md`** ở gốc repo, hoặc
- **`GLOSSARY-MAP.md`** ở gốc repo nếu có: file này trỏ tới một `GLOSSARY.md` cho mỗi context. Đọc từng file liên quan đến chủ đề đang làm.
- **`docs/adr/`**: đọc các ADR đụng tới khu vực bạn sắp làm. Trong repo multi-context, xem thêm `src/<context>/docs/adr/` cho các quyết định riêng của từng context.

Nếu file nào trong số này không tồn tại, **cứ lặng lẽ làm tiếp**. Đừng báo là thiếu; đừng đề nghị tạo chúng từ trước. Skill `/grill-with-docs` (và `/improve-codebase-architecture`) sẽ tạo chúng dần dần, khi thuật ngữ hoặc quyết định thực sự được chốt.

## Cấu trúc file

Repo single-context (phần lớn các repo):

```
/
├── GLOSSARY.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Repo multi-context (có `GLOSSARY-MAP.md` ở gốc):

```
/
├── GLOSSARY-MAP.md
├── docs/adr/                          ← quyết định toàn hệ thống
└── src/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── docs/adr/                  ← quyết định riêng của context
    └── billing/
        ├── GLOSSARY.md
        └── docs/adr/
```

## Dùng đúng từ vựng của glossary

Khi output của bạn gọi tên một khái niệm domain (trong tiêu đề issue, đề xuất refactor, giả thuyết, tên test), hãy dùng đúng thuật ngữ như định nghĩa trong `GLOSSARY.md`. Đừng trôi sang những từ đồng nghĩa mà glossary đã ghi rõ là tránh dùng.

Nếu khái niệm bạn cần chưa có trong glossary, đó là một tín hiệu: hoặc bạn đang tự chế ra ngôn ngữ mà dự án không dùng (cân nhắc lại), hoặc đó là một lỗ hổng thật (ghi lại để xử lý bằng `/grill-with-docs`).

## Nêu rõ khi mâu thuẫn với ADR

Nếu output của bạn đi ngược một ADR đang có, hãy nêu ra rõ ràng thay vì lặng lẽ làm khác:

> _Mâu thuẫn với ADR-0007 (event-sourced orders), nhưng đáng mở lại vì…_
