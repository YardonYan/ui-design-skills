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
    ("foundations", "设计基础", 20, "#8a6f4a"),
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
    o.append(txt(72, 346, "72 个技能  ·  6 类界面  ·  整个仓库作为一个 Skill 调用", 17, MUTED))

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
    items = [("v2.3", ACCENT), ("72 SKILLS", "#4b6b8a"),
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
    o.append(txt(20, 34, "72 个技能，按最终产物分成六类", 20, INK, 700))
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


# ---------------------------------------------------------------- craft demos
# Four artefacts produced by actually running the integrated skills: a before /
# after pass (design-vocabulary), three art directions (art-direction), an
# accessibility report (a11y-rules) and a motion keyframe strip (motion-craft).

CRAFT_BEFORE_AFTER = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#1c1b1a;
font:14px/1.55 -apple-system,"Microsoft YaHei",system-ui,sans-serif}
.wrap{display:grid;grid-template-columns:1fr 1fr;height:720px}
.pane{padding:40px 44px;position:relative}
.pane.before{background:#fff;border-right:1px solid #e2e2e2}
.pane.after{background:#FFFCF0}
.tag{position:absolute;top:22px;right:26px;font-size:12px;padding:4px 11px;border-radius:999px}
.before .tag{background:#ececec;color:#666}
.after .tag{background:#c96442;color:#fff;font-weight:600}
/* before: flat, cramped, no hierarchy */
.pane.before h3{font-size:16px;margin:28px 0 8px;font-weight:400}
.pane.before p{font-size:13px;color:#7a7a7a;margin:0 0 8px}
.pane.before .card{border:1px solid #ddd;padding:12px;margin:10px 0}
.pane.before .ic{width:18px;height:18px;background:#dcdcdc;display:inline-block;margin-right:8px;vertical-align:-3px}
.pane.before .btn{background:#d9d9d9;color:#555;border:0;padding:7px 12px;font:inherit;font-size:13px;margin-top:6px}
/* after: clear scale, room, one accent, aligned icons */
.pane.after h1{font-size:26px;letter-spacing:-.01em;margin:26px 0 6px}
.pane.after .sub{font-size:14px;color:#6f6e69;margin:0 0 22px}
.pane.after .card{background:#fff;border:1px solid #e8e3d6;border-radius:12px;padding:18px 20px;margin:0 0 14px}
.pane.after .row{display:flex;align-items:center;gap:12px}
.pane.after .ic{width:30px;height:30px;border-radius:8px;background:#f3ece2;display:flex;
align-items:center;justify-content:center;font-size:13px;color:#c96442;font-weight:700;flex:none}
.pane.after .card b{font-size:15px;display:block;margin-bottom:2px}
.pane.after .card span{font-size:13px;color:#6f6e69}
.pane.after .btn{background:#c96442;color:#fff;border:0;border-radius:9px;padding:11px 20px;
font:inherit;font-weight:600;margin-top:10px}
.pane.after .txt{font-size:13px;color:#575653;padding:2px 0}
.note{position:absolute;left:44px;bottom:26px;font-size:12px;color:#8a8781}
</style></head><body><div class="wrap">
<div class="pane before"><span class="tag">改前</span>
<h3>工作台</h3><p>今天的任务和最近的文件都在这里。</p>
<div class="card"><span class="ic"></span>项目周报<span style="float:right">编辑</span></div>
<div class="card"><span class="ic"></span>客户资料<span style="float:right">编辑</span></div>
<div class="card"><span class="ic"></span>会议记录<span style="float:right">编辑</span></div>
<button class="btn">新建文档</button><button class="btn">导入</button>
<div class="note">字阶只有一档，间距 8px，图标与文字无对齐关系，两个按钮权重相同</div>
</div>
<div class="pane after"><span class="tag">用 design-vocabulary 整改后</span>
<h1>工作台</h1><p class="sub">今天的任务和最近的文件，按最近使用排序。</p>
<div class="card"><div class="row"><span class="ic">周</span><div><b>项目周报</b><span>14 分钟前编辑 · 3 位协作者</span></div></div></div>
<div class="card"><div class="row"><span class="ic">客</span><div><b>客户资料</b><span>昨天编辑 · 已归档到销售</span></div></div></div>
<div class="card"><div class="row"><span class="ic">会</span><div><b>会议记录</b><span>3 天前 · 待补充结论</span></div></div></div>
<button class="btn">新建文档</button>
<div class="txt" style="margin-top:14px">字阶 26 / 15 / 13 三档，间距 12 / 14 / 22 三档，只有一个主行动，图标统一 30px 圆角 8</div>
<div class="note">改动集中在层级、间距、单一强调色与图标对齐，结构与文案没动</div>
</div></div></body></html>"""

CRAFT_DIRECTIONS = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#1c1b1a;
font:14px/1.55 -apple-system,"Microsoft YaHei",system-ui,sans-serif}
.head{padding:26px 32px 0}
.head h2{margin:0 0 4px;font-size:19px}
.head p{margin:0;color:#6f6e69;font-size:13px}
.cols{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0;height:452px;margin-top:18px}
.col{padding:30px 28px;position:relative}
.col .name{font-size:12px;letter-spacing:.04em;text-transform:uppercase;margin-bottom:18px}
/* editorial */
.e{background:#fff;border-right:1px solid #e6e4e0;border-top:1px solid #e6e4e0}
.e .name{color:#8a8781}
.e h3{font-family:Georgia,"Songti SC",serif;font-size:30px;line-height:1.2;margin:0 0 12px}
.e p{font-size:13px;color:#4a4844;max-width:26ch;margin:0 0 20px}
.e .btn{background:#1c1b1a;color:#fff;border:0;padding:10px 18px;font:inherit;font-size:13px}
.e .rule{height:1px;background:#1c1b1a;margin:22px 0 12px}
.e .meta{font-size:11px;color:#8a8781;letter-spacing:.06em}
/* warm paper */
.w{background:#F7F1E6;border-top:1px solid #e6dcc8}
.w .name{color:#9a7b52}
.w h3{font-size:26px;margin:0 0 10px;color:#3d3226}
.w p{font-size:13px;color:#6b5f4e;max-width:26ch;margin:0 0 20px}
.w .btn{background:#bc5215;color:#fff;border:0;border-radius:14px;padding:11px 20px;font:inherit;font-size:13px;font-weight:600}
.w .stamp{display:inline-block;margin-top:22px;font-size:11px;color:#9a7b52;border:1px dashed #cdb894;border-radius:8px;padding:6px 10px;transform:rotate(-1.5deg)}
/* technical */
.t{background:#12141a;color:#e8ebf0;border-top:1px solid #12141a}
.t .name{color:#7bf29b}
.t h3{font-family:"Consolas","Courier New",monospace;font-size:24px;margin:0 0 10px;letter-spacing:-.01em}
.t p{font-size:13px;color:#9aa3b2;max-width:26ch;margin:0 0 20px}
.t .btn{background:#7bf29b;color:#0d1015;border:0;padding:10px 18px;font:inherit;font-size:13px;font-weight:700}
.t .grid{position:absolute;inset:0;background-image:linear-gradient(#1d2028 1px,transparent 1px),linear-gradient(90deg,#1d2028 1px,transparent 1px);background-size:28px 28px;opacity:.5;pointer-events:none}
.t > *{position:relative}
</style></head><body>
<div class="head"><h2>同一个产品，三种艺术方向</h2>
<p>用 art-direction 先定视觉语气，再落页面，比直接改稿少一轮返工</p></div>
<div class="cols">
<div class="col e"><div class="name">Editorial · 克制编辑感</div>
<h3>A quieter place to keep what you read.</h3>
<p>长文、脚注、克制的层级。适合内容型产品与文档站。</p>
<button class="btn">开始写</button><div class="rule"></div><div class="meta">SERIF · 单栏 · 无圆角</div></div>
<div class="col w"><div class="name">Warm paper · 温暖纸感</div>
<h3>把今天想到的，先记下来。</h3>
<p>暖纸底、宽松间距、手写批注。适合个人工具与笔记类产品。</p>
<button class="btn">新建一页</button><div class="stamp">今天写了 3 条</div></div>
<div class="col t"><div class="grid"></div><div class="name">Technical · 冷峻科技</div>
<h3>notes --sync --offline</h3>
<p>等宽字、深底、荧光强调。适合开发者工具与 API 产品。</p>
<button class="btn">接入 API</button></div>
</div></body></html>"""

CRAFT_A11Y = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#1c1b1a;
font:14px/1.6 -apple-system,"Microsoft YaHei",system-ui,sans-serif;padding:34px 40px}
h2{margin:0 0 4px;font-size:19px}p.lead{margin:0 0 20px;color:#6f6e69;font-size:13px}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;background:#f6f8fa;border-bottom:1px solid #d8dee4;padding:9px 10px;font-weight:600}
td{border-bottom:1px solid #eaeef2;padding:10px;vertical-align:top}
.lv{display:inline-block;font-size:11px;padding:2px 8px;border-radius:999px;font-weight:600;white-space:nowrap}
.hi{background:#fdecea;color:#a4271c}.mid{background:#fff4e0;color:#8a5a12}
code{background:#f6f8fa;border-radius:5px;padding:1px 5px;font-size:12px}
.foot{margin-top:16px;font-size:12px;color:#6f6e69}
</style></head><body>
<h2>a11y-rules 审查输出（节选五条）</h2>
<p class="lead">对象是左边那个改前版本。只出问题清单与位置，不动手改。</p>
<table>
<tr><th style="width:76px">级别</th><th style="width:210px">问题</th><th style="width:290px">证据</th><th>建议</th></tr>
<tr><td><span class="lv hi">阻断</span></td><td>正文对比度不足</td>
<td>灰字 <code>#7a7a7a</code> 落在白底，实测约 4.2:1，小字号下不达 4.5:1</td>
<td>正文改用 <code>#575653</code>，或把字号提到 16px 以上</td></tr>
<tr><td><span class="lv hi">阻断</span></td><td>可点区域过小</td>
<td>卡片右侧「编辑」可点高度约 18px，低于 24×24 下限</td>
<td>可点区域扩到 44×44，视觉尺寸可以不变</td></tr>
<tr><td><span class="lv mid">重要</span></td><td>焦点不可见</td>
<td>键盘 Tab 到按钮时无可见焦点环，<code>outline</code> 被重置</td>
<td>补 <code>:focus-visible</code> 两像素描边，颜色与底色对比不低于 3:1</td></tr>
<tr><td><span class="lv mid">重要</span></td><td>表单缺少标签</td>
<td>搜索框只有占位符，没有 <code>label</code> 或 <code>aria-label</code></td>
<td>加可读标签；占位符不能当标签用</td></tr>
<tr><td><span class="lv mid">重要</span></td><td>动效未降级</td>
<td>入场动画没有 <code>prefers-reduced-motion</code> 分支</td>
<td>在该媒体查询下取消位移与缩放，只保留透明度变化</td></tr>
</table>
<div class="foot">判定依据：WCAG 2.5.8 目标尺寸、1.4.3 对比度、2.4.7 焦点可见、3.3.2 标签、2.3.3 动效。</div>
</body></html>"""

CRAFT_MOTION = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#1c1b1a;
font:14px/1.55 -apple-system,"Microsoft YaHei",system-ui,sans-serif;padding:30px 36px}
h2{margin:0 0 4px;font-size:19px}p.lead{margin:0 0 22px;color:#6f6e69;font-size:13px}
.frames{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.frame{background:#fafaf9;border:1px solid #e6e4e0;border-radius:12px;height:250px;
display:flex;align-items:center;justify-content:center;position:relative}
.stage{width:170px;height:88px;background:#fff;border:1px solid #e8e3d6;border-radius:12px;
display:flex;align-items:center;gap:10px;padding:14px 16px}
.stage .ic{width:30px;height:30px;border-radius:8px;background:#f3ece2;color:#c96442;
font-weight:700;display:flex;align-items:center;justify-content:center;font-size:13px;flex:none}
.stage b{font-size:14px;display:block}.stage span{font-size:12px;color:#6f6e69}
.f1 .stage{box-shadow:0 2px 6px rgba(28,27,26,.08);transform:translateY(0)}
.f2 .stage{box-shadow:0 14px 30px rgba(28,27,26,.16);transform:translateY(-10px) scale(1.02)}
.f3 .stage{box-shadow:0 6px 14px rgba(28,27,26,.10);transform:translateY(-3px)}
.ms{position:absolute;top:12px;left:14px;font-size:11px;color:#8a8781;letter-spacing:.04em}
.curve{margin-top:20px;font-size:12px;color:#575653}
.curve code{background:#f6f8fa;border-radius:5px;padding:2px 6px}
</style></head><body>
<h2>motion-craft 的动效配方：卡片抬起</h2>
<p class="lead">同一个交互的三帧。位移与阴影同时变化，结束前回落到静止位附近，避免悬停时抖动。</p>
<div class="frames">
<div class="frame f1"><span class="ms">0 ms · 静止</span>
<div class="stage"><span class="ic">周</span><div><b>项目周报</b><span>14 分钟前编辑</span></div></div></div>
<div class="frame f2"><span class="ms">120 ms · 抬起</span>
<div class="stage"><span class="ic">周</span><div><b>项目周报</b><span>14 分钟前编辑</span></div></div></div>
<div class="frame f3"><span class="ms">240 ms · 定格</span>
<div class="stage"><span class="ic">周</span><div><b>项目周报</b><span>14 分钟前编辑</span></div></div></div>
</div>
<div class="curve">位移 0 → -10px → -3px，阴影 2px → 14px → 6px，缓动 <code>cubic-bezier(0.22, 1, 0.36, 1)</code>，总时长 240ms。减少动效时只保留阴影变化。</div>
</body></html>"""


def craft_demos() -> None:
    write("assets/demos/craft-before-after.html", CRAFT_BEFORE_AFTER)
    write("assets/demos/craft-directions.html", CRAFT_DIRECTIONS)
    write("assets/demos/craft-a11y.html", CRAFT_A11Y)
    write("assets/demos/craft-motion.html", CRAFT_MOTION)



CRAFT_GIF_HTML = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><style>
*{box-sizing:border-box}html,body{margin:0;height:100%}
body{display:flex;align-items:center;justify-content:center;
font-family:-apple-system,"Microsoft YaHei",system-ui,sans-serif;color:#1c1b1a}
.stage{width:880px;padding:40px 46px}
h1{margin:0 0 8px;font-weight:700;letter-spacing:-.01em}
p.sub{margin:0}
.card{border-style:solid;display:flex;align-items:center}
.ic{display:flex;align-items:center;justify-content:center;font-weight:700;flex:none}
.card b{display:block}
.card span.d{display:block}
#btn{font:inherit;border:0;cursor:default}
.bar{margin-top:28px;background:#e9e4d8;border-radius:999px;height:6px;overflow:hidden}
.bar i{display:block;height:100%;background:#c96442;border-radius:999px}
.meta{margin-top:10px;font-size:12px;color:#8a8781;display:flex;justify-content:space-between}
</style></head><body>
<div class="stage" id="stage">
  <h1 id="title">工作台</h1>
  <p class="sub" id="sub">今天的任务和最近的文件，按最近使用排序。</p>
  <div class="card" id="c1"><span class="ic" id="i1">周</span><div><b>项目周报</b><span class="d">14 分钟前编辑 · 3 位协作者</span></div></div>
  <div class="card" id="c2"><span class="ic" id="i2">客</span><div><b>客户资料</b><span class="d">昨天编辑 · 已归档到销售</span></div></div>
  <div class="card" id="c3"><span class="ic" id="i3">会</span><div><b>会议记录</b><span class="d">3 天前 · 待补充结论</span></div></div>
  <button id="btn">新建文档</button>
  <div class="bar"><i id="fill"></i></div>
  <div class="meta"><span>按 design-vocabulary 逐维整改</span><span id="pct">0%</span></div>
</div>
<script>
const t = Math.max(0, Math.min(1, parseFloat(new URLSearchParams(location.search).get('t') || '0')));
const L = (a, b) => a + (b - a) * t;
const hex = h => [parseInt(h.slice(1,3),16), parseInt(h.slice(3,5),16), parseInt(h.slice(5,7),16)];
const mix = (a, b) => {
  const A = hex(a), B = hex(b);
  const c = A.map((v,i)=>Math.round(v + (B[i]-v)*t));
  return `rgb(${c[0]},${c[1]},${c[2]})`;
};
const el = id => document.getElementById(id);
document.body.style.background = mix('#ffffff', '#FFFCF0');
el('title').style.fontSize = L(15, 26) + 'px';
el('sub').style.fontSize = L(13, 14) + 'px';
el('sub').style.color = mix('#7a7a7a', '#6f6e69');
el('sub').style.marginBottom = L(8, 22) + 'px';
['c1','c2','c3'].forEach((id, i) => {
  const c = el(id);
  c.style.margin = L(6, 14) + 'px 0';
  c.style.padding = `${L(10, 18)}px ${L(12, 20)}px`;
  c.style.borderRadius = L(0, 12) + 'px';
  c.style.borderWidth = '1px';
  c.style.borderColor = mix('#dddddd', '#e8e3d6');
  c.style.background = mix('#ffffff', '#ffffff');
  c.style.boxShadow = t > 0.02 ? `0 ${L(0,2)}px ${L(0,6)}px rgba(28,27,26,${L(0,0.05)})` : 'none';
  const ic = el('i' + (i + 1));
  ic.style.width = ic.style.height = L(18, 30) + 'px';
  ic.style.borderRadius = L(0, 8) + 'px';
  ic.style.background = mix('#dcdcdc', '#f3ece2');
  ic.style.color = mix('#7a7a7a', '#c96442');
  ic.style.fontSize = L(11, 13) + 'px';
  ic.style.marginRight = L(8, 12) + 'px';
  c.querySelector('b').style.fontSize = L(13, 15) + 'px';
  const d = c.querySelector('.d');
  d.style.fontSize = L(12, 13) + 'px';
  d.style.color = mix('#8a8a8a', '#6f6e69');
  d.style.marginTop = L(0, 2) + 'px';
});
const btn = el('btn');
btn.style.background = mix('#d9d9d9', '#c96442');
btn.style.color = mix('#555555', '#ffffff');
btn.style.borderRadius = L(0, 9) + 'px';
btn.style.padding = `${L(7, 11)}px ${L(12, 20)}px`;
btn.style.fontSize = L(13, 14) + 'px';
btn.style.fontWeight = L(400, 600);
btn.style.marginTop = L(6, 10) + 'px';
el('fill').style.width = (t * 100).toFixed(0) + '%';
el('pct').textContent = Math.round(t * 100) + '%';
</script></body></html>"""


def craft_rework_gif() -> None:
    """Render the rework as a GIF: t steps from 0 to 1, one frame per step."""
    import tempfile

    magick = shutil.which("magick") or r"C://Program Files//ImageMagick-7.1.2-Q16-HDRI//magick.exe"
    if not (magick and Path(magick).exists()):
        print("  [skip] craft-rework.gif: ImageMagick not found")
        return
    exe = browser()
    if not exe:
        return
    tmp = Path(tempfile.mkdtemp(prefix="rework-"))
    page = tmp / "rework.html"
    page.write_text(CRAFT_GIF_HTML, encoding="utf-8", newline="\n")
    frames = []
    n = 12
    for i in range(n):
        step = i / (n - 1)
        out = tmp / f"f{i:02d}.png"
        subprocess.run(
            [exe, "--headless", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
             "--virtual-time-budget=1200", f"--screenshot={out}", "--window-size=900,620",
             page.as_uri() + f"?t={step:.3f}"],
            capture_output=True, timeout=120)
        frames.append(str(out))
    gif = SHOTS / "craft-rework.gif"
    cmd = [magick, "-delay", "11", "-loop", "0"] + frames[:-1] + \
          ["-delay", "140", frames[-1]] + \
          ["-resize", "860x", "-colors", "256", "-dither", "None",
           "-layers", "Optimize", str(gif)]
    subprocess.run(cmd, capture_output=True, timeout=300)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"  gif craft-rework.gif: {gif.stat().st_size // 1024 if gif.exists() else 0} KB")


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
    craft_demos()
    craft_rework_gif()
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
    shot(exe, DEMOS / "craft-before-after.html", SHOTS / "craft-before-after.png", 1280, 720)
    shot(exe, DEMOS / "craft-directions.html", SHOTS / "craft-directions.png", 1280, 560)
    shot(exe, DEMOS / "craft-a11y.html", SHOTS / "craft-a11y.png", 1280, 520)
    shot(exe, DEMOS / "craft-motion.html", SHOTS / "craft-motion.png", 1280, 430)
    return 0


if __name__ == "__main__":
    sys.exit(main())
