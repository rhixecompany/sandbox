# MCP Server Installation & Configuration Plan

## Goal

Install, configure, test, and document 40+ MCP servers in Hermes Agent.
Save all docs to `docs/mcp-servers/` with an index catalog.

## Current State

- Hermes MCP config: `~/AppData/Local/hermes/config.yaml` → `mcp_servers:` block
- Stdio servers: use `npx -y <package>` or `uvx <package>`
- HTTP servers: use `url:` + `headers:`
- OAuth servers: need `auth: oauth` + token flow
- Catalog: `hermes mcp` interactive picker for Nous-approved servers

## Plan Review — 2026-06-11
- `mcp-server-time` is unpublished (404 as of 2026-06-11); drop
- `@modelcontextprotocol/server-sqlite` does not exist; drop
- `markdownify-mcp-server` does not exist; drop
|- Config initially had 12 enabled stdio servers; 5 invalid/broken ones have been removed
|- Reduce target scope to servers with valid packages and local/runnable form
|- Removed broken/invalid entries because they cannot run on this system

### Tier 1: Official/Reference Servers (modelcontextprotocol/servers)

| #   | Server                  | Package/Source                                     | Transport | Config                                                                          |
| --- | ----------------------- | -------------------------------------------------- | --------- | ------------------------------------------------------------------------------- |
| 1   | **GitHub**              | `@modelcontextprotocol/server-github`              | stdio     | `npx -y @modelcontextprotocol/server-github` + `GITHUB_PERSONAL_ACCESS_TOKEN`   |
| 2   | **Filesystem**          | `@modelcontextprotocol/server-filesystem`          | stdio     | `npx -y @modelcontextprotocol/server-filesystem /c/Users/Alexa/Desktop/SandBox` |
| 3   | **Fetch**               | `mcp-server-fetch-typescript`                      | stdio     | `npx -y mcp-server-fetch-typescript`                                            |
| 4   | **Memory**              | `@modelcontextprotocol/server-memory`              | stdio     | `npx -y @modelcontextprotocol/server-memory`                                    |
| 5   | **Sequential Thinking** | `@modelcontextprotocol/server-sequential-thinking` | stdio     | `npx -y @modelcontextprotocol/server-sequential-thinking`                       |
| 6   | **Time**                | `mcp-server-time`                                  | stdio     | `npx -y mcp-server-time`                                                        |
| 7   | **SQLite**              | `@modelcontextprotocol/server-sqlite`              | stdio     | `npx -y @modelcontextprotocol/server-sqlite`                                    |
| 8   | **PostgreSQL**          | `@modelcontextprotocol/server-postgres`            | stdio     | needs `DATABASE_URL`                                                            |
| 9   | **Puppeteer**           | `@modelcontextprotocol/server-puppeteer`           | stdio     | `npx -y @modelcontextprotocol/server-puppeteer`                                 |
| 10  | **Brave Search**        | `@modelcontextprotocol/server-brave-search`        | stdio     | needs `BRAVE_API_KEY`                                                           |
| 11  | **Google Maps**         | `google-maps-mcp-server`                           | stdio     | needs `GOOGLE_MAPS_API_KEY`                                                     |
| 12  | **Slack**               | `@modelcontextprotocol/server-slack`               | stdio     | needs Slack OAuth                                                               |
| 13  | **Discord**             | `@modelcontextprotocol/server-discord`             | stdio     | needs Discord bot token                                                         |

### Tier 2: Browser & Automation

| #   | Server                             | Package                                    | Notes                                             |
| --- | ---------------------------------- | ------------------------------------------ | ------------------------------------------------- |
| 14  | **Playwright** (Microsoft)         | `@playwright/mcp`                          | `npx @playwright/mcp@latest`                      |
| 15  | **Playwright** (ExecuteAutomation) | `@executeautomation/playwright-mcp-server` | `npx -y @executeautomation/playwright-mcp-server` |
| 16  | **Desktop Commander**              | `@wonderwhy-er/desktop-commander`          | Terminal + file ops                               |

### Tier 3: AI & Docs

| #   | Server         | Package                     | Notes                                                     |
| --- | -------------- | --------------------------- | --------------------------------------------------------- |
| 17  | **Context7**   | `@upstash/context7-mcp`     | HTTP: `https://mcp.context7.com/mcp` + API key            |
| 18  | **Django MCP** | `django-mcp-server` (pip)   | Needs Django project                                      |
| 19  | **ast-grep**   | `@notprolands/ast-grep-mcp` | `uvx --from git+https://github.com/ast-grep/ast-grep-mcp` |
| 20  | **markitdown** | `markdownify-mcp-server`    | File→Markdown conversion                                  |
| 21  | **shadcn**     | `shadcn-mcp`                | shadcn/ui components                                      |

### Tier 4: Data & Infrastructure

| #   | Server      | Package                                | Notes                                                   |
| --- | ----------- | -------------------------------------- | ------------------------------------------------------- |
| 22  | **Redis**   | `@gongrzhe/server-redis-mcp`           | `npx @gongrzhe/server-redis-mcp redis://localhost:6379` |
| 23  | **MongoDB** | `@modelcontextprotocol/server-mongodb` | needs `MONGODB_URI`                                     |
| 24  | **Neon**    | `@neondatabase/mcp-server-neon`        | Serverless Postgres                                     |
| 25  | **Chroma**  | `chroma-mcp`                           | Vector DB                                               |

### Tier 5: Productivity & APIs

| #   | Server                 | Package                            | Notes                                      |
| --- | ---------------------- | ---------------------------------- | ------------------------------------------ |
| 26  | **YouTube Transcript** | `mcp-server-youtube-transcript`    | `git clone` + build                        |
| 27  | **Hacker News**        | `hacker-news-mcp`                  | HN API                                     |
| 28  | **npm**                | `npm-sentinel-mcp`                 | npm package search                         |
| 29  | **Stripe**             | `stripe-mcp`                       | OAuth + API key                            |
| 30  | **Postman**            | `postman-mcp`                      | API testing                                |
| 31  | **Apify**              | `apify-mcp`                        | Web scraping                               |
| 32  | **Sentry**             | `sentry-mcp`                       | stdio: `uvx mcp-sentry --auth-token TOKEN` |
| 33  | **Git MCP**            | `@mseep/git-mcp-server`            | Git operations                             |
| 34  | **GitMCP**             | `https://gitmcp.io/{owner}/{repo}` | HTTP: per-repo docs                        |

### Tier 6: Cloud & DevOps

| #   | Server                 | Package                            | Notes                   |
| --- | ---------------------- | ---------------------------------- | ----------------------- |
| 35  | **Cloud Run**          | `cloud-run-mcp`                    | GCP Cloud Run           |
| 36  | **API Gateway**        | `api-gateway-mcp`                  | API Gateway             |
| 37  | **Next.js Devtools**   | `next-devtools-mcp`                | Next.js development     |
| 38  | **Python Interpreter** | `python-interpreter-mcp`           | Python execution        |
| 39  | **uv**                 | `uv-mcp`                           | Python package manager  |
| 40  | **Hostinger API**      | `hostinger-mcp`                    | Hostinger hosting       |
| 41  | **Gemini API Docs**    | `gemini-api-docs-mcp`              | Google Gemini API       |
| 42  | **Google Flights**     | `google-flights-mcp`               | Flight search           |
| 43  | **Neo4j Memory**       | `neo4j-memory-mcp`                 | Graph database memory   |
| 44  | **Python Refactoring** | `python-refactoring-assistant-mcp` | Code refactoring        |
| 45  | **Node.js Sandbox**    | `node-code-sandbox-mcp`            | Docker-based JS sandbox |

## Step-by-Step Installation Plan

### Phase 1: Stdio Servers via npx (reduced scope)
- Current enabled stdio stack: filesystem, fetch, memory, sequential-thinking, github, puppeteer, playwright, desktop-commander, ast-grep, shadcn, code-sandbox, mcp-docker
- Proposed addition in Phase 1: github (already enabled), hacker-news-mcp, npm-sentinel-mcp
- Blocked/dropped packages: `mcp-server-time` (`404`), `markitdown`/`markdownify-mcp-server` (`404`)

### Phase 2: HTTP/OAuth Servers (requires credentials)
- Context7, GitMCP, Stripe, Sentry, Google Maps, Neon
- Do not install now; requires API keys/OAuth tokens

### Phase 3: Git Clone + Build Servers

1. YouTube Transcript (clone + npm build)
2. node-code-sandbox (Docker-based)
3. python-interpreter, uv, neo4j-memory
4. cloud-run, api-gateway, next-devtools

### Phase 4: Django/Python Servers

1. Django MCP (pip install + Django project)
2. Redis (needs Redis running)
3. MongoDB (needs MongoDB running)
4. Chroma (pip install)

### Phase 5: Documentation

1. For each server, save a markdown doc to `docs/mcp-servers/<name>.md`
2. Create `docs/mcp-servers/index.md` catalog
3. Create `docs/README.md` master index

### Phase 6: Testing

1. Test each server with `hermes mcp configure <name>`
2. Verify tools are discoverable
3. Run a test query per server

## Files to Create

- `docs/mcp-servers/index.md` — master catalog
- `docs/mcp-servers/<server-name>.md` — per-server docs
- `~/AppData/Local/hermes/config.yaml` — updated with all `mcp_servers:` entries

## Risks

- OAuth servers need browser flow — may require interactive setup
- API key servers need user to provide keys
- Docker-based servers need Docker running
- Some servers may have Windows-specific path issues
- Rate limits on npm/pip installs
