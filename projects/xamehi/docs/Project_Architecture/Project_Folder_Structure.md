# Project Folder Structure Blueprint

## Project: xamehi — Xamehi Project

**Generated:** 2026-06-25  
**Project Type:** Django Python + Node.js/React (Hybrid)  
**Auto-detected:** Yes (Django — `manage.py`; Node.js — `package.json`, `src/`, `public/`)

---

## Directory Tree

```
xamehi/
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
├── index.js                   # Node.js entry point
├── manage.py                  # Django management
├── package-lock.json
├── package.json
├── project-workflow.md
├── public/                    # Node.js/React public assets
├── src/                       # Node.js/React source
│   └── components/
├── technology-stack.md
├── validation-report.md
└── xamehi/                    # Django app
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Django app** | lowercase | `xamehi/` |
| **Node.js source** | kebab-case | `src/components/` |
| **Config** | dotted-prefix | `.github/`, `.vscode/` |
| **Documentation** | UPPER_CASE.md | `README.md`, `USER_GUIDE.md`, `DEVELOPER_GUIDE.md` |

---

## File Placement Patterns

- **Django source**: `xamehi/` app and root-level `manage.py`
- **Node.js/React source**: `src/`, `public/`, `index.js`
- **Documentation**: `docs/`

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `manage.py` | ✅ Django project |
| Has `package.json` + `index.js` | ✅ Node.js / React |
| Has `src/components/` | ✅ React components |
| Has user + developer guides | ✅ Comprehensive documentation |

---

## Key Architecture Decisions

1. **Hybrid Django + Node.js** — Django backend with a Node.js/React frontend.
2. **Minimal structure** — Django app `xamehi/` and React source in `src/`.
3. **Full documentation suite** — Includes user and developer guides.
4. **Node.js entry point** via `index.js`.
