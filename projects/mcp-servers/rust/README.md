# Rust MCP Server

A **Model Context Protocol** (MCP) server implemented in Rust using the [`rmcp`](https://crates.io/crates/rmcp) SDK.

This server exposes tools to MCP clients (e.g., LLM hosts) over **stdio transport**.

## Features

- Greeting tool with shared state (visitor counter)
- Async runtime via `tokio`
- `rmcp` SDK v0.8.1 (server feature)
- Clean, modular structure

## Project Structure

```
rust-mcp-server/
├── Cargo.toml
├── .gitignore
├── README.md
└── src/
    ├── main.rs          # Entry point, stdio server setup
    ├── state.rs         # Shared application state
    └── tools/
        ├── mod.rs       # Router builder
        └── greet.rs     # Greeting tool
```

## Prerequisites

- [Rust](https://www.rust-lang.org/tools/install) 1.75 or later (edition 2021)
- Cargo (usually ships with Rust)

## Build & Run

### Build

```bash
cargo build --release
```

### Run

```bash
cargo run --release
```

The server listens on **stdin/stdout** — it expects a connected MCP client (like an LLM agent) that speaks the Model Context Protocol over stdio.

### Testing the server

You can test the server by piping a JSON-RPC message to it, or by connecting an MCP client. For a quick smoke test:

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"ping"}' | cargo run
```

## Tool Reference

### `greet`

Greet a person by name.

**Parameters:**
| Parameter | Type   | Required | Description          |
|-----------|--------|----------|----------------------|
| `name`    | string | yes      | Name of the person   |

**Returns:** A friendly greeting string with the current visitor count.

## Dependencies

| Crate        | Version | Purpose                    |
|--------------|---------|----------------------------|
| `rmcp`       | 0.8.1   | MCP SDK (server features)  |
| `tokio`      | 1.x     | Async runtime              |
| `serde`      | 1.x     | Serialization              |
| `serde_json` | 1.x     | JSON handling              |
| `anyhow`     | 1.x     | Error handling             |

## License

MIT
