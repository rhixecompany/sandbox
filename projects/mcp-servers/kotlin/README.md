# Kotlin MCP Server

A Model Context Protocol (MCP) server implemented in Kotlin, using the official [kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk).

## Overview

This project implements a lightweight MCP server that communicates via **stdio transport**. It registers tools (e.g. `greet`) that LLM hosts — such as Claude Desktop, Cursor, or any MCP-compatible client — can discover and invoke.

## Architecture

```
src/main/kotlin/com/example/mcp/
├── Main.kt           # Entry point — starts the server with StdioServerTransport
├── Server.kt         # Server setup: tool registration, request handlers
├── config/
│   └── Config.kt     # Configuration (name, version, env-based settings)
└── tools/
    └── GreetTool.kt  # Sample tool: returns a personalised greeting
```

- **Main.kt** – Parses CLI args, reads config, creates the server, and runs it.
- **Server.kt** – Builds the MCP server, registers tools, handles lifecycle.
- **Config.kt** – Holds server name, version, and environment overrides.
- **GreetTool.kt** – Implements a `greet` tool that takes a `name` string and returns a greeting.

## Prerequisites

- JDK 17+
- Gradle 8.x (or use the included Gradle wrapper)

## Building

```bash
./gradlew build
```

## Running

Start the server (stdio mode, the default):

```bash
./gradlew run
```

The server reads requests from stdin and writes responses to stdout — it is designed to be launched by an MCP host, not run interactively.

## Adding Tools

1. Create a new class in `src/main/kotlin/com/example/mcp/tools/` implementing a tool function.
2. Register it in `Server.kt` inside the `registerTools()` function.

## Client / Host Configuration

For Claude Desktop, add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "kotlin-mcp-server": {
      "command": "/path/to/gradle",
      "args": [
        "-p",
        "/absolute/path/to/kotlin-mcp-server",
        "run"
      ]
    }
  }
}
```

Or use a fat JAR:

```bash
./gradlew shadowJar
java -jar build/libs/kotlin-mcp-server-all.jar
```

## License

MIT
