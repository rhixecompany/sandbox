# Python Script Path-Hardcoding Remediation

## Context

Python scripts written for a specific user's Windows machine often hardcode
absolute paths like `C:\Users\Alexa\...` or `C:/Users/Alexa/...`. These break
when:
- The username changes
- The machine changes
- The directory structure evolves
- Running under MSYS/Git Bash where `/c/Users/...` is the native form

## Detection

Search both Windows path forms — Python handles either, so both appear:

```bash
grep -rn 'C:\\Users\\Alexa\\' --include="*.py" path/
grep -rn 'C:/Users/Alexa' --include="*.py" path/
```

Also detect actual environment-variable usage (these are already remediated):

```bash
grep -rn 'os.environ.*HOME\|os.environ.*USERPROFILE' --include="*.py" path/
```

## Fix Pattern

### For `os.path` style (string-based paths)

Replace:

```python
SKILLS_DIR = r'C:\Users\Alexa\AppData\Local\hermes\skills'
```

With:

```python
_HOME = os.environ.get("HOME", os.environ.get("USERPROFILE", "C:\\Users\\Alexa"))
SKILLS_DIR = os.path.join(_HOME, "AppData", "Local", "hermes", "skills")
```

**Key detail:** The fallback `"C:\\Users\\Alexa"` uses double-backslash because it's
a regular (non-raw) string. Keep the fallback for environments where both
`HOME` and `USERPROFILE` are unset (though this is extremely rare on Windows).

### For `pathlib.Path` style (object-based paths)

Replace:

```python
SKILLS_BASE = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
```

With:

```python
_HOME = Path(os.environ.get("HOME", os.environ.get("USERPROFILE", "C:\\Users\\Alexa")))
SKILLS_BASE = _HOME / "AppData" / "Local" / "hermes" / "skills"
```

The `pathlib.Path` style uses `/` operator, which handles path joining
cross-platform regardless of OS path separator.

### For inline Windows-style paths in string literals

Replace:

```python
with open(r'C:\Users\Alexa\Desktop\SandBox\judge_results\remaining.txt') as f:
```

With:

```python
with open(os.path.join(_HOME, "Desktop", "SandBox", "judge_results", "remaining.txt")) as f:
```

### Environment variable resolution (MSYS vs Windows)

| Context | `$HOME` value | `$USERPROFILE` value | Python `os.environ.get("HOME")` |
|---------|---------------|----------------------|---------------------------------|
| MSYS/Git Bash | `/c/Users/Alexa` | `C:\Users\Alexa` | `C:\Users\Alexa` (translated) |
| Windows cmd | (unset or not Windows) | `C:\Users\Alexa` | `C:\Users\Alexa` |
| Python (any) | — | — | `C:\Users\Alexa` |

Both `HOME` and `USERPROFILE` work because Python on Windows accepts both
`/c/Users/...` and `C:\Users\...` style paths in all file APIs. The fallback
chain `HOME → USERPROFILE → hardcoded` ensures maximum portability.

## Verification

### Syntax check (all modified files)

```python
import os
errors = []
for s in modified_scripts:
    path = os.path.join(scripts_dir, s)
    try:
        compile(open(path, 'rb').read(), path, 'exec')
    except SyntaxError as e:
        errors.append((s, e))
```

### Runtime path resolution check

```python
_HOME = os.environ.get("HOME", os.environ.get("USERPROFILE"))
# Verify key paths exist
for p in [skills, sandbox, profiles]:
    print(f"{'EXISTS' if os.path.exists(p) else 'MISSING'} {p}")
```

### Final residual scan

```bash
# After all fixes:
grep -rn 'C:\\Users\\Alexa\|C:/Users/Alexa' scripts/ --include="*.py" | grep -v '__pycache__'
# Should return zero matches
```

## Pitfalls

### 🚩 `\U` escape in heredoc Python

When writing inline Python via `python3 << 'ENDPY'`, the literal `\U` in
`C:\Users\...` triggers a Unicode escape error:

```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
```

**Fix:** Use single-quoted heredoc delimiter (`<< 'ENDPY'` not `<< ENDPY`)
to prevent shell expansion, AND avoid `\U` followed by hex digits in the
Python code itself. Use `os.path.join` instead of raw strings with `C:\Users`.

### 🚩 `os.path.join` creates `\` on Windows (and that's OK)

Python on Windows uses `\` as the path separator in `os.path.join` results.
This is correct for Windows file APIs, even when running under MSYS.
For shell subprocess calls, convert with `.replace("\\", "/")` or use
`pathlib.PurePosixPath` if the target expects POSIX paths.

### 🚩 pathlib's `/` operator

`Path("C:\\Users") / "Alexa"` produces `C:\Users\Alexa` on Windows.
This is fine — `pathlib` normalizes to the platform-native separator.
Do NOT replace backslashes after pathlib joins; it handles interop.
