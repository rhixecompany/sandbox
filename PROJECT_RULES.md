# 🏗️ PROJECT_RULES — SandBox Workspace Rules (Project-Specific)

> Workspace-specific rules for the SandBox project. These supplement the global MASTER_RULES.md.
> **DRY principle:** This file contains ONLY rules specific to this workspace. See `~/AppData/Local/hermes/MASTER_RULES.md` for global rules.

---

## Level 1: Session Lifecycle

| # | Rule |
|---|------|
| 1 | **Update SESSION_REPORT.md at session start and end** — Rolling summary with: session ID, timestamp, profile, model, work completed, tools/skills used, current state, result. |
| 2 | **Capture session metadata** — ID, timestamp, profile, model at session start. |
| 3 | **After compaction** — Re-read SESSION_REPORT.md. Don't trust stale "Historical Task Snapshot" summaries. Verify current file state. |

## Level 2: Environment Facts (Verified)

| # | Fact |
|---|------|
| 4 | **OS:** Windows 11 (not Windows 10) |
| 5 | **Editor:** VS Code (not notepad) |
| 6 | **Terminal:** VS Code Git Bash (bash via git-bash/MSYS) — POSIX syntax in terminal tool |
| 7 | **Python:** python3=3.13.14, python=3.11.15, pip→python3.11, PEP 668=yes (use venv/uv), uv=installed |
| 8 | **Bun:** 1.3.14+ (primary JS/TS runtime) |
| 9 | **`.github/skills/` does NOT exist** — Community skills are reference-only |
| 10 | **Hermes root:** `~/AppData/Local/hermes/` (not `~/.hermes/`) |
| 11 | **Active profile:** `default` — Persona: OWL (pragmatic senior engineer) |
| 12 | **MCP servers:** 11 configured, all verified reachable |
| 13 | **Hooks:** 3 active (session-logger, session-auto-commit, governance-audit) |
| 14 | **Plugins:** 15 enabled, 50+ disabled |
| 15 | **Skills:** 373 total (73 bundled + 216 community + 84 local) |
| 16 | **Toolsets:** 18 enabled (web, browser, terminal, file, code_execution, vision, image_gen, moa, tts, skills, todo, memory, context_engine, session_search, clarify, delegation, cronjob, search) |
| 17 | **Provider chain:** openai-codex (primary) → opencode-zen (fallback) → openrouter → nous |
