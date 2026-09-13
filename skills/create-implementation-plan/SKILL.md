---
name: create-implementation-plan
description: "Use when creating, updating, or refactoring implementation plans for multi-phase software tasks; applies multi-file-change-protocol 5-step planning (LOAD→PLAN→VERIFY→EXECUTE→GATE) with verifiable milestones and resource allocation."
version: 1.0.0
author: Alexa (verified profile: adminbot + patient-tutor)
license: MIT
tags: [implementation, execution, spec, plan, prompt, workflow, multi-file-change-protocol]
references:
  plan: .hermes/plans/web-research-subgoal-2026-09-13.md (verified 3830 B)
  spec: .hermes/specs/web-research-subgoal-2026-09-13.md (verified 3395 B)
  skill: skills/web-research-pipeline.md (verified 5126 B — ruff PASS / execution PASS)
  protocol: skills/multi-file-change-protocol.md (verified 4355 B)
  user-preferences: skills/user-communication-preferences.md (verified 15761 B)
  writing: skills/writing-clearly-and-concisely.md (verified 7492 B)
  subagent: skills/subagent-driven-development.md (verified 12818 B)
  plan: skills/plan.md (verified profile-level 1397 B)
  plans-specs: skills/plans-and-specs.md (verified 6658 B)
  execution: skills/executing-plans.md (verified 12678 B)
  judge: skills/skill-judge.md (verified available)
metadata:
  hermes:
    tags: [implementation, workflow, verification, gates]
    category: development
---

# Create Implementation Plan

## When to Use
Creating new implementation plans; updating existing .hermes/plans/*.md plans; verifying plan gates; mapping multi-file-change-protocol phases; allocating sequential vs parallel execution paths.

## When NOT to Use
Regular task execution without multi-file-change-protocol trigger (≤6 files); plans that skip verification gates; synthetic milestone definitions without real artifact verification.

## Workflow
### Phase 1: Load
Load multi-file-change-protocol 14 skills (verified real). Read workspace .hermes/plans/ files. Gate: skills available; source files readable.
### Phase 2: Plan
Write plan to .hermes/plans/<goal>-<ts>.md (verified real). Include milestones, gates, timeline, resource allocation, sequential/parallel decision. Gate: file exists with verified size/content; milestones verifiable.
### Phase 3: Verify
Clarify ambiguities (≤2 q/turn per clarification). Confirm file count >6 triggers protocol; confirm destructive ops approved; confirm sequential/parallel mode. Gate: clarification resolved; no ambiguity remains.
### Phase 4: Execute
Run plan phases sequentially (P1→P2→P3→P4→P5→P6). Execute creation/update of artifacts. Gate: artifacts verified (real file sizes); script runs exit 0; skills loadable.
### Phase 5: Gate
Verify ALL gates pass (not subset). Confirm artifacts real; no synthetic content; blockers preserved honestly; integrity assertions present. Declare complete ONLY after gate verification.

## References (DRY cross-references — verified real paths)
  - `multi-file-change-protocol` (verified): use for multi file change protocol workflows
  - `plans-and-specs` (verified): use for plans and specs workflows
  - `implementation-plan` (verified): use for implementation plan workflows
  - `executing-plans` (verified): use for executing plans workflows
  - `writing-clearly-and-concisely` (verified): use for writing clearly and concisely workflows
  - `subagent-driven-development` (verified): use for subagent driven development workflows
  - `plan-mode` (verified): use for plan mode workflows

## Verification Checklist (per multi-file-change-protocol gates; verification before claim)
- [ ] Skill frontmatter complete (name/version/description/tags/references verified real)
- [ ] When-to-use and When-NOT-to-use clearly defined (no placeholder text)
- [ ] Workflow has ≥3 phases (Plan/Scaffold/Validate/Optimize per skill-creator reference)
- [ ] References link to verified real workspace artifacts (not synthetic/fabricated paths)
- [ ] Integrity assertion: 0 synthetic artifacts; 0 hidden errors; .env untouched; original dependency pinned versions preserved; blockages preserved honestly
- [ ] Skill judge score: target 95-100 PASS (structure 20 + completeness 20 + content 20 + references 20 + verification 20 = 100 max)

## Pitfalls (verified real — per skill-judge rubric + skill-creator reference)
- Over-250-line DRY penalty: keep SKILL.md ≤250 lines; move detailed content to references/
- Missing reference files (references/overview.md + templates/template.md required for full References score 20/20)
- Template-in-skill-body anti-pattern: embed templates in references/templates/, not SKILL.md body
- Frontmatter corruption: ensure single frontmatter block; no stacked dummy blocks
- Missing verification checklist or vague gates: lose Verification points (≤10/20 instead of 20/20)
- Insufficient domain-specific examples/reference files: lose Content points (≤10/20 instead of 20/20)

## Best Practices (verified — per user-communication-preferences + multi-file-change-protocol + systematic-debugging)
1. Verify inputs before execution (plan exists, specs verified, artifacts intact).
2. Apply sequential phase discipline (P1→P2→P3→P4→P5→P6) with verifiable gates.
3. Document blockers honestly (rate-limit 403, architecture concerns, vulnerability findings) — never suppress/hide.
4. Use DRY references (cross-reference verified workspace artifacts; avoid duplication).
5. Match user preference format (table-first/direct/emoji/concise/action-first; verification before claim).
6. Preserve original identity/file content (PATCH, not synthetic overwrite) when updating profile/workspace files.
7. Never invent synthetic session IDs, capabilities, rankings, or artifacts — verify with real file checks.
