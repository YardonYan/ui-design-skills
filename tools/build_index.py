#!/usr/bin/env python3
"""Regenerate docs/skill-map.md's per-category inventory from live SKILL.md files.

The surrounding prose of docs/skill-map.md is kept; only the section between
<!-- INVENTORY:START --> and <!-- INVENTORY:END --> is replaced.

Run:  python tools/build_index.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MAP = ROOT / "docs" / "skill-map.md"
START = "<!-- INVENTORY:START -->"
END = "<!-- INVENTORY:END -->"
CATS = ("foundations", "web", "enterprise", "mobile", "components", "tooling")
ZH = {
    "foundations": "设计基础与验收", "web": "网页端 UI", "enterprise": "企业内部 UI",
    "mobile": "移动端 UI", "components": "组件、区块与素材", "tooling": "工程链路与格式",
}


def desc_of(p: Path) -> str:
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^description:\s*(.+)$", t, re.M | re.S)
    body = ""
    if m:
        body = m.group(1)
        if body.strip() in {">", ">-", "|", "|-"}:
            body = "\n".join(t[m.end():].splitlines()[:6])
    body = re.sub(r"\s+", " ", body).strip().strip("'\"")
    return (body[:96] + "…") if len(body) > 96 else body


def main() -> int:
    blocks = []
    for c in CATS:
        d = SKILLS / c
        names = sorted(p.name for p in d.iterdir() if p.is_dir()) if d.is_dir() else []
        blocks.append(f"### {c} · {ZH[c]}\n\n| 技能 | 说明 |\n|---|---|\n"
                      + "\n".join(f"| `{n}` | {desc_of(d / n / 'SKILL.md')} |" for n in names))
    body = "\n\n".join(blocks)
    text = MAP.read_text(encoding="utf-8")
    new = START + "\n\n" + body + "\n\n" + END
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: new, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n## 按类逐条清单\n\n" + new + "\n"
    MAP.write_text(text, encoding="utf-8", newline="\n")
    print(f"docs/skill-map.md 已重算：{sum(1 for _ in SKILLS.glob('*/*/SKILL.md'))} 个技能")
    return 0


if __name__ == "__main__":
    sys.exit(main())
