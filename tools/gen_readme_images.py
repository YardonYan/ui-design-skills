#!/usr/bin/env python3
"""Generate all README artwork and real UI screenshots.

Run from anywhere:  python tools/gen_readme_images.py

Produces, under assets/:
  cover.svg                  hero illustration
  badges.svg                 local badge strip (no external CDN)
  category-bar.svg           the six categories and their counts
  flow-choose-skill.svg      "what UI do you want?" decision flow
  skill-anatomy.svg          anatomy of a skill directory
  cover-1280x640.png         PNG cover for social previews
  screenshots/*.png          real renders produced by the skills
  demos/*.html               source of every screenshot, kept for reproducibility

Screenshots are taken with a locally installed Chromium browser (Edge on
Windows, Chrome elsewhere). No third-party Python packages are required.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
DEMOS = ASSETS / "demos"
SHOTS = ASSETS / "screenshots"
SKILLS = ROOT / "skills"

FONT = "'Microsoft YaHei','PingFang SC','Segoe UI',sans-serif"
INK = "#1c1b1a"
PAPER = "#FFFCF0"
MUTED = "#6f6e69"
LINE = "#e3e0d5"
ACCENT = "#c96442"

CATS = [
    ("foundations", "设计基础", 15, "#8a6f4a"),
    ("web", "网页端", 20, "#c96442"),
    ("enterprise", "企业后台", 6, "#4b6b8a"),
    ("mobile", "移动端", 3, "#7a6b9a"),
    ("components", "组件素材", 17, "#3f7d6a"),
    ("tooling", "工程链路", 6, "#8a5a6b"),
]


def write(rel: str, text: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")


def rect(x, y, w, h, fill, stroke=None, rx=0, extra=""):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="1.5"'
    return s + f" {extra}/>"


def txt(x, y, s, size=16, fill=INK, weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>')


# ---------------------------------------------------------------- cover.svg
def cover() -> str:
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640">',
         rect(0, 0, 1280, 640, PAPER)]
    # faint grid
    for gx in range(0, 1281, 40):
        o.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="640" stroke="#efe9d9" stroke-width="1"/>')
    for gy in range(0, 641, 40):
        o.append(f'<line x1="0" y1="{gy}" x2="1280" y2="{gy}" stroke="#efe9d9" stroke-width="1"/>')
    o.append(rect(0, 0, 12, 640, ACCENT))
    o.append(txt(72, 92, "AGENT SKILLS  /  INTERFACE DESIGN", 15, ACCENT, 700))
    o.append(txt(72, 180, "说清产品", 62, INK, 700))
    o.append(txt(72, 252, "自动匹配", 62, INK, 700))
    o.append(txt(72, 306, "AI 按意图挑选技能，不需要你记名字", 22, MUTED))
    o.append(txt(72, 346, "67 个技能  ·  6 类界面  ·  整个仓库作为一个 Skill 调用", 17, MUTED))

    pills = [("说产品", 72), ("自动匹配", 218), ("出界面", 364)]
    for label, x in pills:
        o.append(rect(x, 390, 128, 40, "#ffffff", LINE, 20))
        o.append(txt(x + 64, 416, label, 16, INK, 600, "middle"))
    o.append(txt(72, 500, "装上整个仓库 → 说清产品 → AI 自动匹配技能 → 出界面", 17, INK, 600))
    o.append(txt(72, 534, "网页  /  中后台  /  移动端  /  AI 对话  /  组件  /  验收", 15, MUTED))
    o.append(txt(72, 596, "Apache-2.0  ·  第三方逐条署名  ·  国内工具优先", 14, MUTED))

    # six stacked cards on the right, each with a small glyph
    glyphs = [
        ("设计基础", "foundation", "方向与验收", "#8a6f4a"),
        ("网页端", "browser", "落地页 / 定价页", "#c96442"),
        ("企业后台", "table", "列表 / 表单 / 看板", "#4b6b8a"),
        ("移动端", "phone", "App 单屏 / 引导", "#7a6b9a"),
        ("组件素材", "blocks", "图标 / 区块 / 配色", "#3f7d6a"),
        ("工程链路", "wrench", "调试 / 转换 / 画布", "#8a5a6b"),
    ]
    for i, (name, kind, sub, color) in enumerate(glyphs):
        col, row = i % 2, i // 2
        x = 660 + col * 290
        y = 90 + row * 160
        o.append(rect(x, y, 268, 138, "#ffffff", LINE, 14))
        o.append(rect(x, y, 268, 5, color, rx=2))
        # glyph area
        gx, gy = x + 18, y + 26
        if kind == "browser":
            o.append(rect(gx, gy, 48, 34, "#f4efe4", color, 5))
            o.append(f'<line x1="{gx}" y1="{gy+10}" x2="{gx+48}" y2="{gy+10}" stroke="{color}" stroke-width="1.5"/>')
            o.append(f'<circle cx="{gx+8}" cy="{gy+5}" r="2" fill="{color}"/>')
        elif kind == "table":
            o.append(rect(gx, gy, 48, 34, "#f4efe4", color, 4))
            for k in range(1, 3):
                o.append(f'<line x1="{gx}" y1="{gy+11*k}" x2="{gx+48}" y2="{gy+11*k}" stroke="{color}" stroke-width="1"/>')
            o.append(f'<line x1="{gx+20}" y1="{gy}" x2="{gx+20}" y2="{gy+34}" stroke="{color}" stroke-width="1"/>')
        elif kind == "phone":
            o.append(rect(gx + 14, gy, 22, 36, "#f4efe4", color, 5))
            o.append(f'<line x1="{gx+20}" y1="{gy+5}" x2="{gx+30}" y2="{gy+5}" stroke="{color}" stroke-width="2"/>')
        elif kind == "blocks":
            for k in range(4):
                o.append(rect(gx + (k % 2) * 24, gy + (k // 2) * 17, 20, 14, "#f4efe4", color, 3))
        elif kind == "foundation":
            for k in range(3):
                o.append(rect(gx + k * 16, gy + (2 - k) * 9, 14, 9 + k * 9, "#f4efe4", color, 3))
        else:
            o.append(f'<circle cx="{gx+24}" cy="{gy+17}" r="15" fill="none" stroke="{color}" stroke-width="2"/>')
            o.append(f'<line x1="{gx+24}" y1="{gy+17}" x2="{gx+36}" y2="{gy+29}" stroke="{color}" stroke-width="3"/>')
        o.append(txt(x + 18, y + 94, name, 19, INK, 700))
        o.append(txt(x + 18, y + 120, sub, 13, MUTED))
        o.append(f'<circle cx="{x+242}" cy="{y+28}" r="9" fill="{color}" opacity="0.18"/>')
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- badges.svg
def badges() -> str:
    items = [("v2.3", ACCENT), ("67 SKILLS", "#4b6b8a"),
             ("AGENT SKILLS", "#3f7d6a"), ("APACHE-2.0", "#7a6b9a"),
             ("CN TOOLS FIRST", "#8a6f4a"), ("NO CDN", "#c96442")]
    x = 4
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 40" width="620" height="40">']
    for label, color in items:
        w = 14 + len(label) * 8
        o.append(rect(x, 4, w, 30, color, rx=15))
        o.append(txt(x + w / 2, 24, label, 12, "#ffffff", 700, "middle"))
        x += w + 10
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- tech-stack.svg
def tech_stack() -> str:
    """Coloured pills, four rows from the standard down to the deliverables."""
    rows = [
        ("标准", ["Agent Skills", "SKILL.md"], "#8a6f4a"),
        ("框架", ["React", "TypeScript", "Tailwind CSS", "HTML / CSS"], "#4b6b8a"),
        ("组件", ["shadcn/ui", "Bootstrap", "React Native"], "#3f7d6a"),
        ("工具与产物", ["Node.js", "Python", "SVG", "JSON Canvas"], "#7a6b9a"),
    ]
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 210" width="1200" height="210">',
         rect(0, 0, 1200, 210, PAPER)]
    for i, (label, items, color) in enumerate(rows):
        y = 14 + i * 48
        label_w = len(label) * 16 + 16
        pills = [(it, 20 + len(it) * 9) for it in items]
        total = label_w + 14 + sum(w for _, w in pills) + 10 * len(pills)
        x = (1200 - total) / 2
        o.append(txt(x + label_w, y + 24, label, 15, INK, 600, "end"))
        x += label_w + 14
        for it, w in pills:
            o.append(rect(x, y + 5, w, 32, color, rx=16))
            o.append(txt(x + w / 2, y + 26, it, 13, "#ffffff", 600, "middle"))
            x += w + 10
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- category-bar.svg
def category_bar() -> str:
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 180" width="1200" height="180">',
         rect(0, 0, 1200, 180, PAPER)]
    o.append(txt(20, 34, "67 个技能，按最终产物分成六类", 20, INK, 700))
    for i, (name, zh, n, color) in enumerate(CATS):
        x = 20 + i * 194
        o.append(rect(x, 56, 184, 84, color, rx=10))
        o.append(txt(x + 16, 98, str(n), 30, "#ffffff", 700))
        o.append(txt(x + 16, 124, zh, 15, "#ffffff", 600))
        o.append(txt(x + 8, 162, name, 12, MUTED, 400, "start"))
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- flow.svg
def flow() -> str:
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 430" width="1200" height="430">',
         rect(0, 0, 1200, 430, PAPER)]
    o.append(rect(430, 18, 340, 52, INK, rx=26))
    o.append(txt(600, 51, "你想做哪种 UI？", 21, "#ffffff", 700, "middle"))
    o.append(txt(600, 96, "先说清楚产物是什么，再挑技能", 14, MUTED, 400, "middle"))
    o.append(f'<line x1="600" y1="70" x2="600" y2="122" stroke="{LINE}" stroke-width="2"/>')
    o.append(f'<line x1="100" y1="122" x2="1100" y2="122" stroke="{LINE}" stroke-width="2"/>')

    entries = [
        ("给产品做官网 / 落地页", "web", "saas-landing", "一页讲清价值"),
        ("做管理后台 / 表单 / 看板", "enterprise", "enterprise-admin", "列表详情与校验"),
        ("做 App 界面 / 引导页", "mobile", "mobile-app", "设备样机里的 App"),
        ("做 AI 对话 / 审批卡", "components", "assistant-ui", "对话与工具审批"),
        ("要图标 / 组件 / 配色", "components", "icon-system", "成套图标与色板"),
        ("已有界面想整改 / 验收", "foundations", "unslop", "红笔批改不重写"),
    ]
    col_w = 190
    for i, (ask, cat, skill, note) in enumerate(entries):
        x = 20 + i * 195
        cx = x + col_w / 2
        color = next(c[3] for c in CATS if c[0] == cat)
        o.append(f'<line x1="{cx}" y1="122" x2="{cx}" y2="150" stroke="{LINE}" stroke-width="2"/>')
        o.append(rect(x, 150, col_w, 62, "#ffffff", LINE, 10))
        o.append(txt(cx, 178, ask, 13, INK, 600, "middle"))
        o.append(txt(cx, 199, f"→ {cat}", 11, color, 700, "middle"))
        o.append(f'<line x1="{cx}" y1="212" x2="{cx}" y2="242" stroke="{LINE}" stroke-width="2"/>')
        o.append(rect(x, 242, col_w, 84, color, rx=10))
        o.append(txt(cx, 272, skill, 13, "#ffffff", 700, "middle"))
        o.append(txt(cx, 296, note, 11, "#ffffff", 400, "middle", 'opacity="0.85"'))
        o.append(txt(cx, 348, "复制话术 → 交给助手", 11, MUTED, 400, "middle"))
    o.append(txt(20, 404, "挑不出来就按最终产物归类：产出是界面进这六类，产出是 Word / PDF / PPT 不在本库范围。", 14, MUTED))
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- anatomy.svg
def anatomy() -> str:
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">',
         rect(0, 0, 1200, 300, PAPER)]
    o.append(txt(24, 36, "一个技能就是一个目录，AI 助手先读入口，再按需读其余文件", 19, INK, 700))
    tree = [
        ("skills/web/saas-landing/", "", True),
        ("  SKILL.md", "入口：做什么 / 何时用 / 何时别用", False),
        ("  SOURCE.md", "来源与许可记录", False),
        ("  CONTRIBUTORS", "上游署名", False),
        ("  references/", "规则、规范、语料", False),
        ("  templates/", "可直接改的模板", False),
        ("  assets/", "图标、示例、配置", False),
        ("  scripts/", "校验与生成脚本", False),
    ]
    o.append(rect(24, 58, 520, 220, "#ffffff", LINE, 10))
    for i, (line, note, bold) in enumerate(tree):
        y = 86 + i * 23
        o.append(txt(44, y, line, 14 if bold else 13, INK if bold else "#3d3b37", 700 if bold else 400))
        if note:
            o.append(txt(310, y, note, 12, MUTED))
    o.append(rect(570, 58, 606, 220, "#ffffff", LINE, 10))
    steps = [
        ("1", "你描述需求", "说清产物、场景、风格与不要什么"),
        ("2", "助手命中技能", "按 description 判断该读哪一目录"),
        ("3", "读规则与模板", "只加载需要的文件，不整库灌进上下文"),
        ("4", "产出界面", "HTML / TSX / SVG，可直接落进项目"),
    ]
    for i, (num, title, note) in enumerate(steps):
        y = 88 + i * 48
        o.append(f'<circle cx="600" cy="{y}" r="14" fill="{ACCENT}"/>')
        o.append(txt(600, y + 5, num, 13, "#ffffff", 700, "middle"))
        o.append(txt(628, y + 5, title, 15, INK, 700))
        o.append(txt(760, y + 5, note, 12, MUTED))
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- AI chat demo
CHAT_HTML = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI 对话界面演示 · 工具调用审批</title>
<style>
  :root{--bg:#fafaf9;--fg:#1c1b1a;--muted:#6b6964;--border:#e6e4e0;--accent:#c96442;--surface:#fff;--good:#2f7d4a}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,"Microsoft YaHei",system-ui,sans-serif;display:flex;justify-content:center;padding:28px}
  .app{width:820px;background:var(--surface);border:1px solid var(--border);border-radius:16px;box-shadow:0 12px 40px rgba(28,27,26,.07);overflow:hidden}
  header{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-bottom:1px solid var(--border)}
  .brand{font-weight:700;letter-spacing:-.01em}
  .tag{font-size:12px;color:var(--muted);border:1px solid var(--border);border-radius:999px;padding:4px 10px}
  .thread{padding:22px 24px 8px;min-height:470px}
  .row{display:flex;margin-bottom:18px;gap:10px}
  .row.user{justify-content:flex-end}
  .av{width:28px;height:28px;border-radius:8px;background:var(--bg);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:12px;flex:none}
  .row.user .av{background:var(--fg);color:#fff;border-color:var(--fg)}
  .bubble{max-width:560px;background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:12px 15px}
  .row.user .bubble{background:#f3ece6;border-color:#ead9cc}
  .who{font-size:12px;color:var(--muted);margin-bottom:5px}
  .approval{background:#fffdf7;border:1px solid #e8d7bf;border-radius:12px;padding:14px 16px;margin-top:10px}
  .approval h4{margin:0 0 4px;font-size:14px}
  .approval .scope{font-size:12px;color:var(--muted);margin-bottom:10px}
  .kv{display:flex;gap:8px;font-size:12px;color:var(--muted);border-top:1px dashed var(--border);padding-top:9px;margin-top:9px}
  .kv b{color:var(--fg);font-weight:600}
  .actions{display:flex;gap:8px;margin-top:12px;align-items:center}
  button{font:inherit;font-size:13px;padding:7px 16px;border-radius:8px;cursor:pointer;border:1px solid var(--border);background:#fff}
  button.primary{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}
  .timeout{font-size:11px;color:var(--muted);margin-left:auto}
  .state{display:inline-flex;align-items:center;gap:6px;font-size:11px;color:var(--good);border:1px solid #cfe4d5;background:#f2f9f4;border-radius:999px;padding:3px 9px;margin-top:8px}
  .suggest{display:flex;gap:8px;flex-wrap:wrap;margin:4px 0 18px 38px}
  .chip{font-size:12px;border:1px solid var(--border);border-radius:999px;padding:5px 11px;background:#fff;color:var(--muted)}
  .composer{display:flex;align-items:center;gap:10px;padding:14px 20px;border-top:1px solid var(--border);background:#fcfcfa}
  input{flex:1;font:inherit;padding:10px 14px;border:1px solid var(--border);border-radius:10px;background:#fff}
  .model{font-size:12px;color:var(--muted)}
  .send{background:var(--fg);color:#fff;border-color:var(--fg);font-weight:600}
</style>
</head>
<body>
<div class="app">
  <header><span class="brand">工作台助手</span><span class="tag">模型 · 通用版　|　对话 01</span></header>
  <div class="thread">
    <div class="row user"><div class="bubble"><div class="who">你</div>把上周的订单汇总发给运营组，先让我看一眼再发。</div><div class="av">你</div></div>
    <div class="row"><div class="av">AI</div><div class="bubble">
      <div class="who">助手 · 已生成</div>已整理好上周订单汇总，涉及 3 个字段：时间范围、订单数、金额合计。发送前需要你确认。
      <div class="approval">
        <h4>发送订单汇总到运营组</h4>
        <div class="scope">作用对象：运营组频道　·　影响范围：会向外部频道发送一条消息　·　可撤回：否</div>
        <div class="kv"><span>附件</span><b>weekly-orders.csv</b><span>时间范围</span><b>最近 7 天</b><span>收件方</span><b>运营组</b></div>
        <div class="actions"><button class="primary">批准发送</button><button>拒绝</button><span class="timeout">30 秒未操作则自动取消</span></div>
      </div>
      <span class="state">● 已生成 · 等待审批</span>
    </div></div>
    <div class="suggest"><span class="chip">改成只发金额合计</span><span class="chip">先导出预览</span><span class="chip">换个时间范围</span></div>
  </div>
  <div class="composer"><span class="model">模型 ▾</span><input placeholder="继续描述，或按 Enter 发送"><button class="send">发送</button></div>
</div>
</body>
</html>
"""


# ---------------------------------------------------------------- browser
def browser() -> str:
    env = os.environ.get("README_BROWSER")
    if env and Path(env).exists():
        return env
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "/usr/bin/chromium", "/usr/bin/google-chrome",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return shutil.which("msedge") or shutil.which("chrome") or ""


def shot(exe: str, src: Path, out: Path, width: int, height: int) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    url = src.as_uri()
    cmd = [exe, "--headless", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
           "--virtual-time-budget=3000",
           f"--screenshot={out}", f"--window-size={width},{height}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not out.exists():
        print(f"  [WARN] screenshot failed: {out.name}\n{r.stderr[-400:]}", file=sys.stderr)
    else:
        print(f"  shot {out.name}: {out.stat().st_size // 1024} KB")


def main() -> int:
    ASSETS.mkdir(parents=True, exist_ok=True)
    DEMOS.mkdir(parents=True, exist_ok=True)
    SHOTS.mkdir(parents=True, exist_ok=True)

    write("assets/cover.svg", cover())
    write("assets/badges.svg", badges())
    write("assets/tech-stack.svg", tech_stack())
    write("assets/category-bar.svg", category_bar())
    write("assets/flow-choose-skill.svg", flow())
    write("assets/skill-anatomy.svg", anatomy())
    print("svg artwork written")

    # demo pages: three are the skills' own deliverables, one is authored from
    # the ai-chat-patterns / assistant-ui specs.
    sources = [
        ("skills/web/saas-landing/example.html", "demos/saas-landing.html"),
        ("skills/enterprise/dashboard/example.html", "demos/dashboard.html"),
        ("skills/mobile/mobile-app/example.html", "demos/mobile-app.html"),
    ]
    for src, dst in sources:
        shutil.copy2(ROOT / src, DEMOS / Path(dst).name)
    write("assets/demos/ai-chat.html", CHAT_HTML)
    print("demo html written")

    # temporary wrapper, removed after the shot so the repo stays clean
    render = DEMOS / "_cover-render.html"
    render.write_text(f"""<!doctype html><html><head><meta charset="utf-8">
<style>*{{margin:0;padding:0}}html,body{{width:1280px;height:640px;overflow:hidden}}
img{{display:block;width:1280px;height:640px}}</style></head>
<body><img src="../cover.svg" alt="cover"></body></html>""", encoding="utf-8")

    exe = browser()
    if not exe:
        print("[ERROR] no Chromium browser found; set README_BROWSER to its path", file=sys.stderr)
        return 1
    print(f"browser: {exe}")

    shot(exe, render, ASSETS / "cover-1280x640.png", 1280, 640)
    render.unlink(missing_ok=True)
    shot(exe, DEMOS / "saas-landing.html", SHOTS / "web-landing.png", 1280, 820)
    shot(exe, DEMOS / "dashboard.html", SHOTS / "enterprise-dashboard.png", 1280, 820)
    shot(exe, DEMOS / "mobile-app.html", SHOTS / "mobile-app.png", 820, 940)
    shot(exe, DEMOS / "ai-chat.html", SHOTS / "ai-chat-approval.png", 900, 780)
    return 0


if __name__ == "__main__":
    sys.exit(main())
