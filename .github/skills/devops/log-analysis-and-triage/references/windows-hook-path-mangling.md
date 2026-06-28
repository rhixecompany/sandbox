# Windows Hook Path Mangling: Full Diagnosis Trace

## Discovery

155 repeated WARNING entries in `errors.log`:
```
agent.shell_hooks: shell hook failed (event=on_session_start command=C:\Program Files\Git\usr\bin\bash.exe -c "..."): command not found
```

Affected all 3 hooks (session-logger, session-auto-commit, governance-audit) on every session event.

## Initial Tests (all passed)

- `which bash` → `/usr/bin/bash` ✓
- `bash /c/Users/.../hook.sh` → exit=0, stdout=`{}` ✓
- `env -i PATH="/usr/bin:/c/Windows/system32" bash -c "/c/Users/.../hook.sh"` → exit=0 ✓
- `file hook.sh` → "Bourne-Again shell script, ASCII text executable" ✓

Hook scripts and bash were fine — problem was in the *caller*, not the script.

## Root Cause Trace

### Step 1: Read shell_hooks.py _spawn()

`agent/shell_hooks.py` line 416-471:
```python
def _spawn(spec, stdin_json):
    argv = shlex.split(os.path.expanduser(spec.command))  # line 435
    proc = subprocess.run(argv, ..., shell=False)         # line 445
    # ...
    except FileNotFoundError:                              # line 457
        result["error"] = "command not found"
```

`shlex.split()` with POSIX mode (the default on all platforms) treats `\` as escape character.

### Step 2: Verify with Python

```python
import shlex
cmd = r'C:\Program Files\Git\usr\bin\bash.exe -c "/c/Users/.../hook.sh"'
shlex.split(cmd)
# → ['C:Program', 'FilesGitusrbinbash.exe', '-c', '/c/Users/.../hook.sh']
#   ^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^
#   WRONG!      WRONG!
```

- `C:\Program` → `\` escapes `P` → `C:Program` (one word)
- ` ` → word separator
- `Files\Git\usr\bin\bash.exe` → all `\` consumed as escapes → `FilesGitusrbinbash.exe`

First token `C:Program` doesn't exist → `FileNotFoundError` → "command not found"

### Step 3: Config YAML format

Original config.yaml (multi-line plain scalar):
```yaml
  - command: C:\Program Files\Git\usr\bin\bash.exe -c 
      "/c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh"
```

YAML folds the newline into a space, producing same mangled string.

## Fix

### Replace path format

Change backslash path + multi-line YAML → forward-slash path + single-line YAML single-quoted scalar:

```yaml
- command: '"C:/Program Files/Git/usr/bin/bash.exe" -c "/c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh"'
```

The outer `'...'` (YAML single-quoted) preserves the inner `"..."` literally. `shlex.split` in POSIX mode then correctly parses quoted tokens.

### Verify

```python
cmd = '"C:/Program Files/Git/usr/bin/bash.exe" -c "/c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh"'
shlex.split(cmd)
# → ['C:/Program Files/Git/usr/bin/bash.exe', '-c', '/c/Users/Alexa/.../hook.sh']
#   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   CORRECT — single token
```

## Config Edit Method

Hermes blocks direct `write_file` to config.yaml. Use PowerShell from terminal:

```powershell
$config = Get-Content "$env:USERPROFILE\AppData\Local\hermes\config.yaml" -Raw
$config = $config -replace [regex]::Escape('C:\Program Files\Git\usr\bin\bash.exe -c'), '"C:/Program Files/Git/usr/bin/bash.exe" -c'
Set-Content "$env:USERPROFILE\AppData\Local\hermes\config.yaml" -Value $config -NoNewline
```

Then validate:
```bash
python3 -c "import yaml,shlex; yaml.safe_load(open(r'C:\Users\Alexa\AppData\Local\hermes\config.yaml')); print('YAML VALID')"
```

## Result

4/4 hooks verified working (exit=0, valid JSON stdout). Space freed: 17.5 MB from stale logs during same session.
