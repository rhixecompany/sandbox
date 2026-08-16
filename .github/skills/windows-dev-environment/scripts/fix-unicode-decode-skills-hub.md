# Fix for UnicodeDecodeError in skills_hub.py

## Files to Patch

**File:** `C:\Users\Alexa\AppData\Local\hermes\hermes-agent\tools\skills_hub.py`

### Patch 1: `_read_index_cache()` function (around line 3362)

**Current:**
```python
try:
    stat = cache_file.stat()
    if time.time() - stat.st_mtime > INDEX_CACHE_TTL:
        return None
    return json.loads(cache_file.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError):
    return None
```

**Fixed:**
```python
try:
    stat = cache_file.stat()
    if time.time() - stat.st_mtime > INDEX_CACHE_TTL:
        return None
    return json.loads(cache_file.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError, UnicodeDecodeError):
    return None
```

### Patch 2: `HubLockFile.load()` method (around line 3416)

**Current:**
```python
try:
    return json.loads(self.path.read_text(encoding="utf-8"))
except (json.JSONDecodeError, OSError):
    return {"version": 1, "installed": {}}
```

**Fixed:**
```python
try:
    return json.loads(self.path.read_text(encoding="utf-8"))
except (json.JSONDecodeError, OSError, UnicodeDecodeError):
    return {"version": 1, "installed": {}}
```

## Verification Commands

```bash
# Verify the fix is applied
grep -n "UnicodeDecodeError" "C:/Users/Alexa/AppData/Local/hermes/hermes-agent/tools/skills_hub.py"

# Test: corrupt lock.json with invalid UTF-8
cd "C:/Users/Alexa/AppData/Local/hermes"
echo -e '{"version": 1, "installed": {}}' | iconv -f utf-8 -t cp1252 > skills/.hub/lock.json
hermes skills audit  # Should NOT crash with UnicodeDecodeError
```