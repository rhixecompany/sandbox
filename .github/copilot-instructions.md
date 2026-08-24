# Copilot Instructions — SandBox Monorepo

**Canonical reference:** See `AGENTS.md` (general agent guidance), `.hermes.md` (Hermes-specific), `CLAUDE.md` (Claude-specific).

## Quick Start

```bash

# Root workspace setup

cd C:/Users/Alexa/Desktop/SandBox
bun install
python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt

# Root workspace validation (workspace-level code only)

bun run lint && bun run format:check && bun run typecheck

# For subproject work, see the project's own AGENTS.md and package.json scripts

```

## Architecture: Hermes-Centric Polyglot Monorepo

**SandBox** is a 17+ subproject monorepo with independent build systems, each under `projects/`. Every subproject is autonomous — it has its own `AGENTS.md`, `package.json`/`pyproject.toml`, `tsconfig.json`, and CI workflows.

### Key Pattern: Subproject Autonomy

- **Root workspace** lints only root-level code (config, scripts, top-level TypeScript/Python)

- **Subprojects** are excluded from root `tsconfig.json` and linting (`projects/` is in ignore lists)

- **Each subproject has its own**: AGENTS.md, build commands, test suite, CI workflow

- **Shared:** `.github/workflows/` (shared CI), `.github/prompts/` (canonical prompt library), tool configs (Prettier, ESLint flat config, Ruff, etc.)

When working on a subproject:

1. Read **that project's AGENTS.md** first (e.g., `projects/Bash/AGENTS.md`)

2. Use **that project's build/test commands** from `package.json` or `README.md`

3. Root-level workspace commands apply only to root-level changes

---

*This file is a thin wrapper. All conventions, workflows, and rules are in `AGENTS.md`.*
