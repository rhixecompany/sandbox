---
name: vscode-configuration
title: VSCode Configuration (Workspace + User)
description: Audit, fix, and align VS Code workspace and user settings. Covers terminal emulator integration, Ruff alignment between user/project, task/launch configs, extensions, formatters, and paths.
version: 1.0.0
tags:
- vscode
- ide
- configuration
- terminal
- audit
- ruff
---

# VSCode Configuration (Workspace + User)

## Overview

Audit, fix, and align **both** VS Code workspace (`.vscode/`) **and user** (`Code\User\`) settings. Covers terminal emulator (WezTerm), Ruff config alignment with project `.ruff.toml`, task problem matchers, launch debug configs, extensions, formatters, and hardcoded paths.

## When to Use

- Setting up a new workspace or onboarding a project
- Debugging IDE integration issues (terminal not opening, lint not matching CLI, extensions not activating)
- Periodic workspace hygiene
- Configuring a terminal emulator (WezTerm, etc.) as the default external terminal

## Audit Files

| Scope | Files |
|-------|-------|
| **Workspace** | `.vscode/settings.json`, `tasks.json`, `launch.json`, `extensions.json`, `mcp.json` |
| **User** | `Code\User\settings.json`, `Code\User\keybindings.json` |

**User path on Windows:** `C:\Users\<user>\AppData\Roaming\Code\User\settings.json`

## Audit Categories

### 1. Terminal Configuration
- **External terminal:** `terminal.external.windowsExec` should point to WezTerm or preferred emulator
- **Integrated profile:** `terminal.integrated.defaultProfile.windows` should be consistent between user + workspace
- **Emulator note:** WezTerm is a terminal EMULATOR, not a shell. Cannot be the `defaultProfile` (that expects a shell like bash/powershell). Add it as an external target and as a selectable profile:
  ```json
  "terminal.integrated.profiles.windows": {
    "WezTerm": {
      "icon": "terminal",
      "path": "C:\\Program Files\\WezTerm\\wezterm.exe",
      "args": ["start", "--cwd", "${workspaceFolder}"]
    }
  },
  "terminal.external.windowsExec": "C:\\Program Files\\WezTerm\\wezterm.exe start"
  ```

### 2. Ruff Config Alignment
- User `ruff.lineLength` must match `.ruff.toml` (project likely uses 120)
- User `ruff.lint.select` must include all codes from `.ruff.toml` (B, SIM, ARG, RUF are commonly missing)
- **Why it matters:** User settings override CLI `.ruff.toml` in VSCode — mismatches cause different lint results in editor vs terminal

### 3. Tasks
- Missing `problemMatcher` → pytest output not parsed as test results, ruff output not shown inline
  - `python -m pytest` → `$python.pytest`
  - `ruff check .` → `$ruff`
  - `eslint ...` → `$eslint-stylish`
- Missing `options.cwd` at tasks.json root → tasks run from last active directory
  ```json
  "options": { "cwd": "${workspaceFolder}" }
  ```

### 4. Launch (Debug) Configs
- Python debug: missing `justMyCode`, explicit `python` path, `cwd`
- Bun/Node debug: missing `cwd`

### 5. Extensions
- Baseline: prettier, python+pylance, eslint, ruff, markdownlint, shell-format, errorlens, bun
- Multi-stack additions: YAML (`redhat.vscode-yaml`), spellcheck (`streetsidesoftware.code-spell-checker`), shellcheck (`timonwong.shellcheck`), Docker (`ms-azuretools.vscode-docker`), Mermaid (`bierner.markdown-mermaid`), GitLens (`eamodio.gitlens`)

### 6. Formatters
- Verify single formatter per language — no conflicts
- Global default: `esbenp.prettier-vscode`
- Python: `ms-python.python`
- HTML: `vscode.html-language-features`
- JSON/JSONC: `vscode.json-language-features`
- Shell: `foxundermoon.shell-format`

### 7. Paths
- No hardcoded `C:\Users\...` or `/home/...` paths
- Use `${workspaceFolder}` for workspace-relative paths

### 8. Deprecated Settings (User)
- `python.languageServer` → removed, use Pylance via extension
- `python.linting.enabled` / `python.linting.ruffEnabled` / `python.formatting.provider` → removed, use `ruff.*` settings

## Workflow

### Phase 1: Read All Files
Use `read_file` on each config file in both scopes.

### Phase 2: Run Checks
Write a Python verification script that checks each category, or run checks individually:
```python
import json
for fn in ["settings.json","tasks.json","launch.json","extensions.json","mcp.json"]:
    json.load(open(f".vscode/{fn}"))
```

### Phase 3: Apply Fixes
Patch each file individually. For JSON files with multiple changes, use `write_file` to avoid accumulating indentation issues from `patch`.

### Phase 4: Verify
Write a combined verification script covering:
- All 5 workspace JSON files parse
- User settings JSON parses
- Terminal consistency check
- Ruff alignment check
- Extensions completeness check

## Common Pitfalls

- **`patch` tool corrupts list markers** on `.md` files (turns `- ` into `|- `). Always verify markdown integrity after patching.
- **WezTerm cannot be `defaultProfile`** — it's an emulator, not a shell. Use `external.windowsExec` instead.
- **User ruff settings can diverge** from project `.ruff.toml`. This silently changes lint results in VSCode vs CLI.
- **Deprecated settings still appear** in user configs from older VSCode versions. Check for `python.linting.*`, `python.languageServer`, `python.formatting.*`.
- **Workspace `[python]` section** can duplicate user `[python]` section. Check both.
- **VSCode MCP extension** (`github.vscode-copilot-mcp`) uses `mcp.json` with `inputs` pattern that doesn't auto-resolve `${workspaceFolder}` — use explicit paths or env vars.

## Related Skills

- `vscode-config-audit` — narrower workspace-only audit (overlaps with this skill)
- `vscode-workspace-configurator` — generate configs from scratch
- `vscode-ext-commands` — manage extensions
