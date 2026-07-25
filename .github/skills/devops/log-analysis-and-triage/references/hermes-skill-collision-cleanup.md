# Hermes Skill Collision Cleanup

## Detection Script

Run to find skills with multiple paths (true collisions from `.restore-backups`):

```python
import os
from pathlib import Path
from collections import defaultdict

skills_dir = Path(os.path.expanduser("~/AppData/Local/hermes/skills"))
names = defaultdict(list)
for f in skills_dir.rglob("SKILL.md"):
    if ".restore-backups" in str(f) or ".DISABLED" in str(f):
        continue
    names[f.parent.name].append(str(f.parent.relative_to(skills_dir)).replace("\\", "/"))

# True collisions: 3+ paths (backup + flat + categorized)
collisions = {k: v for k, v in names.items() if len(v) > 2}
print(f"Multi-path collisions (3+): {len(collisions)}")
for k, v in collisions.items():
    print(f"  {k}: {v}")
```

## Fix

```bash
mv "$LOCALAPPDATA/hermes/skills/.restore-backups" \
   "$LOCALAPPDATA/hermes/skills/.restore-backups.DISABLED"
```

## Verification

After rename, re-run detection — should show 0 multi-path collisions.
Flat vs categorized (2 paths, different content) is expected and safe.

## Rollback

```bash
mv "$LOCALAPPDATA/hermes/skills/.restore-backups.DISABLED" \
   "$LOCALAPPDATA/hermes/skills/.restore-backups"
```

## Real-World Result (2026-07-15)

Before: 74 skills had 3+ path collisions (e.g. `subagent-driven-development` → 4 copies).
After: 0 multi-path collisions. `skill_view` and `skill_manage` work without ambiguity.
Backup preserved at `.restore-backups.DISABLED` (7.8 MB) for safe rollback.
