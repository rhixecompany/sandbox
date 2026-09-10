# ~/myvenv — Virtualenv Configuration Reference

## Purpose
This workspace uses `~/myvenv` as the preferred Python virtual environment for all tooling MCP servers (python-quality, tooling-config, tooling-lint, pytest, django) to ensure consistency across hermes, opencode, copilot, and codex.

## Setup (uv / uvx / uvm preferred)

```bash
# Create the virtualenv using uv (fastest)
uv venv ~/myvenv --python python3.11

# Activate
source ~/myvenv/bin/activate   # Linux/macOS
# OR
~/myvenv/Scripts/activate.bat  # Windows

# Install mcp==2.0.0 (canonical version for all tooling servers)
uv pip install mcp==2.0.0

# Verify
python -c "import mcp; print('mcp version:', mcp.__version__ if hasattr(mcp, '__version__') else 'installed')"
```

## uv / uvx / uvm Tools

| Tool | Purpose | Command Example |
|---|---|---|
| `uv` | Fast package manager / venv | `uv pip install ruff pyright` |
| `uvx` | Run Python CLI tools | `uvx ruff check .` |
| `uvm` | Virtualenv manager / project isolation | `uvm install` / `uvm use` |

## Tooling MCP Servers Updated

Each tooling server script references:
- Python interpreter: `~/myvenv/Scripts/python.exe` (Windows) or `~/myvenv/bin/python` (Unix)
- `mcp==2.0.0` package installed in `~/myvenv`
- Tools installed via `uv pip install`: `ruff`, `pyright` (`python-quality`); `pre-commit`, `git-cliff`, `markdownlint-cli2`, `cspell` (`tooling-config`); `eslint`, `prettier`, `markdownlint-cli2`, `cspell` (`tooling-lint`)

## Reference Paths Used in Configs

```json
{
  "python_interpreter": "~/myvenv/bin/python",
  "mcp_version": "2.0.0",
  "package_manager": "uv",
  "run_tool": "uvx",
  "env_manager": "uvm"
}
```

## DRY Note
This reference file (`myvenv-reference.md`) is the single source of truth. All `.opencode/opencode.json` and `.vscode/mcp.json` tooling server entries must reference `~/myvenv` rather than duplicating a different venv path.
