---
name: mcp-smithery
title: MCP Smithery — Tool Registry & GitHub Operations Hub
description: Exposes all Smithery MCP tools for toolbox search/management, GitHub operations (PRs, issues, repos, commits, actions, projects, notifications, security, code search), Context7 documentation, and sandboxed multi-tool execution. Includes test cases per tool group.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - smithery
  - github
  - toolbox
  - registry
metadata:
  hermes:
    tags: []
---
# MCP Smithery

Smithery acts as a centralized tool registry and GitHub operations hub. It provides toolbox management, extensive GitHub API coverage, Context7 documentation lookup, and sandboxed JavaScript execution for chaining tools.

## Overview

Automated reasoning and workflow tool for `mcp-smithery`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `smithery` must be enabled (`hermes mcp list` → `✓ enabled`)
- URL: `https://mcp.smithery.run/rhixecompany`
- Auth: OAuth (logged in via `hermes auth`)

## Tools

### Toolbox Management
| Tool | Description |
|------|-------------|
| `search_toolbox` | Fuzzy-search all installed MCP tools across all connections |
| `get_toolbox_status` | Check health of every connected server |
| `remove_server` | Remove a server connection by ID |
| `execute` | Run JS sandbox with full tool access (`connections.<server>.<tool>`) |

### GitHub — Read
| Tool | Description |
|------|-------------|
| `get_me` | Get authenticated GitHub user |
| `get_commit` | Get commit details |
| `get_issue` | Get issue info |
| `issue_read` | Get issue details |
| `get_notification_details` | Get notification details |
| `list_notifications` | List all GitHub notifications |
| `list_starred_repositories` | List starred repos |
| `list_repository_collaborators` | List repo collaborators |
| `list_repository_security_advisories` | List security advisories |
| `list_pull_requests` | List PRs |
| `list_code_scanning_alerts` | List code scanning alerts |
| `list_issue_types` | List supported issue types |
| `get_copilot_space` | Get Copilot space documents |

### GitHub — Search
| Tool | Description |
|------|-------------|
| `search_code` | Fast code search across all GitHub repos |
| `search_issues` | Search issues with GitHub search syntax |
| `search_pull_requests` | Search PRs with GitHub search syntax |
| `search_commits` | Search commits across repos |
| `search_repositories` | Search repos by metadata |

### GitHub — Write (⚠️)
| Tool | Description |
|------|-------------|
| `create_repository` | Create a new repo |
| `create_branch` | Create a branch |
| `create_pull_request` | Create a PR |
| `create_gist` | Create a gist |
| `push_files` | Push multiple files in one commit |
| `delete_file` | Delete a file |
| `fork_repository` | Fork a repo |
| `merge_pull_request` | Merge a PR |
| `issue_write` | Create or update an issue |
| `issue_read` | Get issue info |
| `add_issue_comment` | Add comment/reaction |
| `label_write` | Manage repo labels |
| `mark_all_notifications_read` | Clear all notifications |

### GitHub — CI/CD & Projects
| Tool | Description |
|------|-------------|
| `actions_list` | List workflows/runs/jobs/artifacts |
| `actions_get` | Get workflow/run/job/artifact details |
| `get_job_logs` | Get job logs (single or all failed) |
| `projects_list` | List GitHub Projects |
| `projects_get` | Get project details |
| `projects_write` | Create/manage projects and items |
| `check_dependency_vulnerabilities` | Check deps against GitHub Advisory DB |

### Context7
| Tool | Description |
|------|-------------|
| `context7_mcp_query_docs` | Query latest library docs |
| `context7_mcp_resolve_library_id` | Resolve library name to Context7 ID |

## Workflow

### Phase 1: Verify

```
hermes mcp test smithery
```

### Phase 2: Toolbox Management

```
# Health check all servers
get_toolbox_status()

# Search for tools
search_toolbox(query: "github search code")

# Execute chained tools
execute(code: "async () => { const repos = await connections['github'].search_repositories({query: 'mcp'}); return repos; }")
```

### Phase 3: GitHub Operations

```
# Self
get_me()
list_notifications()
get_notification_details(id: "notification-id")

# Search
search_code(query: "function fibonacci language:python")
search_issues(query: "is:open label:bug repo:user/repo")
search_repositories(query: "topic:mcp-server")
search_pull_requests(query: "is:open is:pr repo:user/repo")

# Browse
list_pull_requests(owner: "user", repo: "repo")
get_commit(owner: "user", repo: "repo", commit_sha: "abc123")
```

### Phase 4: Test Cases

```bash
# 1. Connectivity
hermes mcp test smithery

# 2. Toolbox search (read-only)
# Call: mcp_smithery_search_toolbox(query: "github search")

# 3. Toolbox health (read-only)
# Call: mcp_smithery_get_toolbox_status()

# 4. GitHub self (read-only)
# Call: mcp_smithery_github_get_me()

# 5. GitHub code search (read-only)
# Call: mcp_smithery_github_search_code(query: "console.log language:javascript")

# 6. GitHub notification check (read-only)
# Call: mcp_smithery_github_list_notifications()
```

## Best Practices

1. **Use `get_toolbox_status`** first when diagnosing "tool not found" errors — shows which servers need re-auth
2. **`search_toolbox`** is the primary discovery tool — fuzzy-searches across ALL installed servers
3. **Use `execute` for chaining** when you need to combine results from multiple servers in one turn
4. **Prefer `search_issues` over `list_pull_requests`** when you need author-specific or label-specific queries
5. **Resolve Context7 library IDs** before querying docs — `context7_mcp_resolve_library_id` first, then `context7_mcp_query_docs`

## Pitfalls

- OAuth tokens expire — re-auth via `hermes login --provider smithery` if `get_toolbox_status` shows `auth_required`
- `execute` code must be an **async arrow function** — `async () => { ... }` format only
- `remove_server` deletes the connection permanently — credentials cannot be recovered
- Context7 queries need a valid library ID — resolve first, or pass `/org/project/version` format directly
- GitHub API rate limits apply (5,000/hr) — cross-server operations consume from the same bucket
- `list_notifications` vs `get_notification_details`: list first, then get details for specific IDs
- `search_commits` searches the default branch only
- `list_notifications` returns 403 with GitHub App integration tokens (scoped to repo-only). Use `search_issues`/`search_pull_requests` with `owner`/`repo` filters instead for actionable items
- Some GitHub tools require specific OAuth scopes — check if 403 errors appear

## Verification Checklist

- [ ] `hermes mcp test smithery` passes
- [ ] `get_toolbox_status` returns server health
- [ ] `search_toolbox` returns results
- [ ] `get_me` returns GitHub user
- [ ] `search_code` returns code matches

## When to Use


- When you need to perform MCP Smithery — Tool Registry & GitHub Operations Hub operations or tasks
- When managing MCP Smithery — Tool Registry & GitHub Operations Hub infrastructure or configurations
- When automating or debugging MCP Smithery — Tool Registry & GitHub Operations Hub workflows
- **Triggers**: "mcp smithery — tool registry & github operations hub" required for a project
