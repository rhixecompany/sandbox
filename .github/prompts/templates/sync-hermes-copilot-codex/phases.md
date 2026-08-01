# Sync Hermes Copilot Codex OpenCode — Phases

> Full operational phases for `prompts/sync-hermes-copilot-codex.prompt.md`.

## Phase 1: Inventory Instructions & Agents

- Inventory instruction/agent artifacts across Hermes, Copilot, Codex, and OpenCode.
- Gate: inventories complete; personality/profile mappings created.

## Phase 2: Identify Agent Roots

- Confirm canonical roots for Hermes (`~/AppData/Local/hermes/`), Copilot (`.github/`),
  Codex (`~/.codex/`), and OpenCode (`~/.opencode/` + workspace `opencode.json`).
- Gate: all 4 roots confirmed; paths documented.

## Phase 3: Bidirectional Sync

- Sync skills, plugins, hooks, prompts, agents, and instructions.
- OpenCode: sync skills/agents into `~/.opencode/` or workspace `.opencode/`; verify
  `opencode.json` config; keep `~/.opencode/bin/opencode` intact (never overwrite the CLI).
- Gate: sync report written; conflicts resolved or documented.

## Phase 4: Verify Completion

- Verify critical assets are in sync and review exceptions.
- Gate: verification report written; all critical assets in sync.

## Completion

- Append progress after each phase.
- Append evidence to `docs/orchestrator-verification.md` after each phase.
