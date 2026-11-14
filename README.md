# UI Design Skills

中文 · [English](README.en.md)

面向 AI 技能场景的界面设计资料库：65 个技能、六类组织、三千多份可直接取用的规范、模板、组件源码与素材。每个技能是一个标准 `SKILL.md` 目录，AI 助手读到即可按其中的规则工作。

内容覆盖企业内部 UI、网页端 UI、移动端 UI，以及支撑它们的组件、图标、配色、验收规范与工程链路。资料来自一个私有技能库、一个公开技能库，以及若干公开上游项目，已按许可与隐私口径筛选。

## 目录

| 目录 | 内容 | 技能数 |
|---|---|---:|
| [`skills/foundations/`](skills/foundations/) | 设计基础与验收 | 14 |
| [`skills/web/`](skills/web/) | 网页端 UI | 20 |
| [`skills/enterprise/`](skills/enterprise/) | 企业内部 UI | 6 |
| [`skills/mobile/`](skills/mobile/) | 移动端 UI | 3 |
| [`skills/components/`](skills/components/) | 组件、区块与素材 | 16 |
| [`skills/tooling/`](skills/tooling/) | 工程链路与格式 | 6 |

| [`references/`](references/) | 跨技能共享语料：84 家设计语料、配色值、画布规范 | 171 份 |
| [`docs/`](docs/) | 技能地图、隐私与许可、排错 | 3 份 |
| [`tools/`](tools/) | 安装器与三个校验脚本 | 4 份 |

选型先看 [`ROUTER.md`](ROUTER.md)（按「你会怎么说」排），命中之后看 [`docs/skill-map.md`](docs/skill-map.md)（按做界面的六段主线排）。

## 安装

零依赖安装器，Node 18 以上即可，不需要 npm install：

```bash
node tools/install.mjs --list
node tools/install.mjs --skill saas-landing --ai workbuddy
node tools/install.mjs --skill all --ai workbuddy --dry-run
```

常用参数：

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

目录是默认值，各家版本可能调整，用 `--dir` 覆盖即可。也可以把整个仓库作为插件市场来源安装；四个插件清单随技能目录一起分发。

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

公开库不出现真实姓名与真实公司名，推送前用 `tools/scan_sensitive.py` 全库扫描。口径见 [`docs/privacy-and-license.md`](docs/privacy-and-license.md)。

自有内容 Apache-2.0，第三方内容保留各自许可，逐条列在 [`THIRD-PARTY.md`](THIRD-PARTY.md)，例外见 [`NOTICE`](NOTICE)。source-available 与许可不明的技能文档不收录正文，只留链接。

## 维护

```bash
python tools/lint_skills.py       # 技能格式校验
python tools/scan_sensitive.py    # 敏感词扫描
python tools/build_index.py       # 重算技能地图清单
```

数字不手写，清单由脚本从 `SKILL.md` 现场读取生成。改了技能名或分类就重跑一次 `build_index.py`。

## 排错

见 [`docs/troubleshooting.md`](docs/troubleshooting.md)，条目都来自实际运行输出。

## 许可

Apache-2.0，见 [`LICENSE`](LICENSE)。第三方内容按 `THIRD-PARTY.md` 各自的条款使用。
