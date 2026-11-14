---
name: ai-chat-patterns
version: 1.0.0
zh_name: "AI 对话界面交互规范"
en_name: "AI Chat Interaction Patterns"
description: "AI 对话界面的状态与交互规范：空态、流式输出、中断与重连、错误恢复、工具调用与人工审批、输入区排队、分支切换、追问建议、可访问性与动效降级。当要评审或设计一个聊天式产品界面、要列出所有要处理的状态、或界面只画了「用户问一句、模型答一句」这种理想路径时用。产出是状态清单、每种状态的界面要求与验收项。要用组件落地用 assistant-ui，要做通用页面用 web 类技能，只做视觉风格用 foundations 类技能，都不走这份。关键词：AI 对话、聊天界面、流式输出、状态机、工具调用、审批卡、追问建议、分支、可访问性、减少动效。"
category: foundations
scenario: ai-product
tags: ["ai-chat", "interaction", "states", "accessibility", "streaming", "approval"]
---

# AI 对话界面交互规范

这份只管「界面该处理哪些状态、每个状态该长什么样」，不提供组件实现。落地到代码时用 `assistant-ui`，那里有对应的 Thread、Composer、Tool UI 与 128 个成品元素。

写界面之前先把状态列全。只画理想路径是这类界面最常见的问题：演示时一句问一句答很顺，真实用户一断网、一改需求、一遇工具审批就掉进空白页。

## 目录

| 文件 | 内容 |
|---|---|
| `references/message-states.md` | 一条消息从发出到结束的全部状态 |
| `references/tool-calls-and-approval.md` | 工具调用展示与人工审批的界面要求 |
| `references/composer-and-input.md` | 输入区、附件、排队与禁用态 |
| `references/branches-and-history.md` | 分支切换、编辑重发、会话列表 |
| `references/accessibility-and-motion.md` | 键盘、读屏、焦点与减少动效 |
| `references/acceptance-checklist.md` | 逐条验收清单 |

## 三条底线

1. **每个异步过程都要有进行中、成功、失败、取消四种可见状态**，不存在「转圈然后什么都不说」。
2. **不靠禁用功能来绕开 bug**。上游的改动规则里也写明，修问题不能用关动效、砍功能、放宽 API 换通过。
3. **信息层级跟着用户当前要做的决定走**。审批时突出「批准什么」，流式时突出「最新内容」，错误时突出「能怎么恢复」。

## 边界

- 不管模型选型、提示词与后端协议。
- 不规定视觉风格，配色与排版交给 `flexoki-palette`、`web-design-guidelines` 一类技能。
- 组件名仅作落点提示，具体实现以 `assistant-ui` 收录的当期文档为准。

## 许可

本技能全部文字由本库编写，Apache-2.0。引用的界面元素名称来自 MIT 许可的 assistant-ui 文档，仅作事实指称。
