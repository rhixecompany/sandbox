# GitHub MCP Server

**Source:** <https://github.com/github/github-mcp-server>

## Overview

**GitHub MCP Server** connects AI tools directly to GitHub's platform, enabling AI agents, assistants, and chatbots to:

- Read repositories and code files
- Manage issues and PRs
- Analyze code
- Automate workflows
- All through natural language interactions

**Repository:** `github/github-mcp-server` | **Language:** Go | **License:** MIT | **Commits:** 930+

## Quick Start Options

### 🌐 Remote Server (Easiest - Hosted by GitHub)

```json
// VS Code (OAuth - recommended)
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}

// VS Code (PAT)
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    }
  },
  "inputs": [{
    "type": "promptString",
    "id": "github_mcp_pat",
    "description": "GitHub Personal Access Token",
    "password": true
  }]
}
```

**Prerequisites:** VS Code 1.101+ for remote MCP and OAuth support

### 🐳 Local Server (Docker)

```json
{
	"command": "docker",
	"args": [
		"run",
		"-i",
		"--rm",
		"-e",
		"GITHUB_PERSONAL_ACCESS_TOKEN",
		"ghcr.io/github/github-mcp-server"
	],
	"env": {
		"GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
	}
}
```

**Prerequisites:**

```bash
docker logout ghcr.io  # If you have old credentials
```

### 🔧 Build from Source

```bash
go build -o github-mcp-server ./cmd/github-mcp-server
# Then use: github-mcp-server stdio with GITHUB_PERSONAL_ACCESS_TOKEN env var
```

## Configuration Deep Dive

### Toolsets (Control Available Capabilities)

| Toolset               | Icon | Description                                             |
| --------------------- | ---- | ------------------------------------------------------- |
| `context`             | 👤   | **Strongly recommended**: Current user & GitHub context |
| `actions`             | ⚙️   | GitHub Actions workflows & CI/CD                        |
| `code_security`       | 🔍   | Code scanning alerts                                    |
| `copilot`             | 🤖   | Copilot tools (remote only)                             |
| `dependabot`          | 🔒   | Dependabot alerts                                       |
| `discussions`         | 💬   | GitHub Discussions                                      |
| `gists`               | 📝   | Gist management                                         |
| `git`                 | 🌿   | Low-level Git operations                                |
| `issues`              | 🐛   | Issues management                                       |
| `labels`              | 🏷️   | Repository labels                                       |
| `notifications`       | 🔔   | Notifications                                           |
| `orgs`                | 🏢   | Organization tools                                      |
| `projects`            | 📋   | GitHub Projects                                         |
| `pull_requests`       | 🔀   | PR management                                           |
| `repos`               | 📦   | Repository operations                                   |
| `secret_protection`   | 🔐   | Secret scanning                                         |
| `security_advisories` | 🛡️   | Security advisories                                     |
| `stargazers`          | ⭐   | Star management                                         |
| `users`               | 👥   | User tools                                              |

**Remote-only additional toolsets:** `copilot`, `copilot_spaces`, `github_support_docs_search`

#### Specifying Toolsets

```bash
# CLI
github-mcp-server --toolsets "repos,issues,pull_requests"

# Environment variable (takes precedence)
GITHUB_TOOLSETS="repos,issues,pull_requests"

# Docker
docker run -e GITHUB_TOOLSETS="repos,issues" ghcr.io/github/github-mcp-server
```

#### Special Toolsets

```bash
# Enable ALL toolsets
--toolsets "all"
GITHUB_TOOLSETS="all"

# Default toolsets (when none specified)
--toolsets "default"
# Default = context, repos, issues, pull_requests, actions, code_security, dependabot, discussions, gists, git, labels, notifications, orgs, projects, secret_protection, security_advisories, stargazers, users
```

#### Individual Tools (Fine-grained Control)

```bash
# CLI
github-mcp-server --tools "get_file_contents,create_pull_request"

# Environment variable
GITHUB_TOOLS="get_file_contents,create_pull_request"

# Combine with toolsets (additive)
--toolsets "repos,issues" --tools "get_gist"
```

### Read-Only Mode

```bash
# CLI
github-mcp-server --read-only

# Docker
docker run -e GITHUB_READ_ONLY=true ghcr.io/github/github-mcp-server
```

### Lockdown Mode (Restrict Public Repo Content)

```bash
# CLI
github-mcp-server --lockdown

# Docker
docker run -e GITHUB_LOCKDOWN=true ghcr.io/github/github-mcp-server
```

**Behavior:** Filters content from users without push access to the repository. Private repos unaffected.

### Insiders Mode (Early Access Features)

```bash
# Remote - URL path
"url": "https://api.githubcopilot.com/mcp/insiders"

# Remote - Header
"headers": { "X-MCP-Insiders": "true" }

# Local - CLI
github-mcp-server --insiders

# Local - Environment
GITHUB_INSIDERS=true

# Docker
docker run -e GITHUB_INSIDERS=true ghcr.io/github/github-mcp-server
```

## GitHub Enterprise Support

### GitHub Enterprise Cloud (ghe.com) - Remote

```json
{
	"github-octocorp": {
		"type": "http",
		"url": "https://copilot-api.octocorp.ghe.com/mcp",
		"headers": {
			"Authorization": "Bearer ${input:github_mcp_pat}"
		}
	}
}
```

**Note:** For OAuth with VS Code, configure VS Code settings to point to your GHE instance.

### GitHub Enterprise Server - Local Only

```bash
# CLI flag
--gh-host https://YOURSUBDOMAIN.ghe.com

# Environment variable
GITHUB_HOST=https://YOURSUBDOMAIN.ghe.com
```

Supports both `https://` and `http://` (for air-gapped).

## Hermes Integration

For Hermes Agent (Docker mode):

```yaml
mcp_servers:
  github:
    command: "docker"
    args:
      [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server",
      ]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
      GITHUB_TOOLSETS: "repos,issues,pull_requests,actions,code_security,dependabot"
    tools:
      include:
        [
          get_file_contents,
          create_issue,
          create_pull_request,
          list_issues,
          search_code,
        ]
```

For Remote HTTP mode:

```yaml
mcp_servers:
  github:
    url: "https://api.githubcopilot.com/mcp/"
    transport: "streamable-http"
    headers:
      Authorization: "Bearer ${GITHUB_TOKEN}"
    tools:
      include:
        [
          get_file_contents,
          create_issue,
          create_pull_request,
          list_issues,
          search_code,
        ]
```

Then run:

```bash
hermes mcp test github
/reload-mcp
```

## References

- GitHub: <https://github.com/github/github-mcp-server>
- Docker Image: ghcr.io/github/github-mcp-server
- Remote Endpoint: <https://api.githubcopilot.com/mcp/>
- Enterprise: <https://copilot-api.octocorp.ghe.com/mcp>
- Reddit Guide: <https://www.reddit.com/r/mcpserver/comments/1jvsyre/github_mcp_server_overview_and_setup_guide>

- Docker Image: ghcr.io/github/github-mcp-server
- Remote Endpoint: <https://api.githubcopilot.com/mcp/>
- Enterprise: <https://copilot-api.octocorp.ghe.com/mcp>
- Reddit Guide: <https://www.reddit.com/r/mcpserver/comments/1jvsyre/github_mcp_server_overview_and_setup_guide>
