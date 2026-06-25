# Project Folder Structure Blueprint

## Project: rhixecompany-comics — Comics Project (Django + React)

**Generated:** 2026-06-25  
**Project Type:** Django Python (Backend) + React (Frontend)  
**Auto-detected:** Yes (Django — `backend/apps/`, `backend/config/`; React — `frontend/`)

---

## Directory Tree

```
rhixecompany-comics/
├── .github/
│   └── workflows/
├── .logs/
├── .vscode/
├── AGENTS.md
├── README.md
├── RESEARCH_REPORT.md
├── architecture.md
├── backend/                    # Django backend
│   ├── .venv/                  # Python virtual environment
│   ├── apps/                   # Django applications
│   │   ├── api/
│   │   ├── comics/
│   │   ├── core/
│   │   ├── scraping/
│   │   └── users/
│   ├── config/                 # Django project configuration
│   └── manage.py
├── code-exemplars.md
├── copilot-instructions.md
├── cross-linking-report.md
├── docker-compose.yml
├── docs/
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── frontend/                   # React frontend
│   ├── public/
│   └── src/
├── project-workflow.md
├── scripts/
├── technology-stack.md
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Django apps** | lowercase plural | `apps/comics/`, `apps/users/`, `apps/core/` |
| **Backend directories** | lowercase | `backend/config/`, `backend/apps/` |
| **Frontend directories** | lowercase | `frontend/src/`, `frontend/public/` |
| **Documentation** | kebab-case.md | `architecture.md`, `code-exemplars.md` |

---

## File Placement Patterns

- **Backend**: `backend/` with `apps/`, `config/`, `manage.py`
- **Frontend**: `frontend/` with `src/`, `public/`
- **Django apps**: `backend/apps/` with domain-focused apps (api, comics, core, scraping, users)
- **Scripts**: `scripts/`
- **Deployment**: `docker-compose.yml`

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `backend/manage.py` | ✅ Django project |
| Has `frontend/` | ✅ React frontend |
| Has Docker Compose | ✅ Docker deployment |
| Has `.venv` | ✅ Python virtual environment |
| Has domain-driven apps | ✅ comics, users, scraping, core, api |

---

## Key Architecture Decisions

1. **Domain-driven Django apps** — Separate apps for comics, users, scraping, core, and API.
2. **React frontend** in separate `frontend/` directory.
3. **Docker Compose** for containerized deployment.
4. **Scraping app** — Dedicated Django app for web scraping functionality.
5. **Virtual environment** bundled locally.
