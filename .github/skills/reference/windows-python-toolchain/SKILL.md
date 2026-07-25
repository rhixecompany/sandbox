---
name: windows-python-toolchain
title: "Windows Python Toolchain Reference"
description: "Quirks and workarounds for Python linting/type-checking/MCP tooling on Windows."
version: 1.0.0
author: "Hermes Agent"
tags: [reference, windows, python, toolchain, pyright, mcp, vscode]
---

# Windows Python Toolchain Reference

## When to Use

- Setting up Python linting/type-checking on Windows
- Debugging subprocess failures when Python tools don't work from MCP servers
- Debugging VSCode settings warnings on Windows
- Testing MCP servers locally on Windows

## `python` vs `python3`

On Windows, `python3` is NOT a valid command — use `python`.

| Context | Use | Don't Use |
|---------|-----|-----------|
| VSCode tasks.json | `"command": "python -m pytest"` | `"command": "python3 -m pytest"` |
| Python subprocess | `subprocess.run(["python", ...])` | `subprocess.run(["python3", ...])` |
| Git Bash terminal | `python` | `python3` |

## `pyright` vs `pyright.cmd`

The `pyright` npm package installs multiple entry points. Only `pyright.cmd` works in subprocess calls:

| File | Type | Subprocess | 
|------|------|-----------|
| `pyright` | POSIX shell script | ❌ `[WinError 193]` |
| `pyright.cmd` | Windows cmd | ✅ |
| `pyright.ps1` | PowerShell | ❌ |

When calling pyright from Python subprocess, resolve to `.cmd`:

```python
import shutil
pyright = shutil.which("pyright.cmd") or shutil.which("pyright") or "pyright"
```

## MCP Server Registration

On Windows, `hermes config set` has limited YAML list support — setting `args.0` creates a mapping, not a list. Workaround: use a `.bat` wrapper.

```bat
@"C:\path\to\python.exe" "C:\path\to\mcp_server.py" %*
```

Register as: `command: "C:\path\to\wrapper.bat"` with no `args`.

For JSON arguments in MCP protocol tests, use forward slashes:
```
C:/Users/Alexa/Desktop/SandBox    # ✅ works
C:\\Users\\...                     # ❌ JSON escape errors
```

## Deprecated VSCode Settings

These generate warnings in VS Code settings UI:

| Setting | Fix |
|---------|-----|
| `python.languageServer: "Pylance"` | Remove — auto-detected |
| `python.linting.enabled: true` | Remove — Ruff extension handles this |
| `python.linting.ruffEnabled: true` | Remove — Ruff extension handles this |
| `python.formatting.provider: "none"` | Remove — Ruff extension handles this |

## Duplicate `[language]` Blocks

JSON allows duplicate keys — the last one wins silently. After editing `settings.json`:
```bash
python -c "import json; json.load(open('.vscode/settings.json'))" && echo "valid"
```

Visually inspect for any `[python]` (or other language block) appearing twice.

## MCP Server Test Snippet

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}\n{"jsonrpc":"2.0","method":"notifications/initialized","params":{}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}\n' | python path/to/mcp_server.py
```

## Related Skills

- `software-development/python-quality` — Python quality workflow
- `vscode-workspace-configurator` — VSCode config templates (note: protected, cannot auto-patch)
