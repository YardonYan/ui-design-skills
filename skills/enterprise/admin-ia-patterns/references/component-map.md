# 组件映射

企业后台 80% 的界面由十来种部件拼出来。这份表说清每个场景该拿什么，别自己造。

## 场景到组件

| 场景 | 用 | 来源 | 备注 |
|---|---|---|---|
| 记录列表 | `DataTable`（TanStack Table） | shadcn/ui 文档 + shadcn-admin 组合 | 列定义与表格分离 |
| 列头排序 | `DataTableColumnHeader` | shadcn-admin | 三态：无、升、降 |
| 筛选 | `DataTableFacetedFilter` | shadcn-admin | 多选 + 计数 |
| 工具栏 | `DataTableToolbar` | shadcn-admin | 搜索 + 筛选 + 视图切换 |
| 分页 | `DataTablePagination` | shadcn-admin | 服务端分页时改 props 来源 |
| 批量操作 | `DataTableBulkActions` | shadcn-admin | 有选中项才出现 |
| 列显示开关 | `DataTableViewOptions` | shadcn-admin | 用户自选列 |
| 行内操作 | `DropdownMenu` | shadcn/ui | 超过三个收进菜单 |
| 确认危险动作 | `AlertDialog` | shadcn/ui | 写清影响条数 |
| 表单 | `Form` + `FormField` | shadcn/ui（react-hook-form） | 错误定位到字段 |
| 金额输入 | `Input` + 千分位格式化 | 自写薄封装 | 存整数分或字符串 |
| 日期 | `DatePicker` | shadcn-admin | Popover + Calendar |
| 日期区间 | `DateRangePicker` | shadcn-admin（简化版） | 预设：今天/本周/本月 |
| 下拉 | `Select` | shadcn/ui | 选项超过 20 条换可搜索 |
| 可搜索下拉 | `Combobox`（Popover + Command） | shadcn/ui | 关联记录选择用这个 |
| 状态 | `Badge` | shadcn/ui | 颜色全站统一映射 |
| 长文本展示 | `LongText`（折叠 + 展开） | shadcn-admin | 详情页备注用 |
| 侧边抽屉 | `Sheet` | shadcn/ui | 编辑少量字段时用 |
| 全局搜索 | `CommandMenu`（⌘K） | shadcn-admin | 搜页面 + 搜记录 |
| 消息提示 | `Sonner` / `Toast` | shadcn/ui | 成功 3 秒，错误手动关 |
| 进度 | `Progress` | shadcn/ui | 导入与批处理 |
| 步骤条 | 自写（Steps） | 组合 | 导入向导四步 |
| 时间轴 | 自写（Timeline） | 组合 | 审批流与日志 |
| 空态 | `Empty`（图标 + 文案 + 按钮） | 自写 | 两种文案分开 |
| 骨架屏 | `Skeleton` | shadcn/ui | 列表与详情各一套 |
| 权限不足页 | `forbidden` | shadcn-admin | 403 |
| 会话过期 | `unauthorized` | shadcn-admin | 401，带重新登录 |
| 找不到 | `not-found` | shadcn-admin | 404 |
| 服务异常 | `general-error` | shadcn-admin | 500，带重试 |
| 维护中 | `maintenance-error` | shadcn-admin | 503 |
| 主题切换 | `ThemeSwitch` + `ConfigDrawer` | shadcn-admin | 深浅色 + 圆角密度 |
| 导航进度条 | `NavigationProgress` | shadcn-admin | 路由切换顶部细条 |
| 跳过导航 | `SkipToMain` | shadcn-admin | 无障碍，键盘用户 |

## 三类部件不要自己写

第一类，表格。排序、筛选、分页、列显隐、批量选择的组合逻辑很绕，TanStack Table 加 shadcn-admin 的六个部件已经覆盖，自己写必踩选中状态与分页联动的坑。

第二类，弹层。Dialog / Sheet / Popover / AlertDialog 的焦点管理、滚动锁定、Esc 关闭、无障碍属性，Radix 底层已经处理。自己写 div 弹层，键盘用户直接用不了。

第三类，表单。react-hook-form 加 zod 的错误定位已经成熟，手写受控组件在字段超过十个后必然出现重渲染和值不同步。

## 需要自己写的三种

- 时间轴（审批流、操作日志）：结构简单，通用库都太重。
- 步骤条（导入向导）：要控制"不可跳步"和"回退保留数据"，通用库反而别扭。
- 权限矩阵：行列都是动态的，没有现成组件。

这三个的骨架在 `templates/` 下。

## 信息密度

企业后台和营销页的密度要求相反。营销页留白，后台塞满。

| 项 | 后台取值 | 说明 |
|---|---|---|
| 基础字号 | 13 到 14px | 12px 太小，16px 一屏装不下 |
| 表格行高 | 40 到 44px | 低于 36px 点不准 |
| 表头字号 | 12 到 13px，中灰 | 弱于正文，不抢注意力 |
| 控件高度 | 32 到 36px | 与行高对齐 |
| 区块间距 | 16 到 24px | 分组之间，不是每个元素之间 |
| 页面左右留白 | 24px | 宽屏可到 32px |
| 圆角 | 4 到 6px | 后台不用大圆角 |

具体色值去 `design-md-library` 取。挑偏产品型的品牌（linear、clickhouse、hashicorp 这类）比挑消费品牌合适，后者为营销页设计的饱和度和留白在后台会显得松散。

## 深浅色

后台必须有深色。不是审美问题，是值班场景：晚上盯屏、机房环境、长时间看表格。

要点：

- 用 CSS 变量定义语义色（`--surface` `--hairline` `--ink`），不要在组件里写死 `bg-white`。
- 表格斑马纹在深色下要降低对比，否则一屏条纹晃眼。
- 状态徽章在深浅两套下都要过对比度检查，尤其是黄色和绿色。
- 图表配色要两套。同一份数据在深色下用浅色主题的色板会糊成一片。

shadcn-admin 的 `ThemeSwitch` 与 `ConfigDrawer` 已经把变量切换做好了，直接复用，别另建一套主题系统。
