# projects/rhixecompany-comics/backend — Architecture Blueprint

## Overview

- Detected stack: Django, Python
- Architectural pattern: Django backend service
- Top-level components: apps, config, __pycache__

## Component Map

- `apps, config, __pycache__`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure

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

## Cross-Cutting Concerns

- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points

- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes

- Regenerate when component boundaries, package dependencies, or folder structure change.
