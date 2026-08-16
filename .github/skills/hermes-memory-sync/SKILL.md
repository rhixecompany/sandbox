---
name: hermes-memory-sync
title: "Profile Memory Sync — Root → Profiles"
description: "Use after compacting or updating root USER.md or MEMORY.md — sync the same content to all Hermes profile copies so validation passes everywhere."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, profiles, memory, maintenance]
---
# Hermes Memory Sync

Sync USER.md and MEMORY.md from the root Hermes memories directory to all profile copies after root compaction or content updates.

**Trigger:** After intentionally rewriting root USER.md or MEMORY.md under `~/AppData/Local/hermes/memories/`.

**Do NOT use for:** SOUL.md (each profile keeps unique personality), transient task progress, one-off session facts.

## Overview

Automated reasoning and workflow tool for `hermes-memory-sync`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Root USER.md was compacted below the size limit and profiles still have the old oversized version
- Root MEMORY.md was rewritten (compacted, cleaned, or threat-resolved) and profile copies need the new version
- `validate-memories` script reports profile USER.md or MEMORY.md over size limits
- User explicitly requested profile synchronization after root fixes

## Workflow

### 1. List Profiles

Check which profiles exist and need syncing:

```bash
ls "C:/Users/Alexa/AppData/Local/hermes/profiles/"
```

Standard profiles: `alexa`, `code-architect`, `creative-director`, `exec-assistant`, `patient-tutor`, `research-analyst`.

### 2. Sync USER.md

For each profile, write the same compact USER.md content:

```bash
# Profiles and target paths
PROFILES="alexa code-architect creative-director exec-assistant patient-tutor research-analyst"
BASE="C:/Users/Alexa/AppData/Local/hermes/profiles"
```

Use `write_file(path=..., content=<same as root>, cross_profile=True)` for each profile.

**Content:** The root compact USER.md (the canonical default profile USER.md). Keep profile title unique per file (`# USER.md — <name> profile`) but all preferences, model, OS, and environment details should match root.

### 3. Sync MEMORY.md

Same pattern — write the compacted root MEMORY.md to each profile's `memories/MEMORY.md`:

```bash
write_file(
  path=f"{BASE}/{profile}/memories/MEMORY.md",
  content=<root MEMORY.md content>,
  cross_profile=True
)
```

### 4. Verify

Run the validation script to confirm all passes:

```bash
python3 "C:/Users/Alexa/AppData/Local/hermes/skills/devops/validate-memories/scripts/validate_memories.py"
```

Expected: 21/21 files passing (root + 6 profiles × 3 files = 21).

## Pitfalls

- **Cross-profile guard blocks writes.** The Hermes soft guard prevents writes under other profiles' paths. Always set `cross_profile=True` on `write_file` — without it, writes silently fail.
- **Do NOT sync SOUL.md.** Each profile's SOUL.md carries unique personality directives, operating model variations, and role-specific constraints. Only USER.md and MEMORY.md are shared root content.
- **Content not absolute byte-copy.** While the core content is identical, adjust the title line per profile (e.g. `# USER.md — code-architect profile`) so it's self-identifying.
- **Run after every root compaction.** If you compact USER.md or MEMORY.md but skip the profile sync, the next session may load stale profile copies and validation will flag them. Make it part of the cleanup routine.
- **Sizes matter.** Root USER.md must be <2000 chars, root MEMORY.md <6000 chars. Same limits apply to profile copies since they carry the same content.

## Related Skills

- `validate-memories` — Validation script that detects oversized/stale profile files (run this to know sync is needed)
- `profile-maintenance` — Broader profile identity management (references/profile-sync-procedure.md covers operational sync; this skill covers memory-only sync)

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Profile Memory Sync — Root → Profiles" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
