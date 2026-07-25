---
name: mcp-docker
title: MCP Docker — Container Management & MCP Tool Gateway
description: Exposes all docker MCP gateway tools for adding/removing/configuring MCP servers, code mode, GitHub operations via Docker containers, fetching, and time utilities. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - docker
  - gateway
  - containers
  - devops
---

# MCP Docker

Provides Docker-based MCP server lifecycle management via the Docker MCP gateway. Acts as a tool registry — can add, remove, configure MCP servers, execute code combining multiple tools, and provides GitHub operations.

## Prerequisites

- MCP server: `mcp-docker` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `docker mcp gateway run --profile adminbot`
- Docker must be running locally
- Note: On Windows, this uses WSL2 — may encounter filesystem limitations

## Tools

| Tool | Description |
|------|-------------|
| `mcp_exec` | Execute any MCP tool in the current session |
| `mcp_add` | Add a new MCP server from the catalog |
| `mcp_remove` | Remove an MCP server |
| `mcp_config_set` | Set config for an MCP server |
| `mcp_find` | Search MCP catalog for servers |
| `code_mode` | Run JS combining multiple MCP tools |
| `fetch_generic_url_content` | Fetch URL content (respects robots.txt) |
| `fetch_generic_documentation` | Fetch GitHub repo docs |
| `convert_time` | Timezone conversion |
| `get_me` | Get authenticated GitHub user |
| `create_repository` | Create GitHub repo |
| `create_branch` | Create GitHub branch |
| `create_pull_request` | Create GitHub PR |
| `create_or_update_file` | Create/update GitHub file |
| `delete_file` | Delete GitHub file |
| `fork_repository` | Fork GitHub repo |
| `get_commit` | Get commit details |
| `issue_read` | Get issue details |
| `add_issue_comment` | Add issue comment |
| `sub_issue_write` | Add sub-issue |
| `merge_pull_request` | Merge PR |
| `list_pull_requests` | List PRs |
| `search_issues` | Search issues |
| `search_pull_requests` | Search PRs |
| `search_repositories` | Search repos |
| `search_code` | Search code |
| `assign_copilot_to_issue` | Assign Copilot agent |

## Workflow

### Phase 1: Verify

```
hermes mcp test mcp-docker
```

### Phase 2: Core MCP Management

```
# Find servers in catalog
mcp_find(query: "code analysis")

# Add a server
mcp_add(server_name: "n8n")

# Remove
mcp_remove(server: "server-name")

# Execute any tool
mcp_exec(tool_name: "any-tool", args: {})
```

### Phase 3: GitHub Operations

```
# Read
get_me()
search_repositories(query: "astro theme dark")
issue_read(owner: "user", repo: "repo-name", issue_number: 1)

# Write (⚠️)
create_issue(owner: "user", repo: "repo-name", title: "title", body: "body")
```

### Phase 4: Utilities

```
# Timezone
convert_time(source_timezone: "America/New_York", target_timezone: "Asia/Tokyo", time: "09:00")

# Code mode — compose tools
code_mode(code: "async () => { return 'hello'; }")
```

### Phase 5: Test Cases

```bash
# 1. Connectivity
hermes mcp test mcp-docker

# 2. Search catalog
# Call: mcp_mcp_docker_mcp_find(query: "github")

# 3. GitHub self-info (read-only)
# Call: mcp_mcp_docker_get_me()

# 4. Timezone conversion
# Call: mcp_mcp_docker_convert_time(source_timezone="UTC", target_timezone="US/Eastern", time="12:00")

# 5. Search repositories
# Call: mcp_mcp_docker_search_repositories(query="mcp server language:typescript")
```

## Best Practices

1. **Use `mcp_find` before `mcp_add`** — confirm server exists in catalog before attempting to add
2. **Prefer native MCP tools** over docker-gateway equivalents when both are available (lower latency)
3. **`code_mode` is powerful** — it lets you chain tools from different servers in one call
4. **Docker profile `adminbot`** is configured — keep consistent naming
5. **Use `convert_time`** for timezone-related queries (meetings, deadlines across timezones)

## Pitfalls

- Docker must be **running** — no Docker daemon = all tools fail
- On Windows, Docker uses WSL2 — expect some filesystem path translation quirks
- The `mcp-exec` tool bypasses visibility — useful for tools that aren't in `listTools`
- `code_mode` creates JS functions — avoid infinite loops or resource exhaustion
- GitHub operations through this gateway are **separate** from the native `github` MCP server — choose one path consistently
- Profile-specific (currently `adminbot`) — changing the profile in config affects available tools

## Verification Checklist

- [ ] `hermes mcp test mcp-docker` passes
- [ ] `get_me` returns GitHub user info
- [ ] `mcp_find` returns catalog results
- [ ] `convert_time` produces correct conversion
