# ScrapeGraph MCP Server

**Source:** https://github.com/ScrapeGraphAI/scrapegraph-mcp

## Overview

**ScrapeGraph MCP Server** is a production-ready Model Context Protocol (MCP) server providing seamless integration with the **ScrapeGraph AI API v2** (`https://v2-api.scrapegraphai.com/api`). It enables language models to leverage advanced AI-powered web scraping with enterprise-grade reliability.

- **License:** MIT
- **Python:** 3.13+
- **Repository:** `github.com/ScrapeGraphAI/scrapegraph-mcp`
- **API Base URL:** `https://v2-api.scrapegraphai.com/api`
- **Auth Header:** `SGAI-APIKEY`

## Key Features & Tools

| Tool | API Endpoint | Description |
|------|--------------|-------------|
| `scrape` | `POST /scrape` | Single page scraping with `output_format`: markdown, html, screenshot, branding, links, images, summary |
| `extract` | `POST /extract` | Structured extraction requiring `website_url` + `user_prompt`; optional `output_schema` |
| `search` | `POST /search` | Web search with `num_results` (1–20), `country_search`, `time_range`, `output_schema` |
| `crawl_start` | `POST /crawl` | Initiate crawl with `extraction_mode`: markdown/html/links/images/summary/branding/screenshot |
| `crawl_get_status` | `GET /crawl/:id` | Poll until `status: completed` |
| `crawl_stop` / `crawl_resume` | `POST /crawl/:id/stop \| resume` | Control crawl execution |
| `schema` | `POST /schema` | Generate/augment JSON Schema from prompt |
| `credits` | `GET /credits` | Check account credits |
| `history` | `GET /history` | Paginated history with `service` filter |
| `monitor_create` / `list` / `get` / `pause` / `resume` / `delete` | `/monitor` API | Monitor management |
| `monitor_activity` | `GET /monitor/:id/activity` | Paginated tick history: `id`, `createdAt`, `status`, `changed`, `elapsedMs`, `diffs` |

**Removed in v3:** `sitemap`, `agentic_scrapper`, async-status polling, `markdownify` (use `scrape` with `output_format="markdown"`)

## Migration: v2 → v3 (Breaking Changes)

| v2 (Old) | v3 (New) |
|----------|----------|
| `smartscraper` | `extract` |
| `searchscraper` | `search` |
| `smartcrawler_initiate` | `crawl_start` |
| `smartcrawler_fetch_results` | `crawl_get_status` |
| `sgai_history` | `history` |
| `generate_schema` | `schema` |
| `markdownify` | **Removed** — use `scrape` with `output_format="markdown"` |

> **Hard rename, no aliases.**

## Environment Variables

```bash
# Required
SGAI_API_KEY=your-api-key-here          # Primary (also accepted: scrapegraphApiKey, X-API-Key)

# Optional (with defaults)
SGAI_API_URL=https://v2-api.scrapegraphai.com/api
SGAI_TIMEOUT=120

# Legacy aliases (still honored)
SCRAPEGRAPH_API_BASE_URL  # → SGAI_API_URL
SGAI_TIMEOUT_S            # → SGAI_TIMEOUT
```

## Quick Start

### 1. Get API Key

Sign up at [ScrapeGraph Dashboard](https://dashboard.scrapegraphai.com)

### 2. Install via Smithery (Recommended)

```bash
# Automated installation
smithery install @ScrapeGraphAI/scrapegraph-mcp
```

### 3. Configure Claude Desktop

**macOS/Linux:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "scrapegraph": {
      "command": "python",
      "args": ["-m", "scrapegraph_mcp.server"],
      "env": {
        "SGAI_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 4. Cursor Integration

Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "scrapegraph": {
      "command": "python",
      "args": ["-m", "scrapegraph_mcp.server"],
      "env": { "SGAI_API_KEY": "your-api-key-here" }
    }
  }
}
```

## Remote Server Usage (No Local Install)

### Claude Desktop (Remote)

```json
{
  "mcpServers": {
    "scrapegraph-remote": {
      "url": "https://mcp.scrapegraphai.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

### Cursor (Remote)

```json
{
  "mcpServers": {
    "scrapegraph-remote": {
      "url": "https://mcp.scrapegraphai.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**Benefits:** No local dependencies, automatic updates, managed infrastructure.

## Local Development Setup

### Prerequisites

- Python 3.13+
- `uv` (recommended) or `pip`

### Installation

```bash
git clone https://github.com/ScrapeGraphAI/scrapegraph-mcp.git
cd scrapegraph-mcp
uv sync  # or: pip install -e .
```

### Run Locally

```bash
# Direct execution (stdio transport)
python -m scrapegraph_mcp.server

# With MCP Inspector (web UI for testing)
npx @modelcontextprotocol/inspector python -m scrapegraph_mcp.server
```

### Configure for Local Use

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "scrapegraph-local": {
      "command": "python",
      "args": ["-m", "scrapegraph_mcp.server"],
      "env": { "SGAI_API_KEY": "your-api-key-here" }
    }
  }
}
```

## Google ADK Integration

```python
# agent.py
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPTool

scrapegraph_tools = [
    MCPTool(
        name="scrape",
        description="Scrape a single page",
        url="http://localhost:8080/mcp"  # or remote URL
    ),
]
```

## Hermes Integration

For Hermes Agent (local stdio mode):

```yaml
mcp_servers:
  scrapegraph:
    command: "python"
    args: ["-m", "scrapegraph_mcp.server"]
    env:
      SGAI_API_KEY: "${SGAI_API_KEY}"
      SGAI_API_URL: "https://v2-api.scrapegraphai.com/api"
      SGAI_TIMEOUT: "120"
    tools:
      include: [scrape, extract, search, crawl_start, crawl_get_status]
```

For Remote HTTP mode:
```yaml
mcp_servers:
  scrapegraph:
    url: "https://mcp.scrapegraphai.com/mcp"
    transport: "streamable-http"
    headers:
      Authorization: "Bearer ${SGAI_API_KEY}"
    tools:
      include: [scrape, extract, search, crawl_start, crawl_get_status]
```

Then run:
```bash
hermes mcp test scrapegraph
/reload-mcp
```

## References

- GitHub: https://github.com/ScrapeGraphAI/scrapegraph-mcp
- Dashboard: https://dashboard.scrapegraphai.com
- Remote MCP: https://mcp.scrapegraphai.com/mcp
- Smithery: https://docs.scrapegraphai.com/services/mcp-server/smithery
- mcp.so: https://mcp.so/server/scrapegraph-mcp/ScrapeGraphAI