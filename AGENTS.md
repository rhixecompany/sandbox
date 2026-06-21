# SandBox Context

Automation scripts, prompt assets, and 15+ subprojects.

## Structure

- `Bash/` — primary toolkit (Bun, TypeScript, shell)
- `projects/` — per-project workspaces
- `docs/` — extracted Hermes docs
- `.github/` — Copilot config, prompts, hooks (no skills directory)

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

### 4. Scripts (Python, JavaScript, TypeScript)

- **NEVER run inline scripts** — no inline Python, JavaScript, or TypeScript
- Create permanent scripts under `C:/Users/Alexa/AppData/Local/hermes/scripts/`
- Execute from there; debug and rerun until clean; keep for reuse
- If updating an existing file, always first read the file and update it using the patch tool with correct context and line number

## Notes

- Never commit secrets, tokens, or `.env`
- Update `SESSION_REPORT.md` on session start/end; rolling 5-session summary
- Toolchain: `python3=3.13.14`, `python=3.11.15`, `pip→python3.11`
- Active ecosystem audit plan: `.hermes/plans/2026-06-16_eco-system-audit-plan.md`

## Hermes Config (Current)

- **Active Profile:** `default` — **gpt-5.4-mini (openai-codex)**
- **Config:** `C:\\Users\\Alexa\\AppData\\Local\\hermes\\config.yaml`
- **Hooks (3, shared):** `session-logger`, `session-auto-commit`, `governance-audit`
- **Plugins (15 enabled):** `basic`, `copilot-provider`, `custom-provider`, `disk-cleanup`, `huggingface-provider`, `langfuse`, `nous`, `nous-provider`, `ollama-cloud-provider`, `openai-codex`, `openai-codex-provider`, `opencode-zen-provider`, `openrouter-provider`, `security-guidance`, `web-tavily`
- **Skills:** 373 available post-dedup (73 bundled + 216 community + 84 local)
- **MCP Servers (11):** `ast-grep`, `code-sandbox`, `fetch`, `filesystem`, `github`, `linear` (disabled), `mcp-docker`, `memory`, `playwright`, `sequential-thinking`, `cli` (built-in)

## Profile Inventory

| Profile | Model | Provider | Purpose |
|---------|-------|----------|---------|
| **default** ⬤ | gpt-5.4-mini | openai-codex | General purpose — **currently active** |
| adminbot | nemotron-3-ultra-free | opencode-zen | System admin, operations |
| code-architect | nemotron-3-ultra-free | opencode-zen | Code changes, debugging, refactoring |
| creative-director | nemotron-3-ultra-free | opencode-zen | Design, content, creative tasks |
| exec-assistant | nemotron-3-ultra-free | opencode-zen | Administrative, planning, coordination |
| patient-tutor | nemotron-3-ultra-free | opencode-zen | Explanations, tutorials, learning |
| research-analyst | nemotron-3-ultra-free | opencode-zen | Deep research, synthesis, documentation |

## Toolsets (21 Enabled)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `moa`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`, `search`

## Provider Chain

| Provider | Role | Status |
|----------|------|--------|
| openai-codex | Active primary (gpt-5.4-mini) | ✓ Configured |
| opencode-zen | Fallback (nemotron-3-ultra-free, nemotron-3-super-free) | ✓ In fallback chain |
| openrouter | Available via plugin | ✓ Enabled |
| nous | Available via plugin | ✓ Enabled |

## Environment Corrections (2026-06-21)

- **OS:** Windows 11 (not Windows 10)
- **Editor:** VS Code (not notepad)
- **Terminal:** VS Code Git Bash (bash via git-bash/MSYS)