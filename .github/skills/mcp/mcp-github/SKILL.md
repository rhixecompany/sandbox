---
name: mcp-github
title: MCP GitHub — Repository & Code Management
description: Exposes all native github MCP tools for repository management, issue tracking, pull requests, code search, file operations, and commits. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - github
  - git
  - repository
  - issues
  - pull-requests
---

# MCP GitHub

Provides native GitHub API access via the standard `@modelcontextprotocol/server-github`. Covers repository, issue, PR, code search, and file management operations.

## Prerequisites

- MCP server: `github` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y @modelcontextprotocol/server-github`
- GitHub token (`GITHUB_TOKEN`) must be configured in `.env`

## Tools

| Tool | Description |
|------|-------------|
| `create_repository` | Create a new repo in your account |
| `fork_repository` | Fork a repo to your account |
| `search_repositories` | Search repos by name, description, topics |
| `get_repository` | Get repo details |
| `search_code` | Search code across all GitHub repos |
| `search_issues` | Search issues & PRs across repos |
| `get_issue` | Get issue details |
| `create_issue` | Create a new issue |
| `update_issue` | Update an existing issue |
| `add_issue_comment` | Add comment to an issue |
| `create_pull_request` | Create a new PR |
| `create_pull_request_review` | Create a PR review |
| `create_or_update_file` | Create/update a single file |
| `push_files` | Push multiple files in one commit |
| `create_branch` | Create a new branch |
| `list_commits` | List commits on a branch |
| `get_commit` | Get commit details |

## Workflow

### Phase 1: Verify

```
hermes mcp test github
```

### Phase 2: Read Operations

```
# Repos
search_repositories(query: "topic:astro theme:dark language:css")
get_repository(owner: "user", repo: "repo-name")

# Code
search_code(query: "function fibonacci path:/src/ language:python repo:user/repo")

# Issues
search_issues(query: "is:issue is:open label:bug repo:user/repo")
get_issue(owner: "user", repo: "repo-name", issue_number: 1)
list_commits(owner: "user", repo: "repo-name", page: 1, per_page: 10)
```

### Phase 3: Write Operations (⚠️ destructive)

```
create_issue(owner: "user", repo: "repo-name", title: "Bug", body: "Description")
create_pull_request(owner: "user", repo: "repo-name", title: "PR", head: "branch", base: "main")
create_or_update_file(owner: "user", repo: "repo-name", path: "file.py", content: "print('hi')", message: "init")
push_files(owner: "user", repo: "repo-name", branch: "main", files: [{path: "a.txt", content: "hello"}], message: "commit")
```

### Phase 4: Test Cases

```bash
# 1. Connectivity
hermes mcp test github

# 2. Search repositories
# Call: mcp_github_search_repositories(query="org:modelcontextprotocol servers")

# 3. Read-only issue check (use an existing repo)
# Call: mcp_github_get_issue(owner="NourResearch", repo="hermes-agent", issue_number=1)

# 4. Search code
# Call: mcp_github_search_code(query="console.log language:javascript repo:expressjs/express")

# 5. List commits
# Call: mcp_github_list_commits(owner="NourResearch", repo="hermes-agent", page: 1, per_page: 5)
```

## Best Practices

1. **Search before creating** — always check if a repo/issue/PR already exists
2. **Use `search_code`** for cross-repo code discovery; scope with `repo:` qualifier
3. **`push_files` is atomic** — all files in one commit, use for multi-file changes
4. **Include `issue_number` as numeric** — strings cause type errors
5. **Create branches before pushing** — use `create_branch` then `push_files`
6. **Prefer `search_issues`** over `get_issue` when you don't have the exact issue number

## Pitfalls

- Requires valid `GITHUB_TOKEN` in `.env` with appropriate scopes (repo, issues, etc.)
- API rate-limited to 5,000 requests/hour for authenticated users
- `create_or_update_file` needs the file's `sha` when updating — get it from `get_repository` or `git rev-parse`
- `fork_repository` only works for public repos your account can access
- `search_code` respects GitHub search limits (indexed code only, not all branches)
- Write operations create real GitHub artifacts — use interactively, test params before calling
- Organization repos may require different auth scopes

## Verification Checklist

- [ ] `hermes mcp test github` passes
- [ ] `search_repositories` returns results
- [ ] `get_issue` returns a valid issue
- [ ] `search_code` returns code matches
- [ ] `list_commits` returns commit history
