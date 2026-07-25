# projects/mcp-servers/php — Architecture Blueprint

## Overview

- Detected stack: PHP/Composer
- Architectural pattern: PHP/Composer project
- Top-level components: src

## Component Map

- `src`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure

```text
php/
├── src/
│   └── Tools/
├── composer.json
├── README.md
└── server.php
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
