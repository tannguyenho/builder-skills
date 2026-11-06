# builder-skills

Bộ skill của **UX Foundation** cho Claude (Claude Code, app Claude desktop, claude.ai). Mỗi skill là một quy trình được đóng gói sẵn: Claude đọc hướng dẫn trong skill và làm theo, nên cả team chạy cùng một cách, cùng một chuẩn đặt tên.

| Skill | Dùng để | Gọi bằng |
| --- | --- | --- |
| [`init-design`](skills/init-design/SKILL.md) | Dựng kiến trúc Figma cho app mới (Team → Folder → File) và ghi link vào `ARCHITECTURE.md` | "init design", "setup Figma cho app mới", "ghi link Figma vào ARCHITECTURE.md"… |

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

**Cập nhật** khi repo có skill mới hoặc bản sửa:

```bash
claude plugin marketplace update tannguyenho
```

> Nếu trước đây bạn đã chép tay skill vào `~/.claude/skills/init-design`, hãy xoá thư mục đó sau khi cài plugin để không bị trùng.

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
python scripts/package_skill.py init-design
```

File nằm ở `dist/init-design.skill`. Tải lên trong phần **Skills** ở Settings của claude.ai.

> Lưu ý: `init-design` cần trình duyệt để tạo Team/Folder trên Figma, nên chạy tốt nhất ở **tab Code của app Claude desktop**. Trên claude.ai chỉ dùng được phần ghi link có sẵn vào `ARCHITECTURE.md`.

---

## 2. Hướng dẫn dùng `init-design`

### Skill làm gì

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

### Cần chuẩn bị

| Thứ cần có | Vì sao | Cách có |
| --- | --- | --- |
| App **Claude desktop → tab Code** (hoặc extension **Claude in Chrome**) | Figma chỉ cho tạo Team/Folder qua giao diện web | Tải app Claude desktop; Browser pane có sẵn (bật/tắt bằng Ctrl+Shift+B) |
| **Figma MCP** đã kết nối | Đọc danh sách team, tạo file nhanh | App desktop: Settings → Connectors → Figma. CLI: `/mcp` |
| Tài khoản Figma có gói **Education** | Gói Starter chỉ cho **1 folder mỗi team**, không đủ cho cấu trúc trên | Xác minh Education trên Figma, hoặc dùng gói trả phí |
| Đăng nhập Figma trong Browser pane **cùng tài khoản** với Figma MCP | File/folder tạo bằng tài khoản khác thì MCP không ghi được | Tự đăng nhập trong Browser pane khi skill nhắc |

Nếu bạn **đã có sẵn** đủ team/folder/file và chỉ cần ghi link thì không cần trình duyệt hay MCP.

### Chạy

1. Mở dự án của app trong Claude (thư mục sẽ chứa `ARCHITECTURE.md`).
2. Gõ: `init design cho app <Tên app>` (hoặc gọi thẳng `/builder-skills:init-design` nếu cài bằng plugin, `/init-design` nếu chép tay).
3. Skill sẽ:
   1. **Kiểm tra môi trường** và báo bảng ✅/❌ (trình duyệt, Figma MCP, đúng tài khoản).
   2. **Hỏi bạn đã có sẵn team/folder/file chưa**: tạo mới hết, đã có đủ (chỉ dán link), hoặc có một phần.
   3. **Gửi bản xác nhận** những gì sẽ tạo mới / dùng lại. Chưa đồng ý thì không tạo gì.
   4. Tạo hoặc bổ sung `ARCHITECTURE.md`, rồi tạo lần lượt Team → Folder → File trên Figma. Mỗi mục tạo xong được ghi link ngay.
   5. Kiểm tra lại và báo cáo kèm link.

### Những bước bạn phải tự làm

- **Đăng nhập Figma** trong Browser pane. Claude không gõ mật khẩu thay bạn.
- **Tích ô đồng ý điều khoản** ở trang chọn gói Education của mỗi team mới. Claude dừng ở trang đó, chờ bạn tích rồi mới bấm "Complete upgrade".

### Bị ngắt giữa chừng?

Cứ chạy lại skill. Mục nào trong `ARCHITECTURE.md` còn ghi `Link figma điền tại đây` là mục chưa làm; skill chỉ làm tiếp những mục đó và không tạo trùng.

### Kết quả mẫu

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
6. **Tăng `version`** trong `.claude-plugin/plugin.json` (vd `0.1.0` → `0.2.0` khi thêm skill, `0.1.1` khi sửa nhỏ), rồi commit và push. Mọi người lấy bản mới bằng `claude plugin marketplace update tannguyenho`.

### Lưu ý khi viết skill

- Repo này **public**: không đưa vào skill token, mật khẩu, email, link Figma/Drive nội bộ của khách hàng.
- Thao tác thật trên dịch vụ ngoài (tạo team, gửi tin, xoá file…) phải có bước **xin xác nhận user** trước khi làm.
- Những việc Claude không được làm thay (đăng nhập, đồng ý điều khoản, thanh toán) phải ghi rõ là user tự làm.
