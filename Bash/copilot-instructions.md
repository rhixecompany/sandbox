# Bash — Automation Toolkit

**Naming**: `kebab-case` for `.ts`, `.sh`, `.ps1`, `.bat` files; `camelCase` for variables/functions in TypeScript; `PascalCase` for types/interfaces; `UPPER_SNAKE_CASE` for constants.

**Patterns**: Dry-run first (`--dry-run`); `--help` for all scripts; logging to `logs/` with timestamps; modular library pattern in `scripts/lib/`; phase-based pipeline (discovery → clone → triage → debug → remediation → cross-ref); cross-platform wrapper parity (`.sh`/`.ps1`/`.bat`).

**Structure**: `src/` for TypeScript source; `scripts/` for PowerShell orchestration; `scripts/lib/` for reusable modules; `tests/` for shell tests; `migrations/<project>/` for per-project migration scripts; `docs/` for documentation.

**TypeScript**: Strict mode; ES Modules (`"type": "module"`); Bun runtime; interfaces over types; explicit exports; `zod` for validation; `yaml` for YAML parsing; `tsx` for execution.

**Shell/PowerShell**: PowerShell 5.1+ for orchestration; Bash for cross-platform; Batch (.bat) as Windows fallback; `$ErrorActionPreference = 'Stop'` in PowerShell; robust error handling with try/catch/finally.

**Env**: No secrets committed; `.env.example` for reference; `NODE_ENV` only in templates.

**Commands**: `bun run format && bun run typecheck && bun run lint:strict` (validation); `bun run clean:cache --all --dry-run` (preview); `bun run clean:deps --dry-run`; `bunx tsx src/<script>.ts` (direct execution).

**Testing**: Vitest for TypeScript unit tests; `tests/verify-dryrun.sh` for shell validation; `process` health checks via `test-all.sh`.

**Pre-commit**: `bun run format && bun run typecheck && bun run lint:strict`.
