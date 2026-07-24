# Copilot Instructions

Project-wide guidance for GitHub Copilot in this workspace.

## Workspace

- Automation root: `projects/Bash/` (Bun/TS + `.sh`/`.ps1`/`.bat` wrappers)
- Project apps: `projects/*/` — use each project's local `AGENTS.md` first
- Prompt/agent/instruction assets: `.github/prompts/`, `.github/agents/`, `.github/instructions/`

## Source of Truth

- `projects/Bash/package.json` scripts and entrypoints
- `projects/Bash/README.md` toolkit overview
- `projects/Bash/docs/CODE_STYLE.md` wrapper/logging/naming rules
- Reuse existing prompts/agents/instructions/skills before creating new ones

## Commands

Run from `projects/Bash/` unless a subproject says otherwise.

```bash
bun install --frozen-lockfile || bun install
bun run format
bun run typecheck
bun run lint:strict
bash tests/verify-dryrun.sh
bash test-all.sh
```

Key scripts: `format`, `typecheck`, `lint:strict`, `lint:fix`, `upgrade`, `clean:cache`, `clean:deps`, `commit:batches`.

## Conventions

- Minimal, scoped edits; preserve wrapper parity across `.sh`, `.ps1`, `.bat`
- Destructive actions require `--dry-run`, confirmation, or explicit `--auto`
- No backup files like `.bak`/`.old`; use git rollback
- Bash: kebab-case files, UPPER_SNAKE vars, `set -uo pipefail`, `trap cleanup EXIT`
- PowerShell: PascalCase files/vars, `param()`, try/catch, `$LASTEXITCODE` checks
- TypeScript: strict, no `any`, `zod` v4 runtime checks, `ts-morph` AST transforms
- Logs: `logs/action_YYYYMMDD_HHMMSS.log`, no secrets

## Python

- `python3` → 3.13.14; `python` → 3.11.15; `pip` → `python3.11`
- Never inline one-off Python; use scripts under `C:/Users/Alexa/AppData/Local/hermes/scripts/`
- Prefer `python3 -m pip`

## Security

- Never commit secrets, `.env`, or credentials
- Validate external paths/args; prefer least privilege
- Keep cleanup/destructive operations explicit and reversible

## Hermes

- Profiles: default, alexa, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst
- Switch: `hermes profile use <name>`
- Match profile to task: code→architect, research→analyst, ops→alexa, planning→exec, teaching→tutor, design→creative
- Hooks: `session-logger`, `session-auto-commit`, `governance-audit`
- Plugins: disk-cleanup, security-guidance, model-providers/openrouter
- Skill scripts use `jq -c`, `awk` for float comparison, and support SKIP flags

## Session Start

1. Read `SESSION_REPORT.md`
2. Prefer MCP tools: `filesystem`, `github`, `ast-grep`, `memory`, `playwright`, `fetch`, `code-sandbox`, `mcp-docker`, `sequential-thinking`, `cli`
3. Switch to the correct Hermes profile for the task
