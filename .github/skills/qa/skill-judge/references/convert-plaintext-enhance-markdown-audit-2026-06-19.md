# Case Study: Audit of convert-plaintext-to-md & enhance-markdown (2026-06-19)

## Summary

Applied skill-judge v1.1.0 criteria to two markdown-related skills. Both achieved AI-ready (≥70) after targeted fixes.

## convert-plaintext-to-md

**Before:** 64/100 (⚠️ Needs work)
**After:** 92/100 (✅ AI-ready)

### Gaps Found (Dimensions 2, 3, 5)

| Dimension | Missing | Fix Applied |
|-----------|---------|-------------|
| Structure | No reference files | Created 4 reference files in `references/` |
| Content Quality | No entry checks, no error handling, no platform fallback | Added entry checks to all 4 phases; error handling for file-not-found/empty/permissions; platform detection section |
| References | Zero reference files | Added: `conversion-patterns.md`, `heading-hierarchy.md`, `code-block-detection.md`, `verification-patterns.md` |

### Key Pattern

Skills doing file transformation need:
1. **Resumability artifacts** per phase (analysis-{basename}.json, converted-{basename}.md, etc.)
2. **Explicit error handling** for: file-not-found, empty input, permission denied, missing prior artifacts
3. **Platform fallback** documentation (Windows/Unix/Node/Python)
4. **Reference files** for pattern tables, validation rules, detection heuristics, verification implementations

## enhance-markdown

**Before:** 88/100 (✅ AI-ready)
**After:** 91/100 (✅ AI-ready)

### Gap Found (Dimension 1)

| Issue | Fix |
|-------|-----|
| Description didn't start with "Use when..." despite having triggers (`/enhance-markdown`, "enhance markdown") | Rewrote description to lead with "Use when auditing and enhancing markdown files..." |

### Note

Already strong: 15 substantive reference files, all phases have entry checks, comprehensive verification gates. Only frontmatter description format needed correction.

## Skill-Judge Criteria Validation

The 5-dimension rubric correctly identified:
- Critical structural gaps (missing references = 0/20 on References dimension)
- Frontmatter compliance nuances (description format for triggered skills)
- Content quality requirements (resumability, error handling, platform fallback)

## Reusable Audit Checklist for Similar Skills

When auditing file-transformation or markdown-processing skills:
- [ ] Check for reference files (conversion patterns, validation rules, detection heuristics)
- [ ] Verify entry checks at each phase (resumability)
- [ ] Verify error handling for: not-found, empty, permissions, missing artifacts
- [ ] Verify platform fallback documentation
- [ ] Check frontmatter description starts with "Use when..." for triggered skills
- [ ] Verify SKILL.md <250 lines (move detail to references/)
- [ ] Verify all reference files cited from SKILL.md body