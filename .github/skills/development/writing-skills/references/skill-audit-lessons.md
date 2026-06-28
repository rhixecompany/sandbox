# Skill Audit Patterns — Lessons from 2026-06-14 Audit

## Anti-Pattern: Template-in-Skill-Body

**Found in 4 skills:** architecture-blueprint-generator, folder-structure-blueprint-generator, technology-stack-blueprint-generator, template

**Problem:** Skills embed massive parameterized templates (200-500+ lines) directly in SKILL.md instead of:
1. Keeping SKILL.md <250 lines as the skill-judge criteria requires
2. Moving templates to `references/` or `templates/` directories
3. Referencing them with one-line pointers from SKILL.md

**Fix:** Split template into separate file:
- `templates/architecture-blueprint-template.md` — the full parameterized template
- `references/architecture-patterns.md` — pattern catalog
- SKILL.md references: `See templates/architecture-blueprint-template.md for the full generator template`

## Systemic Issues Across All 35 Skills Audited

| Issue | Count | % | Root Cause |
|-------|-------|-----|------------|
| No Skills Required table | 35 | 100% | Not in template, not enforced |
| No verification checklist | 32 | 91% | Not in template, not enforced |
| Missing `version` | 14 | 40% | Not in template |
| Missing `license` | 14 | 40% | Not in template |
| Missing `tags` | 16 | 46% | Not in template |
| Missing `author` | 13 | 37% | Not in template |
| No phased workflow | 13 | 37% | Template only says "suggested" |
| No pitfalls section | 14 | 40% | Not in template |
| SKILL.md >250 lines | 9 | 26% | Template-in-skill-body, no DRY enforcement |
| Orphaned/unverified refs | 16 | 46% | References cited but not created/verified |

## Root Cause: The Template Skill Was Broken

The `template` skill (which all new skills copy from) scored **35/100** and had:
- Broken frontmatter (missing version, license, author, tags)
- Placeholder text ("fill in the content")
- No Skills Required table
- No phased workflow
- No pitfalls section
- No verification checklist
- No reference files

**Lesson:** The template for creating skills MUST itself be exemplary (AI-ready ≥70). If the template is broken, every skill created from it inherits the brokenness.

## Remediation Priority

1. **Fix the template skill first** — it's the source of truth for all new skills
2. **Add enforcement to skill-judge** — it now has hard floors for checklist, placeholder text, line count
3. **Create exemplars** — writing-skills, enhance-markdown, skill-judge should be reference implementations
4. **Batch-remediate existing skills** — apply fixes in priority order from audit

## Best Practice: Reference File Structure

For skills with substantial reference material:

```
skill-name/
├── SKILL.md              # <250 lines, core pattern + one-line ref pointers
├── references/
│   ├── evaluation-criteria.md    # Detailed scoring rubric
│   ├── frontmatter-template.md   # Frontmatter standards
│   ├── advanced-usage.md         # Extended patterns
│   └── troubleshooting.md        # Common issues
├── templates/
│   └── blueprint-template.md     # Full parameterized templates
└── scripts/
    └── verify.py                 # Verification scripts
```

**Key principle:** SKILL.md is the entry point. References are for depth. Templates are for copying. Scripts are for running.