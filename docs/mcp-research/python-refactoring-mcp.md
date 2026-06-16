# Python Refactoring Assistant MCP Server

**Category:** Code Intelligence / Developer Tools  
**Related Projects:** rope, libcst, bowler, Sourcery, Refact.ai

## Overview

A **Python refactoring assistant MCP server** exposes Python code analysis and transformation tools to AI agents via the Model Context Protocol. As of 2025, this is primarily a community-driven integration pattern rather than a single canonical package — multiple approaches exist for wrapping Python refactoring engines as MCP tools.

## Common Approaches

### 1. rope + MCP Wrapper

[rope](https://github.com/python-rope/rope) is the most mature Python refactoring engine, supporting rename, extract method/variable, inline, and 20+ other transformations.

```python
from mcp.server.fastmcp import FastMCP
import rope.base.project as rope_project
import rope.refactor.rename as rope_rename

mcp = FastMCP("python-refactoring")

@mcp.tool()
def rename_symbol(file_path: str, offset: int, new_name: str) -> str:
    """Rename a Python symbol at the given file offset."""
    project = rope_project.Project(".")
    resource = project.get_resource(file_path)
    renamer = rope_rename.Rename(project, resource, offset)
    changes = renamer.get_changes(new_name)
    project.do(changes)
    return f"Renamed to {new_name}"
```

### 2. libcst (Concrete Syntax Tree)

[libcst](https://github.com/Instagram/LibCST) preserves all formatting while enabling structural code transformations — ideal for codemods.

```bash
pip install libcst
```

### 3. Sourcery Integration

[Sourcery](https://sourcery.ai) provides AI-powered refactoring suggestions via CLI and CI. Can be wrapped as MCP tools for agent-driven code improvement.

## Tools to Expose as MCP

| Tool | Description |
|------|-------------|
| `rename_symbol` | Rename a class, function, or variable |
| `extract_method` | Extract selected code into a new function |
| `extract_variable` | Extract expression into a named variable |
| `inline_variable` | Inline a variable back to its usage |
| `organize_imports` | Sort and deduplicate imports (isort) |
| `format_code` | Apply black/ruff formatting |
| `find_references` | Find all usages of a symbol |

## Quick Setup with FastMCP

```bash
pip install "mcp[cli]" rope libcst
```

```python
# refactoring_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("python-refactoring-assistant")

@mcp.tool()
def analyze_code(file_path: str) -> str:
    """Analyze Python file for refactoring opportunities."""
    # Use rope/libcst/pylint for analysis
    ...

if __name__ == "__main__":
    mcp.run()
```

## Hermes Config

```yaml
mcp_servers:
  python-refactoring:
    command: python3
    args: ["/path/to/refactoring_server.py"]
    env:
      PYTHONPATH: "/your/project/root"
```

## Related Resources

- [rope — Python Refactoring Engine](https://github.com/python-rope/rope)
- [libcst — Concrete Syntax Tree](https://github.com/Instagram/LibCST)
- [FastMCP — MCP Server Framework for Python](https://github.com/jlowin/fastmcp)
- [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Sourcery AI Code Quality](https://sourcery.ai)
