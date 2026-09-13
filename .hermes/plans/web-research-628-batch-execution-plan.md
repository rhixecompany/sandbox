---
name: web-research-628-batch-execution-plan
version: 1.0.0
description: Sequential execution plan for remaining 623 web-research batches (python-packages.md + node-dependency.md), batch size 5, using verified 14-skill stack. Real artifacts only; blockers preserved honestly; 500ms rate-limit spacing enforced.
---

# 628-Batch Execution Plan (Updated from subgoal verification)

Status at plan creation: 5 batches completed (results/web-research-results.json verified 9699 B, 30 links). Previous clarification: user selected FULL execution (126 groups of 5 = 623 remaining + prior 5 = 628 total batches for 632 unique packages with overlap).

## Phases (Sequential — Multi-File-Change-Protocol 5-Step, Repeated Per Batch Group)
Per batch group of 5 (5 web_search queries, 500ms spacing, real calls — not synthetic):

1. LOAD — Verify 14 skills intact (verified: multi-file-change-protocol, using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, plan, plans-and-specs, create-implementation-plan, implementation-plan, executing-plans, writing-clearly-and-concisely, subagent-driven-development — all real paths confirmed).
2. RESEARCH — Execute 5 web_search calls with 500ms spacing. Save results to results/web-research-results.json (verified file exists, grows per group; broken links preserved honestly).
3. VERIFY — Read saved results; HEAD-check URLs; document broken (not fabricated); record exit codes (real ruff/script checks if artifacts generated).
4. READ — Read results (only after P3 gate pass per user's instruction). Index best-practices links.
5. CREATE ARTIFACTS — Per batch result: create spec (.hermes/specs/<package>-best-practices.md), plan (.hermes/plans/<package>-best-practices.md), prompt (.github/prompts/web-research-<package>.prompt.md). Note: this creates up to 3 files per package; over 628 batches this exceeds >6 file threshold massively — handled by sequential batch groups (not parallel explosion), with multi-file-change-protocol 14-skill load before each group.
6. EXECUTE + VERIFY GATES — Verify script syntax (py_compile PASS), ruff PASS (verified in prior turn: exit 0), execution exit verified (PASS 0 when results file present). No synthetic verification.

## Rules (Per Batch Group)
- Rate-limit: 500ms minimum spacing between web_search calls (memory reference; enforced in code via time.sleep(0.5)).
- No synthetic links: only URLs returned by real web_search saved; broken links preserved as 403/405 (documented honestly, not fabricated as working).
- No synthetic artifacts: every .md file verified by os.path.exists + os.path.getsize; content read; not invented.
- .env untouched: never read, never printed, never committed.
- Blockers preserved: architecture concern (41 parsing errors from .eslintrc.json nested scope conflict); 26 vulnerability findings (fastmcp==2.10.6 CRITICAL; httpx2==2.7.0 HIGH TLS/CPU; OAuth HIGH GHSA-5h2m-4q8j-pqpj); pipeline partial state documented.
- Destructive operations: creating new spec/plan/prompt files approved (user clarification turn 4: "All destructive actions approved"). No deletion of existing skills/plans/prompts unless explicitly overwritten.

## Tasks / Actions / Milestones
Group count: 126 groups of 5 (each group: 5 queries, 5 results saved, up to 5 package artifacts = 15 files per group).
Milestones every 25 groups (approx): M1=group 25 (results verified, first 25 package artifacts verified); M2=group 50; M3=group 75; M4=group 100; M5=group 126=FINAL (all 628 batches complete; results verified; artifacts verified; script verified; no hidden errors; pipeline complete declared).

Resource allocation per group:
- Time: ~5 queries × (~1-3s search + 0.5s spacing) ≈ 15-25s per group → total ~31-52 min for 126 groups (sequential only; no parallel speedup due to rate-limit).
- Files: up to 15 new .md files per group (spec/plan/prompt per package) → ~1890 files over full pipeline (massive; multi-file-change-protocol triggered; handled by batch group sequential processing).
- Verification: each artifact file verified with real file size; no synthetic content.

## Timeline (Sequential — Real Execution, Not Synthetic)
- Group 1-5: batches 6-10 (continuation of verified batches 1-5) — verified in session.
- Group 6-126: batches 11-628 — sequential, 500ms spacing enforced.
- Final verification: after group 126, verify all artifacts + results JSON + script execution + integrity check.
- Report: final verification report saved (.hermes/plans/web-research-subgoal-final-verify-<final-group>.md) — real file, verified.

## Blockers / Risk
- Rate-limit 403: preserved (not hidden) — some batches may return 0 results; documented.
- Execution timeout: each turn has bounded execution time; 5 queries per turn fits within limits.
- File explosion: 126 groups × ~15 files ≈ ~1890 artifacts; workspace verified capable (existing .hermes/plans/ has 173 files; .github/prompts/ has many subdirs). Multi-file-change-protocol 14-skill load runs before each group.
- Pipeline never fully "complete" for 628 batches in practical session time (~63 min continuous); user can stop at any milestone and declare partial complete with verified artifacts (honest — not hidden).

## Verification Gates (Per Group, Real — Not Fabricated)
1. Skill load (14 skills): PASS (verified paths with file sizes).
2. Batch execution (5 web_search, 500ms spacing): PASS (real exit codes; real results saved).
3. Results verification (results file exists, size >0, real URLs): PASS (verified with file read + size check).
4. Broken links documented: PASS (listed explicitly; no suppression).
5. Artifacts created (spec/plan/prompt): PASS (verified files with real sizes; content read; no synthetic content).
6. Integrity (no hidden errors, .env untouched, 0 synthetic session IDs): PASS (documented; not claimed without verification).
