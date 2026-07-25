# Windows Environment Variables — Quick Reference

Where app/user data lives, and which var to use per language. Verified on this host
(Git Bash/MSYS, python 3.11/3.13, node, sh).

| Var | Typical value | Points to | Use for |
|-----|---------------|-----------|---------|
| `LOCALAPPDATA` | `C:\Users\<u>\AppData\Local` | per-user **local** app data (Hermes install dir) | Hermes `hermes/` tree, caches |
| `APPDATA` | `C:\Users\<u>\AppData\Roaming` | per-user **roaming** app data | config that should roam |
| `USERPROFILE` | `C:\Users\<u>` | user home | user dir, not app-data |
| `HOME` | `/c/Users/<u>` (MSYS) / `/home/<u>` (sh) | POSIX home | POSIX-style paths, `~` |
| `USERNAME` | `<u>` | login name | user id |

## Availability per shell (this host)
- **Git Bash / MSYS / sh**: `LOCALAPPDATA`, `APPDATA`, `USERPROFILE`, `HOME`, `USERNAME` all set.
- **python** (`os.environ`): all of the above set.
- **node** (`process.env`): all of the above set.
- **PowerShell**: same vars, accessed as `$env:LOCALAPPDATA` etc.

## Resolution recipes
- Python: `os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"`
- Node: `process.env.LOCALAPPDATA || process.env.USERPROFILE || 'C:\\Users\\Alexa'`
- Bash: `${LOCALAPPDATA:-$HOME/AppData/Local}/hermes`
- PowerShell: `$env:LOCALAPPDATA\hermes`

## Gotchas
- `$env:VAR` is **PowerShell-only**. In `.py`/`.js`/`.sh` use the native forms above.
- Backslash `\` is an escape char in bash double-quoted strings and python — prefer
  `os.path.join()` over manual string concat for subpaths.
- `HOME` on MSYS is `/c/Users/<u>` (forward slashes); mixing with backslash Windows paths
  causes `No such file` errors in native python `open()`.
