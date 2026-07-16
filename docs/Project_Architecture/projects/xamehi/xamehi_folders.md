# projects/xamehi — Folder Structure Blueprint

## Overview
- Namespace: `projects/xamehi`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
