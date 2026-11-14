# Bootstrap 5.3.8 本地清单 · Local inventory

由脚本从本目录实际文件生成，改完重跑。文档正文与示例都在这儿，AI 用之前先查这份，别凭记忆写类名。

## dist（编译产物）

| 文件 | KB |
|---|---|
| `dist/css/bootstrap-grid.css` | 68 |
| `dist/css/bootstrap-grid.min.css` | 50 |
| `dist/css/bootstrap-grid.rtl.css` | 68 |
| `dist/css/bootstrap-grid.rtl.min.css` | 50 |
| `dist/css/bootstrap-reboot.css` | 11 |
| `dist/css/bootstrap-reboot.min.css` | 9 |
| `dist/css/bootstrap-reboot.rtl.css` | 11 |
| `dist/css/bootstrap-reboot.rtl.min.css` | 10 |
| `dist/css/bootstrap-utilities.css` | 105 |
| `dist/css/bootstrap-utilities.min.css` | 83 |
| `dist/css/bootstrap-utilities.rtl.css` | 105 |
| `dist/css/bootstrap-utilities.rtl.min.css` | 83 |
| `dist/css/bootstrap.css` | 273 |
| `dist/css/bootstrap.min.css` | 226 |
| `dist/css/bootstrap.rtl.css` | 272 |
| `dist/css/bootstrap.rtl.min.css` | 226 |
| `dist/js/bootstrap.bundle.js` | 202 |
| `dist/js/bootstrap.bundle.min.js` | 78 |
| `dist/js/bootstrap.esm.js` | 132 |
| `dist/js/bootstrap.esm.min.js` | 72 |
| `dist/js/bootstrap.js` | 142 |
| `dist/js/bootstrap.min.js` | 59 |

## scss（主题定制入口）

| 关键文件 | KB |
|---|---|
| `scss/bootstrap.scss` | 0 |
| `scss/_variables.scss` | 74 |
| `scss/_functions.scss` | 10 |
| `scss/_maps.scss` | 5 |
| `scss/_mixins.scss` | 0 |
| `scss/_root.scss` | 6 |
| `scss/_utilities.scss` | 18 |

共 92 个 scss 文件（含 mixins/ helpers/ forms/ 等子目录）。

## examples（42 个官方示例）

**做后台/交易页优先看：** `cheatsheet`, `checkout`, `checkout-rtl`, `dashboard`, `dashboard-rtl`, `navbar-fixed`, `offcanvas-navbar`, `pricing`, `product`, `sidebars`, `sign-in`, `sticky-footer-navbar`

全部：`album`, `album-rtl`, `assets`, `badges`, `blog`, `blog-rtl`, `breadcrumbs`, `buttons`, `carousel`, `carousel-rtl`, `cheatsheet`, `cheatsheet-rtl`, `checkout`, `checkout-rtl`, `cover`, `dashboard`, `dashboard-rtl`, `dropdowns`, `features`, `footers`, `grid`, `headers`, `heroes`, `jumbotron`, `jumbotrons`, `list-groups`, `masonry`, `modals`, `navbar-bottom`, `navbar-fixed`, `navbar-static`, `navbars`, `navbars-offcanvas`, `offcanvas`, `offcanvas-navbar`, `pricing`, `product`, `sidebars`, `sign-in`, `starter-template`, `sticky-footer`, `sticky-footer-navbar`

## docs（官方文档正文）

| 分区 | 篇数 | 内容 |
|---|---|---|
| `docs/docs/about/` | 5 | 概述/团队/品牌/翻译/许可证 |
| `docs/docs/components/` | 24 | 24 个组件的类名、data 属性、方法、事件 |
| `docs/docs/content/` | 5 | 排版、表格、图片、figures |
| `docs/docs/customize/` | 8 | CSS 变量、SCSS 变量、JS 构建、主题、RTL |
| `docs/docs/extend/` | 2 | 图标与自定义组件建议 |
| `docs/docs/forms/` | 9 | 表单控件、校验、浮动标签、输入组、范围、选择 |
| `docs/docs/getting-started/` | 13 | 下载、内容结构、JS 用法、构建工具、compiler-free、webpack |
| `docs/docs/helpers/` | 12 | ratio/clearfix/color-bg/position/visually-hidden 等辅助类 |
| `docs/docs/layout/` | 8 | 栅格、断点、容器、gutter、z-index、css-grid |
| `docs/docs/utilities/` | 20 | 20 篇工具类（含 api 总表） |
| `docs/docs/*.mdx` 单页 | 2 | docsref.mdx, migration.mdx |

查具体页面：`docs/docs/<分区>/<页>.mdx`。例：模态框 = `docs/docs/components/modal.mdx`；断点默认值 = `docs/docs/layout/breakpoints.mdx`；CSS 变量 = `docs/docs/customize/css-variables.mdx`。