# MCP Servers

A multi-language collection of [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server implementations. Each `<language>/` directory is a complete, buildable MCP server written in that language's standard tooling and idioms.

> [!NOTE]
> Every implementation speaks the MCP **stdio transport** so it composes with any MCP client (Claude Desktop, GitHub Copilot, Cursor, the [MCP Inspector](https://github.com/modelcontextprotocol/inspector), and more). Most servers ship a small, shared tool set (a `greet` tool plus a calculator or file utility) so behavior is comparable across languages.

## Languages

| Language    | Directory       | Build system            | Notes                                  |
|-------------|-----------------|-------------------------|----------------------------------------|
| TypeScript  | `typescript/`   | npm / bun               | Zod-validated tools, ES modules        |
| Python      | `python/`       | uv / pip (FastMCP)     | Greeting + recursive file-search tools |
| Go          | `go/`           | Go modules              | Greet + file-info tools, unit tested    |
| Rust        | `rust/`         | Cargo (`rmcp`)          | Shared-state visitor counter            |
| Java        | `java/`         | Maven (shaded JAR)      | Greet + echo tools                      |
| Kotlin      | `kotlin/`       | Gradle                  | Greet tool                              |
| PHP         | `php/`          | Composer                | Greet tool                              |
| Ruby        | `ruby/`         | Bundler (`mcp` gem)     | Greet tool                              |
| Swift       | `swift/`        | Swift Package Manager   | stdio **and** HTTP transports           |
| C#          | `csharp/`       | .NET 8 SDK              | Host builder pattern                   |
| Copilot Studio | `copilot-studio/` | npm               | API-definition-driven MCP server        |

## Getting started

Each language directory is fully self-contained. Pick the one you want and follow its own `README.md` for prerequisites, build, and run instructions. For example:

```bash
# TypeScript
cd typescript && npm install && npm run build && npm start

# Python (with uv)
cd python && uv sync && uv run python-mcp-server

# Go
cd go && go run .
```

> [!TIP]
> The fastest way to exercise any server locally is the MCP Inspector:
> ```bash
> npx @modelcontextprotocol/inspector node typescript/dist/index.js
> ```
> Swap in the entry point for whichever language server you are testing.

## Repository layout

```text
mcp-servers/
├── <language>/      # One self-contained MCP server per language
│   └── README.md    # Language-specific setup & run instructions
├── AGENTS.md         # Agent-oriented project overview
├── architecture.md   # Cross-language architecture notes
├── folder-structure.md
└── tech-stack.md
```

## Architecture

All servers follow the same shape: an entry point that boots an MCP server over stdio, a tool registry, and one or more tool implementations. The shared `greet` tool is present in every language as a reference; calculator/file utilities vary by implementation. See [`architecture.md`](architecture.md) for details and [`tech-stack.md`](tech-stack.md) for the SDK and runtime choices behind each one.

## Development

- Each `<language>/` directory is independent: its own source, tests, and build config. No shared code is required to build or run a single server.
- Shared patterns across implementations make it easy to port a tool from one language to another.
- Refer to the subdirectory `README.md` for language-specific build, test, and debugging steps.

> [!IMPORTANT]
> This README documents the project root only. Per-language setup, prerequisites, and commands live in each subdirectory's `README.md` — consult that file before building or running a specific server.
