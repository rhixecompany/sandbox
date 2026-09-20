---
goal: "Init all 5 agents — enhance system-prompt & context files with governed artifacts"
version: 1.0
date_created: 2026-09-19
last_updated: 2026-09-19
owner: Alexa
status: "In progress"
tags: [init, implementation-plan, agents]
---

# Implementation Plan — init-20260919T210721

![Status: In progress](https://img.shields.io/badge/status-in%20progress-yellow)

Fresh-init enhancement of agent system-prompts + context files for GitHub Copilot, Hermes, OpenCode, Cursor Agent, and Agent (general), per clarification rounds 1–4 (12/12 answered). Artifacts co-located at `ai-agent-home/{specs,plans,prompts}/init-20260919T210721/`.

## 1. Requirements & Constraints

- **REQ-001** … **REQ-010**: see SPEC.md §1 (all carried by reference; identifiers declared once there).
- **CON-001** … **CON-005**, **GUD-001** … **GUD-003**: see SPEC.md §3.

## 2. Implementation Steps

### Implementation Phase 1 — Author artifacts (status: DONE with these writes)

- GOAL-001: Write SPEC.md, PLAN.md, PROMPTS.md, STATUS.md into the run folder.

| Task     | Description                                                                        | Completed | Date       |
| -------- | ---------------------------------------------------------------------------------- | --------- | ---------- |
| TASK-001 | Verify gate — inventory 5 agents' files, validate JSON/YAML, confirm ai-agent-home | ✅        | 2026-09-19 |
| TASK-002 | Author SPEC.md (requirements, files, risks, acceptance criteria)                   | ✅        | 2026-09-19 |
| TASK-003 | Author PLAN.md (this file, phases + gates)                                         | ✅        | 2026-09-19 |
| TASK-004 | Author PROMPTS.md (per-agent enhancement prompts)                                  | ✅        | 2026-09-19 |
| TASK-005 | Write STATUS.md (phase tracking)                                                   | ✅        | 2026-09-19 |

### Implementation Phase 2 — Plan-approval gate

- GOAL-002: Obtain explicit user approval of the plan before touching repo files.

| Task     | Description                                                  | Completed | Date |
| -------- | ------------------------------------------------------------ | --------- | ---- |
| TASK-006 | Clarify gate: user approves plan → proceed to implementation |           |      |

### Implementation Phase 3 — Enhance 5 agents' files (sequential, one variable at a time)

- GOAL-003: Apply enhancements exactly per PROMPTS.md, preserving existing content/identity; DRY references only.

| Task     | Description                                                                       | Completed | Date |
| -------- | --------------------------------------------------------------------------------- | --------- | ---- |
| TASK-007 | AGENTS.md (Agent general) — append init section, run-artifact pointers, gate refs |           |      |
| TASK-008 | .hermes.md (Hermes) — init run status refs; identity/routing untouched            |           |      |
| TASK-009 | .cursorrules (Cursor) + sync `.cursor/rules/sandbox.mdc`                          |           |      |
| TASK-010 | .github/copilot-instructions.md (Copilot) — init context + artifact pointers      |           |      |
| TASK-011 | Create opencode.json (config + instructions) and opencode.md (agent prompt)       |           |      |
| TASK-012 | CLAUDE.md (Claude pointer) — thin init ref                                        |           |      |

### Implementation Phase 4 — Verify

- GOAL-004: Run full verification: JSON/YAML validity, markdownlint, sizes, .env integrity, identifier-uniqueness checks.

| Task     | Description                                                          | Completed | Date |
| -------- | -------------------------------------------------------------------- | --------- | ---- |
| TASK-013 | `python json.load` opencode.json + all touched configs               |           |      |
| TASK-014 | markdownlint-cli2 on touched .md (`bun run markdownlint` scope)      |           |      |
| TASK-015 | File sizes/diffs recorded; `.env` 5274 B/30269 B unchanged; 0 `.bak` |           |      |
| TASK-016 | STATUS.md → Verified across specs/plans/prompts                      |           |      |

### Implementation Phase 5 — Complete

- GOAL-005: Mark all artifacts Completed; report summary; NO commit/push (gate pending).

| Task     | Description                                      | Completed | Date |
| -------- | ------------------------------------------------ | --------- | ---- |
| TASK-017 | SPEC/PLAN/PROMPTS frontmatter status → Completed |           |      |
| TASK-018 | STATUS.md → Completed; final integrity check     |           |      |
| TASK-019 | Deliver final summary to user (stop and report)  |           |      |

## 3. Alternatives

- **ALT-001**: Per-agent subfolders — rejected (user chose unified shared set).
- **ALT-002**: Reuse `.hermes/plans|specs|prompts` dirs — rejected (user chose fresh `ai-agent-home`).
- **ALT-003**: Auto-proceed without gates — rejected (user chose explicit plan + commit/push gates).

## 4. Dependencies

- **DEP-001**: Clarify answers (12/12) — satisfied.
- **DEP-002**: multi-file-change-protocol + create-implementation-plan + plans-and-specs skill stack — loaded/verified.
- **DEP-003**: Existing agent/context files as pre-state — verified (sizes above).
- **DEP-004**: Workspace validators (bun, python, markdownlint-cli2) — available.

## 5. Files

- **FILE-001** … **FILE-007**: see SPEC.md §2 (declared once).
- **FILE-008**: `ai-agent-home/specs/init-20260919T210721/SPEC.md`
- **FILE-009**: `ai-agent-home/plans/init-20260919T210721/PLAN.md`
- **FILE-010**: `ai-agent-home/prompts/init-20260919T210721/PROMPTS.md`
- **FILE-011**: `ai-agent-home/{specs,plans,prompts}/init-20260919T210721/STATUS.md` (3 copies)

## 6. Testing / Verification

- **TEST-001**: `python -c "import json; json.load(open('opencode.json'))"` exit 0
- **TEST-002**: `bun run markdownlint` (scoped to touched files) exit 0
- **TEST-003**: identifier-uniqueness grep checks (create-implementation-plan §Template Validation) → 0 dupes
- **TEST-004**: `.env` size before/after identical; no new `.bak`
- **TEST-005**: `git status --short` diff limited to intended files

## 7. Risks & Assumptions

- **RISK-001** … **RISK-006**, **ASSUMPTION-001** … **ASSUMPTION-002**: see SPEC.md §5 (declared once).

## 8. Related Artifacts

- SPEC: `ai-agent-home/specs/init-20260919T210721/SPEC.md`
- PROMPTS: `ai-agent-home/prompts/init-20260919T210721/PROMPTS.md`
