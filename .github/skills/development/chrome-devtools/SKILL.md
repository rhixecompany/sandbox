---
author: Hermes Agent
description: Expert-level browser automation, debugging, and performance analysis using Chrome DevTools Protocol. Use when you need to automate browser interactions, debug complex UI issues, profile performance, or capture network activity programmatically.
license: MIT
metadata:
  hermes:
    tags: [imported, browser, debugging, performance, automation, devtools]
name: chrome-devtools
tags:
- imported
- browser
- debugging
- performance
- automation
- devtools
- scripts
title: Chrome DevTools Protocol
version: 1.0.0
---

# Chrome DevTools Protocol

## Purpose

Use this skill when you need to automate browser interactions, debug complex UI issues, profile performance, or capture network activity programmatically using the Chrome DevTools Protocol (CDP).

## When to Use

- Automating browser tasks that require DOM inspection or manipulation
- Debugging JavaScript errors, network failures, or rendering issues
- Profiling page load performance, runtime performance, or memory usage
- Capturing and analyzing network requests (HAR, WebSocket, fetch/XHR)
- Testing responsive design, device emulation, or accessibility
- Intercepting and modifying network requests

## When NOT to Use

- Simple HTTP requests (use `httpie` or `fetch` skill)
- Static page scraping without JS execution (use `scrapling` skill)
- Visual regression testing (use `playwright-automation` skill)
- Cross-browser testing (CDP is Chrome/Edge only)

## Workflow

### Phase 1: Connect to Browser

```bash
# Launch Chrome with remote debugging port
chrome --remote-debugging-port=9222 --user-data-dir=/tmp/cdp-profile

# Or connect to existing instance
# Find debug URL: http://localhost:9222/json
```

```python
# Python CDP connection example
import asyncio
import websockets
import json

async def connect_cdp():
    async with websockets.connect('ws://localhost:9222/devtools/browser/<id>') as ws:
        await ws.send(json.dumps({"id": 1, "method": "Target.getTargets"}))
        print(await ws.recv())
```

### Phase 2: Enable Domains

```json
{"id": 1, "method": "Network.enable"}
{"id": 2, "method": "Page.enable"}
{"id": 3, "method": "Runtime.enable"}
{"id": 4, "method": "Debugger.enable"}
{"id": 5, "method": "Performance.enable"}
```

### Phase 3: Execute Tasks

**Network Monitoring:**
```json
{"id": 6, "method": "Network.requestWillBeSent", "params": {"request": {...}}}
{"id": 7, "method": "Network.responseReceived", "params": {"response": {...}}}
```

**Runtime Evaluation:**
```json
{"id": 8, "method": "Runtime.evaluate", "params": {"expression": "document.title", "returnByValue": true}}
```

**Performance Profiling:**
```json
{"id": 9, "method": "Performance.start"}
# ... page interaction ...
{"id": 10, "method": "Performance.stop"}
```

**Debugger Control:**
```json
{"id": 11, "method": "Debugger.setBreakpointByUrl", "params": {"lineNumber": 42, "urlRegex": "app.js"}}
{"id": 12, "method": "Debugger.stepInto"}
```

### Phase 4: Extract & Analyze

- Save network logs as HAR: `Network.getResponseBody`
- Export performance trace: `Performance.getTimeline`
- Capture screenshots: `Page.captureScreenshot`
- Get accessibility tree: `Accessibility.getFullAXTree`

## Verification Checklist

- [ ] Chrome launched with `--remote-debugging-port`
- [ ] CDP connection established (WebSocket handshake)
- [ ] Required domains enabled before use
- [ ] Events handled asynchronously (non-blocking)
- [ ] Resources cleaned up (targets closed, browser quit)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | Launch browser with debugging flags |
| `browser` | High-level browser automation |
| `playwright-automation` | Alternative for cross-browser |
| `systematic-debugging` | Root cause analysis |

## Related Skills

- `playwright-automation` — Cross-browser automation
- `browser` — High-level browser operations
- `systematic-debugging` — Debugging methodology
- `page-agent` — AI-driven page interaction

## Usage Examples

```bash
# Capture network HAR
python cdp-har-capture.py --url https://example.com --output site.har

# Profile page load
python cdp-profile.py --url https://example.com --output trace.json

# Debug JS error
python cdp-debug.py --url https://example.com --break-on-error
```

## Error Handling

- **Connection refused:** Chrome not started with `--remote-debugging-port`
- **Target not found:** Tab closed or navigated — re-get target list
- **Session detached:** Browser crashed — implement reconnection logic
- **Command timeout:** CDP command took too long — increase timeout or simplify

## Pitfalls

- **Version mismatch:** CDP protocol changes between Chrome versions — pin Chrome DevTools Protocol Viewer: <https://chromedevtools.github.io/devtools-protocol/>
- **Async complexity:** All CDP commands are async — handle promises/await correctly
- **Security restrictions:** Some domains require `--disable-web-security` for cross-origin
- **Resource cleanup:** Always detach and close targets to avoid zombie processes
- **Headless limitations:** Some features (GPU, extensions) don't work in headless

## References

- CDP Protocol Viewer: <https://chromedevtools.github.io/devtools-protocol/>
- `references/cdp-domains.md` — Domain reference with examples
- `references/cdp-python-client.md` — Python async client patterns
- `references/cdp-typescript-client.md` — TypeScript client patterns
- `references/performance-analysis.md` — Trace analysis methodology