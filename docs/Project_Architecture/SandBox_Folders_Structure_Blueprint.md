# SandBox Workspace — Folder Structure Blueprint

> **Generated:** 2026-07-28  
> **Workspace:** `C:\Users\Alexa\Desktop\SandBox`  
> **Scope:** Root-level monorepo + 17 sub-projects under `projects/`  
> **Organization:** Monorepo — root-level automation/config + isolated per-project directories

---

## 1. Structural Overview

The SandBox workspace is a **monorepo** containing:

- **Root level:** Workspace automation scripts, configuration files, CI/CD, Hermes agent config, documentation, and research artifacts
- **`projects/` subdirectory:** 17 independent projects spanning web apps (Next.js, Django, React), CLI tools, scraping platforms, MCP server implementations, a documentation-only project, and a cookiecutter template

### Organizational Principles

| Principle | Description |
|-----------|-------------|
| **Project isolation** | Each project lives in its own directory under `projects/` with its own config, dependencies, and documentation |
| **Workspace-level automation** | Root-level scripts (Python, Bash) orchestrate cross-project operations, audits, and quality checks |
| **AI/Agent tooling** | `.github/prompts/` contains 150+ prompt templates consumed by Copilot, Codex, and Hermes agents |
| **Self-documenting** | Every project has `README.md`, `THE_STORY_OF_THIS_REPO.md`, and `docs/Project_Architecture/` |
| **Root-level documentation** | `docs/` at workspace root aggregates cross-cutting blueprints, audits, and reports |

---

## 2. Workspace Root — Directory Visualization

```
SandBox/
├── .editorconfig
├── .git/
├── .gitattributes
├── .git-blame-ignore-revs
├── .github/
│   ├── prompts/               # 150+ prompt.md templates for agents
│   └── ...                     # CI/workflows
├── .gitignore
├── .gitmodules
├── .hermes/                    # Hermes agent config
├── .hermes.md
├── .mcp.json                   # MCP server registrations
├── .vscode/                    # VS Code workspace settings
├── __pycache__/
├── _pathutil.py
├── AGENTS.html / AGENTS.md     # Agent inventory
├── CLAUDE.md                   # Claude agent instructions
├── CLEANUP_SUMMARY.md
├── CONTRIBUTING.md
├── HERMES_PROFILE_REPORT.md
├── README.md
├── REPOSITORY_SUMMARY.md
├── docs/                       # Root-level documentation
│   ├── Project_Architecture/   # (this file lives here)
│   ├── architecture/
│   ├── archive/
│   ├── audit/
│   ├── catalog/
│   ├── folder-structure/
│   ├── mcp/
│   ├── research/
│   ├── tech-stack/
│   └── vscode-extensions/
├── earnings-kit/               # Research artifacts
├── node_modules/
├── packages/...                # (if applicable)
├── plan/ plans/
├── projects/                   # 17 sub-projects (detailed below)
│   ├── Banking/
│   ├── Bash/
│   ├── comicwise/
│   ├── cookiecutter-django-tailwind/
│   ├── Django-Scrapy-Selenium/
│   ├── docs/
│   ├── ecom/
│   ├── mcp-servers/
│   ├── profile/
│   ├── Python-projects/
│   ├── Resume_maker/
│   ├── rhixe_scans/
│   ├── rhixecompany-comics/
│   ├── selenium_webdriver/
│   ├── university-libary-jsm/
│   ├── xamehi/
│   ├── xamehi.tv/
│   └── youtube-downloader/
├── research/
├── results/
├── scripts/
├── judge_results/
└── ... (root Python/TS scripts)
```

---

## 3. Per-Project Folder Structure Analysis (17 Projects)

### 3.1 Banking — Full-Stack Fintech Application

| Attribute | Value |
|-----------|-------|
| **Stack** | Next.js 16 + Drizzle ORM + Plaid + Dwolla |
| **Type** | Full-Stack Fintech |
| **Status** | Active |

```
projects/Banking/
├── .claude/skills/           # Agent skills for Claude Code
├── .cursor/                  # Cursor IDE rules, agents, hooks, plans
├── .envs/
│   ├── local/                # Local environment variables
│   └── production/           # Production environment variables
├── .github/workflows/        # CI/CD pipelines
├── .husky/                   # Git hooks
├── .vercel/                  # Vercel deployment config
├── .vscode/                  # VS Code settings
├── bin/
│   ├── cleanup/              # Cleanup scripts
│   ├── deploy/               # Deployment scripts + compose
│   ├── docker/               # Docker utilities
│   ├── lib/                  # Shared bash libraries
│   ├── server/               # Server management scripts
│   └── utils/                # Utilities (AST, CI helpers)
├── compose/
│   ├── dev/                  # Docker Compose for development
│   ├── prod/                 # Docker Compose for production (Grafana, Prometheus)
│   └── traefik/              # Traefik reverse proxy config
├── database/
│   └── drizzle/              # Drizzle ORM migrations
├── docs/                     # Project documentation
│   ├── Project_Architecture/ # Architecture blueprints
│   ├── mcp/                  # MCP server docs
│   ├── nextjs/               # Next.js reference
│   ├── patterns/             # Architecture patterns
│   ├── plaid/                # Plaid API docs
│   ├── plans/                # Implementation plans
│   ├── sections/             # Section docs
│   ├── services/             # Service docs
│   └── specs/                # Specifications
├── node_modules/
├── public/icons/             # Static assets / icons
└── scripts/
    ├── codemod/              # Code transformation scripts
    ├── db/                   # Database scripts
    ├── generate/             # Code generation scripts
    └── maintenance/          # Maintenance scripts
```

**Naming Conventions:** PascalCase for files (Next.js convention), kebab-case for directories, underscore-prefixed for `.envs`, `compose/` subdirs mirror environment names.

---

### 3.2 Bash — Automation Toolkit

| Attribute | Value |
|-----------|-------|
| **Stack** | Bun / TypeScript |
| **Type** | Automation Toolkit |
| **Status** | Active |

```
projects/Bash/
├── .github/workflows/
├── .husky/
├── .vscode/
├── archive/
│   ├── artifacts/context-maps/   # Archived context maps
│   └── skills-commit-batches/    # Batch commit artifacts
├── Banking/                      # Banking-related Bash scripts
│   ├── install/
│   ├── install/lib/
│   └── scripts/
├── comicwise/                    # Comicwise-related Bash scripts
├── docs/Project_Architecture/    # Architecture docs
├── ecom/                         # Ecom-related Bash scripts
├── edits/                        # Edit scripts
├── lib/                          # Shared Bash libraries
├── migrations/                   # Migration scripts
│   ├── banking/
│   ├── comicwise/
│   ├── ecom/
│   ├── rhixe_scans/
│   └── root/
├── rhixe_scans/                  # rhixe_scans-related scripts
├── root/                         # Root-level scripts
├── scripts/                      # Main scripts directory
│   ├── BATCH_LOGS/               # Batch processing logs
│   ├── config/                   # Script configurations
│   └── lib/                      # Script libraries (core, data, domain)
├── src/                          # TypeScript source code
│   ├── core/                     # Core automation logic
│   ├── lib/                      # Shared libraries
│   └── migration/                # Migration implementations
└── tests/                        # Test files
```

**Naming Conventions:** PascalCase for TypeScript source, kebab-case for directories, `BATCH_LOGS/` uses UPPER_CASE for output/log directories.

---

### 3.3 comicwise — Comic Streaming Platform

| Attribute | Value |
|-----------|-------|
| **Stack** | Next.js 16 + Prisma/Drizzle + Stripe |
| **Type** | Full-Stack Content Streaming |
| **Status** | Active |

```
projects/comicwise/
├── .github/
│   ├── copilot/                  # Copilot intents
│   ├── ISSUE_TEMPLATE/
│   ├── plugin/                   # GitHub plugins
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
├── .husky/
├── .schemas/                     # JSON schemas
├── .vscode/
├── docs/Project_Architecture/
├── public/uploads/               # User-uploaded content
├── src/
│   ├── actions/                  # Server actions
│   │   └── admin/                # Admin actions
│   ├── app/                      # Next.js App Router
│   │   ├── (auth)/               # Auth-route group
│   │   ├── (root)/               # Root-route group
│   │   ├── admin/                # Admin pages
│   │   └── api/                  # API routes
│   ├── assets/svg/               # SVG assets
│   ├── backuptests/              # Legacy backups of tests
│   │   ├── e2e/
│   │   └── unit/
│   ├── components/               # React components
│   │   ├── activity/
│   │   ├── admin/
│   │   ├── analytics/
│   │   ├── auth/
│   │   ├── bookmarks/
│   │   ├── browse/
│   │   ├── comics/
│   │   ├── comments/
│   │   ├── feed/
│   │   ├── genres/
│   │   ├── home/
│   │   ├── layout/              # Layout components
│   │   ├── notifications/
│   │   ├── profile/
│   │   ├── ratings/
│   │   ├── reading/
│   │   ├── reading-progress/
│   │   ├── recommendations/
│   │   ├── search/
│   │   ├── settings/
│   │   ├── theme/
│   │   ├── ui/                  # Generic UI primitives
│   │   └── users/
│   ├── dal/                     # Data access layer
│   ├── data/                    # Static/data files
│   ├── database/drizzle/        # Drizzle migrations
│   ├── hooks/                   # React hooks
│   ├── lib/                     # Shared libraries
│   ├── schemas/                 # Zod / validation schemas
│   │   └── seed/               # Seed data schemas
│   ├── scripts/                 # Build/utility scripts
│   │   ├── seed/               # Database seeding
│   │   └── shared/             # Shared scripts
│   ├── storages/                # Storage abstractions
│   ├── stores/                  # State management (Zustand)
│   ├── styles/                  # CSS/SCSS styles
│   │   └── fonts/              # Font files
│   ├── tests/                   # Test files
│   │   ├── e2e/
│   │   └── unit/
│   └── types/                   # TypeScript type definitions
```

**Naming Conventions:** Next.js App Router convention (kebab-case route groups `(auth)`, `(root)`). Components organized by feature domain. Strong separation: `components/` by domain, `app/` by route. PascalCase for React components, kebab-case for directories.

---

### 3.4 cookiecutter-django-tailwind — Django Project Generator

| Attribute | Value |
|-----------|-------|
| **Stack** | Django 5.x + Tailwind CSS |
| **Type** | Project Generator / Cookiecutter Template |
| **Status** | Active |

```
projects/cookiecutter-django-tailwind/
├── .github/ISSUE_TEMPLATE/
├── .github/workflows/
├── .vscode/
├── docs/_static/                 # Documentation static assets
├── hooks/                        # Cookiecutter hooks (pre/post generation)
├── scripts/                      # Utility scripts
├── tests/                        # Tests for the template itself
└── {{cookiecutter.project_slug}}/ # Cookiecutter template variables
    ├── .devcontainer/
    ├── .envs/.local/
    ├── .envs/.production/
    ├── .github/workflows/
    ├── compose/local/
    ├── compose/production/
    ├── config/settings/           # Django settings (split by env)
    ├── docs/                      # Generated project docs
    ├── locale/                    # Internationalization
    │   ├── en_US/
    │   ├── fr_FR/
    │   └── pt_BR/
    ├── requirements/              # Split requirements files
    ├── tests/                     # Generated tests
    ├── utility/                   # Utility scripts
    ├── webpack/                   # Webpack configuration
    └── {{cookiecutter.project_slug}}/  # Django project package
        ├── contrib/               # Django contrib apps
        ├── static/                # Static files
        ├── templates/             # Django templates
        └── users/                 # User app
```

**Naming Conventions:** Cookiecutter variable syntax `{{cookiecutter.xxx}}` for template substitution. Standard Django project layout with `config/settings/`, `compose/`, and split `requirements/`.

---

### 3.5 Django-Scrapy-Selenium — Web Scraping Platform

| Attribute | Value |
|-----------|-------|
| **Stack** | Django 4.x + Scrapy + Selenium + Celery |
| **Type** | Web Scraping Platform |
| **Status** | Active |

```
projects/Django-Scrapy-Selenium/
├── .devcontainer/
├── .do/                          # DigitalOcean config
├── .envs/.local/
├── .github/workflows/
├── .vscode/
├── api/                          # Django API apps
│   ├── apps/                     # Custom Django apps
│   │   ├── migrations/
│   │   ├── scripts/
│   │   ├── templatetags/
│   │   ├── urls/
│   │   └── views/
│   ├── contrib/sites/            # Sites contrib
│   ├── home/                     # Home app
│   ├── src/sass/                 # SCSS source
│   ├── src/types/                # TypeScript types
│   ├── static/ckeditor/          # CKEditor files
│   ├── static/fonts/
│   ├── static/images/
│   ├── static/img/
│   ├── static/js/
│   ├── templates/                # Django templates
│   │   ├── account/              # allauth templates
│   │   ├── bookmark/
│   │   ├── chapters/
│   │   ├── comics/
│   │   ├── home/
│   │   ├── partials/             # Partial templates
│   │   └── users/
│   └── users/                    # User management app
├── compose/
│   ├── local/                    # Local Docker (django, docs, node)
│   └── production/               # Production Docker (aws, django, postgres, traefik)
├── config/settings/              # Django settings
├── crawler/                      # Scrapy crawler
│   ├── management/commands/      # Django management commands
│   ├── middlewares/               # Scrapy middlewares
│   ├── pipelines/                # Scrapy pipelines
│   │   ├── images/               # Image processing
│   │   └── redis/                # Redis-backed pipelines
│   └── spiders/                  # Scrapy spiders
├── docs/Project_Architecture/
├── fixtures/                     # Test/data fixtures
├── locale/                       # Internationalization
│   ├── en/LC_MESSAGES/
│   ├── fr/LC_MESSAGES/
│   ├── ja/LC_MESSAGES/
│   └── pt/LC_MESSAGES/
├── requirements/                 # Split requirements
├── tests/                        # Test suite
└── webpack/                      # Webpack config
```

**Naming Conventions:** Django standard layout (apps under `api/`), Scrapy standard layout (`crawler/spiders/`, `crawler/pipelines/`). Templates organized by Django app name. Composes split by environment.

---

### 3.6 docs — Documentation-Only Project

| Attribute | Value |
|-----------|-------|
| **Stack** | Markdown |
| **Type** | Documentation-Only Project |
| **Status** | Reference / Read-Only |

```
projects/docs/
├── .github/workflows/
├── .vscode/
└── docs/Project_Architecture/
    └── projects/                # Per-project architecture docs
```

**Naming Conventions:** Mirrors workspace `docs/` but at project level for cross-referencing.

---

### 3.7 ecom — Ecommerce Platform

| Attribute | Value |
|-----------|-------|
| **Stack** | Django REST Framework + React/Redux |
| **Type** | Full-Stack Ecommerce |
| **Status** | Active |

```
projects/ecom/
├── .github/workflows/
├── .vscode/
├── base/                        # Django base app
│   ├── migrations/
│   ├── urls/
│   └── views/
├── docs/Project_Architecture/
├── ecom/                        # Django project config
├── frontend/                    # React/Redux frontend
│   ├── public/                  # Static public assets
│   └── src/
│       ├── actions/             # Redux actions
│       ├── components/          # React components
│       ├── constants/           # Constants
│       ├── reducers/            # Redux reducers
│       └── screens/             # Page-level components
└── resources/
    └── images/                  # Image resources
```

**Naming Conventions:** Django backend (`base/` for app, `ecom/` for project). React frontend uses Redux convention (`actions/`, `reducers/`, `constants/`). `screens/` maps to pages, `components/` for reusable pieces.

---

### 3.8 mcp-servers — Multi-Language MCP Server Collection

| Attribute | Value |
|-----------|-------|
| **Stack** | 10 languages (TypeScript, Python, Go, Rust, Java, Kotlin, C#, PHP, Ruby, Swift) |
| **Type** | Multi-Language MCP Server Collection |
| **Status** | Active |

```
projects/mcp-servers/
├── .github/workflows/
├── .vscode/
├── copilot-studio/              # Copilot Studio integration
│   ├── .vscode/
│   ├── dist/tools/
│   └── tools/
├── csharp/                      # C# .NET MCP server
│   └── Tools/
├── go/                          # Go MCP server
│   ├── config/
│   └── tools/
├── java/                        # Java MCP server
│   ├── .mvn/wrapper/
│   └── src/main/
├── kotlin/                      # Kotlin MCP server
│   └── src/main/
├── php/                         # PHP MCP server
│   └── src/Tools/
├── python/                      # Python MCP server
│   └── .venv/
├── ruby/                        # Ruby MCP server
│   ├── bin/
│   ├── lib/my_mcp_server/
│   └── test/tools/
├── rust/                        # Rust MCP server
│   └── src/tools/
├── swift/                       # Swift MCP server
│   └── Sources/MyMCPServer/
└── typescript/                  # TypeScript MCP server
    ├── dist/tools/
    └── src/tools/
```

**Naming Conventions:** Each language gets its own directory. Source code follows each language's standard conventions (e.g., `src/` for Rust/Kotlin/Java, `lib/` for Ruby, `Tools/` for C#). `tools/` contains each server's exposed tool implementations.

---

### 3.9 profile — Django Profile/Portfolio Site

| Attribute | Value |
|-----------|-------|
| **Stack** | Django |
| **Type** | Profile/Portfolio Application |
| **Status** | Active |

```
projects/profile/
├── .github/workflows/
├── .vscode/
├── base/                        # Base Django app
│   ├── migrations/
│   ├── static/                  # Static assets (admin, ckeditor, css, images, js)
│   └── templates/
├── rhixecompany/                # Company app
│   └── migrations/
├── static/                      # Project-level static assets
│   ├── admin/
│   ├── ckeditor/
│   ├── css/
│   ├── images/
│   │   ├── images/
│   │   └── uploads/
│   └── js/
├── templates/
│   └── base/                    # Base templates
└── ... (manage.py, etc.)
```

**Naming Conventions:** Standard Django project layout. `static/` mirrors Django's static file discovery. App-level `static/` and project-level `static/` follow Django's `STATICFILES_DIRS` pattern.

---

### 3.10 Python-projects — 18 Beginner Scripts

| Attribute | Value |
|-----------|-------|
| **Stack** | Python 3.x |
| **Type** | Script Collection (Educational/Utility) |
| **Status** | Active |

```
projects/Python-projects/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
├── .vscode/
├── docs/
├── automate_morning_text.py
├── basic_calculator.py
├── binary_search_algorithm.py
├── currency_converter.py
├── dice_rolling_simulator.py
├── email_sender.py
├── email_slicer.py
├── graph_plotter.py
├── image_resizer.py
├── interest_payment_calculator.py
├── leap_year_checker.py
├── python_face_detection.py
├── qr_code_generator.py
├── quiz_program.py
├── random_password_generator.py
├── rock_paper_scissors.py
├── site_connectivity_checker.py
├── word_dictionary.py
└── word_replacement.py
```

**Naming Conventions:** Snake case for Python script files. Flat structure (no subdirectories) — each script is standalone.

---

### 3.11 Resume_maker — Job Documents Generator

| Attribute | Value |
|-----------|-------|
| **Stack** | Bun / TypeScript |
| **Type** | CLI Document Generator |
| **Status** | Active |

```
projects/Resume_maker/
├── .github/workflows/
├── .vscode/
├── application_materials/       # Generated application materials
├── docs/Project_Architecture/
│   └── projects/
├── output/                      # Output directory for generated docs
├── scripts/                     # Utility scripts
├── updated_readmes/             # Updated README versions
├── *.json                       # Input files (alexander-input.json, etc.)
└── ...
```

**Naming Conventions:** Snake case for JSON input files, kebab-case for directories. Scripts in `scripts/`, outputs in `output/`.

---

### 3.12 rhixe_scans — Comic/Manga Reader Platform

| Attribute | Value |
|-----------|-------|
| **Stack** | Next.js 15 + Prisma 6 |
| **Type** | Full-Stack Comic Reader |
| **Status** | Active |

```
projects/rhixe_scans/
├── .devcontainer/
├── .github/workflows/
├── .vscode/
├── backend/                     # Django/DRF backend
│   ├── api/
│   │   ├── contrib/
│   │   ├── home/
│   │   ├── libary/
│   │   ├── templates/
│   │   └── users/
│   ├── config/settings/
│   ├── crawler/                 # Scrapy spiders
│   │   ├── handlers/
│   │   ├── management/
│   │   ├── middlewares/
│   │   └── pipelines/
│   ├── downloader/              # Download management
│   ├── fixtures/
│   └── locale/                  # i18n
│       ├── en/
│       ├── fr/
│       ├── ja/
│       └── pt/
├── bash/                        # Bash automation
├── compose/production/          # Docker Compose (multi-service)
├── docs/Project_Architecture/
├── requirements/                # Split requirements
├── src/                         # Next.js frontend
│   ├── app/
│   │   ├── (auth)/
│   │   ├── (root)/
│   │   ├── admin/
│   │   ├── api/
│   │   └── dashboard/
│   ├── assets/styles/
│   ├── components/
│   │   ├── admin/
│   │   ├── auth/
│   │   ├── shared/
│   │   └── ui/
│   ├── db/migrations/           # Database migrations (frontend)
│   ├── hooks/
│   ├── lib/
│   │   ├── actions/
│   │   ├── constants/
│   │   └── data/
│   └── types/
└── tests/
```

**Naming Conventions:** Dual-stack architecture — `backend/` (Django) and `src/` (Next.js). Django follows standard patterns; Next.js uses App Router. Locale directories use ISO language codes.

---

### 3.13 rhixecompany-comics — Dual-Stack Comics Platform

| Attribute | Value |
|-----------|-------|
| **Stack** | Django 4.x + Next.js 16 + Celery |
| **Type** | Dual-Stack Web Application |
| **Status** | Active |

```
projects/rhixecompany-comics/
├── .github/workflows/
├── .logs/                       # Application logs
├── .vscode/
├── backend/                     # Django REST Framework backend
│   ├── .venv/                   # Python virtual environment
│   ├── apps/
│   │   ├── api/                 # API app
│   │   ├── comics/              # Comics domain
│   │   ├── core/                # Core functionality
│   │   ├── scraping/            # Scraping service
│   │   └── users/               # User management
│   └── config/                  # Django settings
├── docs/Project_Architecture/
├── frontend/                    # Next.js 16 frontend
│   └── src/
│       ├── app/                 # Next.js App Router
│       ├── components/          # React components
│       ├── database/            # Drizzle schema
│       ├── lib/                 # Utilities
│       ├── scripts/             # Build/utility scripts
│       ├── storages/            # Storage layer
│       └── styles/              # CSS/Tailwind
└── scripts/
    └── scraper/                 # Scraper automation scripts
```

**Naming Conventions:** Clear `backend/` / `frontend/` split. Django apps grouped by domain under `apps/`. Next.js uses standard App Router.

---

### 3.14 selenium_webdriver — Chrome Web Scraper

| Attribute | Value |
|-----------|-------|
| **Stack** | Node.js 18+ + Selenium WebDriver 4.x |
| **Type** | CLI Scraper Tool |
| **Status** | Active |

```
projects/selenium_webdriver/
├── .github/workflows/
├── .vscode/
├── docs/
│   ├── code-docs/
│   └── Project_Architecture/
└── src/                         # Source code
```

**Naming Conventions:** Single `src/` directory, flat structure. Minimal.

---

### 3.15 university-libary-jsm — Library Management System

| Attribute | Value |
|-----------|-------|
| **Stack** | Next.js 15 + Drizzle ORM + Neon |
| **Type** | Full-Stack Library Management |
| **Status** | Active |

```
projects/university-libary-jsm/
├── .github/workflows/
├── .vscode/
├── app/                         # Next.js App Router (file-based routing)
│   ├── (auth)/sign-in/          # Auth route group
│   ├── (auth)/sign-up/
│   ├── (root)/books/            # Books pages
│   ├── (root)/library/
│   ├── (root)/my-profile/
│   ├── admin/                   # Admin panel
│   │   ├── account-requests/
│   │   ├── book-requests/
│   │   ├── books/
│   │   └── users/
│   ├── api/                     # API routes
│   │   ├── auth/
│   │   ├── imagekit/
│   │   └── workflows/
│   ├── fonts/                   # Font assets
│   ├── too-fast/                # Rate-limit page
│   └── unauthorized/
├── assets/                      # Project assets
├── components/                  # React components
│   ├── admin/
│   │   ├── books/
│   │   └── forms/
│   └── ui/                      # UI primitives (shadcn/ui)
├── constants/                   # App constants
├── database/                    # Drizzle schema
├── docs/
├── emails/                      # Email templates (react-email)
├── hooks/                       # React hooks
├── lib/                         # Shared libraries
│   ├── actions/                 # Server actions
│   ├── admin/                   # Admin utilities
│   └── queries/                 # Database queries
├── migrations/                  # Drizzle migrations
│   └── meta/
├── public/icons/                # Static icons
│   └── admin/
├── public/images/               # Static images
└── styles/                      # Global styles
```

**Naming Conventions:** Next.js App Router with route groups `(auth)`, `(root)`. Components under `components/admin/` sub-divided by feature. `lib/actions/` for server actions, `lib/queries/` for DB queries.

---

### 3.16 xamehi.tv — Streaming Platform

| Attribute | Value |
|-----------|-------|
| **Stack** | Django REST + React 17 |
| **Type** | Full-Stack Streaming Platform |
| **Status** | Active |

```
projects/xamehi.tv/
├── .github/workflows/
├── .vscode/
├── docs/Project_Architecture/
├── frontend/                    # React 17 frontend
│   ├── public/static/
│   └── src/
│       ├── actions/             # Redux actions
│       ├── components/          # React components
│       ├── constants/           # Constants
│       ├── reducers/            # Redux reducers
│       └── screens/             # Page-level components
├── player/                      # Video player module
├── static/                      # Django static files
│   └── admin/
├── video/                       # Django video app
│   ├── migrations/
│   ├── urls/
│   └── views/
└── ... (manage.py, etc.)
```

**Naming Conventions:** `frontend/` follows React/Redux pattern. Django backend organized by app (`video/`, `player/`). `static/` follows Django discovery.

---

### 3.17 xamehi — Triple-Service Web Application

| Attribute | Value |
|-----------|-------|
| **Stack** | Django + Express + React 18 |
| **Type** | Triple-Service Web Application |
| **Status** | Legacy / Active |

```
projects/xamehi/
├── .github/workflows/
├── .vscode/
├── docs/
├── public/                      # Express/React public assets
├── src/components/              # React 18 components
└── xamehi/                      # Django project
```

**Naming Conventions:** Minimal structure — `xamehi/` is Django project, `src/` is React frontend, `public/` is Express static.

---

### 3.18 youtube-downloader — CLI Video Downloader

| Attribute | Value |
|-----------|-------|
| **Stack** | Python 3.x + yt-dlp |
| **Type** | CLI Utility Tool |
| **Status** | Active |

```
projects/youtube-downloader/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
├── .vscode/
├── docs/
├── requirements/
├── main_loop_noplaylist.py
├── main_loop_playlist.py
├── main_noplaylist.py
├── main_playlist.py
├── test.py
```

**Naming Conventions:** Snake case for Python scripts. Flat structure. Descriptive filename suffixes: `_noplaylist`, `_playlist`, `_loop`.

---

## 4. File Placement Patterns

### 4.1 Configuration Files

| Pattern | Location | Examples |
|---------|----------|----------|
| Root workspace config | `SandBox/` root | `.editorconfig`, `.gitignore`, `.mcp.json`, `.ruff.toml` |
| Root tooling config | `SandBox/` | `pyrightconfig.json`, `tsconfig.json`, `bun.lock`, `package.json` |
| Project-level config | `projects/<project>/` | `package.json`, `tsconfig.json`, `pyproject.toml` |
| Environment variables | `projects/<project>/.envs/` | `.envs/local/`, `.envs/production/` |
| VS Code | `<project>/.vscode/` | `settings.json`, `extensions.json` |
| Agent config | `<project>/.claude/`, `<project>/.cursor/` | Skills, rules, hooks |
| CI/CD | `<project>/.github/workflows/` | YAML workflow files |
| MCP | `SandBox/.mcp.json`, `<project>/docs/mcp/` | MCP server registrations |
| Docker Compose | `<project>/compose/` | `docker-compose.yml`, `compose/local/`, `compose/production/` |

### 4.2 Source Code / Business Logic

| Pattern | Location | 
|---------|----------|
| Next.js pages/routes | `<project>/src/app/` or `<project>/app/` |
| React components | `<project>/src/components/` (sub-divided by domain) |
| Server actions | `<project>/src/lib/actions/` or `<project>/src/actions/` |
| Django apps | `<project>/<appname>/` or `<project>/api/<appname>/` |
| Scrapy spiders | `<project>/crawler/spiders/` |
| MCP server tools | `<project>/src/tools/` or `<project>/Tools/` |
| Shared libraries | `<project>/src/lib/` or `<project>/lib/` |
| TypeScript types | `<project>/src/types/` or `<project>/types/` |
| Validation schemas | `<project>/src/schemas/` |

### 4.3 Database

| Pattern | Location |
|---------|----------|
| ORM schemas | `<project>/database/` or `<project>/src/database/` |
| Migrations | `<project>/database/drizzle/` or `<project>/src/db/migrations/` |
| Fixtures | `<project>/fixtures/` |
| Seed data | `<project>/src/schemas/seed/` or `<project>/src/scripts/seed/` |

### 4.4 Styles and Assets

| Pattern | Location |
|---------|----------|
| Global styles | `<project>/src/styles/` or `<project>/styles/` |
| UI primitives | `<project>/src/components/ui/` |
| Static files | `<project>/static/` or `<project>/public/` |
| Images/icons | `<project>/public/images/`, `<project>/public/icons/` |
| Fonts | `<project>/src/styles/fonts/` or `<project>/app/fonts/` |

### 4.5 Tests

| Pattern | Location |
|---------|----------|
| Unit tests | `<project>/src/tests/unit/` or `<project>/tests/` |
| E2E tests | `<project>/src/tests/e2e/` |
| Fixtures | `<project>/fixtures/` |

### 4.6 Documentation

| Pattern | Location |
|---------|----------|
| Project README | `<project>/README.md` |
| Story of the repo | `<project>/THE_STORY_OF_THIS_REPO.md` |
| Repository summary | `<project>/REPOSITORY_SUMMARY.md` |
| Architecture blueprints | `<project>/docs/Project_Architecture/` |
| API references | `<project>/API_REFERENCE.md` |
| Setup guides | `<project>/SETUP_GUIDE.md` |
| Stack docs | `<project>/technology-stack.md` |

---

## 5. Naming and Organization Conventions

### 5.1 File Naming Patterns

| Convention | Used In | Examples |
|-----------|---------|----------|
| **snake_case** | Python scripts, data files | `main_loop_playlist.py`, `automate_morning_text.py` |
| **PascalCase** | Next.js components, React files, some TypeScript | React components, Next.js page files |
| **kebab-case** | Directories, route groups, utility dirs | `compose/local/`, `cookiecutter-django-tailwind/` |
| **UPPER_CASE** | Log/output dirs, constants | `BATCH_LOGS/`, `CONTRIBUTORS.txt` |
| **dot-prefixed** | Config directories | `.github/`, `.vscode/`, `.envs/`, `.husky/` |

### 5.2 Directory Naming Conventions

| Pattern | Usage |
|---------|-------|
| `<project-name>/` | Root project directory (hyphenated, e.g., `cookiecutter-django-tailwind/`) |
| `src/` | Primary source code directory (Next.js, TypeScript, Rust, Java projects) |
| `app/` | Next.js App Router directory |
| `api/` | Django API apps or Next.js API routes |
| `compose/` | Docker Compose configurations |
| `config/` | Framework configuration (Django settings) |
| `docs/` | Documentation |
| `lib/` | Shared/shared libraries |
| `public/` | Static assets |
| `scripts/` | Utility/build scripts |
| `tests/` | Test suites |
| `(auth)/`, `(root)/` | Next.js route groups (parenthesized) |

### 5.3 Organizational Patterns

| Pattern | Description | Examples |
|---------|-------------|---------|
| **By Feature** | Components grouped by domain | `components/comics/`, `components/auth/`, `components/feed/` (comicwise) |
| **By Layer** | Code split by architectural layer | `actions/`, `reducers/`, `components/`, `screens/` (Redux pattern) |
| **By Environment** | Config split by deployment env | `compose/local/`, `compose/production/`, `.envs/local/` |
| **By Language** | Multi-language projects | `mcp-servers/csharp/`, `mcp-servers/go/`, `mcp-servers/python/` |
| **By Service** | Backend/frontend separation | `backend/` + `frontend/` (rhixecompany-comics, rhixe_scans) |
| **Route Groups** | Next.js App Router collocation | `app/(auth)/`, `app/(root)/`, `app/admin/`, `app/api/` |

---

## 6. Technology-Specific Structure Patterns

### 6.1 Next.js Projects (Banking, comicwise, rhixe_scans, university-libary-jsm)

```
├── app/                    # App Router
│   ├── (auth)/             # Route groups
│   ├── (root)/
│   ├── admin/
│   └── api/                # API route handlers
├── components/             # React components
│   └── ui/                 # Shadcn/ui primitives
├── lib/
│   └── actions/            # Server Actions
├── database/               # ORM (Drizzle/Prisma)
├── hooks/                  # React hooks
├── public/                 # Static assets
└── styles/                 # Global CSS/Tailwind
```

### 6.2 Django Projects (Django-Scrapy-Selenium, ecom, profile, xamehi.tv, xamehi)

```
├── api/                    # Django apps
│   ├── <app>/
│   │   ├── migrations/
│   │   ├── templates/
│   │   └── views/
├── config/settings/        # Split settings
├── compose/                # Docker
├── locale/                 # i18n
├── requirements/           # Pip requirements
├── static/                 # Static files
└── templates/              # Project templates
```

### 6.3 MCP Server Projects (mcp-servers/*)

Each language directory follows its ecosystem's standard:
- **TypeScript/Python/Go/Rust:** `src/` + `dist/`
- **Java/Kotlin:** `src/main/` + Maven wrapper
- **C#:** `Tools/` directory
- **Ruby:** `lib/` + `bin/` + `test/`
- **PHP:** `src/Tools/`
- **Swift:** `Sources/MyMCPServer/`

---

## 7. Build and Output Organization

| Artifact | Location | Notes |
|----------|----------|-------|
| Node modules | `<project>/node_modules/` | Excluded from version control |
| Python venv | `<project>/.venv/` | Per-project virtual environment |
| Compiled output | `<project>/dist/` | TypeScript, MCP servers |
| Ruff cache | `<project>/.ruff_cache/` | Python linter cache |
| Judge results | `SandBox/judge_results/` | Workspace-level QA reports |
| Reports | `SandBox/results/` | Benchmark/analysis output |

---

## 8. Extension Points and Evolution

### How to Add a New Project

1. Create directory `projects/<new-project>/`
2. Include standard files: `README.md`, `THE_STORY_OF_THIS_REPO.md`, `.gitignore`
3. Add `.github/workflows/` for CI if needed
4. Document structure under `docs/Project_Architecture/`
5. Follow technology-specific conventions from Section 6

### Adding a New Feature to an Existing Project

- **Next.js:** Add route under `app/`, components under `components/<domain>/`, actions under `lib/actions/`
- **Django:** Create/update app under `api/`, add URL patterns and views
- **Python CLI:** Add script at project root with snake_case filename

### Cross-Cutting Changes

- **Root automation:** Add scripts to `SandBox/scripts/` or `projects/Bash/`
- **Agent prompts:** Add/update files in `SandBox/.github/prompts/`
- **Shared config:** Update root `.editorconfig`, `.gitignore`, `.mcp.json`

---

## 9. Structure Templates

### New Next.js Feature

```
src/
├── app/<feature>/
│   └── page.tsx
├── components/<feature>/
│   ├── <Feature>List.tsx
│   └── <Feature>Card.tsx
├── lib/
│   └── actions/
│       └── <feature>.ts
└── types/
    └── <feature>.ts
```

### New Django App

```
<app_name>/
├── migrations/
├── templates/<app_name>/
├── templatetags/
├── admin.py
├── models.py
├── urls.py
└── views.py
```

### New MCP Tool (TypeScript)

```
src/tools/
├── <tool-name>.ts
└── index.ts
```

---

## 10. Structure Enforcement

### Current Enforcement Mechanisms

| Mechanism | Scope | Description |
|-----------|-------|-------------|
| `.editorconfig` | Workspace root | Coding style consistency |
| `.gitignore` | Workspace root | Prevents generated files from being committed |
| ESLint/Ruff | Per-project | Linting enforces code patterns |
| Prettier | Per-project | Code formatting |
| GitHub Actions | Per-project `.github/workflows/` | CI enforces quality gates |
| Pyright | Workspace root | Python type checking |
| Hermes prompts | `.github/prompts/` | Agent instruction templates enforce conventions |

### Maintenance

This blueprint should be updated when:
- A new project is added to `projects/`
- An existing project undergoes significant restructuring
- Cross-cutting naming conventions change
- New technology stacks are introduced

---

*Generated 2026-07-28 for the SandBox workspace (17 projects under `projects/`).*
