# Approval Request: Skills Audit Remediation — Patch 51 Skills + Re-judge 26

**Date:** 2026-06-16
**Requestor:** Alexa (workspace owner)
**Owner(s):** Alexa
**Status:** PENDING

---

## Scope

Perform targeted patches on **51 skills** rated "needs work" (scores 40–69) and re-judge **26 previously patched skills** to confirm they meet the AI-ready threshold (≥70).

### Files to Modify

**51 skills to patch** (per `remediation-plan-v2.md` and `remaining-remediation-plan.md`):
- Batch B (8): customize-opencode, mermaid-diagrams, template-skill, claude-api, copilot-cli, plan, projects-multi-repo-init-normalize, stable-diffusion-image-generation
- Batch C (13): banking, copilot-cli-quickstart, hermes-skill-library-maintenance, qdrant-vector-search, hermes-breakdown, simpo-training, agent-browser, using-superpowers, peft-fine-tuning, writing-clearly-and-concisely, algorithmic-art, brand-guidelines, canvas-design
- Batch D (15): copilot-usage-metrics, qwen-code, agent-governance, create-web-form, fine-tuning-with-trl, plantuml-ascii, legacy-circuit-mockups, nano-banana-pro-openrouter, prompt-builder, session-audit-report, writing-skills, validate-memories, agentic-eval
- Exception: frontend-design (skipped due to prior write failure)

**26 skills to re-judge** (already patched):
template, ai-prompt-engineering-safety-review, context-map, convert-plaintext-to-md, skills, rbac-audit-logging, httpie, clonedeps, codemap, code-docs, create-readme, vscode-ext-commands, azure-role-selector, vscode-ext-localization, folder-structure-blueprint-generator, architecture-blueprint-generator, technology-stack-blueprint-generator, datadog, multi-stage-dockerfile, shadcn, django-application, caveman-unified, worktrunk, sandbox, receiving-code-review, webapp-testing

---

## Justification

The skills audit pipeline (28 batches, 191 skills judged) identified 51 skills below the AI-ready threshold (≥70). These skills lack standard frontmatter fields, Skills Required tables, Pitfalls sections, and Verification Checklists. Patching them will:
- Improve consistency across the skill library
- Enable reliable automated discovery and routing
- Reduce session startup overhead (skills load correctly on first try)

---

## Rollback Plan

All changes are `skill_manage(action='patch')` operations on individual `SKILL.md` files. Rollback commands:

```bash
# For any single skill patch revert:
git checkout HEAD -- <skill-path>/SKILL.md

# For all skill patches in a batch:
git diff --name-only HEAD -- '*skills*/SKILL.md' | xargs -I {} git checkout HEAD -- {}

# Full revert to pre-remediation state:
git reset --hard <commit-before-remediation>
```

The git history provides complete traceability. No config files or external systems modified.

---

## Verification Steps

Post-patch verification (per `verification-before-completion` skill):

1. **Syntax validation:** `skill_manage` auto-runs syntax checks on each patch
2. **Re-judge:** Run `skill-judge` evaluation on each patched skill
3. **Threshold check:** Confirm score ≥ 70 for all 77 skills (51 new + 26 re-judged)
4. **Audit re-run:** `hermes skills audit && hermes skills update` passes
5. **Report update:** Update `skills_audit_final_report.md` with before/after scores
6. **Final report:** Generate `skills_audit_final_report.md` with aggregate statistics

---

## Approval

**Owner:** _______________ (Alexa)
**Date:** _______________
**Signature:** +1

**Approval valid until:** 2026-07-16

---

## Post-Execution Notes

_To be filled after execution:_

- Commit SHA: _______________
- Verification outputs appended: [ ] Yes [ ] No
- Any failures/remediation: _______________