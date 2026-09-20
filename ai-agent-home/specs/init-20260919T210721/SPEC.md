---
name: init-all-agents-spec
title: "Spec — Enhance System-Prompts & Context Files for 5 Agents (Copilot, Hermes, OpenCode, Cursor, Agent)"
goal: Fresh-init enhancement of all 5 agents' system-prompt/context files, governed by specs/plans/prompts artifacts
version: 1.0
date_created: 2026-09-19
last_updated: 2026-09-19
owner: Alexa
status: "In progress"
tags: [init, agents, prompts, context-files, spec]
---

# Spec — /init for Copilot · Hermes · OpenCode · Cursor-agent · Agent

![Status: In progress](https://img.shields.io/badge/status-in%20progress-yellow)

Fresh init run. All decisions captured via clarify (12/12 answered over 4 rounds). Unified shared artifact set.

## 1. Requirements

- **REQ-001**: Enhance system-prompt + context files for ALL 5 agents: GitHub Copilot, Hermes, OpenCode, Cursor Agent, Agent (general).
- **REQ-002**: Fresh init — generate everything new; do not reuse prior runs (3 prior runs exist: 194300Z, 203754Z, 194800Z — left untouched).
- **REQ-003**: Artifacts live at `ai-agent-home/{specs,plans,prompts}/<unique-run>/` — run name `init-20260919T210721` (local WAT, user-chosen format).
- **REQ-004**: STATUS.md updated inside the artifact folder at each phase (spec → plan → prompts → implement → verified → completed).
- **REQ-005**: Begin every init with ask-all clarification (3 questions/turn via clarify) covering: new/old requests, remaining tasks, blockers, approval gates.
- **REQ-006**: Approval gates: user confirms plan BEFORE implementation; user confirms again before any commit/push.
- **REQ-007**: Carryover folded in: web-research-628 remaining batches (plan 5991 B) + adminbot profile MISSING (documented, not fabricated).
- **REQ-008**: All known blockers documented as risks (see Risks).
- **REQ-009**: Verify gate (full) before implementation: inspect existing agent/context files, validate JSON/YAML/frontmatter, confirm ai-agent-home state — DONE (evidence below).
- **REQ-010**: On completion: stop and report full summary (no commit/push unless separately gated).

## 2. Target Files (verified pre-state, 2026-09-19 21:07 WAT)

| #        | Agent           | File                              | Pre-size (B) | Action                                             |
| -------- | --------------- | --------------------------------- | ------------ | -------------------------------------------------- |
| FILE-001 | Agent (general) | `AGENTS.md`                       | 14280        | Enhance (append-init section, gate refs)           |
| FILE-002 | Hermes          | `.hermes.md`                      | 6094         | Enhance (init status, run ref)                     |
| FILE-003 | Cursor          | `.cursorrules`                    | 1370         | Enhance + keep `.cursor/rules/sandbox.mdc` in sync |
| FILE-004 | Copilot         | `.github/copilot-instructions.md` | present      | Enhance                                            |
| FILE-005 | OpenCode        | `opencode.json`                   | **MISSING**  | Create (config + instructions ref)                 |
| FILE-006 | OpenCode        | `opencode.md`                     | **MISSING**  | Create (agent instructions)                        |
| FILE-007 | Claude pointer  | `CLAUDE.md`                       | 992          | Enhance (thin pointer + init ref)                  |

> `ai-agent-home/` pre-state verified: exists, 3 prior run dirs under specs/, plans/, prompts/. New run dir created fresh.

## 3. Constraints

- **CON-001**: `.env` protected — never read/print/modify; sizes recorded: workspace 5274 B, hermes 30269 B (verify unchanged at gates).
- **CON-002**: DRY — identity → SOUL.md/profile dirs; prefs → `user-communication-preferences`; protocol → `multi-file-change-protocol`; reference, never duplicate.
- **CON-003**: No synthetic artifacts — every claimed size/exit code must be observed.
- **CON-004**: 0 new `.bak`; no destructive ops; no commit/push without gate.
- **CON-005**: Keep existing content & identity; enhance by appending/referencing, not rewriting ownership.
- **GUD-001**: Follow create-implementation-plan identifier rules (unique declarations).
- **GUD-002**: Match repo conventions (tabs/2, lf, markdownlint-cli2, pre-commit: lint → typecheck → format:check → markdownlint → spellcheck).
- **GUD-003**: Verification-first — run validators after every implementation step.

## 4. Acceptance Criteria

- **AC-001**: All 7 target files present with verified sizes/diffs; opencode.json + opencode.md created and JSON-valid.
- **AC-002**: `ai-agent-home/{specs,plans,prompts}/init-20260919T210721/` contains SPEC.md, PLAN.md, PROMPTS.md, STATUS.md.
- **AC-003**: STATUS.md reflects phase progression and ends at `Completed`.
- **AC-004**: SPEC.md, PLAN.md, PROMPTS.md all marked Completed with 0 placeholder text.
- **AC-005**: All 5 agents' system-prompt/context files reference this run's artifacts (DRY pointer).
- **AC-006**: Blockers documented (web-research-628, adminbot MISSING, MSYS2 FAIL, rate-limit 403, vision REJECTS, 26 vulns, 41 parse errors).
- **AC-007**: Final report delivered; no commit/push performed.

## 5. Risks & Assumptions

- **RISK-001**: adminbot profile MISSING (carryover) — documented; no fabrication of its identity files.
- **RISK-002**: web-research-628 remaining — future batches 23–628 NOT executed this run (requires new clarification).
- **RISK-003**: MSYS2 FAIL (env) — preserved; may affect validators → use python/bun fallbacks.
- **RISK-004**: Rate-limit 403 possible on web/provider calls — bounded retries, honest reporting.
- **RISK-005**: Vision primary REJECTS — vision_analyze fallback via mindstudio/OpenRouter nano-vl.
- **RISK-006**: 26 vulnerabilities + 41 parsing errors preserved — not fixed/not hidden this run.
- **ASSUMPTION-001**: Repo root = `C:/Users/Alexa/Desktop/SandBox`; git branch clean-development; auth FULL (destructive approved, but run is non-destructive).
- **ASSUMPTION-002**: Prior 3 init runs remain canonical history; this run does not overwrite them.

## 6. Related Artifacts

- PLAN: `ai-agent-home/plans/init-20260919T210721/PLAN.md`
- PROMPTS: `ai-agent-home/prompts/init-20260919T210721/PROMPTS.md`
- STATUS: `ai-agent-home/{specs,plans,prompts}/init-20260919T210721/STATUS.md`
