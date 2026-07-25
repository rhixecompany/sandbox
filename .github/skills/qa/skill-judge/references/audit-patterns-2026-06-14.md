# Batch Audit Patterns — 2026-06-14

## Audit Scope
- 191 local skills across 28 batches of 7
- Scored on 5 dimensions (Frontmatter, Structure, Content, DRY, References) / 100

## Score Distribution
| Score | Count | Category |
|-------|-------|----------|
| 80-100 | 28 | Excellent |
| 70-79 | 35 | Good |
| 60-69 | 23 | Acceptable |
| 50-59 | 17 | Below average |
| 40-49 | 28 | Needs work |
| 30-39 | 12 | Poor |
| 20-29 | 5 | Very poor |
| 0-19 | 1 | Placeholder |

## Universal Missing Elements (All 191 Skills)
| Section | Present | Missing | Coverage |
|---------|---------|---------|----------|
| Skills Required table | 0 | 191 | 0% |
| Verification checklist | 17 | 174 | 9% |
| Pitfalls section | 111 | 80 | 58% |
| Reference files | 72 | 119 | 38% |
| version in frontmatter | 88 | 103 | 46% |
| author in frontmatter | 89 | 102 | 47% |
| license in frontmatter | 87 | 104 | 46% |
| tags in frontmatter | 84 | 107 | 44% |

## Template-in-Skills Anti-Pattern
**Affected skills:** folder-structure-blueprint-generator, architecture-blueprint-generator, technology-stack-blueprint-generator

**Problem:** 300+ line parameterized prompt templates embedded directly in SKILL.md body. Scores poorly on DRY (capped at 10/20 for >250 lines) and Structure.

**Fix:** Move template content to templates/blueprint-template.md, replace SKILL.md body with concise workflow guide pointing to template. Score improvement: 41-44 to 70+.

## Placeholder Skills (Score less than 25)
- template (35) — useful as template, not executable
- ai-prompt-engineering-safety-review (22) — pure placeholder
- context-map (21) — pure placeholder
- convert-plaintext-to-md (21) — pure placeholder
- skills (21) — pure placeholder
- rbac-audit-logging (18) — pure placeholder

**Signal:** "This skill is a placeholder and needs to be filled in" + [Add ... here] text patterns.

## Top 10 Highest-Scored Skills
1. django-celery (85) — Complete celery.py, 5 task patterns, canvas, DLQ, production checklist
2. web-research-pipeline (84) — 4-phase, end-to-end code, slugify, verification checklist
3. 3-statement-model (83) — Formulas over hardcodes, 9 validation categories
4. bash-scripts-audit-remediation (83) — 6-phase pipeline, 12 refs, 19-item checklist
5. accelerate (82) — 4-line conversion, 5 workflows
6. repo-research-pipeline (82) — 6-phase, cross-ref symmetry, 8 gates
7. subagent-driven-development (81) — 4-step workflow, 2-stage review
8. godmode (81) — 3 attack modes, auto_jailbreak, tested results
9. systematic-debugging (80) — 4-phase, Iron Law, rule of 3
10. executing-plans (80) — Batch processing, bulk sweeps, cross-platform

## Skill Name Collision Pairs
When skill_view() returns "Ambiguous skill name":
- accelerate / huggingface-accelerate — shorter name is canonical
- cli / inference-sh-cli — shorter name is canonical
- ideation / creative-ideation — shorter name is canonical
- lambda-labs / lambda-labs-gpu-cloud — shorter name is canonical
- modal / modal-serverless-gpu — shorter name is canonical
- skills (in development/) / hermes-skills — different skills, use full path

**Fix:** Use read_file() with absolute path instead of retrying skill_view().

## Profile Visibility Issues
- skill_manage() from default profile may report "Skill not found" for skills in category subdirectories
- skill_view() same limitation
- **Workaround:** Use read_file() with absolute path, or patch() with absolute path parameter

## Remediation Priority
1. **Rewrite (6 skills)**: All pure placeholders to complete rewrites with real content
2. **Major fix (20 skills)**: Score 40-49 to add concrete examples, workflows, pitfalls
3. **Minor fix (69 skills)**: Score 50-69 to add frontmatter fields, Skills Required, pitfalls, verification
4. **Result**: 26 skills fixed in session, ~69 minor fixes remaining

## Context Window Management for Large Audits
- Process in batches of 7 skills max
- Write results to judge_batch_N_results.md after each batch
- Do NOT retain full skill text between batches
- After compaction/resume, re-read batch result files — don't trust in-context running counts
- Final totals: reconcile from 28 batch files, not from memory
