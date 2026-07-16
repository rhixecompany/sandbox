# projects/ecom — Architecture Blueprint

## Overview
- Detected stack: Django, Python
- Architectural pattern: Django backend service
- Top-level components: frontend, docs

## Component Map
- `frontend, docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
ecom/
├── .github/
│   ├── workflows/
│   └── copilot-instructions.md
├── base/
│   ├── migrations/
│   ├── urls/
│   ├── views/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── products.py
│   ├── serializers.py
│   ├── signals.py
│   └── tests.py
├── ecom/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── frontend/
│   ├── public/
│   ├── src/
│   ├── bun.lock
│   ├── package-lock.json
│   ├── package.json
│   └── README.md
├── resources/
│   ├── images/
│   ├── bucket-policy.txt
│   ├── favicon.ico
│   ├── products.js
│   └── products.py
├── .env.example
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── AUDIT_ecom.md
├── CHANGELOG.md
├── code-exemplars.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── db.sqlite3
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── ecom.service
├── ecom.socket
├── execution-summary.md
├── folder-structure.md
├── install.sh
├── manage.py
├── modules.txt
├── Pipfile
├── Pipfile.lock
├── Procfile
├── project-workflow.md
├── README.md
├── REPOSITORY_SUMMARY.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── runtime.txt
├── SECURITY.md
├── SETUP_GUIDE.md
├── technology-stack.md
├── TESTING_GUIDE.md
```

## Cross-Cutting Concerns
- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points
- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes
- Regenerate when component boundaries, package dependencies, or folder structure change.
