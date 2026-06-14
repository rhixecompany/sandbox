---
name: remediation-plan-remaining-51
title: Remediation Plan — Remaining 51 Skills
description: "Batch remediation plan for all 51 skills still in Needs Work (40-69) after initial major fixes. Includes exact paths, fixes, and verification tracking."
date_created: 2026-06-14
last_updated: 2026-06-14
status: in_progress
---

# Remediation Plan — Remaining 51 Skills

## Summary

| Category | Count | Score Range | Status |
|----------|-------|-------------|--------|
| Already patched (26) | 26 | 18-69 | ✅ Patched, some need re-verification |
| Needs minor fixes | 51 | 40-69 | 🔧 Remaining |
| AI-ready | 113 | 70-100 | ✅ No action |

## Remaining 51 Skills (Actual Paths)

### Batch A: DevOps (9 skills)
| Skill | Score | Path |
|-------|-------|------|
| glab | 42 | devops/glab/SKILL.md |
| jira | 42 | devops/jira/SKILL.md |
| work-on-ticket | 42 | devops/work-on-ticket/SKILL.md |
| asdf | 48 | devops/asdf/SKILL.md |
| terraform-azurerm-set-diff-analyzer | 48 | devops/terraform-azurerm-set-diff-analyzer/SKILL.md |
| azure-devops-cli | 52 | devops/azure-devops-cli/SKILL.md |
| appinsights-instrumentation | 54 | devops/appinsights-instrumentation/SKILL.md |
| customization-audit | 54 | devops/customization-audit/SKILL.md |
| fabric-lakehouse | 56 | devops/fabric-lakehouse/SKILL.md |

### Batch B: Development (14 skills)
| Skill | Score | Path |
|-------|-------|------|
| skill-creator | 49 | skill-creator/SKILL.md |
| make-repo-contribution | 51 | make-repo-contribution/SKILL.md |
| content-research-writer | 51 | creative/content-research-writer/SKILL.md |
| marp-slide | 51 | creative/marp-slide/SKILL.md |
| web-artifacts-builder | 51 | creative/web-artifacts-builder/SKILL.md |
| frontend-design | 52 | creative/frontend-design/SKILL.md |
| customize-opencode | 53 | development/customize-opencode/SKILL.md |
| mermaid-diagrams | 53 | creative/mermaid-diagrams/SKILL.md |
| template-skill | 55 | development/template-skill/SKILL.md |
| claude-api | 56 | development/claude-api/SKILL.md |
| copilot-cli | 56 | copilot-cli/SKILL.md |
| plan | 56 | software-development/plan/SKILL.md |
| projects-multi-repo-init-normalize | 56 | devops/projects-multi-repo-init-normalize/SKILL.md |
| stable-diffusion-image-generation | 56 | stable-diffusion-image-generation/SKILL.md |

### Batch C: Creative & Advanced Dev (13 skills)
| Skill | Score | Path |
|-------|-------|------|
| banking | 58 | software-development/banking/SKILL.md |
| copilot-cli-quickstart | 58 | development/copilot-cli-quickstart/SKILL.md |
| hermes-skill-library-maintenance | 58 | development/hermes-skill-library-maintenance/SKILL.md |
| qdrant-vector-search | 59 | qdrant-vector-search/SKILL.md |
| hermes-breakdown | 60 | hermes-breakdown/SKILL.md |
| simpo-training | 60 | simpo-training/SKILL.md |
| agent-browser | 61 | development/agent-browser/SKILL.md |
| using-superpowers | 61 | development/using-superpowers/SKILL.md |
| peft-fine-tuning | 62 | peft-fine-tuning/SKILL.md |
| writing-clearly-and-concisely | 62 | creative/writing-clearly-and-concisely/SKILL.md |
| algorithmic-art | 63 | creative/algorithmic-art/SKILL.md |
| brand-guidelines | 63 | creative/brand-guidelines/SKILL.md |
| canvas-design | 63 | creative/canvas-design/SKILL.md |

### Batch D: Research & Models (15 skills)
| Skill | Score | Path |
|-------|-------|------|
| copilot-usage-metrics | 65 | development/copilot-usage-metrics/SKILL.md |
| qwen-code | 65 | qwen-code/SKILL.md |
| agent-governance | 66 | development/agent-governance/SKILL.md |
| create-web-form | 67 | development/create-web-form/SKILL.md |
| fine-tuning-with-trl | 67 | fine-tuning-with-trl/SKILL.md |
| plantuml-ascii | 67 | creative/plantuml-ascii/SKILL.md |
| legacy-circuit-mockups | 68 | creative/legacy-circuit-mockups/SKILL.md |
| nano-banana-pro-openrouter | 68 | creative/nano-banana-pro-openrouter/SKILL.md |
| prompt-builder | 68 | development/prompt-builder/SKILL.md |
| session-audit-report | 68 | devops/session-audit-report/SKILL.md |
| writing-skills | 68 | development/writing-skills/SKILL.md |
| validate-memories | 45 | validate-memories/SKILL.md |
| agentic-eval | 69 | development/agentic-eval/SKILL.md |

---

## Remediation Strategy

### Common Fix Pattern (per skill)

Each fix applies:
1. **Frontmatter**: Add `version`, `author`, `license`, `tags` if missing
2. **Skills Required**: Add cross-reference table
3. **Pitfalls**: Add 3-5 common mistakes section
4. **Verification Checklist**: Add 5-8 item checklist
5. **Content gaps**: Add concrete examples where only prose exists

### Execution Order

1. **Batch A** (DevOps) — 9 skills
2. **Batch B** (Development) — 14 skills
3. **Batch C** (Creative/Advanced) — 13 skills
4. **Batch D** (Research/Models) — 15 skills
5. **Re-judge all 51**
6. **Update final report**

### Verification Gate

After each batch:
- [ ] All skills patched
- [ ] Re-judge confirms score ≥ 70 for each skill
- [ ] Log saved to `remediation_verification_2026-06-14.md`

---

## Saved Plan Location

`.hermes/plans/2026-06-14_remaining-remediation-plan.md`

---
**Status:** Ready to execute Batch A (devops/glab, devops/jira, devops/work-on-ticket)
