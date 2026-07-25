# projects/xamehi.tv/frontend — Folder Structure Blueprint

## Overview

- Namespace: `projects/xamehi.tv/frontend`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
frontend/
├── public/
│   ├── static/
│   ├── index.html
│   └── robots.txt
├── src/
│   ├── actions/
│   ├── components/
│   ├── constants/
│   ├── reducers/
│   ├── screens/
│   ├── App.js
│   ├── bootstrap.min.css
│   ├── index.css
│   ├── index.js
│   ├── reportWebVitals.js
│   └── store.js
├── .eslintcache
├── bun.lock
├── debug.log
├── package-lock.json
└── package.json
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
