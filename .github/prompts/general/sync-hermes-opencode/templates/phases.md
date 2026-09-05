# Sync Hermes OpenCode — Phase Instructions

> Extracted from `sync-hermes-opencode.prompt.md`. One platform at a time; each phase must pass its gate before advancing.

## Phase 1 — Inventory Instructions & Agents

- Inventory instructions (AGENTS.md/CLAUDE.md/.cursorrules/personality files) and agent definitions across Hermes, Codex, OpenCode.
- **Gate**: inventories complete; personality/profile mappings created.

## Phase 2 — Identify Agent Roots

- Confirm roots:
  - Hermes → `~/AppData/Local/hermes/` (skills/, plugins/, hooks/, profiles/)
  - OpenAI Codex → `~/.codex/` (agents/*.toml, skills/)
  - OpenCode → `~/.opencode/` (config) and workspace `opencode.json`
- **Gate**: all 3 roots confirmed; paths documented.

## Phase 3 — Bidirectional Sync

- Sync skills, plugins, hooks, prompts, agents, instructions. Resolve or document conflicts (never silently drop).
- **Gate**: sync report written; conflicts resolved or documented.

## Phase 4 — Verify Completion

- Run verification checklist; confirm all critical assets in sync.
- **Gate**: verification report written; all critical assets in sync.

## Rules

- No backup files — use git history for rollback; never `.bak`/`.old`/timestamped copies.
- Execute phases in order; do not reorder.

---

> TODO-to-author: extend with exact per-asset sync commands when the mirror script set stabilizes.
