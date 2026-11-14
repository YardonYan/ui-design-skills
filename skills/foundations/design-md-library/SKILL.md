---
name: design-md-library
description: 84 家网站的设计语言分析库（DESIGN.md）查询入口。当需要具体视觉 token 而不是形容词时使用：定落地页/后台/品牌页的配色与字号、要"像 Linear 那样""Airbnb 那种暖白+单一品牌色"的效果、给现有页面做视觉升级、判断某品牌的圆角/间距/字重取值、写 DESIGN.md 时需要对照结构。语料在 ~/.teamai/docs/design-md/<品牌>/DESIGN.md，来自 VoltAgent/awesome-design-md。关键词：设计语言、DESIGN.md、配色 token、字体搭配、参考站风格、视觉基线。
---

# 设计语言库（84 个 DESIGN.md）

## 什么时候用它

要的是**可写进 CSS 的具体值**，不是"高级感""简洁"这类形容词。典型：做落地页要定色板和字阶、要复刻某个产品的视觉气质、给现有页面做视觉升级、给项目写 DESIGN.md 需要参照结构。

## 怎么查

```bash
ls ~/.teamai/docs/design-md              # 看有哪些品牌
cat ~/.teamai/docs/design-md/linear.app/DESIGN.md   # 每个文件 400-550 行
```

每个 `DESIGN.md` 的 frontmatter 是结构化 token（`colors:` / 字体与字阶 / `rounded:` / 间距），正文是这套语言为什么这样组织的解释。

**硬规矩**：不许凭记忆写某品牌的色值、字号、圆角。要用就打开文件读，并在结论里给出文件路径。记忆里的 "Stripe 是紫色" 这类印象一律不算依据。

## 84 个条目按用途分组

- 开发者工具与后台：`linear.app` `clickhouse` `supabase` `sentry` `vercel` `raycast` `warp` `opencode.ai` `cursor` `figma` `framer` `webflow` `sanity` `mintlify` `miro` `posthog` `resend` `composio` `mongodb` `hashicorp` `oracle` `sap` `dell-1996` `hp` `ibm`
- AI 与模型：`claude` `mistral.ai` `ollama` `runwayml` `cohere` `minimax` `elevenlabs` `x.ai` `together.ai` `replicate` `lovable` `superhuman` `jobright`
- 消费与金融：`airbnb` `uber` `pinterest` `spotify` `stripe` `coinbase` `revolut` `mercury` `wise` `kraken` `mastercard` `binance` `1win` `mintlify` `cal` `notion` `slack` `intercom`
- 汽车与硬件：`tesla` `bmw` `bmw-m` `bugatti` `lamborghini` `renault` `ferrari` `spacex` `nvidia` `apple` `dji` `oura` `nintendo-2001`
- 媒体与零售：`aljazeera` `theverge` `wired` `nike` `starbucks` `shopify` `playstation` `vodafone` `mydealz` `nerdwallet` `airtable` `clay` `zapier` `expo` `meta` `voltagent` `webflow`

选参照对象要跨组挑两三个对照，别只看一个站就定色板。

## 与同仓其它设计 skill 的分工

- 要**选型和数据**（79 风格 / 192 配色 / 74 字体搭配 / UX 规则）→ `ui-ux-pro-max`
- 要**反 AI-slop 的底线和审查清单** → `hallmark`、`web-design-guidelines`、`review-animations`
- 要把"我喜欢的感觉"落成可复用契约 → `reference-design-contract`
- 要**真实品牌的现成 token 取值** → 本库

四者不互相替代：本库提供的是别人已经付过学费的具体数值，不是方法论。

## 加新品牌

在 `~/.teamai/docs/design-md/<品牌>/DESIGN.md` 按同样的 frontmatter 结构写，或从 https://getdesign.md/<品牌>/design-md 取，然后 `teamai push`（docs 走仓库 `docs/` 目录，`teamai pull` 下发到各机器）。

上游：`https://github.com/VoltAgent/awesome-design-md`，许可见 `docs/design-md-LICENSE`；本库是它的快照副本，2026-10-26 收录 84 条。
