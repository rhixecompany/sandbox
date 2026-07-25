---
name: mcp-playwright
title: MCP Playwright — Browser Automation
description: Exposes all Playwright MCP tools for browser navigation, page interaction, form filling, screenshots, tab management, and JavaScript evaluation. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - playwright
  - browser
  - automation
  - testing
---

# MCP Playwright

Provides full browser automation via the `@playwright/mcp` server. Enables navigating, clicking, typing, screenshotting, form filling, and evaluating JavaScript in real browser contexts.

## Prerequisites

- MCP server: `playwright` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y @playwright/mcp@latest`
- Playwright browsers must be installed (`npx playwright install chromium`)

## Tools

| Tool | Description |
|------|-------------|
| `browser_navigate` | Navigate to a URL |
| `browser_navigate_back` | Go back in history |
| `browser_close` | Close the current page |
| `browser_snapshot` | Capture accessibility tree of current page |
| `browser_click` | Click an element |
| `browser_type` | Type into an editable element |
| `browser_fill_form` | Fill multiple form fields at once |
| `browser_hover` | Hover over an element |
| `browser_drag` | Drag and drop between elements |
| `browser_select_option` | Select dropdown option |
| `browser_press_key` | Press a keyboard key |
| `browser_resize` | Resize the browser window |
| `browser_tabs` | List, create, close, or select tabs |
| `browser_console_messages` | Get console log output |
| `browser_evaluate` | Run JavaScript in page context |
| `browser_file_upload` | Upload file(s) |
| `browser_handle_dialog` | Accept/dismiss JS dialogs |
| `browser_wait_for` | Wait for text or timeout |
| `browser_run_code_unsafe` | ⚠️ Run arbitrary Playwright code (RCE-equivalent) |

## Workflow

### Phase 1: Verify

```
hermes mcp test playwright
```

### Phase 2: Basic Navigation & Interaction

```
# Navigate
browser_navigate(url: "https://example.com")
browser_snapshot()          # accessibility tree

# Interact
browser_fill_form(fields: {selector: "#search", value: "query"})
browser_click(selector: "button#submit")
browser_type(selector: "input[name=email]", text: "test@example.com")
browser_select_option(selector: "select#country", value: "US")

# Navigate
browser_navigate_back()
browser_press_key(key: "Enter")
```

### Phase 3: Advanced Features

```
# Debug
browser_console_messages()     # check for JS errors
browser_snapshot()             # verify page state after action
browser_evaluate(script: "document.title")

# Multi-tab
browser_tabs(action: "list")
browser_tabs(action: "create", url: "https://example.com")
browser_tabs(action: "select", index: 1)

# Wait
browser_wait_for(text: "Loading complete", timeout: 5000)
browser_resize(width: 1280, height: 720)
```

### Phase 4: Test Cases

```bash
# 1. Connectivity
hermes mcp test playwright

# 2. Navigate + snapshot (read-only)
# Call: mcp_playwright_browser_navigate(url="https://example.com")
# Call: mcp_playwright_browser_snapshot()

# 3. Evaluate JS (no side effects)
# Call: mcp_playwright_browser_evaluate(script="navigator.userAgent")

# 4. Console messages (read-only)
# Call: mcp_playwright_browser_console_messages()

# 5. Tab management
# Call: mcp_playwright_browser_tabs(action="list")

# 6. Close
# Call: mcp_playwright_browser_close()
```

## Best Practices

1. **Always call `browser_snapshot` after navigation** — it returns the AX tree showing all interactive elements
2. **Use `browser_fill_form` for multiple fields** — more efficient than sequential `browser_type` calls
3. **Use `browser_evaluate` for page state** — check DOM state, read variables, get computed styles
4. **Call `browser_console_messages` to detect errors** — JS exceptions, 404s, API failures appear here
5. **Use `browser_tabs` for multi-page workflows** — avoids losing state when navigating between sites
6. **Always `browser_close` after done** — frees browser resources

## Pitfalls

- `browser_run_code_unsafe` is **RCE-equivalent** — only use in trusted environments
- Selector syntax is **Playwright locator format** — CSS selectors work, but `getByRole`, `getByText`, etc. are preferred
- Snapshots use AX tree, not visual rendering — use screenshots (`browser_vision` in built-in tools) for visual verification
- `browser_handle_dialog` must be called before the dialog auto-dismisses
- File upload paths must be absolute paths on the system running Playwright
- Tab indices are 0-based — index 0 is the original tab
- Some `wait_for` conditions may timeout — set appropriate timeout values
- Playwright browsers must be installed separately: `npx playwright install chromium`

## Verification Checklist

- [ ] `hermes mcp test playwright` passes
- [ ] `browser_navigate` loads a page
- [ ] `browser_snapshot` returns accessibility tree
- [ ] `browser_evaluate` returns JS result
- [ ] `browser_close` succeeds
