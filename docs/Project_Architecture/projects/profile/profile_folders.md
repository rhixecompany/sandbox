# projects/profile — Folder Structure Blueprint

## Overview
- Namespace: `projects/profile`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
