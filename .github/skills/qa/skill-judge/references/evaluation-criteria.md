# Skill Judge Evaluation Criteria — Reference

**Version:** 1.1.0
**Companion to:** skill-judge SKILL.md

---

## Dimension 1: Frontmatter Compliance (20 pts)

| Field | Points | Required | Notes |
|-------|--------|----------|-------|
| `name` | 3 | Yes | Lowercase, hyphens only |
| `title` | 3 | Yes | Human-readable |
| `description` | 3 | Yes | ≤500 chars, starts with "Use when..." for triggered skills |
| `version` | 3 | Yes | Semver preferred |
| `author` | 3 | Yes | |
| `license` | 3 | Yes | SPDX identifier (MIT, Apache-2.0, etc.) |
| `tags` | 2 | Yes | Array format `tags: [tag1, tag2]` under `metadata.hermes.tags` or root `tags` |

**Deductions:**
- `trigger:` in skill frontmatter: -3 (that's for prompt files)
- Non-standard fields don't count toward score
- Missing required field: -points for that field

**Pass threshold:** ≥14/20 (all required fields present)

---

## Dimension 2: Structure & Organization (20 pts)

| Criterion | Points | How to Verify |
|-----------|--------|---------------|
| Skills Required table present | 4 | Markdown table with `| Skill | Purpose |` header in body |
| Phased workflow (≥3 phases) | 4 | `## Phase 1`, `## Phase 2`, etc. or `### Step 1` |
| Pitfalls section present | 4 | `## Pitfalls` or `## Common Mistakes` with actionable items |
| Verification checklist at end | 4 | `## Verification Checklist` with `- [ ]` items |
| Reference files exist & substantive | 4 | `skill_view(name, 'references/...')` each ref; >3 lines |

**Pass threshold:** ≥12/20

---

## Dimension 3: Content Quality (20 pts)

| Criterion | Points | How to Verify |
|-----------|--------|---------------|
| Resumability (entry checks) | 4 | Each phase has "Entry check: if X exists → skip to Y" |
| Error handling | 4 | `## Common Issues` or error cases in workflow with solutions |
| Platform detection/fallback | 4 | Windows/Linux/macOS differences addressed, or cross-platform notes |
| Concrete examples/templates | 4 | Runnable code blocks, not just prose descriptions |
| No placeholder text | 4 | Search for `[Add`, `TODO`, `FIXME`, `[...]` — any = -4 |

**Auto-fail:** Placeholder text present → max 60 total score
**Pass threshold:** ≥12/20

---

## Dimension 4: DRY Compliance (20 pts)

| Criterion | Points | How to Verify |
|-----------|--------|---------------|
| No duplicate content across sections | 5 | Search for repeated paragraphs/tables |
| No duplicate content vs reference files | 5 | Compare SKILL.md content with `references/` files |
| SKILL.md <250 lines | 5 | `wc -l SKILL.md` — if >250, cap at 10/20 for this dimension |
| Cross-reference consistency | 5 | Sections reference each other correctly (e.g., Phase 2 cites refs from Phase 1) |

**Hard cap:** >250 lines → Dimension 4 max = 10/20
**Pass threshold:** ≥12/20 (or ≥10 if >250 lines)

---

## Dimension 5: Reference Files (20 pts)

| Criterion | Points | How to Verify |
|-----------|--------|---------------|
| All 3 ref types present (where applicable) | 5 | `references/`, `templates/`, `scripts/` each have ≥1 file if skill needs them |
| Each ref file substantive (>3 lines) | 5 | `read_file()` each; count lines; stubs = -1 each |
| Refs cited from SKILL.md body | 5 | One-line pointer like "See `references/xyz.md` for details" |
| No orphaned reference files | 5 | Every file in `references/`, `templates/`, `scripts/` is cited in SKILL.md |

**Penalty:** Cited ref missing on disk = -1 to -3 per missing ref
**Pass threshold:** ≥10/20

---

## Score Bands

| Total Score | Rating | Action |
|-------------|--------|--------|
| ≥70 | ✅ AI-ready | Minor fixes only |
| 40–69 | ⚠️ Needs work | Patch required |
| <40 | ❌ Rewrite | Rebuild from scratch |

---

## Calibration Notes (2026-06 Audit)

- **Frontmatter:** 46% missing `version`, 50% missing `tags` — common gap
- **Structure:** 93% missing verification checklist, 100% missing Skills Required table
- **Content:** Placeholder text in 2 skills → auto-cap at 60
- **DRY:** 20% >250 lines — mostly blueprint generators
- **References:** 43% have orphaned/unverified refs — always verify on disk

---

## Quick Scoring Checklist (for batch audit)

```
Skill: _______________
Lines: _____

[ ] Frontmatter: name / title / desc / version / author / license / tags
[ ] Skills Required table
[ ] Phased workflow (≥3)
[ ] Pitfalls section
[ ] Verification checklist
[ ] Reference files cited
[ ] Ref files exist on disk
[ ] Ref files >3 lines
[ ] No placeholder text
[ ] <250 lines
[ ] Concrete examples
[ ] Error handling
[ ] Platform notes
[ ] Entry checks (resumability)

Score: ___/100 →  [ ] AI-ready  [ ] Needs work  [ ] Rewrite
```