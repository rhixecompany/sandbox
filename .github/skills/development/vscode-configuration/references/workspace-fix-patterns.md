# VSCode Workspace Config Fixes (Tasks, Launch, Extensions)

Reference patterns from 2026-07-24 audit session.

## tasks.json — Fixed Structure

```json
{
  "version": "2.0.0",
  "options": {
    "cwd": "${workspaceFolder}"
  },
  "tasks": [
    {
      "command": "python -m pytest",
      "label": "Python: Test All",
      "type": "shell",
      "group": "test",
      "problemMatcher": "$python.pytest",
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    },
    {
      "command": "ruff check .",
      "label": "Python: Lint",
      "type": "shell",
      "group": "build",
      "problemMatcher": "$ruff",
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    }
  ]
}
```

**Changes from baseline:**
- Added `options.cwd` at root (tasks run from workspace root, not last active directory)
- Added `problemMatcher: "$python.pytest"` on pytest task (test output parsed as test results)
- Added `problemMatcher: "$ruff"` on ruff task (lint warnings shown inline)

## launch.json — Fixed Python Debug Config

```json
{
  "name": "Python: Current File",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal",
  "justMyCode": true,
  "python": "${workspaceFolder}/myvenv/Scripts/python.exe",
  "cwd": "${workspaceFolder}"
}
```

**Changes from baseline:**
- `justMyCode: true` — skip library frames by default
- `python: "${workspaceFolder}/myvenv/Scripts/python.exe"` — explicit venv path
- `cwd: "${workspaceFolder}"` — working directory

## extensions.json — Recommended Extension Set

```json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "batisteo.vscode-django",
    "bradlc.vscode-tailwindcss",
    "dbaeumer.vscode-eslint",
    "oven.bun-vscode",
    "foxundermoon.shell-format",
    "usernamehw.errorlens",
    "charliermarsh.ruff",
    "davidanson.vscode-markdownlint",
    "redhat.vscode-yaml",
    "streetsidesoftware.code-spell-checker",
    "timonwong.shellcheck",
    "ms-azuretools.vscode-docker",
    "bierner.markdown-mermaid",
    "eamodio.gitlens"
  ],
  "unwantedRecommendations": [
    "ms-vscode.vscode-typescript-tslint-plugin",
    "hookyqr.beautify"
  ]
}
```

**Added:**
- `redhat.vscode-yaml` — for GitHub Actions, MCP configs
- `streetsidesoftware.code-spell-checker` — matches cspell MCP server
- `timonwong.shellcheck` — shell script lint
- `ms-azuretools.vscode-docker` — Docker support
- `bierner.markdown-mermaid` — Mermaid diagram preview
- `eamodio.gitlens` — Git history/blame

## Verification Script Template

```python
#!/usr/bin/env python3
import json, sys, os

errors = 0
def check(name, ok):
    global errors
    print(f"  {'PASS' if ok else 'FAIL'} {name}")
    if not ok: errors += 1

# Workspace files
for fn in ["settings.json","tasks.json","launch.json","extensions.json","mcp.json"]:
    with open(f".vscode/{fn}") as f:
        json.load(f)
check("All .vscode JSON files valid", True)

# User settings
with open(r"C:\Users\Alexa\AppData\Roaming\Code\User\settings.json") as f:
    u = json.load(f)

# Terminal consistency
with open(".vscode/settings.json") as f:
    w = json.load(f)
check("Terminal profiles match",
      u.get("terminal.integrated.defaultProfile.windows") ==
      w.get("terminal.integrated.defaultProfile.windows"))

# Ruff alignment
check("ruff.lineLength matches .ruff.toml",
      u.get("ruff.lineLength") == 120)
codes = set(u.get("ruff.lint.select", []))
for code in ["B","SIM","ARG","RUF"]:
    check(f"ruff includes {code}", code in codes)

# Extensions — all 17 present
with open(".vscode/extensions.json") as f:
    e = json.load(f)
check("extensions count >= 17", len(e["recommendations"]) >= 17)

sys.exit(0 if errors == 0 else 1)
```
