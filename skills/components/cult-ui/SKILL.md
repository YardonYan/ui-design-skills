---
name: cult-ui
description: "cult/ui 动效组件库（154 个组件条目 / 141 个 React + Tailwind + Motion 源文件、153 个示例条目）的选型与落地手册。当要做落地页/后台/AI 产品界面并且技术栈是 Next.js/React + Tailwind + shadcn/ui、需要现成的动效组件（首屏标题、发光描边 halo、卡片光束、动态岛、终端动画、看板、提示词输入框等）时使用：先按风格族选件，再读 docs 看 props，再拷源码进项目。关键词：组件选型、动效组件、shadcn 组件库、landing 首屏、halo、border beam、Motion、tailwind 组件。不适用：纯静态 HTML/Shopify 站不能直接装（只能借结构与参数）；要新建组件库规范用 components-build；动画掉帧用 fixing-motion-performance；定视觉方向与配色用 ui-ux-pro-max。"
license: MIT
metadata:
  author: nolly-studio/cult-ui（上游）+ 本地收录与索引（YardonYan）
  upstream: https://github.com/nolly-studio/cult-ui
  commit: 7f031dc812f7bda10213bab62752dd6d080297ff
  captured: "2026-10-28"
  components: 154
  examples: 136
---

# cult/ui 组件库 · 选型与落地

上游是 [cult-ui](https://cult-ui.com)（MIT，150+ 动画组件，React + Tailwind + Motion）。本 skill 把**组件源码、示例、用法文档和一份分类索引**一起收进本地，断网也能查。

口径要说准：registry 里 **154 个 `registry:ui` 组件条目**落在 **141 个 `.tsx` 源文件**上（多个条目会共用同一文件，例如同一组件的不同导出），示例侧是 **153 个条目 / 136 个 example 文件 + 1 个 block**。按文件找组件用 `references/INDEX.md` 的「源码」列，别按数量对账。

## 什么时候用哪个

| 场景 | 用 |
|---|---|
| React/Next + Tailwind 项目要现成动效组件 | 本 skill |
| 要**新建**一套组件库/定组件 API 规范 | `components-build`（shadcn 与 Hayden Bleasel 写的 16 类规则） |
| 组件动画掉帧、长列表卡顿 | `fixing-motion-performance` |
| 还没有技术栈、要先定风格与配色 | `ui-ux-pro-max` → `hallmark` 兜底 |
| 要照某个真实网站的观感做 | `design-md-library` / `reference-design-contract` |

## 三步用法（MUST 按顺序）

1. **选族再选件**：打开 [references/INDEX.md](references/INDEX.md)。同一控件有多套外观族（`animated-`／`halo-`／`border-beam-`／`organic-`／`neumorph-`／`texture-`），**一个页面只用一族**，混用会一眼假。索引里每个组件给了说明、npm 依赖、依赖组件和源码文件名。
2. **读用法与 props**：`docs/components/<name>.mdx` 是上游原稿（含 CLI 与手动两种安装、props 表、变体示例）；示例真码在 `registry/default/example/<name>-demo.tsx`。
3. **拷源码进项目**：源码在 `registry/default/ui/<name>.tsx`。复制过去后做三件事——补 npm 依赖、把 `@/registry/...` 与 `@/lib/utils` 改成项目自己的别名、确认 `cn()` 与 CSS 变量基座存在（shadcn 的 `globals.css` token）。

也可以走 CLI（需要联网）：`npx shadcn@latest add @cult-ui/<name>`。

## 硬约束

1. **别一次拷几十个组件**。按页面上的具体位置选 3–8 个，多余的组件是多余的维护债。
2. **依赖前提**：React 18+/Next.js、Tailwind、shadcn/ui 基座（`components.json` + `cn` 工具）、多数组件依赖 `motion`（原 framer-motion），部分依赖 Radix UI。项目没有这些基座时，先补基座或改用纯 CSS 实现，不要硬塞。
3. **`"use client"` 要保留**。这些组件大量使用 hooks 与 Motion，去掉指令会在 RSC 里直接报错。
4. **动效必须尊重 `prefers-reduced-motion`**：首屏动画类组件（`text-animate`、`hero-*`、`bg-animate-*`）落地时补媒体查询降级，或按 `fixing-motion-performance` 的口径处理。
5. **不许伪造依赖**：INDEX 里 `deps` 是上游 registry 的真值，照抄；不确定就读 `registry.json` 对应条目，别猜。
6. **纯静态/Shopify 场景**：不能装 React 组件。此时只借它的**结构与参数**（层级、间距、发光强度、时长缓动），用 HTML/CSS 重写，并在交付说明里写清"参考 cult/ui 某组件，非直接复用"。
7. **版本追踪**：本目录内容对应上游 commit `7f031dc`（2026-10-14 抓取）。要更新就重新稀疏克隆该仓库并覆盖 `registry/`、`docs/`、`registry.json`，然后重跑索引生成（见 CONTRIBUTORS）。

## 目录结构

```
cult-ui/
├── SKILL.md                 本文件
├── registry.json            上游 registry 索引（307 条：154 组件 + 136 示例 + 区块）
├── references/INDEX.md      分类索引（按风格族与用途分组，含 deps 与源码名）
├── registry/default/
│   ├── ui/                  141 个组件源文件 .tsx（对应 154 个 registry 条目）
│   ├── example/             136 个示例 .tsx（对应 153 个条目）
│   └── block/               整块页面示例
├── docs/                    上游用法文档 .mdx（含 props、安装、变体）
├── references-DESIGN.md     上游站点自己的设计说明
└── LICENSE.md               MIT
```

## 交付时的说法

给用户的说明里写清：组件来自 cult/ui（MIT，可商用），用了哪几个、依赖装了哪些、哪些地方是照它的参数改写的。别把上游组件说成自研。
