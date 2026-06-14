# Batch 28 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 28 (Skills 190-191)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 190 | worktrunk | 58/100 | ⚠️ Needs work | Diverged clone pattern, no wt.toml/hook examples |
| 191 | writing-plans | 77/100 | ✅ AI-ready | 7-step process, plan template, DRY/YAGNI/TDD |

**Aggregate:** 1/2 AI-ready, 1/2 Need work

---

## FINAL TOTALS (All 28 Batches, 191 skills)

| Category | Count | Percentage |
|----------|-------|------------|
| ✅ AI-ready | 96/191 | 50% |
| ⚠️ Needs work | 89/191 | 47% |
| 🔴 Rewrite | 6/191 | 3% |

---

## Top 10 Highest-Scored Skills

| Rank | Skill | Score | Batch |
|------|-------|-------|-------|
| 1 | django-celery | 85 | 23 |
| 2 | web-research-pipeline | 84 | 24 |
| 3 | 3-statement-model | 83 | 23 |
| 4 | bash-scripts-audit-remediation | 83 | 25 |
| 5 | accelerate | 82 | 23 |
| 6 | repo-research-pipeline | 82 | 24 |
| 7 | subagent-driven-development | 81 | 22 |
| 8 | godmode | 81 | 24 |
| 9 | systematic-debugging | 80 | 22 |
| 10 | executing-plans | 80 | 26 |

## Bottom 10 Lowest-Scored Skills (Rewrite Candidates)

| Rank | Skill | Score | Batch |
|------|-------|-------|-------|
| 1 | template | 35 | 4 |
| 2 | ai-prompt-engineering-safety-review | 22 | 8 |
| 3 | context-map | 21 | 8 |
| 4 | convert-plaintext-to-md | 21 | 8 |
| 5 | skills | 21 | 11 |
| 6 | rbac-audit-logging | 18 | 16 |
| 7 | create-readme | 38 | 10 |
| 8 | vscode-ext-commands | 38 | 12 |
| 9 | azure-role-selector | 38 | 13 |
| 10 | vscode-ext-localization | 39 | 12 |

## Cross-Cutting Issues (All 191 Skills)

| Issue | Frequency |
|-------|-----------|
| Missing `version` in frontmatter | ~54% |
| Missing `license` in frontmatter | ~53% |
| Missing `tags` in frontmatter | ~56% |
| Missing `author` in frontmatter | ~53% |
| No Skills Required table | ~100% |
| No verification checklist | ~91% |
| No pitfalls section | ~42% |
| SKILL.md >250 lines | ~18% |
| Orphaned/unverified reference files | ~46% |

## Next Steps (Per Plan)

1. **Remediate failures** — Patch/fix the 89 "Needs work" + 6 "Rewrite" skills
2. **Re-judge patched skills** — Confirm they pass after fixes
3. **Final report** — Create `skills_audit_final_report.md`
