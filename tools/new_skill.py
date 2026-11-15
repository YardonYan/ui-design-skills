#!/usr/bin/env python3
"""Scaffold a new skill with the repository's conventions.

Usage:
  python tools/new_skill.py --name admin-report --category enterprise \
      --zh "后台报表" --desc "做什么。什么时候用。什么时候别用。"

Creates skills/<category>/<name>/ with SKILL.md, CONTRIBUTORS and an empty
references/ directory, then prints the commands to run next.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATS = ("foundations", "web", "enterprise", "mobile", "components", "tooling")
NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)+$")

SKILL = """---
name: {name}
version: 2.3.0
zh_name: "{zh}"
en_name: "{name}"
description: "{desc}"
category: {category}
scenario: design
tags: []
---

# {zh}

按需加载。由仓库根 `SKILL.md` 判断是否需要，命中后只读本技能 `references/` 里用得到的那几份。

## 目录

| 路径 | 内容 |
|---|---|
| `SKILL.md` | 本文件，入口与边界 |
| `references/` | 规则、模板或语料，按主题拆分 |

## 什么时候别用

写清不适用的情况，避免和相邻技能抢活。

## 许可

本技能属仓库自有内容，Apache-2.0，见根目录 `LICENSE`。
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="生成一个符合本库约定的技能骨架")
    ap.add_argument("--name", required=True, help="小写连字符名称，如 admin-report")
    ap.add_argument("--category", required=True, choices=CATS)
    ap.add_argument("--zh", default="", help="中文名，留空则用名称")
    ap.add_argument("--desc", required=True, help="写清做什么 / 什么时候用 / 什么时候别用")
    a = ap.parse_args()

    if not NAME_RE.match(a.name):
        raise SystemExit("名称需为小写连字符形式，且至少两段，例如 admin-report")
    if len(a.desc.strip()) < 40:
        raise SystemExit("description 至少 40 字，要写清做什么、什么时候用、什么时候别用")

    dest = ROOT / "skills" / a.category / a.name
    if dest.exists():
        raise SystemExit(f"已存在：{dest.relative_to(ROOT)}")

    (dest / "references").mkdir(parents=True)
    (dest / "SKILL.md").write_text(
        SKILL.format(name=a.name, zh=a.zh or a.name, desc=a.desc, category=a.category),
        encoding="utf-8", newline="\n")
    (dest / "CONTRIBUTORS").write_text("仓库自有内容。\n", encoding="utf-8", newline="\n")

    print(f"created {dest.relative_to(ROOT).as_posix()}")
    print("next:")
    print("  python tools/build_index.py    # 重算技能地图清单")
    print("  python tools/lint_skills.py    # 格式与数字一致性校验")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
