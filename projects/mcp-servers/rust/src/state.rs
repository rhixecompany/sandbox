use std::collections::HashMap;
use std::sync::Mutex;

/// Shared application state for the MCP server.
///
/// This state is wrapped in `Arc<AppState>` and injected into tool handlers
/// via rmcp's state mechanism.
#[derive(Debug)]
pub struct AppState {
    /// Counter tracking how many times the greet tool has been called.
    pub greeting_count: Mutex<u64>,
    /// A simple key-value store for persisting messages across tool calls.
    pub messages: Mutex<HashMap<String, String>>,
}

impl AppState {
    /// Create a new, empty application state.
    pub fn new() -> Self {
        Self {
            greeting_count: Mutex::new(0),
            messages: Mutex::new(HashMap::new()),
        }
    }

    /// Increment the greeting counter and return the new value.
    pub fn increment_greeting_count(&self) -> u64 {
        let mut count = self.greeting_count.lock().unwrap();
        *count += 1;
        *count
    }

    /// Store a message in the key-value store.
    pub fn set_message(&self, key: String, value: String) {
        let mut messages = self.messages.lock().unwrap();
        messages.insert(key, value);
    }

    /// Retrieve a message from the key-value store.
    pub fn get_message(&self, key: &str) -> Option<String> {
        let messages = self.messages.lock().unwrap();
        messages.get(key).cloned()
    }
}

impl Default for AppState {
    fn default() -> Self {
        Self::new()
    }
}
