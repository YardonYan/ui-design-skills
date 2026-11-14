---
name: admin-form-schema
version: 1.0.0
zh_name: "中后台字段 Schema"
en_name: "admin-form-schema"
description: "把一堆业务字段整理成可校验的表单 Schema：字段类型、必填与默认值、字典与枚举、主从表关系、编号规则、校验时机。当要做录入表单、编辑页、导入模板，或要把业务口述的字段落成可被程序消费的定义时用。产出是字段清单、类型与校验规则、示例 JSON。要做整页后台用 enterprise-admin，只做信息架构用 admin-ia-patterns，做单页看板用 dashboard，都不走这份。关键词：表单、字段 Schema、校验规则、字典、枚举、主从表、编号规则、导入模板。"
category: enterprise
scenario: enterprise
tags: ["admin", "schema", "ia", "backoffice", "form"]
---

# 中后台字段 Schema

内容抽自 `enterprise-admin` 的参考资料，按「只解决一件事」重新拆开。整页后台的实现请看 `enterprise-admin`，本技能只管下面这一层。

## 目录

| 文件 | 内容 |
|---|---|
| `references/field-schema.md` | field-schema 的约定与示例 |
| `references/component-map.md` | component-map 的约定与示例 |
| `templates/field-schema.example.json` | 可直接改的 Schema 样例 |

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
