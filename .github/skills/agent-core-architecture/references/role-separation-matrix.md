# Role Separation Verification Matrix

After each restructure or enhancement round, verify separation holds:

```bash
# Confirm SOUL.md owns behavioral rules — USER.md doesn't restate them
grep -ci "persona\|cognitive\|architectural\|invariant\|execution framework" USER.md

# Confirm USER.md owns preferences — MEMORY.md doesn't duplicate them
grep -ci "planning style\|prompting preference\|skill utilization" MEMORY.md

# Confirm MEMORY.md owns heuristics — SOUL.md doesn't log session-level facts
grep -ci "workspace has\|skill-patching blocker\|msys2" SOUL.md

# All three should return 0
```

## Round Sequence Example (2026-07-24 session)

This session processed 3 reference docs in sequence:

1. **Round 1**: "Rule examples for core agent files" — added 8 items (sharp opinions, breakdown rule, inheritance rule, constraint rule, discovery rule, credential isolation, pre_exec hook, post_exec hook) + updated USER.md with comm pref + environment stack + MEMORY.md with archival/anti-bloat rules + created pre-exec-validate.sh + post-exec-state-log.py

2. **Round 2**: "Comparison of File Responsibilities" — added Architectural Invariants section (4 subsections), restructured USER.md into 4 workflow sections (Planning Style, Prompting, Skill Utilization, Hooks), restructured MEMORY.md into 4 categories with 8 sub-sections

3. **Round 3**: "Example rules tailored for SOUL.md/USER.md/MEMORY.md" — added Intent-Driven Formatting, expanded pre_flight to include env check, added incremental plans/approval gates/light wit/preferred stack/.env.local to USER.md, added 8 template sub-sections to MEMORY.md

Key principle: each round only adds genuinely new rules — never re-adds what was already incorporated.
