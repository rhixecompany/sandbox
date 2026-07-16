# projects/mcp-servers/python — Architecture Blueprint

## Overview
- Detected stack: Python
- Architectural pattern: Python service or utility project
- Top-level components: __pycache__

## Component Map
- `__pycache__`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
python/
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
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
