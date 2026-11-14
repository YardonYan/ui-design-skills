---
name: dashboard
zh_name: "管理后台仪表板"
en_name: "Admin Dashboard"
emoji: "🎛️"
description: "做单页数据看板：固定侧栏、顶栏、KPI 网格与一到两张图。当只要一个能看数的概览页时用。产出是单页 HTML 模板。要增删改查、列表详情与字段校验用 enterprise-admin，要团队实时动态用 live-dashboard，都不走这份。关键词：看板、仪表盘、KPI、数据概览、单页。"
category: dashboard
scenario: operations
aspect_hint: "桌面 1440"
tags: ["dashboard", "admin", "analytics"]
---

【模板: 管理后台 Dashboard】
【意图】标准 admin/analytics 仪表板单页。
【布局】
- Fixed left sidebar (logo + 导航 + 用户 footer)
- Top bar (search + 通知 + avatar)
- Main: KPI cards 网格 (3-5 个)
- 1-2 张主图表 (折线 / 柱 / 区域)
- 底部 recent activity 列表
