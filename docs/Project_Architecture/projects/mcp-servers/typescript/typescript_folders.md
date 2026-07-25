# projects/mcp-servers/typescript — Folder Structure Blueprint

## Overview

- Namespace: `projects/mcp-servers/typescript`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
typescript/
├── src/
│   ├── tools/
│   └── index.ts
├── bun.lock
├── package-lock.json
├── package.json
├── README.md
└── tsconfig.json
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
