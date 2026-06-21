# 🏗️ PROJECT_RULES — SandBox Workspace Rules (Project-Specific)

> Workspace-specific rules for the SandBox project. These supplement the global MASTER_RULES.md.
> **DRY principle:** This file contains ONLY rules specific to this workspace. See `~/AppData/Local/hermes/MASTER_RULES.md` for global rules.

---

## Level 1: Session Lifecycle

| #   | Rule                                                                                                                                                                           |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | **Update SESSION_REPORT.md at session start and end** — Rolling summary with: session ID, timestamp, profile, model, work completed, tools/skills used, current state, result. |
| 2   | **Capture session metadata** — ID, timestamp, profile, model at session start.                                                                                                 |
| 3   | **After compaction** — Re-read SESSION_REPORT.md. Don't trust stale "Historical Task Snapshot" summaries. Verify current file state.                                           |
| 4   | **Session Startup (mandatory)** — Load 5 skills before any response: `/using-superpowers`, `/user-communication-preferences`, `/session-audit-report`, `/hermes-profiles`, `/validate-memories`. Verify all loaded. |
| 5   | **MCP First** — Use MCP server tools (filesystem, github, ast-grep, memory, playwright, sequential-thinking, cli, code-sandbox, fetch, mcp-docker, codex, copilot-mcp, mindstudio, smithery) before native equivalents. |
| 6   | **Profile Per Task** — Run `hermes profile use <name>` matching task type before execution (see Profile Routing table in `.hermes.md`).                                       |

## Level 2: Environment Facts (Verified)

| #   | Fact                                                                                                                                                                                             |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4   | **OS:** Windows 11 (not Windows 10)                                                                                                                                                              |
| 5   | **Editor:** VS Code (not notepad)                                                                                                                                                                |
| 6   | **Terminal:** VS Code Git Bash (bash via git-bash/MSYS) — POSIX syntax in terminal tool                                                                                                          |
| 7   | **Python:** python3=3.13.14, python=3.11.15, pip→python3.11, PEP 668=yes (use venv/uv), uv=installed                                                                                             |
| 8   | **Bun:** 1.3.14+ (primary JS/TS runtime)                                                                                                                                                         |
| 9   | **`.github/skills/` does NOT exist** — Community skills are reference-only                                                                                                                       |
| 10  | **Hermes root:** `~/AppData/Local/hermes/` (not `~/.hermes/`)                                                                                                                                    |
| 11  | **Default profile:** `default` at `~/AppData/Local/hermes` (root config.yaml), NOT `~/AppData/Local/hermes/profiles/default/`                                                                    |
| 12  | **Active profile:** `default` — Persona: OWL (pragmatic senior engineer)                                                                                                                         |
| 13  | **MCP servers:** 13 configured, all verified reachable                                                                                                                                           |
| 14  | **Hooks:** 3 active (session-logger, session-auto-commit, governance-audit)                                                                                                                      |
| 15  | **Plugins:** 15 enabled, 50+ disabled                                                                                                                                                            |
| 16  | **Skills:** 373 total (73 bundled + 216 community + 84 local)                                                                                                                                    |
| 17  | **Toolsets:** 18 enabled (web, browser, terminal, file, code_execution, vision, image_gen, moa, tts, skills, todo, memory, context_engine, session_search, clarify, delegation, cronjob, search) |
| 18  | **Provider chain:** openrouter (primary, qwen/qwen3-coder:free) → opencode-zen (fallback, nemotron-3-ultra-free) → openai-codex → nous → huggingface → ollama-cloud                            |

## Level 3: Profile Routing (Verified from config.yaml)

| Profile           | Model                     | Provider     | Purpose                                 |
| ----------------- | ------------------------- | ------------ | --------------------------------------- |
| **default** ⬤     | qwen/qwen3-coder:free     | OpenRouter   | General purpose — **currently active**  |
| alexa             | deepseek-v4-flash-free    | OpenRouter   | System admin, operations                |
| code-architect    | deepseek-v4-flash-free    | OpenRouter   | Code changes, debugging, refactoring    |
| creative-director | deepseek-v4-flash-free    | OpenRouter   | Design, content, creative tasks         |
| exec-assistant    | deepseek-v4-flash-free    | OpenRouter   | Administrative, planning, coordination  |
| patient-tutor     | deepseek-v4-flash-free    | OpenRouter   | Explanations, tutorials, learning       |
| research-analyst  | deepseek-v4-flash-free    | OpenRouter   | Deep research, synthesis, documentation |
