# projects/mcp-servers/go — Folder Structure Blueprint

## Overview

- Namespace: `projects/mcp-servers/go`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
go/
├── config/
│   └── config.go
├── tools/
│   ├── registry.go
│   ├── tool1.go
│   └── tool2.go
├── go.mod
├── main.go
├── main_test.go
└── README.md
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
