# Chrome DevTools MCP — Reference Overview

## Key Concepts

- **Chrome DevTools MCP** provides programmatic control over a live Chrome browser session through the Model Context Protocol. It exposes tools for navigation, input interaction, debugging (console, network), screenshots, performance profiling, and emulation — all without requiring manual DevTools usage.
- **Snapshot-First Workflow** — Always use `take_snapshot` to get an accessibility tree with `uid` values before interacting with elements. The `uid` is required by click, fill, and hover tools. `take_screenshot` is for visual verification only.
- **Performance Tracing** — Use `performance_start_trace` with `reload=true` and `autoStop=true` to capture a page load trace. Then use `performance_analyze_insight` to diagnose LCP, layout shifts, and other Core Web Vitals. This is the primary workflow for performance debugging.
- **Debugging Workflow** — When a page is failing, follow this chain: `list_console_messages` (for JS errors) → `list_network_requests` (for failed 4xx/5xx resources) → `evaluate_script` (for DOM/global state inspection).
- **Context Management** — Always run `list_pages` and `select_page` if unsure which tab is active. After any navigation or DOM change, take a new snapshot as `uid` values may change. Use `wait_for` with reasonable timeouts for dynamic content.