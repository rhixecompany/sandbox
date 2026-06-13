# Playwright MCP Server

**Source:** https://github.com/microsoft/playwright-mcp

## Overview

**Playwright MCP** is a Model Context Protocol (MCP) server that provides browser automation capabilities using [Playwright](https://playwright.dev). It enables LLMs to interact with web pages through **structured accessibility snapshots** rather than screenshots or vision models.

> **Key Differentiator**: Uses Playwright's accessibility tree for deterministic, LLM-friendly automation without pixel-based input or vision models.

## MCP vs CLI: When to Use Which

| Approach | Best For | Trade-offs |
|----------|----------|------------|
| **MCP** (this package) | Exploratory automation, self-healing tests, long-running autonomous workflows, persistent state & rich introspection | Higher token cost (loads tool schemas + accessibility trees) |
| **CLI + Skills** ([playwright-cli](https://github.com/microsoft/playwright-cli)) | High-throughput coding agents, large codebases, limited context windows | More token-efficient; avoids verbose schemas/trees |

> **Recommendation**: Use **CLI + Skills** for coding agents; use **MCP** for specialized agentic loops needing persistent browser context.

## Quick Start

### Standard Configuration (works with most MCP clients)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

### Client-Specific Installation

| Client | Install Command / Config |
|--------|-------------------------|
| **VS Code** | Click badge or use `vscode:mcp/install` URI |
| **Claude Code** | `claude mcp add playwright npx @playwright/mcp@latest` |
| **Claude Desktop** | Follow [MCP guide](https://modelcontextprotocol.io/quickstart/user) |
| **Cursor** | Settings → MCP → Add Server → `npx @playwright/mcp@latest` |
| **Windsurf** | Follow [Windsurf MCP docs](https://docs.windsurf.com/windsurf/cascade/mcp) |
| **Goose** | Advanced → Extensions → Add Custom → STDIO → `npx @playwright/mcp` |
| **Junie** | Type `/mcp` → `Ctrl+A` → Select Playwright |
| **Codex** | Edit `~/.codex/config.toml` with MCP config |
| **Copilot CLI** | `/mcp add` or edit `~/.copilot/mcp-config.json` |
| **Gemini CLI** | Follow [Gemini MCP guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) |
| **Docker** | See [Docker section](#docker) below |

## Configuration Options

All options can be passed via `--args` in MCP config or as environment variables (prefix: `PLAYWRIGHT_MCP_`).

### Core Browser Options

| Option | Description | Default |
|--------|-------------|---------|
| `--browser` | Browser: `chrome`, `firefox`, `webkit`, `msedge` | chromium |
| `--headless` | Run headless | `false` (headed) |
| `--device` | Device emulation (e.g., `"iPhone 15"`) | — |
| `--viewport-size` | Viewport (e.g., `"1280x720"`) | — |
| `--user-agent` | Custom user agent string | — |
| `--executable-path` | Path to browser executable | — |
| `--user-data-dir` | Persistent profile directory | Temp dir |
| `--isolated` | Keep profile in memory (no disk) | `false` |
| `--storage-state` | Path to storage state file | — |
| `--cdp-endpoint` | Connect to existing browser via CDP | — |
| `--extension` | Connect via Playwright Extension (Chrome/Edge) | `false` |

### Network & Security

| Option | Description |
|--------|-------------|
| `--allowed-hosts` | Comma-separated hosts server can serve from (DNS rebinding protection) |
| `--allowed-origins` | Semicolon-separated trusted origins (allowlist) |
| `--blocked-origins` | Semicolon-separated blocked origins (blocklist evaluated first) |
| `--ignore-https-errors` | Ignore HTTPS errors |
| `--proxy-server` | Proxy (e.g., `http://myproxy:3128`) |
| `--proxy-bypass` | Domains to bypass proxy |
| `--grant-permissions` | Permissions to grant (e.g., `geolocation,clipboard-read`) |

### Timeouts

| Option | Default |
|--------|---------|
| `--timeout-action` | 5000ms |
| `--timeout-navigation` | 60000ms |

### Output & Debugging

| Option | Description | Default |
|--------|-------------|---------|
| `--output-dir` | Directory for output files | — |
| `--output-mode` | `file` or `stdout` | `stdout` |
| `--console-level` | `error`, `warning`, `info`, `debug` | `info` |
| `--snapshot-mode` | `full` or `none` | `full` |
| `--image-responses` | `allow` or `omit` | `allow` |
| `--save-session` | Save session to output dir | `false` |

### Capabilities (opt-in via `--caps`)

| Capability | Tools Enabled |
|------------|---------------|
| `core` | Core automation (default) |
| `pdf` | PDF generation |
| `vision` | Coordinate-based mouse interactions |
| `devtools` | Debugging, tracing, video recording |
| `network` | Route mocking, network state |
| `storage` | Cookie/localStorage/sessionStorage management |
| `testing` | Test assertions, locator generation |
| `config` | Get resolved config |

### Initialization Scripts

```bash
# TypeScript file evaluated on Playwright page object
--init-page path/to/init-page.ts

# JavaScript file added as script tag
--init-script path/to/init-script.js
```

## Hermes Integration

For Hermes Agent, add to `config.yaml`:

```yaml
mcp_servers:
  playwright:
    command: "npx"
    args: ["@playwright/mcp@latest"]
    env:
      PLAYWRIGHT_MCP_HEADLESS: "true"
      PLAYWRIGHT_MCP_BROWSER: "chromium"
      PLAYWRIGHT_MCP_CAPS: "core,pdf,network,storage"
    tools:
      include: [navigate, click, fill, screenshot, evaluate, wait_for]
```

Then run:
```bash
hermes mcp test playwright
/reload-mcp
```

## Docker Usage

```bash
docker run -i --rm \
  -v /path/to/output:/output \
  mcr.microsoft.com/playwright/mcp:latest \
  --output-dir /output
```

## References

- GitHub: https://github.com/microsoft/playwright-mcp
- Playwright MCP Configuration: https://playwright.dev/mcp/configuration/options
- mcpservers.org: https://mcpservers.org/servers/Automata-Labs-team/MCP-Server-Playwright
- Playwright CLI (alternative): https://github.com/microsoft/playwright-cli