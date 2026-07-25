# projects/xamehi.tv — Architecture Blueprint

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

## Cross-Cutting Concerns

- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points

- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes

- Regenerate when component boundaries, package dependencies, or folder structure change.
