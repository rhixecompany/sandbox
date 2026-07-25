# Batch Audit Findings — Skill Library Quality Pipeline

**Date:** 2026-06-14
**Auditor:** skill-judge v1.1.0 via default profile
**Scope:** 191 local skills, 28 batches × 7 skills (last batch = 2)
**Status:** COMPLETE — all 28 batches judged

---

## Final Score Distribution (191 Skills)

| Score Range | Count | Category |
|-------------|-------|----------|
| 80-100 | 28 | Excellent |
| 70-79 | 35 | Good |
| 60-69 | 23 | Acceptable |
| 50-59 | 17 | Below average |
| 40-49 | 28 | Needs work |
| 30-39 | 12 | Poor |
| 20-29 | 5 | Very poor |
| 0-19 | 1 | Placeholder |

**Final Tally:** 96 AI-ready (50%), 89 Needs work (47%), 6 Rewrite (3%)

---

## Cross-Batch Patterns (All 191 Skills)

| Issue | Count | % of 191 |
|-------|-------|----------|
| No Skills Required table | 191 | 100% |
| No verification checklist | 174 | 91% |
| Missing `version` in frontmatter | 103 | 54% |
| Missing `license` in frontmatter | 104 | 54% |
| Missing `tags` in frontmatter | 107 | 56% |
| Missing `author` in frontmatter | 102 | 53% |
| No phased workflow | 56 | 29% |
| No pitfalls section | 80 | 42% |
| SKILL.md >250 lines | 34 | 18% |
| Orphaned/unverified reference files | 88 | 46% |

---

## Pure Placeholder Skills (Rewrite Required)

| Skill | Score | Batch | Issue |
|-------|-------|-------|-------|
| `template` | 35 | 4 | Must be exemplary; has placeholder text |
| `ai-prompt-engineering-safety-review` | 22 | 8 | Pure placeholder |
| `context-map` | 21 | 8 | Pure placeholder |
| `convert-plaintext-to-md` | 21 | 8 | Pure placeholder |
| `skills` | 21 | 11 | Pure placeholder |
| `rbac-audit-logging` | 18 | 16 | Pure placeholder |

---

## Template-in-Skill-Body Anti-Pattern

**Skills affected (3):**
- `architecture-blueprint-generator` (42/100)
- `folder-structure-blueprint-generator` (41/100)
- `technology-stack-blueprint-generator` (44/100)

**Fix:** Move template to `templates/blueprint.md`; keep SKILL.md <250 lines.

---

## Generic Boilerplate Verification Checklists

**Pattern:** Identical 5-item checklist copied verbatim across 15+ skills. Replace with skill-specific verification gates.

---

## Long Skills Needing Split (>250 lines, 28 skills)

Top offenders: copilot-cli-quickstart (769), refactor (645), excalidraw-diagram-generator (660), agent-governance (572), lambda-labs-gpu-cloud (549), hermes-skill-library-maintenance (557), stable-diffusion-image-generation (523), qdrant-vector-search (497), godmode (408), quasi-coder (389), bun-shell (393), systematic-debugging (392), test-driven-development (537), subagent-driven-development (460), django-celery (457), 3-statement-model (433), writing-plans (357), executing-plans (316), script-orchestration (323), bun-nextjs (322), web-design-reviewer (370)

---

## Top 20 Highest-Scored Skills

| Rank | Skill | Score |
|------|-------|-------|
| 1 | django-celery | 85 |
| 2 | web-research-pipeline | 84 |
| 3 | 3-statement-model | 83 |
| 4 | bash-scripts-audit-remediation | 83 |
| 5 | accelerate | 82 |
| 6 | repo-research-pipeline | 82 |
| 7 | subagent-driven-development | 81 |
| 8 | godmode | 81 |
| 9 | systematic-debugging | 80 |
| 10 | executing-plans | 80 |
| 11 | test-driven-development | 79 |
| 12 | debugging-hermes-tui-commands | 79 |
| 13 | web-design-reviewer | 78 |
| 14 | fluentui-blazor | 78 |
| 15 | refactor | 78 |
| 16 | spike | 77 |
| 17 | writing-plans | 77 |
| 18 | quasi-coder | 76 |
| 19 | script-orchestration | 76 |
| 20 | mindstudio-wrapper | 76 |

---

## Remediation Priority (Top 20)

| Rank | Skill | Score | Primary Issue |
|------|-------|-------|---------------|
| 1 | template | 35 | Placeholder — must be exemplary |
| 2 | rbac-audit-logging | 18 | Pure placeholder |
| 3 | ai-prompt-engineering-safety-review | 22 | Pure placeholder |
| 4 | context-map | 21 | Pure placeholder |
| 5 | convert-plaintext-to-md | 21 | Pure placeholder |
| 6 | skills | 21 | Pure placeholder |
| 7 | create-readme | 38 | Minimal |
| 8 | vscode-ext-commands | 38 | Minimal |
| 9 | azure-role-selector | 38 | Single paragraph |
| 10 | vscode-ext-localization | 39 | Minimal |
| 11 | folder-structure-blueprint-generator | 41 | Template-in-body |
| 12 | httpie | 42 | No examples |
| 13 | receiving-code-review | 42 | Minimal |
| 14 | architecture-blueprint-generator | 42 | Template-in-body |
| 15 | clonedeps | 44 | Generic |
| 16 | codemap | 44 | Generic |
| 17 | webapp-testing | 44 | No Playwright code |
| 18 | technology-stack-blueprint-generator | 44 | Template-in-body |
| 19 | code-docs | 46 | No examples |
| 20 | shadcn | 46 | No CLI examples |

---

## Notes for Future Auditors

1. Use read_file() with absolute paths — bypasses skill_view resolution bugs
2. Verify reference files on disk — each cited ref must exist and be >3 lines
3. Calibrate on Batch 1 — lock thresholds; criterion drift is real across 28 batches
4. Placeholder skills — score <40, flag for rewrite not patch
5. Scoring caps — placeholder caps at 40; no verification checklist caps at 70; >250 lines caps DRY at 10
6. Profile visibility — running from default profile may not see all skills; use absolute paths
