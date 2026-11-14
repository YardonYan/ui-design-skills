# UI Design Skills

[中文](README.md) · English

A skill library for AI agents working on interface design. 67 skills in six categories, 4332 files in total, each skill a standard `SKILL.md` directory that an agent can read and act on.

Coverage spans web UI, enterprise back-office UI, mobile UI and AI chat interfaces, plus the components, icons, palettes, interaction rules and review criteria behind them. Material comes from a private skill library, a public skill library and several public upstream projects, filtered for licensing and privacy before inclusion.

## Repository history

This repository was originally named daily-log and held daily technical notes, code snippets and hand-drawn figures. On 2026-11-15 it was converted into a dedicated UI design skill library and renamed ui-design-skills.

| Item | Current state |
|---|---|
| Old URL | `github.com/YardonYan/daily-log` redirects automatically to the new address; old links keep working |
| Commit history | Pre-conversion history fully preserved, no history rewrite, contribution graph unaffected |
| Local working copy | The directory is still named daily-log because the daily contribution script writes to that path |
| Log-style commits | The script still produces a few commits under `notes/`, `snippets/` and `assets/`; these are legacy, not skill content |

Moving contribution commits to a separate repository means changing the script and its schedule, not this library. See `docs/troubleshooting.md`.

## What this is and is not

| Is | Is not |
|---|---|
| Instructions, rules, templates and assets for AI agents | An installable npm component library |
| Skill directories organised by the task at hand | A tutorial site arranged by framework |
| HTML, TSX, SVG and palette values ready to copy | An archive of mockups or screenshots |
| Public material with provenance and licence records | A full copy of anyone's private knowledge base |

The boundary is simple: if the output is a web page or an interface, it belongs in these six categories; if the output is a Word, PDF or PPT file, it is out of scope.

## Quick start

1. Find a skill. Start with `ROUTER.md`, indexed by what you would say, then `docs/skill-map.md`, arranged along the six stages of making an interface.
2. Install it. Use `tools/install.mjs` to copy it into your agent's skills directory, or point `--dir` anywhere you like.
3. Use it. Hand the skill's `SKILL.md` to the agent, then let it read `references/` and `templates/` when it needs rules or a starting file.

Example: for an AI chat interface with tool-call approval, use `ai-chat-patterns` to enumerate states, `assistant-ui` to implement the components, and `web-design-guidelines` to review the result.

## Six categories

| Category | Scope | Skills | Typical request | Representative skills |
|---|---|---:|---|---|
| `foundations` | Direction, specs, colour, branding, interaction states, review | 15 | Remove the AI look, pick a palette, list chat states | `oil-ui`, `unslop`, `flexoki-palette`, `ai-chat-patterns` |
| `web` | Public-facing pages and page types | 20 | Build a landing page, pricing page, docs site, clone a site | `saas-landing`, `pricing-page`, `docs-page`, `web-clone` |
| `enterprise` | Back office, forms, information architecture, dashboards | 6 | Build a full admin, turn fields into a validated Schema | `enterprise-admin`, `admin-form-schema`, `admin-ia-patterns` |
| `mobile` | App screens, onboarding, multi-platform dimensions | 3 | Render one app screen, look up platform specs | `mobile-app`, `mobile-design-spec` |
| `components` | Components, blocks, icons, illustrations, charts, chat UI | 17 | Need motion component source, a full icon set, chat components | `cult-ui`, `ricoui-blocks`, `icon-system`, `assistant-ui` |
| `tooling` | Debugging, conversion, canvas formats, delivery | 6 | Debug in the browser, HTML to PDF, read canvas data | `chrome-devtools`, `html-to-pdf`, `json-canvas` |

## Contents

| Path | Contents | Count |
|---|---|---:|
| `skills/` | 67 skills in the six categories above | 67 skill directories |
| `references/` | Shared corpus: 84 design-system references, Flexoki values, JSON Canvas spec | 174 files |
| `docs/` | Skill map, privacy and licensing, troubleshooting | 3 files |
| `tools/` | Installer and three checks | 4 files |

4332 files in total. Inside a skill, `SKILL.md` is the entry point, `SOURCE.md` and `CONTRIBUTORS` record provenance, and the remaining directories hold rules, templates and assets.

## Provenance

| Source | What was included | Licence |
|---|---|---|
| Private skill library | Page recipes, back-office structures, components, icons, review rules | Original work Apache-2.0, third-party items attributed individually |
| `YardonYan/for-my-self-skills` | Single-file HTML, mobile dimensions, Markdown fixes, conversion tooling | Apache-2.0 |
| `assistant-ui/assistant-ui` | Chat UI docs, API declarations, component source, starter templates | MIT |
| `kubai087/kubai-icons` | Icon definitions, badges, construction kit | MIT, icons portion only |
| `ricocc/ricoui-blocks` | Motion blocks and design docs | MIT |
| `kepano/flexoki`, `obsidianmd/jsoncanvas` | Palette values and canvas spec | MIT |
| Design corpus | DESIGN.md references for 84 products | MIT |

Per-skill sources, licences and inclusion notes are in `THIRD-PARTY.md`. Source-available skill documents and third-party skills with unclear terms are linked, not copied.

## Install

Zero dependencies, Node 18 or newer, no npm install required:

```bash
node tools/install.mjs --list
node tools/install.mjs --skill saas-landing --ai workbuddy
node tools/install.mjs --skill all --ai workbuddy --dry-run
```

| Flag | Effect |
|---|---|
| `--list` | List every skill and category |
| `--skill <name>` / `--skill all` | Pick one skill or all |
| `--ai <id>` / `--ai all` | Install into one assistant or all configured assistants |
| `--project` | Install into the current project instead of the user-level directory |
| `--dir <path>` | Explicit target directory, overrides the `--ai` default |
| `--dry-run` | Print planned copies without writing |
| `--force` | Overwrite an existing target |
| `--uninstall` | Remove skills installed from this library |

The installer refuses to copy anything unless every selected skill has `SKILL.md` at its root.

## Where it works

Domestic tools first (usable without a proxy in mainland China), then international tools (usually need outbound access).

| Assistant | `--ai` id | Default user-level directory |
|---|---|---|
| WorkBuddy | `workbuddy` | `~/.workbuddy/skills/` |
| CodeBuddy | `codebuddy` | `~/.codebuddy/skills/` |
| TRAE CN | `trae-cn` | `~/.trae-cn/skills/` |
| Qoder | `qoder` | `~/.qoder/skills/` |
| Qwen Code | `qwen-code` | `~/.qwen/skills/` |
| OpenClaw | `openclaw` | `~/.openclaw/skills/` |
| Claude Code | `claude` | `~/.claude/skills/` |
| Codex | `codex` | `~/.codex/skills/` |
| Cursor | `cursor` | `~/.cursor/skills/` |

These are defaults and may change between releases; override with `--dir`.

To install from a plugin marketplace, add this repository to your assistant's marketplace list. Four manifests ship at the repository root: `.claude-plugin/`, `.codebuddy-plugin/`, `.codex-plugin/` and `.cursor-plugin/`.

```bash
claude plugin marketplace add YardonYan/ui-design-skills
```

Not applicable: browser IDEs, cloud shells and online notebooks. Skills are instruction files for an agent, not a runnable app; those environments have no loader. To get a working interface, take the templates into your own project.

## Skill format

Each skill directory has at least `SKILL.md`. The YAML frontmatter requires `name` and `description`, and `name` must equal the directory name. `description` states three things: what it does, when to use it and when not to. Optional fields include `category`, `zh_name`, `en_name`, `tags`, `version` and `license`.

```
skills/<category>/<skill>/
  SKILL.md          entry point, required
  SOURCE.md         provenance and license record
  CONTRIBUTORS      upstream attribution
  references/       rules, specs, corpus
  templates/        editable templates
  assets/           icons, samples, config
  scripts/          checks and generators
```

`tools/lint_skills.py` verifies these rules. Run it after changing a skill.

## Privacy and licensing

No real names or real company names appear in this public repository; `tools/scan_sensitive.py` scans the whole tree before every push. Public upstream credits and copyright notices are kept because their licences require it; see `docs/privacy-and-license.md`.

Original content is Apache-2.0. Third-party material keeps its own license, listed per skill in `THIRD-PARTY.md`, with exceptions in `NOTICE`. The 34 skills whose licence could not be verified and the 2 skills that declare a LICENSE.txt but ship without it are listed separately in the pending-verification section of `THIRD-PARTY.md` rather than hidden behind a generic "see upstream".

## Maintenance

```bash
python tools/lint_skills.py       # validate skill format
python tools/scan_sensitive.py    # sensitive-term scan
python tools/build_index.py       # regenerate the skill map
```

Counts are generated from `SKILL.md` files, never written by hand. Re-run `build_index.py` after renaming a skill or moving it between categories.

## Troubleshooting

See `docs/troubleshooting.md`. Every item comes from an actual run, not a guessed error message.

## Changelog

| Date | Change |
|---|---|
| 2026-11-15 | Converted from a daily notes repository into a UI design skill library: 67 skills in six categories, old content removed in a normal commit, history preserved |
| 2026-11-15 | Added the assistant-ui component library and the AI chat interaction spec, 65 to 67 skills |
| 2026-11-15 | Renamed to ui-design-skills; About description, topics and this document rewritten for the new purpose |

## License

Apache-2.0, see `LICENSE`. Third-party material follows the terms in `THIRD-PARTY.md`.
