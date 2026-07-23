# Implementation Details

> Extracted from `python-mcp-server-generator.prompt.md`.

## Implementation Details

### Project Setup

- Initialize with `uv init project-name`
- Add MCP SDK: `uv add "mcp[cli]"`
- Create main server file (e.g., `server.py`)
- Add `.gitignore` for Python projects
- Configure for direct execution with `if __name__ == "__main__"`

### Server Configuration

- Use `FastMCP` class from `mcp.server.fastmcp`
- Set server name and optional instructions
- Choose transport: stdio (default) or streamable-http
- For HTTP: optionally configure host, port, and stateless mode

### Tool Implementation

- Use `@mcp.tool()` decorator on functions
- Always include type hints - they generate schemas automatically
- Write clear docstrings - they become tool descriptions
- Use Pydantic models or TypedDicts for structured outputs
- Support async operations for I/O-bound tasks
- Include proper error handling

### Resource/Prompt Setup (Optional)

- Add resources with `@mcp.resource()` decorator
- Use URI templates for dynamic resources: `"resource://{param}"`
- Add prompts with `@mcp.prompt()` decorator
- Return strings or Message lists from prompts

### Code Quality

- Use type hints for all function parameters and returns
- Write docstrings for tools, resources, and prompts
- Follow PEP 8 style guidelines
- Use async/await for asynchronous operations
- Implement context managers for resource cleanup
- Add inline comments for complex logic
