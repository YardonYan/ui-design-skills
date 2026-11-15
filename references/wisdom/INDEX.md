# 外部智慧 · 总览

默认不加载。这里收的是五个来源的设计技能文本，由仓库根 `SKILL.md` 按意图判断是否读取；命中后只读其中一个来源目录里用得到的那几份文件。

| 来源 | 许可 | 文本数 | 入口 | 什么时候读 |
|---|---|---:|---|---|
| `impeccable` | Apache-2.0 | 51 | [`SKILL.md`](impeccable/SKILL.md) | 提升界面质感、给设计下准确指令、按间距配色字体动效逐维整改时 |
| `taste-skill` | MIT | 28 | [`SKILL.md`](taste-skill/SKILL.md) | 先定艺术方向、拆解参考图语言、做有性格的视觉稿时 |
| `jakubkrehel` | MIT | 52 | [`better-accessibility/SKILL.md`](jakubkrehel/better-accessibility/SKILL.md) | 逐条核对可访问性、表单、焦点、触控热区、颜色对比度时 |
| `emilkowalski` | MIT | 31 | [`animate/SKILL.md`](emilkowalski/animate/SKILL.md) | 做动效、动画性能、苹果风格界面与组件细节打磨时 |
| `motion-prompt` | MIT | 7 | [`FORMAT.md`](motion-prompt/FORMAT.md) | 把动效需求写成可复用提示词、给动效定格式时 |

合计 5 个来源、169 份 Markdown。归属与许可统一登记在根目录 `THIRD-PARTY.md`。

## 加载规则

1. 先判断意图属于哪一列，只进入对应的一个来源目录。
2. 先读该目录的说明文件确认范围，再读用得到的 `SKILL.md` 或规则文件。
3. 一次最多读三份文件；不要把整个目录或五个来源全灌进上下文。
4. 这些是参考语料，不是可安装技能。要产出界面时仍由 `skills/` 下的技能负责。
5. 使用者没提质感、动效、可访问性、艺术方向这类诉求时，不加载本目录。

## 与本地 67 个技能的关系

本库已有的整改、设计智能、前端设计、设计工程与品牌语料不重复收。这里补的是设计词汇、艺术方向、可访问性细则、动效技能与提示词写法，作为按需查阅的第二层。

## 维护

各来源目录的说明文件与本文件保持同一套格式。索引由 `tools/build_resource_index.py` 生成，不要手改。
