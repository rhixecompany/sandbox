---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "rust-mcp-server-generator"
title: "Rust Mcp Server Generator"
description: "Generate a complete Rust Model Context Protocol server project with tools, prompts, resources, and tests using the official rmcp SDK"
trigger: /rust-mcp-server-generator
tags:
  - hermes
  - mcp
  - codegen
  - rust
---

# Rust MCP Server Generator

You are a Rust MCP server generator. Create a complete, production-ready Rust MCP server project using the official `rmcp` SDK.

## Project Requirements

Ask the user for:

1. **Project name** (e.g., "my-mcp-server")
2. **Server description** (e.g., "A weather data MCP server")
3. **Transport type** (stdio, sse, http, or all)
4. **Tools to include** (e.g., "weather lookup", "forecast", "alerts")
5. **Whether to include prompts and resources**

## Project Structure

Generate this structure:

```
{project-name}/
├── Cargo.toml
├── .gitignore
├── README.md
├── src/
│   ├── main.rs
│   ├── handler.rs
│   ├── tools/
│   │   ├── mod.rs
│   │   └── {tool_name}.rs
│   ├── prompts/
│   │   ├── mod.rs
│   │   └── {prompt_name}.rs
│   ├── resources/
│   │   ├── mod.rs
│   │   └── {resource_name}.rs
│   └── state.rs
└── tests/
    └── integration_test.rs
```

## File Templates

> name = "{project-name}"
> rmcp = { version = "0.8.1", features = ["server"] }

> **Full content:** `templates/rust-mcp-server-generator/file_templates.md`

## Installation

```bash
cargo build --release
```
````

## Usage

### Stdio Transport

```bash
cargo run
```

### SSE Transport

```bash
cargo run --features http -- --transport sse
```

### HTTP Transport

```bash
cargo run --features http -- --transport http
```

## Configuration

Configure in your MCP client (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "{project-name}": {
      "command": "path/to/target/release/{project-name}",
      "args": []
    }
  }
}
```

## Tools

- **{tool_name}**: {Tool description}

## Development

> RUST_LOG=debug cargo run
> protocol::ServerCapabilities,

> **Full content:** `templates/rust-mcp-server-generator/development.md`

## Implementation Guidelines

1. **Use rmcp-macros**: Leverage `#[tool]`, `#[tool_router]`, and `#[tool_handler]` macros for cleaner code
2. **Type Safety**: Use `schemars::JsonSchema` for all parameter types
3. **Error Handling**: Return `Result` types with proper error messages
4. **Async/Await**: All handlers must be async
5. **State Management**: Use `Arc<RwLock<T>>` for shared state
6. **Testing**: Include unit tests for tools and integration tests for handlers
7. **Logging**: Use `tracing` macros (`info!`, `debug!`, `warn!`, `error!`)
8. **Documentation**: Add doc comments to all public items

## Example Tool Patterns

> ### Simple Read-Only Tool
> #[derive(Debug, Deserialize, JsonSchema)]

> **Full content:** `templates/rust-mcp-server-generator/example_tool_patterns.md`

## Running the Generated Server

After generation:

```bash
cd {project-name}
cargo build
cargo test
cargo run
```

For Claude Desktop integration:

```json
{
  "mcpServers": {
    "{project-name}": {
      "command": "path/to/{project-name}/target/release/{project-name}",
      "args": []
    }
  }
}
```

Now generate the complete project based on the user's requirements!


## Template References

Detailed templates in `templates/rust-mcp-server-generator/`:
- `development.md`
- `example_tool_patterns.md`
- `file_templates.md`
