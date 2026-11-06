# builder-skills

Bộ skill của **UX Foundation** cho Claude (Claude Code, app Claude desktop, claude.ai). Mỗi skill là một quy trình được đóng gói sẵn: Claude đọc hướng dẫn trong skill và làm theo, nên cả team chạy cùng một cách, cùng một chuẩn đặt tên.

| Skill | Dùng để | Gọi bằng |
| --- | --- | --- |
| [`init-figma-design`](skills/init-figma-design/SKILL.md) | Dựng kiến trúc Figma cho app mới (Team → Folder → File) và ghi link vào `ARCHITECTURE.md` | "init design", "setup Figma cho app mới", "ghi link Figma vào ARCHITECTURE.md"… |
| [`ds-page-manager`](skills/ds-page-manager/SKILL.md) | Sắp xếp page trong file **Design System** theo Category (FOUNDATION, ACTIONS, DATA ENTRY…) | "sắp xếp page file DS", "kiểm tra cấu trúc page DS"… |
| [`snowflake-page-manager`](skills/snowflake-page-manager/SKILL.md) | Sắp xếp page trong file **Snowflake** theo BASE / COMPONENT / SCREEN | "sắp xếp page file Snowflake", "kiểm tra page Snowflake"… |
| [`handoff-page-manager`](skills/handoff-page-manager/SKILL.md) | Sắp xếp page trong file **Handoff** theo CHANGE LOG / USER FLOW / UI GUIDELINE / DESIGN QA / COVER | "sắp xếp page file handoff", "tạo page còn thiếu cho handoff"… |

Thứ tự dùng thường gặp cho một app mới:

```
init-figma-design          → tạo team/folder/file trống, ghi link vào ARCHITECTURE.md
   ├── ds-page-manager         → dựng page cho file  [Design System] Version x.y.z
   ├── snowflake-page-manager  → dựng page cho file  ❄️ [Snowflake] <App>
   └── handoff-page-manager    → dựng page cho file  ✅ [Handoff] <App>
```

---

## 1. Cài đặt

Chọn **một** trong ba cách. Đừng cài cùng một skill bằng hai cách, vì Claude sẽ thấy hai bản và có thể chọn nhầm bản cũ.

### Cách A — Plugin cho Claude Code / app Claude desktop (khuyên dùng)

Cài một lần, sau này cập nhật bằng một lệnh. Chạy trong terminal:

```bash
claude plugin marketplace add tannguyenho/builder-skills
```

```bash
claude plugin install builder-skills@tannguyenho
```

Hoặc gõ trong phiên `claude` tương tác: `/plugin marketplace add tannguyenho/builder-skills` rồi `/plugin install builder-skills@tannguyenho`.

Plugin cài ở phạm vi user nên dùng được cả trong terminal lẫn tab **Code** của app Claude desktop. Mở phiên mới để Claude nạp skill.

**Cập nhật** khi repo có skill mới hoặc bản sửa (lệnh 1 tải bản mới của repo, lệnh 2 cài bản đó), rồi mở phiên mới:

```bash
claude plugin marketplace update tannguyenho
```

```bash
claude plugin update builder-skills@tannguyenho
```

> **Tránh trùng skill:** nếu trước đây bạn đã có các skill này dưới tên cũ (`uxf-init-design`, `uxf-ds-page-manager`, `uxf-snowflake-page-manager`, `uxf-handoff-page-manager`) — chép tay trong `~/.claude/skills/` hoặc tải lên claude.ai — hãy xoá bản cũ sau khi cài plugin. Skill tải lên claude.ai được đồng bộ về app desktop, nên phải xoá trong phần **Skills** ở Settings của claude.ai.

### Cách B — Chép tay vào thư mục skills

Dùng khi muốn sửa thử skill ngay trên máy.

```bash
git clone https://github.com/tannguyenho/builder-skills.git
```

Rồi chép thư mục skill cần dùng vào một trong hai nơi:

- `~/.claude/skills/<tên-skill>/` — dùng cho mọi dự án (Windows: `C:\Users\<bạn>\.claude\skills\`).
- `<dự án>/.claude/skills/<tên-skill>/` — chỉ dùng trong dự án đó, commit cùng dự án để cả team có.

Cách này không tự cập nhật: muốn bản mới thì `git pull` rồi chép lại.

### Cách C — claude.ai (web / app chat)

claude.ai nhận skill dạng file `.skill` (zip của thư mục skill). Đóng gói:

```bash
python scripts/package_skill.py
```

Lệnh trên đóng gói mọi skill vào `dist/<tên-skill>.skill`; muốn một skill thì thêm tên, vd `python scripts/package_skill.py ds-page-manager`. Tải file lên trong phần **Skills** ở Settings của claude.ai.

> Lưu ý: `init-figma-design` cần trình duyệt để tạo Team/Folder trên Figma, nên chạy tốt nhất ở **tab Code của app Claude desktop**. Trên claude.ai chỉ dùng được phần ghi link có sẵn vào `ARCHITECTURE.md`. Ba skill `*-page-manager` chạy được ở mọi nơi có kết nối Figma.

---

## 2. Hướng dẫn dùng

### 2.1 `init-figma-design` — dựng kiến trúc Figma

#### Skill làm gì

Tạo "khung nhà" Figma cho một app và ghi toàn bộ link vào file `ARCHITECTURE.md` ở gốc dự án, để designer, dev và AI agent đều biết design nằm ở đâu:

```
Figma
├── Team "0. Design system"            ← dùng chung cho mọi app
│   └── Folder "[Design System] <App>"
│       └── File "[Design System] Version 0.0.0"
└── Team "<N>. <App>"                  ← mỗi app một team
    ├── Folder "[Library] Snowflake"   → ❄️ [Snowflake] <App>
    ├── Folder "[Concept] Sandbox"     → 🖼️ [Concept] <App>
    └── Folder "[Handoff] App"         → ✅ [Handoff] <App>
```

#### Cần chuẩn bị

| Thứ cần có | Vì sao | Cách có |
| --- | --- | --- |
| App **Claude desktop → tab Code** (hoặc extension **Claude in Chrome**) | Figma chỉ cho tạo Team/Folder qua giao diện web | Tải app Claude desktop; Browser pane có sẵn (bật/tắt bằng Ctrl+Shift+B) |
| **Figma MCP** đã kết nối | Đọc danh sách team, tạo file nhanh | App desktop: Settings → Connectors → Figma. CLI: `/mcp` |
| Tài khoản Figma có gói **Education** | Gói Starter chỉ cho **1 folder mỗi team**, không đủ cho cấu trúc trên | Xác minh Education trên Figma, hoặc dùng gói trả phí |
| Đăng nhập Figma trong Browser pane **cùng tài khoản** với Figma MCP | File/folder tạo bằng tài khoản khác thì MCP không ghi được | Tự đăng nhập trong Browser pane khi skill nhắc |

Nếu bạn **đã có sẵn** đủ team/folder/file và chỉ cần ghi link thì không cần trình duyệt hay MCP.

#### Chạy

1. Mở dự án của app trong Claude (thư mục sẽ chứa `ARCHITECTURE.md`).
2. Gõ: `init design cho app <Tên app>` (hoặc gọi thẳng `/builder-skills:init-figma-design` nếu cài bằng plugin, `/init-figma-design` nếu chép tay).
3. Skill sẽ:
   1. **Kiểm tra môi trường** và báo bảng ✅/❌ (trình duyệt, Figma MCP, đúng tài khoản).
   2. **Hỏi bạn đã có sẵn team/folder/file chưa**: tạo mới hết, đã có đủ (chỉ dán link), hoặc có một phần.
   3. **Gửi bản xác nhận** những gì sẽ tạo mới / dùng lại. Chưa đồng ý thì không tạo gì.
   4. Tạo hoặc bổ sung `ARCHITECTURE.md`, rồi tạo lần lượt Team → Folder → File trên Figma. Mỗi mục tạo xong được ghi link ngay.
   5. Kiểm tra lại và báo cáo kèm link.

#### Những bước bạn phải tự làm

- **Đăng nhập Figma** trong Browser pane. Claude không gõ mật khẩu thay bạn.
- **Tích ô đồng ý điều khoản** ở trang chọn gói Education của mỗi team mới. Claude dừng ở trang đó, chờ bạn tích rồi mới bấm "Complete upgrade".

#### Bị ngắt giữa chừng?

Cứ chạy lại skill. Mục nào trong `ARCHITECTURE.md` còn ghi `Link figma điền tại đây` là mục chưa làm; skill chỉ làm tiếp những mục đó và không tạo trùng.

#### Kết quả mẫu

```markdown
<!-- Design Figma Architecture Start -->
## 🎨 Design Figma Architecture

### Team

| Team | Link |
| --- | --- |
| 0. Design system | https://www.figma.com/files/team/<teamId> |
| 1. My App | https://www.figma.com/files/team/<teamId> |

### My App

#### Bảng Folder My App
...
#### Bảng File My App
...
<!-- Design Figma Architecture End -->
```

### 2.2 Ba skill `*-page-manager` — sắp xếp page trong file Figma

Ba skill cùng một cách làm, mỗi skill áp chuẩn cho một loại file:

| Skill | Áp cho file | Cấu trúc page chuẩn |
| --- | --- | --- |
| `ds-page-manager` | `[Design System] Version x.y.z` | `🖼️ Cover` → các nhóm Category viết HOA kèm emoji (`🎨 FOUNDATION`, `⚡ ACTIONS`, `✏️ DATA ENTRY`, `📊 DATA DISPLAY`, `🧩 PATTERNS`, `📐 TEMPLATES`), mỗi component một sub-page `→ Tên` |
| `snowflake-page-manager` | `❄️ [Snowflake] <App>` | `🖼️ COVER` → `📦 BASE` → `🍀 COMPONENT` (A–Z) → `🖥️ SCREEN`, mỗi mục một sub-page `→ Tên` |
| `handoff-page-manager` | `✅ [Handoff] <App>` | `📋 CHANGE LOG` → `🦶 USER FLOW` → `📐 UI GUIDELINE` → `🚧 DESIGN QA` → `🖼️ COVER` (cover nằm **cuối**) |

Quy ước chung của cả ba:

- Sub-page bắt đầu bằng `→ ` (mũi tên thật, không phải `->`).
- Page tên `---` để trống, làm vạch ngăn giữa các nhóm.
- Emoji chỉ dùng ở tên page nhóm, **không** dùng trong tên component.

#### Cần chuẩn bị

- **Figma MCP** đã kết nối, bằng tài khoản có quyền sửa file (ghế Full). App desktop: Settings → Connectors → Figma.
- Link file Figma cần sắp xếp. Nếu dự án đã chạy `init-figma-design`, link nằm sẵn trong `ARCHITECTURE.md`.

#### Chạy

Mở dự án trong Claude rồi nói, kèm link file nếu có, ví dụ:

- `Sắp xếp page cho file DS <link>`
- `Kiểm tra cấu trúc page file Snowflake của app này đúng chuẩn chưa`
- `Tạo các page còn thiếu cho file handoff <link>`

Hoặc gọi thẳng `/builder-skills:ds-page-manager`, `/builder-skills:snowflake-page-manager`, `/builder-skills:handoff-page-manager`.

#### Skill sẽ và không làm gì

- **Có:** tạo page còn thiếu, đổi tên page, sắp xếp lại thứ tự page theo chuẩn.
- **Không:** di chuyển, cắt/dán hay đổi chỗ bất kỳ component, frame, instance nào. Nội dung trong mỗi page giữ nguyên. Tên `→ …` trong chuẩn chỉ là tên gợi ý cho page, không phải lệnh chuyển component sang đó.

---

## 3. Build skill mới trong repo này

### Cấu trúc repo

```
builder-skills/
├── .claude-plugin/
│   ├── marketplace.json     ← khai báo marketplace "tannguyenho"
│   └── plugin.json          ← plugin "builder-skills", nạp mọi skill trong skills/
├── skills/
│   └── <tên-skill>/
│       ├── SKILL.md         ← bắt buộc
│       ├── assets/          ← mẫu, template mà skill dùng (tuỳ chọn)
│       ├── references/      ← tài liệu dài, chỉ đọc khi cần (tuỳ chọn)
│       └── scripts/         ← script skill gọi tới (tuỳ chọn)
└── scripts/package_skill.py ← đóng gói .skill cho claude.ai
```

Plugin tự nạp mọi thư mục trong `skills/`, nên thêm skill mới **không cần sửa** `plugin.json`.

### Quy trình

1. **Tạo thư mục** `skills/<tên-skill>/`. Tên viết thường, nối bằng gạch ngang, **không** thêm tiền tố `uxf-` (vd `handoff-page-manager`). Khi cài bằng plugin, Claude tự gắn tiền tố `builder-skills:` nên không cần thêm gì để phân biệt.
2. **Viết `SKILL.md`**. Cách nhanh nhất: mở Claude trong repo này và nói *"tạo skill mới tên … để …"*. Claude sẽ dùng skill `skill-creator` để soạn, chạy thử và chỉnh. Khung tối thiểu:

   ```markdown
   ---
   name: ten-skill
   description: >-
     Skill làm gì + KHI NÀO dùng. Liệt kê các câu user hay nói để kích hoạt
     ("…", "…"), kể cả khi user không nhắc tên skill.
   ---

   # Tiêu đề

   Mục tiêu, các bước, nguyên tắc an toàn…
   ```

   - `name` phải trùng tên thư mục.
   - `description` quyết định Claude có tự gọi skill hay không: ghi rõ *làm gì* và *khi nào dùng*.
   - Giữ `SKILL.md` gọn (dưới ~500 dòng). Phần dài đưa vào `references/` và ghi trong `SKILL.md` khi nào cần đọc.
   - Giải thích *vì sao* cho mỗi quy tắc quan trọng, để Claude xử lý được cả trường hợp skill không nói tới.
3. **Chạy thử trên máy** trước khi push. Mở Claude với plugin lấy thẳng từ thư mục repo:

   ```bash
   claude --plugin-dir .
   ```

   Rồi gõ đúng câu mà user thật sẽ nói, xem skill có được gọi và làm đúng không.
4. **Kiểm tra định dạng / đóng gói**:

   ```bash
   python scripts/package_skill.py <tên-skill>
   ```

   Script báo lỗi nếu thiếu frontmatter hoặc `name` không khớp tên thư mục.
5. **Cập nhật README**: thêm một dòng vào bảng skill ở đầu file, và một mục hướng dẫn dùng nếu skill cần chuẩn bị gì.
6. **Tăng `version`** trong `.claude-plugin/plugin.json` (vd `0.1.0` → `0.2.0` khi thêm skill, `0.1.1` khi sửa nhỏ), rồi commit và push. Mọi người lấy bản mới bằng `claude plugin marketplace update tannguyenho` rồi `claude plugin update builder-skills@tannguyenho`.

### Lưu ý khi viết skill

- Repo này **public**: không đưa vào skill token, mật khẩu, email, link Figma/Drive nội bộ của khách hàng.
- Thao tác thật trên dịch vụ ngoài (tạo team, gửi tin, xoá file…) phải có bước **xin xác nhận user** trước khi làm.
- Những việc Claude không được làm thay (đăng nhập, đồng ý điều khoản, thanh toán) phải ghi rõ là user tự làm.
