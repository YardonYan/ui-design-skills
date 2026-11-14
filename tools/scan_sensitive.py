#!/usr/bin/env python3
"""Scan the public tree for real names and real company names.

GitHub account identifiers inside URLs and copyright lines are public project
attribution and are intentionally kept. See docs/privacy-and-license.md.

Run:  python tools/scan_sensitive.py
Exit 0 when clean, 1 on any hit.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Patterns are assembled from escapes so this file never contains a literal
# sensitive term and therefore does not flag itself during the scan.
PATTERNS = {
    "真实公司名（中文）": re.compile("\u7acb\u6668"),
    "真实公司名（英文）": re.compile("LC\\s?SIGN|LCS" + "ign|lcs" + "ign", re.I),
    "真实姓名": re.compile("\u989c\u5fe0\u6c11"),
}
TEXT_EXT = {
    ".md", ".mdx", ".html", ".htm", ".css", ".scss", ".sass", ".less",
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".json", ".jsonc",
    ".yaml", ".yml", ".txt", ".py", ".svg", ".csv", ".sh", ".bat", ".ps1",
    ".vue", ".xml", ".toml", ".canvas", ".gitignore", ".gitattributes", "",
}


def main() -> int:
    hits: list[str] = []
    scanned = 0
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.suffix.lower() not in TEXT_EXT:
            continue
        try:
            raw = p.read_bytes()
            if b"\x00" in raw[:512]:
                continue
            text = raw.decode("utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        scanned += 1
        for label, pat in PATTERNS.items():
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                hits.append(f"{p.relative_to(ROOT).as_posix()}:{line} [{label}] {m.group(0)!r}")

    print(f"扫描文本文件 {scanned} 个，敏感命中 {len(hits)} 条")
    for h in hits[:40]:
        print("  - " + h)
    if len(hits) > 40:
        print(f"  ... 另有 {len(hits) - 40} 条")
    print("结果：" + ("通过" if not hits else "未通过，禁止推送"))
    return 0 if not hits else 1


if __name__ == "__main__":
    sys.exit(main())
