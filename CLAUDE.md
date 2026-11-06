# builder-skills — ghi chú cho Claude

Repo chứa skill của UX Foundation, phát hành dưới dạng plugin Claude Code (`builder-skills@tannguyenho`). Giao tiếp với user bằng tiếng Việt.

- Mỗi skill nằm ở `skills/<tên-skill>/SKILL.md`; `name:` trong frontmatter phải trùng tên thư mục. Skill UXF đặt tên `uxf-…`.
- Khi tạo hoặc sửa skill, dùng skill `skill-creator` nếu có.
- Repo public: không ghi token, email, link Figma/Drive nội bộ vào skill.
- Sau khi thêm/sửa skill: chạy `python scripts/package_skill.py <tên-skill>` để kiểm tra, cập nhật bảng skill trong `README.md`, tăng `version` trong `.claude-plugin/plugin.json`.
- Thư mục `dist/` là sản phẩm đóng gói, không commit.
