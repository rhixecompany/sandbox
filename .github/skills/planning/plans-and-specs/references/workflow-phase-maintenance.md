# Multi-Phase Workflow Document Maintenance

When a driving `.prompts.md` or `PLAN.md` has a structured phase list and you need to add, remove, or reorder phases.

## Cross-Reference Sections That Must Stay in Sync

| Section | What to update |
|---------|---------------|
| Frontmatter `description:` | Bump phase counts, add new priorities |
| Frontmatter `tags:` | Add new domain tags |
| Frontmatter `dependencies:` / `skills:` | Add skills needed by new phases |
| Top-level summary | Renumber priorities, extend text |
| Priority tiers table | Insert new tiers, renumber subsequent |
| Phase sections (the body) | Insert new `### Phase N:` blocks |
| Skill cross-reference table | Add rows for each new phase |
| Verification gate script | Add checks for new phase deliverables |
| Pitfalls list | Add phase-specific pitfalls |
| Actions list | Add tool/skill refs needed by new phases |

## Rules
- If you add a phase but miss any cross-ref section, the document becomes self-contradictory
- Per-repo optimization/debt work must come BEFORE consolidation/merge phases
- Before closing, check tail of file for orphaned duplicate sections
- Run `grep -c '```'` parity check for unclosed code fences
