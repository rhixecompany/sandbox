# projects/mcp-servers/php — Folder Structure Blueprint

## Overview

- Namespace: `projects/mcp-servers/php`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
php/
├── src/
│   └── Tools/
├── composer.json
├── README.md
└── server.php
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
