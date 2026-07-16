# Project Folder Structure Blueprint

## Project: xamehi.tv — TV / Streaming Platform

**Generated:** 2026-06-25  
**Project Type:** Django Python + React Frontend (TV/Streaming)  
**Auto-detected:** Yes (Django — `manage.py`; React — `frontend/src/`)

---

## Directory Tree

```
xamehi.tv/
├── .github/
│   └── workflows/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPER_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── Procfile
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── USER_GUIDE.md
├── code-exemplars.md
├── copilot-instructions.md
├── cross-linking-report.md
├── docs/
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── frontend/                  # React frontend
│   ├── public/
│   │   └── static/
│   └── src/
│       ├── actions/
│       ├── components/
│       ├── constants/
│       ├── reducers/
│       └── screens/
├── gunicorn.service / gunicorn.socket
├── manage.py                  # Django management
├── player/                    # Video player module
├── project-workflow.md
├── requirements.txt
├── runtime.txt
├── static/                    # Django static files
│   └── admin/
└── technology-stack.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
| --- | --- | --- |
| **Django** | standard | `manage.py`, `player/`, `static/` |
| **React** | kebab-case | `frontend/src/actions/`, `frontend/src/screens/` |
| **Config** | dotted-prefix | `.github/`, `.vscode/` |
| **Systemd units** | lowercase.service | `gunicorn.service`, `gunicorn.socket` |
| **User/developer docs** | UPPER_CASE.md | `USER_GUIDE.md`, `DEVELOPER_GUIDE.md` |

---

## File Placement Patterns

- **Django backend**: `manage.py`, `player/`, `static/`
- **React frontend**: `frontend/` with Redux-style structure
- **Deployment**: `Procfile`, `gunicorn.service`, `gunicorn.socket`, `runtime.txt`
- **Player module**: `player/` for video playback logic

---

## Project Type Indicators

| Indicator | Value |
| --- | --- |
| Has `manage.py` | ✅ Django project |
| Has `frontend/src/` | ✅ React frontend |
| Has `player/` | ✅ Video player module |
| Has `Procfile` + `runtime.txt` | ✅ Heroku deployable |
| Has systemd service files | ✅ Linux production deployment |
| Has user guide | ✅ End-user documentation |

---

## Key Architecture Decisions

1. **Django backend** with a dedicated `player/` module for video/tv streaming.
2. **React frontend** with Redux-style architecture (actions, constants, reducers, screens).
3. **Gunicorn + systemd** for production Linux deployment.
4. **Heroku-ready** with `Procfile` and `runtime.txt`.
5. **Comprehensive docs** — Includes both developer and end-user guides.
