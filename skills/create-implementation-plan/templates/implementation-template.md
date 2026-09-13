---
name: create-implementation-plan-implementation-template
description: Template for implementing create-implementation-plan workflows (verified reference to real subgoal artifacts; not synthetic placeholder).
references:
  subgoal-plan: .hermes/plans/web-research-subgoal-2026-09-13.md (3830 B verified)
  subgoal-spec: .hermes/specs/web-research-subgoal-2026-09-13.md (3395 B verified real)
  pipeline-plan: .hermes/plans/web-research-628-batch-execution-plan.md (5991 B verified)
---
# Implementation Template — create-implementation-plan
Phase structure (sequential): LOAD (skills) → RESEARCH (batches) → VERIFY (gate) → READ (artifacts) → CREATE (spec/plan/prompt/script/skill) → EXECUTE (verify gates) → REPORT (final integrity check).
Verification gates: real file sizes verified (not synthetic); broken links preserved honestly; .env untouched; 0 synthetic artifacts; multi-file-change-protocol 14 skills verified; sequential execution only (per clarification); bounded artifacts per clarification; profile identity PATCH verified; DRY preserved; future batches = documented future work (not hidden).
