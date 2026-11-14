# UI Design Skills

[中文](README.md) · English

A skill library for AI agents working on interface design: 67 skills in six categories, with over four thousand ready-to-use guidelines, templates, component sources and assets. Every skill is a standard `SKILL.md` directory that an agent can read and act on.

Coverage includes enterprise back-office UI, web UI and mobile UI, plus the components, icons, palettes, review rules and tooling behind them. Material is drawn from a private skill library, a public skill library and several public upstream projects, filtered for licensing and privacy.

## Layout

| Path | Contents | Skills |
|---|---|---:|
| [`skills/foundations/`](skills/foundations/) | Foundations & Review | 15 |
| [`skills/web/`](skills/web/) | Web UI | 20 |
| [`skills/enterprise/`](skills/enterprise/) | Enterprise UI | 6 |
| [`skills/mobile/`](skills/mobile/) | Mobile UI | 3 |
| [`skills/components/`](skills/components/) | Components & Assets | 17 |
| [`skills/tooling/`](skills/tooling/) | Tooling & Formats | 6 |

| [`references/`](references/) | Shared corpus: 84 design-system references, palette values, canvas spec | 171 files |
| [`docs/`](docs/) | Skill map, privacy and licensing, troubleshooting | 3 files |
| [`tools/`](tools/) | Installer and three checks | 4 files |

Start with [`ROUTER.md`](ROUTER.md) (phrased as "what you would say"), then [`docs/skill-map.md`](docs/skill-map.md) (the six stages of making an interface).

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

These are defaults and may change between releases; override with `--dir`. The repository can also be used as a plugin-marketplace source, and plugin manifests ship with the skill directories.

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

No real names or real company names appear in this public repository; `tools/scan_sensitive.py` scans the whole tree before every push. See [`docs/privacy-and-license.md`](docs/privacy-and-license.md).

Original content is Apache-2.0. Third-party material keeps its own license, listed per skill in [`THIRD-PARTY.md`](THIRD-PARTY.md), with exceptions in [`NOTICE`](NOTICE). Source-available or unclear skill documents are linked, not copied.

## Maintenance

```bash
python tools/lint_skills.py       # validate skill format
python tools/scan_sensitive.py    # sensitive-term scan
python tools/build_index.py       # regenerate the skill map
```

Counts are generated from `SKILL.md` files, never written by hand. Re-run `build_index.py` after renaming a skill or moving it between categories.

## Troubleshooting

See [`docs/troubleshooting.md`](docs/troubleshooting.md). Every item comes from an actual run.

## License

Apache-2.0, see [`LICENSE`](LICENSE). Third-party material follows the terms in `THIRD-PARTY.md`.
