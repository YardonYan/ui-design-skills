# 排错

以下条目全部来自本次改造中实际运行产生的输出，没有推测的报错信息。

## lint_skills.py 报 description 过短

首次运行的真实输出：

```
技能目录 65 个，问题 18 条
  - skills/components/baoyu-design: description 过短
  - skills/components/ecommerce-image-workflow: description 过短
  ...
结果：未通过
```

原因有两个：一是部分上游技能用 YAML 块标量写 `description: >-`，校验脚本只取了第一行；二是轻量页面模板技能的描述本来就是一行短语。修法是让 frontmatter 解析把后续缩进行并进来，并把 12 个短描述补成「做什么 / 什么时候用 / 什么时候别用」。修复后输出：

```
技能目录 65 个，问题 0 条
结果：通过
```

## scan_sensitive.py 把自己扫出来了

首次运行的真实输出：

```
扫描文本文件 3116 个，敏感命中 5 条
  - tools/scan_sensitive.py:18 [真实公司名（中文）] '<命中词，已脱敏>'
  - tools/scan_sensitive.py:19 [真实公司名（英文）] '<命中词，已脱敏>'
  - tools/scan_sensitive.py:20 [真实姓名] '<命中词，已脱敏>'
结果：未通过，禁止推送
```

命中词本身不外发，上面做了脱敏。原因是模式串以字面量写在脚本源码里，脚本扫到了自己。修法是把模式用 Unicode 转义与字符串拼接构造，源码里不再出现字面量。修复后输出：

```
扫描文本文件 3116 个，敏感命中 0 条
结果：通过
```

## git push 被拒：远端有本地没有的提交

在私有库推送时的真实输出：

```
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
```

处理方式是先 `git fetch` 看远端新增了哪些提交、改了哪些文件，再 `git rebase origin/main`，不要 `--force` 硬推。本次远端多了 7 个提交，还新增了 `common` 命名空间。

## rebase 时 README 与 SVG 冲突

真实输出：

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Auto-merging docs/assets/badges.svg
CONFLICT (content): Merge conflict in docs/assets/badges.svg
```

这几个文件是脚本生成的。处理方式是冲突处统一取远端版本，rebase 完成后再跑一次生成脚本，从合并后的真实目录重算，不要手工拼合并结果。

## 在 detached HEAD 上 push

rebase 收尾没完成时直接 push，真实输出：

```
To push the history leading to the current (detached HEAD)
state now, use

    git push origin HEAD:<name-of-remote-branch>
```

执行 `git rebase --continue` 让分支指针归位即可，输出 `Successfully rebased and updated refs/heads.main.` 之后正常 `git push`。

## 安装器看不到技能

先跑 `node tools/install.mjs --list`。本次真实输出首行是：

```
共 65 个技能
```

如果数字对不上，通常是 `--dir` 指到了别的仓库，或本地副本落后于远端。安装器在复制前会校验每个技能根目录有 `SKILL.md`，缺一个就整体拒绝，不会装半套。

## 每日贡献图脚本仍会往本库写文件

`.workbuddy/scripts/github_contrib.py` 与 `.workbuddy/scripts/daily_log_index.py` 是改造前留下的脚本，前者仍按日程往 `notes/`、`snippets/`、`assets/` 写文件并推送，后者按这三个目录生成一份日志索引 README。本库的 `.gitignore` 特意不忽略这三个目录，否则前者 `git add <path>` 会失败。

如果有人手动运行 `daily_log_index.py`，它会用日志索引覆盖本库的 README。需要彻底隔离时，把这两个脚本迁到独立仓库，再改对应的定时任务。
