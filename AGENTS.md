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

**See `PROJECT_RULES.md` at workspace root for project-specific rules + `~/AppData/Local/hermes/MASTER_RULES.md` for global rules.**

Context files follow the DRY hierarchy:

- `SOUL.md` — Core 5 non-negotiables (inline) + reference to MASTER_RULES.md + PROJECT_RULES.md
- `USER.md` — Execution preferences (inline) + reference to MASTER_RULES.md + PROJECT_RULES.md
- `AGENTS.md` — Workspace conventions + reference to PROJECT_RULES.md + MASTER_RULES.md
- `.hermes.md` — Hermes-specific overrides + reference to PROJECT_RULES.md + MASTER_RULES.md

### Quick Rule Summary

| #   | Rule                   | Brief                                                 |
| --- | ---------------------- | ----------------------------------------------------- |
| 1   | **Session Start**      | Search/read/explain SESSION_REPORT.md before any work |
| 2   | **MCP Tools**          | Use MCP over native equivalents                       |
| 3   | **Profile Selection**  | Route by task type                                    |
| 4   | **Scripts (PY/JS/TS)** | NEVER inline; create permanent files; use patch tool  |
| 5   | **Strict Sequential**  | "only then" = hard constraint                         |

## Notes

- Never commit secrets, tokens, or `.env`
- Update `SESSION_REPORT.md` on session start/end; rolling session summary
- Toolchain: `python3=3.13.14`, `python=3.11.15`, `pip→python3.11`, `uv=installed`
- Active ecosystem audit plan: `.hermes/plans/2026-06-16_eco-system-audit-plan.md`

## Hermes Config (Current)

- **Active Profile:** `default` — **OWL persona** (pragmatic senior engineer)
- **Current Runtime:** deepseek-v4-flash-free (opencode fallback chain)
- **Primary Config:** gpt-5.4-mini (openai-codex)
- **Config:** `~/AppData/Local/hermes/config.yaml`
- **Hooks (3, shared):** `session-logger`, `session-auto-commit`, `governance-audit`
- **Plugins (15 enabled):** `basic`, `copilot-provider`, `custom-provider`,
  `disk-cleanup`, `huggingface-provider`, `langfuse`, `nous`, `nous-provider`,
  `ollama-cloud-provider`, `openai-codex`, `openai-codex-provider`,
  `opencode-zen-provider`, `openrouter-provider`, `security-guidance`, `web-tavily`
- **Skills:** 373 available post-dedup (73 bundled + 216 community + 84 local)
- **MCP Servers (11):** ast-grep, cli, code-sandbox, fetch, filesystem, github,
  linear, mcp-docker, memory, playwright, sequential-thinking

## Profile Inventory

| Profile           | Model                 | Provider     | Purpose                                 |
| ----------------- | --------------------- | ------------ | --------------------------------------- |
| **default** ⬤     | gpt-5.4-mini          | openai-codex | General purpose — **currently active**  |
| adminbot          | nemotron-3-ultra-free | opencode-zen | System admin, operations                |
| code-architect    | nemotron-3-ultra-free | opencode-zen | Code changes, debugging, refactoring    |
| creative-director | nemotron-3-ultra-free | opencode-zen | Design, content, creative tasks         |
| exec-assistant    | nemotron-3-ultra-free | opencode-zen | Administrative, planning, coordination  |
| patient-tutor     | nemotron-3-ultra-free | opencode-zen | Explanations, tutorials, learning       |
| research-analyst  | nemotron-3-ultra-free | opencode-zen | Deep research, synthesis, documentation |

## Toolsets (18 Enabled)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`,
`moa`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`,
`clarify`, `delegation`, `cronjob`, `search`

## Provider Chain

| Provider     | Role                                                    | Status              |
| ------------ | ------------------------------------------------------- | ------------------- |
| openai-codex | Active primary (gpt-5.4-mini)                           | ✓ Configured        |
| opencode-zen | Fallback (nemotron-3-ultra-free, nemotron-3-super-free) | ✓ In fallback chain |
| openrouter   | Available via plugin                                    | ✓ Enabled           |
| nous         | Available via plugin                                    | ✓ Enabled           |

## Environment Corrections (2026-06-21)

- **OS:** Windows 11 (not Windows 10)
- **Editor:** VS Code (not notepad)
- **Terminal:** VS Code Git Bash (bash via git-bash/MSYS)
