# Project Folder Structure Blueprint

## Project: Django-Scrapy-Selenium — Django + Scrapy + Selenium

**Generated:** 2026-06-25  
**Project Type:** Django Python + Scrapy + Selenium Web Scraping  
**Auto-detected:** Yes (Django — `manage.py`, `config/`, `api/`; Scrapy — `crawler/`)

---

## Directory Tree

```
Django-Scrapy-Selenium/
├── .devcontainer/
├── .do/
├── .envs/
│   └── .local/
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
├── api/                     # Django REST API
│   ├── apps/                # Django applications
│   │   ├── migrations/
│   │   ├── scripts/
│   │   ├── templatetags/
│   │   ├── urls/
│   │   └── views/
│   ├── contrib/
│   │   └── sites/
│   │       └── migrations/
│   ├── home/
│   │   └── migrations/
│   ├── src/
│   │   ├── sass/
│   │   └── types/
│   └── static/
│       ├── ckeditor/
│       ├── fonts/
│       └── images/
├── api.sqlite3
├── chapters.json
├── code-exemplars.md
├── comics.json
├── compose/
├── config/                   # Django project configuration
├── copilot-instructions.md
├── crawler/                  # Scrapy crawler
│   └── spiders/
├── cross-linking-report.md
├── docker-compose.docs.yml
├── docker-compose.local.yml
├── docker-compose.production.yml
├── docs/
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── locale/
├── manage.py
├── project-workflow.md
├── requirements/
├── technology-stack.md
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
| --- | --- | --- |
| **Django apps** | lowercase | `apps/`, `home/`, `contrib/` |
| **Docker compose files** | docker-compose.<env>.yml | `docker-compose.local.yml`, `docker-compose.production.yml` |
| **Config files** | dotted-prefix | `.devcontainer/`, `.envs/` |
| **Documentation** | UPPER_CASE.md | `README.md`, `CHANGELOG.md`, `CONTRIBUTORS.txt` |

---

## File Placement Patterns

- **Django API**: `api/` directory with apps, contrib, home, static
- **Web scraper**: `crawler/` with Scrapy spiders
- **Django project config**: `config/`
- **Docker Compose**: Multiple files for different environments
- **Python requirements**: `requirements/`

---

## Project Type Indicators

| Indicator | Value |
| --- | --- |
| Has `manage.py` | ✅ Django project |
| Has `crawler/` | ✅ Scrapy crawler |
| Has `api/` with Django apps | ✅ Django REST API |
| Has Docker Compose variants | ✅ Multi-environment Docker |
| Has `Procfile` | ✅ Heroku deployment |
| Has `Makefile` | ✅ Build automation |
| Has `locale/` | ✅ i18n support |

---

## Key Architecture Decisions

1. **Django REST API** as backend with multiple apps (apps, home, contrib/sites).
2. **Scrapy crawler** in `crawler/` directory for web scraping with Selenium integration.
3. **Multi-env Docker** — Separate compose files for local, production, and docs.
4. **Static files** with CKEditor integration for rich content.
5. **JSON data files** (`chapters.json`, `comics.json`) for seed/test data.
6. **Heroku-ready** with `Procfile` and `requirements/`.
