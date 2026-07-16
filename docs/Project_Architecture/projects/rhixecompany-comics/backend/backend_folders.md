# projects/rhixecompany-comics/backend — Folder Structure Blueprint

## Overview
- Namespace: `projects/rhixecompany-comics/backend`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
```text
backend/
├── apps/
│   ├── api/
│   ├── comics/
│   ├── core/
│   ├── scraping/
│   ├── users/
│   └── __init__.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env.example
├── Dockerfile
├── manage.py
└── requirements.txt
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
