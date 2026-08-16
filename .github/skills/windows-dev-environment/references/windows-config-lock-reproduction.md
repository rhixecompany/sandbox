# Hermes Config Pitfalls on Windows

## 1. Config File Lock

### Observed Behavior

When running `hermes plugins enable <name>` commands sequentially from a running Hermes TUI session on Windows, the first command succeeds but subsequent commands fail with:

```
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process
```

The Hermes TUI process holds an open handle to `config.yaml`, and the atomic file replacement (`os.replace()`) used by `hermes plugins enable` races with the running session's own config reads.

### Reproduction

```bash
# In a running Hermes TUI session:
hermes plugins enable plugin-a    # Succeeds (takes effect next session)
hermes plugins enable plugin-b    # FAILS — PermissionError on os.replace()
hermes plugins enable plugin-c    # FAILS — same error
```

### Workaround: Retry with Exponential Backoff

```python
import time

plugins = ["plugin-a", "plugin-b", "plugin-c"]
for p in plugins:
    for attempt in range(3):
        r = terminal(f"hermes plugins enable {p}", timeout=30)
        if r["exit_code"] == 0:
            break
        time.sleep(1.5 ** attempt)  # 1s, 1.5s, 2.25s
```

The delay lets the TUI session release its file handle between writes.

### Workaround: Batch via Direct Config Edit

For bulk changes, patch `config.yaml` directly with `write_file` or `patch` tools instead of sequential `hermes plugins enable` calls.

### Root Cause

- Hermes TUI reads `config.yaml` at startup and periodically (hooks, state tracking)
- `hermes plugins enable` writes to `config.yaml` via `os.replace(new_file, config_path)` — atomic but requires exclusive access
- On Windows, `os.replace()` fails immediately if another handle has the file open (unlike Linux which allows deletion of open files)
- The TUI session doesn't release its handle predictably between sequential CLI calls

### Verified Fix

Tested with 15+ plugins in one session: retry script with 1.5× backoff succeeded for all where a naive loop failed on the second plugin. Total completion time: ~60s for 15 plugins.

---

## 2. `hermes config set` Mangles YAML Lists

### Observed Behavior

`hermes config set plugins.enabled plugin-name` converts the YAML field into a JSON string instead of a YAML list:

```yaml
# Before:
plugins:
  enabled:
    - plugin-a
    - plugin-b

# After hermes config set plugins.enabled plugin-name:
plugins:
  enabled: '-'
```

### Why

The `hermes config set` CLI serializes the value argument as a scalar string, not as a YAML sequence. When the value was originally a list, it's written as a string representation of the first element.

### Fix

```bash
# Remove the corrupted key
hermes config unset plugins.enabled

# Then use plugins enable/disable to rebuild the list properly
hermes plugins enable plugin-a
hermes plugins enable plugin-b
```

### Prevention

Do NOT use `hermes config set <list_field> <value>` for YAML list fields (`plugins.enabled`, `plugins.disabled`, `fallback_providers`, `mcp_servers.<name>.args`, etc.). Use instead:
- `hermes plugins enable/disable` for plugin lists
- `hermes config edit` (opens $EDITOR) for manual changes
- `hermes config unset <key>` then re-add via proper CLI commands
- Direct `write_file` / `patch` on `config.yaml` for bulk batch operations
