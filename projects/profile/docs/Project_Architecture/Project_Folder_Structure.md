# Project Folder Structure Blueprint

## Project: profile — Django Profile Project

**Generated:** 2026-06-25  
**Project Type:** Django Python Web Application  
**Auto-detected:** Yes (Django — `manage.py`, `base/`, `rhixecompany/`, `static/`, `templates/`)

---

## Directory Tree

```
profile/
├── .github/
│   └── workflows/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── Procfile
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── base/                      # Django base app
│   ├── migrations/
│   ├── static/
│   │   ├── admin/
│   │   ├── ckeditor/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   └── templates/
├── code-exemplars.md
├── copilot-instructions.md
├── cross-linking-report.md
├── db.sqlite3
├── docs/
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── manage.py
├── migrate.yaml
├── project-workflow.md
├── requirements.txt
├── rhixecompany/              # Django app
│   ├── migrations/
│   └── templates/
├── static/                    # Static files
│   ├── admin/
│   ├── ckeditor/
│   ├── css/
│   ├── images/
│   └── js/
├── technology-stack.md
├── templates/                 # Django templates
│   └── base/
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Django apps** | lowercase | `base/`, `rhixecompany/` |
| **Django templates** | lowercase | `templates/base/` |
| **Static assets** | lowercase | `static/css/`, `static/js/`, `static/images/` |
| **Config/setup** | dotted-prefix | `.github/`, `.vscode/` |
| **Migration config** | kebab-case | `migrate.yaml` |

---

## File Placement Patterns

- **Django apps**: `base/` and `rhixecompany/` apps
- **Static files**: `static/` with standard Django layout (admin, ckeditor, css, images, js)
- **Templates**: `templates/`
- **Database**: `db.sqlite3` for development
- **Deployment**: `Procfile` for Heroku

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `manage.py` | ✅ Django project |
| Has `static/` with Django admin | ✅ Standard Django static layout |
| Has `templates/` | ✅ Django templates |
| Has CKEditor | ✅ Rich text editor integration |
| Has `Procfile` | ✅ Heroku deployable |
| Has `migrate.yaml` | ✅ Migration workflow config |

---

## Key Architecture Decisions

1. **Django standard layout** — Two apps (`base`, `rhixecompany`) with separate responsibilities.
2. **CKEditor integration** for rich text editing in static files.
3. **Comprehensive documentation** — Standard set of project docs (API reference, DB schema, deployment, etc.).
4. **Heroku-ready** with `Procfile`.
5. **Migration workflow** defined in `migrate.yaml`.
