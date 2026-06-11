# Copilot Instructions

Project-wide guidance for GitHub Copilot in this workspace.

## Workspace shape

- `Bash/` is the main automation toolkit and operational root.
- `Bash/src/` contains the TypeScript implementations.
- `Bash/` root scripts (`*.sh`, `*.ps1`, `*.bat`) are thin wrappers around shared logic.
- `Bash/docs/` contains script documentation and style guidance.
- `Bash/tests/` contains script-level verification.
- `projects/` contains separate apps with their own package managers and local instructions.
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
bun install --frozen-lockfile || bun install
bun run format
bun run typecheck
bun run lint:strict
bash tests/verify-dryrun.sh
bash test-all.sh
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

## Architecture

- This is a script-focused monorepo, not a single compiled app.
- The Bash toolkit favors dry-run safety, reproducible execution, and parity across Bash, PowerShell, and batch wrappers.
- Cleanup and upgrade workflows are implemented in TypeScript and surfaced through shell entrypoints.
- Logs are written to `logs/` with timestamped filenames.
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
- Hermes hooks: session-logger, session-auto-commit, governance-audit
- Hermes plugins: disk-cleanup, model-providers/openrouter, security-guidance
- Hook scripts must use `jq -c` for compact JSON, `awk` for float comparison, and support SKIP flags
