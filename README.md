# UI Design Skills

中文 · [English](README.en.md)

面向 AI 技能场景的界面设计资料库。67 个技能按六类组织，共 4332 份文件，每个技能都是一个标准 `SKILL.md` 目录，AI 助手读到即可按其中的规则工作。

内容覆盖网页端 UI、企业内部 UI、移动端 UI、AI 对话界面，以及支撑它们的组件、图标、配色、交互规范与验收标准。资料来自一个私有技能库、一个公开技能库和若干公开上游项目，收录前已按许可与隐私口径筛选。

## 仓库沿革

这个仓库原名 daily-log，最初用于每日技术记录、代码片段和手写图形。2026 年 11 月 15 日改造为专门的 UI 设计技能库，并改名为 ui-design-skills。

| 项 | 现状 |
|---|---|
| 旧地址 | `github.com/YardonYan/daily-log` 由 GitHub 自动重定向到新地址，旧链接不会失效 |
| 提交历史 | 改造前的提交历史完整保留，未做历史重写，贡献图记录不受影响 |
| 本地工作副本 | 目录名仍是 daily-log，因为每日贡献脚本按这个路径写文件 |
| 日志类提交 | 脚本仍会在 `notes/`、`snippets/`、`assets/` 下产生少量提交，属历史遗留，不是技能内容 |

需要把贡献提交彻底迁到独立仓库时，改的是脚本和定时任务，不是本库内容。详见 `docs/troubleshooting.md`。

## 这个库是什么，不是什么

| 是 | 不是 |
|---|---|
| 给 AI 助手读的指令、规则、模板与素材 | 可安装的 npm 组件库 |
| 按任务类型组织的技能目录 | 按技术栈排列的教程站 |
| 可直接复制进项目的 HTML、TSX、SVG 与配色值 | 设计稿或截图存档 |
| 带来源与许可记录的公开资料 | 任何人的私人知识库全量副本 |

判断口径很简单：产出是网页或界面，进这六类；产出是 Word、PDF、PPT 这类文件，不在本库范围内。

## 快速开始

1. 找技能。先看 `ROUTER.md`，它按你会怎么说排；命中之后看 `docs/skill-map.md`，它按做界面的六段主线排。
2. 装技能。用 `tools/install.mjs` 复制到你正在用的 AI 助手目录，或直接用 `--dir` 指到任意位置。
3. 用技能。把该技能的 `SKILL.md` 交给助手，需要模板与规范时再让它读同目录下的 `references/` 与 `templates/`。

举例：要做一个带工具调用审批的 AI 对话界面，先用 `ai-chat-patterns` 列全状态，再用 `assistant-ui` 落地组件，最后用 `web-design-guidelines` 验收。

## 六类导航

| 类别 | 管什么 | 技能数 | 典型问法 | 代表技能 |
|---|---|---:|---|---|
| `foundations` | 方向、规范、配色、品牌、交互状态、验收 | 15 | 界面一眼 AI 味怎么改、要一套色板、AI 对话要处理哪些状态 | `oil-ui`、`unslop`、`flexoki-palette`、`ai-chat-patterns` |
| `web` | 面向公众的网页与页面类型 | 20 | 做个落地页、定价页、文档站、复刻某个站 | `saas-landing`、`pricing-page`、`docs-page`、`web-clone` |
| `enterprise` | 中后台、表单、信息架构、看板 | 6 | 做整套后台、把字段整理成可校验的 Schema | `enterprise-admin`、`admin-form-schema`、`admin-ia-patterns` |
| `mobile` | App 界面、引导页、多端尺寸 | 3 | 做一屏 App 展示、查五端尺寸规范 | `mobile-app`、`mobile-design-spec` |
| `components` | 组件、区块、图标、插画、图表、AI 对话组件 | 17 | 要动效组件源码、一整套图标、聊天界面组件 | `cult-ui`、`ricoui-blocks`、`icon-system`、`assistant-ui` |
| `tooling` | 调试、转换、画布格式、交付链路 | 6 | 浏览器里调试页面、HTML 转 PDF、读写画布数据 | `chrome-devtools`、`html-to-pdf`、`json-canvas` |

## 内容构成

| 目录 | 内容 | 数量 |
|---|---|---:|
| `skills/` | 67 个技能，按上表六类分 | 67 个技能目录 |
| `references/` | 跨技能共享语料：84 家设计语料、Flexoki 色值、JSON Canvas 规范 | 174 份 |
| `docs/` | 技能地图、隐私与许可、排错 | 3 份 |
| `tools/` | 安装器与三个校验脚本 | 4 份 |

仓库合计 4332 份文件。技能内的 `SKILL.md` 是入口，`SOURCE.md` 与 `CONTRIBUTORS` 记录来源，其余目录放规则、模板与素材。

## 来源分层

| 来源 | 收录内容 | 许可 |
|---|---|---|
| 私有技能库整理稿 | 页面配方、中后台结构、组件、图标、验收规范 | 自有内容 Apache-2.0，第三方逐条署名 |
| `YardonYan/for-my-self-skills` | 单文件 HTML、移动端尺寸、Markdown 修复、转换链路 | Apache-2.0 |
| `assistant-ui/assistant-ui` | AI 对话界面文档、API 声明、组件源码、starter 模板 | MIT |
| `kubai087/kubai-icons` | 图标定义、徽标、构造工具 | MIT，仅收图标部分 |
| `ricocc/ricoui-blocks` | 动效区块组件与设计文档 | MIT |
| `kepano/flexoki`、`obsidianmd/jsoncanvas` | 色值与画布格式规范 | MIT |
| 设计语料 | 84 家产品的 DESIGN.md | MIT |

逐条来源、许可与收录方式见 `THIRD-PARTY.md`。source-available 的技能文档与许可不明的第三方技能不收正文，只留链接。

## 安装

零依赖安装器，Node 18 以上即可，不需要 npm install：

```bash
node tools/install.mjs --list
node tools/install.mjs --skill saas-landing --ai workbuddy
node tools/install.mjs --skill all --ai workbuddy --dry-run
```

| 参数 | 作用 |
|---|---|
| `--list` | 列出全部技能与分类 |
| `--skill <名>` / `--skill all` | 选一个技能或全部 |
| `--ai <id>` / `--ai all` | 装到指定助手，或一次装到全部已配置的助手 |
| `--project` | 装到当前项目的技能目录而不是用户级 |
| `--dir <路径>` | 直接指定目标目录，覆盖 `--ai` 的默认值 |
| `--dry-run` | 只打印将要复制的内容，不写文件 |
| `--force` | 目标已存在时覆盖 |
| `--uninstall` | 移除本库装过的技能 |

安装器在拷贝前会校验每个技能根目录下确有 `SKILL.md`，缺了就整体拒绝，不装半套。

## 使用途径

国内工具排前面，默认可直接用；国外工具通常需要外网环境。

| 助手 | `--ai` 目标 id | 用户级默认目录 |
|---|---|---|
| WorkBuddy | `workbuddy` | `~/.workbuddy/skills/` |
| CodeBuddy | `codebuddy` | `~/.codebuddy/skills/` |
| TRAE 国内版 | `trae-cn` | `~/.trae-cn/skills/` |
| Qoder | `qoder` | `~/.qoder/skills/` |
| Qwen Code | `qwen-code` | `~/.qwen/skills/` |
| OpenClaw | `openclaw` | `~/.openclaw/skills/` |
| Claude Code | `claude` | `~/.claude/skills/` |
| Codex | `codex` | `~/.codex/skills/` |
| Cursor | `cursor` | `~/.cursor/skills/` |

目录是默认值，各家版本可能调整，用 `--dir` 覆盖即可。

作为插件市场来源安装时，把本仓库地址加进各助手的插件市场即可，`.claude-plugin/`、`.codebuddy-plugin/`、`.codex-plugin/`、`.cursor-plugin/` 四套清单已经放在仓库根：

```bash
claude plugin marketplace add YardonYan/ui-design-skills
```

不适用的场景：网页 IDE、云 Shell、在线 Notebook。技能是给 AI 助手读的指令文件，不是可运行应用，这些环境没有加载入口。需要一个能跑的界面时，取技能里的模板落到自己的项目里。

## 技能格式

每个技能目录至少有一份 `SKILL.md`，YAML frontmatter 里 `name` 与 `description` 必填，`name` 必须等于目录名。`description` 要写清三件事：做什么、什么时候用、什么时候别用。其余字段（`category`、`zh_name`、`en_name`、`tags`、`version`、`license`）按需补。

```
skills/<类别>/<技能名>/
  SKILL.md          入口，必填
  SOURCE.md         来源与许可记录
  CONTRIBUTORS      上游署名
  references/       规则、规范、语料
  templates/        可直接改的模板
  assets/           图标、示例、配置
  scripts/          校验与生成脚本
```

`tools/lint_skills.py` 会逐项核对这些约定，改动技能后跑一次。

## 隐私与许可

公开库不出现真实姓名与真实公司名，推送前用 `tools/scan_sensitive.py` 全库扫描。上游作者的公开署名与版权声明按许可义务保留，口径见 `docs/privacy-and-license.md`。

自有内容 Apache-2.0，第三方内容保留各自许可，逐条列在 `THIRD-PARTY.md`，例外见 `NOTICE`。许可核不出来的 34 个技能与 2 个声明了 LICENSE.txt 但缺文件的技能，单列在 `THIRD-PARTY.md` 的许可待核实清单里，不混成一句见上游。

## 维护

```bash
python tools/lint_skills.py       # 技能格式校验
python tools/scan_sensitive.py    # 敏感词扫描
python tools/build_index.py       # 重算技能地图清单
```

数字不手写，清单由脚本从 `SKILL.md` 现场读取生成。改了技能名或分类就重跑一次 `build_index.py`。

## 排错

见 `docs/troubleshooting.md`，条目都来自实际运行输出，没有推测的报错信息。

## 更新记录

| 日期 | 变更 |
|---|---|
| 2026-11-15 | 由每日技术记录仓库改造为 UI 设计技能库，67 个技能按六类重组，旧内容由普通提交删除，历史保留 |
| 2026-11-15 | 补入 assistant-ui 组件库与 AI 对话界面交互规范，技能数 65 增至 67 |
| 2026-11-15 | 仓库改名 ui-design-skills，About 描述、topics 与本页文档按新定位重写 |

## 许可

Apache-2.0，见 `LICENSE`。第三方内容按 `THIRD-PARTY.md` 各自的条款使用。
