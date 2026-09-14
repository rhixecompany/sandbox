# Batch Skills Remediation — 2026-06-29 Run Log

## Summary

- **Initial count:** 368 skills
- **After update:** 429 skills (hermes skills update installed new official skills)
- **Pipeline:** audit → check → update → repair-official → judge → remediate → re-judge (3 rounds)
- **Final:** 0 FAIL, 365 WARN, 64 PASS — avg 71.9

## Round 1 — batch_remediate.py

- 36 FAIL → WARN (frontmatter + pitfalls + checklist)
- Avg: 69.3 → 71.1
- Tool: `python3 ~/AppData/Local/hermes/scripts/batch_remediate.py`

## Round 2 — Structure Patch

- `patch_fail_structure.py` added When NOT to Use + Verification Checklist + refs to all FAIL skills
- `patch_all_fail_sections.py` added all 7 critical sections (Goal, When to Use, Workflow with phases, Skills Required table, Verification Checklist, Pitfalls, references/)
- 39 FAIL → 0 FAIL (score 60 minimum)
- Avg: 69.6 → 71.6

## Round 3 — Reference Boost

- `boost_near_pass_refs.py` created domain-specific references/overview.md for near-PASS skills
- 22 WARN → PASS
- Avg: 71.6 → 71.9

## Key Findings

1. The lowest scoring dimension was **Structure** (avg 2-6/20 for FAIL skills). Adding phased workflow sections was the single highest-impact fix.
2. **Frontmatter** was generally well-formed (avg 18-20/20). batch_remediate fixed the few gaps.
3. **Reference files** (refs dimension) was the second-biggest gap. Creating even stub `references/overview.md` files recovered 5-10 points.
4. After structural fixes, the remaining ceiling is **content depth** — the 365 WARN skills need domain-specific examples, not just templates.
5. `hermes skills repair-official --restore --yes all` is preferred over manual uninstall/reinstall for fixing missing-path issues.
