# projects/xamehi — Architecture Blueprint

## Overview
- Detected stack: React, Node.js, Django
- Architectural pattern: Full-stack dual-stack app (Django backend + JavaScript frontend/tooling)
- Top-level components: src, docs

## Component Map
- `src, docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
xamehi/
├── .github/
│   └── copilot-instructions.md
├── public/
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── src/
│   ├── components/
│   ├── App.js
│   ├── index.css
│   ├── index.js
│   └── reportWebVitals.js
├── xamehi/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env.example
├── AGENTS.md
├── ARCHITECTURE.md
├── AUDIT_xamehi.md
├── CONTRIBUTING.md
├── DEVELOPER_GUIDE.md
├── index.js
├── manage.py
├── package.json
├── README.md
├── REPOSITORY_SUMMARY.md
├── RESEARCH_REPORT.md
├── THE_STORY_OF_THIS_REPO.md
├── USER_GUIDE.md
└── web-research-xamehi.md
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
