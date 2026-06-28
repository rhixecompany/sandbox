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

| #   | Rule                   | Brief                                                                                                                      |
| --- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Session Start**      | Search/read/explain SESSION_REPORT.md before any work                                                                      |
| 2   | **MCP Tools**          | Use MCP over native equivalents                                                                                            |
| 3   | **Profile Selection**  | Route by task type                                                                                                         |
| 4   | **Scripts (PY/JS/TS)** | NEVER inline; create permanent files; use patch tool                                                                       |
| 5   | **Strict Sequential**  | "only then" = hard constraint                                                                                              |
| 6   | **Session Startup**    | Load 5 skills: using-superpowers, user-communication-preferences, session-audit-report, hermes-profiles, validate-memories |
| 7   | **MCP First**          | Use MCP server tools before native tool equivalents                                                                        |
| 8   | **Profile Per Task**   | `hermes profile use <name>` before task execution                                                                          |

## Notes

- Never commit secrets, tokens, or `.env`
- Update `SESSION_REPORT.md` on session start/end; rolling session summary
- Toolchain: `python3=3.13.14`, `python=3.11.15`, `pip→python3.11`, `uv=installed`
- Active ecosystem audit plan: `.hermes/plans/2026-06-16_eco-system-audit-plan.md`

## Hermes Config (Current)

- **Active Profile:** `alexa` — **OWL persona** (pragmatic senior engineer)
- **Current Runtime:** deepseek-v4-flash-free (opencode-zen) — _active primary_
- **Primary Config:** deepseek-v4-flash-free (opencode-zen)
- **Config:** `~/AppData/Local/hermes/config.yaml` (root = default profile)
- **Hooks (3, shared):** `session-logger`, `session-auto-commit`, `governance-audit`
- **Plugins (15 enabled):** `basic`, `copilot-provider`, `custom-provider`,
  `disk-cleanup`, `huggingface-provider`, `langfuse`, `nous`, `nous-provider`,
  `ollama-cloud-provider`, `openai-codex`, `openai-codex-provider`,
  `opencode-zen-provider`, `openrouter-provider`, `security-guidance`, `web-tavily`
- **Skills:** 373 available post-dedup (73 bundled + 216 community + 84 local)
- **MCP Servers (14 Configured):**
  - `ast-grep` — Code pattern searching (AST-based) via npx @notprolands/ast-grep-mcp
  - `code-sandbox` — Node.js code execution via npx node-code-sandbox-mcp
  - `codex` — Codex CLI integration via codex mcp-server
  - `copilot-mcp` — GitHub Copilot MCP via Python script
  - `fetch` — Web content fetching via npx mcp-server-fetch-typescript
  - `filesystem` — Project file access (sandboxed to C:/Users/Alexa) via npx @modelcontextprotocol/server-filesystem
  - `github` — GitHub API operations via npx @modelcontextprotocol/server-github
  - `linear` — Linear project management via OAuth (<https://mcp.linear.app/mcp>)
  - `mcp-docker` — Docker container management via docker mcp gateway (adminbot profile)
  - `memory` — Persistent memory backend via npx @modelcontextprotocol/server-memory
  - `mindstudio` — MindStudio integration via mindstudio mcp
  - `playwright` — Browser automation via npx @playwright/mcp@latest
  - `sequential-thinking` — Structured reasoning via npx @modelcontextprotocol/server-sequential-thinking
  - `smithery` — Smithery registry via OAuth (<https://mcp.smithery.run/rhixecompany>)

## Profile Inventory

| Profile                        | Model                  | Provider     | Purpose                                         |
| ------------------------------ | ---------------------- | ------------ | ----------------------------------------------- |
| **alexa** ⬤                    | deepseek-v4-flash-free | opencode-zen | System admin, operations — **currently active** |
| default                        | deepseek-v4-flash-free | opencode-zen | General purpose                                 |
| code-architect                 | deepseek-v4-flash-free | opencode-zen | Code changes, debugging, refactoring            |
| creative-director              | deepseek-v4-flash-free | opencode-zen | Design, content, creative tasks                 |
| exec-assistant                 | deepseek-v4-flash-free | opencode-zen | Administrative, planning, coordination          |
| patient-tutor                  | deepseek-v4-flash-free | opencode-zen | Explanations, tutorials, learning               |
| research-analyst               | deepseek-v4-flash-free | opencode-zen | Deep research, synthesis, documentation         |
| arch                           | —                      | —            | (unconfigured)                                  |
| architect                      | —                      | —            | (unconfigured)                                  |
| debugger                       | —                      | —            | (unconfigured)                                  |
| devops-expert                  | —                      | —            | (unconfigured)                                  |
| github-actions-expert          | —                      | —            | (unconfigured)                                  |
| hermes                         | —                      | —            | (unconfigured)                                  |
| implementation-plan            | —                      | —            | (unconfigured)                                  |
| mentor                         | —                      | —            | (unconfigured)                                  |
| planner                        | —                      | —            | (unconfigured)                                  |
| power-bi-data-modeling-expert  | —                      | —            | (unconfigured)                                  |
| prd                            | —                      | —            | (unconfigured)                                  |
| prompt-engineer                | —                      | —            | (unconfigured)                                  |
| qa-subagent                    | —                      | —            | (unconfigured)                                  |
| reviewer                       | —                      | —            | (unconfigured)                                  |
| specification                  | —                      | —            | (unconfigured)                                  |
| tanstack-start-shadcn-tailwind | —                      | —            | (unconfigured)                                  |
| terraform                      | —                      | —            | (unconfigured)                                  |

## Toolsets (18 Enabled)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`,
`moa`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`,
`clarify`, `delegation`, `cronjob`, `search`

## Provider Chain

| Provider     | Role                                    | Status     |
| ------------ | --------------------------------------- | ---------- |
| opencode-zen | Active primary (deepseek-v4-flash-free) | ✓ Active   |
| nous         | Fallback (stepfun/step-3.7-flash:free)  | ✓ In chain |
| openrouter   | Fallback (qwen/qwen3-coder:free)        | ✓ In chain |

## Environment Corrections (2026-06-21)

- **OS:** Windows 11 (not Windows 10)
- **Editor:** VS Code (not notepad)
- **Terminal:** VS Code Git Bash (bash via git-bash/MSYS)
