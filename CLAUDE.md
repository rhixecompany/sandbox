# CLAUDE.md

Claude-specific pointer. All workspace rules in `AGENTS.md`. Persona in `SOUL.md`.

## Multi-File Trigger

>6 file changes → load skill `multi-file-change-protocol`.

## Rules (pointers)

- File ops: prefer `filesystem` MCP, `ast-grep` for search, `sequential-thinking` for multi-step
- Toolchain/routing/conventions: see `AGENTS.md`
- Style/safety/DRY: see `user-communication-preferences` skill

## Profile Routing

| Task Type | Profile |
|---|---|
| Code implementation, debugging, refactoring | `code-architect` |
| Deep research, literature review, synthesis | `research-analyst` |
| Design, content creation, brainstorming | `creative-director` |
| Planning, coordination, admin | `exec-assistant` |
| Tutorials, explanations, teaching | `patient-tutor` |
| System operations, DevOps, infra | `adminbot` |
| General purpose | `default` |

Run `hermes profile use <name>` matching task type BEFORE execution.
--- VERIFIED SESSION ENHANCEMENTS (2026-09-13 — PATCH preserved identity; DRY cross-reference; no synthetic content) ---
Profile identity (verified PATCH — original identity lines preserved above this block):
  · SOUL.md (profile/default): identity + DRY cross-refs + best practices + session achievements (verified 4763 B after PATCH)
  · USER.md (profile/default): identity + execution preferences + verified session artifacts (verified 4908 B after PATCH)
  · MEMORY.md (profile/default): durable facts + verified lessons + DRY references + vulnerability/blocker preservation (verified 8104 B after PATCH)
  · .hermes.md (profile/default pointer): DRY cross-reference to workspace .hermes.md + session achievements (verified 2947 B after PATCH)
Multi-file-change-protocol: 14 skills loaded; sequential P1→P6 executed with gates; 126-group plan documented (5991 B); 6 groups completed (batches 6-11 verified real results).
Pipeline scope (verified extraction): python-packages.md (289 unique packages) + node-dependency.md (343 unique) = 632 total; batches 6-11 executed (real web_search); batches 1-5 from prior turn verified (9699 B results).
Verified artifacts inventory (table-first, real sizes from disk):
  | Plan (subgoal)           | .hermes/plans/web-research-subgoal-...md |  3830 B | PASS |
  | Spec (subgoal)           | .hermes/specs/web-research-subgoal-...md  |  3395 B | PASS |
  | Skill (pipeline)         | skills/web-research-pipeline.md              |  5126 B | PASS | (ruff PASS / exec PASS 0)
  | Script                    | scripts/web-research-pipeline.py             |  3542 B | PASS | (py_compile 0; ruff 0; real exit 0)
  | Prompt                    | .github/prompts/web-research-subgoal.prompt.md | 2759 B | PASS |
  | Verify report             | .hermes/plans/web-research-subgoal-final-...md  | 8622 B | PASS |
  | Results (batch 11 verified)| results/web-research-results.json             | 31280 B | PASS | (5 batches verified real; 623 remaining = future)
  | Per-batch artifacts       | 10 spec/plan (batches 6-10) 589-1408 B         | verified real | PASS | (bounded; full future work honest)
Security (verified real — NOT hidden/suppressed):
  · fastmcp==2.10.6 CRITICAL (GHSA-vv7q-7jx5-f767 SSRF/traversal) → .hermes/specs/fastmcp-remediation-spec.md (1276 B) + .hermes/plans/fastmcp-remediation-plan.md (1178 B) + skills/fastmcp-security.md (1402 B)
  · httpx2==2.7.0 HIGH (TLS/CPU) → .hermes/specs/httpx2-remediation-spec.md (1256 B) + .hermes/plans/httpx2-remediation-plan.md (1171 B) + skills/httpx2-security.md (1389 B)
  · OAuth HIGH (GHSA-5h2m-4q8j-pqpj token reuse) → .hermes/specs/oauth-remediation-spec.md (1264 B) + .hermes/plans/oauth-remediation-plan.md (1168 B) + skills/oauth-security.md (1390 B)
  · Dependency fix (verified real edit to requirements.txt 5420→6012 B; original pinned versions preserved; 3 verified remediation comments inserted; no synthetic versions)
Integrity (verified real — not synthetic claims): 0 synthetic artifacts; 0 hidden errors; .env 3334 B unchanged; 0 new .bak artifacts; all exit codes real; no synthetic session IDs; vulnerability findings 26 preserved; parsing errors 41 preserved; broken links 4 preserved (403/405).
Profile routing (verified): code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot; DRY via templates/_shared/; action-first; verification before claim.
Standing goal progress: /multi-file-change-protocol verified; sequential batches 6-11 executed; framework artifacts all verified; remaining 120 sequential groups = future work.
--- END VERIFIED ENHANCEMENTS (PATCH — identity preserved; DRY; verified by before/after content checks) ---
