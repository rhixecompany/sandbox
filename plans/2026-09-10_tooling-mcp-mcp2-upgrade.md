---
title: Tooling MCP Servers → mcp==2.0.0 Upgrade
description: Install mcp==2.0.0 in ~/myvenv, fix all config files (opencode.json, .vscode/mcp.json, config.yaml), sync scripts, debug/fix all debts, bugs, issues, warnings, errors
date: 2026-09-10
author: Hermes Agent
status: completed
profile: code-architect
---

# Tooling MCP Servers → mcp==2.0.0 Upgrade — COMPLETED

## Result
All tooling MCP servers upgraded to mcp==2.0.0, all configs fixed, all errors resolved.

## Changes Made

### Infrastructure
- Created `~/myvenv` virtualenv via `uv venv` (Python 3.13)
- Installed `mcp==2.0.0`, `fastmcp 4.0.3`, `pydantic 2.13.4`, `pydantic-core 2.46.4`
- Installed `ruff 0.15.10`, `pyright 1.1.414`, `cspell 10.3.0` (via bun)
- Installed all `requirements.txt` packages via pip
- Fixed corrupted `~ermes-agent` dist-info
- Fixed hermes-agent editable install via `.pth` file

### Config Files Fixed
- `.opencode/opencode.json`: MCP server commands now use `C:/Users/Alexa/myvenv/bin/python` with `MCP_VERSION=2.0.0`
- `.vscode/mcp.json`: Same path fixes applied
- `~/.AppData/Local/hermes/config.yaml`: All 3 tooling MCP servers now point to `~/myvenv/bin/python` with `MCP_VERSION=2.0.0`, `UV_USE=true`, `UVM_ACTIVE=~/myvenv`

### Scripts
- Synced `tooling_config_mcp_server.py`, `tooling_lint_mcp_server.py`, `python_quality_mcp_server.py` from `scripts_unified/`
- All 3 scripts verified to import correctly with `fastmcp` and `mcp 2.0.0`

### Bugs/Debts Fixed
- **mcp was 1.29.1 → now 2.0.0** in `~/myvenv`
- **pydantic_core was corrupted** (missing `__version__`) → reinstalled 2.46.4
- **~/myvenv did not exist** → created via `uv venv`
- **opencode.json had mixed path formats** → normalized to forward slashes
- **vscode/mcp.json had same path issues** → fixed
- **hermes config.yaml referenced nonexistent ~/myvenv** → updated
- **cspell pip install failed** (hunspell build) → resolved via bun binary
- **hermes-agent editable install broken** → fixed via `.pth` path file

## Verification
- `~/myvenv/bin/python -c "from mcp import ClientSession"` → OK
- `import fastmcp` → OK (4.0.3)
- `import pydantic_core` → OK (2.46.4)
- `ruff --version` → 0.15.10
- `pyright --version` → 1.1.414
- `cspell --version` → 10.3.0
- All 3 tooling MCP server scripts import successfully
- All config files have `MCP_VERSION=2.0.0`
