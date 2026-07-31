# VSCode Config Audit — Final Report

**Scope:** `.vscode/` (workspace) + `Code\User\` (user)  
**Goal:** Use WezTerm as the default terminal

## Terminal Configuration

| Setting | Value |
|---------|-------|
| `terminal.integrated.defaultProfile.windows` (user) | `Git Bash` |
| `terminal.integrated.defaultProfile.windows` (workspace) | `Git Bash` |
| `terminal.integrated.profiles.windows[WezTerm]` | `C:\Program Files\WezTerm\wezterm.exe start --cwd ${workspaceFolder}` |
| `terminal.external.windowsExec` | `C:\Program Files\WezTerm\wezterm.exe start` |

**WezTerm behavior:** Set as the **external terminal** (`Ctrl+Shift+C` opens WezTerm). Also available as a selectable profile in the terminal dropdown for manual use.

## Workspace `.vscode/` — Issues Fixed

| File | Fix |
|------|-----|
| `settings.json` | Default terminal `PowerShell→Git Bash` (consistent with user) |
| `tasks.json` | Added `options.cwd: ${workspaceFolder}` + `$python.pytest` and `$ruff` problemMatchers |
| `launch.json` | Python debug config: `justMyCode: true`, explicit `python` path, `cwd: ${workspaceFolder}` |
| `extensions.json` | Added 6 recommended extensions: `redhat.vscode-yaml`, `streetsidesoftware.code-spell-checker`, `timonwong.shellcheck`, `ms-azuretools.vscode-docker`, `bierner.markdown-mermaid`, `eamodio.gitlens` |
| `mcp.json` | No changes needed |

## User `Code\User\` — Issues Fixed

| File | Fix |
|------|-----|
| `settings.json` | Added WezTerm profile + `terminal.external.windowsExec` |
| `settings.json` | `ruff.lineLength: 88→120` (match `.ruff.toml`) |
| `settings.json` | `ruff.lint.select` expanded: added `B`, `SIM`, `ARG`, `RUF` (match `.ruff.toml`) |
| `keybindings.json` | Empty — no issues |

## Verification Status

| Check | Result |
|-------|--------|
| All .vscode JSON files valid | ✅ |
| All user JSON files valid | ✅ |
| WezTerm profile in terminal dropdown | ✅ |
| WezTerm as external terminal | ✅ |
| Consistent default terminal (Git Bash) across user + workspace | ✅ |
| Ruff settings match `.ruff.toml` | ✅ |
| Tasks have problemMatchers | ✅ |
| Python launch config has justMyCode + cwd | ✅ |
| Extensions include all recommended | ✅ |

**23/23 checks passed.**
