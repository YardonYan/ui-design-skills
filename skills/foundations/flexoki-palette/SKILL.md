---
name: flexoki-palette
version: 1.0.0
zh_name: "油墨感配色"
en_name: "Inky Color Palette"
description: "一套面向屏幕阅读与写作的低饱和油墨色板，含 16 级中性灰阶与 8 组彩色各 11 级，深浅双底色。当要给笔记应用、文档站、编辑器或代码高亮定颜色，且希望暖纸底而不是纯白、纯黑灰或紫蓝渐变时用。产出是 CSS 变量、亮暗映射与语义角色分配。要做品牌色板提取用 brand-extract，要贴官方品牌规范用 brand-guidelines，要审界面配色合规性用 web-design-guidelines，都不走这份。关键词：配色、色板、油墨色、暖纸底、暗色主题、CSS 变量、代码高亮、Flexoki。"
category: foundation
scenario: web
tags: ["color", "palette", "css-variables", "dark-mode", "typography"]
license: MIT
---

# 油墨感配色

色值来自 Flexoki，MIT 许可。设计目标是长时间在屏幕上读写：底色偏暖纸，彩色取自印刷油墨，整体低饱和，靠灰阶拉层级而不是靠纯黑对比。

## 目录

- `references/palette.css`：完整色值，CSS 变量形式，原样收录。
- `references/usage.md`：亮暗映射、语义角色、对比度注意事项与代码高亮分配。

## 用法

1. 先定底色：浅色用 `--flexoki-paper`（#FFFCF0），深色用 `--flexoki-black`（#100F0F）。不要拿纯白 #FFFFFF 或纯黑 #000000 替换，暖底是这套配色的前提。
2. 正文与边框从中性 16 级灰阶里取，层级靠 100/300/600/850 这类跨度拉开。
3. 彩色只作语义点缀：红表错误、黄表提醒、绿表通过、蓝表链接、紫表引用，每组用 400 或 600 一级，避免同屏出现多级同色。
4. 深浅两套都给出，跟随系统 `prefers-color-scheme` 切换，不要只交一套。

## 边界

- 这是一套读写型配色，不适合强调科技感、促销感或高对比营销页。
- 品牌色已由客户指定时不覆盖品牌色，只用它做中性层级。
- 色值表是事实来源，不要在正文里另写一份十六进制值；要用就引用 `references/palette.css`。

## 许可

MIT，见 `LICENSE`。
