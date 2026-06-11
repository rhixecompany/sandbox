# GitHub MCP Server (Official)

**Source:** https://github.com/github/github-mcp-server

## Overview

The **GitHub MCP Server** is GitHub's official Model Context Protocol (MCP) server that connects AI tools directly to GitHub's platform. It enables AI agents, assistants, and chatbots to read repositories and code files, manage issues and PRs, analyze code, and automate workflows — all through natural language interactions.

> "The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows."

---

## Deployment Options

### Remote GitHub MCP Server (Recommended)

Hosted by GitHub — the easiest way to get started. No local setup required.

- **Endpoint**: `https://api.githubcopilot.com/mcp/`
- **Requires**: VS Code 1.01+ for remote MCP and OAuth support
- **Fallback**: Use the local version if your MCP host doesn't support remote servers

#### Quick Install (VS Code)
One-click install buttons available for VS Code and VS Code Insiders.

#### Manual Configuration

**Using OAuth:**
```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

**Using a GitHub Personal Access Token (PAT):**
```json
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
  "inputs": [
    {
      "type": "promptString",
      "id": "github_mcp_pat",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
```

#### Insiders Mode (Early Access Features)

Access experimental tools and new features early:

**Via URL Path:**
```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/insiders"
    }
  }
}
```

**Via Header:**
```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "X-MCP-Insiders": "true"
      }
    }
  }
}
```

#### GitHub Enterprise Cloud (ghe.com)

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

> **Note:** GitHub Enterprise Server does **not** support remote server hosting. Use the [local server](#local-github-mcp-server) instead.

---

### Local GitHub MCP Server

Runs locally via Docker or built from source.

#### Prerequisites
- Docker installed
- GitHub Personal Access Token (PAT)

#### Quick Install (Docker in VS Code)
One-click install buttons available for VS Code and VS Code Insiders using Docker.

#### Docker Command
```bash
docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server
```

#### Environment Variables (Recommended for Security)

Store your PAT in environment variables or a `.env` file:

```bash
# .env file
GITHUB_PERSONAL_ACCESS_TOKEN=your_token_here
```

> **Protect your `.env` file:** Never commit it to version control. Restrict file permissions.

#### Token Security Best Practices

- **Minimum scopes**: Only grant necessary permissions (`repo`, `read:packages`, `read:org`)
- **Separate tokens**: Use different PATs for different projects/environments
- **Regular rotation**: Update tokens periodically
- **Never commit**: Keep tokens out of version control
- **File permissions**: Restrict access to config files containing tokens

#### GitHub Enterprise Server / Enterprise Cloud (ghe.com)

Use the `--gh-host` flag or `GITHUB_HOST` environment variable:

```bash
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN \
  -e GITHUB_HOST=https://YOURSUBDOMAIN.ghe.com \
  ghcr.io/github/github-mcp-server
```

#### Build from Source

```bash
cd cmd/github-mcp-server
go build -o github-mcp-server
GITHUB_PERSONAL_ACCESS_TOKEN=your_token ./github-mcp-server stdio
```

#### CLI Utilities

```bash
# Search available tools
github-mcp-server tool-search "<query>" --max-results 10
```

---

## Tool Configuration

Control which GitHub API capabilities are available to your AI tools using **toolsets** and **individual tools**.

### Specifying Toolsets

**Command Line:**
```bash
github-mcp-server stdio --toolsets repos,issues,pull_requests
```

**Environment Variable:**
```bash
GITHUB_TOOLSETS=repos,issues,pull_requests
```

> **Note:** The `GITHUB_TOOLSETS` environment variable takes precedence over the command line argument.

### Specifying Individual Tools

**Command Line:**
```bash
github-mcp-server stdio --tools get_file_contents,get_me
```

**Environment Variable:**
```bash
GITHUB_TOOLS=get_file_contents,get_me
```

**Combining Toolsets and Tools (additive):**
```bash
GITHUB_TOOLSETS=repos,issues GITHUB_TOOLS=get_gist
```

### Special Toolsets

| Toolset | Description |
|---------|-------------|
| `all` | Enable all available toolsets |
