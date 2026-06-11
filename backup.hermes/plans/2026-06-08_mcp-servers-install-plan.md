# MCP Server Installation & Configuration Plan

## Goal
Install, configure, test, and document 40+ MCP servers in Hermes Agent.
Save all docs to `docs/mcp-servers/` with an index catalog.

## Current State
- Hermes MCP config: `~/.hermes/config.yaml` → `mcp_servers:` block
- Stdio servers: use `npx -y <package>` or `uvx <package>`
- HTTP servers: use `url:` + `headers:`
- OAuth servers: need `auth: oauth` + token flow
- Catalog: `hermes mcp` interactive picker for Nous-approved servers

## MCP Servers to Install (with configs)

### Tier 1: Official/Reference Servers (modelcontextprotocol/servers)

| # | Server | Package/Source | Transport | Config |
|---|--------|---------------|-----------|--------|
| 1 | **GitHub** | `@modelcontextprotocol/server-github` | stdio | `npx -y @modelcontextprotocol/server-github` + `GITHUB_PERSONAL_ACCESS_TOKEN` |
| 2 | **Filesystem** | `@modelcontextprotocol/server-filesystem` | stdio | `npx -y @modelcontextprotocol/server-filesystem /c/Users/Alexa/Desktop/SandBox` |
| 3 | **Fetch** | `mcp-server-fetch-typescript` | stdio | `npx -y mcp-server-fetch-typescript` |
| 4 | **Memory** | `@modelcontextprotocol/server-memory` | stdio | `npx -y @modelcontextprotocol/server-memory` |
| 5 | **Sequential Thinking** | `@modelcontextprotocol/server-sequential-thinking` | stdio | `npx -y @modelcontextprotocol/server-sequential-thinking` |
| 6 | **Time** | `mcp-server-time` | stdio | `npx -y mcp-server-time` |
| 7 | **SQLite** | `@modelcontextprotocol/server-sqlite` | stdio | `npx -y @modelcontextprotocol/server-sqlite` |
| 8 | **PostgreSQL** | `@modelcontextprotocol/server-postgres` | stdio | needs `DATABASE_URL` |
| 9 | **Puppeteer** | `@modelcontextprotocol/server-puppeteer` | stdio | `npx -y @modelcontextprotocol/server-puppeteer` |
| 10 | **Brave Search** | `@modelcontextprotocol/server-brave-search` | stdio | needs `BRAVE_API_KEY` |
| 11 | **Google Maps** | `google-maps-mcp-server` | stdio | needs `GOOGLE_MAPS_API_KEY` |
| 12 | **Slack** | `@modelcontextprotocol/server-slack` | stdio | needs Slack OAuth |
| 13 | **Discord** | `@modelcontextprotocol/server-discord` | stdio | needs Discord bot token |

### Tier 2: Browser & Automation

| # | Server | Package | Notes |
|---|--------|---------|-------|
| 14 | **Playwright** (Microsoft) | `@playwright/mcp` | `npx @playwright/mcp@latest` |
| 15 | **Playwright** (ExecuteAutomation) | `@executeautomation/playwright-mcp-server` | `npx -y @executeautomation/playwright-mcp-server` |
| 16 | **Desktop Commander** | `@wonderwhy-er/desktop-commander` | Terminal + file ops |

### Tier 3: AI & Docs

| # | Server | Package | Notes |
|---|--------|---------|-------|
| 17 | **Context7** | `@upstash/context7-mcp` | HTTP: `https://mcp.context7.com/mcp` + API key |
| 18 | **Django MCP** | `django-mcp-server` (pip) | Needs Django project |
| 19 | **ast-grep** | `@notprolands/ast-grep-mcp` | `uvx --from git+https://github.com/ast-grep/ast-grep-mcp` |
| 20 | **markitdown** | `markdownify-mcp-server` | File→Markdown conversion |
| 21 | **shadcn** | `shadcn-mcp` | shadcn/ui components |

### Tier 4: Data & Infrastructure

| # | Server | Package | Notes |
|---|--------|---------|-------|
| 22 | **Redis** | `@gongrzhe/server-redis-mcp` | `npx @gongrzhe/server-redis-mcp redis://localhost:6379` |
| 23 | **MongoDB** | `@modelcontextprotocol/server-mongodb` | needs `MONGODB_URI` |
| 24 | **Neon** | `@neondatabase/mcp-server-neon` | Serverless Postgres |
| 25 | **Chroma** | `chroma-mcp` | Vector DB |

### Tier 5: Productivity & APIs

| # | Server | Package | Notes |
|---|--------|---------|-------|
| 26 | **YouTube Transcript** | `mcp-server-youtube-transcript` | `git clone` + build |
| 27 | **Hacker News** | `hacker-news-mcp` | HN API |
| 28 | **npm** | `npm-sentinel-mcp` | npm package search |
| 29 | **Stripe** | `stripe-mcp` | OAuth + API key |
| 30 | **Postman** | `postman-mcp` | API testing |
| 31 | **Apify** | `apify-mcp` | Web scraping |
| 32 | **Sentry** | `sentry-mcp` | stdio: `uvx mcp-sentry --auth-token TOKEN` |
| 33 | **Git MCP** | `@mseep/git-mcp-server` | Git operations |
| 34 | **GitMCP** | `https://gitmcp.io/{owner}/{repo}` | HTTP: per-repo docs |

### Tier 6: Cloud & DevOps

| # | Server | Package | Notes |
|---|--------|---------|-------|
| 35 | **Cloud Run** | `cloud-run-mcp` | GCP Cloud Run |
| 36 | **API Gateway** | `api-gateway-mcp` | API Gateway |
| 37 | **Next.js Devtools** | `next-devtools-mcp` | Next.js development |
| 38 | **Python Interpreter** | `python-interpreter-mcp` | Python execution |
| 39 | **uv** | `uv-mcp` | Python package manager |
| 40 | **Hostinger API** | `hostinger-mcp` | Hostinger hosting |
| 41 | **Gemini API Docs** | `gemini-api-docs-mcp` | Google Gemini API |
| 42 | **Google Flights** | `google-flights-mcp` | Flight search |
| 43 | **Neo4j Memory** | `neo4j-memory-mcp` | Graph database memory |
| 44 | **Python Refactoring** | `python-refactoring-assistant-mcp` | Code refactoring |
| 45 | **Node.js Sandbox** | `node-code-sandbox-mcp` | Docker-based JS sandbox |

## Step-by-Step Installation Plan

### Phase 1: Stdio Servers via npx (Batch 1)
Install all pure-npx servers that don't need API keys first:
1. filesystem, fetch, memory, sequential-thinking, time, sqlite
2. playwright (microsoft), desktop-commander
3. ast-grep, markitdown, shadcn
4. git-mcp, hacker-news, npm-sentinel

### Phase 2: HTTP/OAuth Servers
5. Context7 (HTTP, needs API key)
6. GitMCP (HTTP per-repo)
7. Stripe (OAuth)
8. Sentry (needs token)
9. Google Maps (needs API key)
10. Neon (needs connection string)

### Phase 3: Git Clone + Build Servers
11. YouTube Transcript (clone + npm build)
12. node-code-sandbox (Docker-based)
13. python-interpreter, uv, neo4j-memory
14. cloud-run, api-gateway, next-devtools

### Phase 4: Django/Python Servers
15. Django MCP (pip install + Django project)
16. Redis (needs Redis running)
17. MongoDB (needs MongoDB running)
18. Chroma (pip install)

### Phase 5: Documentation
19. For each server, save a markdown doc to `docs/mcp-servers/<name>.md`
20. Create `docs/mcp-servers/index.md` catalog
21. Create `docs/README.md` master index

### Phase 6: Testing
22. Test each server with `hermes mcp configure <name>`
23. Verify tools are discoverable
24. Run a test query per server

## Files to Create
- `docs/mcp-servers/index.md` — master catalog
- `docs/mcp-servers/<server-name>.md` — per-server docs
- `~/.hermes/config.yaml` — updated with all `mcp_servers:` entries

## Risks
- OAuth servers need browser flow — may require interactive setup
- API key servers need user to provide keys
- Docker-based servers need Docker running
- Some servers may have Windows-specific path issues
- Rate limits on npm/pip installs
