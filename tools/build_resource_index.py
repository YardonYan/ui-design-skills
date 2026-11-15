#!/usr/bin/env python3
"""Generate the resource and wisdom indexes from local sources.

Run from anywhere:  python tools/build_resource_index.py

Truth sources:
  references/resources/SOURCE.md   the original 9-class link collection
  references/wisdom/*/SOURCE.md    provenance of each upstream skill repo

Generated (do not hand-edit):
  references/resources/INDEX.md
  references/resources/0X-*.md
  references/wisdom/INDEX.md

The point of splitting is progressive disclosure: the router reads one short
INDEX and then loads only the one file that matches the user's intent.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "references" / "resources"
WIS = ROOT / "references" / "wisdom"
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

WISDOM = [
    ("impeccable", "pbakaus/impeccable", "Apache-2.0", "SKILL.md",
     "提升界面质感、给设计下准确指令、按间距配色字体动效逐维整改时"),
    ("taste-skill", "Leonxlnx/taste-skill", "MIT", "SKILL.md",
     "先定艺术方向、拆解参考图语言、做有性格的视觉稿时"),
    ("jakubkrehel", "jakubkrehel/skills", "MIT", "better-accessibility/SKILL.md",
     "逐条核对可访问性、表单、焦点、触控热区、颜色对比度时"),
    ("emilkowalski", "emilkowalski/skills", "MIT", "animate/SKILL.md",
     "做动效、动画性能、苹果风格界面与组件细节打磨时"),
    ("motion-prompt", "showheyohtaki/motion-prompt", "MIT", "FORMAT.md",
     "把动效需求写成可复用提示词、给动效定格式时"),
]


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")


def parse_source() -> tuple[dict[str, list[str]], dict[str, list[tuple[str, str]]]]:
    """Return {cat: [github urls]} and {cat: [(name, urls)]}."""
    text = SRC.read_text(encoding="utf-8")
    blocks = re.findall(r"```\n(.*?)```", text, re.S)
    if len(blocks) < 2:
        raise SystemExit("SOURCE.md: expected two fenced code blocks")

    gh: dict[str, list[str]] = {}
    sites: dict[str, list[tuple[str, str]]] = {}

    cur = ""
    for line in blocks[0].splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            cur = s[2:].split("-")[0].strip()
            continue
        if s.startswith("http") and cur:
            gh.setdefault(cur, []).append(s)

    cur = ""
    for line in blocks[1].splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            cur = s[2:].split("-")[0].strip()
            continue
        if " :: " in s and cur:
            name, urls = s.split(" :: ", 1)
            sites.setdefault(cur, []).append((name.strip(), urls.strip()))
    return gh, sites


def resource_files(gh, sites) -> list[tuple[str, str, str, int, int]]:
    out = []
    for num, slug, zh, when in CATS:
        g = gh.get(num, [])
        s = sites.get(num, [])
        body = [f"# {num} {zh}", "",
                "按需加载文件。只有意图命中本类时才读，默认不加载。", "",
                "| 项 | 值 |", "|---|---|",
                f"| GitHub 链接 | {len(g)} 条 |",
                f"| 其余站点 | {len(s)} 条 |",
                "| 真相源 | [SOURCE.md](SOURCE.md) |",
                "| 生成脚本 | `tools/build_resource_index.py` |", "",
                "## 什么时候读", "", when + "。读完只取用得上的条目，不要把整份清单塞进回答。", ""]

        if g:
            body += ["## GitHub 仓库", "", "```text"]
            body += g
            body += ["```", ""]
        else:
            body += ["## GitHub 仓库", "", "本类没有 GitHub 链接。", ""]

        if s:
            body += ["## 其余站点", "", "| 名称 | 原始链接 |", "|---|---|"]
            for name, urls in s:
                links = " ; ".join(f"`{u.strip()}`" for u in urls.split(";"))
                body.append(f"| {name} | {links} |")
            body.append("")
        else:
            body += ["## 其余站点", "", "本类没有其余网址条目。", ""]

        body += ["## 口径", "",
                 "链接按收集时的原文保留，未核验时效，也未统一改写成 HTTPS。带两个地址的是同一资源的主链接与第二地址，两者都保留。",
                 "",
                 "这些是外部资源索引，不是本库收录的源码或技能。内容、可用性与许可均以原站点为准，本库不替上游作授权解释。",
                 "",
                 "本文件由脚本生成，改链接请改 [SOURCE.md](SOURCE.md) 后重跑脚本。", ""]
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
    lines += ["", f"合计 {total_g} 条 GitHub 链接、{total_s} 条其余网址，分在 {len(rows)} 个文件里。",
              "", "## 加载规则", "",
              "1. 判断意图属于哪一类，一次最多读两份 `0X-*.md`，不要全读。",
              "2. 只在需要具体网址时读；要的是产物（页面、图标、配色）就走 `skills/` 下的技能，不读这里。",
              "3. 回答里只列与需求直接相关的条目，不要复述整份清单。",
              "4. 使用者没问资源时，不加载本目录任何文件。", "",
              "## 口径", "",
              "真相源是 [SOURCE.md](SOURCE.md)，所有 `0X-*.md` 与本文件由 `tools/build_resource_index.py` 生成，不要手工编辑生成物。",
              "链接按原文保留，未核验时效。外链资源不属于本库收录内容，许可以原站点为准。", ""]
    write(RES / "INDEX.md", "\n".join(lines))
    print(f"resources: {len(rows)} files, {total_g} github + {total_s} sites")


def wisdom_index() -> None:
    lines = ["# 外部智慧 · 总览", "",
             "默认不加载。这里收的是五个上游技能仓库的文本内容，由仓库根 `SKILL.md` 按意图判断是否读取；命中后只读其中一个来源目录里用得到的那几份文件。", "",
             "| 来源 | 上游 | 许可 | 文本数 | 入口 | 什么时候读 |", "|---|---|---|---:|---|---|"]
    total = 0
    for name, repo, lic, entry, when in WISDOM:
        d = WIS / name
        n = len([p for p in d.rglob("*.md") if p.name != "SOURCE.md"]) if d.is_dir() else 0
        total += n
        lines.append(f"| `{name}` | [{repo}](https://github.com/{repo}) | {lic} | {n} | [`{entry}`]({name}/{entry}) | {when} |")
    lines += ["", f"合计 {len(WISDOM)} 个来源、{total} 份 Markdown，每个目录都带 LICENSE 与 SOURCE.md。", "",
              "## 加载规则", "",
              "1. 先判断意图属于哪一列，只进入对应的一个来源目录。",
              "2. 先读该目录的 `SOURCE.md` 确认范围与许可，再读用得到的 `SKILL.md` 或规则文件。",
              "3. 一次最多读三份文件；不要把整个目录或五个来源全灌进上下文。",
              "4. 这些是参考语料，不是可安装技能。要产出界面时仍由 `skills/` 下的技能负责。",
              "5. 使用者没提质感、动效、可访问性、艺术方向这类诉求时，不加载本目录。", "",
              "## 与本地 67 个技能的关系", "",
              "本库已收 `hallmark`、`ui-ux-pro-max`、`frontend-design`、`emil-design-eng` 与 84 家 DESIGN.md 语料，本目录不重复收这些上游。这里补的是尚未收录的设计词汇、艺术方向、可访问性细则、动效技能与提示词写法，作为按需查阅的第二层。", "",
              "## 口径", "",
              "内容按上游原文收录，未改写，是 2026-11-15 的快照。上游更新时按各目录 `SOURCE.md` 里的地址自行核对。",
              "本文件由 `tools/build_resource_index.py` 生成，不要手工编辑。", ""]
    write(WIS / "INDEX.md", "\n".join(lines))
    print(f"wisdom: {len(WISDOM)} sources, {total} md")


def main() -> int:
    if not SRC.exists():
        raise SystemExit(f"missing truth source: {SRC}")
    gh, sites = parse_source()
    rows = resource_files(gh, sites)
    resource_index(rows)
    wisdom_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
