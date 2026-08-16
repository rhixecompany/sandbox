# Batch Frontmatter Audit Pattern

Real-world example from a 213-file prompt library:

**Problem:** 197/213 `.prompt.md` files had duplicate entries in their YAML `tags:` lists (each tag appeared twice). 6 files had `title:` equal to the kebab-case `name:` instead of a human-readable string.

**Pattern used (audit → classify → fix → verify → cleanup):**

1. **Phase 1 — Scan:** Write a Python script that reads every target file, parses YAML frontmatter (via `yaml.safe_load`), checks for each issue category. Output JSON with per-file issue list.
2. **Phase 2 — Classify:** Aggregate issue types across all files. Identify which can be fixed deterministically (dup tags, missing fields) vs which need judgement (wrong titles).
3. **Phase 3 — Fix in batches:** For each issue category, write a targeted fix script. Parse frontmatter, edit the dict, dump back with `yaml.dump(sort_keys=False)`. Or for simple cases, parse the raw YAML block line-by-line to preserve formatting while deduplicating. Apply in batches of 10+ files, then re-validate.
4. **Phase 4 — Verify independently:** Write a SEPARATE verification script (different code path than the fixer). Run it to confirm zero remaining issues before marking done. The fixer's self-report is never sufficient proof.
5. **Phase 5 — Clean up:** Remove temporary auditor/fixer scripts after completion. No stale artifacts left in the workspace.

**Key lesson:** A single audit script run first saves guessing. Classifying issues by type before fixing avoids random one-off edits. An independent verifier prevents self-deception about fix quality.
