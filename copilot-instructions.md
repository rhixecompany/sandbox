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

*All conventions, workflows, and rules are in `AGENTS.md`.*
