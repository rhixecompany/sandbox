use rmcp::tool;
use std::sync::Arc;

use crate::state::AppState;

/// Greet a person by name.
///
/// This tool demonstrates a simple text-generation handler with
/// access to shared server state (the greeting counter).
#[tool(description = "Greet a person by name and return a friendly message")]
pub async fn greet(name: String, state: Arc<AppState>) -> String {
    let count = state.increment_greeting_count();
    format!(
        "Hello, {name}! You are visitor number {count}. Welcome to the Rust MCP server."
    )
}
