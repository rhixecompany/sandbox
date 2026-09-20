---
profile: default
version: 1.0.0
alias: default (workspace default; routing: general→default, user→default)
canonical_profile_root: ~/AppData/Local/hermes/profiles/default/
workspace: ~/Desktop/SandBox (rhixecompany/sandbox)
verified: 2026-09-20
identity_preserved: true
dry_ref: .hermes.md (6691 B verified) / AGENTS.md (17041 B verified) / user-communication-preferences SKILL.md
---

# SOUL.md — Workspace Mirror + Agent Catalog (Refactored 2026-09-20)

> **Identity Protocol Ref** (verified 2026-09-20): This file references `identity-context-protocol` SKILL.md (created at $HERMES_HOME/skills/development/identity-context-protocol/SKILL.md, 6876 B). DRY enforced: do not duplicate identity/protocol/routing content; reference skills/files instead.
> **Best practices applied**: concise bullets + table-first + emoji + direct; verification before claim; honest blocker reporting; no synthetic artifacts.
> **.env protection**: 30501 B (verified); never read/printed/committed.
> **Protocol skills verified**: `multi-file-change-protocol` + `multi-file-crud-protocol` (installed, SKILL.md present).

**Canonical identity**: `C:\Users\Alexa\AppData\Local\hermes\SOUL.md` (refactored 2026-09-20: 35745 B → 12156 B, deduped; all rules + evidence preserved). This workspace file is a thin mirror + cross-agent catalog — DRY, no rule duplication.

**Routing (live-verified 2026-09-20)**: code→architect | research→analyst | design→creative | planning→exec-assistant | teaching→tutor | ops→adminbot | general→default | user→default. (Fixed in `config.yaml` — dead refs `ops: alexa`, `planning: exec` removed.)

**Identity DRY refs**:

- Profile identity rules → `.hermes.md` (workspace overrides) | Preferences → `user-communication-preferences` SKILL.md | Protocol → `multi-file-change-protocol` SKILL.md | Debugging → `systematic-debugging` SKILL.md.

## Workspace Context (verified 2026-09-20)

- Repo: `rhixecompany/sandbox` (`clean-development`; git clean at session start, auto-commits by session hooks)
- Agent framework artifacts: `.github/prompts/` (large prompt library, verif-registered), `.github/agents/`, `agents/` (30 `.agent.md`), `.cursor/rules/sandbox.mdc` (1204 B), `.hermes.md` (6691 B), `opencode.md` (3233 B), `copilot-instructions.md` (585 B) → `.github/copilot-instructions.md` (9159 B), `AGENTS.md` (17041 B), `CLAUDE.md` (1150 B), `.cursorrules` (1844 B), workspace `config.yaml` (1771 B, routes fixed), `.opencode/opencode.json` (467 B — CREATED 2026-09-20)
- `docs/user-guide/`: 14 real .md (411–108621 B); 3 markdown warnings preserved (NOT hidden)
- `ai-agent-home/`: canonical run `init-20260919-212743` (SPEC 6149 B / PLAN 6126 B / PROMPTS 4109 B); older runs T194300Z/T203754Z/T210721 + design-md run — consolidation future work
- `.hermes/{plans,specs}` evidence: debug-run-logs.md (53152 B — 14 real exit codes), skill-verification-evidence.md (2658 B — 28 skills), exposure-correction.md (1333 B), debug-analysis-2026-09-13.md (6081 B — 4 failure classes), debug-subgoal-plan-2026-09-13.md (4340 B), web-research-628-batch-execution-plan.md (5991 B — 623 batches future, NOT executed, requires new clarification)

## Compulsory Rules (6 — compressed; full evidence in canonical SOUL.md)

1. > 5-file trigger → 14-skill stack + SPEC/PLAN/PROMPTS at $HERMES_HOME/{specs,plans,prompts}/<slug>/ (this run: context-refactor-2026-09-20)
2. DRY/Direct/Table-first: concise bullets + table-first + emoji + direct; verification before claim; honest blockers; no synthetic
3. Security preservation: 26 vulns (fastmcp CRITICAL, httpx2 HIGH, OAuth HIGH) + 41 parse errors (nested .codex/.copilot; .eslintrc.json 69 B fix, ruff+py_compile PASS) + rate-limit 403 + MSYS2 FAIL + adminbot profile-docs gap — ALL preserved
4. Profile identity DRY: identity→SOUL.md; prefs→skill; protocol→skill; routing→.hermes.md/config.yaml; 14 profiles verified 2026-09-14, 15 live 2026-09-20
5. Session achievements real: .hermes/{plans,specs} + docs/user-guide/ + .eslintrc.json — verified sizes/exit codes; 0 synthetic
6. .env protection: 0 reads/writes/commits; size-references only (3334 B 2026-09-14 ref → workspace 5274 B ref → hermes home 30504 B 2026-09-20); exposure-correction documented (API_KEY=vault = vault handle ref)

## Agent-Context Status (triaged 2026-09-20 — all 5 present; created if missing)

| Agent     | File                       | Status      | Action this run                      |
| --------- | -------------------------- | ----------- | ------------------------------------ |
| Hermes    | $HERMES_HOME/SOUL.md       | ✓ canonical | REFACTORED 35745→12156 B             |
| Hermes    | memories/USER.md           | ✓           | UPDATED (1912 B)                     |
| Hermes    | memories/MEMORY.md         | ✓           | CONSOLIDATED (5769 B)                |
| Hermes    | .hermes.md (workspace)     | ✓           | routing table → live 15              |
| Copilot   | copilot-instructions.md    | ✓           | pointer OK; adapter 9159 B READ      |
| OpenCode  | opencode.md                | ✓           | blockers refreshed; config ref fixed |
| OpenCode  | .opencode/opencode.json    | MISSING     | **CREATED** (467 B, lint OK)         |
| Cursor    | .cursorrules + sandbox.mdc | ✓           | verified                             |
| Claude    | CLAUDE.md                  | ✓           | thin pointer OK                      |
| Agent lib | agents/*.agent.md (30)     | ✓           | verified                             |

## Integrity (2026-09-14 GATE-A→F PASS; re-verified 2026-09-20)

0 synthetic artifacts; 0 hidden errors; .env untouched; 0 new .bak created by sessions; stale `~/` dir + 5 memory `.bak` DELETED (user-approved 2026-09-20); identity preserved; verified PASS.

**Status**: REFACTORED / VERIFIED 2026-09-20 (canonical deduped; catalog refreshed; live-state verified; 0 synthetic; .env untouched).
