# Swift MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server written in Swift,
providing tools that can be discovered and called by MCP clients (such as LLM agents).

## Features

- **MCP-compliant** — speaks the Model Context Protocol for tool discovery and execution.
- **Two transports** — supports both **stdio** (local/CLI) and **HTTP** (remote) transports.
- **Graceful shutdown** — uses Swift ServiceLifecycle for clean signal handling.
- **Configurable** — all settings via environment variables or defaults.

## Tools

| Tool        | Description                                           |
|-------------|-------------------------------------------------------|
| `greet`     | Greet a person by name with an optional title.        |
| `calculate` | Perform basic arithmetic: add, subtract, multiply, divide. |

## Requirements

- **Swift 6.0+**
- **macOS 15+** (for running; can be edited on any platform)
- An Internet connection for the first build (to resolve dependencies)

## Getting Started

### Build

```bash
swift build
```

### Run (stdio transport — default)

```bash
swift run MyMCPServer
```

The server reads JSON-RPC messages from stdin and writes responses to stdout,
which is the standard MCP transport for local integrations.

### Run (HTTP transport)

```bash
MCP_TRANSPORT=http MCP_PORT=8080 swift run MyMCPServer
```

## Configuration

All configuration is via environment variables:

| Variable         | Default             | Description                                 |
|------------------|---------------------|---------------------------------------------|
| `MCP_TRANSPORT`  | `stdio`             | Transport protocol (`stdio` or `http`).     |
| `MCP_HOST`       | `127.0.0.1`         | Host address for HTTP transport.            |
| `MCP_PORT`       | `8080`              | Port for HTTP transport.                    |
| `MCP_LOG_LEVEL`  | `info`              | Log level (`trace`, `debug`, `info`, etc.). |
| `MCP_SERVER_NAME`| `swift-mcp-server`  | Server name advertised to MCP clients.      |
| `MCP_SERVER_VERSION`| `1.0.0`          | Server version advertised to MCP clients.   |

## Project Structure

```
swift-mcp-server/
├── Package.swift                       # Swift Package Manager manifest
├── Sources/
│   └── MyMCPServer/
│       ├── main.swift                  # Entry point with ServiceLifecycle
│       ├── Server.swift                # MCP server configuration & run loop
│       ├── Config.swift                # Environment-based configuration
│       └── Tools/
│           ├── ToolDefinitions.swift   # Tool schemas (greet, calculate)
│           └── ToolHandlers.swift      # Tool implementation logic
└── README.md
```

## Extending

To add a new tool:

1. **Define the schema** — Add a new static property in `ToolDefinitions.swift`.
2. **Implement the handler** — Add a corresponding method in `ToolHandlers.swift`.
3. **Register the tool** — Add a `case` in the `switch` inside `Server.swift`'s `handleToolCall`.
4. **Add the tool to `all`** — Append it to the `ToolDefinitions.all` array.

## License

MIT
