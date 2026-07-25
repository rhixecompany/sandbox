# projects/xamehi.tv — Folder Structure Blueprint

## Overview

- Namespace: `projects/xamehi.tv`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
xamehi.tv/
├── .github/
│   ├── workflows/
│   └── copilot-instructions.md
├── frontend/
│   ├── public/
│   ├── src/
│   ├── .eslintcache
│   ├── bun.lock
│   ├── debug.log
│   ├── package-lock.json
│   └── package.json
├── player/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── admin/
├── video/
│   ├── migrations/
│   ├── urls/
│   ├── views/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── pymongo_views.py
│   ├── serializers.py
│   ├── tests.py
│   ├── url.py
│   └── view.py
├── .env.example
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── AUDIT_xamehi.tv.md
├── CHANGELOG.md
├── code-exemplars.md
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPER_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── execution-summary.md
├── folder-structure.md
├── gunicorn.service
├── gunicorn.socket
├── manage.py
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
├── THE_STORY_OF_THIS_REPO.md
├── USER_GUIDE.md
├── validation-report.md
└── web-research-xamehi-tv.md
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
