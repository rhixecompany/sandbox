# Apify MCP Server - Comprehensive Summary

## Overview

The **Apify MCP Server** ([mcp.apify.com](https://mcp.apify.com)) enables AI agents to extract data from social media, search engines, maps, e-commerce sites, and any website using thousands of ready-made scrapers, crawlers, and automation tools from [Apify Store](https://apify.com/store).

**Key Features:**
- Supports OAuth for easy connection from Claude.ai, VS Code, Cursor, and other MCP clients
- Compatible with any client adhering to the Model Context Protocol
- Hosted server at `https://mcp.apify.com` (recommended) or local stdio via `npx @apify/actors-mcp-server`
- Supports agentic payments via x402 and Skyfire (no API token needed)

---

## Quickstart

### Two Connection Methods:

**1. HTTPS Endpoint (Recommended)**
```
https://mcp.apify.com
```
- Connect via OAuth or include `Authorization: Bearer <APIFY_TOKEN>` header
- Supports latest features like output schema inference

**2. Standard Input/Output (stdio)**
```bash
npx @apify/actors-mcp-server
```
- Requires `APIFY_TOKEN` environment variable
- Ideal for local integrations and command-line tools

---

## ⚠️ Important: SSE Transport Deprecation

**April 1, 2026**: Apify is dropping Server-Sent Events (SSE) transport in favor of Streamable HTTP per the official MCP spec. Update your client config before this date.

---

## Agentic Payments

Pay for Actor runs without an Apify API token using **x402** or **Skyfire**.

### Payment Flow (4 steps):
1. Search for Actors (`search-actors`)
2. Fetch Actor details (`fetch-actor-details`)
3. Create payment token (`mcpc create-pay-token`)
4. Execute Actor run

### x402 Protocol
- Machine-to-machine payments using USDC on Base blockchain
- Bypasses need for Apify API token
- Requires wallet setup

### Skyfire
- Managed payment infrastructure for AI agents
- Uses PAY tokens
- Add `payment=skyfire` to server URL

---

## Tools Overview

### Default Tools (Enabled by default marked with ✅)

| Tool | Category | Description |
|------|----------|-------------|
| `search-actors` | actors | Search for Actors in Apify Store |
| `fetch-actor-details` | actors | Get Actor details, input schema, README, pricing |
| `call-actor` | actors | Call an Actor and get results |
| `search-apify-docs` | docs | Search Apify documentation |
| `fetch-apify-docs` | docs | Fetch full documentation page |
| `apify--rag-web-browser` | Actor | Web browsing tool |

### Additional Tools (⚡ = auto-injected when needed)

| Tool | Category | Description |
|------|----------|-------------|
| `get-actor-run` | runs | Get specific Actor run details |
| `get-dataset-items` | storage | Retrieve dataset items with filtering/pagination |
| `get-key-value-store-record` | storage | Get value from key-value store |
| `abort-actor-run` | runs | Abort a running Actor |
| `get-actor-run-list` | runs | List Actor runs by status |
| `get-actor-log` | runs | Retrieve Actor run logs |
| `get-dataset` | storage | Get dataset metadata |
| `get-dataset-schema` | storage | Generate JSON schema from dataset |
| `get-key-value-store` | storage | Get key-value store metadata |
| `get-key-value-store-keys` | storage | List keys in key-value store |
| `get-dataset-list` | storage | List all datasets |
| `get-key-value-store-list` | storage | List all key-value stores |
| `add-actor` | experimental | Add Actor as new tool |

**Note:** When `call-actor` or Actor tools are used, `get-actor-run`, `get-dataset-items`, `get-key-value-store-record`, and `abort-actor-run` are auto-injected.

---

## Tools Configuration

### Default Configuration
When no `tools` parameter is specified:
- `actors` category
- `docs` category
- `apify/rag-web-browser` Actor

### Hosted Server Configuration
```
https://mcp.apify.com?tools=actors,docs,apify/rag-web-browser
```

Minimal (single Actor only):
```
https://mcp.apify.com?tools=apify/my-actor
```

### CLI Configuration
```bash
npx @apify/actors-mcp-server --tools actors,docs,apify/rag-web-browser
```

### UI Mode
Enable interactive MCP App widgets:
```
https://mcp.apify.com?ui=true
```

### ⚠️ Production Recommendation
**Always explicitly specify the `tools` parameter** for stable interfaces across updates.
