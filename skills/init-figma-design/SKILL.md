---
name: init-figma-design
description: >-
  Khởi tạo kiến trúc Figma cho một dự án/app mới theo chuẩn UXF: kiểm tra trình
  duyệt + đăng nhập Figma + Figma MCP, hỏi tên app, tạo (hoặc bổ sung) file
  ARCHITECTURE.md, rồi lần lượt tạo Team → Folder → File trên Figma và điền
  link vào ARCHITECTURE.md. Cấu trúc gồm team "0. Design system" (dùng chung)
  và team "N. Tên app" với 3 folder [Library] Snowflake, [Concept] Sandbox,
  [Handoff] App. Dùng skill này mỗi khi user nói "init design", "khởi tạo dự án
  design", "setup Figma cho app mới", "tạo team/folder/file Figma cho dự án",
  "dựng kiến trúc Figma", "tạo ARCHITECTURE.md cho design", "ghi link Figma có
  sẵn vào ARCHITECTURE.md", hoặc bắt đầu một app
  mới cần chỗ chứa design system/snowflake/concept/handoff — kể cả khi không
  nhắc tên skill.
---

# Init Figma Design — Khởi tạo kiến trúc Figma cho dự án

Skill này dựng "khung nhà" Figma cho một app mới để cả team (designer, dev, AI agent) biết design nằm ở đâu. Nguồn sự thật là file `ARCHITECTURE.md` ở thư mục gốc dự án: mọi team/folder/file tạo trên Figma đều được ghi link vào đó ngay khi tạo xong, nên nếu phiên bị ngắt giữa chừng thì lần chạy sau chỉ cần đọc file là biết còn thiếu gì.

```
Figma
├── Team "0. Design system"            ← dùng chung cho mọi app
│   └── Folder "[Design System] <App>"
│       └── File "[Design System] Version 0.0.0"
└── Team "<N>. <App>"                  ← mỗi app một team (N = 1, 2, 3...)
    ├── Folder "[Library] Snowflake"   → ❄️ [Snowflake] <App>   (component có context + screen)
    ├── Folder "[Concept] Sandbox"     → 🖼️ [Concept] <App>     (draft, demo, test concept trước khi chốt UI)
    └── Folder "[Handoff] App"         → ✅ [Handoff] <App>     (flow + mô tả dự án để build app)
```

Tên team/folder/file phải **giống từng ký tự** (kể cả emoji, ngoặc vuông, khoảng trắng) vì các skill khác (`uxf-ds-page-manager`, `uxf-snowflake-page-manager`, `uxf-handoff-page-manager`…) và dev dựa vào tên này để tìm file.

Giao tiếp với user bằng tiếng Việt.

---

## B1 — Kiểm tra môi trường

Cần đủ 3 thứ trước khi làm B4. B2–B3 vẫn làm được khi thiếu, nên đừng chặn user ở đây: cứ báo thiếu gì rồi sang B2. Nếu ở B2 user đã có đủ team/folder/file và chỉ cần điền link thì không cần đến các thứ này.

### 1.1 Trình duyệt

Xem trong danh sách tool (kể cả tool deferred) có:
- `mcp__Claude_Browser__*` — trình duyệt tích hợp của app Claude desktop (tab Code). **Ưu tiên dùng cái này.**
- `mcp__claude-in-chrome__*` — Claude in Chrome (dùng khi user muốn, hoặc không có cái trên).

Nếu không có cái nào (thường do đang chạy `claude` trong terminal/IDE), khuyên user:
> Skill này cần trình duyệt để tạo Team/Folder trên Figma. Bạn mở **app Claude desktop → tab Code** (có sẵn Browser pane), hoặc cài extension **Claude in Chrome**, rồi chạy lại skill.

Trước lần đầu dùng trình duyệt, đọc skill `anthropic-skills:built-in-browser` (hoặc `anthropic-skills:chrome-browser` khi dùng Chrome) nếu có trong danh sách skill.

**Browser pane phải đang hiển thị** thì Figma mới vẽ trang và click mới chạy (khi pane bị ẩn, click báo lỗi "not on screen / has not drawn yet"). Gặp lỗi đó thì nhờ user bật lại pane (**Ctrl+Shift+B** / Cmd+Shift+B) rồi làm tiếp.

### 1.2 Figma MCP — tài khoản chuẩn

Tìm tool `whoami` của Figma MCP (thường deferred → `ToolSearch` với query `figma whoami create_new_file`). Gọi `whoami`:
- Trả về `user_id`, `email` + danh sách `plans` (tên plan = tên team) → đã kết nối. Giữ lại kết quả, B2 và B4 cần dùng.
- Không có tool / báo cần xác thực / lỗi kết nối → nhờ user kết nối Figma MCP (app desktop: **Settings → Connectors → Figma**; CLI: chạy `/mcp` trong terminal `claude`). Không có MCP vẫn làm được (B4 tạo file bằng trình duyệt), nhưng chậm hơn — báo user.

**Tài khoản của MCP là tài khoản chuẩn** của cả phiên: mọi team/folder/file phải tạo bằng đúng tài khoản này, nếu không MCP sẽ không ghi được vào team vừa tạo. Báo email này cho user và hỏi đúng tài khoản họ muốn dùng chưa. Nếu user muốn tài khoản khác thì họ phải kết nối lại MCP bằng tài khoản đó.

### 1.3 Đăng nhập Figma trên trình duyệt (cùng tài khoản với MCP)

Mở `https://www.figma.com/files` (Browser pane: `preview_start` với `url`).
- Bị chuyển về trang login → nhờ user **tự đăng nhập trong Browser pane** bằng tài khoản ở 1.2 rồi báo lại. Không bao giờ tự gõ email/mật khẩu hay bấm "Sign in with Google" thay user.
- Đã đăng nhập → kiểm tra **đúng tài khoản**. Trình duyệt có thể đăng nhập nhiều tài khoản Figma cùng lúc; tài khoản đang active nằm trong tham số `fuid=<user_id>` của URL. Xem các tài khoản đang đăng nhập (chỉ đọc), chạy trong trang figma.com:
  ```js
  const r = await fetch('/api/session/state',{credentials:'include'}).then(r=>r.json());
  r.meta.users.map(u=>({id:u.id,email:u.email}))
  ```
  Chuyển sang tài khoản của MCP bằng cách thêm `?fuid=<user_id của whoami>` vào URL, và **giữ `fuid` đó trên mọi URL** điều hướng về sau. Nếu tài khoản của MCP không có trong danh sách → nhờ user đăng nhập thêm tài khoản đó.

Báo kết quả B1 thành một bảng ngắn: Trình duyệt ✅/❌ · Figma MCP ✅/❌ (email) · Trình duyệt đăng nhập đúng tài khoản ✅/❌.

---

## B2 — Giới thiệu skill và lấy input

Giới thiệu ngắn gọn **cấu trúc cần có** (vẽ lại cây ở đầu skill), giải thích công dụng từng folder:
- **[Library] Snowflake** — lưu component có context và screen (thư viện riêng của app, xây trên design system).
- **[Concept] Sandbox** — file nháp: demo, thử concept trước khi chốt giao diện.
- **[Handoff] App** — flow, luồng và mô tả dự án mà dev dùng để build app.

### 2.1 Hỏi user đã có sẵn team/folder chưa

Nhiều dự án đã dựng Figma từ trước. Khi đó việc của skill chỉ là ghi link vào `ARCHITECTURE.md`; tự tạo thêm sẽ sinh team/folder trùng tên. Vì vậy ngay sau phần giới thiệu, hỏi user bằng tool **`AskUserQuestion`** (nếu tool deferred thì load bằng `ToolSearch` query `select:AskUserQuestion`). Chỉ khi không có tool này mới hỏi bằng tin nhắn thường.

```
question: "Bạn đã có team / folder / file Figma cho dự án này chưa?"
header:   "Figma có sẵn"
options:
  - "Chưa có, tạo mới hết"  — Skill tạo toàn bộ team → folder → file (B4) và điền link.
  - "Đã có đầy đủ"           — Bạn dán link theo mẫu, skill chỉ điền vào ARCHITECTURE.md, không tạo gì trên Figma.
  - "Có một phần"            — Bạn dán link những mục đã có, skill tạo phần còn thiếu.
```

**Nếu chọn "Đã có đầy đủ" hoặc "Có một phần"**, gửi mẫu dưới đây (đã thay sẵn tên app nếu biết) và **chờ user dán lại**. Chưa có link thì không tự tạo gì. Mục nào user để trống nghĩa là chưa có.

```
Tên app: 
Team "0. Design system": 
Team "<N>. <App>": 
Folder "[Design System] <App>": 
Folder "[Library] Snowflake": 
Folder "[Concept] Sandbox": 
Folder "[Handoff] App": 
File "[Design System] Version 0.0.0": 
File "❄️ [Snowflake] <App>": 
File "🖼️ [Concept] <App>": 
File "✅ [Handoff] <App>": 
```

Khi user dán link vào:
1. **Kiểm tra loại link khớp với mục**:
   - Team: `figma.com/files/team/<teamId>`
   - Folder: `.../folder/<folderId>`, `.../project/<projectId>` hoặc `figma.com/files/project/<id>`
   - File: `figma.com/design/<fileKey>` hoặc `figma.com/file/<fileKey>`

   Dán nhầm loại (vd link file vào ô folder) → báo lại cho user, không tự đoán.
2. **Chuẩn hoá** theo định dạng ở B3: bỏ `fuid=`, `t=`, `node-id=` và slug tên. Link folder dạng `.../project/<projectId>` đổi thành `.../folder/<projectId>` (cùng một ID). Link folder **không có `teamId`** (`figma.com/files/project/<id>`) → lấy `teamId` từ link team mà folder đó thuộc về (user đã dán cùng mẫu) để ghép thành `https://www.figma.com/files/team/<teamId>/folder/<id>`; nếu chưa có link team thì mở link folder bằng trình duyệt (URL sau khi chuyển hướng có `teamId`), còn không có trình duyệt thì giữ nguyên `https://www.figma.com/files/project/<id>` và báo user.
3. **Kiểm tra tên nếu có trình duyệt** (không bắt buộc): mở `.../team/<teamId>/all-folders` rồi dùng `get_page_text` xem tên team/folder/file thật. Tên thật khác chuẩn (vd team tên `0. [Design System] Multiverse`) → **ghi tên thật vào bảng** để link và tên khớp nhau, báo user chỗ lệch. Không tự đổi tên trên Figma trừ khi user yêu cầu.
4. Lấy `teamId`/`folderId` từ link để B4 tạo đúng chỗ những mục còn thiếu.

Với "Đã có đầy đủ", không cần trình duyệt hay MCP: thiếu ở B1 cũng không sao, chỉ bỏ qua bước kiểm tra tên. Làm B3 xong thì sang 4.4 kiểm tra và báo cáo, bỏ qua 4.1–4.3. Ở 4.4 chỉ làm những bước có đủ công cụ (thiếu trình duyệt → bỏ bước kiểm tra tên/folder; bước kiểm tra file trống không áp dụng vì skill không tạo file nào), và ghi rõ trong báo cáo bước nào đã bỏ qua.

### 2.2 Input còn lại

| Input | Bắt buộc | Mặc định / cách suy ra |
| --- | --- | --- |
| Tên app | ✅ | Hỏi user. Không tự đoán từ tên thư mục, chỉ có thể *gợi ý*. |
| Số thứ tự team app `N` | | Lấy số lớn nhất trong **cả hai** nguồn rồi + 1: tên team dạng `<số>. <tên>` trong danh sách `plans` của `whoami`, và bảng Team của `ARCHITECTURE.md` (nếu có). Không có số nào thì `1`. Lý do: mỗi repo có `ARCHITECTURE.md` riêng còn team trên Figma là chung, nên chỉ đọc file sẽ khiến app nào cũng ra `1.`. Không có MCP → hỏi user số đang dùng lớn nhất. |
| Version design system | | `0.0.0` |
| Thư mục chứa `ARCHITECTURE.md` | | Thư mục gốc dự án (working directory) |

Đối chiếu với Figma bằng kết quả `whoami`:
- Đã có team tên đúng `0. Design system` → **dùng lại**, không tạo mới.
- Đã có team `<N>. <App>` → hỏi user dùng lại team đó hay đổi N/tên app. Tránh tạo trùng tên — Figma cho phép trùng nên rất dễ sinh rác.

Trước khi sang B4, gửi user một bản xác nhận gồm:
1. Những gì **sẽ tạo mới** và những gì **dùng lại** (gồm cả các mục user đã dán link ở 2.1).
2. **Các bước user phải tự làm**: với mỗi team mới, Figma bắt tích ô đồng ý điều khoản ở trang xác nhận gói (Claude không được tự đồng ý điều khoản thay user). Claude sẽ dừng ở trang đó và báo user.
3. Xin phép (một lần cho cả phiên): chọn gói **Education** (miễn phí), bấm "Complete upgrade" sau khi user đã tích ô, và nhận **ghế Full** ($0) khi Figma hỏi lúc tạo file đầu tiên trong team mới. Báo trước: nếu tài khoản không có gói Education thì skill sẽ dừng sau khi tạo team (gói Starter chỉ cho 1 folder mỗi team nên không dùng được cho cấu trúc này).

Chờ user đồng ý rồi mới làm. Tạo team trên Figma là thao tác thật, user khó dọn nếu sai tên.

---

## B3 — Tạo / bổ sung ARCHITECTURE.md

Khối kiến trúc nằm giữa 2 marker (HTML comment, không hiện khi render):
```
<!-- Design Figma Architecture Start -->
...
<!-- Design Figma Architecture End -->
```
Mẫu đầy đủ: `assets/architecture-block.md` (thay `{{APP}}`, `{{N}}`, `{{DS_VERSION}}`). Placeholder link luôn là chuỗi chính xác `Link figma điền tại đây` để dễ tìm những mục chưa có link.

Ba trường hợp:
1. **Chưa có file** → tạo `ARCHITECTURE.md` với tiêu đề `# Architecture` rồi chèn khối từ mẫu.
2. **Có file nhưng chưa có marker** → giữ nguyên nội dung cũ, chèn khối vào cuối file.
3. **Đã có khối** (thêm app thứ 2, 3…) → chỉ bổ sung, không viết lại:
   - Bảng Team: thêm dòng `| <N>. <App> | Link figma điền tại đây |`. Không thêm lại dòng `0. Design system`.
   - Thêm section `### <App>` gồm `Bảng Folder <App>` và `Bảng File <App>` trước marker End.
   - Nếu app đã có section → chỉ điền link còn thiếu, không nhân đôi dòng.

Link user đã dán ở 2.1 → điền ngay khi tạo/bổ sung khối. Những mục còn `Link figma điền tại đây` là việc của B4.

**Khi điền link**, sửa theo **nguyên dòng** của bảng, kèm dòng phía trên nếu cần. Lý do: chuỗi `| 0. Design system | Link figma điền tại đây |` và `| 1. <App> | Link figma điền tại đây |` cũng nằm trong các dòng của Bảng Folder, nên thay chuỗi ngắn sẽ khớp nhiều chỗ.

Định dạng link (bỏ `fuid=`, `t=`, `node-id=` và slug tên):
- Team: `https://www.figma.com/files/team/<teamId>`
- Folder: `https://www.figma.com/files/team/<teamId>/folder/<folderId>`
- File: `https://www.figma.com/design/<fileKey>`

---

## B4 — Dựng trên Figma: Team → Folder → File

Chỉ tạo những mục **còn placeholder** trong `ARCHITECTURE.md`. Mục user đã dán link ở 2.1 thì dùng lại, lấy `teamId`/`folderId` từ link đó để tạo phần con bên trong.

Làm **theo đúng thứ tự** vì mỗi cấp cần ID của cấp trên. **Sau mỗi mục tạo xong**, điền ngay link vào `ARCHITECTURE.md` trước khi sang mục tiếp theo, để nếu bị ngắt giữa chừng thì file vẫn phản ánh đúng thực tế.

**Trước khi tạo bất cứ thứ gì**, kiểm tra nó đã có chưa (dòng đã có link trong `ARCHITECTURE.md`, team có trong `whoami`, folder/file hiện trên trang team). Có rồi thì lấy link, không tạo lại.

Mẹo thao tác trình duyệt: tìm nút bằng `find` theo chữ ("Create folder", "Continue", "Skip for now", "Design"…) rồi click theo `ref`. Nếu `ref` báo "outside the viewport" thì chụp screenshot và click theo toạ độ. Popup gợi ý của Figma (vd "Code, now on canvas") có thể chiếm focus — đóng đi trước khi gõ phím. Figma gọi folder là "folder" trên UI nhưng là `projectId` trong MCP.

### 4.1 Team

Thứ tự: `0. Design system` (nếu chưa có) → `<N>. <App>`.

1. Mở thẳng trang tạo team: `https://www.figma.com/files/team/<id của team bất kỳ>/create-team?fuid=<user_id>` (hoặc menu chọn team ở sidebar → **Create new**).
2. Ô "Add a name" → gõ tên chính xác → **Create team**. URL chuyển sang `/files/team/<teamIdMới>/add-collaborators/...` → lấy `teamId` và **điền link team vào ARCHITECTURE.md ngay**.
3. "Add your collaborators" → **Skip for now**.
4. "Choose your team plan" → chọn **Education → "Upgrade for free"**. **Không chọn Starter**: team Starter chỉ được **1 folder** (và tối đa 3 file Design trong folder đó), mà team mới đã có sẵn "Team folder" chiếm chỗ, nên không tạo được folder nào ở 4.2 — team app cần 3 folder, team `0. Design system` cần thêm 1 folder cho mỗi app. Nếu không có lựa chọn Education (tài khoản chưa xác minh giáo dục) → **dừng lại**, giữ link team đã điền, báo user: cần xác minh Education cho tài khoản, hoặc user tự nâng cấp gói trả phí, rồi chạy lại skill. **Không bao giờ tự chọn Professional** hay gói nào có phí, không nhập thẻ.
5. Với Education, trang "Almost done! Everything look good?" ($0.00) có ô đồng ý điều khoản (nội dung có nhắc tự gia hạn/trừ tiền). **Dừng lại, nhờ user tự tích ô**. Khi user báo đã tích, chụp screenshot xác nhận ô đã được tích rồi mới bấm **Complete upgrade**. Trang chuyển về `/files/team/<teamId>/all-folders` là xong.

Team mới luôn có sẵn một folder rỗng tên "Team folder" — cứ để nguyên, không xoá hay đổi tên.

### 4.2 Folder

| Folder | Trong team |
| --- | --- |
| `[Design System] <App>` | `0. Design system` |
| `[Library] Snowflake` | `<N>. <App>` |
| `[Concept] Sandbox` | `<N>. <App>` |
| `[Handoff] App` | `<N>. <App>` |

Với mỗi folder: mở `https://www.figma.com/files/team/<teamId>/all-folders?fuid=<user_id>` → nút **Create folder** (góc trên phải, "+ Folder") → ô "Folder name": click, Ctrl+A, gõ tên → **Continue** → bước 2 (mời người) bấm **Create**. URL chuyển sang `/files/team/<teamId>/folder/<folderId>` → `folderId` chính là `projectId` cho 4.3. Điền link ngay.

### 4.3 File

| File | Trong folder |
| --- | --- |
| `[Design System] Version <DS_VERSION>` | `[Design System] <App>` |
| `❄️ [Snowflake] <App>` | `[Library] Snowflake` |
| `🖼️ [Concept] <App>` | `[Concept] Sandbox` |
| `✅ [Handoff] <App>` | `[Handoff] App` |

**Vì sao file đầu tiên của team mới phải tạo bằng trình duyệt:** ở team vừa tạo, tài khoản chỉ có ghế **View** (`whoami` thấy `"seat":"View"`), nên MCP `create_new_file` báo `Invalid planKey` hoặc "don't have edit access". Ghế Full ($0 trên Education) chỉ được cấp khi tạo file đầu tiên qua giao diện. Vì vậy với mỗi team:

1. **Gọi `whoami` lại**: kiểm tra tài khoản vẫn đúng (tài khoản của MCP có thể đổi giữa phiên) và xem `seat` của team.
2. **Nếu seat là View → tạo 1 file bằng trình duyệt**:
   - Mở folder (`.../folder/<folderId>?fuid=...`) → bấm nút **Create** (góc trên phải) → chọn **Design**.
   - Hộp thoại "You're about to get a Full seat" / "Get access to create files" → **Continue** (user đã cho phép ở B2). Editor mở file "Untitled".
   - Đổi tên — làm đúng trình tự, vì nếu ô tên chưa được focus thì phím gõ sẽ rơi xuống canvas thành phím tắt:
     1. Đóng popup gợi ý nếu có.
     2. Double-click vào tên file "Untitled" ở góc trên trái.
     3. `find` "File name" → click vào **textbox** "File name".
     4. Ctrl+A → gõ tên chính xác (emoji gõ trực tiếp được) → Enter.
     5. Tiêu đề tab đổi thành tên mới là xong.
   - Lấy `fileKey` từ URL `https://www.figma.com/design/<fileKey>/...` → điền link.
3. **Các file còn lại của team → MCP**: load skill `figma:figma-create-new-file` nếu có trong danh sách skill (tool yêu cầu vậy), rồi gọi `create_new_file` với `fileName` chính xác, `editorType: "design"`, `planKey: "team::<teamId>"`, `projectId: "<folderId>"`. Tool trả `file_url` → điền link.
4. MCP vẫn lỗi (không có MCP, sai tài khoản…) → tạo bằng trình duyệt như bước 2.

File để **trống** — skill này không dựng page. Dựng page để sau cho `uxf-ds-page-manager`, `uxf-snowflake-page-manager`, `uxf-handoff-page-manager`.

### 4.4 Kiểm tra cuối

- Trong khối của app vừa tạo không còn dòng nào chứa `Link figma điền tại đây`. (Luôn làm được, không cần công cụ.)
- *Cần trình duyệt:* mở `.../team/<teamId>/all-folders?fuid=...` của từng team, dùng `get_page_text` xem mỗi file nằm đúng folder và tên đúng từng ký tự (kể cả emoji).
- *Cần MCP, chỉ với file skill tạo bằng trình duyệt trong phiên này:* gọi `get_metadata` (`nodeId: "0:1"`) để chắc file vẫn trống, không bị phím gõ nhầm tạo layer.

Thiếu công cụ cho bước nào thì bỏ qua bước đó và ghi rõ trong báo cáo.

Báo cáo cho user: bảng những gì đã **tạo mới** / **dùng lại** kèm link, đường dẫn `ARCHITECTURE.md`, và gợi ý bước tiếp theo (dựng page bằng các skill `uxf-*-page-manager`).

---

## Nguyên tắc an toàn

- Không đăng nhập, không gõ mật khẩu, không cấp quyền OAuth thay user.
- Không tự tích ô đồng ý điều khoản; không chọn gói trả phí, không nhập thông tin thanh toán.
- Không xoá, đổi tên hay di chuyển team/folder/file có sẵn — skill chỉ tạo mới hoặc dùng lại.
- Gặp lỗi giữa chừng (Figma báo giới hạn gói, không thấy nút, mất đăng nhập, pane bị ẩn…): dừng, đảm bảo `ARCHITECTURE.md` đã có đủ các link đã tạo, báo user lỗi và cách tiếp tục. Lần chạy sau sẽ tiếp tục từ những dòng còn placeholder.
