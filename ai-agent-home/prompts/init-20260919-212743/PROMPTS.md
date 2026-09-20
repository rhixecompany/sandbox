---
name: init-all-agents-prompts
title: "Prompts — /init enhancements for Copilot, Hermes, OpenCode, Cursor-agent, Agent"
version: 1.0
date_created: 2026-09-19
last_updated: 2026-09-19
owner: Alexa
status: "In progress"
tags: [init, prompts, agents]
---

# PROMPTS.md — Enhancement Prompts (init-20260919-212743)

![Status: In progress](https://img.shields.io/badge/status-in%20progress-yellow)

One shared prompt set for all 5 agents (unified structure per user decision). Each prompt targets ONE file; all must preserve existing identity/content and add DRY pointers + init-run refs only. No synthetic claims. `.env` never exposed.

## Shared Ground Rules (apply to every prompt below)

1. Preserve all existing content; append/enhance, never rewrite ownership sections.
2. Add a clear `## Init Run 2026-09-19 (init-20260919-212743)` block per file with: run id, artifact paths, STATUS pointer.
3. Reference (never duplicate): `user-communication-preferences`, `multi-file-change-protocol`, identity via profile dirs / `AGENTS.md`.
4. Keep blockers honest: web-research-628 remaining, adminbot MISSING, MSYS2 FAIL, rate-limit 403, vision REJECTS, 26 vulns, 41 parse errors — as risks, not resolutions.
5. Match repo style: tabs, LF, markdownlint-clean.

---

## PROMPT-001 — Agent general → `AGENTS.md`

Role: senior engineer. Add section `## Init Run 2026-09-19 (init-20260919-212743)` listing: fresh-init status, artifact pointers (specs/plans/prompts/STATUS), clarification summary (5 agents, fresh init, carryover web-research-628 + adminbot MISSING), gate rules (plan approval before implementation; commit/push needs approval). Update the Agent Integration Contract table row for Hermes/OpenCode only if needed — otherwise append. Do NOT touch: Honcho peer card, blockers list, safety boundaries.

## PROMPT-002 — Hermes → `.hermes.md`

Role: Hermes context maintainer. Append `## Init Run 2026-09-19 (init-20260919-212743)` — run id, artifact pointers, status=In progress (phase-gated), note that this file's routing/identity tables are untouched. Add to Session Evidence: this init run (verified sizes: 7 target files). Keep DRY.

## PROMPT-003 — Cursor Agent → `.cursorrules` + `.cursor/rules/sandbox.mdc`

Role: Cursor rules author. Keep `.cursorrules` thin (1370 B pre-state): append short init block (run id + artifact pointer). Keep parity with `.cursor/rules/sandbox.mdc` (single source of truth stays `.cursorrules`, per AGENTS.md contract). No rule changes — context additions only.

## PROMPT-004 — GitHub Copilot → `.github/copilot-instructions.md`

Role: Copilot instruction author. Append `## Init Run 2026-09-19 (init-20260919-212743)`: read order unchanged (this file → nearest AGENTS.md), artifact pointers, note that `.github/prompts/` (14 groups) remains canonical prompt library. Preserve all existing instructions.

## PROMPT-005 — OpenCode → `opencode.json` + `opencode.md` (both MISSING — create)

Role: OpenCode bootstrap. Create:

- `opencode.json`: minimal valid JSON `{ "instructions": "opencode.md", "$schema": "https://opencode.ai/config.json" }` (no provider keys — vault handles).
- `opencode.md`: agent instructions — identity (Alexa, SandBox), read AGENTS.md first, work loop, safety boundaries, blockers (honest), init-run artifact pointers, gate rules.
  Requirement: `python -c "import json; json.load(...)"` must pass.

## PROMPT-006 — Claude pointer → `CLAUDE.md`

Role: thin-pointer maintainer. Append init block: run id + artifact pointer + status. Keep file thin (<1.5 KB after edit); full identity stays in `AGENTS.md`/profile dirs.

---

## Execution order (sequential, one file at a time)

1. PROMPT-001 AGENTS.md → 2. PROMPT-002 .hermes.md → 3. PROMPT-003 .cursorrules + sandbox.mdc → 4. PROMPT-004 copilot-instructions.md → 5. PROMPT-005 opencode.json + opencode.md → 6. PROMPT-006 CLAUDE.md → 7. Run Phase-3 verify → 8. Complete.

## Verification after each prompt

- File exists + size recorded; JSON valid (opencode.json); markdownlint-clean; no `.env` touched; diff limited to intended file.
