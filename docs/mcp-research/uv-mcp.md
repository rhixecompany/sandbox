# uv MCP Server

**Source:** https://github.com/astral-sh/uv  
**Package:** `uv` (Astral)  
**Docs:** https://docs.astral.sh/uv/

## Overview

**uv** is an extremely fast Python package manager and project tool written in Rust, designed as a drop-in replacement for `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, and `virtualenv`. As of 2025, uv supports running as an MCP server, enabling AI agents to manage Python environments, install packages, run scripts, and resolve dependencies through the Model Context Protocol.

## Key Capabilities as MCP Server

- Install and manage Python packages
- Create and manage virtual environments
- Run Python scripts in isolated environments
- Resolve dependency trees
- Manage multiple Python versions
- Build and publish Python packages

## Tools Exposed via MCP

| Tool | Description |
|------|-------------|
| `uv_install` | Install one or more packages |
| `uv_run` | Run a Python script with uv |
| `uv_add` | Add dependency to project |
| `uv_remove` | Remove a dependency |
| `uv_sync` | Sync environment with lockfile |
| `uv_python` | Manage Python version for project |
| `uv_venv` | Create a new virtual environment |

## Installation

### Install uv

```bash
# On Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Via pip (alternative)
pip install uv
```

### Run as MCP Server

```bash
# Start the MCP server (stdio transport)
uvx mcp-server-uv

# Or using uv tool run
uv tool run mcp-server-uv
```

### Using as Tool in Agent Context

uv can also wrap Python execution so agents can run scripts without pre-installing deps:

```bash
# Run a script with auto-dependency resolution
uv run --with requests,pandas my_script.py
```

## Hermes Config

```yaml
mcp_servers:
  uv:
    command: uvx
    args: ["mcp-server-uv"]
```

## Key uv Commands (for Context)

```bash
# Create virtual environment
uv venv .venv

# Install packages
uv pip install requests pandas numpy

# Run Python with inline deps (no venv needed)
uv run --with rich,typer my_script.py

# Add to project
uv add django celery

# Sync all dependencies
uv sync

# Manage Python versions
uv python install 3.12
uv python pin 3.12
```

## Performance

uv is **10-100x faster** than pip for most operations due to:
- Rust implementation with async I/O
- Aggressive caching of wheel files and metadata
- Parallel downloads and installs
- Global shared cache across environments

## Workspace Rules

Per `AGENTS.md` in this workspace: **always use `bun` for the Bash toolkit and `uv`/`python3 -m pip` for Python scripts**. Never use `npm`/`yarn` for workspace-level TypeScript tasks.

```bash
# Correct patterns for this workspace
uv pip install <package>        # Python dependencies
python3 -m pip install <pkg>    # Alternative
bun install                     # JS/TS dependencies (Bash toolkit)
```

## Related Resources

- [uv GitHub](https://github.com/astral-sh/uv)
- [uv Documentation](https://docs.astral.sh/uv/)
- [uv vs pip comparison](https://docs.astral.sh/uv/pip/compatibility/)
- [Astral Blog: Introducing uv](https://astral.sh/blog/uv)
