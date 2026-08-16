---
name: mcp-server-health
title: "MCP Server Health — Use, Test, Execute"
description: "Use to test all 17 MCP servers with scripts and hooks."
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - health
  - testing
  - diagnostics
  - monitoring
  - hooks
---

# MCP Server Health — Use, Test, Execute

## Overview

Systematic workflow for testing, verifying, and monitoring all 17 MCP servers configured in Hermes. Each server is tested by sending a real MCP initialize handshake and confirming it responds with its capabilities.

## When to Use

- After configuring or modifying MCP servers
- When MCP tools fail to appear in the tool list
- After a Hermes update or gateway restart
- Before important sessions that depend on specific MCP servers
- As a preflight hook before every LLM call

## Server Inventory

### Group 1: npm-based (npx)

| Server | Package | Tools |
|--------|---------|-------|
| `ast-grep` | `@notprolands/ast-grep-mcp` | Code search, AST analysis, rewrite |
| `code-sandbox` | `@anthropic/mcp-code-sandbox` | Isolated JS/Node execution |
| `fetch` | `@anthropic/mcp-fetch` | Web content extraction |
| `filesystem` | `@modelcontextprotocol/server-filesystem` | File read/write/edit |
| `github` | `@anthropic/mcp-github` or native | GitHub API (PRs, issues, code) |
| `memory` | `@anthropic/mcp-memory` | Knowledge graph memory |
| `playwright` | `@playwright/mcp` | Browser automation |
| `sequential-thinking` | `@modelcontextprotocol/server-sequential-thinking` | Structured reasoning |
| `tavily` | npx-based | Web search & research |
| `parallel-search` | npx-based | Parallel web search |
| `parallel-task` | npx-based | Batch data enrichment |

### Group 2: Python-based (direct)

| Server | Script | Tools |
|--------|--------|-------|
| `python-quality` | `.github/scripts/python_quality_mcp_server.py` | Ruff lint/format, Pyright typecheck |
| `tooling-lint` | `.github/scripts/tooling_lint_mcp_server.py` | ESLint, Prettier, Markdownlint, CSpell |
| `tooling-config` | `.github/scripts/tooling_config_mcp_server.py` | Pre-commit, git-cliff, .gitignore, .editorconfig |

### Group 3: Direct command

| Server | Command | Tools |
|--------|---------|-------|
| `mindstudio` | `mindstudio` binary | 197 MindStudio actions (Google, Slack, Gmail, Telegram, etc.) |
| `mcp-docker` | `docker` + gateway | GitHub, fetch, code, time via Docker containers |

### Group 4: Plugin-based

| Server | Source | Tools |
|--------|--------|-------|
| `alexanderrhixe30` | Smithery plugin | 116 tools (Exa, Gmail, Google Tasks, Notion, PubMed, Smithery API) |

## Quick Reference

```bash
# List all servers and their status
hermes mcp list

# Test a single server
hermes mcp test <server-name>

# Full automated test (from workspace root)
python scripts/test_all_mcp_servers.py

# Preflight check (hook-friendly)
python scripts/mcp_preflight_check.py
```

## Testing Workflow

### Phase 1: Verify Connectivity

Run `hermes mcp list`. For any server showing disabled or 0 tools, run:
```bash
hermes mcp test <server-name>
```

### Phase 2: Initialize Handshake Test

Each MCP server must complete an initialize handshake. Use the test script:
```bash
python scripts/test_all_mcp_servers.py
```

Output: `PASS` (handshake completed) or `FAIL` (process died, timed out, or error).

### Phase 3: Tool Execution Test

For servers that pass handshake, test a basic tool via Hermes:
```bash
hermes mcp call fetch get_markdown '{"url": "https://example.com"}'
hermes mcp call sequential-thinking sequentialthinking '{"thought": "Test connectivity"}'
hermes mcp call python-quality python_lint '{"path": "."}'
```

### Phase 4: Preflight Hook

Wire the preflight check as a `pre_llm_call` hook:
```yaml
hooks:
  pre_llm_call:
    - command: "C:/Program Files/Git/usr/bin/bash.exe"
      args: ["-c", "python /path/to/mcp_preflight_check.py --hook --critical ast-grep,github,fetch"]
      timeout: 30
      allowed: true
```

## Per-Server Test Commands

### Direct handshake (npm-based)
```bash
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}' | npx -y @notprolands/ast-grep-mcp 2>/dev/null | head -5
```

### Direct handshake (Python-based)
Use the test script which sends the initialize handshake programmatically.

### Plugin-based (via Hermes MCP)
```bash
hermes mcp call alexanderrhixe30 get_toolbox_status '{}'
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|------|
| `Connection closed` | Server died during init | Run directly; check FastMCP API compat |
| `McpError: Timeout` | Too slow | Increase `connect_timeout` |
| `Tool not found` | Server registered but call failed | `hermes mcp list` to verify tool count |
| `Failed after N attempts` | Persistent failure | Disable/re-enable; check wrapper path |
| `Parked until reconnect` | 3 retries exhausted | `hermes mcp test <name>` to reconnect |
| `enabled: false` | Disabled in config | `hermes config set mcp.servers.<name>.enabled true` |

## Scripts

- `scripts/test_all_mcp_servers.py` — Comprehensive test of all 17 MCP servers
- `scripts/mcp_preflight_check.py` — Lightweight health check, hook-ready

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "MCP Server Health — Use, Test, Execute" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "MCP Server Health — Use, Test, Execute".

### Phase 2: Execution

Run the primary "MCP Server Health — Use, Test, Execute" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
