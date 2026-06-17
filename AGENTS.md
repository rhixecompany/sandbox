# SandBox Context

Automation scripts, prompt assets, and 15+ subprojects.

## Structure

- `Bash/` — primary toolkit (Bun, TypeScript, shell)
- `projects/` — per-project workspaces
- `docs/` — extracted Hermes docs
- `.github/` — Copilot config, skills, prompts, hooks

## Conventions

- Bun for TypeScript (`bun run`, `bun install`)
- PowerShell 5.1+ for orchestration
- Git for version control; no `.bak`/`.backup` files
- Keep edits minimal and scoped

## Toolkit Validation

```bash
cd Bash && bun run format && bun run typecheck && bun run lint:strict
```

## Subprojects

Each has its own `AGENTS.md`. See `projects/*/`.

## Strict Rules

### 1. Session Start

1. Search for `SESSION_REPORT.md`
2. Read it completely
3. Summarize back before proceeding

### 2. MCP Preference

Use MCP tools when available over native equivalents.

### 3. Profile Selection

| Profile             | Use                   |
| ------------------- | --------------------- |
| `code-architect`    | Code, debug, refactor |
| `research-analyst`  | Research, synthesis   |
| `creative-director` | Design, content       |
| `exec-assistant`    | Planning, admin       |
| `patient-tutor`     | Tutorials, teaching   |
| `adminbot`          | Ops, DevOps, infra    |
| `default`           | Fallback              |

### 4. Python Scripts

- Create permanent scripts under `C:/Users/Alexa/AppData/Local/hermes/scripts/`
- Execute from there; debug and rerun until clean; keep for reuse

## Notes

- Never commit secrets, tokens, or `.env`
- Update `SESSION_REPORT.md` on session start/end; rolling 5-session summary
- Toolchain: `python3=3.14.6`, `python=3.11.14`, `pip→python3.11`
- Active ecosystem audit plan: `.hermes/plans/2026-06-16_eco-system-audit-plan.md`

## Hermes Config

- Active profile: `default` (`nvidia/nemotron-3-ultra:free`)
- Config: `C:\Users\Alexa\AppData\Local\hermes\config.yaml`
- Hooks: `session-logger`, `session-auto-commit`, `governance-audit`
- Plugins: `awesome-hermes-agent`, `disk-cleanup`, `memory/honcho`, `model-providers/openrouter`, `security-guidance`
- Skills: 289 bundled + 216 community

## MCP Servers

`ast-grep`, `cli`, `code-sandbox`, `fetch`, `filesystem`, `github`, `mcp-docker`, `memory`, `playwright`, `sequential-thinking`
