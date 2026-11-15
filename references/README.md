# 跨技能共享语料

这里放的是多个技能共用的事实来源，不属于任何一个技能目录。技能里引用语料时写相对路径，不要复制一份正文进去，避免同一份数据在两个地方各改一次。

| 目录 | 内容 | 文件数口径 |
|---|---|---|
| `design-md/` | 84 家产品与品牌的设计语料，供 `design-md-library`、`brand-extract` 等按风格取用 | 167 份，MIT，许可见目录内 LICENSE |
| `palettes/` | Flexoki 油墨色板原始 CSS 变量 | 1 份，MIT |
| `specs/` | JSON Canvas 1.0 规范原文与相关许可 | 3 份，MIT |
| `resources/` | 9 类外部网址索引，含 37 条 GitHub 与 103 条站点 | 9 个分类文件 + INDEX + SOURCE |
| `wisdom/` | 5 个上游技能仓库的文本快照，统合外部设计经验 | 169 份 Markdown，各带 LICENSE 与 SOURCE |

`resources/` 与 `wisdom/` 默认不加载。只有意图命中找资源、找灵感或借外部经验时，才按 `docs/resource-routing.md` 读命中的一份。两层的 INDEX 与各分类文件由 `tools/build_resource_index.py` 生成，真相源分别是 `resources/SOURCE.md` 与各智慧目录的 `SOURCE.md`。

## 维护约定

- 语料只从上游原样收录，不在本库里改写内容；要加工就写成技能内的 `references/`。
- 每份语料带自己的 LICENSE，移动目录时许可文件必须跟着走。
- 新增语料后，在根目录 `THIRD-PARTY.md` 补一行来源与许可。
