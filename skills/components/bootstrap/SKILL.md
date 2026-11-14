---
name: bootstrap
description: "Bootstrap 5.3.8 离线全套（编译好的 CSS/JS、SCSS 主题变量、42 个官方示例、117 篇官方文档正文）的选型与落地手册。当要做 SaaS 后台/管理端、需要不引构建链就能打开的离线 HTML 原型、需要客户熟悉的前端框架交付、需要现成的栅格+表单+表格+侧栏骨架时使用。关键词：Bootstrap、后台骨架、admin dashboard、离线 HTML、CDN 内联、SCSS 变量主题、暗色 data-bs-theme、RTL、栅格断点、表单校验、模态框、下拉、导航栏。不适用：项目已用 Tailwind/shadcn 生态（改用 cult-ui、ui-ux-pro-max 或 frontend-design）；要 React 组件封装（Bootstrap 是 CSS+原生 JS，React 侧要另装 react-bootstrap）。"
license: MIT
metadata:
  author: twbs/bootstrap（上游）+ 本地收录与索引（YardonYan）
  upstream: https://github.com/twbs/bootstrap
  version: "5.3.8"
  released: "2025-08-26"
  captured: "2026-10-28"
  sources: "release dist.zip + release examples.zip + npm package scss/ + tag v5.3.8 的 site/src/content"
---

# Bootstrap 5.3.8 · 离线全套与落地

上游 [twbs/bootstrap](https://getbootstrap.com)（MIT）。本 skill 把**编译产物、SCSS 源、官方示例、官方文档正文**四样一起收进本地，断网可用，AI 做后台和原型时不必再靠记忆写类名和 API。

## 什么时候用它，什么时候别用

| 情况 | 选择 |
|---|---|
| SaaS 后台、管理端、内部工具，要快、要稳、要客户能接手 | **本 skill** |
| 要交付一个不引构建链、双击就能打开的离线 HTML 原型/演示页 | **本 skill**（内联 dist） |
| 客户或团队已经在 Tailwind/shadcn 生态里 | 别引 Bootstrap，用 `cult-ui`、`ui-ux-pro-max`、`frontend-design` |
| 要 React/Vue 组件封装 | Bootstrap 本体是 CSS + 原生 JS，React 侧需另装 `react-bootstrap`（本包不含） |
| 要图标 | Bootstrap Icons 是**独立项目**，本包不含，需要时单独取 |

## 里面有什么

```
bootstrap/
├── dist/css/     bootstrap.min.css / .css / .rtl.min.css / grid / reboot / utilities（含非 min 版）
├── dist/js/      bootstrap.bundle.min.js（含 Popper）· bootstrap.min.js（不含 Popper）· esm 版
├── scss/         92 个 SCSS 源：_variables.scss、_functions.scss、_maps.scss、bootstrap.scss 等
├── examples/     42 个官方示例目录（dashboard、sidebars、sign-in、checkout、pricing、product、cheatsheet…）
├── docs/         117 篇官方文档正文（.mdx）：components 24 篇、utilities 20 篇、forms 9 篇、layout 8 篇、customize、helpers、getting-started
├── references/INDEX.md   本地生成的清单（文件、大小、示例名、文档页）
└── LICENSE       MIT
```

## 三种落地方式

**1. 离线单文件 HTML（做演示页/原型最常用）**

把 `dist/css/bootstrap.min.css` 与 `dist/js/bootstrap.bundle.min.js` 的内容直接内联进 `<style>` / `<script>`，产物不联网也能开。要走 CDN 时，SRI 哈希必须**当场从本地 dist 算**或从上游发布页取，不许凭记忆写。

**2. 有构建链的项目**

`npm i bootstrap@5.3.8`，SCSS 定制走本目录 `scss/`：新建入口 scss，先覆盖 `$primary`、`$enable-shadows`、断点 `$grid-breakpoints` 等变量，再 `@import "bootstrap/scss/bootstrap"`。CSS 变量主题走 `--bs-*`（见 `docs/docs/customize/css-variables.mdx`）。

**3. 抄官方示例（做后台最快）**

`examples/dashboard/` 就是完整 SaaS 管理端骨架（侧栏 + 顶栏 + 指标卡 + 表格 + 图表占位），`examples/sidebars/`、`examples/sign-in/`、`examples/checkout/`、`examples/pricing/`、`examples/cheatsheet/` 各对应一类页面。抄之前先读它的 `index.html` 引了哪些文件，别只拷半截。

## 硬约束

1. **类名与 API 要查不要背**。组件的 data 属性、方法、事件、栅格断点默认值都在 `docs/` 里；不确定就打开对应 mdx 读，并在结论里给出文件路径。
2. **JS 依赖 Popper**：下拉、提示、气泡、offcanvas 定位需要 Popper，用 `bootstrap.bundle*.js`（已含）；只引 `bootstrap.min.js` 时必须自己补 `@popperjs/core`。
3. **jQuery 的准确说法**：Bootstrap 5 **不要求** jQuery，但脚本会探测 `window.jQuery`，存在时顺带注册 jQuery 插件接口；要彻底关掉就在 `<body>` 上加 `data-bs-no-jquery`。别说成"完全无关"，也别说成"需要 jQuery"。
4. **暗色模式**用 `data-bs-theme="dark"`（可只在组件级覆盖），不要自己造一套反色 class。
5. **RTL**：换 `bootstrap.rtl.min.css`（JS 无需换），示例有 `dashboard-rtl`、`album-rtl` 等对照。
6. **动效降级**：官方对 `prefers-reduced-motion` 有处理，自定义动画要跟上同样待遇。
7. **别混框架**：同一页面不要 Bootstrap + Tailwind 双基座（reset 与优先级会互相打架）。已有 Tailwind 项目要 Bootstrap 组件，改成手写实现或独立页面。
8. **版本要写死**：本目录是 5.3.8（2025-08-26 发布）。上游另有 `6.0.0-alpha.1`，**别拿 alpha 上生产**；要升级就整目录换版本并复跑一遍交付验收。

## 交付前验收（机械可判）

- 断网打开产物：无 404、无 CDN 请求、样式与交互正常。
- 控制台零报错；下拉/模态框/提示各点一次。
- 暗色与 RTL 两态各截一张图自查。
- 引用的类名能在 `docs/` 对应页找到出处（防自造类名）。

## 更新方式

上游发新版后：取 `bootstrap-<ver>-dist.zip` 与 `-examples.zip`、npm 包里的 `scss/`、tag 上的 `site/src/content`，覆盖对应目录后重跑 `references/INDEX.md` 生成，并把 frontmatter 的 `version`/`released`/`sources` 改掉。
