"""Đóng gói skill thành file .skill (zip) để tải lên claude.ai.

Cách dùng:
    python scripts/package_skill.py               # đóng gói mọi skill trong skills/
    python scripts/package_skill.py init-figma-design

Kết quả nằm ở dist/<tên-skill>.skill (thư mục dist/ không được commit).
"""

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def check(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        sys.exit(f"Thiếu {skill_md}")
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        sys.exit(f"{skill_md}: thiếu frontmatter (phải bắt đầu bằng ---)")
    header = text.split("---", 2)[1]
    if f"name: {skill_dir.name}" not in header:
        sys.exit(f"{skill_md}: 'name:' phải trùng tên thư mục '{skill_dir.name}'")
    if "description:" not in header:
        sys.exit(f"{skill_md}: thiếu 'description:'")


def package(skill_dir: Path) -> Path:
    check(skill_dir)
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{skill_dir.name}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file():
                z.write(f, f"{skill_dir.name}/{f.relative_to(skill_dir).as_posix()}")
    return out


def main() -> None:
    # Console Windows mặc định cp1252, không in được tiếng Việt/ký tự ✓.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    names = sys.argv[1:] or sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    for name in names:
        skill_dir = SKILLS / name
        if not skill_dir.is_dir():
            sys.exit(f"Không có skill '{name}' trong {SKILLS}")
        print(f"✓ {package(skill_dir).relative_to(ROOT)}")


if __name__ == "__main__":
    main()
