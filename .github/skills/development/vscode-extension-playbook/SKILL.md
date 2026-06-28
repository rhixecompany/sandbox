---
author: Alexa
description: Use when inventorying installed VS Code extensions, pairing them with
  Hermes workflows, and validating extension-specific editor behavior.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: vscode-extension-playbook
tags:
- imported
title: VS Code Extension Playbook
version: 1.1.0

---
# VS Code Extension Playbook

## Purpose

Use this skill when you need to work with the installed VS Code extension set instead of guessing from memory.

## When to use

- Listing installed extensions
- Mapping extensions to the right Hermes skill or workflow
- Verifying the extension surface after changes
- Deciding whether a task should be done in VS Code or via terminal/skill
- Auditing extension coverage in a workspace or profile

## Workflow

### 1) Inventory

- Run `code --version`
- Run `code --list-extensions --show-versions`
- Record the active profile if relevant

### 2) Classify

- Group extensions by docs, frontend, Git, Python, testing, HTTP, data, or utilities

### 3) Analyze (deduplicate & conflict-check)

- Scan for functional overlap: two TODO-highlighters, two snippet packs for same framework, two formatters for same language.
- Scan for formatter conflicts: `editor.defaultFormatter` or `[lang].editor.defaultFormatter` in settings must reference a single installed extension per language. If two formatters target the same language, pick one and remove the other.
- Check for unmaintained extensions: version <1.0.0, last update >2 years ago, or very low version number (e.g. v0.0.3). These can often be replaced by built-in VS Code features or a more current alternative.
- Identify obvious replacement candidates:
  - Yarn-specific extensions → `oven.bun-vscode` when Bun is the package manager
  - Extension-specific TODO highlighting → `aaron-bond.better-comments` (superset)
  - Niche snippet packs → built-in TypeScript/React IntelliSense
  - Low-utility tools (code screenshot, single-purpose viewers) → built-in VS Code features or tool skills
- Record removals in `references/extension-mapping.md` under a "Removed Extensions" table with reason + replacement.

### 4) Pair

- Use `references/extension-mapping.md` to pick the primary Hermes skill or workflow
- If no direct skill exists, use the nearest fallback listed in the matrix

### 5) Execute (install / uninstall / configure)

- Install missing recommendations: `code --install-extension <id>`
- Uninstall redundant extensions: `code --uninstall-extension <id>`
- Update `.vscode/settings.json` — remove config blocks for any removed extension
- Use the extension in VS Code and the paired Hermes skill for the actual task

### 6) Subproject scan

- Run `find <workspace>/projects -maxdepth 2 -name ".vscode" -type d` to locate all nested `.vscode/` directories
- Also check for stale `.vscode_bak` directories — remove them (they contain broken JSON from old backups)
- For each, check `settings.json` for `editor.defaultFormatter`, `[lang].editor.defaultFormatter`, and any extension-specific config keys referencing extensions that were removed or are not installed in this profile
- Fix stale references — if the referenced extension is gone, change to an installed equivalent (e.g. `charliermarsh.ruff` → `ms-python.python` for Python formatting; `foxundermoon.shell-format` → `esbenp.prettier-vscode` for dotenv/ignore)
- Remove JS-in-JSON comments from subproject settings if present (VS Code tolerates them but they aren't valid JSONC)
- Ensure `terminal.integrated.profiles.windows` is defined in root settings (PowerShell, CMD, Git Bash)

### 7) Sync workspace recommendations

- Update `.vscode/extensions.json`:
  - Remove any uninstalled extensions from `recommendations`
  - Add any newly installed extensions to `recommendations`
  - Move removed extensions to `unwantedRecommendations` for team consistency (when applicable)

### 8) Verify

- Re-run `code --list-extensions --show-versions` and confirm the diff matches expectations
- Confirm all `.vscode/*.json` files reference only installed extensions
- Confirm settings have no dead config blocks
- Confirm the extension behavior matches the task

## Usage rules

- Treat extension names as capabilities, not proof of suitability.
- Prefer a direct Hermes skill when one exists.
- Use VS Code UI for extension-specific behavior; use terminal for reproducible setup.
- Do not assume an extension is the only tool needed.
- If an extension has no direct skill, use the documented fallback workflow instead of inventing one.

## Coverage matrix

- See `references/extension-mapping.md` for the current installed extension inventory and its paired skill or workflow.
- Refresh the matrix whenever `code --list-extensions --show-versions` changes.

## Pitfalls

- UI-only extensions need visual verification, not just CLI confirmation.
- Formatting and linting extensions can hide bad content; verify the file output, not the editor state.
- Subproject `.vscode/settings.json` files frequently reference extensions that exist in a different profile or were removed — always scan nested `.vscode/` dirs across the full workspace after any extension change.
- `.vscode/settings.json` config blocks for removed extensions silently bloat the file and can cause confusion (settings are parsed but ignored, not errored).
- `extensions.json` recommendations and actual installed set will drift over time — always check `code --list-extensions` against `extensions.json` recommendations when auditing.
- When removing an extension, also check `settings.json` for `todohighlight`, `better-comments`, and other config keys — removing the extension alone leaves dead config behind.
- Formatter conflicts in subproject settings are silent: VS Code picks the first matching formatter without warning. A subproject can accidentally override the workspace default formatter for a language with a formatter not installed on this machine.
- Yarn-specific extensions (`gamunu.vscode-yarn`) should be removed when Bun is the package manager — they add UI surface for a non-operational workflow.
- GH API extension references (`github.vscode-github-actions`, `github.vscode-pull-request-github`) are safe to keep even if `gh` CLI handles the bulk of GitHub operations — they provide UI surfaces the CLI can't.
- Diagnostics extensions are support tools, not substitutes for tests.
- Query and data extensions help inspect output; they do not replace domain validation.
- **Windows `code` CLI from Python subprocess**: On Windows, `code` is a shell script (`cmd` wrapper), not a native executable. Calling it from Python `subprocess.run()` fails with `FileNotFoundError`. Use the `terminal()` tool instead: `terminal("code --list-extensions --show-versions")`.

## Verification checklist

- [ ] Installed extension inventory captured with `code --list-extensions --show-versions`
- [ ] Each extension has a paired Hermes skill or explicit fallback workflow
- [ ] Duplicates and conflicts identified and resolved (no two extensions serving the same purpose)
- [ ] Unmaintained or superseded extensions removed (version <1.0.0, stale, replaced by built-in feature)
- [ ] Removed extensions documented in mapping's "Removed Extensions" table with reason + replacement
- [ ] All `.vscode/settings.json` files (root + projects/*/.vscode/) reference only currently-installed extensions
- [ ] `.vscode/extensions.json` recommendations match the installed set (no stale recs, no missing recs)
- [ ] No dead config blocks in settings.json for removed extensions
- [ ] The chosen workflow was exercised, not just described
- [ ] Any extension-specific change was verified in VS Code or in output files
- [ ] No stale extension references remain in docs
