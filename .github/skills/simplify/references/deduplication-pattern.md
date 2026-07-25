# Deduplication Pattern — SandBox vs Hermes Root

## Problem
SandBox `.github/skills/`, `.github/hooks/`, `.github/plugins/` accumulate copies of items that also live in `~/AppData/Local/hermes/`. The hermes root is canonical; SandBox copies are redundant.

## Detection Logic (Python via execute_code)

```python
import os

def find_duplicates(sb_dir, hermes_dir):
    sb_items = set(os.listdir(sb_dir))
    hermes_items = set(d for d in os.listdir(hermes_dir) if not d.startswith('.'))
    duplicates = sorted(sb_items & hermes_items)
    sb_only = sorted(sb_items - hermes_items)
    hermes_only = sorted(hermes_items - sb_items)
    return duplicates, sb_only, hermes_only
```

## Deletion Pattern

```python
import shutil
for item in duplicates:
    path = os.path.join(sb_dir, item)
    if os.path.isdir(path):
        shutil.rmtree(path)  # May fail on Windows-locked git dirs
    else:
        os.remove(path)
```

## Windows Git Dir Workaround

When `shutil.rmtree` fails on plugin dirs containing `.git/`:

```bash
cd <parent_dir>
chmod -R +w <locked_dir>
rm -rf <locked_dir>
```

## Verification

```bash
# Source should only have unique items
ls <sb_dir>
# Canonical should be intact
ls <hermes_dir>
```

## Real Session Result (2026-06-29)
- 122 duplicate skills deleted from `.github/skills/`
- 7 duplicate hooks deleted from `.github/hooks/` (dir removed)
- 4 duplicate plugins deleted from `.github/plugins/` (dir emptied)
- 18 SandBox-only skills preserved
- All 123 hermes root skills, 7 hooks, 4 plugins intact
