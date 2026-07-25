# projects/mcp-servers/go — Architecture Blueprint

## Overview

- Detected stack: Go
- Architectural pattern: Go service/library
- Top-level components: config, tools

## Component Map

- `config, tools`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure

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

## Cross-Cutting Concerns

- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points

- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes

- Regenerate when component boundaries, package dependencies, or folder structure change.
