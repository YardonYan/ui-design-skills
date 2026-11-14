---
name: ricoui-blocks
version: 1.0.0
zh_name: "动效区块组件"
en_name: "Motion UI Blocks"
description: "一组 React + Tailwind 的高辨识度界面区块：按钮开关、翻页进度、光学放大镜、空状态、贡献图、ASCII 背景、多帘预加载器等。当落地页、作品集、产品展示或 AI 产品界面需要一个有记忆点的交互组件，且希望直接复制源码而不是引 npm 依赖时用。产出是带类型声明的 tsx 源码与组件配置。做整套基础控件用 cult-ui 或 bootstrap，做完整页面用 saas-landing，只做视觉规范用 frontend-spec，都不走这份。关键词：动效组件、React 区块、Tailwind、Copy Source、shadcn registry、空状态、预加载器、放大镜、贡献图。"
category: components
scenario: web
tags: ["react", "tailwind", "motion", "blocks", "registry", "tsx"]
license: MIT
---

# 动效区块组件

来源为 RicoUI Blocks V1.0，MIT 许可。它的定位不是基础控件库，而是补齐 shadcn/ui 不覆盖的那类「强视觉 + 强交互」组件。安装方式是复制源码，装完代码归项目自己，不存在运行时锁定。

## 目录

- `references/`：上游的设计说明、页面结构、组件规范与 registry 约定。动手前先读 `DESIGN.md` 与 `COMPONENT-GUIDELINES.md`。
- `templates/`：registry 下的组件源码，按文件名对应组件。
- `assets/registry.json`：组件清单，含每个组件的分类、依赖与登记信息。

## 选型

| 手上的活 | 先看 |
|---|---|
| 要判断某个区块是否适合当前页面 | `references/PAGE-STRUCTURE.md` |
| 要写新区块并保持风格一致 | `references/COMPONENT-GUIDELINES.md` |
| 要接 shadcn registry 分发 | `references/REGISTRY.md` |
| 要理解整体分层 | `references/ARCHITECTURE.md` |
| 要挑具体组件 | `assets/registry.json` |

## 边界

- 组件按个引入，Motion、GSAP 等依赖由组件自己声明，不要全局预装。
- 动效组件要保留 `prefers-reduced-motion` 分支与键盘可达性，这两条是上游的硬性约定。
- 需要一整套表单、表格、导航等基础控件时，去 `cult-ui` 或 `bootstrap`；这里只有 15 个高辨识度区块，不覆盖通用控件。

## 许可

MIT，版权声明见 `LICENSE`。改动与商用允许，但须保留版权与许可声明。
