---
name: live-dashboard
zh_name: "Notion 风团队仪表板"
en_name: "Live Team Dashboard"
emoji: "📈"
description: "做团队实时动态看板，含 KPI、七日趋势线与活动流。当要显示团队正在做什么、现在进展如何时用。产出是单页 HTML 模板。只要静态数据概览用 dashboard，要完整中后台用 enterprise-admin，都不走这份。关键词：实时看板、活动流、趋势线、团队动态、KPI。"
category: dashboard
scenario: operations
aspect_hint: "桌面长页"
featured: 1
tags: ["notion", "team", "live", "dashboard"]
---

【模板: Live Team Dashboard】
【意图】Notion 风的团队动态总览, 即使没有数据源也用 seed 数据兜底。
【布局】
- Header (团队 + 时间窗)
- KPI 卡片网格
- 7 天 sparkline 趋势
- Real-time activity feed (avatar + 动作 + 时间)
- Linked database task table (zebra + 状态 pill)
【设计细节】
- Notion-callout / toggle / 数据库表配色风格
