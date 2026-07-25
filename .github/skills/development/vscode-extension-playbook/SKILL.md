---
author: Alexa
description: Use when inventorying installed VS Code extensions, pairing them with Hermes workflows, and validating extension-specific editor behavior.
license: MIT
metadata:
  hermes:
    tags:
    - imported
    - development
    - vscode
    - extensions
    - audit
    - configuration
name: vscode-extension-playbook
tags:
- imported
- development
- vscode
- extensions
- audit
- configuration
- scripts
title: VS Code Extension Playbook
version: 1.3.0
---

# VS Code Extension Playbook

## Overview

Use this skill when you need to work with the installed VS Code extension set instead of guessing from memory. Provides a complete workflow for inventory, classification, conflict resolution, configuration generation, and verification.

## When to Use

- Listing installed extensions with versions
- Mapping extensions to the right Hermes skill or workflow
- Verifying the extension surface after changes
- Deciding whether a task should be done in VS Code or via terminal/skill
- Auditing extension coverage in a workspace or profile
- Resolving formatter/linter conflicts across extensions

## When NOT to Use

- Writing VS Code extension code (use `vscode-extension-playbook`)
- Designing UI/UX for web components (use `frontend-design`)
- General terminal operations unrelated to VS Code

## Workflow

### Phase 1: Inventory

```bash
# Check VS Code version
code --version

# List all installed extensions with versions
code --list-extensions --show-versions

# Record active profile if relevant
code --profile
```

### Phase 2: Classify

Group extensions by category:

| Category | Example Extensions |
|----------|-------------------|
| Python | `ms-python.python`, `ms-python.vscode-pylance`, `charliermarsh.ruff` |
| JS/TS | `dbaeumer.vscode-eslint`, `esbenp.prettier-vscode`, `bradlc.vscode-tailwindcss` |
| Git | `eamodio.gitlens`, `mhutchie.git-graph`, `github.vscode-pull-request-github` |
| Visual | `usernamehw.errorlens`, `naumovs.color-highlight`, `aaron-bond.better-comments` |
| Testing | `vitest.explorer`, `ms-playwright.playwright` |
| Data | `mechatroner.rainbow-csv`, `humao.rest-client`, `mtxr.sqltools` |
| Shell/Config | `foxundermoon.shell-format`, `editorconfig.editorconfig` |
| Theme | `pkief.material-icon-theme` |
| Runtime | `oven.bun-vscode`, `ms-vscode.powershell` |

### Phase 3: Analyze (Deduplicate & Conflict-Check)

- **Scan for functional overlap:** Two TODO-highlighters, two snippet packs for same framework, two formatters for same language
- **Scan for formatter conflicts:** `editor.defaultFormatter` or `[lang].editor.defaultFormatter` in settings must reference a single installed extension per language
- **Check for unmaintained extensions:** version <1.0.0, last update >2 years ago, or very low version number (e.g. v0.0.3)
- **Identify replacement candidates:**
  - Yarn-specific extensions → `oven.bun-vscode` when Bun is the package manager
  - Extension-specific TODO highlighting → `aaron-bond.better-comments` (superset)
  - Niche snippet packs → built-in TypeScript/React IntelliSense
  - Low-utility tools (code screenshot, single-purpose viewers) → built-in VS Code features or tool skills

Record removals in `references/extension-mapping.md` under a "Removed Extensions" table with reason + replacement.

### Phase 4: Pair

Use `references/extension-mapping.md` to pick the primary Hermes skill or workflow. If no direct skill exists, use the nearest fallback listed in the matrix.

### Phase 5: Research & Generate Extension Config

Before execute/configure, research each extension's configurable settings:

- **Marketplace URL pattern:** `https://marketplace.visualstudio.com/items?itemName={publisher}.{name}`
- **Fetch docs:** Use `web_extract` with batch size ≤7 URLs per call to get marketplace pages
- **Source known defaults:** Many well-known extensions (Prettier, GitLens, Ruff, ESLint, etc.) have well-documented settings
- **Extensions with no user settings:** Note in coverage matrix (commands-only extensions like Git History, snippet packs, theme-only extensions)

**Key pattern — Python Ruff integration:** When Ruff is installed alongside Pylance, configure Python's `editor.codeActionsOnSave` for both `source.fixAll.ruff` and `source.organizeImports.ruff` in the `[python]` language block (NOT at global `editor.codeActionsOnSave`) so Ruff handles linting/fixing while Pylance provides type analysis.

**Key pattern — markdown formatter:** Set `[markdown].editor.defaultFormatter` to `esbenp.prettier-vscode` with `editor.wordWrap: "on"`. The `yzhang.markdown-all-in-one` extension handles TOC/sections/shortcuts, not formatting. Without an explicit block, format-on-save behavior for markdown is unpredictable.

### Phase 6: Execute (Install / Uninstall / Configure)

```bash
# Install missing recommendations
code --install-extension <id>

# Uninstall redundant extensions
code --uninstall-extension <id>

# Update settings.json — add generated config blocks for each extension
# Remove config blocks for any removed extension

# Both scopes: Update user-default AND workspace settings
# User: ~/AppData/Roaming/Code/User/settings.json
# Workspace: .vscode/settings.json

# Sync extensions.json
# Add all installed extensions to recommendations
# Move removed ones to unwantedRecommendations

# Validate all JSON
python3 -m json.tool <file>
```

### Phase 7: Subproject Scan

```bash
# Find all nested .vscode directories
find <workspace>/projects -maxdepth 2 -name ".vscode" -type d

# Check for stale .vscode_bak directories — remove them
# For each, check settings.json for dead extension references
```

### Phase 8: Sync Workspace Recommendations

Update `.vscode/extensions.json`:
- Remove uninstalled extensions from `recommendations`
- Add newly installed extensions to `recommendations`
- Move removed extensions to `unwantedRecommendations`

### Phase 9: Verify

- [ ] Re-run `code --list-extensions --show-versions` and confirm diff matches expectations
- [ ] Confirm all `.vscode/*.json` files reference only installed extensions
- [ ] Confirm settings have no dead config blocks
- [ ] Validate JSON syntax of all modified files: `python3 -m json.tool <file>`
- [ ] Build a **coverage matrix** — map every installed extension to its config status
- [ ] Flag any extension without config as a gap
- [ ] Note discrepancies between plan assumptions and live inventory
- [ ] Confirm the extension behavior matches the task

## Verification Checklist

- [ ] Installed extension inventory captured with `code --list-extensions --show-versions`
- [ ] Each extension has a paired Hermes skill or explicit fallback workflow
- [ ] Duplicates and conflicts identified and resolved (no two extensions serving the same purpose)
- [ ] Unmaintained or superseded extensions removed (version <1.0.0, stale, replaced by built-in feature)
- [ ] Removed extensions documented in mapping's "Removed Extensions" table with reason + replacement
- [ ] Every installed extension has config status documented in a coverage matrix
- [ ] Both user-default and workspace settings.json updated with generated config blocks
- [ ] All `.vscode/settings.json` files (root + projects/*/.vscode/) reference only currently-installed extensions
- [ ] `.vscode/extensions.json` recommendations match the installed set (no stale recs, no missing recs)
- [ ] No dead config blocks in settings.json for removed extensions
- [ ] All modified JSON files pass `python3 -m json.tool` validation
- [ ] The chosen workflow was exercised, not just described
- [ ] Any extension-specific change was verified in VS Code or in output files
- [ ] No stale extension references remain in docs

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | Run VS Code CLI commands |
| `file` | Manage extension inventory files |
| `web_extract` | Fetch extension marketplace docs |
| `vscode-cli` | Control VS Code from terminal |

## Related Skills

- `vscode-cli` — VS Code CLI control
- `vscode-workspace-configurator` — Workspace JSON configuration
- `vscode-ext-commands` — Extension command reference

## Usage Examples

```bash
# Full audit workflow
vscode-extension-playbook --inventory
vscode-extension-playbook --analyze
vscode-extension-playbook --configure
vscode-extension-playbook --verify

# Dry run to see what would change
vscode-extension-playbook --dry-run

# Only check for formatter conflicts
vscode-extension-playbook --check-formatters
```

## Error Handling

- **Command not found:** `code` must be on PATH or called by full path — Exits with code 127
- **Extension not found:** `--install-extension` fails with code 1 if extension ID invalid
- **Permission denied:** User data dir access fails — Exits with code 2
- **Already running:** Some operations require VS Code to not be running — Use `--new-window` or kill existing
- **Windows `code` CLI:** On Windows, `code` is a shell script (`cmd` wrapper), not a native executable. Calling it from Python `subprocess.run()` fails with `FileNotFoundError`. Use the `terminal()` tool instead: `terminal("code --list-extensions --show-versions")`.

## Pitfalls

- UI-only extensions need visual verification, not just CLI confirmation
- Formatting and linting extensions can hide bad content; verify the file output, not the editor state
- Subproject `.vscode/settings.json` files frequently reference extensions that exist in a different profile or were removed — always scan nested `.vscode/` dirs across the full workspace after any extension change
- `.vscode/settings.json` config blocks for removed extensions silently bloat the file and can cause confusion (settings are parsed but ignored, not errored)
- `extensions.json` recommendations and actual installed set will drift over time — always check `code --list-extensions` against `extensions.json` recommendations when auditing
- When removing an extension, also check `settings.json` for `todohighlight`, `better-comments`, and other config keys — removing the extension alone leaves dead config behind
- Formatter conflicts in subproject settings are silent: VS Code picks the first matching formatter without warning. A subproject can accidentally override the workspace default formatter for a language with a formatter not installed on this machine
- Yarn-specific extensions (`gamunu.vscode-yarn`) should be removed when Bun is the package manager — they add UI surface for a non-operational workflow
- GH API extension references (`github.vscode-github-actions`, `github.vscode-pull-request-github`) are safe to keep even if `gh` CLI handles the bulk of GitHub operations — they provide UI surfaces the CLI can't
- Diagnostics extensions are support tools, not substitutes for tests
- Query and data extensions help inspect output; they do not replace domain validation

## References

- `references/extension-mapping.md` — Current installed extension inventory and paired skill/workflow
- `references/vscode-extension-config-patterns.md` — Known-good config patterns for popular extensions
- `references/marketplace-fetch.md` — Batch fetching extension docs from marketplace

## Templates

- `templates/extension-mapping.md` — Mapping table template
- `templates/coverage-matrix.md` — Coverage matrix template