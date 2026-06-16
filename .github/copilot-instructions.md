# Copilot Instructions

Project-wide guidance for GitHub Copilot in this workspace.

## Workspace shape

- `Bash/` is the main automation toolkit and operational root.
- `Bash/src/` contains the TypeScript implementations (`upgrade.ts`, `cache-clean.ts`, `clean-dep.ts`, `git-commit-batches.ts`).
- `Bash/src/core/` contains shared utilities: `dry-run.ts`, `script-runner.ts`, `ast-transformer.ts`.
- `Bash/src/migration/` contains migration helpers and the `ts-morph-helper.ts` code-transform layer.
- `Bash/` root scripts (`*.sh`, `*.ps1`, `*.bat`) are thin wrappers that delegate to the TypeScript implementations.
- `Bash/docs/` contains script documentation, `CODE_STYLE.md`, `ARCHITECTURE.md`, and style guidance.
- `Bash/tests/` contains `verify-dryrun.sh` and `behavior/` + `integration/` sub-suites.
- `projects/` contains ~15 separate apps (Next.js, Django, Python, full-stack) with their own package managers and local instructions.
- `Resume_maker/` is a standalone Bun/TypeScript project.

Use the nearest `AGENTS.md` and local `.github` instructions first; root guidance is fallback.

## Source of truth

- `Bash/package.json` for scripts and task entrypoints.
- `Bash/README.md` for the Bash toolkit overview and script reference.
- `Bash/docs/CODE_STYLE.md` for naming, logging, and wrapper conventions.
- `reports/inventory/refresh-agent-inventory-summary-2026-05-30.md` before creating new prompts, skills, agents, hooks, or plugins.

Workspace inventory snapshot (2026-05-30):

- Instructions: 34
- Agents: 159
- Prompts: 185
- Skills: 289
- Hooks: 2
- Plugins: 21

## Commands

Run these from `Bash/` unless the target subproject says otherwise.

```bash
# Dependencies
bun install --frozen-lockfile || bun install

# Format, type-check, lint
bun run format
bun run typecheck
bun run lint:strict

# Tests
bash tests/verify-dryrun.sh
bash test-all.sh

# Shell linting (run from Bash/ root)
shfmt -d .
shellcheck $(git ls-files | grep -E '\.sh$' || true)
```

Single Vitest file:

```bash
bunx vitest run src/migration/__tests__/ts-module-template.test.ts
```

Helpful variants:

```bash
bun run format:check
bun run format:markdown:check
bun run lint:fix
```

Key `bun run` script names (from `Bash/package.json`):

| Script | Purpose |
|---|---|
| `format` | Prettier write |
| `typecheck` | `tsc --noEmit` |
| `lint:strict` | ESLint, zero warnings |
| `lint:fix` | ESLint auto-fix |
| `upgrade` | Run `src/upgrade.ts` |
| `clean:cache` | Run `src/cache-clean.ts` |
| `clean:deps` | Run `src/clean-dep.ts` |
| `commit:batches` | Run `src/git-commit-batches.ts` |
| `verify-install` | Run `scripts/phase-5-verify-install.sh` |

## Architecture

- This is a script-focused monorepo, not a single compiled app.
- The Bash toolkit favors dry-run safety, reproducible execution, and parity across Bash, PowerShell, and batch wrappers.
- Each script type has a canonical pattern: **Bash** (`set -uo pipefail`, color output with `RED`/`GREEN`/`NC`, `trap cleanup EXIT`); **PowerShell** (`param()` block, PascalCase vars, try/catch, `$LASTEXITCODE` checks).
- Cleanup and upgrade workflows are implemented in TypeScript (`src/`) and surfaced through thin shell entrypoints — never duplicate logic in both layers.
- Logs are written to `logs/` with timestamped filenames (`action_YYYYMMDD_HHMMSS.log`).
- All destructive scripts must support `--dry-run` / `-DryRun` for preview and require confirmation unless `--auto` / `-Auto` is set.
- CI expectations for the Bash toolkit are encoded in:
  - `.github/workflows/bash-scripts-ci.yml`
  - `.github/workflows/copilot-setup-steps.yml`

## Conventions

- Keep edits minimal and scoped to the requested behavior.
- Preserve wrapper behavior across `.sh`, `.ps1`, and `.bat`.
- Keep destructive actions behind confirmations or explicit flags.
- Support `--help` and `--dry-run` where the script is meant to preview changes.
- Keep logs and console output actionable and consistent.
- Use the project-local instructions for any `projects/*` app instead of assuming Bash conventions apply there.
- Never create `.bak`, `.backup`, `.old`, or timestamped backup files — use git for rollback.

### Naming

- Bash scripts: `lowercase-with-hyphens.sh`; Bash vars: `UPPER_SNAKE_CASE`; Bash functions: `lower_snake_case()`
- PowerShell scripts: `PascalCase.ps1`; PS vars: `$PascalCase`; PS functions: `Verb-Noun`
- TypeScript: follow existing file names in `src/`

### Python toolchain

- `python3` → 3.14.6; `python` → 3.11.14; `pip` → resolves to python3.11 (mismatch — use `python3 -m pip` explicitly)
- Never write inline one-off Python. Create scripts in `C:/Users/Alexa/AppData/Local/hermes/scripts/` and run from there.

## AI asset reuse

- Reuse existing prompts, skills, agents, hooks, and plugins before adding new ones.
- Check root `.github` assets first, then subproject-local assets, then the inventory report for conflicts.
- Hermes hooks live in `~/AppData/Local/hermes/hooks/`.
- Hermes plugins live in `~/AppData/Local/hermes/plugins/`.

## Security

- Never commit secrets, tokens, credentials, or local environment files.
- Validate and sanitize external paths and arguments.
- Prefer least-privilege execution.
- Keep cleanup and destructive operations explicit and reversible where possible.

## Hermes Integration

- Hermes profiles: adminbot (active), default, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst
- Switch profile: `hermes profile use <name>`
- **Match profile to task**: `code-architect` for code/debug/refactor; `research-analyst` for research; `adminbot` for system/DevOps; others as appropriate.
- Hermes hooks: session-logger, session-auto-commit, governance-audit
- Hermes plugins: disk-cleanup, model-providers/openrouter, security-guidance
- Hook scripts must use `jq -c` for compact JSON, `awk` for float comparison, and support SKIP flags

## Session start

At the start of every session:
1. Search for and read `SESSION_REPORT.md` in the workspace root before proceeding.
2. Prefer MCP server tools when available (`filesystem`, `github`, `ast-grep`, `memory`, `playwright`, `fetch`, `code-sandbox`, `mcp-docker`, `sequential-thinking`, `cli`).
3. Switch to the correct Hermes profile for the task.
