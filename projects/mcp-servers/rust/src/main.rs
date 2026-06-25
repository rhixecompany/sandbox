//! Rust MCP Server
//!
//! A Model Context Protocol (MCP) server implemented in Rust using the `rmcp` SDK.
//! Communicates over stdio transport, providing tool-based interaction
//! to the MCP client (e.g., an LLM host).

use rmcp::ServiceExt;
use rmcp::transport::stdio;
use std::sync::Arc;

mod state;
mod tools;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // Initialise shared application state (wrapped in Arc for thread-safe access).
    let state = Arc::new(state::AppState::new());

    // Build the router with all registered tool handlers.
    let router = tools::create_router(state);

    // Serve over stdio transport — the standard MCP transport layer.
    // The server will read JSON-RPC messages from stdin and write responses
    // to stdout, using stderr for diagnostics.
    router
        .serve(stdio::transport())
        .await?;

    Ok(())
}
