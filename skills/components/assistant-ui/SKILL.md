---
name: assistant-ui
version: 1.0.0
zh_name: "AI 对话界面组件库"
en_name: "AI Chat UI Primitives"
description: "用 assistant-ui 搭生产级 AI 对话界面：运行时与组件分层、Thread / Composer / Message / Attachment 等原语、128 个成品界面元素、工具调用与生成式界面、以及可直接起项目的模板。当要在 React 应用里做聊天界面、要给已有产品补 AI 助手面板、要做审批卡片与工具调用展示、或要接流式输出与多模型后端时用。产出是组件组合方式、状态接线与可复制的 tsx 模板。只做静态落地页用 saas-landing，只做通用组件用 cult-ui，只定交互规范不落地代码用 ai-chat-patterns，都不走这份。关键词：AI 聊天界面、assistant-ui、Thread、Composer、runtime、流式输出、工具调用、审批卡、生成式界面、generative UI、React。"
category: components
scenario: ai-product
tags: ["ai-chat", "react", "runtime", "streaming", "tool-ui", "generative-ui", "components"]
license: MIT
---

# AI 对话界面组件库

assistant-ui 是 TypeScript / React 的开源组件库，MIT 许可，用来做生产级 AI 对话体验。本技能收录它的文档、原语源码、界面元素示例与 starter 模板；SKILL.md 与 OVERVIEW 为本库编写。

## 先分清两层

| 层 | 是什么 | 在哪看 |
|---|---|---|
| runtime | 与框架无关的状态与协议层，负责消息、流式、工具调用、线程 | `references/docs/runtimes/`、`references/api-surface/assistant-ui__core.ts` |
| primitives | 无样式的 React 组件原语，负责结构与可访问性 | `references/docs/primitives/`、`src/react/` |
| elements | 带样式的成品界面区块，可直接复制进项目 | `references/elements/` |

上层用下层，不要反过来自己重写 runtime 状态。上游仓库约定里明确写了：功能要用现有 runtime 与组件模型组合，不新增平行抽象，不重复实现状态、响应式与接线。

## 上手顺序

1. 新项目用 `npx assistant-ui@latest create`，已有项目用 `npx assistant-ui@latest init`；让代码助手代跑时用 `npx assistant-ui@latest setup`，它会引导选 runtime、后端和组件。
2. 直接装包是 `npm install @assistant-ui/react @assistant-ui/ai-sdk ai`。
3. 最小闭环是 `AssistantRuntimeProvider` 包住页面，`useChatRuntime()` 提供运行时，再放一个 `Thread`。先跑通这一条再扩功能。
4. 按 `references/docs/runtimes/pick-a-runtime` 选后端适配：AI SDK、LangGraph、自定义 transport 各有一套。
5. 需要成品区块时去 `references/elements/` 找对应的 `.mdx`，128 个里有审批卡、产物卡、思维链、代码 diff、模型选择器、追问建议等。

## 目录

| 路径 | 内容 |
|---|---|
| `references/docs/` | 上游文档：入门、runtime、primitives、tools、guides、integrations、迁移、可访问性相关约定 |
| `references/elements/` | 128 个成品界面元素的说明与代码 |
| `references/design/` | 上游自身设计系统的组件文档 |
| `references/examples/` | 文档里的完整示例 |
| `references/api-surface/` | 48 份公开 API 声明快照，查导出名与签名用 |
| `references/repo-conventions.md` | 上游 AGENTS.md：包结构、改动规则、发布约束 |
| `references/OVERVIEW.md` | 本库编写的结构导览与选型提示 |
| `src/react/` | `@assistant-ui/react` 的组件源码 |
| `templates/` | 官方 starter 模板（Next.js、cloud、clerk 等变体） |
| `examples/` | 精选完整示例：生成式界面、产物、思维链、可交互组件、图片生成、自定义线程列表等 |

## 三条硬约束

1. **可访问性不能砍**。上游把键盘操作、aria 属性、响应式布局列为每条 UI 改动的必守项，动效也要给 `prefers-reduced-motion` 分支。修 bug 不允许用「关掉动效」「禁用功能」这类 UX 回退换通过。
2. **不要在组件里重做状态**。消息、分支、排队、流式、工具结果都由 runtime 管；组件只订阅。
3. **改了 `packages/ui/src/` 或 registry 模板要跑同步**。上游有 `pnpm sync-templates --write`，模板漂移会在 CI 失败。

## 边界

- 这是前端组件库，不含模型推理与后端服务。后端协议看 `references/docs/runtimes/` 与各 adapter 文档。
- 上游文档里的安装命令与包名会随版本变，落地前对一下当前版本。
- 云端持久化与控制台相关文档（`docs/cloud`）未收录，那是服务侧内容，与界面技能无关。

## 许可

MIT，Copyright (c) 2026 AgentbaseAI Inc.，全文见 `LICENSE`。本库只做目录裁剪与二次编写，未改动上游源码；裁剪口径见 `CONTRIBUTORS`。
