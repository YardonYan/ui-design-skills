# assistant-ui 结构导览

本文件由本库编写，用来给 `references/docs/` 那几百份上游文档一个入口。事实以原文档为准，这里只讲怎么找。

## 按任务找文档

| 手上的活 | 去哪个目录 |
|---|---|
| 第一次接、装包、起项目 | `docs/(getting-started)/` |
| 选后端 / 接自己的协议 | `docs/runtimes/` |
| 想知道某个组件的 props | `docs/(reference)/api-reference/primitives/` |
| 想查导出名与签名 | `api-surface/` |
| 做工具调用、审批、生成式界面 | `docs/tools/` |
| 做消息、附件、输入框、分支切换 | `docs/primitives/` |
| 找现成界面区块 | `elements/` |
| 做持久化、状态存储 | `docs/store/` |
| 迁移版本 | `docs/migrations/` |
| 接第三方模型或框架 | `docs/integrations/` |
| 移动端 | `docs/react-native/` |
| 通用做法与专题 | `docs/guides/` |

## 概念对照

| 概念 | 作用 | 常见误区 |
|---|---|---|
| runtime | 持有会话状态、消息流、工具结果，向组件提供订阅 | 误当成 HTTP 客户端，在组件里自己轮询 |
| Thread | 一条会话的消息列表容器 | 与 ThreadList 混淆，后者是会话列表 |
| Composer | 输入区，管附件、提交、排队、禁用态 | 把模型选择、斜杠命令塞进一个组件，难维护 |
| Message / MessagePart | 一条消息及其分片，流式输出按分片追加 | 把整条流式文本当单块重渲染 |
| Tool UI | 工具调用的展示与人工审批 | 只显示 JSON，用户看不懂在批准什么 |
| Generative UI | 模型从你给出的组件词表里组合界面 | 直接让模型输出任意 HTML |

## 未收录的部分及原因

| 上游目录 | 原因 |
|---|---|
| `apps/docs/content/docs/cloud/` | 云端服务与控制台文档，与界面组件技能无关 |
| `apps/docs/content/docs/vue/` | Vue 版本，本技能按 React 主线组织 |
| `apps/docs/app/`、`apps/docs/public/` | 文档站应用代码与静态素材，不是技能载荷 |
| `examples/` 全量 759 文件 | 只精选与界面模式直接相关的若干示例，其余是集成样板 |
| 图片、视频、字体、lockfile、构建产物 | 体积大且与技能载荷无关 |

需要完整仓库时按 `CONTRIBUTORS` 里的地址自行克隆，本库不替代上游。
