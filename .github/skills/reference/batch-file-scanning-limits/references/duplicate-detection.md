# Duplicate Skill Detection Pattern

## Root-vs-Category Duplicates

Hermes skills frequently appear in **two locations** simultaneously:
- Root-level: `skills/<name>/SKILL.md` (standalone placement)
- Category-level: `skills/<category>/<name>/SKILL.md` (organized under a domain category)

Both copies get loaded, causing potential confusion and wasted disk space.

## Detection — Python (Single Terminal Call)

```python
import os, hashlib
from collections import defaultdict

root = os.path.expanduser("~/AppData/Local/hermes/skills")
names = defaultdict(list)

for dirpath, dirs, files in os.walk(root):
    if "SKILL.md" in files:
        name = os.path.basename(dirpath)
        names[name].append(os.path.join(dirpath, "SKILL.md"))

for name, paths in sorted(names.items()):
    if len(paths) < 2: continue
    root_level = [p for p in paths if p.count(os.sep) == 3 and "skills" in p]
    cat_level = [p for p in paths if p.count(os.sep) > 3]
    if not root_level or not cat_level: continue
    s1 = os.path.getsize(root_level[0])
    s2 = os.path.getsize(cat_level[0])
    if s1 == s2:
        print(f"IDENTICAL: {name} -> rm -rf {os.path.dirname(root_level[0])}")
    else:
        print(f"DIFFERENT: {name} root={s1}B cat={s2}B")
```

## Resolution

| Condition | Action |
|-----------|--------|
| Identical content | Remove root-level directory (category-level is canonical) |
| Different content | Review both; merge or pick the better version |
| Root-only (no category copy) | Leave as-is (may be intentionally uncategorized) |
| Category-only (no root copy) | Leave as-is (correct placement) |

## Pitfalls

- **Don't remove the last copy:** Some skills legitimately live only at root level.
- **Empty directories:** After removal, check for orphaned empty category directories.
- **Scoring calibration:** When judging skill quality, weight missing frontmatter (-40) heavier than short description (-10). A skill with 100/100 content but a 15-char description is not "broken".
