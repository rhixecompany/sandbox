# MCP Python Interpreter — PyPI Summary

**Package:** `mcp-python-interpreter`
**Version:** 1.2.3 (Latest release: Oct 12, 2025)
**Author:** YZFly (ethereal_ai@hotmail.com)
**License:** MIT
**Requires:** Python >= 3.10
**Homepage:** [github.com/yzfly/mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)
**Bug Tracker:** [github.com/yzfly/mcp-python-interpreter/issues](https://github.com/yzfly/mcp-python-interpreter/issues)

---

## Overview

A **Model Context Protocol (MCP) server** that enables LLMs to interact with Python environments. It supports code execution, file operations, package management, and environment management — all within a secure, isolated working directory.

---

## Key Features

- **Environment Management**: List and use system or conda Python environments
- **Code Execution**: Run Python code or scripts in any available environment
- **Package Management**: List installed packages; install new ones
- **File Operations**:
  - Read text, source code, and binary files (up to 1MB)
  - Write text and binary files
  - Syntax highlighting for source code
  - Hex representation for binary files
- **Python Prompts**: Templates for function creation, refactoring, and debugging

---

## Installation

```bash
pip install mcp-python-interpreter
```

Or with `uv`:

```bash
uv install mcp-python-interpreter
```

---

## Usage with Claude Desktop

### Prerequisites

- Install [`uv`](https://astral.sh/uv):
  ```bash
  # macOS/Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh

  # Windows
  powershell -ExecutionPolicy Bypass -Command "iwr -useb https://astral.sh/uv/install.ps1 | iex"
  ```

### Configuration

Add to `claude_desktop_config.json` (macOS/Linux):

```json
{
  "mcpServers": {
    "mcp-python-interpreter": {
      "command": "uvx",
      "args": [
        "mcp-python-interpreter",
        "--dir",
        "/path/to/your/work/dir",
        "--python-path",
        "/path/to/your/python"
      ],
      "env": {
        "MCP_ALLOW_SYSTEM_ACCESS": 0
      }
    }
  }
}
```

**Windows:**

```json
{
  "mcpServers": {
    "python-interpreter": {
      "command": "uvx",
      "args": [
        "mcp-python-interpreter",
        "--dir",
        "C:\\path\\to\\your\\working\\directory",
        "--python-path",
        "/path/to/your/python"
      ],
      "env": {
        "MCP_ALLOW_SYSTEM_ACCESS": 0
      }
    }
  }
}
```

> **Note:** The `--dir` parameter is **required** — it isolates all file operations to a specific directory for security.

---

## Available Tools

### Environment & Package Management
| Tool | Description |
|------|-------------|
| `list_python_environments` | List all available Python environments (system + conda) |
| `list_installed_packages` | List packages in a specific environment |
| `install_package` | Install a package in a specific environment |

### Code Execution
| Tool | Description |
|------|-------------|
| `run_python_code` | Execute Python code in a specific environment |
| `run_python_file` | Execute a Python file in a specific environment |

### File Operations
| Tool | Description |
|------|-------------|
| `read_file` | Read any file type (text/binary), with size and safety limits |
| `write_file` | Create or overwrite text or binary files |
| `write_python_file` | Create or overwrite a Python file specifically |
| `list_directory` | List Python files in a directory |

---

## Available Resources

- `python://environments` — List all available Python environments
- `python://packages/{env_name}` — List installed packages for an environment
- `python://file/{file_path}` — Get content of a Python file
- `python://directory/{directory_path}` — List all Python files in a directory

---

## Prompts

- `python_function_template` — Generate a Python function template
- `refactor_python_code` — Help refactor Python code
- `debug_python_error` — Help debug a Python error

---

## Example Use Cases

> - "Show me all available Python environments on my system"
> - "Run this Python code in my conda-base environment: `print('Hello, world!')`"
> - "Create a new Python file called 'hello.py' with a function that says hello"
> - "Read the contents of my 'data.json' file"
> - "Write a new configuration file with these settings..."
> - "List all packages installed in my system Python environment"
> - "Install the requests package in my system Python environment"
> - "Run data_analysis.py with these arguments: --input=data.csv --output=results.csv"

---

## Security Considerations

- **Isolated working directory** — all operations confined to `--dir`
- **File size limits** — reads capped at 1MB
- **Path restrictions** — writes outside working directory are blocked
- **Explicit overwrite protection**
- **Caution advised** — review code/file operations before execution

---

## Release History

| Version | Release Date |
|---------|--------------|
| 1.2.3 | Oct 12, 2025 |
| 1.1   | Apr 4, 2025  |
