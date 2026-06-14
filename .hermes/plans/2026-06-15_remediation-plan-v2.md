---
name: remediation-plan-v2
title: Skills Audit Remediation v2 — Remaining 51 Skills (Targeted Patch)
description: "Targeted patch of remaining 51 needs-work skills. Only adds missing pieces: frontmatter fields, Skills Required table, pitfalls section, verification checklist."
status: executing
date: 2026-06-15
---

# Remediation Plan v2 — Remaining 51 Skills

## Strategy

**Targeted patch only** — for each skill:
1. Add missing frontmatter fields (version, author, license, tags)
2. Add Skills Required table
3. Add pitfalls section (3-5 items)
4. Add verification checklist (5-8 items)
5. Preserve all existing content intact

**Do NOT**:
- Rewrite or remove existing prose
- Change workflow structure
- Move or rename files

## Exception

- `frontend-design` — write failed in prior session, left as-is, accepted risk

## Execution Order

### Batch B Remaining (8 skills)
| Skill | Path | Status |
|-------|------|--------|
| frontend-design | creative/frontend-design/SKILL.md | ⚠️ SKIPPED (write failed) |
| customize-opencode | development/customize-opencode/SKILL.md | pending |
| mermaid-diagrams | creative/mermaid-diagrams/SKILL.md | pending |
| template-skill | development/template-skill/SKILL.md | pending |
| claude-api | software-development/claude-api/SKILL.md | pending |
| copilot-cli | copilot-cli/SKILL.md | pending |
| plan | software-development/plan/SKILL.md | pending |
| projects-multi-repo-init-normalize | devops/projects-multi-repo-init-normalize/SKILL.md | pending |
| stable-diffusion-image-generation | stable-diffusion-image-generation/SKILL.md | pending |

### Batch C (13 skills)
| Skill | Path | Status |
|-------|------|--------|
| banking | software-development/banking/SKILL.md | pending |
| copilot-cli-quickstart | development/copilot-cli-quickstart/SKILL.md | pending |
| hermes-skill-library-maintenance | development/hermes-skill-library-maintenance/SKILL.md | pending |
| qdrant-vector-search | qdrant-vector-search/SKILL.md | pending |
| hermes-breakdown | hermes-breakdown/SKILL.md | pending |
| simpo-training | simpo-training/SKILL.md | pending |
| agent-browser | development/agent-browser/SKILL.md | pending |
| using-superpowers | development/using-superpowers/SKILL.md | pending |
| peft-fine-tuning | peft-fine-tuning/SKILL.md | pending |
| writing-clearly-and-concisely | creative/writing-clearly-and-concisely/SKILL.md | pending |
| algorithmic-art | creative/algorithmic-art/SKILL.md | pending |
| brand-guidelines | creative/brand-guidelines/SKILL.md | pending |
| canvas-design | creative/canvas-design/SKILL.md | pending |

### Batch D (15 skills)
| Skill | Path | Status |
|-------|------|--------|
| copilot-usage-metrics | development/copilot-usage-metrics/SKILL.md | pending |
| qwen-code | qwen-code/SKILL.md | pending |
| agent-governance | development/agent-governance/SKILL.md | pending |
| create-web-form | development/create-web-form/SKILL.md | pending |
| fine-tuning-with-trl | fine-tuning-with-trl/SKILL.md | pending |
| plantuml-ascii | creative/plantuml-ascii/SKILL.md | pending |
| legacy-circuit-mockups | creative/legacy-circuit-mockups/SKILL.md | pending |
| nano-banana-pro-openrouter | creative/nano-banana-pro-openrouter/SKILL.md | pending |
| prompt-builder | development/prompt-builder/SKILL.md | pending |
| session-audit-report | devops/session-audit-report/SKILL.md | pending |
| writing-skills | development/writing-skills/SKILL.md | pending |
| validate-memories | validate-memories/SKILL.md | pending |
| agentic-eval | development/agentic-eval/SKILL.md | pending |

## Verification

After all patches:
1. Re-judge all 51 patched skills using skill-judge criteria
2. Confirm each scores ≥ 70 (AI-ready threshold)
3. Update `remediation_verification_2026-06-14.md` with before/after scores
4. Update `skills_audit_final_report.md` with final totals

## Tracking

- [ ] Batch B (8 skills)
- [ ] Batch C (13 skills)
- [ ] Batch D (15 skills)
- [ ] frontend-design exception documented
- [ ] Re-judge all 51
- [ ] Update verification report
- [ ] Update final report
