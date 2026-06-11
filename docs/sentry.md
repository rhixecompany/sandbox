# Sentry MCP Server

**Source:** https://github.com/getsentry/sentry-mcp

## Overview

**sentry-mcp** is Sentry's Model Context Protocol (MCP) server designed for human-in-the-loop coding agents. It acts as middleware to the upstream Sentry API, optimized for coding assistants like Cursor, Claude Code, and similar development tools.

> "Our tool selection and priorities are focused on developer workflows and debugging use cases, rather than providing a general-purpose MCP server for all Sentry functionality."

**Production URL:** https://mcp.sentry.dev

---

## Transport Modes

### Remote MCP (Primary)
- Cloudflare-based remote MCP service
- Production deployment at `https://mcp.sentry.dev`

### Stdio Transport (Self-hosted)
- For connecting to self-hosted Sentry installations
- **Required OAuth Scopes:**
  ```
  org:read
  project:read
  project:write
  team:read
  team:write
  event:write
  ```

**Self-hosted connection flags:**
```bash
--host=sentry.example.com    # hostname only
--insecure-http              # for plain HTTP deployments
```

---

## AI-Powered Search Tools

Tools like `search_events` and `search_issues` require an LLM provider (OpenAI or Anthropic) for natural language to Sentry query translation.

> **Important:** Always set `EMBEDDED_AGENT_PROVIDER` to explicitly specify your LLM provider. Auto-detection based on API keys alone is deprecated.

---

## Claude Code Plugin Installation

Install as a Claude Code plugin for automatic subagent delegation:

- Provides a `sentry-mcp` subagent
- Claude automatically delegates when you ask about Sentry errors, issues, traces, or performance

---

## Local Development Setup

### 1. Environment & Skills Setup
```bash
# Installs shared skills from getsentry/skills into:
# .agents/skills/ (symlinked to .claude/skills and .cursor/skills)
npx @sentry/dotagents install
```

### 2. Create OAuth App in Sentry
Navigate to: Settings → API → Applications

**Required URLs:**
- Redirect URI: `http://localhost:5173/oauth/callback`

### 3. Configure Credentials

**Root `.env` file:**
```env
OPENAI_API_KEY=your_key
```

**`packages/mcp-cloudflare/.env`:**
```env
SENTRY_CLIENT_ID=your_development_sentry_client_id
SENTRY_CLIENT_SECRET=your_development_sentry_client_secret
COOKIE_SECRET=my-super-secret-cookie
```

### 4. Start Development Server
Server available at: `http://localhost:5173`

### 5. Verify with MCP Inspector
- Enter `http://localhost:5173/mcp` into Inspector
- Follow authentication prompts
- Use "List Tools" to verify

> **Note:** If OAuth issues on `127.0.0.1`, try `http://localhost:6274` instead.

---

## Testing

### Three Test Suites:

**1. Unit Tests**
```bash
pnpm test
```

**2. Evaluations**
Requires `.env` configuration with:
- `SENTRY_AUTH_TOKEN`
- `SENTRY_ORG`
- `SENTRY_PROJECT`
- `SENTRY_URL` (for self-hosted)
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`

```bash
pnpm test:eval
```

**3. Manual Testing (Preferred for MCP changes)**
```bash
pnpm test:manual
```

> **Note:** CLI defaults to `http://localhost:5173`. Override with `--mcp-host` or `MCP_URL` environment variable.

**Testing Playbooks:**
- `docs/testing-stdio.md`
- `docs/testing-remote.md`

---

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `EMBEDDED_AGENT_PROVIDER` | **Required.** Explicitly set LLM provider (OpenAI/Anthropic) |
| `OPENAI_API_KEY` | OpenAI API key for AI-powered tools |
| `ANTHROPIC_API_KEY` | Anthropic API key for AI-powered tools |
| `SENTRY_CLIENT_ID` | OAuth client ID |
| `SENTRY_CLIENT_SECRET` | OAuth client secret |
| `COOKIE_SECRET` | Secret for cookie encryption |
| `MCP_URL` | Override default MCP server URL |

> **Note:** Root `.env` provides defaults for all packages. Individual packages can have their own `.env` files to override defaults.

---

## Self-Hosted Considerations

- Some features (like Seer) may not be available on self-hosted instances
- Disable specific skills to prevent unsupported tools from being exposed
- Use `--insecure-http` for deployments without TLS
- Only set `SENTRY_URL` override when operating self-hosted Sentry

---

## Automated Code Review

This repository uses automated code review tools (like Cursor BugBot):

- Provide helpful feedback and suggestions
- **Not recommended as required checks** (accuracy still evolving)
- Can produce false positives
- Focus on underlying concerns rather than strictly following every suggestion

---

## Key Documentation

| File | Purpose |
|------|---------|
| `CLAUDE.md` / `AGENTS.md` | Contributor workflows and complete docs index |
| `docs/` | Per-topic guides and tool-integrated `.md` files |
| `docs/embedded-agents.md` | Detailed LLM provider configuration |
| `docs/testing-stdio.md` | Stdio transport testing guide |
| `docs/testing-remote.md` | Remote transport testing guide |
| `TELEMETRY.md` | Telemetry documentation |
