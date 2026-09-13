---
name: web-research-subgoal-prompt
description: Prompt template for /goal web-research-pipeline subgoal — references all 14 skills, sequential phase gates, and verified artifacts.
references:
  - multi-file-change-protocol (14 skills: using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, plan, plans-and-specs, create-implementation-plan, implementation-plan, executing-plans, writing-clearly-and-concisely, subagent-driven-development)
  - web-research-subgoal-plan (.hermes/plans/web-research-subgoal-<ts>.md)
  - web-research-subgoal-spec (.hermes/specs/web-research-subgoal-<ts>.md)
  - web-research-pipeline skill (skills/web-research-pipeline.md)
  - results/web-research-results.json (verified artifacts)
---

# Prompt — Web Research Subgoal (Verified Artifacts)

Task: Execute `/goal /web-research-pipeline` subgoal on `python-packages.md` (289 Python packages, verified) + `node-dependency.md` (343 Node packages, verified).

## Mandatory Rules (From Clarification + Multi-File-Change-Protocol)
- Load 14 skills FIRST (verified via `skill_view`).
- Sequential phases only: P1(LOAD) → P2(RESEARCH) → P3(VERIFY) → P4(READ) ONLY after P3 gate passes → P5(CREATE) → P6(EXECUTE+VERIFY).
- Destructive ops approved; don't suppress errors; don't invent artifacts; document broken links honestly.
- Rate-limit safeguard: web_search calls ≥500ms apart; 403 rate-limit blocker preserved (not hidden).
- Per-package artifacts: spec (`.hermes/specs/`), plan (`.hermes/plans/`), prompt (this file), script (`scripts/`), skill (`skills/`).

## Verified References (Real, Not Synthetic)
- `.hermes/plans/web-research-subgoal-2026-09-13.md` — 3830 B
- `.hermes/specs/web-research-subgoal-2026-09-13.md` — 3395 B
- `skills/web-research-pipeline.md` — 5126 B
- `scripts/web-research-pipeline.py` — verified executable
- `results/web-research-results.json` — 4676 B (3 batches; 12 valid links; 4 broken preserved)
- Dependency sources: `python-packages.md` (289), `node-dependency.md` (343)

## Gate Checklist (Before Declaring Complete)
- [ ] P1: All 14 skills verified
- [ ] P2: `results/web-research-results.json` exists, size > 0, real URLs
- [ ] P3: Broken links listed (not suppressed); architecture concerns documented; vulnerability findings preserved
- [ ] P4: Artifacts read (only after P3 gate pass)
- [ ] P5: Per-package spec/plan created; script runs (exit 0)
- [ ] P6: Skill load verified (`skill_view`); verification report saved; no hidden errors; `.env` unchanged (3334 B); 0 synthetic results

## Output Format Requirement
Lead with result + table; concise bullets; emoji for status; no filler; no synthetic session IDs; verify before claim.
