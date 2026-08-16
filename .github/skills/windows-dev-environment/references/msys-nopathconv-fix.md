# MSYS_NO_PATHCONV for running Python scripts from git-bash

When running native Windows Python (not MSYS2 Python) from git-bash, MSYS2's path translation converts POSIX paths (`/c/Users/...`) into Windows paths with a broken prefix (`C:\c\Users\...`).

## The fix

Always prefix native-Python calls with `MSYS_NO_PATHCONV=1` when running from git-bash/MSYS2:

```bash
# BROKEN (MSYS translates /c/ → C:\c\)
python /c/Users/Alexa/AppData/Local/hermes/scripts/batch_skill_judge.py

# WORKS
MSYS_NO_PATHCONV=1 python "C:/Users/Alexa/AppData/Local/hermes/scripts/batch_skill_judge.py"
```

This disables MSYS2's automatic path conversion for that command only.

## Affected tools

- `batch_skill_judge.py` — must use `MSYS_NO_PATHCONV=1` when invoked from bash
- Any native Windows Python script invoked from git-bash terminal with absolute paths

## Also documented in

- `windows-msys2-path-portability` skill (legacy reference)
