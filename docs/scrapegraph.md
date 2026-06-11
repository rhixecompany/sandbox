# ScrapeGraph MCP Server

**Source:** https://github.com/scrapegraphai/scrapegraph-mcp

> Note: The original URL `https://github.com/scrapegraphaiiscrapegraph-mcp` returned a 404. The correct repository is `https://github.com/scrapegraphai/scrapegraph-mcp`.

## Overview

**ScrapeGraph MCP Server** is a production-ready [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that integrates with the [ScrapeGraph AI API v2](https://v2-api.scrapegraphai.com/api), enabling AI assistants (Claude, Cursor, Google ADK agents) to perform advanced AI-powered web scraping with enterprise-grade reliability.

- **License:** MIT
- **Python:** 3.13+
- **Repository:** `ScrapeGraphAI/scrapegraph-mcp` (96 commits)
- **Smithery:** [@ScrapeGraphAI/scrapegraph-mcp](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

---

## API v2 Configuration

- **Base URL:** `https://v2-api.scrapegraphai.com/api`
- **Auth header:** `SGAI-APIKEY`
- **Environment variables:**

| Variable | Default | Notes |
|---|---|---|
| `SGAI_API_URL` | `https://v2-api.scrapegraphai.com/api` | Legacy alias: `SCRAPEGRAPH_API_BASE_URL` |
| `SGAI_API_KEY` | — | Also accepts `scrapegraphApiKey`, `X-API-Key` |
| `SGAI_TIMEOUT` | `120` | Legacy alias: `SGAI_TIMEOUT_S` |

---

## Migration: v2 → v3 (Hard Rename, No Aliases)

| v2 (old) | v3 (new) |
|---|---|
| `smartscraper` | `extract` |
| `searchscraper` | `search` |
| `smartcrawler_initiate` | `crawl_start` |
| `smartcrawler_fetch_results` | `crawl_get_status` |
| `sgai_history` | `history` |
| `generate_schema` | `schema` |
| `markdownify` | **removed** — use `scrape` with `output_format="markdown"` |

**Removed tools:** `sitemap`, `agentic_scrapper`, async-status polling.

---

## Available Tools

| Tool | HTTP | Key Parameters |
|---|---|---|
| `scrape` | POST /scrape | `output_format`: markdown, html, screenshot, branding, links, images, summary |
| `extract` | POST /extract | `website_url` + `user_prompt`; optional `output_schema` |
| `search` | POST /search | `num_results` (1–20); `country_search`, `time_range`, `output_schema` |
| `crawl_start` | POST /crawl | `extraction_mode`: markdown / html / links / images / summary / branding / screenshot |
| `crawl_get_status` | GET /crawl/:id | Poll until `status: completed` |
| `crawl_stop` / `crawl_resume` | POST /crawl/:id/stop | — |
| `schema` | POST /schema | Generate or augment a JSON Schema from a prompt |
| `credits` | GET /credits | — |
| `history` | GET /history | Paginated; `service` filter |
| `monitor_create`, `monitor_list`, `monitor_get`, `monitor_pause`, `monitor_resume`, `monitor_delete` | /monitor API | — |
| `monitor_activity` | GET /monitor/:id/activity | Paginated tick history: `id`, `createdAt`, `status`, `changed`, `elapsedMs`, `diffs` |

---

## Quick Start

### 1. Get API Key
Sign up at the [ScrapeGraph Dashboard](https://dashboard.scrapegraphai.com).

### 2. Install via Smithery (Recommended)
Use Smithery for automated installation of the ScrapeGraph API Integration Server.

### 3. Start Using
Ask Claude or Cursor — the server is immediately available to your AI assistant.

---

## Setup Instructions

### Claude Desktop Configuration

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

### Cursor Integration
Add the ScrapeGraphAI MCP server in Cursor's settings (top right of the Cursor page).

---

## Remote Server Usage

No local installation required. Connect to the hosted MCP server.

### Claude Desktop (Remote)
Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS).

### Cursor (Remote)
Add to `~/.cursor/mcp.json`. Cursor supports native HTTP MCP connections.

### Benefits of Remote Server
- No local setup or maintenance
- Always up-to-date
- Scalable infrastructure

---

## Local Usage

### Prerequisites
- Python 3.13+
- ScrapeGraph API key

### Installation
Install from source using `pyproject.toml`.

### Running the Server
The server communicates via **stdio** (standard MCP transport).

### Testing with MCP Inspector
Provides a web interface to test all available tools interactively.

### Claude Desktop (Local)

**macOS/Linux:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

> **Note:** Ensure Python is in your PATH (`python --version`).

### Cursor (Local)
In Cursor's MCP settings, add a new server with:
- Command: `python`
- Args: `["-m", "scrapegraph_mcp.server"]`
- Env: `{"SGAI_API_KEY": "your-api-key-here"}`

---

## Google ADK Integration

Integrate with [Google Agent Development Kit](https://github.com/google/adk) to create AI agents with web scraping capabilities.

### Configuration Options
- **Timeout settings:** Configurable
- **Tool filtering:** Use `tool_filter`
- **API key:** `export SGAI_API_KEY=your-key` or via `env` dict: `'SGAI_API_KEY': 'your-key-here'`

### Usage
Agents use natural language to interact with web scraping tools.

---

## Example Use Cases

| Scenario | Tools Used |
|---|---|
| Single page scraping | `scrape` |
| Search and research | `search` (with `time_range`, `country_search`) |
| Structured data extraction | `extract` with `output_schema` |
| Multi-page crawling | `crawl_start` → `crawl_get_status` |
| Scheduled monitoring | `monitor_create` + `monitor_activity` |
