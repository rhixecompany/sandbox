# projects/profile — Architecture Blueprint

## Overview
- Detected stack: Django, Python
- Architectural pattern: Django backend service
- Top-level components: base, rhixecompany, static, templates

## Component Map
- `base, rhixecompany, static, templates`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
profile/
├── .github/
│   └── copilot-instructions.md
├── base/
│   ├── migrations/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── rhixecompany/
│   ├── migrations/
│   ├── __init__.py
│   ├── asgi.py
│   ├── setting.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── admin/
│   ├── ckeditor/
│   ├── css/
│   ├── images/
│   ├── js/
│   └── resume.pdf
├── templates/
│   ├── base/
│   ├── email_sent.html
│   ├── password_reset.html
│   ├── reset.html
│   └── reset_complete.html
├── .gcloudignore
├── AGENTS.md
├── AUDIT_profile.md
├── db.sqlite3
├── manage.py
├── migrate.yaml
├── Procfile
├── REPOSITORY_SUMMARY.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── THE_STORY_OF_THIS_REPO.md
└── web-research-profile.md
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
