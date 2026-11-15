# 参与与维护

这个仓库按一处一处的界面问题组织技能。加技能、改规则、补例子都欢迎；改之前花两分钟看完这份文件，能省掉一半返工。

## 三种参与方式

| 想做什么 | 怎么做 |
|---|---|
| 报一个问题 | 开 issue，写清你说了什么、AI 做了什么、期望是什么 |
| 加一个技能 | 看下面的四步 |
| 改已有技能 | 直接改该技能的 `SKILL.md` 或 `references/`，跑一次校验 |

## 加一个技能：四步

1. 生成骨架。一条命令，不用手抄格式：

```bash
python tools/new_skill.py --name admin-report --category enterprise \
  --zh "后台报表" --desc "做什么。什么时候用。什么时候别用。"
```

2. 写准 `description`。这是 AI 判断要不要读它的唯一依据，必须写清三件事：做什么、什么时候用、什么时候别用。只写`很好用`等于没写。

3. 放内容。规则与语料进 `references/`，能直接改的模板进 `templates/`，图标与示例进 `assets/`。大文件、图片、依赖不要进仓库。

4. 跑校验并看数字有没有变：

```bash
python tools/build_index.py    # 重算技能地图清单
python tools/lint_skills.py    # 格式、入口、索引、数字一致性
python tools/scan_sensitive.py # 敏感词扫描
```

加完技能总数会变，文档里写死的数字要跟着改；漏改 `lint_skills.py` 会直接报错，不会悄悄放过。

## 命名与格式

- 技能名用小写连字符，至少两段，例如 `admin-form-schema`。
- `SKILL.md` 的 `name` 必须等于目录名。
- 目录结构固定为 `skills/<六类之一>/<技能名>/`，六类见根 `SKILL.md`。
- 新增技能后同步三处：根 `SKILL.md` 的快捷映射、`ROUTER.md` 的口语索引、`docs/skill-map.md`（由脚本生成，不要手改）。

## 不要做的事

| 不要 | 原因 |
|---|---|
| 手改 `docs/skill-map.md` 的清单 | 它是 `tools/build_index.py` 的生成物，重跑会覆盖 |
| 手改 `references/resources/0X-*.md` | 由 `SOURCE.md` 生成，改真相源再重跑 |
| 把公司内部字段、真实客户资料写进技能 | 公开库，扫描脚本会拦 |
| 把技能总数手写多遍 | 让 `lint_skills.py` 帮你查一致性 |
| 一次提交十几个不相关的改动 | 一处一改，回滚和 review 都容易 |

## 提交信息

统一用英文，一次提交一件事。示例：

```
feat(skills): add admin-report for monthly operations summaries
fix(readme): correct the skill count after adding admin-report
docs(router): route report requests to admin-report
```

## 许可

自有内容 Apache-2.0。第三方内容的归属与许可统一登记在 `THIRD-PARTY.md`，版权声明不得删除；新增第三方内容时在同一份文件补一行。
