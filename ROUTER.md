# 选型索引

按「你会怎么说」排，只负责第一步命中。命中之后到 [`docs/skill-map.md`](docs/skill-map.md) 看同段里还有谁、什么时候该换一个。

| 你会这么说 | 去哪一类 | 先用 |
|---|---|---|
| 不知道从哪下手，先定设计方向 | `foundations` | `oil-ui` |
| 界面一眼 AI 味，要批改不要重写 | `foundations` | `unslop` |
| 审界面规范与可访问性 | `foundations` | `web-design-guidelines` |
| 要一整套色板 | `foundations` | `flexoki-palette` |
| 做官网首页 / 落地页 | `web` | `saas-landing` |
| 做定价页 / FAQ / 文档站 | `web` | `pricing-page` |
| 做海报 / 社交卡片 | `web` | `poster-hero` |
| 复刻一个站 / 把设计图变代码 | `web` | `web-clone` |
| 做企业后台整套页面 | `enterprise` | `enterprise-admin` |
| 做列表详情页 / 导入向导 / 权限矩阵 | `enterprise` | `admin-ia-patterns` |
| 把一堆字段整理成可校验的 Schema | `enterprise` | `admin-form-schema` |
| 做数据看板 | `enterprise` | `dashboard` |
| 做 App 界面 / 引导页 | `mobile` | `mobile-app` |
| 查五端移动端尺寸规范 | `mobile` | `mobile-design-spec` |
| 要 React 动效组件源码 | `components` | `cult-ui` |
| 要单个高辨识度交互区块 | `components` | `ricoui-blocks` |
| 要一套风格统一的图标 | `components` | `icon-system` |
| 要功能插图 / 空状态图 | `components` | `spotkit` |
| 要图表模板 | `components` | `lieflat-charts` |
| 在浏览器里调试页面 | `tooling` | `chrome-devtools` |
| 让 Agent 操作网页取结构化内容 | `tooling` | `agent-browser` |
| 出单文件 HTML 工件 | `tooling` | `html-skill-effectiveness` |
| HTML 转 PDF / Markdown 渲染修复 | `tooling` | `html-to-pdf` |
| 读写无限画布数据 | `tooling` | `json-canvas` |

## 六类怎么分

| 类别 | 管什么 | 不管什么 |
|---|---|---|
| `foundations` | 方向、规范、配色、品牌、验收 | 不产出具体页面 |
| `web` | 面向公众的网页与页面类型 | 不做管理端 |
| `enterprise` | 中后台、表单、信息架构、看板 | 不做营销页 |
| `mobile` | App 界面、引导页、多端尺寸 | 不做桌面网页 |
| `components` | 组件、区块、图标、插画、图表 | 不组装整页 |
| `tooling` | 调试、转换、画布格式、交付链路 | 不做设计判断 |

## 判断口径

产出是网页或界面，进这六类；产出是 Word、PDF、PPT 这类文件，不在本库范围内。同一个需求跨两类时，先按最终产物归类，另一类只作为参考。
