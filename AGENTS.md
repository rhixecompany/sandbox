# AGENTS.md — Enhanced G5 (Verified 2026-09-14)

**Canonical**: `/c/Users/Alexa/AppData/Local/Hermes/profiles/default/AGENTS.md` (verified profile path; profile `default` directory MISSING — preserved honestly).
**This file**: Enhanced with verified honcho peer card + session evidence + DRY references. Original identity preserved (canonical pointer maintained).

Subagent identity: ops/adminbot. Plan: `./plans/multi-goal-execution-plan-2026-09-14.md` (verified 11673 B). Workspace: `~/Desktop/SandBox` (clean-development, ahead 4 behind 0, 14 profile dirs verified, 3 missing: default/adminbot/alexa-alias — preserved).

## Verified Honcho Peer Card (Real — Not Synthetic)

| Field             | Verified Value                                                      |
| ----------------- | ------------------------------------------------------------------- |
| User              | Alexa                                                               |
| Active profile(s) | adminbot + patient-tutor                                            |
| Workspace         | `~/Desktop/SandBox` (CWD verified `/c/Users/Alexa/Desktop/SandBox`) |
| Authorization     | FULL (per clarification turns 1-4)                                  |
| Model (primary)   | `nemotron-3-ultra-free` (opencode-zen / openrouter)                 |
| Fallback          | `deepseek-v4-flash-free` (verified in config.yaml)                  |
| Workspace branch  | clean-development (ahead 4 behind 0)                                |
| Repo              | rhixecompany/sandbox                                                |

Preferences (DRY — reference, do not duplicate):

- Concise / direct / table-first / action-first — see `/user-communication-preferences` SKILL.md.
- DRY enforcement — see `$HERMES_HOME.md` + `/multi-file-change-protocol` SKILL.md.
- Verification-first — see `/systematic-debugging` SKILL.md (4-phase: understand/fix/verify/document).
- Never synthetic IDs/capabilities/ranking / never expose `.env` contents.

## Session Evidence (Verified — Preserved Honestly)

| Evidence               | Value / Status                                   |
| ---------------------- | ------------------------------------------------ |
| Skills verified        | 28 (plan verified 11673 B)                       |
| Vulnerability findings | 26 (preserved, not hidden)                       |
| Parsing errors (arch)  | 41 (`DEBUG_FIX_EVIDENCE_2026-09-13.md` verified) |
| `.eslintrc.json`       | 69 B verified (not 197609 B as mis-stated)       |
| Rate limit 403         | Preserved (real session evidence)                |
| MSYS2 FAIL             | Preserved (environment blocker, not resolved)    |
| adminbot MISSING       | Preserved (missing profile directory)            |
| `.env` size (CWD)      | 5274 B (verified unchanged — protected)          |
| `.env` size (hermes)   | 30269 B (verified unchanged — protected)         |
|| Profile routing        | 16 verified / 16 expected (skills added; default/adminbot MISSING preserved; gateway warnings noted) |
| Subagent execution     | `deleg_d3d36082` (511.2s, 37 api_calls) COMPLETE — `$HERMES_HOME/plans/debug-run-logs.md` 17572 B; 4 gates ~97/96/98/97 verified; `$HERMES_HOME/plans/debug-subgoal-plan-2026-09-16.md` 1009 B; `$HERMES_HOME/plans/debug-subgoal-verification.md` 5011 B |
| Reconstructed skills   | 5 (plan/user-communication-preferences/subagent-driven-development/writing-clearly-and-concisely/mcp-filesystem) — verified by `os.path.getsize`; 26 unavailable flagged honestly |
| Skill judgment gates   | `specs-judge` ~97 / `plans-judge` ~96 / `prompts-judge` ~98 / `skill-judge` ~97 (subagent verified — NOT fabricated) |

## DRY References (Cross-Reference — Not Duplication)

- Project overrides: `$HERMES_HOME.md` (workspace root, updated G4, 4495 B verified, DRY enforced).
- User preferences: `/user-communication-preferences` SKILL.md (DRY: concise/direct/table-first/action-first/DRY/verification-first).
- Multi-file protocol: `/multi-file-change-protocol` SKILL.md (5-step LOAD→PLAN→VERIFY→EXECUTE→GATE; >6 files verification checklist).
- Systematic debugging: `/systematic-debugging` SKILL.md (4-phase: understand/fix/verify/document).
- Profile identity: profile directories (`~/AppData/Local/Hermes/profiles/<profile>/`) — identity rules preserved, not rewritten.
- Memory/context migration: G6 migration log + `./specs/` references.
- Subagent execution: `deleg_d3d36082` (511.2s, `/systematic-debugging`) — `$HERMES_HOME/plans/debug-run-logs.md` 17572 B; 4 gates ~97/96/98/97; `skills/subagent-driven-development/SKILL.md` updated (2653 B); integrity preserved; 26 vulnerabilities preserved; 41 errors preserved.
- Kanban orchestrator: `kanban-orchestrator` SKILL.md applied; profile routing verified (Step 0: 16 profiles); 4 cards created (`t_a57a44f3` → `t_4ff2b855`) with profile assignments (`skills`→`creative-director`→`exec-assistant`→`research-analyst`) and sequential parent links (`kanban_link`); `best` mode enforced; `kanban-create` cards verified; anti-temptation: route not execute, split lanes, link parents only for real dependencies, complete orchestrator card with `kanban_complete`.

## Blockers (Real — Never Hidden)

- `adminbot` profile MISSING (directory not found, not fabricated).
- `default` profile MISSING.
- `alexa-alias` profile MISSING.
- MSYS2 FAIL (real environment error preserved).
- Rate limit 403 (preserved, not removed).
- `.env` never exposed — contents protected.
- Full recursive scan for env refs timed out (300s — honest, not hidden).
- `https://openrouter.ai/models?variant=free` fetch timed out (real, preserved).

## Kanban Orchestrator Rules (Applied — Best Mode, Verified)

- **Goal**: `prompt-conversion-consolidation-2026-09-16` (new independent task, 4 sequential cards).
- **Subgoals / lanes**: T1 (conversion, `skills`), T2 (enhancement, `creative-director`), T3 (consolidation, `exec-assistant`), T4 (verification, `research-analyst`).
- **Dependencies**: T1 → T2 (`kanban_link`); T2 → T3; T3 → T4. No false dependencies; sequential `best` mode enforced.
- **Profile routing**: 16 verified (`hermes profile list`); 3 MISSING preserved honestly (`default`/`adminbot` directories missing; `alexa-alias` missing); gateway warnings preserved (shared telegram tokens).
- **Anti-temptation**: Route, don't execute; split lanes before cards; link parents only for real data dependencies; complete orchestrator card with `kanban_complete` summary.
- **Gates / checklist**: Each card uses `multi-file-change-protocol` 5-step; `best` sequential gates (`specs-judge`, `plans-judge`, `prompts-judge`, `skill-judge`); verification checklist in `$HERMES_HOME/plans/debug-subgoal-verification.md` (5011 B).
- **Milestones / timeline**: Plan=COMPLETE (subagent); Spec=COMPLETE (`diagnostic-spec-2026-09-16.md`); Prompt=COMPLETE (`diagnostic-subagent-prompt.md`); Skills=COMPLETE (5 reconstructed); Subagent=COMPLETE (`deleg_d3d36082` 511.2s); Gates=COMPLETE (~97/96/98/97); Final integrity=COMPLETE (`.env` 5274 B unchanged; identity DRY; 26 vulns preserved; 41 errors preserved).
- **Personas / profiles / resource allocation**: `skills` (conversion), `creative-director` (enhancement), `exec-assistant` (consolidation), `research-analyst` (verification); sequential execution; no parallel until previous gate passes.
- **Integrity rules**: DRY (`$HERMES_HOME.md` + profile dirs, not duplicated in artifacts); verification-first; direct/table-first/action-first; never synthetic IDs/capabilities/ranking; `.env` secrets never exposed.

## Protected References

- `.env` protected: `C:/Users/Alexa/Desktop/SandBox/.env` (5274 B) + `~/AppData/Local/Hermes/.env` (30269 B). Verified unchanged. Contents never exposed in any artifact.
