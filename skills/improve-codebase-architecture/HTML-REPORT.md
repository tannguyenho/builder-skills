# Định dạng báo cáo HTML

Bản rà soát kiến trúc được xuất thành một file HTML tự đủ duy nhất trong thư mục tạm của hệ điều hành. Tailwind và Mermaid đều lấy từ CDN. Mermaid xử lý tốt các sơ đồ dạng đồ thị; div dựng tay và SVG inline xử lý các hình minh hoạ mang tính biên tập hơn (mass diagram, mặt cắt). Trộn cả hai: đừng dựa vào Mermaid cho mọi thứ, nhìn sẽ bắt đầu nhàm chán, rập khuôn.

Mọi chữ hiển thị cho người đọc trong báo cáo (tiêu đề, nhãn, chú giải, câu mô tả) viết bằng tiếng Việt; tên file, tên module trong code, class CSS và thuật ngữ kiến trúc (module, interface, seam…) giữ nguyên.

## Khung sườn

```html
<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8" />
    <title>Rà soát kiến trúc cho {{repo name}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
      mermaid.initialize({ startOnLoad: true, theme: "neutral", securityLevel: "loose" });
    </script>
    <style>
      /* lớp tuỳ biến nhỏ cho những thứ Tailwind không xử lý gọn:
         đường seam nét đứt, đầu mũi tên kiểu vẽ tay, v.v. */
      .seam { stroke-dasharray: 4 4; }
      .leak { stroke: #dc2626; }
      .deep { background: linear-gradient(135deg, #0f172a, #1e293b); }
    </style>
  </head>
  <body class="bg-stone-50 text-slate-900 font-sans">
    <main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
      <header>...</header>
      <section id="candidates" class="space-y-10">...</section>
      <section id="top-recommendation">...</section>
    </main>
  </body>
</html>
```

## Phần đầu (header)

Tên repo, ngày, và một chú giải gọn: khung liền = module, nét đứt = seam, mũi tên đỏ = rò rỉ, khung đậm màu tối = deep module. Không có đoạn giới thiệu. Vào thẳng các ứng viên.

## Thẻ ứng viên

Sơ đồ gánh phần chính. Chữ ít, đơn giản, dùng các thuật ngữ trong bảng thuật ngữ (của skill `codebase-design`) một cách tự nhiên, không rườm rà.

Mỗi ứng viên là một `<article>`:

- **Tiêu đề**: ngắn, gọi tên việc làm sâu (vd "Gộp pipeline Order intake").
- **Hàng badge**: mức khuyến nghị (`Khuyến nghị mạnh` = emerald, `Đáng tìm hiểu` = amber, `Phỏng đoán` = slate), kèm một tag cho loại dependency (`in-process`, `local-substitutable`, `ports & adapters`, `mock`).
- **File**: danh sách font monospace, `font-mono text-sm`.
- **Sơ đồ Trước / Sau**: trung tâm của thẻ. Hai cột, đặt cạnh nhau. Xem các mẫu bên dưới.
- **Vấn đề**: một câu. Đau ở đâu.
- **Giải pháp**: một câu. Thay đổi gì.
- **Được gì**: gạch đầu dòng, mỗi dòng ≤6 từ. vd "Test chạm một interface duy nhất", "Logic Pricing hết rò rỉ", "Xoá 4 wrapper nông".
- **Khung ADR** (nếu có): một dòng trong một hộp tô màu amber.

Không có đoạn văn giải thích. Nếu sơ đồ cần cả một đoạn văn mới hiểu được, hãy vẽ lại sơ đồ.

## Các mẫu sơ đồ

Chọn mẫu hợp với ứng viên. Trộn chúng với nhau. Đừng để sơ đồ nào cũng giống nhau. Sự đa dạng là một phần của mục đích.

### Mermaid graph (con ngựa thồ cho dependency / luồng gọi)

Dùng Mermaid `flowchart` hoặc `graph` khi ý chính là "X gọi Y gọi Z, và nhìn mớ bòng bong này đi". Bọc nó trong một card style bằng Tailwind để không trông như bị thả từ trên trời xuống. Style bằng classDef để tô đỏ các cạnh rò rỉ và tô tối deep module. Sequence diagram rất hợp cho kiểu "trước: 6 lượt gọi qua lại; sau: 1".

```html
<div class="rounded-lg border border-slate-200 bg-white p-4">
  <pre class="mermaid">
    flowchart LR
      A[OrderHandler] --> B[OrderValidator]
      B --> C[OrderRepo]
      C -.rò rỉ.-> D[PricingClient]
      classDef leak stroke:#dc2626,stroke-width:2px;
      class C,D leak
  </pre>
</div>
```

### Hộp-và-mũi-tên dựng tay (khi bố cục của Mermaid chống lại bạn)

Module là các `<div>` có viền và nhãn. Mũi tên là các phần tử SVG inline `<line>` hoặc `<path>` đặt `absolute` phía trên một container `relative`. Dùng cách này khi bạn muốn sơ đồ "sau" trông như một deep module viền dày với phần bên trong mờ xám, vì Mermaid không vẽ được đúng độ nặng đó.

### Mặt cắt (hợp với kiểu nông nhiều tầng)

Xếp chồng các dải ngang (`h-12 border-l-4`) để thể hiện các tầng mà một lời gọi đi qua. Trước: 6 tầng mỏng, tầng nào cũng chẳng làm gì. Sau: 1 dải dày, ghi nhãn trách nhiệm đã được gom lại.

### Mass diagram (hợp với kiểu "interface rộng bằng implementation")

Mỗi module hai hình chữ nhật: một cho diện tích bề mặt interface, một cho implementation. Trước: hình interface cao gần bằng hình implementation (shallow). Sau: hình interface thấp, hình implementation cao (deep).

### Thu gọn call graph

Trước: một cây lời gọi hàm vẽ thành các hộp lồng nhau. Sau: cùng cây đó thu gọn vào một hộp, các lời gọi giờ đã thành nội bộ hiện mờ bên trong.

## Hướng dẫn style

- Thiên về phong cách biên tập, không phải dashboard doanh nghiệp. Nhiều khoảng trắng. Có thể dùng serif cho heading (`font-serif` hợp với tông stone/slate).
- Dùng màu tiết kiệm: một màu nhấn (emerald hoặc indigo) cộng đỏ cho rò rỉ và amber cho cảnh báo.
- Giữ sơ đồ cao khoảng ~320px để cặp trước/sau nằm vừa cạnh nhau mà không phải cuộn.
- Dùng `text-xs uppercase tracking-wider` cho nhãn module bên trong sơ đồ, để chúng đọc như bản vẽ kỹ thuật chứ không như UI.
- Script duy nhất là Tailwind CDN và lệnh import Mermaid ESM. Ngoài ra báo cáo hoàn toàn tĩnh: không có code ứng dụng, không tương tác gì ngoài phần render của chính Mermaid.

## Mục khuyến nghị hàng đầu

Một thẻ lớn hơn. Tên ứng viên, một câu nói vì sao, một anchor link tới thẻ của nó. Thế thôi.

## Giọng văn

Lời lẽ đời thường, súc tích, nhưng các danh từ và động từ kiến trúc lấy thẳng từ skill `codebase-design`. Súc tích không phải cái cớ để trôi khỏi thuật ngữ.

**Dùng đúng:** module, interface, implementation, depth, deep, shallow, seam, adapter, leverage, locality.

**Không bao giờ thay bằng:** component, service, unit (thay cho module) · API, signature (thay cho interface) · boundary (thay cho seam) · layer, wrapper (thay cho module, khi ý bạn là module).

**Những câu đúng phong cách:**

- "Module Order intake bị shallow: interface gần bằng implementation."
- "Pricing rò rỉ qua seam."
- "Làm sâu: một interface, một chỗ để test."
- "Hai adapter biện minh cho seam: HTTP ở prod, in-memory trong test."

**Gạch đầu dòng "Được gì"** gọi tên lợi ích bằng thuật ngữ trong bảng thuật ngữ: *"locality: bug dồn về một module"*, *"leverage: một interface, N chỗ gọi"*, *"interface thu nhỏ; implementation hấp thụ các wrapper"*. Đừng viết *"dễ bảo trì hơn"* hay *"code sạch hơn"*, vì những từ đó không có trong bảng thuật ngữ và không xứng đáng chiếm chỗ.

Không rào đón, không dạo đầu, không "cũng cần lưu ý rằng…". Nếu một câu có thể thành gạch đầu dòng, hãy biến nó thành gạch đầu dòng. Nếu một gạch đầu dòng có thể cắt, hãy cắt. Nếu một thuật ngữ không có trong bảng thuật ngữ của `codebase-design`, hãy tìm một từ có sẵn trong đó trước khi tự đặt từ mới.
