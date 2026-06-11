# Wrapper Orchestration Contract

## Goal

Normalize cross-platform wrappers (`.sh`, `.ps1`, `.bat`) so they act as thin delegators that forward arguments and propagate exit codes consistently to a TypeScript or core runner.

## Core Pattern

All wrappers follow the same contract regardless of platform:

1. **Accept all arguments** from the caller
2. **Forward all arguments** to the TypeScript runner without modification
3. **Propagate exit code** of the runner back to the caller
4. **Handle help/no-args case** consistently (usually shows help from the TS runner)
5. **Keep no business logic** — orchestration only

## Platform-Specific Implementation

### Bash (`.sh`)

```bash
#!/usr/bin/env bash
# Thin wrapper: forward to TypeScript implementation

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)

cd "$REPO_ROOT"
bunx tsx scripts/ts/runner.ts "$@"
exit $?
```

**Key points:**
- `set -euo pipefail` for strict mode
- `"$@"` passes all arguments unchanged
- `exit $?` propagates the TS runner's exit code
- Change to repo root if runner uses relative paths
- No `if [ "$#" -eq 0 ]` branching — let the TS runner handle help

### PowerShell (`.ps1`)

```powershell
#!/usr/bin/env pwsh
# Thin wrapper: forward to TypeScript implementation

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$tsPath = Join-Path $scriptDir 'runner.ts'

try {
    & bunx tsx $tsPath @Arguments
    exit $LASTEXITCODE
} catch {
    Write-Error "Failed to invoke runner: $_"
    exit 1
}
```

**Key points:**
- `param([Parameter(ValueFromRemainingArguments = $true)] [string[]]$Arguments)` captures all args
- `Set-StrictMode -Version Latest` and `$ErrorActionPreference = 'Stop'` for error handling
- `@Arguments` splatting passes all args unchanged
- `exit $LASTEXITCODE` propagates the TS runner's exit code
- `try/catch` provides minimal error handling (optional but recommended)
- No custom help logic — let the TS runner handle it

### Batch/CMD (`.bat`)

```batch
@echo off
REM Thin wrapper: forward to TypeScript implementation
REM Usage: runner.bat [arguments]

setlocal enabledelayedexpansion
set "SCRIPT_DIR=%~dp0"
set "TS_PATH=%SCRIPT_DIR%runner.ts"

bunx tsx "%TS_PATH%" %*
exit /b %ERRORLEVEL%
```

**Key points:**
- `setlocal enabledelayedexpansion` for variable expansion
- `%~dp0` gets the script directory
- `%*` passes all arguments unchanged
- `exit /b %ERRORLEVEL%` propagates the TS runner's exit code
- No `:label` branching or conditional logic
- No `if "%*"==""` branching unless the TS runner does NOT support no-args help (rare)

## Detection: Thin Wrapper vs Business Logic

### Thin Wrapper (Correct)

- Shell script is ≤20 lines
- Only does: shebang, variable setup, `cd` to repo root, and forwards to TS runner
- No loops, conditionals, or variable manipulation beyond setup
- Passes all arguments via `"$@"` (bash), `@Arguments` (PS1), or `%*` (BAT)
- Exit code propagation is explicit: `exit $?`, `exit $LASTEXITCODE`, `exit /b %ERRORLEVEL%`

### Business Logic Hidden in Wrapper (Bug to Fix)

Red flags:
- Script is 50+ lines
- Contains loops, extensive conditionals, or test runners
- Runs external commands (e.g. `bun run type-check`, `bun run lint:strict`) that are not delegated to the TS runner
- Accepts special flags like `--dry-run`, `--help` and implements them locally instead of forwarding to TS runner
- Modifies arguments (e.g. adds flags, filters inputs) before passing to runner
- Uses `if [ "$#" -eq 0 ]` to show help instead of delegating help to TS runner

**Example bug**: `verify-agents.ps1` running `bun run type-check && bun run lint:strict && bun run test:browser -- --run` is test orchestration logic that belongs in the TS runner, not the wrapper.

**Fix**: Convert to thin wrapper that forwards all arguments to the TypeScript config validator (`scripts/ts/verify-agents.ts`), which owns the actual verification logic.

## Verification Checklist

After normalizing a wrapper family:

- [ ] All platform variants (`.sh`, `.ps1`, `.bat`) follow the same forwarding contract
- [ ] No business logic in wrappers — only orchestration
- [ ] All wrappers parse syntax correctly (AST parser for PS1, `bash -n` for SH, readable for BAT)
- [ ] Help output works: `wrapper --help`, `wrapper -h`, `wrapper` (no args)
- [ ] Argument forwarding works: `wrapper --flag value --another-flag` passes through unchanged
- [ ] Exit code parity: wrapper returns same exit code as TS runner
- [ ] No placeholder comments or stale references remain

## Batch Execution Checklist

When normalizing a wrapper family across multiple files:

1. **Read all current versions** to understand the existing contract (or lack thereof)
2. **Identify the canonical TypeScript runner** — it owns the real logic
3. **Create or update PowerShell wrapper** (`.ps1`) to the standard contract
4. **Create or update Batch wrapper** (`.bat`) to the standard contract
5. **Normalize Bash wrapper** (`.sh`) to match
6. **Run syntax validation**: AST parser for PS1, `bash -n` for SH, readable for BAT
7. **Test execution**: `wrapper --help`, `wrapper [arguments]`, verify exit codes
8. **Update progress log** with files changed, actions, and verification results
9. **Update verification report** matrix entry and checkpoint log

## Related Patterns

- **Thin wrapper pattern**: See `references/bat-thin-delegator-pattern.md` for `.bat` → `.ps1` delegation pattern
- **Strict mode**: See `references/powershell-strict-mode-and-deprecations.md` for PS1 best practices
- **Bash pitfalls**: See `references/bash-common-pitfall-fixes.md` for `set -u`, `eval`, subshell patterns
