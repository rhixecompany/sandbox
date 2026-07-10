# SandBox — Technology Stack

## Root

| Layer | Tech |
| --- | --- |
| Runtime | Bun 1.3.14+, Node, Python 3.11.15 / 3.13.14 |
| Language | TypeScript (strict), Python |
| Package mgr | bun, pip/uv (venv) |
| Tooling | ruff, eslint, prettier, tsc, playwright |
| Editor | VS Code (multi-root), Pylance, Bun debugger |

## Subproject Stacks

- **Bash / Resume_maker / web**: Bun + TypeScript + Prettier + ESLint
- **mcp-servers**: per-language (TS/Python/Go/Rust/Java/Kotlin/PHP/Ruby/Swift/C#) with dotnet/Cargo/go toolchains
- **Python-projects**: Python + ruff + mypy
- **Django apps**: Django + Tailwind + Supabase (rhixe_scans)
- **docs / profile**: markdown + VS Code writing tools
