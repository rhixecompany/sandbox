# Multi-Group Skill Library Consolidation (Class Pattern)

For large-scale consolidation of many skills into umbrella groups.

## Safety-First Backup
Before any mutations, create timestamped backup at `%LOCALAPPDATA%/hermes/skills-backup/<UTC-TIMESTAMP>`. Copy all SKILL.md files + support dirs. Write `manifest.json`.

## Tool Quirks
- `skill_manage(action='delete', absorbed_into='x')` archives (doesn't remove). Use `rm -rf` for true deletion.
- `skill_manage` can't resolve `software-development/` skills by bare name — use `rm -rf` for those.
- `skill_view()` returns stale cached content — use `read_file(path=...)` for post-patch verification.
- `absorbed_into` must reference existing skill by bare name only (no `/` paths).

## Per-Group Execution
1. Enrich umbrella SKILL.md (phases, "Absorbed Skills" table, cross-refs)
2. Archive sub-skills as ARCHIVED stubs pointing to umbrella
3. Delete thin stubs with `rm -rf` (body_lines ≤ 10, no unique content)
4. Verify on disk, not via skill_view()
5. Record all absorbed skills in umbrella's SKILL.md

## Example Result (2026-06-13)
645 → 622 skills. Agent delegation (13→5), GitHub (11→3), Hermes self-mgmt (18→4), Planning/breakdown (13→2), Maintenance stubs (9→0).
