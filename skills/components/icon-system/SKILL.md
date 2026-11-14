---
name: icon-system
version: 1.0.0
zh_name: "成套功能图标"
en_name: "Consistent Icon Set"
description: "一套风格统一的功能图标资产：近千个图标定义与二十个徽标，配合一份成体系的一致性规则。当页面需要一整套图标、要新增图标却怕风格跑偏、或要把图标批量导出成静态 SVG 给设计工具和原生界面使用时用。产出是图标定义文件、命名与关键词表、一致性检查清单。只要一两个通用图标用 bootstrap 或组件库自带的即可；要做插画与空状态图用 spotkit，要做品牌标识用 brandkit，都不走这份。关键词：图标、icon、图标集、SVG 导出、功能图标、徽标、命名规范、风格统一。"
category: components
scenario: web
tags: ["icons", "svg", "asset", "naming", "consistency"]
license: MIT
---

# 成套功能图标

图标定义与徽标来自 Kubai Icons 的 MIT 部分（`icons/`、`badges/`、`packages/`）。规则文字由本库编写，不复制上游的技能文档。

## 目录

- `upstream/icons/`：964 个图标定义，按主题分组，`_` 开头的文件是共享几何与零件。
- `upstream/badges/`：20 个徽标定义。
- `upstream/packages/`：图标定义依赖的构造工具与导出实现，相对路径依赖，不要单独移动这三个目录。
- `references/icon-consistency.md`：成套图标的一致性规则与验收清单。
- `references/naming.md`：命名、关键词与多语言名字的约定。

## 用法

1. 先读 `references/icon-consistency.md`，确认线宽、圆角、留白与色阶这几个不变量。
2. 在 `upstream/icons/` 里找结构最接近的现成图标，照它的写法改，不从零画。
3. 新图标按 `references/naming.md` 命名，并在同组索引里登记。
4. 用 `upstream/packages/` 里的导出实现生成静态 SVG，交付给不能跑脚本的界面。

## 边界

- 图标资产是 MIT，可以改、可以商用、可以随产品分发；`LICENSE-ICONS` 必须跟着走。
- 上游的技能文档与提示词是另一套许可，本库未收录、未改编，也不对外提供。
- 图标是功能图标，不承担品牌标识作用；logo 与品牌视觉另走 `brandkit`。

## 许可

MIT，见 `LICENSE-ICONS`。上游地址与完整条款见根目录 `THIRD-PARTY.md`。
