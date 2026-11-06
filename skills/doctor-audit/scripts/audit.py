#!/usr/bin/env python3
"""Kiểm tra bộ skill builder-skills. Chỉ dùng thư viện chuẩn.

Cách dùng (chạy từ gốc repo builder-skills):
    python skills/doctor-audit/scripts/audit.py check [tên-skill ...]
    python skills/doctor-audit/scripts/audit.py upstream --clone <owner/repo>=<thư mục clone> ...
    python skills/doctor-audit/scripts/audit.py mark-synced <owner/repo> <commit>

`check`     kiểm tra tĩnh mọi skill (hoặc các skill được nêu tên). Mã thoát 1 nếu có lỗi (❌).
`upstream`  so bản clone mới nhất của repo gốc với commit đã ghi trong references/upstream.json:
            skill nào có file gốc đổi, skill gốc mới chưa dịch, đường dẫn gốc đã biến mất.
`mark-synced` ghi commit mới vào upstream.json sau khi đã dịch xong phần thay đổi.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
ROOT = SKILL_DIR.parent.parent
SKILLS = ROOT / "skills"
MANIFEST = SKILL_DIR / "references" / "upstream.json"

DESC_MAX = 1024          # giới hạn độ dài description của Claude
DESC_WARN = 900          # sát giới hạn: thêm một câu kích hoạt là vượt
NEAR_DUP = 0.6           # lọc nhanh theo ký tự
NEAR_DUP_LINES = 0.3     # tỉ lệ dòng giống nhau từ mức này mới báo
BODY_WARN = 500          # SKILL.md dài hơn thì nên tách references/
VI_CHARS = re.compile(r"[ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]", re.I)
SECRET_PATTERNS = {
    "link Figma file": re.compile(r"figma\.com/(design|file|board|proto)/[A-Za-z0-9]{10,}"),
    "link Google Drive/Docs": re.compile(r"(drive|docs)\.google\.com/[^\s)]+/d/[A-Za-z0-9_-]{15,}"),
    "token dạng ghp_/sk-/xox": re.compile(r"\b(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|xox[abp]-[A-Za-z0-9-]{10,})"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
}
EMAIL_OK = {"noreply@anthropic.com"}
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
PATH_MENTION = re.compile(r"`((?:references|assets|scripts)/[^`\s]+|[A-Z][A-Z0-9-]+\.md)`")
# Lời GỌI skill (agent sẽ chạy nó) — dùng để phát hiện skill bị gọi mà lại chặn tự gọi.
SKILL_CALL = re.compile(r"(?:gọi Skill tool với|gọi skill|Skill tool with|Skill tool twice, for)\s+[`\"]([a-z0-9]+(?:-[a-z0-9]+)*)[`\"]", re.I)
# Mọi lần NHẮC tới một skill — tên phải tồn tại trong repo.
SKILL_MENTION = re.compile(r"(?:skill|Skill tool với|Skill tool with)\s+[`\"]([a-z0-9]+(?:-[a-z0-9]+)*)[`\"]", re.I)


# ---------------------------------------------------------------- helpers

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    _, header, body = text.split("---", 2)
    fm: dict[str, str] = {}
    key = None
    for line in header.splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            fm[key] = "" if val in (">-", ">", "|", "|-") else val.strip("\"'")
        elif key and line.startswith((" ", "\t")):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def skill_dirs(names: list[str] | None) -> list[Path]:
    all_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not names:
        return all_dirs
    by = {p.name: p for p in all_dirs}
    missing = [n for n in names if n not in by]
    if missing:
        sys.exit(f"Không có skill: {', '.join(missing)}")
    return [by[n] for n in names]


# ---------------------------------------------------------------- check

def check(names: list[str] | None) -> int:
    issues: dict[str, list[tuple[str, str]]] = defaultdict(list)
    all_names = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    manual: set[str] = set()
    callers: dict[str, set[str]] = defaultdict(set)
    hashes: dict[str, list[str]] = defaultdict(list)
    targets = skill_dirs(names)

    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir() or not (d / "SKILL.md").is_file():
            continue
        text = (d / "SKILL.md").read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm.get("disable-model-invocation") == "true":
            manual.add(d.name)
        for f in d.rglob("*.md"):
            for callee in SKILL_CALL.findall(strip_code(f.read_text(encoding="utf-8"))):
                if callee != d.name:
                    callers[callee].add(d.name)
        for f in d.rglob("*"):
            if f.is_file():
                hashes[hashlib.sha1(f.read_bytes()).hexdigest()].append(str(f.relative_to(SKILLS)))

    for d in targets:
        n = d.name
        add = lambda lvl, msg: issues[n].append((lvl, msg))
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            add("❌", "thiếu SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if not fm:
            add("❌", "thiếu frontmatter")
        if fm.get("name") != n:
            add("❌", f"name '{fm.get('name')}' không trùng tên thư mục")
        desc = fm.get("description", "")
        if not desc:
            add("❌", "thiếu description")
        elif len(desc) > DESC_MAX:
            add("❌", f"description dài {len(desc)} ký tự (> {DESC_MAX})")
        elif len(desc) > DESC_WARN:
            add("⚠️", f"description dài {len(desc)}/{DESC_MAX} ký tự — sát giới hạn")
        elif n not in manual and len(desc) < 120:
            add("⚠️", f"description ngắn ({len(desc)} ký tự) — Claude có thể không tự gọi skill")
        if n.startswith("uxf-"):
            add("❌", "tên skill không được có tiền tố uxf-")
        lines = body.count("\n")
        if lines > BODY_WARN:
            add("⚠️", f"SKILL.md dài {lines} dòng (> {BODY_WARN}) — cân nhắc tách sang references/")

        # liên kết & file được nhắc tới
        referenced: set[Path] = set()
        for f in d.rglob("*.md"):
            t = f.read_text(encoding="utf-8")
            prose = strip_code(t)
            for target in LINK.findall(prose):
                if re.match(r"^[a-z]+:", target):
                    continue
                p = (f.parent / target).resolve()
                referenced.add(p)
                if not p.exists():
                    add("❌", f"{f.relative_to(d)}: link hỏng → {target}")
            for target in PATH_MENTION.findall(t):
                for base in (d, f.parent):
                    if (base / target).exists():
                        referenced.add((base / target).resolve())
            for callee in SKILL_MENTION.findall(prose):
                if callee not in all_names:
                    add("❌", f"{f.relative_to(d)}: nhắc tới skill không tồn tại '{callee}'")
            for label, pat in SECRET_PATTERNS.items():
                for hit in (mm.group(0) for mm in pat.finditer(t)):
                    if label == "email" and (hit in EMAIL_OK or hit.endswith("@example.com")):
                        continue
                    add("❌", f"{f.relative_to(d)}: có {label} ({hit[:40]}) — repo public")
            # đoạn văn còn tiếng Anh (bỏ code, bảng, tiêu đề ngắn)
            for para in re.split(r"\n\s*\n", prose):
                words = re.findall(r"[A-Za-zÀ-ỹ]+", para)
                if len(words) >= 25 and not VI_CHARS.search(para) and not para.lstrip().startswith(("|", "<", "-", "#", ">", "`")):
                    add("⚠️", f"{f.relative_to(d)}: có đoạn có vẻ chưa dịch: \"{para.strip()[:70]}…\"")
                    break
        for f in d.rglob("*"):
            if f.is_file() and f.name != "SKILL.md" and f.suffix in (".md", ".sh", ".py", ".html", ".json") \
                    and f.resolve() not in referenced and f.parent.name != "scripts":
                # file trong references/ mà không ai nhắc tới thì agent không bao giờ đọc
                if f.name not in text and not any(f.name in g.read_text(encoding="utf-8") for g in d.rglob("*.md") if g != f):
                    add("⚠️", f"{f.relative_to(d)}: không được nhắc tới ở đâu — agent sẽ không đọc")

        # skill bị gọi bởi skill khác nhưng lại chặn tự gọi
        if n in manual and callers.get(n):
            add("❌", f"có disable-model-invocation nhưng được gọi từ: {', '.join(sorted(callers[n]))}")

    # file trùng nhau giữa các skill
    dup_report = []
    for paths in hashes.values():
        involved = {p.split("/", 1)[0] for p in paths}
        if len(paths) > 1 and involved & {t.name for t in targets}:
            dup_report.append(paths)

    # file cùng tên, gần giống nhau (không y hệt) giữa các skill — dễ lệch thuật ngữ
    by_name: dict[str, list[Path]] = defaultdict(list)
    for f in SKILLS.rglob("*.md"):
        if f.name != "SKILL.md":
            by_name[f.name].append(f)
    near_report = []
    target_names = {t.name for t in targets}
    for name, files in sorted(by_name.items()):
        for i, a in enumerate(files):
            for b in files[i + 1:]:
                sa, sb = a.relative_to(SKILLS).parts[0], b.relative_to(SKILLS).parts[0]
                if sa == sb or not ({sa, sb} & target_names):
                    continue
                ta, tb = a.read_text(encoding="utf-8"), b.read_text(encoding="utf-8")
                if ta == tb:
                    continue
                ratio = difflib.SequenceMatcher(None, ta, tb, autojunk=False).quick_ratio()
                if ratio >= NEAR_DUP:
                    ratio = difflib.SequenceMatcher(None, ta.splitlines(), tb.splitlines()).ratio()
                    if ratio >= NEAR_DUP_LINES:
                        near_report.append((a.relative_to(SKILLS), b.relative_to(SKILLS), ratio))

    # README & plugin
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    for d in targets:
        if f"(skills/{d.name}/SKILL.md)" not in readme:
            issues[d.name].append(("⚠️", "chưa có trong bảng skill của README.md"))

    errors = sum(1 for v in issues.values() for lvl, _ in v if lvl == "❌")
    warns = sum(1 for v in issues.values() for lvl, _ in v if lvl == "⚠️")
    print(f"# Kiểm tra tĩnh — {len(targets)} skill, {errors} lỗi ❌, {warns} cảnh báo ⚠️\n")
    for d in targets:
        rows = issues.get(d.name)
        if not rows:
            print(f"- ✅ `{d.name}`")
            continue
        print(f"- `{d.name}`")
        for lvl, msg in sorted(rows):
            print(f"  - {lvl} {msg}")
    if dup_report:
        print("\n## File trùng nội dung giữa các skill")
        print("(Có thể cố ý — vd tdd.md cần có ở cả implement và implement-spec — nhưng khi sửa phải sửa đồng bộ.)\n")
        for paths in dup_report:
            print("- " + " = ".join(f"`{p}`" for p in sorted(paths)))
    if near_report:
        print("\n## File cùng tên, gần giống nhau giữa các skill")
        print("(Xem có nên thống nhất đoạn chung và thuật ngữ không — xem review-criteria.md.)\n")
        for a, b, r in near_report:
            print(f"- `{a}` ≈ `{b}` — {r:.0%} dòng giống nhau")
    return 1 if errors else 0


# ---------------------------------------------------------------- upstream

def git(clone: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(clone), *args], check=True, capture_output=True, text=True).stdout


def upstream(clones: dict[str, Path]) -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    print("# So với repo gốc\n")
    for repo, meta in data["upstreams"].items():
        clone = clones.get(repo)
        if not clone:
            print(f"## {repo}\n\n- ⏭️ bỏ qua (không truyền --clone {repo}=<thư mục>)\n")
            continue
        old = meta["synced_commit"]
        head = git(clone, "rev-parse", "HEAD").strip()
        print(f"## {repo}\n\n- Đã đồng bộ: `{old[:10]}` ({meta['synced_at']}) → mới nhất: `{head[:10]}`")
        if old == head:
            print("- ✅ Không có commit mới.\n")
        try:
            git(clone, "cat-file", "-e", old + "^{commit}")
        except subprocess.CalledProcessError:
            print(f"- ❌ Bản clone không có commit `{old[:10]}` — clone lại không dùng --depth (vd `--filter=blob:none`).\n")
            continue
        mapped = {s: v for s, v in data["skills"].items() if v["upstream"] == repo}
        changed_any = False
        for skill, v in sorted(mapped.items()):
            gone = [p for p in v["paths"] if not (clone / p).exists()]
            if gone:
                print(f"- ❌ `{skill}`: đường dẫn gốc không còn: {', '.join(gone)} (bị đổi tên/xoá? tìm bằng `git log --follow`)")
            if old == head:
                continue
            files = git(clone, "diff", "--name-status", old, head, "--", *v["paths"]).strip()
            if files:
                changed_any = True
                print(f"- 🔄 `{skill}` có thay đổi:")
                for line in files.splitlines():
                    print(f"  - `{line}`")
        if old != head and not changed_any:
            print("- ✅ Các skill đã dịch không đổi (commit mới chỉ chạm file khác).")
        # skill gốc mới chưa dịch
        covered = {p.rstrip("/").split("/")[-1] for v in mapped.values() for p in v["paths"]}
        known = covered | set(meta.get("ignored_skills", []))
        new = []
        for base in meta.get("scan", []):
            for sk in sorted((clone / base).glob("*/SKILL.md")):
                if sk.parent.name not in known:
                    new.append(f"{base}{sk.parent.name}/")
        if new:
            print("- 🆕 Skill gốc chưa dịch, chưa bị bỏ qua: " + ", ".join(f"`{p}`" for p in new))
        print()
    return 0


def mark_synced(repo: str, commit: str) -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if repo not in data["upstreams"]:
        sys.exit(f"Không có upstream '{repo}' trong {MANIFEST.name}")
    data["upstreams"][repo]["synced_commit"] = commit
    data["upstreams"][repo]["synced_at"] = date.today().isoformat()
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ {repo} → {commit[:10]}")
    return 0


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("skills", nargs="*")
    u = sub.add_parser("upstream")
    u.add_argument("--clone", action="append", default=[], metavar="OWNER/REPO=DIR")
    m = sub.add_parser("mark-synced")
    m.add_argument("repo")
    m.add_argument("commit")
    a = ap.parse_args()
    if a.cmd == "check":
        return check(a.skills)
    if a.cmd == "upstream":
        clones = {}
        for item in a.clone:
            repo, _, path = item.partition("=")
            clones[repo] = Path(path).expanduser().resolve()
        return upstream(clones)
    return mark_synced(a.repo, a.commit)


if __name__ == "__main__":
    sys.exit(main())
