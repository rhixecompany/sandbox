# Cross-Platform Wrapper Standardization

Reference captured from Batches 4a–4b execution (Comicwise wrapper normalization), covering matched `.sh` and `.ps1` wrappers targeting the same canonical runner.

## Pattern: Matched Wrapper Pairs

When a wrapper family (e.g., `dev`, `setup-dev`, `quality-gate`) needs both bash and PowerShell variants, create matching pairs that follow a unified contract:

```
dev.sh           ← Bash wrapper → pnpm dev
dev.ps1          ← PowerShell wrapper → pnpm dev
setup-dev.sh     ← Bash wrapper → pnpm setup
setup-dev.ps1    ← PowerShell wrapper → pnpm setup
```

All variants must:
1. Accept the same arguments from caller
2. Forward arguments unchanged to the canonical runner
3. Propagate exit code back to caller
4. Keep no business logic (orchestration only)
5. Provide help in a consistent style

## Help Flag Convention

**Bash**: Use `--help` or `-h`
- Trigger: `[[ "$*" == *"--help"* ]] || [[ "$*" == *"-h"* ]]`
- Output with `echo` or `cat`
- Exit with code 0

**PowerShell**: Use `-Help` switch parameter
- Trigger: `param( [switch]$Help )`
- Output with `Write-Host`
- Exit with code 0

## Exit Code Propagation

**Bash**:
```bash
exec pnpm dev "$@"
# or
pnpm dev "$@"
exit $?
```

**PowerShell**:
```powershell
& pnpm dev @args_list @args
exit $LASTEXITCODE
```

## Argument Forwarding

**Bash**: All args passed as-is
```bash
exec pnpm quality:gate:sh "$@"
```

**PowerShell**: Build args array and pass
```powershell
$args_list = @()
if ($SkipLint) { $args_list += "--skip-lint" }
if ($SkipBuild) { $args_list += "--skip-build" }
if ($Json) { $args_list += "--json" }
& pnpm quality:gate:sh @args_list @args
```

## Size Targets

For wrapper families delegating to pnpm commands:
- **Thin delegators**: 40–60 lines per variant is normal
- **Quality gate family** (5 commands chained): 44–62 lines per variant
- **Cleanup family** (1 command): 39–47 lines per variant
- **VSCode extensions** (VSCode CLI orchestration): 180–201 lines per variant (business logic specific to `code` CLI, not duplicated elsewhere)

Expect **13–78% reduction** from original business-logic wrappers.

## Verification Pattern

For each wrapper pair:

1. **Syntax validation**:
   - Bash: `bash -n wrapper.sh`
   - PowerShell: `powershell -NoProfile -Command "[System.Management.Automation.Language.Parser]::ParseInput((Get-Content wrapper.ps1), [ref]$null, [ref]$null)"`

2. **Help verification**:
   - `bash wrapper.sh --help 2>&1 | head -10`
   - `powershell -NoProfile ".\wrapper.ps1 -Help" 2>&1 | head -10`

3. **Exit code propagation**:
   - Success: wrapper.sh + success runner → wrapper exit 0
   - Failure: wrapper.sh + failing runner → wrapper exit 1+
   - Same for .ps1

4. **Argument forwarding**:
   - `bash wrapper.sh --flag1 --flag2 value` should forward both flags to canonical runner
   - `powershell ".\wrapper.ps1 -Flag1 -Flag2 value"` should forward both to runner

## Example: quality-gate.sh & quality-gate.ps1

**quality-gate.sh** (44 lines):
```bash
#!/bin/bash
set -e

if [[ "$*" == *"--help"* ]]; then
  echo "ComicWise Quality Gate Runner"
  echo ""
  echo "Usage:"
  echo "  ./quality-gate.sh [options]"
  echo ""
  exit 0
fi

exec pnpm quality:gate:sh "$@"
```

**quality-gate.ps1** (62 lines):
```powershell
param(
  [switch]$SkipLint,
  [switch]$SkipBuild,
  [switch]$SkipTypeCheck,
  [switch]$SkipTests,
  [switch]$SkipTriage,
  [switch]$ContinueOnError,
  [switch]$Json,
  [switch]$Help
)

if ($Help) {
  Write-Host "ComicWise Quality Gate Runner"
  Write-Host ""
  Write-Host "Usage:"
  Write-Host "  .\quality-gate.ps1 [options]"
  Write-Host ""
  exit 0
}

$args_list = @()
if ($SkipLint) { $args_list += "--skip-lint" }
if ($SkipBuild) { $args_list += "--skip-build" }
if ($SkipTypeCheck) { $args_list += "--skip-type-check" }
if ($SkipTests) { $args_list += "--skip-tests" }
if ($SkipTriage) { $args_list += "--skip-triage" }
if ($ContinueOnError) { $args_list += "--continue-on-error" }
if ($Json) { $args_list += "--json" }

& pnpm quality:gate:sh @args_list @args
exit $LASTEXITCODE
```

Both are thin delegators with help, argument forwarding, and exit-code propagation.

## When NOT to Use This Pattern

- **VSCode extension management**: Keep business logic in shell wrapper when it's specific to `code` CLI tool (idempotent checks, parallel install/uninstall, verification loops). Create PowerShell equivalent for parity, but don't try to consolidate to TypeScript (too tightly coupled to VSCode API).
- **Complex prerequisite checking**: If wrapper needs extensive environment validation (e.g., check Node version, detect OS quirks), consider moving that to a TypeScript runner. But if it's a quick inline check, thin wrapper is fine.

## Batch Sizing for Wrapper Families

When you have 10 wrappers across 5 families (e.g., dev, setup-dev, quality-gate, cleanup, install-extensions) with 2 platform variants each, split by **purpose**, not platform:

- **Batch 4a**: dev.sh, dev.ps1, setup-dev.sh, setup-dev.ps1 (4 files, both families)
- **Batch 4b**: quality-gate.sh, quality-gate.ps1, cleanup.sh, cleanup.ps1, install-vscode-extensions.sh, install-vscode-extensions.ps1 (6 files, three families)

This keeps related functionality together during verification and makes checkpoint testing easier.
