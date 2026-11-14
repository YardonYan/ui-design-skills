---
name: json-canvas
version: 1.0.0
zh_name: "无限画布数据格式"
en_name: "Infinite Canvas Data"
description: "读写 JSON Canvas 格式的画布文件：节点、边、坐标、分组与颜色枚举。当要把笔记、图片与想法铺到一张画布上、要把界面原型导出成可交换的画布数据、或要为自己的工具加画布导入导出时用。产出是合法的 .canvas 文件与字段对照说明。要做画布视觉设计用 canvas-design，要画流程图用 drawio-diagram 或 excalidraw-diagram，都不走这份。关键词：Canvas、画布、节点、连线、JSON Canvas、无限画布、导出格式、坐标。"
category: tooling
scenario: web
tags: ["canvas", "json", "spec", "interchange", "nodes", "edges"]
license: MIT
---

# 无限画布数据格式

规范来自 JSON Canvas Spec 1.0，MIT 许可，原样收在 `references/spec-1.0.md`，示例文件在 `assets/sample.canvas`。本文件只讲用法与坑，字段定义以规范为准。

## 结构

一个 `.canvas` 文件是 JSON，顶层只有两个可选数组：`nodes` 与 `edges`。

| 对象 | 必填字段 | 追加字段 |
|---|---|---|
| 通用节点 | id、type、x、y、width、height | color（可选） |
| text 节点 | 同上 | text，纯文本，允许 Markdown |
| file 节点 | 同上 | file；可选 subpath，以 # 开头 |
| link 节点 | 同上 | url |
| group 节点 | 同上 | label、background、backgroundStyle |
| 边 | id、fromNode、toNode | fromSide、toSide、label、color、箭头 |

`type` 只有 text、file、link、group 四种。

## 三条容易踩的坑

1. **节点顺序即层叠顺序**。数组按 z-index 升序，第一个在最底层，最后一个在最顶层。导入导出时不能按字典序重排，否则分组会被盖住。
2. **坐标是整数像素**。布局算法输出前要取整，浮点坐标在部分实现里会被截断。
3. **颜色是枚举不是自由色值**。映射到自定义主题时要建一张对照表，不要把十六进制色直接写进 color 字段。

## 对做界面的人有什么用

- 画布数据是纯 JSON，可以脱离具体应用读写，适合把界面原型的卡片与连线导出成可交换格式。
- 分组节点提供的是视觉容器，不是数据嵌套；父子关系靠坐标与视觉表达，别当树结构解析。
- file 节点的路径是库内相对路径，跨库迁移时要一并改写。

## 许可

MIT，见 `LICENSE`。上游地址见根目录 `THIRD-PARTY.md`。
