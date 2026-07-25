# projects/mcp-servers/kotlin — Folder Structure Blueprint

## Overview

- Namespace: `projects/mcp-servers/kotlin`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
kotlin/
├── src/
│   └── main/
├── build.gradle.kts
├── gradle.properties
├── README.md
└── settings.gradle.kts
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
