---
title: "Tree Prompt"
description: "Converted from tree.prompt.txt — structured tree of goals, skills, and operations for multi-file change protocol, cleanup, and systematic debugging."
category: "general"
trigger: "init-run"
profile: "default"
mode: "best"
source_file: "tree.prompt.txt"
source_size_bytes: 6165
---

# Tree Prompt

Converted from `tree.prompt.txt` (6,165 B) via `/convert-plaintext-to-md`.

## Core Skill Stack (used sequentially in best order)

/goal /using-superpowers /brainstorming /user-communication-preferences /mcp-sequential-thinking /mcp-filesystem /mcp-ast-grep /mcp-memory /writing-clearly-and-concisely /subagent-driven-development /plan /plan-mode /plans-and-specs /create-implementation-plan /update-implementation-plan /implementation-plan /execute-implementation-plan /executing-plans /create-implementation-spec /update-implementation-spec /implementation-spec /execute-implementation-spec /executing-specs /create-implementation-prompt /update-implementation-prompt /implementation-prompt /execute-implementation-prompt /executing-prompts

Begin by using the `clarify` tool to ask all unknown, confusing, needed questions about the goal and subgoal. Then close any remaining open items. Use all available Hermes tools (approved on all destructive operations). Include steps, phases, rules, tasks, actions, timelines, milestones, and resource allocation.

## Cleanup Goals (structured tree)

- Delete and cleanup `.enhance`, `.goals`, `$HERMES_HOME_diagnostics`, `.mcp`, `.*_cache`, `.worktrees`, `hermes-memory-safety`, `judge_results`, `logs`, `session-state`, `thoughts` folders.
- Search, delete, and cleanup `*.json`, `*-report.md` files except for `package.json`, `pyrightconfig.json`.
- Update, refactor, and verify `.editorconfig`, `.git-blame-ignore-revs`, `.gitattributes`, `.gitignore`, `.gitmodules`, `.markdownlint-cli2.jsonc`, `.markdownlint.jsonc`, `.pre-commit-config.yaml`, `.prettierignore`, `.prettierrc.json`, `*.toml`, `*.yaml`.
- Search, delete, and cleanup `*.log`, `*.txt` (skip `*.prompt.txt` files).
- Convert, update, refactor, and verify `*.mjs` files into `.mts` files.
- Cleanup, update, refactor, and verify `*.md` files including `PLAN.md`, `SOUL.md`, `SPEC.md`, `USER.md` and all files in `docs` and subdirectories.
- Update, refactor, and verify `*.py`, `*.mjs`, `*.mts` files; create `src` directory and migrate files into `src` and subdirectories (`main.py`, all `.py` files).
- Update, refactor, and verify `requirements.txt`, `tsconfig.json`.
- Update, refactor, and verify `.markdownlint-cli2.jsonc`, `.markdownlint.jsonc`, `.pre-commit-config.yaml`, `.prettierignore`, `.prettierrc.json` files; create `.mts` files.
- Update, refactor, and verify `package.json`, `pyrightconfig.json`, `*.json` files.

## Systematic Debug + Implementation Pipeline

- Start by using `clarify` to ask all blockers, unknowns, confusing items, recommendations, and optional questions about user input, request, query, tasks, goal, and subgoal (2 questions per turn; ask all even across multi-turns).
- Only when all questions are answered: create/update/verify valid specs, plans, prompts, scripts, skills that fully implement, execute, verify the user input/request/task/goal/subgoal.
- Delegate to subagent passing all needed data and context; ask user for best/fastest/worst implementation order.
- Continue by validating all artifacts; request approvals on all CRUD operations; use all available Hermes tools to CRUD specs/plans/prompts/skills/scripts.
- Use `/honcho` for the user input/request/query/task/goal/subgoal.
- Enforce rules: valid goals, subgoals, todos, steps, phases, rules, tasks, actions, timelines, gates, checklist, milestones, personas, profile, personality, model, resource allocation.

## Specific Operations

- `cd ../../AppData/Local/Hermes/hermes-agent`
- Apply stashes: `git stash apply hermes-update-autostash-20260905-011604`, `hermes-update-autostash-20260828-151448`, `hermes-update-autostash-20260804-191747`, `hermes-update-autostash-20260728-015200`
- `/systematic-debugging`: debug, fix, test browser tools (timing out); audit `config.yaml` for conflicts; debug and fix conflicts.
- Web search / web extract: fetch `https://openrouter.ai/models?variant=free`; output markdown report; convert HTML page to markdown; write `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md`.
- `/mcp-tavily` / `/mcp-parallel-search` / `/mcp-fetch`: web-research-pipeline / repo-research-pipeline for best practices for `opencode-free` and `opencode-zen` provider; `/test-providers-models` on each model.
- Get all configured environment variables and update all files that need/don't have environment variables in this repo and `../../AppData/Local/Hermes`.
- Use `.github/prompts/general/run-all-goals/run-all-goals-five-day.prompt.md` to create `run-today-and-yesterday.prompt.md` at general category (get all today and yesterday sessions: initial query, user input, goals, subgoals, clarifying questions/answers; retry intelligently).

---
*Identity preserved: DRY enforced; never expose `.env` secrets; never duplicate identity rules across profile docs; verification before claim; honest blocker reporting; enhanced per brand-guidelines.*

## Verification Checklist

- [x] Skill stack verified (`/using-superpowers` → `/writing-{spec|plan|prompt}`).
- [x] Cleanup goals defined (`.enhance`, `.goals`, `.worktrees`, caches, logs, reports).
- [x] Systematic debug pipeline (clarify → validate → execute → verify) included.
- [x] Multi-file-change-protocol and judgment gates referenced.
- [x] Environment variables and stash operations documented.
- [x] No `.env` secrets exposed; identity DRY preserved.
