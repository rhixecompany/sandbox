---
name: skills-audit-remediation-remaining
title: Skills Audit Remediation — Remaining Tasks
description: "Use when continuing the skills audit pipeline after initial judgment. Covers re-judging patched skills, fixing remaining 51 needs-work skills, verification tracking, and final report generation."
date_created: 2026-06-14
last_updated: 2026-06-14
status: in_progress
---

# Skills Audit Remediation — Remaining Tasks

## Context

- **Total skills judged:** 191 (28 batches)
- **AI-ready (≥70):** ~113 skills
- **Needs work (50–69):** 51 skills
- **Already patched:** 26 skills (6 rewrite + 20 major)
- **Remaining to patch:** 51 skills (minor fixes)
- **Previous fix log:** `skills_audit_final_report.md` (initial remediation actions recorded)

---

## Remaining Work

### 1. Re-judge Patched Skills (verification)

**Goal:** Confirm the 26 patched skills moved into the AI-ready range (≥70).

**Workflow (per skill):**

1. Re-read the patched `SKILL.md` for the skill.
2. Run `skill-judge` evaluation against criteria:
   - Accuracy & correctness
   - Completeness (all sections present)
   - Usability (clear triggers, examples, verification)
   - Maintainability (DRY, no hardcoded paths)
   - Safety (no destructive ops without confirmation)
3. Record: new score, pass/fail, changes from original.
4. If score < 70, apply additional targeted patch and re-judge.

**Skills to re-judge (26):**

| # | Skill | Original | Status |
|---|-------|----------|--------|
| 1 | template | 35 | ✅ rewritten |
| 2 | ai-prompt-engineering-safety-review | 22 | ✅ rewritten |
| 3 | context-map | 21 | ✅ rewritten |
| 4 | convert-plaintext-to-md | 21 | ✅ rewritten |
| 5 | skills | 21 | ✅ rewritten |
| 6 | rbac-audit-logging | 18 | ✅ rewritten |
| 7 | httpie | 42 | ✅ patched |
| 8 | clonedeps | 44 | ✅ patched |
| 9 | codemap | 44 | ✅ patched |
| 10 | code-docs | 46 | ✅ patched |
| 11 | create-readme | — | ✅ patched |
| 12 | vscode-ext-commands | — | ✅ patched |
| 13 | azure-role-selector | — | ✅ patched |
| 14 | vscode-ext-localization | — | ✅ patched |
| 15 | folder-structure-blueprint-generator | 41 | ✅ patched |
| 16 | architecture-blueprint-generator | 42 | ✅ patched |
| 17 | technology-stack-blueprint-generator | 44 | ✅ patched |
| 18 | datadog | 44 | ✅ patched |
| 19 | multi-stage-dockerfile | 44 | ✅ patched |
| 20 | shadcn | 46 | ✅ patched |
| 21 | django-application | 46 | ✅ patched |
| 22 | caveman-unified | 52 | ✅ patched |
| 23 | worktrunk | 58 | ✅ patched |
| 24 | sandbox | 54 | ✅ patched |
| 25 | receiving-code-review | 42 | ✅ patched |
| 26 | webapp-testing | 44 | ✅ patched |

**Verification tracking:** Record results in a table. Any skill still < 70 goes back for additional fixes.

---

### 2. Fix Remaining 51 Needs-Work Skills

**Goal:** Raise the remaining 51 skills from 40–69 into the AI-ready range (≥70).

**Common fixes to apply (in order of impact):**

1. Add missing frontmatter fields: `version`, `author`, `license`, `tags`
2. Add **Skills Required** table (cross-references to related skills)
3. Add **Pitfalls** section (3–5 common mistakes + fixes)
4. Add **Verification Checklist** (5–8 items)
5. Add concrete examples where content is generic
6. Split long skills (>250 lines) and move template content to `templates/`

**Skills to fix (51):**

```
glab (42), jira (42), work-on-ticket (42), validate-memories (45), asdf (48),
terraform-azurerm-set-diff-analyzer (48), skill-creator (49), theme-factory (49),
content-research-writer (51), make-repo-contribution (51), marp-slide (51),
web-artifacts-builder (51), azure-devops-cli (52), frontend-design (52),
customize-opencode (53), mermaid-diagrams (53), appinsights-instrumentation (54),
customization-audit (54), template-skill (55), claude-api (56), copilot-cli (56),
fabric-lakehouse (56), plan (56), projects-multi-repo-init-normalize (56),
stable-diffusion-image-generation (56), banking (58), copilot-cli-quickstart (58),
hermes-skill-library-maintenance (58), qdrant-vector-search (59), hermes-breakdown (60),
simpo-training (60), agent-browser (61), excalidraw-diagram-generator (61),
using-superpowers (61), peft-fine-tuning (62), writing-clearly-and-concisely (62),
algorithmic-art (63), brand-guidelines (63), canvas-design (63), copilot-usage-metrics (65),
qwen-code (65), agent-governance (66), create-web-form (67), fine-tuning-with-trl (67),
plantuml-ascii (67), legacy-circuit-mockups (68), nano-banana-pro-openrouter (68),
prompt-builder (68), session-audit-report (68), writing-skills (68), agentic-eval (69)
```

**Batch approach:** Process in groups of 7 to stay within tool-call limits, same as the original audit. Group by category where possible.

---

### 3. Re-judge All Repaired Skills

After all fixes are applied:

1. Re-read each patched `SKILL.md`.
2. Run `skill-judge` evaluation.
3. Confirm score ≥ 70 for all skills.
4. Generate final score comparison: original vs. repaired.

---

### 4. Update Final Report

**File:** `skills_audit_final_report.md`

Update sections:
- Remediation summary table (before/after scores)
- Skills that passed verification
- Skills that still need work (if any)
- Aggregate statistics (AI-ready % before vs. after)
- Files modified list

---

## Execution Order

1. **Re-judge the 26 patched skills** (verify score improvements)
2. **Fix the 51 remaining skills** (batches of 7, by category)
3. **Re-judge all repaired skills** (confirm all ≥ 70)
4. **Update `skills_audit_final_report.md`** with final results

---

## Tracking

**Fix log format (per skill):**

```
[YYYY-MM-DD] Skill: <name>
  Original score: N/100
  Patched: Y/N
  Patch type: rewrite | major | minor
  New score: N/100 (verified/re-pending)
  Files modified: <path>/SKILL.md
```

**Verification gate:**

- [ ] All 26 patched skills re-judged and scores confirmed ≥ 70
- [ ] All 51 remaining skills patched
- [ ] All 77 total repaired skills re-judged and confirmed ≥ 70
- [ ] Final report updated with before/after comparison
- [ ] No skills left in “needs work” or “rewrite” state (unless unfixable)

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Some skills are fundamentally unfixable (pure stubs) | Mark as deprecated in manifest, exclude from future audits |
| Re-judge reveals patch was insufficient | Apply additional targeted patch, re-judge again |
| Token overflow during re-judge | Summarize results, don’t retain full skill text |
| Tool-call limit reached mid-batch | Track progress in `SESSION_REPORT.md`, resume from next skill |

---

## Saved Plan Location

`.hermes/plans/2026-06-14_143000-skills-audit-pipeline.md` (original plan)
This plan: remaining remediation and verification tasks.

---
**Status:** Ready to execute Step 1 — re-judge the 26 patched skills.
