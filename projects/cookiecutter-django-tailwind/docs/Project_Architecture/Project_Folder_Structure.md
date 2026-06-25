# Project Folder Structure Blueprint

## Project: cookiecutter-django-tailwind — Django Template with Tailwind CSS

**Generated:** 2026-06-25  
**Project Type:** Django Python + Cookiecutter Template  
**Auto-detected:** Yes (Django — `manage.py`, `pyproject.toml`, `setup.py`, `requirements.txt`, `tox.ini`)

---

## Directory Tree

```
cookiecutter-django-tailwind/
├── .dockerignore
├── .editorconfig
├── .env.example
├── .flake8
├── .github/
├── .gitignore
├── .pre-commit-config.yaml
├── .pyup.yml
├── .readthedocs.yaml
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── LICENSE
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── code-exemplars.md
├── cookiecutter.json        # Cookiecutter configuration
├── copilot-instructions.md
├── cross-linking-report.md
├── docs/
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── hooks/                   # Cookiecutter hooks (pre/post generation)
├── project-workflow.md
├── pyproject.toml
├── requirements.txt
├── scripts/
├── setup.py
├── technology-stack.md
├── tests/
├── tox.ini
├── validation-report.md
└── {{cookiecutter.project_slug}}/   # Cookiecutter template variables
    ├── manage.py
    ├── requirements/
    ├── config/
    │   ├── settings/
    │   ├── urls.py
    │   └── wsgi.py
    ├── apps/
    ├── static/
    ├── templates/
    ├── theme/               # Tailwind CSS theme
    │   └── static_src/
    └── docker-compose.yml
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Cookiecutter variable dirs** | `{{...}}` template syntax | `{{cookiecutter.project_slug}}/` |
| **Django apps** | lowercase plural | `apps/`, `config/`, `theme/` |
| **Config files** | dotted-prefix | `.flake8`, `.pre-commit-config.yaml` |
| **Documentation** | UPPER_CASE.md | `README.md`, `CHANGELOG.md`, `LICENSE` |
| **Python files** | snake_case | `setup.py`, `pyproject.toml` |

---

## File Placement Patterns

- **Cookiecutter template**: Root-level `{{cookiecutter.project_slug}}/` contains generated project template
- **Cookiecutter config**: `cookiecutter.json`
- **Python packaging**: `setup.py`, `pyproject.toml`, `tox.ini`
- **Quality tools**: `.flake8`, `.pre-commit-config.yaml`, `.pyup.yml`
- **Tests**: `tests/`
- **Generated Django project**: `{{cookiecutter.project_slug}}/` with standard Django layout

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `cookiecutter.json` | ✅ Cookiecutter template |
| Has `manage.py` inside template | ✅ Django project |
| Has `tox.ini` | ✅ Python testing matrix |
| Has `.pre-commit-config.yaml` | ✅ Pre-commit hooks |
| Has `.flake8` | ✅ Flake8 linting |
| Has `setup.py` | ✅ Python package |
| Tailwind CSS theme | ✅ Uses django-tailwind |

---

## Key Architecture Decisions

1. **Cookiecutter template** — Generates new Django projects with Tailwind CSS pre-configured.
2. **Django standard layout** — `config/` for settings, `apps/` for applications, `static/` for assets.
3. **django-tailwind** integration with `theme/` app containing `static_src/` for Tailwind source files.
4. **Two-tier docs**: Documentation for the template itself and generated project doc stubs.
5. **Docker-ready** — Generated project includes `docker-compose.yml`.
