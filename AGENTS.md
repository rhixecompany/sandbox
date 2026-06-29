# SandBox Context

Automation scripts, prompt assets, and 15+ subprojects.

## Structure

- `Bash/` — primary toolkit (Bun, TypeScript, shell)
- `projects/` — per-project workspaces
- `docs/` — extracted Hermes docs, architecture, audit reports
- `.github/` — Copilot config, prompts, hooks (reference only)
- `.hermes/` — Hermes plans and workspace config

## Conventions

- Bun for TypeScript (`bun run`, `bun install`)
- PowerShell 5.1+ for orchestration
- Git for version control; no `.bak`/`.backup`/`.old` copies
- Keep edits minimal and scoped
- DRY: don't repeat facts across files

## Toolkit Validation

```bash
cd Bash && bun run format && bun run typecheck && bun run lint:strict
```

## Subprojects

Each has its own `AGENTS.md`. See `projects/*/`.

## Rules

**See `SOUL.md` for core operating principles (rules consolidated there).**

### Quick Rule Summary

1. **Session Start** — Search/read/explain SESSION_REPORT.md
2. **MCP Tools** — Use MCP over native equivalents
3. **Profile Selection** — Route by task type
4. **Scripts** — NEVER inline; create permanent files; patch tool
5. **Strict Sequential** — "only then" = hard constraint
6. **Session Startup** — Load 5 skills (using-superpowers, user-communication-preferences, session-audit-report, hermes-profiles, validate-memories)
7. **MCP First** — MCP server tools before native
8. **Profile Per Task** — `hermes profile use <name>` before execution

## Notes

- Never commit secrets, tokens, or `.env`
- Update `SESSION_REPORT.md` on session start/end
- Toolchain: python3=3.13.14, python=3.11.15, pip→python3.11, uv, Bun=1.3.14+
- Active ecosystem audit plan: `.hermes/plans/2026-06-16_eco-system-audit-plan.md`
