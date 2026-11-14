---
name: admin-ia-patterns
version: 1.0.0
zh_name: "中后台信息架构与页面配方"
en_name: "admin-ia-patterns"
description: "中后台的信息架构与页面配方：列表页、详情页、编辑页三件套，导入向导，审批流，权限矩阵，导航层级与页面间的跳转关系。当要从零规划一个管理端、或现有后台页面之间关系混乱要重整时用。产出是页面清单、导航结构、每页的字段与动作。只定字段规则用 admin-form-schema，做现成页面用 enterprise-admin，做单张看板用 dashboard，都不走这份。关键词：中后台、信息架构、列表页、详情页、导入向导、审批流、权限矩阵、导航。"
category: enterprise
scenario: enterprise
tags: ["admin", "schema", "ia", "backoffice", "form"]
---

# 中后台信息架构与页面配方

内容抽自 `enterprise-admin` 的参考资料，按「只解决一件事」重新拆开。整页后台的实现请看 `enterprise-admin`，本技能只管下面这一层。

## 目录

| 文件 | 内容 |
|---|---|
| `references/ia-patterns.md` | ia-patterns 的约定与示例 |
| `references/page-recipes.md` | page-recipes 的约定与示例 |
| `references/component-map.md` | component-map 的约定与示例 |
## 使用顺序

1. 先把业务字段列全，不漏项，也不臆造没出现过的字段。
2. 再定类型、必填、默认值与校验时机。
3. 然后定页面之间的跳转关系与导航层级。
4. 最后才选组件与写页面代码。

## 边界

- 字段以实际业务资料为准，资料里没有的字段不补、不猜。
- 这份给的是结构与约定，不产出可直接运行的后台系统。
- 涉及具体企业的组织名、系统名与人员信息一律不写进产物。

## 许可

参考资料与 `enterprise-admin` 同源，见根目录 `THIRD-PARTY.md`；本文件为本库编写。
