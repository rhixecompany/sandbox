# Project Context

This is the SandBox multi-project workspace for automation scripts, prompt/instruction assets, and repository maintenance tooling.

## Architecture
- **Root orchestration:** PowerShell/Bun scripts for workspace management
- **Primary toolkit:** `Bash/` — Bun, TypeScript, shell automation
- **Subprojects:** 15+ projects under `projects/` (Next.js, Django, Python, full-stack)
- **Documentation:** `docs/` — extracted Hermes Agent documentation (13 pages)
- **Configuration:** `.github/` — Copilot agents, skills, prompts, hooks, plugins

## Conventions
- Use Bun for TypeScript execution (`bun run`, `bun install`)
- PowerShell 5.1+ for orchestration scripts
- Git for version control — never create .bak/.backup files
- Keep edits minimal and scoped to requested behavior
- Follow DRY: one concern per file, no duplication across AGENTS.md files

## Validation & Quality Gates
```bash
# Bash toolkit
cd Bash && bun run format && bun run typecheck && bun run lint:strict

# Subprojects: each has own validation (see local AGENTS.md)
```

## Important Notes
- Never commit secrets, tokens, credentials, or `.env` files
- Hermes profile: `adminbot` (model: openrouter/owl-alpha)
- Active skills: 289 in `.github/skills/`
- Active hooks: session-logger, session-auto-commit, governance-audit
- Active plugins: disk-cleanup, model-providers/openrouter, security-guidance

## Subdirectory Context Discovery
This workspace uses progressive subdirectory discovery. Each major project has its own AGENTS.md:
- `Bash/AGENTS.md` — Automation toolkit conventions
- `projects/*/AGENTS.md` — Per-project context (see Phase 6)