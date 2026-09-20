# Spec: Skill registry cleanup and duplicate consolidation

**Feature**: Inspect skills from `jsmastery-pro/skills` (13) and `vercel-labs/agent-skills` (10); install confirmed; consolidate duplicates; verify best categorized version at profile-dir (`$HERMES_HOME/skills/`).

**Design decisions (confirmed via clarify)**:
- Inspect before install (not install-all-first)
- Best categorized version = profile-directory match (`$HERMES_HOME/skills/`); delete others
- Scope/plans/specs cover this feature
- Delete duplicates immediately after identifying best; no synthetic results

## Build plan
1. Inspect remaining skills (`architect`, `audit` from jsm; 3 vercel timeouts)
2. Confirm install per non-timeout skill (batch 1 results shown)
3. Re-inspect timeouts or skip
4. Identify duplicates against 162 hub skills
5. Confirm best version per duplicate group
6. Delete duplicates
7. Verify with audit/spec evidence

## Evidence rules
- All `hermes skills inspect` results preserved (real exit codes; timeouts documented honestly)
- No fabricated session IDs / capabilities / rankings
- `.env` untouched (size-only verification; never read contents)
