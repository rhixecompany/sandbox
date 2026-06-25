# Python MCP Server

A production-ready [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server built with the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk). Uses **stdio transport** and provides greeting and file‑search tools.

## Features

- **Greeting tool** — generate personalised greetings, with optional title and formal/casual modes.
- **File‑search tool** — recursively search directories with glob patterns; returns paths, sizes, and timestamps.
- **FastMCP** — built on the modern `FastMCP` API for clean, type‑hinted tool definitions.
- **Error handling** — typed exceptions, input validation, and graceful partial‑result fallback.
- **CLI entry point** — ready to run directly or install as a console script.

## Prerequisites

- Python **3.11+**
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Quick Start

### 1. Clone / enter the project

```bash
cd projects/mcp-servers/python
```

### 2. Create virtual environment & install dependencies

**With uv (recommended):**

```bash
uv sync
```

**With pip:**

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows (cmd / PowerShell)
pip install -e .
```

### 3. Run the server

```bash
uv run python-mcp-server
# or
python -m main
# or
python main.py
```

The server starts and listens for **stdio**‑based MCP requests (the default transport). No network ports are opened.

## Usage

### Client configuration

Configure your MCP client (e.g. Claude Desktop, VS Code extension, or a custom script) to launch this server:

**Example `mcp.json` or Claude Desktop config:**

```json
{
  "mcpServers": {
    "python-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/projects/mcp-servers/python",
        "run",
        "python-mcp-server"
      ]
    }
  }
}
```

Or, if the package is installed in a virtual environment:

```json
{
  "mcpServers": {
    "python-mcp-server": {
      "command": "/absolute/path/to/.venv/bin/python",
      "args": ["-m", "main"]
    }
  }
}
```

### Tools reference

#### 1. `greeting`

Generate a personalised greeting.

| Parameter | Type   | Required | Default | Description                              |
|-----------|--------|----------|---------|------------------------------------------|
| `name`    | `str`  | ✅       | —       | The person's name to greet.              |
| `title`   | `str?` | ❌       | `None`  | Honorific (Mr., Ms., Dr., etc.).         |
| `formal`  | `bool` | ❌       | `False` | `True` for a formal greeting, `False` for casual. |

**Examples:**

```
→ greeting(name="Alice")
← "Hey Alice, welcome to the MCP server! 👋"

→ greeting(name="Dr. Smith", title="Dr.", formal=True)
← "Greetings, Dr. Dr. Smith. It is a pleasure to meet you."
```

#### 2. `search_files`

Search for files under a directory using a glob pattern.

| Parameter       | Type       | Required | Default | Description                                      |
|-----------------|------------|----------|---------|--------------------------------------------------|
| `pattern`       | `str`      | ✅       | —       | Glob pattern (e.g. `"*.py"`, `"**/*.md"`).      |
| `root_dir`      | `str`      | ❌       | `"."`   | Root directory to search (resolved from CWD).    |
| `max_results`   | `int`      | ❌       | `20`    | Max results (1–200).                             |
| `case_sensitive`| `bool`     | ❌       | `False` | Case‑sensitive pattern matching.                 |

**Returns:** list of objects with `path` (absolute), `size` (bytes), `modified` (Unix timestamp), and `is_dir`.

**Example:**

```
→ search_files(pattern="*.py", root_dir=".", max_results=5)
← [
     {
       "path": "/home/user/project/main.py",
       "size": 4281,
       "modified": 1719000000.0,
       "is_dir": false
     },
     ...
   ]
```

## Project Structure

```
python-mcp-server/
├── main.py            # Server implementation (FastMCP)
├── pyproject.toml     # Project metadata & dependencies
├── README.md          # This file
├── .python-version    # Required Python version
└── .venv/             # Virtual environment (auto-created by uv)
```

## Development

### Type checking

```bash
uv run mypy main.py
```

### Linting

```bash
uv run ruff check main.py
```

### Formatting

```bash
uv run ruff format main.py
```

## License

MIT
