# Skill-Judge Audit Summary — 2026-06-16

## Results
- **Total skills scored:** 352
- **✅ AI-ready (≥80):** 24 skills (6.8%)
- **⚠️ Needs work (60-79):** 217 skills (61.6%)
- **🔴 Rewrite (<60):** 111 skills (31.5%)
- **Below 80 total:** 328 skills

## Top 10 Highest-Scored Skills
| Score | Skill |
|-------|-------|
| 90 | pretext |
| 89 | test-driven-development |
| 88 | skills |
| 88 | plans-and-specs |
| 88 | hermes-skills |
| 88 | enhance-markdown |
| 88 | documentation-extraction-and-indexing |
| 88 | code-wiki |
| 88 | baoyu-comic |
| 87 | hyperframes |

## Bottom 10 Lowest-Scored Skills
| Score | Skill |
|-------|-------|
| 30 | drawio-skill |
| 30 | playwright-automation-fill-in-form |
| 30 | playwright-generate-e2e-test |
| 30 | playwright-generate-test |
| 31 | scoutqa-test |
| 33 | transloadit-media-processing |
| 34 | postgresql-code-review |
| 34 | snowflake-semanticview |
| 35 | ci-cd-best-practices |
| 35 | gh-cli |

## Planning Skills (Post-Enhancement)
| Skill | Score | Rating | Notes |
|-------|-------|--------|-------|
| brainstorming | 65 | ⚠️ | Enhanced after audit — re-judge needed |
| plans-and-specs | 88 | ✅ | Enhanced after audit — score already good |
| prompt-planning-orchestration | 60 | ⚠️ | Enhanced after audit — re-judge needed |

## Score Distribution
| Score Range | Count |
|-------------|-------|
| 90-100 | 1 |
| 85-89 | 6 |
| 80-84 | 17 |
| 75-79 | 0 |
| 70-74 | 42 |
| 65-69 | 40 |
| 60-64 | 77 |
| 55-59 | 33 |
| 50-54 | 27 |
| 45-49 | 27 |
| 40-44 | 24 |
| 35-39 | 18 |
| 30-34 | 10 |

## Common Issues (Below 80)
1. **Missing frontmatter fields** — ~50% missing version, author, license, or tags
2. **No Skills Required table** — ~90% missing
3. **No pitfalls section** — ~60% missing
4. **No verification checklist** — ~70% missing
5. **No reference files** — ~50% missing refs/, templates/, scripts/
6. **Thin content** — Many skills are <100 lines with only bullet points
7. **No workflow phases** — Many lack structured Phase 1-4 workflows

## Remediation Priority
1. **🔴 <60 (111 skills)** — Full rewrite needed
2. **⚠️ 60-79 (217 skills)** — Targeted patches (frontmatter, Skills Required, pitfalls, verification)
3. **✅ ≥80 (24 skills)** — No action needed

## Data Files
- Full results: `judge_results/all_results.tsv` (352 entries)
- Batch files: `judge_results/batch_0001_results.md` through `batch_0051_results.md`
- Format: `skill_name|path|score|rating|dim1|dim2|dim3|dim4|dim5|lines`
