# PowerShell Strict Mode & Deprecation Guide

## Set-StrictMode -Version Latest

Every `.ps1` file should start with `Set-StrictMode -Version Latest` (analogous to `set -euo pipefail` in bash).

**Insertion points** (in priority order):
1. After `param(...)` block: identify by `^param(` on first lines
2. After `<#...#>` comment block
3. After `#` comment block lines
4. Before first code line (fallback)

**Exclusions**: Files named `skills-commit-batch-*.ps1` are git command lists with `.ps1` extension — not real PowerShell scripts. Skip them.

## PSIsContainer Deprecation

`$_.PSIsContainer` is deprecated in PowerShell 7.4+ and removed in some editions.

**Replace with**:
- `$_.PSIsContainer` → `Get-ChildItem -Directory` switch
- `-not $_.PSIsContainer` → `Get-ChildItem -File` switch

**Pattern**:
```powershell
# OLD — deprecated
$items = Get-ChildItem -Path $Path -Recurse
$files = $items | Where-Object { -not $_.PSIsContainer }
$dirs  = $items | Where-Object { $_.PSIsContainer }

# NEW — future-proof
$files = Get-ChildItem -Path $Path -Recurse -File
$dirs  = Get-ChildItem -Path $Path -Recurse -Directory
```
