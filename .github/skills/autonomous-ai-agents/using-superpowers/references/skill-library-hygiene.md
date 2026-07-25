# Skill Library Hygiene

## Why this exists

This reference captures reusable maintenance rules for the skill library after real sessions.

## Trigger signals

Treat any of these as a cue to update a skill or support file:

- The user asks to review the conversation and update the skill library.
- A loaded skill proved incomplete, stale, or too narrow.
- The session exposed a reusable fix, workaround, or workflow.
- The session surfaced a user preference that changes how a class of task should be handled.
- Two skills overlap enough that future maintenance would benefit from clearer separation.

## Preferred action order

1. Patch the currently loaded skill that governed the work.
2. If no loaded skill fits, patch the existing umbrella skill for the class.
3. If the lesson is durable but narrow, add a file under `references/`, `templates/`, or `scripts/`.
4. Create a new skill only when no class-level umbrella exists.

## What to capture

- Short pitfall statements.
- Concrete steps or verification checks.
- Tool-usage patterns that will recur.
- User preferences that affect the whole class of task.
- Path-specific or provider-specific notes that are stable enough to matter again.

## What not to capture

- Task progress logs.
- One-off artifact names.
- Environment-dependent failures that are likely to disappear after setup changes.
- Secrets, tokens, or credentials.
- Overly specific session narration that will not generalize.

## Good update shape

- Keep `SKILL.md` focused on triggers, workflow, and verification.
- Put session-specific detail in `references/`.
- Put reusable starter content in `templates/`.
- Put deterministic commands or generators in `scripts/`.
- Prefer one durable improvement over several tiny narrow skills.

## Batch Operations: Move Before Remove

When reorganizing large numbers of files (e.g., 100+ skills into categories):
1. **Remove duplicates first** — `rm -rf` root-level copies that have category duplicates
2. **Then batch move** — use `execute_code` with `shutil.move()` instead of shell `mv` chains
3. **Verify after** — count remaining root-level entries, should be 0 (or only real categories)

Shell `mv` in a chain fails entirely if one destination exists. Python `shutil.move()` can skip existing destinations gracefully.

## Audit False Positives: Code Blocks vs Executable

When auditing skills for supply-chain risks (e.g., `pip install` patterns):
- **Strip code blocks first** — remove all ` ```...``` `` and `` `...` `` content before pattern matching
- **Then check** — only flag patterns that appear in prose (not documentation examples)
- Most `pip install` in SKILL.md files are user instructions, not executable code

## Quality check

Before stopping, ask:

- Did this session leave the library clearer than it was?
- Is the improvement reusable by the next session?
- Did I avoid creating a one-off skill when a reference file was enough?
- Did I preserve class-level structure instead of fragmenting the library?
