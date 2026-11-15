---
name: ui-design-skills
version: 2.3.0
zh_name: "界面设计技能总入口"
en_name: "UI Design Skills Router"
description: "当用户说要做某个产品、页面、界面、图标、配色或前端效果，却没有指明该用哪个技能时，用这个入口按意图自动匹配本仓库里的技能。用户只需要描述想做什么，由你判断该读哪一份 SKILL.md。适用于 Vibe Coding 场景下的一句话需求、产品原型、页面整改与界面验收。也负责在使用者找外部组件库、灵感站、UI 提示词库，或想借外部设计经验提升质感、动效、可访问性时，按 docs/resource-routing.md 按需加载 references 下的索引与快照，默认一律不加载。产出是 Word / PDF / PPT 文件、后端接口、数据分析或纯运维任务时不走这份。关键词：做个产品、做个网页、做个 App、设计图标、前端 UI、界面、找灵感、找组件库、UI 技能、设计质感、vibe coding、自动匹配、不知道用哪个技能。"
category: router
scenario: intent
tags: ["router", "intent", "auto-match", "skills", "vibe-coding", "fallback"]
---

# UI Design Skills 总入口

这是整个仓库的入口，不是某一个具体技能。使用者把仓库交给 AI 之后，AI 先读这份文件，再按意图去读 `skills/` 下该读的那几份 `SKILL.md`。

## 一条硬规则

使用者不需要知道技能名，也不需要先查目录。

不要要求对方报出某个技能名，不要让用户在一堆技能里做选择，不要因为对方没说清楚用哪个技能就停下来。使用者只负责说清楚想做什么产品、给谁用、大概什么样子；选哪个技能是本文件要解决的问题。

同样，默认不加载 `references/resources/` 与 `references/wisdom/` 里的任何文件。只有使用者明确要找外部资源、找灵感，或想借外部设计经验时，才按 `docs/resource-routing.md` 读其中命中的一份。这两层合计三百多份文件，全读会拖慢上下文。

## 四步流程

1. 从描述里抽取意图信号，最多四个维度：产物是什么、载体是什么、处在哪个阶段、有什么约束。字段说明见 `docs/intent-routing.md`。
2. 按 `docs/intent-routing.md` 的映射表落到六类之一，选 1 个主技能，必要时加 1 到 2 个辅助技能。跨类需求按最终产物定主技能，另一类只作参考。
3. 读这些技能的 `SKILL.md`，需要模板与规则时再读同目录的 `references/`、`templates/`。不要一次把 67 个技能全灌进上下文。
4. 交付产物，并用一句话说明匹配了哪几个技能、为什么。不要长篇解释路由过程。

## 常见意图的快捷映射

| 使用者大概会这么说 | 主技能 | 常一起用 |
|---|---|---|
| 我要做个产品官网、落地页、首页 | `saas-landing` | `web-design-guidelines` |
| 我要给 SaaS 做定价页、套餐页 | `pricing-page` | `saas-landing` |
| 我要做个 FAQ 或文档站 | `faq-page`、`docs-page` | `web-design-guidelines` |
| 我要做个管理后台、订单系统、CRM 页面 | `enterprise-admin` | `admin-form-schema`、`admin-ia-patterns` |
| 把字段整理成能校验的表单 | `admin-form-schema` | `enterprise-admin` |
| 我要看数据的看板、仪表盘 | `dashboard` | `live-dashboard` |
| 我要做个 App 界面、手机上的一屏 | `mobile-app` | `mobile-design-spec` |
| 查 iOS、Android、小程序的尺寸 | `mobile-design-spec` | 无 |
| 我要做个 AI 助手、聊天界面、带审批的对话 | `assistant-ui` | `ai-chat-patterns` |
| 列全对话界面要处理的状态 | `ai-chat-patterns` | `assistant-ui` |
| 我要一套图标、几个功能图标 | `icon-system` | `spotkit` |
| 我要插图、空状态图 | `spotkit` | `icon-system` |
| 我要给产品定配色、深浅两套 | `flexoki-palette` | `web-design-guidelines` |
| 这个界面一眼 AI 味，帮我改 | `unslop` | `review-animations` |
| 帮我审一下界面规范和可访问性 | `web-design-guidelines` | `frontend-spec` |
| 把设计图、截图变成代码 | `image-to-code` | `web-clone` |
| 复刻一个站 | `web-clone` | `image-to-code` |
| 出单文件报告、HTML 转 PDF | `html-skill-effectiveness`、`html-to-pdf` | 无 |

完整映射、冲突裁决与兜底路径在 `docs/intent-routing.md`；按人类口语排的索引在 `ROUTER.md`；按做界面六段主线排的地图在 `docs/skill-map.md`。

## 资源层与智慧层

除了 67 个技能，仓库还收了两层参考资料，用来统合外部经验，避免使用者再到处翻别的技能库。两者都按需加载，默认不读。

| 层 | 路径 | 是什么 | 什么时候读 |
|---|---|---|---|
| 资源层 | `references/resources/` | 9 类外部链接索引，37 条 GitHub + 103 条站点 | 找组件库、灵感站、配色工具、UI 提示词库、模板时 |
| 智慧层 | `references/wisdom/` | 5 个上游技能仓库的文本快照，169 份 Markdown | 要提升设计质感、艺术方向、可访问性、动效或提示词写法时 |

判断顺序：使用者要的是产物，就直接走 `skills/` 下的技能，不读这两层；只有出现找、有没有、参考、灵感、别人怎么做、提升质感这类信号才进入。进入后先读该层的 `INDEX.md`，再只读命中的那一份分类文件或一个来源目录，规则见 `docs/resource-routing.md`。

智慧层收的是 `impeccable`、`taste-skill`、`jakubkrehel/skills`、`emilkowalski/skills`、`motion-prompt` 五家的实际技能文本，各带一份统一说明文件，归属集中登记在 `THIRD-PARTY.md`；本库已有的 hallmark、ui-ux-pro-max、frontend-design、emil-design-eng 与 84 家 DESIGN.md 语料不重复收。资源层只是网址索引，不是收录的源码。

## 兜底

| 情况 | 怎么做 |
|---|---|
| 描述太模糊，判断不出产物 | 最多问 2 个澄清问题，只问产物是什么、给谁用；不要连环追问 |
| 完全没命中任何映射 | 先用 `oil-ui` 定方向；网页类接 `saas-landing`，后台类接 `enterprise-admin`，再按反馈收敛 |
| 同时像网页又像后台 | 按最终产物定主技能；管理端走 `enterprise-admin`，营销页走 `saas-landing` |
| 需要多个技能协作 | 顺序是：定方向 → 定结构或状态 → 出稿 → 配素材 → 验收，不要反过来 |
| 使用者给了字段清单 | 只用给出的字段，不臆造资料里没有的字段 |
| 涉及外部服务或联网检索 | 查询词里不带内部系统名与内部实体信息，用抽象描述 |
| 使用者主动点名了某个技能 | 尊重指定，但仍先读该技能的 `SKILL.md` 确认边界 |
| 使用者要找资源或参考 | 按 `docs/resource-routing.md` 只读命中的一份；分不清要网址还是要做法时，问自己这一句即可 |
| 使用者只是问有哪些资源 | 只读 `references/resources/INDEX.md` 给分类概览，不要展开全部链接 |

## 边界

- 本入口只做意图判断与路由，不替代具体技能的规则。落地代码、模板、素材都在被选中的技能目录里。
- 产出是 Word、PDF、PPT 这类文件，或后端接口、数据分析、运维任务时，不在本仓库范围内，直接说明不适用即可。
- 不确定时宁可少选技能，也不要一次加载一堆；选错了按使用者反馈换一个即可。

## 许可

本文件属仓库自有内容，Apache-2.0，见 `LICENSE`。第三方内容按 `THIRD-PARTY.md` 各自条款使用。
