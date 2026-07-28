# 🏗 Technology Stack Blueprint — SandBox Monorepo

**Workspace:** `C:\Users\Alexa\Desktop\SandBox`
**Generated:** 2026-07-28
**Depth:** Comprehensive
**Categorization:** Technology Type × Layer

---

## 1. Technology Identification Phase

### 1.1 Languages Detected

| Language | Version(s) | Projects Using | File Extensions |
|----------|-----------|----------------|-----------------|
| **TypeScript** | 5.9 (root), 6.0 (Banking), 5.x (most) | All JS/TS projects | `.ts`, `.tsx`, `.mts`, `.cts` |
| **JavaScript** | ES2024 (ESNext modules) | Legacy/webpack projects | `.js`, `.jsx`, `.mjs`, `.cjs` |
| **Python** | 3.11 (root), 3.12 (Django), 3.10 (legacy) | Django projects, scripts, automation | `.py`, `.pyi` |
| **Bash** | POSIX | `.github/workflows`, scripts | `.sh` |
| **PowerShell** | 5.1+ | Windows automation | `.ps1` |
| **Go** | 1.22 | mcp-servers/go | `.go` |
| **Rust** | 2021 edition | mcp-servers/rust | `.rs` |
| **Java** | 17+ (Maven) | mcp-servers/java | `.java` |
| **Kotlin** | 1.9.22 (Gradle) | mcp-servers/kotlin | `.kt` |
| **PHP** | 8.2+ (Composer) | mcp-servers/php | `.php` |
| **Swift** | 6.0 tools, macOS 15 | mcp-servers/swift | `.swift` |
| **C#** | 12.0 (.NET 8) | mcp-servers/csharp | `.cs` |

### 1.2 Runtimes & Package Managers

| Runtime/Manager | Version | Usage |
|----------------|---------|-------|
| **Bun** | 1.3.14 | Primary runtime & package manager (root, Banking, Bash, Resume_maker) |
| **Node.js** | 18+ / 22 | Legacy projects (xamehi, selenium_webdriver, Django-Scrapy-Selenium) |
| **pnpm** | 9.12.3 | comicwise |
| **npm** | Latest (bundled) | Legacy JS projects |
| **pip** | Latest | Python dependency management |
| **uv** | Latest | Alternative Python package management |
| **Cargo** | Built-in | Rust (mcp-servers/rust) |
| **Maven** | 3.9+ | Java (mcp-servers/java) |
| **Gradle** | 8.x (Kotlin DSL) | Kotlin (mcp-servers/kotlin) |
| **Composer** | 2.x | PHP (mcp-servers/php) |
| **SwiftPM** | Built-in | Swift (mcp-servers/swift) |
| **dotnet CLI** | 8.x | C# (mcp-servers/csharp) |

---

## 2. Core Technologies Analysis

### 2.1 TypeScript / Bun Stack (Primary)

#### Root TypeScript Configuration
```json
{
  "target": "ESNext",
  "module": "Preserve",
  "moduleResolution": "bundler",
  "strict": true,
  "skipLibCheck": true,
  "noUncheckedIndexedAccess": true,
  "noImplicitOverride": true,
  "verbatimModuleSyntax": true,
  "noEmit": true
}
```

#### Key Workspace Dependencies (Root)
| Package | Version | Type |
|---------|---------|------|
| `@types/bun` | 1.3.14 (latest) | dev |
| `typescript` | ^5.9.3 | peer |

#### Bun Lockfile
- **File:** `bun.lock` (v1 format)
- **Managed by:** `bun install`
- **Workspaces:** Root only (monorepo root)

---

### 2.2 Python Stack

#### Python Configuration (Root)
| Setting | Value |
|---------|-------|
| **Version** | 3.11 (pyrightconfig.json) |
| **Linter** | Ruff 0.15.10 (`.ruff.toml`) |
| **Type Checker** | Pyright (basic mode) |
| **Line Length** | 120 |
| **Quote Style** | Double |

#### Root Python Dependencies (`requirements.txt`)
| Category | Key Packages |
|----------|-------------|
| **AI/LLM SDKs** | `anthropic==0.87.0`, `openai==2.24.0` |
| **Web Framework** | `fastapi==0.139.0`, `starlette==1.3.1`, `uvicorn==0.51.0` |
| **MCP Protocol** | `mcp==1.28.1` |
| **HTTP Clients** | `httpx==0.28.1`, `httpx-sse==0.4.3`, `aiohttp==3.14.1`, `requests==2.33.0` |
| **Cloud SDKs** | `boto3==1.42.89`, `google-api-python-client==2.194.0`, `google-auth==2.55.1` |
| **Chat/Messaging** | `discord-py==2.7.1`, `slack-bolt==1.27.0`, `slack-sdk==3.40.1`, `python-telegram-bot==22.6` |
| **MS Teams** | `microsoft-teams-api==2.0.13.4`, `microsoft-teams-apps==2.0.13.4`, `microsoft-teams-cards==2.0.13.4`, `microsoft-teams-common==2.0.13.4` |
| **Auth** | `msal==1.37.0`, `oauthlib==3.3.1`, `pyjwt==2.13.0`, `google-auth-oauthlib==1.3.1` |
| **Validation** | `pydantic==2.13.4`, `pydantic-core==2.46.4`, `pydantic-settings==2.14.2` |
| **Data** | `youtube-transcript-api==1.2.4`, `pillow==12.3.0`, `tabulate==0.10.0`, `tqdm==4.68.4` |
| **Testing** | `pytest==9.0.3`, `pytest-asyncio==1.3.0` |
| **Dev Tooling** | `ruff==0.15.10` |

#### Hermes Agent Dependency
- **Package:** `hermes-agent` (editable)
- **Path:** `file:///C:/Users/Alexa/AppData/Local/hermes/hermes-agent`
- **Purpose:** Local development of Hermes Agent itself

---

### 2.3 Frontend Frameworks

| Framework | Version | Projects |
|-----------|---------|----------|
| **Next.js** | 16.2.4 | Banking, rhixecompany-comics (frontend) |
| **Next.js** | 15.3-15.4 | comicwise, rhixe_scans, university-libary-jsm |
| **React** | 19.x | All Next.js 15/16 projects |
| **React** | 18.2 | xamehi (CRA) |
| **React** | 17.x | xamehi.tv (CRA) |
| **Django Templates** | 5.x / 4.x | profile, ecom, xamehi.tv, cookiecutter-django-tailwind |

---

### 2.4 Backend Frameworks & APIs

| Framework | Version | Projects |
|-----------|---------|----------|
| **Django** | 5.x | rhixecompany-comics, cookiecutter-django-tailwind |
| **Django** | 4.x | profile |
| **Django** | 3.1 | ecom |
| **DRF** | 3.15+ | rhixecompany-comics, xamehi, xamehi.tv, ecom |
| **DRF** | 3.13 | ecom |
| **Express.js** | ^4.18 | xamehi, mcp-servers/copilot-studio |
| **FastAPI** | 0.139.0 | Root automation services |
| **Prisma** | 6.x | comicwise, rhixe_scans, rhixecompany-comics (frontend) |
| **Drizzle ORM** | 0.44-0.45 | Banking, university-libary-jsm |
| **NextAuth.js** | v4 / v5 (beta) | Banking, comicwise, rhixe_scans, university-libary-jsm |
| **SimpleJWT** | 5.2-5.3 | ecom, xamehi.tv, rhixecompany-comics |

---

### 2.5 Databases & Storage

| Technology | Version | Projects | Purpose |
|------------|---------|----------|---------|
| **PostgreSQL** | Latest | All Django/Next.js apps | Primary relational DB |
| **Neon** | Serverless | university-libary-jsm | Serverless PostgreSQL |
| **SQLite** | 3.x | Dev environments | Lightweight dev DB |
| **Redis** | Latest | rhixe_scans, university-libary-jsm, rhixecompany-comics | Caching, sessions, Celery broker |
| **Upstash Redis** | ^1.37 | Banking, comicwise, university-libary-jsm | Serverless Redis (QStash, Rate Limiting) |
| **Google Cloud Storage** | - | profile | Media file storage |
| **UploadThing** | ^7 | rhixe_scans | File upload service |
| **ImageKit** | ^6 | comicwise, university-libary-jsm | Image optimization, CDN |
| **Cloudinary** | ^2.9 | comicwise | Image hosting |

---

### 2.6 Payment / Fintech

| Service | Projects | Integration |
|---------|----------|-------------|
| **Plaid** | Banking | Account linking, transactions |
| **Dwolla** | Banking | ACH transfers |
| **Stripe** | comicwise, rhixe_scans, rhixecompany-comics | Subscriptions, payments |
| **PayPal** | rhixe_scans, xamehi.tv, ecom | Payment processing |

---

### 2.7 Tooling & Quality Gates

| Tool | Purpose | Config |
|------|---------|--------|
| **TypeScript** (`tsc --noEmit`) | Type checking | `tsconfig.json` (strict) |
| **ESLint** 10 (flat config) | JS/TS linting (zero-warnings) | `eslint.config.mts` |
| **Prettier** 3 | Code formatting | `.prettierrc.ts` |
| **Ruff** | Python linting & formatting | `.ruff.toml` |
| **Pyright** | Python type checking | `pyrightconfig.json` |
| **markdownlint-cli2** | Markdown linting | `.markdownlintrc.json` |
| **cspell** 10 | Spell checking | `cspell.json` |
| **pre-commit** 4.6 | Git hooks | `.pre-commit-config.yaml` |
| **git-cliff** 2.13 | Changelog generation | `cliff.toml` |
| **EditorConfig** | Cross-editor consistency | `.editorconfig` |
| **ShellCheck + shfmt** | Shell script quality | `.shellcheckrc` |
| **codespell** | Spelling verification | `.codespellrc` |

---

### 2.8 MCP Server Ecosystem (16 Servers)

| Server | Purpose |
|--------|---------|
| `ast-grep` | AST-based code search & replace |
| `code-sandbox` | Isolated Node.js execution |
| `fetch` | HTTP content extraction |
| `filesystem` | Sandboxed file operations |
| `github` | GitHub API operations |
| `linear` | Project management |
| `mcp-docker` | Container management |
| `memory` | Persistent agent memory |
| `mindstudio` | Multi-modal AI tools |
| `playwright` | Browser automation |
| `sequential-thinking` | Structured reasoning |
| `smithery` | MCP registry |
| `python-quality` | Ruff + Pyright integration |
| `tooling-lint` | ESLint, Prettier, markdownlint, cspell |
| `tooling-config` | Pre-commit, git-cliff, editorconfig |
| `copilot-mcp` | GitHub Copilot integration |

---

## 3. Per-Project Technology Stack Index

Each project has its own `TECHNOLOGY_STACK.md` in its root directory:

| Project | Path | Stack Summary |
|---------|------|---------------|
| **Banking** | `projects/Banking/TECHNOLOGY_STACK.md` | Next.js 16 + Drizzle + Plaid/Dwolla + Bun |
| **Bash** | `projects/Bash/TECHNOLOGY_STACK.md` | TypeScript/Bun 6-phase automation orchestrator |
| **comicwise** | `projects/comicwise/TECHNOLOGY_STACK.md` | Next.js 15 + Drizzle + Stripe + pnpm |
| **cookiecutter-django-tailwind** | `projects/cookiecutter-django-tailwind/TECHNOLOGY_STACK.md` | Django 5 + Tailwind template generator |
| **Django-Scrapy-Selenium** | `projects/Django-Scrapy-Selenium/TECHNOLOGY_STACK.md` | Django + Scrapy + Selenium + Celery (consolidation target) |
| **ecom** | `projects/ecom/TECHNOLOGY_STACK.md` | Django 3.1 + DRF + React/Redux + PayPal (legacy) |
| **mcp-servers** | `projects/mcp-servers/*/TECHNOLOGY_STACK.md` | 10 language MCP server implementations |
| **profile** | `projects/profile/TECHNOLOGY_STACK.md` | Django 4.x + GCS + CKEditor 5 |
| **Python-projects** | `projects/Python-projects/TECHNOLOGY_STACK.md` | 18 standalone Python scripts |
| **Resume_maker** | `projects/Resume_maker/TECHNOLOGY_STACK.md` | Bun CLI: JSON → Markdown → PDF |
| **rhixe_scans** | `projects/rhixe_scans/TECHNOLOGY_STACK.md` | Next.js 15 + Prisma + WebSocket + Stripe/PayPal |
| **rhixecompany-comics** | `projects/rhixecompany-comics/TECHNOLOGY_STACK.md` | Django 5 + Next.js 16 (dual-stack) |
| **selenium_webdriver** | `projects/selenium_webdriver/TECHNOLOGY_STACK.md` | Node.js 18 + Selenium 4 CLI scraper |
| **university-libary-jsm** | `projects/university-libary-jsm/TECHNOLOGY_STACK.md` | Next.js 15 + Drizzle + Neon + Upstash Redis |
| **xamehi** | `projects/xamehi/TECHNOLOGY_STACK.md` | Django + Express + React 18 CRA (legacy) |
| **xamehi.tv** | `projects/xamehi.tv/TECHNOLOGY_STACK.md` | DRF + React 17 + Material-UI + PayPal |
| **youtube-downloader** | `projects/youtube-downloader/TECHNOLOGY_STACK.md` | Python + yt-dlp + curl_cffi CLI |

---

## 4. Coding Conventions

### 4.1 Workspace-Wide Standards

| Convention | Rule |
|-----------|------|
| **Line Endings** | CRLF (`.editorconfig`, Windows host) |
| **Indent (TS/JS)** | 2 spaces |
| **Indent (Python)** | 4 spaces |
| **Indent (YAML)** | 2 spaces |
| **Quotes (TS/JS)** | Single quotes |
| **Quotes (Python)** | Double quotes |
| **UTF-8** | Required everywhere |
| **Trailing Whitespace** | Trimmed |
| **Final Newline** | Required at EOF |
| **Backup Files** | Forbidden (`.bak`, `.old`, `.backup`) — use git |
| **Secrets** | Never committed (`.env` in `.gitignore`) |

### 4.2 TypeScript Conventions

| Rule | Standard |
|------|----------|
| **Strict Mode** | All strict flags enabled |
| **No `any`** | Banned — use `unknown` + type guards |
| **Module System** | ESM (`"type": "module"`) |
| **No Emit** | `noEmit: true` (Bun handles transpilation) |
| **Path Aliases** | `@/` → `src/` |
| **Naming (Components)** | PascalCase (`UserProfile.tsx`) |
| **Naming (Hooks)** | camelCase (`useAuth.ts`) |
| **Naming (Utils)** | camelCase (`formatDate.ts`) |
| **Naming (Pages)** | kebab-case (`user-profile/page.tsx`) |
| **Validation** | zod v4 for all API inputs |
| **Formatting** | Prettier 3 (tailwindcss, organize-imports plugins) |

### 4.3 React Conventions

| Rule | Standard |
|------|----------|
| **Components** | Function components only (no classes) |
| **Server Components** | Default in App Router |
| **Client Components** | Only when needed (`'use client'`) |
| **State Management** | Zustand (global), TanStack Query (server) |
| **Styling** | `cn()` utility + CVA for variants |
| **Forms** | react-hook-form + zod resolver |
| **Animations** | Framer Motion (comicwise), embla-carousel (carousels) |

### 4.4 Python Conventions

| Rule | Standard |
|------|----------|
| **Style** | PEP 8 |
| **Type Hints** | Required in all new code |
| **Linting** | Ruff (E, F, I, N, W, UP, B, SIM, ARG, RUF) |
| **Formatting** | Ruff formatter (line-length: 120) |
| **Imports** | isort-style (ruff lint I) |
| **Naming** | `snake_case` (vars/funcs), `PascalCase` (classes) |
| **Config** | Settings hierarchy (base → local → production) |

### 4.5 Git & Branching Conventions

| Convention | Standard |
|------------|----------|
| **Branch Strategy** | `production` ← `staged` ← `development` ← `feature/*` |
| **Branch Naming** | `<type>/<project>/<kebab-case-description>` |
| **Types** | `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf` |
| **Commit Format** | Conventional: `<type>: <description>` |
| **Rebase** | Prefer over merge (linear history) |
| **PR Target** | `development` (never `production` directly) |
| **PR Size** | <100 files recommended |

### 4.6 Testing Conventions

| Stack | Framework | Location | Pattern |
|-------|-----------|----------|---------|
| **TypeScript/Bun** | Vitest | `**/*.test.ts` alongside source | Unit + component |
| **React** | Vitest + @testing-library/react | `**/*.test.tsx` | Render, fire, assert |
| **E2E** | Playwright | `tests/` or `e2e/` | Page-level flows |
| **Python (Django)** | pytest + pytest-django | `tests/` per app | Test DB, API clients |
| **Python (scripts)** | pytest | `test_*.py` alongside | Unit + integration |
| **Shell** | bash test scripts | `tests/verify-dryrun.sh` | Dry-run verification |

### 4.7 CI/CD Conventions

| Convention | Detail |
|------------|--------|
| **PR Workflow** | `pr-ci.yml` — detects changed projects, runs project-appropriate checks |
| **Type Check Gate** | `tsc --noEmit` (TS) or `pyright` (Python) |
| **Lint Gate** | ESLint `--max-warnings=0` or `ruff check` |
| **Format Gate** | Prettier `--check` or Ruff `format --check` |
| **Spell Gate** | cspell + codespell |
| **Forbidden Files** | Blocks `.env`, credentials, binaries |
| **Deploy** | Push to `production` triggers deployment workflows |

---

## 5. Dependency Map & Cross-Project Relationships

```
SandBox Root
├── .github/workflows/ ────────── CI/CD for ALL projects
│
├── projects/Banking/ ─────────── Next.js 16 + Drizzle + Plaid/Dwolla
├── projects/Bash/ ────────────── Bun/TS automation (6-phase orchestrator)
├── projects/comicwise/ ───────── Next.js 15 + Drizzle + Stripe + pnpm
├── projects/cookiecutter-django-tailwind/ ── Template (not run directly)
├── projects/Django-Scrapy-Selenium/ ────── Legacy → consolidating into rhixecompany-comics
├── projects/ecom/ ────────────── Legacy dual-stack (Django 3.1 + React/Redux)
├── projects/mcp-servers/ ─────── MCP examples (10 languages)
│   ├── copilot-studio/ ──────── TypeScript HTTP MCP for Power Platform
│   ├── go/ ──────────────────── Go 1.22
│   ├── java/ ────────────────── Java 17 + Maven
│   ├── kotlin/ ──────────────── Kotlin 1.9 + Gradle
│   ├── php/ ─────────────────── PHP 8.2 + Composer
│   ├── python/ ──────────────── Python 3.11 + mcp[cli]
│   ├── ruby/ ────────────────── Ruby 3.x + mcp gem
│   ├── rust/ ────────────────── Rust 2021 + rmcp
│   ├── swift/ ───────────────── Swift 6 + SwiftPM
│   ├── csharp/ ──────────────── C# 12 + .NET 8
│   └── typescript/ ──────────── TypeScript + MCP SDK 1.9
├── projects/profile/ ─────────── Django 4.x + GCS + CKEditor 5
├── projects/Python-projects/ ─── 18 standalone Python scripts
├── projects/Resume_maker/ ────── Bun CLI: JSON → Markdown → PDF
├── projects/rhixe_scans/ ─────── Next.js 15 + Prisma + WebSocket + Stripe/PayPal
├── projects/rhixecompany-comics/ ── Django 5 + Next.js 16 (dual-stack)
│   ├── backend/ ──────────────── Django + DRF + Celery + Scrapy
│   └── frontend/ ─────────────── Next.js 16 App Router
├── projects/selenium_webdriver/ ── Node.js 18 + Selenium 4 CLI
├── projects/university-libary-jsm/ ── Next.js 15 + Drizzle + Neon + Upstash
├── projects/xamehi/ ──────────── Django + Express + React 18 CRA (legacy)
├── projects/xamehi.tv/ ───────── DRF + React 17 + Material-UI + PayPal
└── projects/youtube-downloader/ ── Python + yt-dlp + curl_cffi CLI
```

---

## 6. Technology Decision Context

### Key Architectural Decisions

1. **Bun as Primary Runtime** — Chosen for speed, TypeScript-native support, built-in test runner/toolchain. Used across most active TypeScript projects.

2. **Drizzle vs Prisma** — Drizzle used in newer projects (Banking, university-libary-jsm) for lighter footprint and SQL-like approach. Prisma retained in rhixe_scans/comicwise for mature schema management.

3. **Next.js 16 (App Router)** — Adopted for all new projects. React 19 Server Components reduce client JS. Turbopack for dev.

4. **Tailwind CSS v4** — Adopted in newer projects (Banking) with CSS-first configuration. v3 retained in rhixe_scans.

5. **Dual-Stack (Django + Next.js)** — rhixecompany-comics demonstrates hybrid: Django for backend/celery/scraping, Next.js for frontend/SSR.

6. **Monorepo with Autonomy** — Each subproject independently configurable with its own `AGENTS.md`, tooling config, and CI pipeline. Shared root tooling for consistency.

7. **MCP-First Tooling** — Prefer MCP servers over native CLI for every capability (16 servers integrated).

### Deprecated / Consolidation Targets

| Project | Reason | Replacement |
|---------|--------|-------------|
| xamehi | Legacy 3-service architecture | Consolidate to single stack |
| ecom | Django 3.1 (EOL), Python 3.10 (EOL Oct 2026) | Upgrade to Django 5.x |
| Django-Scrapy-Selenium | Scraping moved to rhixecompany-comics | rhixecompany-comics |
| Python-projects (partial) | 18 beginner scripts | Archive candidate |

---

*Generated by Hermes Agent — Technology Stack Blueprint Generator*
*Per-project details in each `projects/*/TECHNOLOGY_STACK.md`*