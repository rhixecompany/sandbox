# Python Scripts Permanent File Workflow

**Purpose:** Document Strict Rule #4 — NEVER run inline Python; create permanent scripts in `C:/Users/Alexa/AppData/Local/hermes/scripts/`, debug/fix/rerun until zero issues.

---

## Rule Definition (from SOUL.md)

> **Rule 4: Python Scripts Rule**
> NEVER run inline Python scripts via `execute_code` or terminal one-liners.
> Instead:
> 1. Create the script as a permanent file in `C:/Users/Alexa/AppData/Local/hermes/scripts/`
> 2. Execute it from there
> 3. If it fails, debug, fix, and rerun until zero issues
> 4. Keep the script for reuse — no throwaway inline code

---

## Workflow

### Step 1: Create Script File

```bash
# Directory exists: C:/Users/Alexa/AppData/Local/hermes/scripts/
# Naming: <purpose>-<date>.py or <purpose>.py
cat > /c/Users/Alexa/AppData/Local/hermes/scripts/sync-profiles.py << 'EOF'
#!/usr/bin/env python3
"""Sync Hermes profiles - deduplicate configs, standardize SOUL.md"""
import os
import shutil
from pathlib import Path

def main():
    # ... implementation
    pass

if __name__ == "__main__":
    main()
EOF
chmod +x /c/Users/Alexa/AppData/Local/hermes/scripts/sync-profiles.py
```

### Step 2: Execute from Script Location

```bash
# Preferred: run from scripts directory
cd /c/Users/Alexa/AppData/Local/hermes/scripts/
python3 sync-profiles.py

# Or with full path
python3 /c/Users/Alexa/AppData/Local/hermes/scripts/sync-profiles.py
```

### Step 3: Debug → Fix → Rerun Loop

```bash
# 1. Run
python3 script.py

# 2. If error: read traceback, identify root cause
# 3. Edit script: fix the issue
# 4. Rerun: python3 script.py
# 5. Repeat until exit code 0 and expected output
```

### Step 4: Keep for Reuse

- Scripts persist in `scripts/` directory
- Can be called from cron jobs, hooks, other scripts
- Version controlled if needed (git add scripts/)

---

## Why Permanent Scripts Over Inline

| Inline (`execute_code` / one-liner) | Permanent Script (`scripts/`) |
|-------------------------------------|-------------------------------|
| Lost after session | Persists across sessions |
| Hard to debug (no file to edit) | Edit in place, rerun |
| Can't share with cron/hooks | Cron jobs can call directly |
| No version history | Git trackable |
| Token overhead (re-send code) | Send path only |
| Context pollution | Clean separation |

---

## Script Templates

### Basic Template
```python
#!/usr/bin/env python3
"""<Description>"""
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
HERMES_ROOT = SCRIPTS_DIR.parent

def main():
    try:
        # ... logic
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### Hermes-Aware Template (uses HERMES paths)
```python
#!/usr/bin/env python3
"""<Description> - Uses HERMES paths from environment"""
import os
import sys
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes"))
SCRIPTS_DIR = HERMES_HOME / "scripts"
PROFILES_DIR = HERMES_HOME / "profiles"
WORKSPACE = Path("C:/Users/Alexa/Desktop/SandBox")

def main():
    # ... logic using HERMES paths
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

## Verification Checklist

When auditing SOUL.md for Python rule compliance:

- [ ] Rule text identical across all 7 profiles
- [ ] `scripts/` directory exists and is writable
- [ ] No inline Python examples in SOUL.md that contradict rule
- [ ] `.hermes.md` and `AGENTS.md` reference the rule
- [ ] Example scripts in `scripts/` follow template

---

## Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| `python3 -c "import x; x.do()"` | Create `scripts/do-x.py` |
| `execute_code` with Python logic | Write `scripts/task.py`, call via `terminal` |
| One-off script in `/tmp` | Use `scripts/` with descriptive name |
| Deleting script after use | Keep in `scripts/` for reuse |

---

## Integration with Profile Maintenance

When running `profile-maintenance`:
1. Verify Python rule present in all 7 SOUL.md files
2. Verify `scripts/` directory exists: `ls /c/Users/Alexa/AppData/Local/hermes/scripts/`
3. Check for orphaned inline patterns in other docs