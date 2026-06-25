# go-mcp-server

A Go MCP (Model Context Protocol) server with greeting and file info tools.

## Overview

This server implements the [Model Context Protocol](https://modelcontextprotocol.io) using stdio transport.
It exposes two tools:

- **`greet`** — Generate a personalized greeting message.
- **`file_info`** — Get metadata about a file or directory on the local filesystem.

## Project Structure

```
go-mcp-server/
├── config/
│   └── config.go      # Environment-based configuration
├── tools/
│   ├── registry.go    # Tool registration and execution
│   ├── tool1.go       # Greet tool
│   └── tool2.go       # File info tool
├── main.go            # Entry point and stdio MCP server loop
├── main_test.go       # Tests for tools and protocol handling
├── go.mod             # Go module definition
└── README.md          # This file
```

## Prerequisites

- Go 1.22 or later

## Building

```bash
cd go-mcp-server
go build -o go-mcp-server .
```

## Running

```bash
# Default configuration
go run .

# With environment overrides
MCP_LOG_LEVEL=debug go run .
```

The server listens on stdin/stdout using the MCP stdio transport. Use it with any MCP client
that supports stdio mode.

## Configuration

All configuration is via environment variables:

| Variable              | Default          | Description                     |
|-----------------------|------------------|---------------------------------|
| `MCP_SERVER_NAME`     | `go-mcp-server`  | Server name advertised to client |
| `MCP_SERVER_VERSION`  | `1.0.0`          | Server version                   |
| `MCP_LOG_LEVEL`       | `info`           | Log verbosity (debug, info)      |
| `MCP_MAX_TOOL_RESULTS`| `100`            | Max results from tool calls      |

## Testing

```bash
go test -v ./...
```

## Protocol

This server speaks the MCP JSON-RPC protocol over stdio:

1. Client sends `initialize` to negotiate protocol version.
2. Client calls `tools/list` to discover available tools.
3. Client calls `tools/call` with tool name and arguments.

### Example: calling the greet tool

Input (stdin):
```json
{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"greet","arguments":{"name":"Alice"}}}
```

Output (stdout):
```json
{"jsonrpc":"2.0","id":1,"result":{"content":[{"type":"text","text":"{\"greeting\":\"Hello, Alice! Welcome to the Go MCP server.\"}"}]}}
```

## License

MIT
