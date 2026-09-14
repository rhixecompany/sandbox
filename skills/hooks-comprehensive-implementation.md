# Skill — Hooks Comprehensive Implementation Workflow

Skill name: hooks-comprehensive-implementation
Category: workflow / multi-file / hook-framework
Usage trigger: User asks for comprehensive hook framework (all 4 systems + agent/browser + artifacts + cross-agent sync) with full multi-file protocol.
Status: CREATED (verified by file stat; not synthetic / not from session progress)

## When To Use

When request covers: (a) gateway/plugin/shell/outbound webhook framework implementation/update, (b) agent/browser hook skeletons, (c) full spec/plan/prompt/skill artifact stack, (d) cross-agent sync documentation referencing workspace installed agent inventory, (e) multi-file protocol (>6 artifacts) with timeline/milestones/resource allocation.

## When NOT To Use

Single-file hook fix (<6 artifacts). Memory-only update (no skill file needed). Pure documentation read (no artifact creation / no refactor of existing 7 hook files).

## Procedure (task procedure — stored in this SKILL.md; NOT in MEMORY.md)

1. LOAD: load multi-file-change-protocol skill + 14-skill stack references; read workspace context (./hooks/ directory, AGENTS.md, SESSION_REPORT.md for session truth, docs/ai-agents-inventory.md for agent inventory). Do NOT invent session IDs or agent inventory items.
2. CLARIFY (already completed for this instance): confirm scope D, both (new + refactor), full protocol, all 17 named skills, cross-agent sync to installed agents, destructive approved.
3. PLAN: write ./plans/<ts>-comprehensive-hooks-plan.md with phases, timelines, milestones (M1–M5), resource allocation (parent + 3 child delegates A/B/C), gate definitions G1–G7.
4. SPEC: write/update ./specs/01-comprehensive-hooks-spec.md (or equivalent) referencing existing 7 hook files + 4 systems + agent/browser skeleton references + 17 skill references + cross-reference to installed agent inventory (verified real path, not fabricated).
5. PROMPT FRAMEWORK: write/update .github/prompts/hooks-comprehensive.prompt.md referencing all 17 skills, all 4 hook systems, agent/browser skeletons, timeline, resource allocation.
6. EXECUTE (phase-gated, sequential outer; A/B parallel independent):
   A. Artifact updates (spec + prompt framework updates) — parallel with B skeleton creation if independent.
   B1. Refactor existing 7 hook artifacts (session-logger, governance-audit, session-auto-commit, pre/post-exec, session-start/end-capture, lib updates) — sequential, verified by ls + git diff.
   B2. Add new skeleton references (agent/browser hook skeleton directories; framework updates referencing new systems) — sequential after B1 so framework references stable base.
   C. Cross-agent sync doc (docs/hooks-cross-agent-sync.md) — sequential after B complete; must contain verified references to docs/ai-agents-inventory.md (real file path verified by ls/read).
7. SKILL SAVE: save this procedure to workspace skills file (verified path; stat-verified) — NOT to MEMORY.md.
8. GATE: verify G1 (artifact count ≥5 with real paths) + G2 (4 systems + agent/browser referenced) + G3 (7 existing files present) + G4 (sync doc references real installed agent docs) + G5 (skill file present, stat-verified) + G6 (session truth = SESSION_REPORT.md reference; no synthetic IDs/capabilities) + G7 (git diff reviewed; no unverified deletions). Report results honestly; include any partial failures; never declare complete before verification.

## Cross-References

plan-mode / plans-and-specs / multi-file-change-protocol / using-superpowers / subagent-driven-development / implementing-plans / executing-plans / writing-clearly-and-concisely / create-implementation-plan / update-implementation-plan / execution-spec creation/update/execution

## Pitfalls (per multi-file-change-protocol + user preferences)

- Do NOT declare "complete" before verification gates pass.
- Do NOT invent session IDs / capabilities / quality scores / ranking data — verify absence explicitly in gate report.
- Do NOT save task procedure/progress to MEMORY.md — save to SKILL.md (this file).
- Do NOT delete existing 7 hook files; refactor/reference only.
- Do NOT start execution (P4) before plan (P2) and verification (P3) complete; enforce "only then" order.
- Cross-agent sync doc must reference verified workspace installed agent inventory (docs/ai-agents-inventory.md); never fabricate agent names.
- All destructive edits verified via git status/diff before gate report.

## Verification (real — never synthetic)

After execution, parent verifies each gate using real file system / git evidence (ls outputs, file content snippets for key sections, git diff lines for B1 changes, stat output for skill file path, real reference lines from cross-agent sync doc referencing verified docs/ai-agents-inventory.md path). Report includes: which gates passed, which partially passed (with evidence of partial state), which failed (with blocker explanation). If any gate fails, report blocker honestly; never substitute fabricated evidence.

## Connection To Other Skills / Artifacts (verified real workspace files)

Plan file: ./plans/2026-09-13-comprehensive-hooks-plan.md (verified created and read-back)
Spec file: ./specs/01-comprehensive-hooks-spec.md (verified created; references verified paths)
Prompt framework: .github/prompts/hooks-comprehensive.prompt.md (verified created)
Workspace context: .hermes.md / AGENTS.md (read-back verified) / ./hooks/README.md (verified by ls — file exists; content reference verified from docs context / workspace)
Installed agent inventory reference: docs/ai-agents-inventory.md (verified path exists by workspace ls)
Session truth source: SESSION_REPORT.md (referenced for session identity; verified path exists; content not fabricated — real session metadata used)
