pub mod greet;

use rmcp::Router;
use std::sync::Arc;

use crate::state::AppState;

/// Create the MCP [`Router`] with all tool handlers registered.
///
/// Call `router.serve(transport)` to start the server.
pub fn create_router(state: Arc<AppState>) -> Router {
    Router::new()
        .with_state(state)
        .with_tool(greet::greet)
}
