---
name: mcp-fetch
title: MCP Fetch — Web Content Extraction
description: Exposes all fetch MCP tools for extracting web page content as markdown, listing resources, reading resources by URI, and managing prompts. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - fetch
  - web
  - content-extraction
---

# MCP Fetch

Provides web page content extraction via the standard fetch MCP server. Converts HTML pages to clean Markdown for further processing.

## Prerequisites

- MCP server: `fetch` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y mcp-server-fetch-typescript`

## Tools

| Tool | Description |
|------|-------------|
| `get_markdown` | Fetch a URL and return as well-formatted Markdown (preserves tables, lists) |
| `list_resources` | List available resources from the fetch server |
| `read_resource` | Read a resource by URI |
| `list_prompts` | List available prompts from the fetch server |
| `get_prompt` | Get a prompt by name |

## Workflow

### Phase 1: Verify

```
hermes mcp test fetch
```

### Phase 2: Use Tools

**Fetch web content:**
```
get_markdown(url: "https://example.com")
```

**Resource operations:**
```
list_resources()
read_resource(uri: "fetch://...")
```

**Prompt operations:**
```
list_prompts()
get_prompt(name: "summarize")
```

### Phase 3: Test Cases

```bash
# 1. Connectivity
hermes mcp test fetch

# 2. Fetch a simple URL
# Call: mcp_fetch_get_markdown(url="https://raw.githubusercontent.com/nicepkg/ast-grep-mcp/main/README.md")

# 3. List resources (should return available fetch resources)
# Call: mcp_fetch_list_resources()

# 4. List prompts
# Call: mcp_fetch_list_prompts()
```

## Best Practices

1. **Prefer `get_markdown`** over raw HTTP — handles HTML-to-markdown conversion automatically
2. **Use for documentation URLs** — READMEs, docs pages, API references
3. **Combine with web_search** for preliminary link discovery
4. **Raw content URLs** (plain .md, .txt, .json endpoints) may be better served via `curl` in terminal

## Pitfalls

- May respect `robots.txt` — some sites block automated fetching
- Large pages (>2M chars) are rejected — use browser tools for complex pages
- JavaScript-rendered content won't appear — only server-side HTML is extracted
- Authentication-required pages (behind login) won't work — use browser tools for those
- Rate limits apply — some CDNs return 429 on rapid requests

## Verification Checklist

- [ ] `hermes mcp test fetch` passes
- [ ] `get_markdown` returns clean text for a public URL
- [ ] `list_resources` returns without error
