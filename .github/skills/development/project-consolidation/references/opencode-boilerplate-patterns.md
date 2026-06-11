# OpenCode Scaffolding — Detection Patterns

When cleaning up a repo that was imported or scaffolded from an OpenCode dotfiles setup, watch for these telltale signs:

## High-Confidence Signals (present = OpenCode boilerplate)

| Signal | What to look for | Example |
|---|---|---|
| **`docs/` with agent docs** | Subdirectories like `docs/01-core/`, `docs/02-languages/`, `docs/03-infrastructure/` each with `.md` files | `docs/01-core/backend-developer.md` |
| **CONTRIBUTING.md links to jjmartres/opencode** | `github.com/jjmartres/opencode` in the opening paragraphs | "We use GitHub Issues to track bugs" |
| **Makefile with stow** | `STOW_DIR := opencode`, makes `~/.config/opencode` the target | Targets: install, restow, uninstall |
| **`.stowrc` file** | Config for GNU Stow, usually empty or with single option | `--target=$HOME/.config/opencode` |
| **`opencode-logo.png`** | PNG file in project root, OpenCode branding | Usually around 14KB |
| **`.pre-commit-config.yaml`** | References `jjmartres/opencode`, hooks without working `.pre-commit-hooks.yaml` | Repo-level hook config from dotfiles |

## Medium-Confidence Signals (often accompany OpenCode)

| Signal | Notes |
|---|---|
| **`.markdownlint.yaml`** | Often a duplicate of `.markdownlint.json` — check which one `package.json` scripts reference |
| **Project context file referencing agents** | Content describing "01-core", "02-languages" agents (not the project's own context — check body content) |
| **`updated_readmes/` directory** | Draft READMEs for portfolio repos, named like `ecom_README.md` |
| **Sample CSV with headers + 1 row** | `application-tracker.csv` with just headers and a dummy row |
| **Root-level `.md` files unrelated to project** | `interview-qa.md`, `linkedin-guide.md`, `search-keywords.md` in root (likely generated outputs) |

## Cleanup Decision Tree

```
File matches OpenCode pattern?
├── Yes — is it referenced by package.json, tsconfig.json, or index.ts?
│   ├── No  → DELETE (dead scaffolding)
│   └── Yes → KEEP (repurposed for this project)
└── No — treat as project-native file
```

## Removal Commands

```bash
# Remove common OpenCode boilerplate artifacts
# These are files from the original scaffold that have no project references
rm docs/CONTRIBUTING.md  # if it references jjmartres/opencode
```

> **Note**: The `Makefile` from OpenCode typically references `opencode/` directory, `.stowrc`, and pre-commit — none of which survive a clean import. Always check `package.json` scripts before removing a `Makefile` — if `make` targets aren't referenced by `bun run` or `npm run`, it's dead code.
