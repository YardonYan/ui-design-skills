#!/usr/bin/env python3
"""Generate the resource index from its local truth source.

Run from anywhere:  python tools/build_resource_index.py

Truth source:
  references/resources/SOURCE.md   the 9-class link collection

Generated (do not hand-edit):
  references/resources/INDEX.md
  references/resources/0X-*.md

The point of splitting is progressive disclosure: the router reads one short
INDEX and then loads only the one file that matches the user's intent.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "references" / "resources"
SRC = RES / "SOURCE.md"

CATS = [
    ("01", "components", "组件与前端开发",
     "要找现成组件库、前端 UI Kit、DESIGN.md 规范站点时"),
    ("02", "inspiration", "设计灵感与参考",
     "要找设计灵感、参考截图、配色、字体、页脚与导航范例时"),
    ("03", "motion", "动效与视觉素材",
     "要找动效参考、着色器、背景、插画与视觉素材时"),
    ("04", "ai-tools", "AI工具与效率服务",
     "要找前端审美 Skill、UI 提示词库、AI 设计工具与技能市场时"),
    ("05", "templates", "模板与落地页",
     "要找落地页模板、整页区块与现成 section 时"),
    ("06", "growth", "AI商业化与增长工具",
     "需要参考开源 SaaS 与增长类产品的界面时，与 UI 技能本身无直接关系"),
    ("07", "methods", "方法笔记",
     "要查方法类笔记时，本类无外部链接"),
    ("08", "cross-refs", "跨类引用视图",
     "要看收集箱自己的跨类视图时，链接与其他类重复，不重复列出"),
    ("09", "open-source", "开源软件平替",
     "要参考开源产品源码时，属于产品而非 UI 技能"),
]



def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")


def parse_source() -> tuple[dict[str, list[str]], dict[str, list[tuple[str, str]]]]:
    """Parse the structured tables in SOURCE.md.

    {cat: [repo urls]} and {cat: [(name, urls)]}. The truth source uses the
    same table style as the rest of the repository, not fenced code blocks.
    """
    text = SRC.read_text(encoding="utf-8")
    gh: dict[str, list[str]] = {}
    sites: dict[str, list[tuple[str, str]]] = {}
    cur = ""
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            m = re.match(r"## (\d{2})\s", s)
            cur = m.group(1) if m else ""
            continue
        if not cur or not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != 3:
            continue
        kind, name, links = cells
        if kind == "仓库" and links.startswith("http"):
            gh.setdefault(cur, []).append(links)
        elif kind == "站点" and links.startswith("http"):
            sites.setdefault(cur, []).append((name, links))
    return gh, sites


def resource_files(gh, sites) -> list[tuple[str, str, str, int, int]]:
    out = []
    for num, slug, zh, when in CATS:
        g = gh.get(num, [])
        s = sites.get(num, [])
        body = [f"# {num} {zh}", "",
                "按需加载，默认不读。命中本类时只读这一份。", "",
                "| 项 | 值 |", "|---|---|",
                f"| 仓库 | {len(g)} 条 |",
                f"| 站点 | {len(s)} 条 |",
                f"| 什么时候读 | {when} |", ""]

        if g:
            body += ["## 仓库", "", "```text"]
            body += g
            body += ["```", ""]
        else:
            body += ["## 仓库", "", "本类没有仓库条目。", ""]

        if s:
            body += ["## 站点", "", "| 名称 | 链接 |", "|---|---|"]
            for name, urls in s:
                links = " ; ".join(f"`{u.strip()}`" for u in urls.split(";"))
                body.append(f"| {name} | {links} |")
            body.append("")
        else:
            body += ["## 站点", "", "本类没有站点条目。", ""]

        body += ["## 约定", "",
                 "按需取用，不要整份复述。带两个地址的是同一资源的主链接与第二地址。",
                 "改链接请改真相源 [SOURCE.md](SOURCE.md) 后重跑脚本。", ""]
        write(RES / f"{num}-{slug}.md", "\n".join(body))
        out.append((num, slug, zh, len(g), len(s)))
    return out


def resource_index(rows) -> None:
    lines = ["# 资源索引 · 总览", "",
             "默认不加载。只有意图是找外部资源、找灵感、找现成组件、找工具时才读本文件，并只加载命中的那一份 `0X-*.md`。", "",
             "| 类别 | 文件 | GitHub | 站点 | 什么时候读 |", "|---|---|---:|---:|---|"]
    for (num, slug, zh, ng, ns), (_, _, _, when) in zip(rows, CATS):
        lines.append(f"| {num} {zh} | [`{num}-{slug}.md`]({num}-{slug}.md) | {ng} | {ns} | {when} |")
    total_g = sum(r[3] for r in rows)
    total_s = sum(r[4] for r in rows)
    lines += ["", f"合计 {total_g} 条仓库链接、{total_s} 条站点，分在 {len(rows)} 个文件里。",
              "", "## 加载规则", "",
              "1. 判断意图属于哪一类，一次最多读两份 `0X-*.md`，不要全读。",
              "2. 只在需要具体网址时读；要的是产物（页面、图标、配色）就走 `skills/` 下的技能，不读这里。",
              "3. 回答里只列与需求直接相关的条目，不要复述整份清单。",
              "4. 使用者没问资源时，不加载本目录任何文件。", "",
              "## 维护", "",
              "真相源是 [SOURCE.md](SOURCE.md)，分类文件与本文件由 `tools/build_resource_index.py` 生成，不要手改。",
              "要产物走技能，要网址才读这里，两者不要混在一次加载里。", ""]
    write(RES / "INDEX.md", "\n".join(lines))
    print(f"resources: {len(rows)} files, {total_g} github + {total_s} sites")



def main() -> int:
    if not SRC.exists():
        raise SystemExit(f"missing truth source: {SRC}")
    gh, sites = parse_source()
    rows = resource_files(gh, sites)
    resource_index(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
