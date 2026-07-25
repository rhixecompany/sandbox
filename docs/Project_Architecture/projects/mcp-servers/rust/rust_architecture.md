# projects/mcp-servers/rust — Architecture Blueprint

## Overview

- Detected stack: Rust
- Architectural pattern: Rust crate / tool
- Top-level components: src

## Component Map

- `src`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure

```text
rust/
├── src/
│   ├── tools/
│   ├── main.rs
│   └── state.rs
├── Cargo.toml
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
