# Project Folder Structure Blueprint

## Project: rhixe_scans — Scans Project (Django + Next.js Hybrid)

**Generated:** 2026-06-25  
**Project Type:** Django Python (Backend) + Next.js (Frontend) + Scrapy (Crawler)  
**Auto-detected:** Yes (Django — `backend/manage.py`; Next.js — `next.config.ts`, `package.json`, `src/`; Scrapy — `backend/crawler/`)

---

## Directory Tree

```
rhixe_scans/
├── .devcontainer/
├── .envs/
│   ├── .local/
│   └── .production/
├── .github/
│   └── workflows/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CONTRIBUTORS.txt
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── LICENSE
├── Makefile
├── Procfile
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── backend/                   # Django backend
│   ├── api/                   # Django API apps
│   │   ├── contrib/
│   │   ├── home/
│   │   ├── libary/
│   │   ├── templates/
│   │   └── users/
│   ├── config/                # Django settings
│   │   └── settings/
│   ├── crawler/               # Scrapy crawler
│   │   └── handlers/
│   ├── downloader/
│   ├── fixtures/
│   ├── locale/
│   ├── manage.py
│   ├── superbase.py
│   ├── api.sqlite3
│   ├── *.json                 # Seed data (comic, chapter, author, etc.)
│   └── logs.txt
├── bash/
├── bin/
├── bun.lock
├── code-exemplars.md
├── components.json            # shadcn/ui components
├── compose/
├── copilot-instructions.md
├── cross-linking-report.md
├── docker-compose.docs.yml
├── docker-compose.local.yml
├── docker-compose.production.yml
├── docs/
│   ├── conf.py
│   ├── __init__.py
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── jest.config.ts / jest.setup.ts
├── merge_production_dotenvs_in_dotenv.py
├── next.config.ts             # Next.js config
├── package.json               # Next.js/Node dependencies
├── project-workflow.md
├── src/                       # Next.js App Router source
│   ├── auth.config.ts
│   ├── auth.ts
│   └── middleware.ts
├── tailwind.config.ts
├── technology-stack.md
├── tests/
│   ├── paypal.test.ts
│   ├── test_*.py
│   └── __init__.py
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Django apps** | lowercase | `api/`, `home/`, `libary/`, `users/` |
| **Next.js source** | kebab-case | `src/auth.config.ts`, `tailwind.config.ts` |
| **Docker compose** | docker-compose.<env>.yml | `docker-compose.local.yml` |
| **Seed data** | lowercase.json | `comic.json`, `chapter.json`, `author.json` |
| **Tests** | test_*.py / *.test.ts | `test_selenium.py`, `paypal.test.ts` |

---

## File Placement Patterns

- **Django backend**: `backend/` with `api/`, `config/`, `crawler/`
- **Next.js frontend**: Root-level `src/`, `next.config.ts`, `package.json`
- **Scrapy crawler**: `backend/crawler/`
- **Seed data**: `backend/*.json` files
- **Tests**: `tests/`
- **Docker**: Multiple compose files

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `backend/manage.py` | ✅ Django project |
| Has `next.config.ts` | ✅ Next.js frontend |
| Has `backend/crawler/` | ✅ Scrapy crawler |
| Has `.devcontainer/` | ✅ VS Code dev container |
| Has `components.json` | ✅ shadcn/ui |
| Has Jest config | ✅ Jest testing |
| Has Tailwind config | ✅ Tailwind CSS |
| Multi-test types | ✅ Python tests + TypeScript tests |

---

## Key Architecture Decisions

1. **Hybrid architecture** — Django REST backend for data/API + Next.js frontend for UI.
2. **Scrapy crawler** for web scraping comics data.
3. **Large seed data** — Extensive JSON data files for comics, chapters, authors, artists.
4. **Multi-language tests** — Both Python (pytest) and TypeScript (Jest) test suites.
5. **Comprehensive environment config** — Local and production env files.
