# Sentry MCP Server

**Source:** https://github.com/getsentry/sentry-mcp

## Overview

**Sentry's MCP (Model Context Protocol) server** designed for **human-in-the-loop coding agents** (Cursor, Claude Code, etc.). It acts as middleware to the upstream Sentry API, optimized for developer workflows and debugging—not a general-purpose Sentry MCP.

- **Production endpoint**: https://mcp.sentry.dev
- **Based on**: Cloudflare's remote MCP work
- **License**: MIT
- **1,055 commits** — active development

## Quick Start Options

### 1. Claude Code Plugin (Recommended)

```bash
# Install as Claude Code plugin for automatic subagent delegation
sentry-mcp
```

Provides a `sentry-mcp` subagent that Claude auto-delegates to for Sentry errors, issues, traces, performance.

### 2. Remote MCP (Production)

Use the deployed service at `https://mcp.sentry.dev` — no local setup needed.

### 3. Stdio Transport (Self-Hosted / Local)

```bash
# Default (targets Sentry SaaS)
stdio

# Self-hosted Sentry
stdio --host=sentry.example.com

# Self-hosted without TLS (plain HTTP)
stdio --host=sentry.example.com --insecure-http

# Disable specific skills (e.g., Seer unavailable on self-hosted)
stdio --disable-skills=seer
```

### Critical Environment Variables

```bash
# REQUIRED: Explicitly specify LLM provider (auto-detection deprecated)
EMBEDDED_AGENT_PROVIDER=openai  # or anthropic

# For local development .env
OPENAI_API_KEY=your_key
# or
ANTHROPIC_API_KEY=your_key
```

> **Note**: AI-powered search tools (`search_events`, `search_issues`, etc.) require an LLM provider. Without one, these tools are unavailable but all other tools work normally.

## Local Development Setup

### Prerequisites

```bash
# 1. Install dependencies & shared skills
make setup
# Runs: npx @sentry/dotagents install
# Installs skills from getsentry/skills into .agents/skills/ (symlinked to .claude/skills, .cursor/skills)

# 2. Update skills later if needed
npx @sentry/dotagents install
```

### Create OAuth App in Sentry

- **Settings → API → Applications**
- **Redirect URIs**:
  ```
  http://localhost:5173
  http://localhost:5173/oauth/callback
  ```

### Configure Credentials

```bash
# Root .env (provides defaults for all packages)
cp .env.example .env

# Package-specific override (e.g., Cloudflare worker)
# packages/mcp-cloudflare/.env
SENTRY_CLIENT_ID=your_development_sentry_client_id
SENTRY_CLIENT_SECRET=your_development_sentry_client_secret
COOKIE_SECRET=my-super-secret-cookie
```

### Start Development Server

```bash
make dev
# Server available at http://localhost:5173
```

### Verify with MCP Inspector

1. Open Inspector: https://modelcontextprotocol.io/docs/tools/inspector
2. Enter: `http://localhost:5173/mcp`
3. Connect → authenticate → "List Tools"

> **Tip**: If OAuth fails on `127.0.0.1`, use `localhost` instead (`http://localhost:6274`)

## Testing

### Three Test Suites

| Suite | Command | Notes |
|-------|---------|-------|
| **Unit tests** | `make test` | Fast, isolated |
| **Evaluations** | `make eval` | Requires root `.env` with config |
| **Manual testing** | `make test-manual` | Preferred for MCP changes |

### Manual Testing Details

```bash
# Defaults to http://localhost:5173
# Override with:
--mcp-host <url>
# or env var:
MCP_URL=<url>
```

### Comprehensive Playbooks

- `docs/testing-stdio.md` — stdio transport testing
- `docs/testing-remote.md` — remote MCP testing

## Repository Structure (Key Paths)

```
├── .agents/skills/          # Shared agent skills (symlinked to .claude/, .cursor/)
├── .claude-plugin/          # Claude Code plugin
├── .cursor-plugin/          # Cursor plugin
├── .github/workflows/       # CI/CD
├── bin/                     # Executable scripts
├── docs/                    # Per-topic guides & tool-integrated .md files
├── packages/                # Monorepo packages (mcp-cloudflare, etc.)
├── plugins/                 # MCP plugins
├── scripts/                 # Build/dev scripts
├── .mcp.json                # MCP server manifest
├── AGENTS.md / CLAUDE.md    # Contributor workflows & full docs index
├── agents.toml              # Agent configuration
├── biome.json               # Linter/formatter config
├── Makefile                 # Primary dev commands
├── package.json             # Root package (pnpm workspace)
├── pnpm-workspace.yaml      # Workspace config
├── turbo.json               # Turborepo config
├── vitest.workspace.ts      # Test workspace
└── warden.toml              # Security/policy config
```

## Key Technical Details

### Transport Modes

| Mode | Use Case | Auth |
|------|----------|------|
| **Remote (Cloudflare)** | Production, SaaS | OAuth via `mcp.sentry.dev` |
| **Stdio** | Self-hosted, local dev | User Auth Token + env vars |

### Required Sentry User Auth Token Scopes

```
org:read
project:read
project:write
team:read
team:write
event:write
```

## Hermes Integration

For Hermes Agent (STDIO self-hosted mode):

```yaml
mcp_servers:
  sentry:
    command: "stdio"  # Requires sentry-mcp binary in PATH
    args: ["--host=your-sentry-instance.com"]
    env:
      EMBEDDED_AGENT_PROVIDER: "openai"
      OPENAI_API_KEY: "${OPENAI_API_KEY}"
    tools:
      include: [get_issue, search_issues, get_trace, search_events]
```

For Remote mode (recommended for SaaS):
```yaml
mcp_servers:
  sentry:
    url: "https://mcp.sentry.dev"
    transport: "streamable-http"
    # Auth handled via OAuth in Sentry
```

Then run:
```bash
hermes mcp test sentry
/reload-mcp
```

## mcpservers.org Listing

- https://mcpservers.org/servers/MCP-100/mcp-sentry

## References

- GitHub: https://github.com/getsentry/sentry-mcp
- Sentry MCP Docs: https://docs.sentry.io/ai/monitoring/mcp/getting-started
- Production endpoint: https://mcp.sentry.dev
- MCP Inspector: https://modelcontextprotocol.io/docs/tools/inspector