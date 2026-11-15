# 外部智慧 · 总览

默认不加载。这里收的是五个上游技能仓库的文本内容，由仓库根 `SKILL.md` 按意图判断是否读取；命中后只读其中一个来源目录里用得到的那几份文件。

| 来源 | 上游 | 许可 | 文本数 | 入口 | 什么时候读 |
|---|---|---|---:|---|---|
| `impeccable` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 | 51 | [`SKILL.md`](impeccable/SKILL.md) | 提升界面质感、给设计下准确指令、按间距配色字体动效逐维整改时 |
| `taste-skill` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT | 28 | [`SKILL.md`](taste-skill/SKILL.md) | 先定艺术方向、拆解参考图语言、做有性格的视觉稿时 |
| `jakubkrehel` | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | MIT | 52 | [`better-accessibility/SKILL.md`](jakubkrehel/better-accessibility/SKILL.md) | 逐条核对可访问性、表单、焦点、触控热区、颜色对比度时 |
| `emilkowalski` | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT | 31 | [`animate/SKILL.md`](emilkowalski/animate/SKILL.md) | 做动效、动画性能、苹果风格界面与组件细节打磨时 |
| `motion-prompt` | [showheyohtaki/motion-prompt](https://github.com/showheyohtaki/motion-prompt) | MIT | 7 | [`FORMAT.md`](motion-prompt/FORMAT.md) | 把动效需求写成可复用提示词、给动效定格式时 |

合计 5 个来源、169 份 Markdown，每个目录都带 LICENSE 与 SOURCE.md。

## 加载规则

1. 先判断意图属于哪一列，只进入对应的一个来源目录。
2. 先读该目录的 `SOURCE.md` 确认范围与许可，再读用得到的 `SKILL.md` 或规则文件。
3. 一次最多读三份文件；不要把整个目录或五个来源全灌进上下文。
4. 这些是参考语料，不是可安装技能。要产出界面时仍由 `skills/` 下的技能负责。
5. 使用者没提质感、动效、可访问性、艺术方向这类诉求时，不加载本目录。

## 与本地 67 个技能的关系

本库已收 `hallmark`、`ui-ux-pro-max`、`frontend-design`、`emil-design-eng` 与 84 家 DESIGN.md 语料，本目录不重复收这些上游。这里补的是尚未收录的设计词汇、艺术方向、可访问性细则、动效技能与提示词写法，作为按需查阅的第二层。

## 口径

内容按上游原文收录，未改写，是 2026-11-15 的快照。上游更新时按各目录 `SOURCE.md` 里的地址自行核对。
本文件由 `tools/build_resource_index.py` 生成，不要手工编辑。
