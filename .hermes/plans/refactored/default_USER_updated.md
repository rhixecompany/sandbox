---
user: Alexa
---

# USER.md — default profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity

- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: default

## Environment Stack

- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint

## Model

- nemotron-3-ultra-free (opencode-zen) [primary]
- deepseek-v4-flash-free (opencode-zen) [fallback]

## Execution Preferences

- Communication: concise bullets, lead with result, skip fluff
- Code: TypeScript strict, JSDoc/docstring _why_ not _what_
- Skills: structured SKILL.md (YAML frontmatter + md body)
- Hooks: ruff format+check --fix pre-commit
- Execution: read→patch→verify, MCP-first, no backup files

## Profile Routing

| Task Type | Profile |
|-----------|---------|
| Code implementation, debugging, refactoring | `code-architect` |
| Deep research, literature review, synthesis | `research-analyst` |
| Design, content creation, brainstorming | `creative-director` |
| Planning, coordination, admin | `exec-assistant` |
| Tutorials, explanations, teaching | `patient-tutor` |
| System operations, DevOps, infra | `adminbot` |
| General purpose | `default` |

Run `hermes profile use <name>` matching task type BEFORE execution.

## Standing Goal

Maintain/enhance .github/prompts/ with DRY, structural sections. Stacked
bundles: using-superpowers, subagent-driven-development, brainstorming.

## Multi-File Change Protocol (≥3 files)

When >3 files modified, agent MUST load 14 skills: /using-superpowers
/brainstorming /user-communication-preferences /mcp-sequential-thinking
/mcp-filesystem /mcp-ast-grep /mcp-memory /plan /plans-and-specs
/create-implementation-plan /implementation-plan /executing-plans
/writing-clearly-and-concisely /subagent-driven-development Protocol: Load
skills → create plan → verify → execute → verify gates.

## Honcho Memory

Active (hybrid mode). Use honcho_profile/context/reasoning/search. Interests:
motorcycles (Harley Sportster 1200), family travel (Air Peace PNR 1J9A2F). Repo:
rhixecompany/sandbox. Prompt quality: comprehensive, best practices, all
MCP/skills.

## Session Info

Conversation started: Tuesday, September 08, 2026 (Africa/Lagos, WAT, UTC+01:00)
Model: nemotron-3-ultra-free
Provider: opencode-zen
Platform: tui


--- ENHANCEMENT (feature-doc synthesis applied to profile identity, DRY, verified) ---
## Feature-Integrated Preferences (from verified docs/features/*.md)
- Communication: concise, direct, no filler; lead with result; verification before claim (from overview.md + SOUL.md rules).
- Memory use: save durable facts (§-delimited, bounded 2200 chars in MEMORY.md); skip temporary/task-progress/logs (per memory.md save/skip rules); session DB truth over synthetic IDs.
- Skills: use structured SKILL.md (YAML frontmatter + body >=10 lines) with progressive disclosure; apply security gate (dangerous-findings / quarantine); approve/reject/diff workflow.
- Tools: prefer MCP-first for external integrations; use native equivalents when profile skills unavailable (honest blocker reporting); multi-category awareness (browser/media/file/search/orchestration/memory).
- Gateway: access image generation via gateway (FLUX/FLUX Pro/Z-Image/Nano Banana Pro/GPT Image/Ideogram/Recraft/Qwen); provider-independent endpoints; TTS/text-to-speech available.
- Kanban/Orchestration: parallel-ready design; collision awareness; run tracking; sequential gate verification.
- Hooks: deterministic, lightweight, non-blocking; session/task/turn/model/platform context available; append-only state logs; no synthetic lifecycle injection.
- Profile routing (DRY): default/architect/analyst/creative/exec/tutor/adminbot — customized only at routing/mapping level, shared identity at core.
- Blocker reporting: after 2 failures, report honestly; never fabricate success (SOUL.md + feature-doc verification rules).
