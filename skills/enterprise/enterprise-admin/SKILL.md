---
name: enterprise-admin
version: 1.0.0
zh_name: "企业后台页面与模块"
en_name: "Enterprise Admin Pages"
emoji: "🏢"
description: "企业级后台（ERP / CRM / SaaS 管理端）的页面配方与字段约定。当要把业务做成能用的管理端、要给现有系统补列表页详情页、要做导入向导或权限矩阵、要把一堆字段整理成可校验的表单 Schema 时用。产出是 React + shadcn/ui 的可落地页面结构与字段定义，不是营销页、不是单页看板。做落地页用 saas-landing，做单张看板用 dashboard，做组件 API 规范用 components-build，只管代码风格用 frontend-spec，都不走这份。关键词：企业后台、管理端、ERP、CRM、SaaS 后台、中后台、列表页、详情页、导入向导、权限矩阵、审批流、字段 Schema、主从表、字典管理、编号规则。"
category: admin
scenario: enterprise
tags: ["admin", "erp", "crm", "backoffice", "schema", "shadcn", "list-detail"]
---

# 企业后台页面与模块

营销页解决"让人相信"，后台解决"让人干活"。两者的差别不在好不好看，在三件事：字段多、动作多、错一次代价大。后台页面做砸的典型症状是字段堆成一坨、动作散在四个角落、导错数据没法回滚。

这份技能把后台页面拆成三段，每段有独立判据：

| 段 | 解决什么 | 落在哪 |
|---|---|---|
| 字段 Schema | 一条业务记录到底有哪些字段、什么类型、怎么校验 | `references/field-schema.md` |
| 页面配方 | 八个固定场景各自长什么样、要放哪些动作 | `references/page-recipes.md` |
| 模块划分 | 一个后台该切成哪些模块、怎么命名 | `references/ia-patterns.md` |
| 组件映射 | 场景里的每个部件对应哪个 shadcn/ui 组件 | `references/component-map.md` |

视觉 token 不在这份里，去 `design-md-library` 取具体色值字号；代码风格去 `frontend-spec`；组件 API 设计去 `components-build`。

## 八个页面配方

先认场景，再挑配方。认错了会白做一遍。

| 你要做的 | 配方 | 关键判据 |
|---|---|---|
| 一屏看全部记录、要筛要排要批量操作 | 列表页 | 分页必须服务端；筛选条件要进 URL |
| 看一条记录的全部信息与关联 | 详情页 | 首屏给结论，明细放 Tab；操作按钮跟随状态 |
| 新建或修改一条记录 | 编辑页 | 字段分组不超过 5 组；离开前拦未保存 |
| 一次性录入几十上百条 | 导入向导 | 必须先出预检报告，用户确认后才入库 |
| 谁能看谁能改 | 权限矩阵 | 角色 × 资源 × 动作，行内开关，改动即生效 |
| 单据要走审核 | 审批流 | 状态机 + 时间轴；驳回要留原因 |
| 下拉选项与单据编号 | 字典与编号规则 | 字典可维护；编号并发安全 |
| 一张单据带多行明细 | 主从表 | 明细行内编辑；合计自动算且后端复算 |

每个配方的骨架、必备部件、易错点写在 `references/page-recipes.md`。

## 十二条硬规矩

这些不是建议，是做过一次就会知道代价的判据。写完页面逐条对一遍。

1. 分页只在服务端做。前端假分页在两千条以上必崩，且筛选和统计会算错。
2. 筛选、排序、页码全部写进 URL query。刷新、分享、回退都要能还原同一屏。
3. 金额不用浮点。数据库用 `numeric`，前端用整数分或字符串，展示时再格式化。
4. 时间存 UTC，展示按用户时区。前端不许 `new Date().toLocaleString()` 直接存库。
5. 列表页默认给空态、加载态、错误态三张面孔。只做有数据的样子等于没做完。
6. 删除走软删，保留操作日志。后台里没有"真的删掉"这个动作。
7. 必填校验前后端各做一遍。前端做体验，后端做底线。
8. 导入分两步：先预检出报告，再确认入库。一步到位的导入一定会脏数据。
9. 单据编号生成要防并发。两个人同时点新建，不能拿到同一个号。
10. 主从表的合计由后端复算。前端算的合计只用于即时反馈。
11. 危险动作（作废、批量删、覆盖导入）二次确认，并在确认框里写清影响条数。
12. 每个写操作留 `created_by` / `updated_by` / `updated_at`。出事时要能定位到人。

## 与现有技能的边界

| 要做的事 | 用这个 | 不用那个 | 为什么 |
|---|---|---|---|
| 企业后台整套页面 | `enterprise-admin` | `dashboard` | 后者是单页 HTML 看板模板，没有增删改查 |
| 中后台列表与表单 | `enterprise-admin` | `saas-landing` | 后者是营销页，字段和动作模型完全不同 |
| 要某家的视觉气质 | `design-md-library` | 这份 | 那份给具体 token，这份给页面结构，可以叠加用 |
| 组件该怎么设计 API | `components-build` | 这份 | 那份管组件契约，这份管业务页面拼装 |
| 代码命名与目录 | `frontend-spec` | 这份 | 那份是通用规范，不含业务场景 |

## 从字段清单到能跑的页面

五步，顺序不能倒。第三步之前不要写组件。

1. 列字段清单：把业务方给的表格、老系统截图、纸质单据上的字段全抄下来，包括下拉、手填、备注格。宁多勿少。
2. 定 Schema：每个字段给 `fieldname` / `label` / `type` / `required` / `options` / `group` / `in_list`。模板见 `templates/field-schema.example.json`。
3. 分组排序：按业务动作分组，不按技术类型分组。一屏不超过 5 组，每组不超过 12 个字段。
4. 选配方：列表页 + 详情页 + 编辑页是底座，导入向导与权限矩阵按需加。
5. 拼组件：照 `references/component-map.md` 取 shadcn/ui 部件，照配方的骨架摆位置。

字段清单里没有的字段不要凭想象补。用户上传什么就学什么，没出现的字段不写进 Schema。这条比其余十一条都重要，因为它会污染整张表。

## 反面清单

以下都见过，都返工过。

- 把 ERP 的 176 个字段原样搬进页面。其中 58 个是分组分隔符，真正要填的只有一百来个，全平铺等于没有设计。
- 列表页塞了十二个筛选条件，用户每次都要滚动找。超过五个条件收进"更多筛选"。
- 详情页顶部放操作按钮，滚到第三屏才看到。主操作固定在页面头部或右下角悬浮。
- 编辑页用弹窗。字段一多弹窗必溢出，改用独立路由或抽屉。
- 导入只给"成功 98 条、失败 2 条"，不说哪两行错在哪。用户没法修，只能重来。
- 权限用前端隐藏按钮实现。接口没拦就是没权限。

## 来源

页面结构参照 `satnaing/shadcn-admin`（MIT，2.5k fork）的实际组织方式：features 下按业务切 auth / dashboard / users / tasks / apps / chats / settings / errors，data-table 拆成 bulk-actions / column-header / faceted-filter / pagination / toolbar / view-options 六个部件。

字段 Schema 的分组与校验思路参照 ERPNext 的 DocType 定义方式（GPL-3.0，只取结构不取代码）：176 个字段里 Section Break、Column Break、Tab Break 共 58 个负责分组，`depends_on` 管字段联动，`permissions` 按角色给 read / write / create / delete / submit / cancel / amend 十二种动作。

模块划分参照 twenty 的前端模块切法（AGPL-3.0，只取思路不取代码）：object-metadata 管字段定义、views 管保存的视图、record-export 与 spreadsheet-import 管进出、workflow 管自动化、command-menu 与 keyboard-shortcut-menu 管效率。

具体许可见 `CONTRIBUTORS`。
