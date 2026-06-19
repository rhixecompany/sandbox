# PROMPTS-AUDIT Fix Progress Log

**Purpose**: `prompts-audit` — Fix application progress tracking

**Generated**: 2026-06-17 | Plan: `thoughts/plans/prompts-debug.md`

---

## Batch 1 — Proof of Concept (7 files)

| # | File | Issues Targeted | Channel | Status | Verified |
|---|------|-----------------|---------|--------|----------|
| 1 | `Prompts/dev-init.prompts.md` | 1H, 16M | B (complex) | ✅ Fixed | ✅ Verified |
| 2 | `Prompts/repo-management.prompts.md` | 1H, 3M | B (parse error) | ✅ Fixed | ✅ Verified |
| 6 | `Prompts/agents-fix.prompts.md` | 1H | B | ✅ Fixed | ✅ Verified |

> After re-run: files 1–3 and 6 now have 0 first-60-lines frontmatter issues. Cases 4–5 already had valid frontmatter; their reported HIGHs were false-positive double-/unclosed-fence detections.

> Case 7 was a separate verification issue (empty zombie file).

---

## Fix Commands Reference

### Channel A (Plugin/Automation)
```bash
# Run enhance-markdown on single file
/enhance-markdown path/to/file.md prompts-audit
```

### Channel B (Manual Patches)
```bash
# Fix unclosed frontmatter: insert --- before first heading
# Fix double fence: remove extra --- markers
# Fix parse error: fix line 33 in repo-management.prompts.md
# Fix empty file: rm or populate zod-schema-generation.prompt.md
# Fix duplicate headings: rename with prefixes
# Fix hierarchy: insert missing ## levels
# Fix extension: mv old new
# Trim whitespace: sed -i 's/[[:space:]]*$//' file
```

---

## Verification Checklist (per file)

After each fix, run:
- [ ] `python3 -c "import yaml; yaml.safe_load(open('file').read().split('---')[1])"` — parses clean
- [ ] `grep -n '^---$' file | head -5` — exactly 2 fences
- [ ] `grep -A5 '^skills:' file | head -6` — no prose entries
- [ ] Heading hierarchy check — no level skips
- [ ] Extension convention matches directory

---

## Progress Notes

---
*Batch 1 start: 2026-06-17*
