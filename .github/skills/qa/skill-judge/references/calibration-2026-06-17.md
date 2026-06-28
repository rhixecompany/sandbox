# 2026-06-17 Full Audit Calibration Data

## Scope
- **Skills scored:** 352 (all SKILL.md files under `~/.hermes/skills/`)
- **Date:** 2026-06-17
- **Judge version:** skill-judge v1.1.0
- **Output format:** TSV (`skill_name|path|score|rating|dim1|dim2|dim3|dim4|dim5|lines`)

## Results Summary
| Category | Count | Percentage |
|----------|-------|------------|
| ✅ AI-ready (≥80) | 24 | 6.8% |
| ⚠️ Needs work (60-79) | 217 | 61.6% |
| 🔴 Rewrite (<60) | 111 | 31.5% |
| **Below 80 total** | **328** | **93.2%** |

## Score Distribution
| Score | Count |
|-------|-------|
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

## Key Findings
1. **Content depth is the bottleneck**: Most skills scoring 60-79 have correct structure but lack concrete examples, templates, or reference files.
2. **The references/ pattern works**: plans-and-specs scored 88 after moving 6 class-pattern sections to references/ (289→147 lines).
3. **Bottom skills are thin stubs**: Skills scoring 30-35 are typically <100 lines with only bullet points.

## Remediation Strategy
- **60-79 range**: Add concrete examples, create reference files, expand workflow phases
- **<60 range**: Full rewrite with frontmatter, Skills Required, phases, pitfalls, verification, references
