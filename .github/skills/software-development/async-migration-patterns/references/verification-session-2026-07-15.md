# Async Conversion Verification — 2026-07-15

## Scope
- **82 Python scripts** in `~/AppData/Local/hermes/scripts/` — sync to async
- **3 hook packages** + `lib.py` in `~/AppData/Local/hermes/hooks/` — sync to async
- **17 non-Python files** (`.sh`, `.cjs`, `.js`, `.ps1`, `.json`) — skipped

## Batch Dispatch
5 parallel subagents via `delegate_task`:
- Task 1: 18 scripts ✅ (completed)
- Task 2: 18 scripts ⚠ (timed out at 20m — verified independently)
- Task 3: 17 scripts ✅ (completed)
- Task 4: 16 scripts ✅ (completed)
- Task 5: 13 scripts created from scratch ✅ (previously placeholder-only)

## Verification Results
| Check | Result |
|-------|--------|
| AST syntax pass | 82/82 ✅ |
| Has async pattern (asyncio.run or async def) | 82/82 ✅ |
| Hook.sh wrappers reference hook.py | 3/3 ✅ |
| Hooks have async def + asyncio.run | 4/4 ✅ |
| Missing `import os` despite os usage | 0 (4 false positives — comma-imports) |
| Bare `subprocess.run` without async wrapper | 0 |

## Bug Found and Fixed
**File:** `fix-frontmatter.py`
**Symptoms:** Runtime `NameError` when run with `--help`
**Root cause:** Two issues in subagent-created code:
1. `SANDBOX = Path(os.environ.get("HOME")) / "Desktop" / "SandBox"` — `import os` was missing (using `os.environ` without importing `os`)
2. The variable `SANDBOX` was never defined in the first place (referenced an assumed global that existed in other scripts but not this one)

**Fix:** Added `import os` + defined `SANDBOX = Path(...)` at module level before `async def main()`.

**Lesson:** Subagents assume globals used by sibling scripts are available. Always smoke-test a representative sample — especially scripts that use workspace-specific paths or environment variables.

## Skills Audit
- 159 skills reference these scripts by name
- Async conversion is transparent at CLI level — no skill files needed updating
- Commands use `python3 $LOCALAPPDATA/hermes/scripts/<name>.py` which works identically for sync and async
