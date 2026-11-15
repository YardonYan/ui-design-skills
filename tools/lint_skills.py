#!/usr/bin/env python3
"""Validate the UI skill tree.

Checks: the repository root SKILL.md is a valid router entry; every skill
directory has SKILL.md; frontmatter has name and description; name equals
the directory name; descriptions are long enough to be useful; skill names
are unique across categories.

Run from anywhere:  python tools/lint_skills.py
Exit 0 when clean, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
FIELD = re.compile(r"^([a-zA-Z_-]+):\s*(.*)$", re.M)


def frontmatter(text: str) -> dict[str, str]:
    m = FM.match(text)
    if not m:
        return {}
    lines = m.group(1).splitlines()
    out: dict[str, str] = {}
    i = 0
    while i < len(lines):
        mm = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", lines[i])
        if not mm:
            i += 1
            continue
        key, val = mm.group(1), mm.group(2).strip()
        i += 1
        if val in {">", ">-", ">+", "|", "|-", "|+"}:
            parts = []
            while i < len(lines) and (lines[i][:1].isspace() or not lines[i].strip()):
                parts.append(lines[i].strip())
                i += 1
            val = " ".join(p for p in parts if p)
        out[key] = val
    return out


def main() -> int:
    errors: list[str] = []
    seen: dict[str, str] = {}
    total = 0

    # The repository root is itself a router skill. Validate its entry too,
    # but do not apply the "name equals directory name" rule to it.
    entry = ROOT / "SKILL.md"
    if not entry.exists():
        errors.append("仓库根缺 SKILL.md，整体调用时没有入口")
    else:
        fm = frontmatter(entry.read_text(encoding="utf-8", errors="replace"))
        if not fm:
            errors.append("根 SKILL.md 没有合法的 YAML frontmatter")
        else:
            if not fm.get("name"):
                errors.append("根 SKILL.md 缺 name")
            if len(fm.get("description", "").strip().strip("'\"").strip(">-|")) < 40:
                errors.append("根 SKILL.md 的 description 过短，需写清触发条件与边界")

    # On-demand reference layers must be complete, otherwise the router may
    # point at a file that does not exist.
    res = ROOT / "references" / "resources"
    lic = ROOT / "references" / "licenses"
    for f in [res / "SOURCE.md", res / "INDEX.md", ROOT / "docs" / "resource-routing.md"]:
        if not f.exists():
            errors.append(f"缺按需加载文件：{f.relative_to(ROOT).as_posix()}")
    for n in range(1, 10):
        if not list(res.glob(f"{n:02d}-*.md")):
            errors.append(f"资源索引缺 {n:02d} 类分类文件")
    if not lic.is_dir() or len(list(lic.glob("*"))) < 5:
        errors.append("references/licenses/ 下的整合技能许可文件不完整")

    for cat in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        for d in sorted(p for p in cat.iterdir() if p.is_dir()):
            total += 1
            rel = d.relative_to(ROOT).as_posix()
            f = d / "SKILL.md"
            if not f.exists():
                errors.append(f"{rel}: 缺 SKILL.md")
                continue
            text = f.read_text(encoding="utf-8", errors="replace")
            fm = frontmatter(text)
            if not fm:
                errors.append(f"{rel}: SKILL.md 没有合法的 YAML frontmatter")
                continue
            name = fm.get("name", "")
            desc = fm.get("description", "")
            if not name:
                errors.append(f"{rel}: frontmatter 缺 name")
            elif name != d.name:
                errors.append(f"{rel}: name={name!r} 与目录名不一致")
            if not desc:
                errors.append(f"{rel}: frontmatter 缺 description")
            elif len(desc.strip().strip("'\"").strip(">-|")) < 40:
                errors.append(f"{rel}: description 过短，需写清做什么 / 什么时候用 / 什么时候别用")
            if name in seen:
                errors.append(f"{rel}: 技能名 {name} 与 {seen[name]} 重复")
            else:
                seen[name] = rel

    print(f"技能目录 {total} 个，问题 {len(errors)} 条")
    for e in errors:
        print("  - " + e)
    print("结果：" + ("通过" if not errors else "未通过"))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
