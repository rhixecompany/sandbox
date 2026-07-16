# projects/mcp-servers/copilot-studio — Architecture Blueprint

## Overview
- Detected stack: Bun, TypeScript
- Architectural pattern: Lightweight utility or scaffold project
- Top-level components: dist, node_modules, tools

## Component Map
- `dist, node_modules, tools`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
copilot-studio/
├── tools/
│   ├── get-customer-details.ts
│   └── search-customers.ts
├── apiDefinition.swagger.json
├── bun.lock
├── package-lock.json
├── package.json
├── README.md
├── server.ts
└── tsconfig.json
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
