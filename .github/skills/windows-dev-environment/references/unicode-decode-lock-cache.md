# UnicodeDecodeError on lock.json / Index Cache Files

## Symptom

```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 1108: invalid start byte
  File ".../tools/skills_hub.py", line 3416, in load
    return json.loads(self.path.read_text(encoding="utf-8"))
```

Or in `_read_index_cache`:
```
  File ".../tools/skills_hub.py", line 3362, in _read_index_cache
    return json.loads(cache_file.read_text(encoding="utf-8"))
```

## Root Cause

Both `HubLockFile.load()` (line ~3416) and `_read_index_cache()` (line ~3362) catch:
- `json.JSONDecodeError`
- `OSError`

But **not** `UnicodeDecodeError` — which is a `ValueError` subclass, not an `OSError`.

When a cache/lock file contains invalid UTF-8 (e.g., byte `0x97` = smart quote / right single quotation mark in Windows-1252), the `.read_text(encoding="utf-8")` call raises `UnicodeDecodeError` and crashes instead of falling back to empty state.

## Fix

Add `UnicodeDecodeError` to the except clause in both locations:

```python
# HubLockFile.load() — around line 3416
try:
    return json.loads(self.path.read_text(encoding="utf-8"))
except (json.JSONDecodeError, OSError, UnicodeDecodeError):
    return {"version": 1, "installed": {}}

# _read_index_cache() — around line 3362
try:
    stat = cache_file.stat()
    if time.time() - stat.st_mtime > INDEX_CACHE_TTL:
        return None
    return json.loads(cache_file.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError, UnicodeDecodeError):
    return None
```

## Reproduction

1. Corrupt `~/.hermes/skills/.hub/lock.json` or a file in `~/.hermes/skills/.hub/index-cache/` with invalid UTF-8:
   ```bash
   echo -e '{"version": 1, "installed": {}}' | iconv -f utf-8 -t cp1252 > lock.json
   # Or manually inject byte 0x97
   ```
2. Run `hermes skills audit` or any command that loads the lock file
3. Observe `UnicodeDecodeError` crash

## Prevention

- Always write JSON with `ensure_ascii=False` and explicit `encoding="utf-8"` (already done in `save()` methods)
- The fix is defensive: even if a file gets corrupted, the system degrades gracefully instead of crashing

## Related

- `references/hermes-config-validation-pitfalls.md` — other config validation issues
- `references/hermes-hook-config-pitfalls.md` — hook command format errors