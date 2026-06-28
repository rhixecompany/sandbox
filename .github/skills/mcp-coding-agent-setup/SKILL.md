---
author: Hermes Agent
description: Install, configure, and test MCP servers for MindStudio, Codex CLI, and
  Copilot CLI — all three expose tools to run AI prompts from within Hermes.
license: MIT
name: mcp-coding-agent-setup
platforms:
- windows
prerequisites:
  commands:
  - mindstudio
  - codex
  - copilot
  python_packages:
  - fastmcp
title: MCP Coding Agent Setup
version: 1.0.0

---

# MCP Coding Agent Setup

Set up MCP servers for three coding agents (MindStudio, Codex CLI, Copilot CLI) to run prompts from within Hermes.

## When to Use

Use this skill when setting up MCP servers for AI coding agents on a Hermes installation. Each agent exposes tools that Hermes can use to run AI prompts and code generation tasks.

## Prerequisites

Before starting, verify the CLI tools are installed:

```bash
which mindstudio codex copilot
```

- **MindStudio** — installed via MindStudio SDK (`mindstudio mcp`)
- **Codex CLI** — OpenAI's coding agent (v0.141.0+) (`codex mcp-server`)
- **Copilot CLI** — GitHub Copilot (`copilot -p`)

Install FastMCP for wrapping CLIs as MCP servers:

```bash
pip install fastmcp
```

## MCP Server Checklist

| Server | Command | Args | Tool Count | Key Tool |
|---|---|---|---|---|
| mindstudio | `mindstudio` | `["mcp"]` | 197 | `ask` |
| codex | `codex` | `["mcp-server"]` | 2 | `codex` |
| copilot-mcp | `python.exe` | `[script.py]` | 1 | `run_prompt` |

## Configuration

Add to `~/.hermes/config.yaml` under `mcp_servers`:

```yaml
mcp_servers:
  # Direct stdio MCP servers
  mindstudio:
    command: mindstudio
    args: [mcp]
    enabled: true
  codex:
    command: codex
    args: [mcp-server]
    enabled: true
  # FastMCP wrapper for Copilot (no native MCP server)
  copilot-mcp:
    command: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe
    args:
      - C:\Users\Alexa\AppData\Local\hermes\scripts\copilot_mcp_server.py
    enabled: true
```

### Copilot MCP Server Script

Create `copilot_mcp_server.py` in `~/AppData/Local/hermes/scripts/`:

```python
"""Copilot MCP Server — run prompts through GitHub Copilot CLI."""
import subprocess
import os
from fastmcp import FastMCP

mcp = FastMCP("copilot-mcp")
BASH = r"C:\Program Files\Git\usr\bin\bash.exe"

@mcp.tool()
def run_prompt(prompt: str) -> str:
    """Run a coding prompt through GitHub Copilot CLI."""
    copilot = _find_copilot()
    # MSYS path conversion
    if ":" in copilot and copilot[1] == ":":
        drive = copilot[0].lower()
        rest = copilot[2:].replace("\\", "/")
        copilot = f"/{drive}{rest}"
    try:
        cmd = f"{copilot} -p {_q(prompt)} --allow-all"
        result = subprocess.run(
            [BASH, "-c", cmd],
            capture_output=True, text=True, timeout=120,
        )
        return (result.stdout or "").strip()[:8000]
    except subprocess.TimeoutExpired:
        return "Error: timed out after 120 seconds"
    except Exception as e:
        return f"Error: {e}"

def _find_copilot() -> str:
    copilot = __import__("shutil").which("copilot")
    if copilot:
        dir_name = os.path.dirname(copilot)
        base = os.path.join(dir_name, "copilot")
        if os.path.isfile(base):
            return base
        return copilot
    raise FileNotFoundError("copilot CLI not found")

def _q(s):
    return "'" + s.replace("'", "'\\''") + "'"

if __name__ == "__main__":
    mcp.run(show_banner=False)
```


## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-mcp` | MCP server lifecycle management |
| `native-mcp` | MCP client configuration |

## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
- **Reference file:** See `references/quick-reference.md` for common commands and config snippets
## Verification

Test each MCP server:

```bash
hermes mcp test mindstudio
hermes mcp test codex
hermes mcp test copilot-mcp
```

Expected output:

```
✓ Connected (XXXms)
✓ Tools discovered: N

    tool_name  Description...
```

After verification, reload MCP in the current session:

```bash
# In Hermes TUI, press Ctrl+R or type /reload-mcp
# Or start a new session
```

## Troubleshooting

### Copilot hangs / times out
- Add `--allow-all` to the copilot command (prevents TTY permission prompts)
- Ensure the bash path is correct for Windows (`C:\Program Files\Git\usr\bin\bash.exe`)

### Codex "usage limit" error
- Free tier rate limit. Upgrade to Codex Plus at chatgpt.com or wait for monthly reset.

### MindStudio "out of credits"
- Top up at https://app.mindstudio.ai/services/balance

### MCP tools not available after config change
- Run `hermes mcp list` to verify the server shows as ✓ enabled
- Reload MCP or start a new Hermes session

## Windows-Specific Notes

- `codex` is a POSIX shell script — must be run through bash, not cmd.exe
- `copilot` is a bash script that wraps `copilot.bat` — subprocess must use bash
- MCP servers inherit PATH from Hermes environment
