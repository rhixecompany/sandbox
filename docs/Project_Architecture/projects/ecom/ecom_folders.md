# projects/ecom — Folder Structure Blueprint

## Overview
- Namespace: `projects/ecom`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
