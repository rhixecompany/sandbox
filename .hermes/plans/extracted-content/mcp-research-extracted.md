# MCP Research — Extracted Content

> Generated from 34 files in `docs/mcp-research/`
> Date: 2026-06-22

---

## Table of Contents

1. [API Gateway / AWS API MCP](#1-api-gateway--aws-api-mcp)
2. [ast-grep MCP](#2-ast-grep-mcp)
3. [Cloud Run MCP](#3-cloud-run-mcp)
4. [Context7 MCP](#4-context7-mcp)
5. [Desktop Commander MCP](#5-desktop-commander-mcp)
6. [Django MCP](#6-django-mcp)
7. [Fetch MCP](#7-fetch-mcp)
8. [Filesystem MCP](#8-filesystem-mcp)
9. [Gemini API Docs MCP](#9-gemini-api-docs-mcp)
10. [GitHub MCP](#10-github-mcp)
11. [GitMCP](#11-gitmcp)
12. [Google Flights MCP](#12-google-flights-mcp)
13. [Google Maps MCP](#13-google-maps-mcp)
14. [Hacker News MCP](#14-hacker-news-mcp)
15. [Hostinger API MCP](#15-hostinger-api-mcp)
16. [Markdownify MCP](#16-markdownify-mcp)
17. [MarkItDown MCP](#17-markitdown-mcp)
18. [Memory (Knowledge Graph) MCP](#18-memory-knowledge-graph-mcp)
19. [Node Code Sandbox MCP](#19-node-code-sandbox-mcp)
20. [NPM Sentinel MCP](#20-npm-sentinel-mcp)
21. [Playwright MCP](#21-playwright-mcp)
22. [Postman MCP](#22-postman-mcp)
23. [Python Refactoring MCP](#23-python-refactoring-mcp)
24. [Redis MCP](#24-redis-mcp)
25. [ScrapeGraph MCP](#25-scrapegraph-mcp)
26. [Sentry MCP](#26-sentry-mcp)
27. [Sequential Thinking MCP](#27-sequential-thinking-mcp)
28. [SQLite MCP](#28-sqlite-mcp)
29. [Stripe MCP](#29-stripe-mcp)
30. [Targets (Phase 2 MCP Research Targets)](#30-targets)
31. [Time MCP](#31-time-mcp)
32. [uv MCP](#32-uv-mcp)
33. [Vitest MCP](#33-vitest-mcp)
34. [YouTube Transcript MCP](#34-youtube-transcript-mcp)

---

## 1. API Gateway / AWS API MCP

- **Source:** https://github.com/awslabs/mcp
- **Announcement:** https://aws.amazon.com/about-aws/whats-new/2025/07/aws-api-mcp-server-available/
- **Type:** AWS Labs official — translates natural language to valid AWS CLI commands
- **Language:** Python
- **License:** MIT

### Key Features
- Translate natural language to valid AWS CLI commands
- Execute AWS API calls on behalf of AI agents
- Scoped IAM-based execution for least-privilege access
- Supports Lambda, ECS, Fargate deployment patterns behind API Gateway
- OAuth / Cognito integration for client auth

### Tools
| Tool | Description |
|------|-------------|
| `aws_api_call` | Execute an AWS CLI command |
| `list_resources` | List resources in a service/region |
| `describe_resource` | Get details about a specific resource |
| `create_resource` | Create a new AWS resource |

### Setup Notes
- Clone from `awslabs/mcp`, install with `pip install -r requirements.txt`
- Requires AWS credentials configured
- Can deploy via AWS SAM (serverless Lambda + API Gateway)

---

## 2. ast-grep MCP

- **Source:** https://github.com/ast-grep/ast-grep-mcp
- **Type:** Experimental — structural code search via AST pattern matching (not text-based)
- **Language:** Python (original); Rust port available
- **Prerequisites:** ast-grep installed, uv (Python package manager)

### Key Features
- AST pattern matching instead of simple text-based search
- Supports many languages (Python, JS, TS, Rust, Go, Java, C/C++, etc.)
- Custom ast-grep configuration via `sgconfig.yaml`

### Tools
| Tool | Description |
|------|-------------|
| `dump_syntax_tree` | Visualize AST structure of code snippets |
| `test_match_code_rule` | Test ast-grep YAML rules before applying |
| `find_code` | Search codebases using simple ast-grep patterns |
| `find_code_by_rule` | Advanced search using complex YAML rules |

### Setup Notes
- `uv sync` to install dependencies
- Quick run: `uvx --from git+https://github.com/ast-grep/ast-grep-mcp.git ast-grep-mcp`
- Config precedence: CLI flag `--config` > env var `AST_GREP_CONFIG`
- Rust alternative: `cargo install ast-grep-mcp`

---

## 3. Cloud Run MCP

- **Source:** https://github.com/GoogleCloudPlatform/cloud-run-mcp
- **Type:** Google's official Cloud Run MCP server + Gemini CLI extension
- **Language:** Node.js
- **License:** Apache 2.0 (implied from Google)

### Key Features
- Deploy containerized applications to Cloud Run
- Retrieve service logs and status
- Manage environment variables and secrets
- Scale services and adjust concurrency settings
- Integrate with Gemini CLI for natural language deployments

### Tools
| Tool | Description |
|------|-------------|
| `deploy` | Deploy a container image to Cloud Run |
| `get_logs` | Retrieve logs from a Cloud Run service |
| `list_services` | List all Cloud Run services in a project |
| `describe_service` | Get details about a specific service |
| `delete_service` | Remove a Cloud Run service |

### Setup Notes
- Prerequisites: `gcloud` CLI authenticated, GCP project with Cloud Run API enabled, Node.js 18+
- Run with `npx @google-cloud/cloud-run-mcp`
- Uses `gcloud` Application Default Credentials (ADC)
- Production: deploy the MCP server itself to Cloud Run

---

## 4. Context7 MCP

- **Source (unofficial):** https://github.com/quiint/c7-mcp-server
- **Official (Upstash):** `@upstash/context7-mcp` on npm
- **Type:** MCP bridge to Context7 API for documentation querying
- **Language:** TypeScript (unofficial); both available

### Key Features
- Query documentation context for any project/library
- Search for projects
- Retrieve project metadata
- List available projects

### Tools
| Tool | Description |
|------|-------------|
| `c7_query` | Query documentation context for a project |
| `c7_search` | Search for projects |
| `c7_info` | Retrieve project metadata |
| `c7_projects_list` | List available projects |

Official Upstash tools: `resolve-library-id`, `query-docs`

### Setup Notes
- Unofficial: `npm install -g c7-mcp-server`
- Official: `npx -y @upstash/context7-mcp --api-key YOUR_API_KEY`
- API key from https://context7.com/dashboard (free tier available)
- Resources: `context7://projects/list` returns JSON list

---

## 5. Desktop Commander MCP

- **Source:** https://github.com/wonderwhy-er/DesktopCommanderMCP
- **Type:** Terminal control, filesystem, and diff file editing
- **Language:** Node.js/TypeScript
- **License:** MIT
- **Commits:** 363+, **Releases:** 134

### Key Features
- Terminal: start/interact with processes, list sessions, kill, SSH
- Filesystem: read/write files (text, Excel, PDF, URLs), list directories, search
- Text editing: surgical search/replace with fuzzy matching and diff preview
- Configuration: runtime config management via MCP tools
- Analytics: usage stats, tool call history, feedback

### Tools
- **Configuration:** `get_config`, `set_config_value`
- **Terminal:** `start_process`, `interact_with_process`, `read_process_output`, `force_terminate`, `list_sessions`, `list_processes`
- **Filesystem:** `read_file`, `write_file`, `edit_file`, `list_directory`, `search_files`, `get_file_info`
- **Text Editing:** `replace_in_file`, `insert_into_file`
- **Analytics:** `get_usage_stats`, `submit_feedback`

### Setup Notes
- NPX auto-updates: `npx @wonderwhy-er/desktop-commander@latest setup`
- Smithery install available
- Docker: `mcp/desktop-commander:latest`
- Supports Claude Desktop, Cursor, Windsurf, VS Code, Cline, Roo Code, Claude Code, JetBrains, Gemini CLI, Augment Code, Qwen Code, Trae, Kiro, Codex
- Remote MCP (no desktop app): https://mcp.desktopcommander.app

---

## 6. Django MCP

- **Source:** https://github.com/gts360/django-mcp-server
- **Type:** Django extension implementing MCP for AI agent interaction with Django apps
- **Language:** Python
- **License:** MIT
- **Maintained by:** Smart GTS Software Engineering

### Key Features
- Django-style declarative tools for AI agents
- Expose Django models for AI querying in 2 lines of code (safely)
- Convert DRF APIs to MCP tools with one annotation
- Works on both WSGI and ASGI
- Validated as Remote Integration with Claude AI

### Tools
- `ModelQueryToolset` — expose Django models for querying
- `MCPToolset` — define custom generic tools
- DRF decorators: `drf_publish_create_mcp_tool`, `drf_publish_update_mcp_tool`, `drf_publish_delete_mcp_tool`, `drf_publish_list_mcp_tool`
- Low-level: `@mcp_server.tool()`, `@mcp_server.resource()`

### Setup Notes
- `pip install django-mcp-server`
- Add `'mcp_server'` to `INSTALLED_APPS`
- Add `path('mcp/', include('mcp_server.urls'))` to urlpatterns
- Create `mcp.py` in your app with toolsets
- `python manage.py mcp_inspect` to verify
- Settings: `DJANGO_MCP_GLOBAL_SERVER_CONFIG`, `DJANGO_MCP_AUTHENTICATION_CLASSES`, `DJANGO_MCP_ENDPOINT`
- Supports OAuth2 authentication

---

## 7. Fetch MCP

- **Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- **Type:** Official MCP server for web content fetching
- **Language:** Python
- **License:** MIT

### Key Features
- Fetch URL and extract as markdown
- Chunked reading via `start_index` parameter
- robots.txt compliance (default: obeys for tools, ignores for prompts)
- Proxy configuration support

### Tools
| Tool | Description |
|------|-------------|
| `fetch` | Fetches a URL and extracts contents as markdown |

Parameters: `url` (required), `max_length` (default 5000), `start_index` (default 0), `raw` (default false)

### Setup Notes
- Run with `uvx mcp-server-fetch` (recommended)
- Or `pip install mcp-server-fetch` then `python -m mcp_server_fetch`
- Docker: `mcp/fetch`
- Windows: set `PYTHONIOENCODING=utf-8`
- Customize: `--ignore-robots-txt`, `--user-agent`, `--proxy-url`
- ⚠️ Security caution: can access local/internal IP addresses

---

## 8. Filesystem MCP

- **Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- **Type:** Official MCP server for filesystem operations
- **Language:** TypeScript (Node.js)
- **License:** MIT

### Key Features
- Directory access control: CLI arguments (static) or MCP Roots (dynamic)
- Read operations, write operations
- Alternative implementations in Go and Java

### Tools — Read Operations
| Tool | Description |
|------|-------------|
| `read_text_file` | Read text file with optional line limits |
| `read_media_file` | Read binary/media files |
| `read_multiple_files` | Batch read multiple files |
| `list_directory` | List directory contents |
| `list_directory_with_sizes` | List with file sizes |
| `directory_tree` | Recursive tree |
| `search_files` | Glob pattern search |
| `get_file_info` | File metadata |
| `list_allowed_directories` | Returns currently allowed directories |

### Tools — Write Operations
| Tool | Description |
|------|-------------|
| `create_directory` | Create directory (idempotent) |
| `write_file` | Write file (overwrites) |
| `edit_file` | Edit with edits array (not idempotent) |
| `move_file` | Move/rename file (destructive) |

### Setup Notes
- NPX: `npx -y @modelcontextprotocol/server-filesystem /allowed/path`
- Docker: `mcp/filesystem`
- Access control via Roots is recommended (dynamic runtime updates)
- Alternative Go impl: `mark3labs/mcp-filesystem-server`

---

## 9. Gemini API Docs MCP

- **Source (community):** https://github.com/google-gemini/gemini-api-mcp-server
- **Official Docs:** https://ai.google.dev/docs
- **SDK:** https://github.com/google-gemini/generative-ai-python
- **Type:** Community implementation wrapping Google Gemini API as MCP tools
- **Language:** Python / Node.js

### Key Features
- Call Gemini models (gemini-1.5-pro, gemini-1.5-flash, etc.)
- Multimodal: text + image + video inputs
- Embedding generation with `text-embedding-004`
- Code execution via Gemini Code Execution tool
- Document (PDF) processing
- Search Gemini API documentation

### Tools
| Tool | Description |
|------|-------------|
| `generate_text` | Generate text using a Gemini model |
| `generate_with_image` | Multimodal generation with image input |
| `create_embedding` | Generate text embeddings |
| `execute_code` | Use Gemini's code execution capability |
| `search_docs` | Search Gemini API documentation |

### Setup Notes
- API key from https://aistudio.google.com/app/apikey
- `pip install google-generativeai`, then wrap with FastMCP
- Or Node.js: `npm install @google/generative-ai @modelcontextprotocol/sdk`
- Available models: gemini-1.5-pro (2M ctx), gemini-1.5-flash (1M ctx), gemini-2.0-flash (1M ctx), text-embedding-004

---

## 10. GitHub MCP

- **Source:** https://github.com/github/github-mcp-server
- **Type:** Official GitHub MCP server
- **Language:** Go
- **License:** MIT
- **Commits:** 930+

### Key Features
- Connect AI tools directly to GitHub
- Read repositories and code files
- Manage issues and PRs
- Analyze code
- Automate workflows via natural language

### Toolsets (20 available)
| Toolset | Description |
|---------|-------------|
| `context` | Current user & GitHub context |
| `repos` | Repository operations |
| `issues` | Issues management |
| `pull_requests` | PR management |
| `actions` | GitHub Actions workflows & CI/CD |
| `code_security` | Code scanning alerts |
| `copilot` | Copilot tools (remote only) |
| `dependabot` | Dependabot alerts |
| `discussions` | GitHub Discussions |
| `gists` | Gist management |
| `git` | Low-level Git operations |
| `labels` | Repository labels |
| `notifications` | Notifications |
| `orgs` | Organization tools |
| `projects` | GitHub Projects |
| `secret_protection` | Secret scanning |
| `security_advisories` | Security advisories |
| `stargazers` | Star management |
| `users` | User tools |

### Setup Notes
- **Remote (easiest)**: URL `https://api.githubcopilot.com/mcp/` — VS Code 1.101+
- **Docker**: `ghcr.io/github/github-mcp-server` with `GITHUB_PERSONAL_ACCESS_TOKEN`
- **Build from source**: `go build -o github-mcp-server ./cmd/github-mcp-server`
- Configure toolsets: `--toolsets "repos,issues,pull_requests"` or `GITHUB_TOOLSETS`
- Read-only mode: `--read-only`
- Lockdown mode: restrict public repo content
- GitHub Enterprise support (Cloud and Server)
- Insiders mode for early access features

---

## 11. GitMCP

- **Source:** https://github.com/idosal/git-mcp
- **Type:** Free, open-source, remote MCP server for any GitHub project
- **Language:** Go/Service

### Key Features
- Transforms any GitHub repo into documentation hub accessible via MCP
- Dynamic endpoint lets AI pick any repo on the fly
- Support for GitHub Pages sites
- Priority fetch order: `llms.txt` → `README.md` → other docs

### Tools
| Tool | Description |
|------|-------------|
| `fetch_<repo>_documentation` | Gets primary docs |
| `search_<repo>_documentation` | Searches docs with a query |
| `fetch_url_content` | Retrieves linked external content |
| `search_<repo>_code` | Searches actual code via GitHub Code Search |

### Setup Notes
- URL format: `https://gitmcp.io/{owner}/{repo}` or `https://{owner}.gitmcp.io/{repo}`
- Dynamic endpoint: `https://gitmcp.io/docs`
- Supported clients: Cursor, Windsurf, VSCode, Claude Desktop, Cline, Highlight AI, Augment Code, Msty
- Repository badge available: `[![GitMCP](https://gitmcp.io/badge/OWNER/REPO)]`
- Transport: streamable-http

---

## 12. Google Flights MCP

- **Community implementations (4+):**
  - `punitarani/fli` (Python, recommended) — https://github.com/punitarani/fli
  - `HaroldLeo/google-flights-mcp` (9 tools, SerpAPI)
  - `pulsemcp` TypeScript implementation
  - `tistaharahap/google-flights-mcp` (FastMCP + Docker)
- **Type:** Community-built (no official Google MCP)

### Key Features
- One-way and round-trip flight search
- Cheapest fare discovery across date ranges
- Airport code lookup
- Multi-passenger support
- Currency and cabin class filtering
- Price history and trend analysis

### Tools (fli — recommended)
| Tool | Description |
|------|-------------|
| `search_flights` | Search one-way flights |
| `search_round_trip` | Search round-trip flights |
| `get_cheapest_dates` | Find cheapest travel window |
| `search_airports` | Lookup airport codes by city |

### Setup Notes
- fli: `pip install fli` then `fli mcp`
- HaroldLeo: clone, `pip install -r requirements.txt`, optional `SERP_API_KEY`
- pulsemcp: `npm install` and `npm start`, no API key required
- Data sources: `fast-flights` (no key), SerpAPI (paid), direct scraping

---

## 13. Google Maps MCP

- **Source:** https://github.com/vicpeacock/google-maps-comprehensive-mcp
- **Alternative (18 tools):** https://github.com/cablate/mcp-google-map
- **Type:** Community implementation
- **Language:** TypeScript

### Key Features
- 8 tools covering geocoding, places, directions, elevation
- Uses Google's latest APIs (Places API New, Routes API, Geocoding API, Elevation API)

### Tools
| Tool | Description |
|------|-------------|
| `maps_ping` | Health check |
| `maps_geocode` | Forward geocoding |
| `maps_reverse_geocode` | Reverse geocoding |
| `maps_search_places` | Places search |
| `maps_place_details` | Place details (ratings, reviews, hours, photos) |
| `maps_distance_matrix` | Distance/duration matrix |
| `maps_elevation` | Elevation data |
| `maps_directions` | Turn-by-turn directions |

### Setup Notes
- Requires Google Maps API Key with Places, Routes, Geocoding, Elevation APIs enabled
- `npm install`, `npm run build`, `npm start`
- Docker available
- Alternative `cablate/mcp-google-map` has 18 tools including weather, air quality, batch geocode

---

## 14. Hacker News MCP

- **Source:** https://github.com/erithwik/mcp-hn
- **Alternative:** https://github.com/paabloLC/mcp-hacker-news (TypeScript)
- **Type:** Community implementation
- **Language:** Python
- **License:** See repository

### Key Features
- Fetch top/current stories from Hacker News
- Story details including comments
- Search stories
- User profile and activity information

### Tools
| Tool | Description |
|------|-------------|
| `get_stories` | Fetch top/current stories |
| `get_story_info` | Get detailed info about a specific story (incl. comments) |
| `search_stories` | Search Hacker News for stories |
| `get_user_info` | Retrieve user profile and activity |

### Setup Notes
- Install via Smithery: `npx -y @smithery/cli@latest run mcp-hn --key YOUR_SMITHERY_API_KEY`
- Docker available from `erithwik/mcp-hn:latest`
- Alternative TypeScript impl: `paabloLC/mcp-hacker-news`

---

## 15. Hostinger API MCP

- **Source:** https://github.com/hostinger/api-mcp-server
- **Package:** `hostinger-api-mcp`
- **Type:** Official Hostinger MCP server
- **Language:** Node.js (20+)
- **Official Docs:** https://www.hostinger.com/support/11079316-hostinger-api-mcp-server/

### Key Features
- Web hosting management (sites, files, databases)
- VPS creation and management
- Domain registration and renewal
- DNS record management
- Billing and subscription queries
- Per-product enable/disable granularity
- Supports stdio, HTTP streaming, and SSE transport

### API Products
| Product | Description |
|---------|-------------|
| Web Hosting | Manage hosting plans, files, DBs |
| VPS | Create and configure VPS instances |
| Domains | Register, transfer, renew domains |
| DNS | Manage DNS zones and records |
| Billing | Queries invoices and subscriptions |
| Reach | Marketing and outreach tools |

### Setup Notes
- `npm install -g hostinger-api-mcp`
- Or `npx hostinger-api-mcp` (no install)
- Authentication: API Token (`HOSTINGER_API_TOKEN`) or OAuth 2.0 with PKCE
- Transport modes: stdio (default), HTTP Streaming (`--http --port 8100`), SSE (`--sse`)

---

## 16. Markdownify MCP

- **Source:** https://github.com/zcaceres/markdownify-mcp
- **Type:** File/web content to Markdown conversion
- **Language:** TypeScript (Bun runtime)
- **License:** MIT
- **Commits:** 123

### Key Features
- Converts 10+ content types to Markdown: PDF, images, audio (transcription), web pages, Bing search, YouTube, DOCX, XLSX, PPTX, Git repos, existing Markdown files
- Directory restriction via `MD_ALLOWED_PATHS`

### Tools (10 total)
| Tool | Description |
|------|-------------|
| `youtube-to-markdown` | Convert YouTube videos to Markdown |
| `pdf-to-markdown` | Convert PDF files to Markdown |
| `bing-search-to-markdown` | Convert Bing search results to Markdown |
| `webpage-to-markdown` | Convert web pages to Markdown |
| `image-to-markdown` | Convert images to Markdown with metadata |
| `audio-to-markdown` | Convert audio files to Markdown with transcription |
| `docx-to-markdown` | Convert DOCX files to Markdown |
| `xlsx-to-markdown` | Convert XLSX files to Markdown |
| `pptx-to-markdown` | Convert PPTX files to Markdown |
| `get-markdown-file` | Retrieve existing Markdown file |

### Setup Notes
- Requires Bun and Python (for markitdown via venv)
- `git clone`, `bun install`, `bun run build`, `bun start`
- Docker: `mcp/markdownify`
- Environment: `MARKITDOWN_PATH`, `REPOMIX_PATH`, `MD_ALLOWED_PATHS`
- Alternative UTF-8 enhanced version: `jdjr2024/markdownify-mcp-utf8`

---

## 17. MarkItDown MCP

- **Source:** https://github.com/trsdn/markitdown-mcp
- **Type:** File format to Markdown conversion (29+ formats)
- **Language:** Python 3.10+
- **License:** MIT

### Key Features
- 29+ formats: PDF, Office docs, images, audio, web, books, archives, text
- Batch processing (convert entire directories)
- Metadata extraction (EXIF from images, speech-to-text from audio)
- Archive support (auto-extract and process `.zip` files)

### Tools
| Tool | Description |
|------|-------------|
| `convert_file` | Convert a single file to Markdown |
| `list_supported_formats` | Get complete list of supported formats |
| `convert_directory` | Convert all supported files in a directory |

### Supported Formats
- **Office:** `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.xls`
- **Images:** `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`
- **Audio:** `.mp3`, `.wav` (speech-to-text)
- **Web:** `.html`, `.htm`, `.xml`, `.json`, `.csv`
- **Books:** `.epub`
- **Archives:** `.zip`
- **Text:** `.txt`, `.md`, `.rst`

### Setup Notes
- `pipx install markitdown-mcp && pipx inject markitdown-mcp 'markitdown[all]'`
- For basic install: `pipx install markitdown-mcp`
- Docker available
- Based on Microsoft MarkItDown library (139k stars)

---

## 18. Memory (Knowledge Graph) MCP

- **Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- **Type:** Official MCP server — persistent memory via local knowledge graph
- **Language:** TypeScript
- **License:** MIT

### Key Features
- Entities (nodes) with: name, entityType, observations[]
- Relations: directed connections between entities (active voice)
- Observations: atomic/fact-based pieces of info attached to entities
- JSONL storage file

### Tools
| Tool | Description |
|------|-------------|
| `create_entities` | Create new entities |
| `create_relations` | Create directed relations |
| `add_observations` | Add observations to entities |
| `delete_entities` | Remove entities |
| `delete_observations` | Remove specific observations |
| `delete_relations` | Remove relations |
| `read_graph` | Read entire knowledge graph |
| `search_nodes` | Search entities by query |
| `open_nodes` | Open specific nodes by name |

### Setup Notes
- NPX: `npx -y @modelcontextprotocol/server-memory`
- Docker: `mcp/memory` with volume mount `claude-memory:/app/dist`
- Custom memory file path via `MEMORY_FILE_PATH` env var
- Alternative: `local-memory-mcp` npm package
- Remote memory generator: https://memory.mcpgenerator.com

---

## 19. Node Code Sandbox MCP

- **Source:** https://github.com/alfonsograziano/node-code-sandbox-mcp
- **Type:** Disposable Node.js sandbox via Docker containers
- **Language:** Node.js
- **Website:** https://jsdevai.com/

### Key Features
- Ephemeral Docker containers for JavaScript execution
- On-the-fly npm dependency installation
- Controlled resource limits (CPU/memory)
- File I/O support
- Multiple execution modes: one-off or persistent sandbox
- npm package search

### Tools
| Tool | Description |
|------|-------------|
| `run_js_ephemeral` | One-off script in disposable container |
| `sandbox_initialize` | Start a persistent sandbox container |
| `run_js` | Execute code in existing sandbox |
| `sandbox_exec` | Run shell commands in sandbox |
| `sandbox_stop` | Terminate and remove sandbox container |
| `search_npm_packages` | Search npm registry |

### Setup Notes
- **Docker must be installed and running**
- NPX: `npx -y node-code-sandbox-mcp` with `FILES_DIR` env var
- Pre-pull: `docker pull node:lts-slim` to avoid first-execution delays
- Docker Hub image: `mcp/node-code-sandbox`
- Requires Docker socket mount for container creation

---

## 20. NPM Sentinel MCP

- **Source:** https://github.com/Nekzus/npm-sentinel-mcp
- **Package:** `@nekzus/mcp-server` on npm
- **Type:** NPM package analysis with AI integration
- **Language:** Node.js/TypeScript
- **License:** MIT
- **Commits:** 363, **Releases:** 134

### Key Features
- Real-time package intelligence (security, deps, performance)
- 18+ specialized analysis tools
- Robust caching with invalidation strategies
- Lockfile-aware analysis (pnpm, npm, yarn)
- Multi-transport support (stdio + HTTP streamable)
- AI-assisted analysis through MCP integration

### Tools (18+)
| Tool | Description |
|------|-------------|
| `npmVersions` | Get all published versions |
| `npmLatest` | Get latest version info |
| `npmDeps` | Analyze dependencies |
| `npmTypes` | TypeScript definitions info |
| `npmSize` | Package size analysis |
| `npmVulnerabilities` | Security vulnerabilities |
| `npmTrends` | Download trends over time |
| `npmCompare` | Compare multiple packages |
| `npmMaintainers` | Maintainer information |
| `npmScore` | Quality/security/maintenance scores |
| `npmPackageReadme` | Fetch README content |
| `npmSearch` | Search NPM registry |
| `npmLicenseCompatibility` | License compatibility analysis |
| `npmRepoStats` | GitHub repository statistics |
| `npmDeprecated` | Check deprecation status |
| `npmChangelogAnalysis` | Analyze changelog patterns |
| `npmAlternatives` | Find alternative packages |
| `npmQuality` | Code quality metrics |
| `npmMaintenance` | Maintenance health indicators |

### Setup Notes
- NPX: `npx -y @nekzus/mcp-server@latest`
- Docker: `mcp/npm-sentinel` (mount to `/projects`)
- Custom registry via `NPM_REGISTRY_URL` env var
- Cache bypass with `{ "ignoreCache": true }` in tool arguments

---

## 21. Playwright MCP

- **Source:** https://github.com/microsoft/playwright-mcp
- **Type:** Official Microsoft Playwright MCP for browser automation
- **Language:** TypeScript/Node.js

### Key Features
- Browser automation via structured accessibility snapshots (not screenshots/vision)
- Supports Chrome, Firefox, WebKit, MS Edge
- Device emulation
- Network interception
- Session persistence
- Capabilities system for opt-in features (core, pdf, vision, devtools, network, storage, testing, config)

### Tools
- Core: `navigate`, `click`, `fill`, `type`, `snapshot`, `screenshot`, `evaluate`, `wait_for`, etc.
- Capabilities expand tools: PDF generation, vision-based interaction, devtools, network mocking, storage management, test assertions

### Setup Notes
- `npx @playwright/mcp@latest`
- Highly configurable: browser choice, headless mode, viewport, user agent, device emulation, timeouts
- Network security: allowed-hosts, allowed/blocked origins, proxy support
- Docker: `mcr.microsoft.com/playwright/mcp:latest`
- MCP config can be passed via args or env vars (prefix `PLAYWRIGHT_MCP_`)
- Alternative for coding agents: Playwright CLI (lower token cost)

---

## 22. Postman MCP

- **Source (official docs):** https://learning.postman.com/docs/reference/postman-api/postman-mcp-server/postman-mcp-local-server
- **GitHub:** https://github.com/postmanlabs/postman-mcp-server
- **Type:** Official Postman MCP server — local STDIO server
- **Language:** Node.js

### Key Features
- Access Postman API tools via MCP
- 100+ Postman API tools in Full mode
- API key authentication (Postman API key or Bearer token)
- Region support: `us` or `eu`
- Special `--quiet` mode for Windsurf on Windows

### Configurations
| Configuration | Description |
|--------------|-------------|
| Minimal (Default) | Essential tools for basic Postman operations |
| Code | Tools for searching API definitions + generating client code |
| Full | All 100+ Postman API tools |
| Quiet | Suppresses debug/info logs; required for Windsurf on Windows |

### Setup Notes
- `npx @postman/postman-mcp-server` with `--full`, `--code`, or `--minimal` flags
- Authentication: `POSTMAN_API_KEY` env var
- Region: `--region us|eu` or `POSTMAN_API_BASE_URL` env var
- Claude Desktop: download `.mcpb` file from releases
- Windsurf: use `--quiet` flag on Windows to avoid stderr buffer deadlock

---

## 23. Python Refactoring MCP

- **Type:** Community-driven integration pattern (no single canonical package)
- **Related projects:** rope, libcst, bowler, Sourcery, Refact.ai

### Key Features
- Wraps Python refactoring engines as MCP tools
- Supports rename, extract method/variable, inline, organize imports, format code, find references

### Common Approaches
1. **rope + MCP Wrapper** — mature refactoring engine (20+ transformations)
2. **libcst** (Instagram) — preserves formatting for codemods
3. **Sourcery** — AI-powered refactoring suggestions

### Tools
| Tool | Description |
|------|-------------|
| `rename_symbol` | Rename a class, function, or variable |
| `extract_method` | Extract selected code into a new function |
| `extract_variable` | Extract expression into a named variable |
| `inline_variable` | Inline a variable back to its usage |
| `organize_imports` | Sort and deduplicate imports (isort) |
| `format_code` | Apply black/ruff formatting |
| `find_references` | Find all usages of a symbol |

### Setup Notes
- `pip install "mcp[cli]" rope libcst`
- Wrapping with FastMCP is the recommended approach
- No single canonical package as of 2025

---

## 24. Redis MCP

- **Source:** https://github.com/redis/mcp-redis
- **Type:** Official Redis MCP server
- **Language:** Python
- **License:** MIT

### Key Features
- Natural language interface for Redis data management
- Supports: string, hash, list, set, sorted set, pub/sub, streams, JSON
- Transport: stdio, streamable-http
- Comprehensive connection management: host, port, SSL, ACL, cluster mode
- EntraID authentication for Azure Managed Redis
- Caching and documentation tools

### Tools
Core Redis operations: `get`, `set`, `delete`, `exists`, `keys`, `scan`, `incr`, `decr`, `lpush`, `lpop`, `lrange`, `sadd`, `srem`, `smembers`, `zadd`, `zrem`, `zrange`
Plus: `docs`, `query engine`, `server management`

### Setup Notes
- `uvx --from redis-mcp-server@latest redis-mcp-server --url redis://localhost:6379/0`
- Or `pip install redis-mcp-server`
- Connection URL formats: `redis://`, `rediss://` (encrypted), `rediss://` with cert verification
- EntraID auth for Azure Managed Redis (Service Principal, Managed Identity, Default Azure Credential)
- Docker: `mcp/redis`
- Config precedence: CLI args > Environment variables > Default values

---

## 25. ScrapeGraph MCP

- **Source:** https://github.com/ScrapeGraphAI/scrapegraph-mcp
- **Type:** Official ScrapeGraph MCP server — AI-powered web scraping
- **Language:** Python 3.13+
- **License:** MIT

### Key Features
- Production-ready integration with ScrapeGraph AI API v2
- Single page scraping with multiple output formats
- Structured extraction with prompt
- Web search
- Crawling with start/stop/resume
- Schema generation
- Monitor management
- Credit and history tracking

### Tools
| Tool | Description |
|------|-------------|
| `scrape` | Single page scraping (markdown, html, screenshot, etc.) |
| `extract` | Structured extraction with prompt and optional schema |
| `search` | Web search with num_results, country, time_range |
| `crawl_start` | Initiate crawl |
| `crawl_get_status` | Poll crawl status |
| `crawl_stop` / `crawl_resume` | Control crawl execution |
| `schema` | Generate/augment JSON Schema from prompt |
| `credits` | Check account credits |
| `history` | Paginated history |
| `monitor_create` / `list` / `get` / `pause` / `resume` / `delete` | Monitor management |

### Setup Notes
- Requires API key from https://dashboard.scrapegraphai.com
- `SGAI_API_KEY` environment variable required
- Remote server: `https://mcp.scrapegraphai.com/mcp` (no local install)
- Local: `python -m scrapegraph_mcp.server`
- v2 → v3 breaking changes: tool renames (smartscraper → extract, etc.)
- Docker available

---

## 26. Sentry MCP

- **Source:** https://github.com/getsentry/sentry-mcp
- **Type:** Official Sentry MCP server for human-in-the-loop coding agents
- **Language:** TypeScript/Node.js (monorepo)
- **License:** MIT
- **Commits:** 1,055

### Key Features
- Production endpoint: https://mcp.sentry.dev
- Designed for Cursor, Claude Code coding agents
- Acts as middleware to upstream Sentry API
- AI-powered search tools (require LLM provider: OpenAI or Anthropic)
- Self-hosted Sentry support

### Transport Modes
| Mode | Auth |
|------|------|
| Remote (Cloudflare) | OAuth via `mcp.sentry.dev` |
| Stdio (self-hosted) | User Auth Token + env vars |

### Setup Notes
- Production: use remote endpoint `https://mcp.sentry.dev` (OAuth)
- Self-hosted: `stdio --host=sentry.example.com`
- Required Sentry User Auth Token scopes: `org:read`, `project:read`, `project:write`, `team:read`, `team:write`, `event:write`
- Claude Code Plugin: `sentry-mcp` (auto-delegates for errors, issues, traces)
- Local dev: `make setup`, `make dev`, test at `http://localhost:5173`

---

## 27. Sequential Thinking MCP

- **Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- **Type:** Official MCP server — structured step-by-step reasoning
- **Language:** TypeScript
- **License:** MIT

### Key Features
- Single tool for dynamic, reflective problem-solving
- Supports: thought steps, revisions, branching, needs-more-thoughts signaling

### Tool: `sequential_thinking`

| Parameter | Type | Description |
|-----------|------|-------------|
| `thought` | string | Current thinking step |
| `nextThoughtNeeded` | boolean | Whether another step is required |
| `thoughtNumber` | number | Current step number |
| `totalThoughts` | number | Estimated total steps |
| `isRevision` | boolean | Whether this revises a previous thought |
| `revisesThought` | number | Which thought number this revises |
| `branchFromThought` | number | Branch point for alternative reasoning |
| `branchId` | string | Identifier for reasoning branch |
| `needsMoreThoughts` | boolean | Whether additional thoughts needed |

### Setup Notes
- NPX: `npx -y @modelcontextprotocol/server-sequential-thinking`
- Docker: `mcp/sequentialthinking`
- Windows NPX: `cmd /c npx ...`
- Environment variable: `DISABLE_THOUGHT_LOGGING=true`
- Alternative Python implementation available

---

## 28. SQLite MCP

- **Source (Go):** https://github.com/liliang-cn/mcp-sqlite-server
- **Alternatives:** `@berthojoris/mcp-sqlite-server` (TypeScript), Augment Code mcp-sqlite, VS Code extension
- **Type:** Community implementation
- **Language:** Go (primary), TypeScript, Python

### Key Features
- Full SQLite database interaction
- Directory-restricted access for security
- 19 tools: queries, table management, indexes, databases, optimization

### Tools (19 total)
| Tool | Description |
|------|-------------|
| `query` | Execute SELECT query |
| `execute` | Execute non-SELECT statements |
| `transaction` | Execute multiple statements in a transaction |
| `create_table` | Create a new table |
| `list_tables` | List all tables |
| `describe_table` | Get detailed schema info |
| `drop_table` | Drop a table |
| `create_index` | Create an index |
| `list_indexes` | List all indexes |
| `drop_index` | Drop an index |
| `create_database` | Create a new database file |
| `database_exists` | Check if a database exists |
| `switch_database` | Switch current database context |
| `current_database` | Get current database name |
| `list_database_files` | List all database files |
| `delete_database` | Delete a database file |
| `vacuum` | Run VACUUM to reclaim space |
| `analyze_query` | Analyze query execution plan |
| `database_stats` | Get database statistics |

### Setup Notes
- Go: `go install github.com/liliang-cn/mcp-sqlite-server@latest`
- Must specify at least one database path or directory
- TypeScript alternative: `npx @berthojoris/mcp-sqlite-server sqlite:///path`
- Permission levels for TS version: list, read, create, update, delete, ddl, transaction, utility

---

## 29. Stripe MCP

- **Source:** https://github.com/stripe/ai/tree/main/tools/modelcontextprotocol
- **Package:** `@stripe/mcp`
- **Type:** Official Stripe MCP server
- **Language:** Node.js (18+)
- **Official Docs:** https://docs.stripe.com/mcp

### Key Features
- Customer lifecycle management (create, list, update)
- Product and price management
- Payment link and intent creation
- Invoice generation and management
- Balance queries and dispute handling
- Documentation search within Stripe docs
- Hosted remote server at `https://mcp.stripe.com` (OAuth)

### Tools
| Tool | Description |
|------|-------------|
| `customers.create` | Create a new Stripe customer |
| `customers.read` | Retrieve customer details |
| `products.create` | Create a product in the catalog |
| `prices.create` | Set pricing for a product |
| `payment_links.create` | Generate a shareable payment link |
| `payment_intents.create` | Initiate a payment intent |
| `invoices.create` | Create a new invoice |
| `invoices.send` | Send invoice to customer |
| `balance.retrieve` | Get current account balance |
| `documentation.search` | Search Stripe documentation |

### Setup Notes
- `npx -y @stripe/mcp --tools=all --api-key=$STRIPE_SECRET_KEY`
- Use **Restricted API Keys** (`rk_*`) for least privilege
- Test with test mode keys (`sk_test_*`) before production
- Remote server: `https://mcp.stripe.com` with OAuth
- Compatible with Cursor, Claude Desktop, Codex CLI
- Programmatic: `npm install @stripe/agent-toolkit/modelcontextprotocol`

---

## 30. Targets

- **File:** `docs/mcp-research/targets.md`
- **Type:** Phase 2 MCP Research target tracking spreadsheet
- **Total targets:** 42

### Complete Target List
The file tracks 42 MCP servers targeted for research, including all 34 documented servers plus:
- 8 additional: apify, chroma, neo4j memory, next.js devtools, python interpreter, neon, shadcn, linear, mcp-docker

### Status
- All 34 documented servers: extracted (this document)
- Remaining 8 targets: searched status pending

---

## 31. Time MCP

- **Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/time
- **Type:** Official MCP server — time and timezone conversion
- **Language:** Python
- **License:** MIT

### Tools
| Tool | Description |
|------|-------------|
| `get_current_time` | Get current time in a specific timezone |
| `convert_time` | Convert time between timezones |

### Setup Notes
- `uvx mcp-server-time` (recommended)
- Or `pip install mcp-server-time`
- Docker: `mcp/time`
- Override system timezone: `--local-timezone America/New_York`
- Uses IANA timezone names

---

## 32. uv MCP

- **Source:** https://github.com/astral-sh/uv
- **Package:** `uv` (Astral) — `mcp-server-uv`
- **Type:** Official uv MCP server — Python package manager
- **Language:** Rust
- **Docs:** https://docs.astral.sh/uv/

### Key Features
- Extremely fast Python package manager (10-100x faster than pip)
- Drop-in replacement for pip, pip-tools, pipx, poetry, pyenv, virtualenv
- MCP enables AI agents to manage Python environments

### Tools
| Tool | Description |
|------|-------------|
| `uv_install` | Install one or more packages |
| `uv_run` | Run a Python script with uv |
| `uv_add` | Add dependency to project |
| `uv_remove` | Remove a dependency |
| `uv_sync` | Sync environment with lockfile |
| `uv_python` | Manage Python version for project |
| `uv_venv` | Create a new virtual environment |

### Setup Notes
- `uvx mcp-server-uv` or `uv tool run mcp-server-uv`
- Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh` (Linux/macOS)
- Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Performance: Rust implementation, aggressive caching, parallel downloads

---

## 33. Vitest MCP

- **Source:** https://github.com/djankies/vitest-mcp
- **Package:** `@djankies/vitest-mcp`
- **Type:** AI-optimized Vitest test runner
- **Language:** Node.js/TypeScript
- **License:** MIT
- **Commits:** 94, **Releases:** 12

### Key Features
- LLM-Optimized Output: clean, structured test results for AI consumption
- Log Capturing: `console.log`/`console.error` with `[stdout]`/`[stderr]` prefixes
- Line-by-Line Coverage: detailed coverage analysis with gap insights
- Multi-Repository Support: works across monorepos
- Claude Code Hook: automatically redirects Vitest commands to MCP tools

### Tools
| Tool | Description |
|------|-------------|
| `set_project_root` | **Required first** — sets project root |
| `list_tests` | Lists test files in your project |
| `run_tests` | Executes tests with structured output |
| `analyze_coverage` | Analyzes test coverage with gap insights |

### Setup Notes
- `npx -y @djankies/vitest-mcp`
- Prerequisites: `npm install --save-dev vitest@latest @vitest/coverage-v8@latest`
- Supports Claude Code, Claude Desktop, VS Code, Cursor, Windsurf, Cline
- Multi-IDE support
- Coverage thresholds configured in `vitest.config.ts`, not MCP parameters

---

## 34. YouTube Transcript MCP

- **Source:** https://github.com/kyong0612/youtube-mcp
- **Type:** High-performance YouTube transcript fetching
- **Language:** Go
- **License:** MIT

### Key Features
- Fetch transcript for single or multiple YouTube videos
- Translate transcripts to target language
- Format output (JSON, text, SRT, VTT)
- List available transcript languages
- Optional Redis caching
- Monitoring with Prometheus + Grafana

### Tools
| Tool | Description |
|------|-------------|
| `get_transcript` | Fetch transcript for a single video |
| `get_multiple_transcripts` | Fetch transcripts for multiple videos |
| `translate_transcript` | Translate transcript to target language |
| `format_transcript` | Format transcript output (JSON, text, SRT, VTT) |
| `list_available_languages` | List available transcript languages |

### Setup Notes
- Go 1.21+ required for building
- Quick install: `curl -fsSL https://raw.githubusercontent.com/kyong0612/youtube-mcp/main/scripts/install.sh | bash`
- Or `go install github.com/kyong0612/youtube-mcp/cmd/youtube-mcp-stdio@latest`
- Docker: `ghcr.io/kyong0612/youtube-mcp:latest`
- Cache options: `memory` (default), `redis`, `none`
- Configuration: `.env` file with `YOUTUBE_DEFAULT_LANGUAGES`, `CACHE_TYPE`, `LOG_LEVEL`, etc.
