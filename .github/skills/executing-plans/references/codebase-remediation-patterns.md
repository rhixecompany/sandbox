# Codebase Remediation — Standardization Patterns

> Reference document for `executing-plans` — captured from a 231-file cross-project script audit and remediation session.

## Shebang & Header Standards

### Shell Scripts (.sh)

- **Shebang**: `#!/usr/bin/env bash` (portable across Linux/macOS/Windows Git Bash — never `#!/bin/bash` or `#!/usr/bin/env sh`)
- **Shellcheck directive**: `# shellcheck shell=bash` immediately after shebang
- **Error handling**: `set -euo pipefail` (catches undefined vars, early exit on pipe failure, exit on error)
- **Ordering**: shebang → shellcheck → set directive

```
#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail
```

### PowerShell Scripts (.ps1)

- **Shebang**: `#!/usr/bin/env pwsh` (cross-platform PowerShell 7+)
- **Error action**: `$ErrorActionPreference = "Stop"` after shebang
- **Detection: Scripts without shebangs** are common — always check and add one

### Orphan Files

- **No shebang at all**: The script may still be called by an explicit interpreter. Add shebangs for editor/tool compatibility even if not strictly required.
- **`#/bin/bash` (missing `!`)**: Fix to `#!/usr/bin/env bash` — the missing `!` renders the shebang non-functional on most systems.

## Shell Linting & Quality Gates

- Every `.sh` file should have `# shellcheck shell=bash` for ShellCheck dialect detection
- Common ShellCheck warnings to suppress explicitly or fix:
  - **SC1091** (can't follow sourced file): add `# shellcheck source=/dev/null` if the sourced file is not available at analysis time
  - **SC3043** (local outside function): In POSIX sh mode `local` is undefined. Using `#!/usr/bin/env bash` fixes this
  - **SC2086** (unquoted variable): Always double-quote `"$var"` in conditionals and arguments

## TypeScript Patterns

### fs → fs.promises Migration

Replace callback-wrapped fs operations with direct promises:

**Before:**
```typescript
import fs from "fs";
// ...
new Promise<string>((resolve, reject) => {
    fs.readFile(path, "utf-8", (err, data) => {
        if (err) reject(err);
        else resolve(data);
    });
});
```

**After:**
```typescript
import { promises as fs } from "fs";
// ...
const data = await fs.readFile(path, "utf-8");
```

### Placeholder / Generated JSDoc

Watch for these stale auto-generated annotations and replace them with meaningful documentation:

- `@author Adminbot` — remove or replace with actual author
- `Description placeholder` — replace with a real description
- `CreatedBy: convert-scripts` — remove (reveals the file was auto-converted and is untrusted)
- `@type {*}` — narrow to the actual type (e.g., `string`, `number`, `string[]`)
- Empty JSDoc blocks — either fill or remove

Use `search_files` with regex to find remaining placeholders:
- `search_files("@author Adminbot", path="src/", file_glob="*.ts")`
- `search_files("Description placeholder", file_glob="*.ts")`
- `search_files("CreatedBy: convert-scripts", file_glob="*.ts")`

## Shell Script Architecture

- **Thin orchestrators**: Shell scripts should be thin wrappers that call TypeScript for business logic
- **Call pattern**: Use `bunx tsx <script.ts>` for TypeScript execution in npm/bun projects
- **Routing pattern**: When a script conditionally calls PowerShell or bash based on OS, the bash version should always exist as a fallback — never require `pwsh` to run on Linux
- **Script naming**: Keep names consistent across languages (`dev.sh` / `dev.ps1`, `quality-gate.sh` / `quality-gate.ps1`)

## Variable & Path Hygiene

- Use `${var}` with braces in interpolated contexts for clarity: `"${HOME}/project"`, `"${REPO_DIR}"`
- Use `$HOME` (POSIX) or `%USERPROFILE%` (PowerShell env vars) — never hardcode `/home/user/` or `C:\Users\someone\`
- Watch for double-variable typos: `CRITICAL_REPOS_REPOS` → `CRITICAL_REPOS` (duplicated suffix in concatenation)
- Track undefined variable references: scripts that reference `$Bold`, `$Blue` etc. without defining them will silently fail

## Color Escape Handling (PowerShell)

PowerShell scripts using ANSI color codes need explicit variable definitions:

```powershell
$Bold   = "`e[1m"
$Blue   = "`e[34m"
$Red    = "`e[31m"
$Yellow = "`e[33m"
$Gray   = "`e[90m"
$Reset  = "`e[0m"
```

(In bash these are fine as inline escape sequences or `tput` calls — PowerShell requires explicit vars.)

## Bulk Sweep Techniques — Large-Scale Pattern Replacement

When a remediation involves the same fix across 50–200+ files, file-by-file patching is not viable. Use a **bulk sweep** instead.

### When to Sweep

- **Same exact string** in many files (e.g., `@author Adminbot` → `@author Alexa`)
- **Same line to delete** (e.g., `Description placeholder`, `CreatedBy: convert-scripts`)
- Multiple patterns can be combined into one pass

### Workflow from a Session That Cleared 346 Placeholders Across 189 Files

1. **Identify targets** — `search_files(pattern, output_mode="files_only", limit=250)` for each pattern
2. **Merge and deduplicate** — combine into a single file list (union of all patterns)
3. **Exclude non-targets** — filter out `docs/`, `node_modules/`, `.next/`
4. **Apply via Python** — use `execute_code` with native `open()`/`write()` to read each file, apply all replacement patterns, and write back. This is faster and more reliable than `find | xargs sed`.
5. **Verify all patterns at once** — re-run `search_files` for each pattern, confirm zero remaining

### Patterns Swept in This Session

| Pattern | Files Affected | Action |
|---------|---------------|--------|
| `@author Adminbot` | 138 | → `@author Alexa` |
| `Description placeholder` | 187 | Line removed |
| `CreatedBy: convert-scripts` | 21 | Line removed |

**Tip**: Lines removed from JSDoc blocks may leave blank `/**` or `*` comment lines. The extra whitespace is cosmetic and typically safe — but if you need clean blocks, add a follow-up pass that collapses multi-line empty JSDoc.

### Script Template

The skill includes `scripts/bulk-placeholder-sweep.py` — a reusable template. Load it into `execute_code` via:

```python
exec(open("scripts/bulk-placeholder-sweep.py").read())
```

Edit the `REPLACEMENTS` dict and `DELETE_LINES_CONTAINING` set at the top of the script to match your patterns, then run.

## Cross-Platform Drift Detection

When you have parallel Bash/PowerShell/BAT scripts that should behave identically, implement automated drift detection.

### Pair Definition Pattern

Define parallel pairs as arrays so the cross-ref tool can iterate them:

```bash
PAIRS=(
  "install.sh|install.ps1|install.bat"
  "dev.sh|dev.ps1"
)
```

For each pair, check:

1. **Shebangs**: `sh` → `#!/usr/bin/env bash` + `shellcheck shell=bash`. `ps1` → `#!/usr/bin/env pwsh`. `bat` → `@echo off`
2. **Error handling**: `sh` → `set -euo pipefail`. `ps1` → `$ErrorActionPreference = "Stop"`
3. **Version alignment**: If files embed `Version: x.y.z`, all parallel copies match
4. **ShellCheck directive**: Every `.sh` has `# shellcheck shell=bash` on line 2

### Path Resolution Pitfall

When verifying module paths with `$(dirname "$0")/../../lib/`, the resolved path is relative to the script's own directory (`Bash/scripts/`), not the repo root or subproject root. If modules live under `rhixecompany/Banking/install/lib/`, the verify script must account for this:

```bash
# Wrong — resolves to ${PWD}/install/lib/
SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
source "${SCRIPT_DIR}/install/lib/00-config.sh"

# Right — explicitly include the subproject directory
SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
source "${SCRIPT_DIR}/rhixecompany/Banking/install/lib/00-config.sh"
```

Or better, use an env var or config file to decouple the verify script from the module location.

## Git Bash (MSYS) Portability

### `echo -e` vs `printf`

Git Bash's `echo` does not reliably interpret `-e` as an escape flag — it outputs the literal `-e` string. Always use `printf` for formatted output:

```bash
# Wrong on Git Bash:
echo -e "\033[32mOK\033[0m"    # Outputs: -e \033[32mOK\033[0m

# Portable:
printf "\033[32m%s\033[0m\n" "OK"   # Works everywhere
```

### Array Handling in Functions

Indexed arrays may not persist after function exit in Git Bash without explicit `declare -g`:

```bash
# Fragile:
analyze_pair() {
  issues+=("shebang mismatch")  # May be lost after return
}

# Portable:
analyze_pair() {
  echo "shebang mismatch" >> /tmp/issues.txt
}
# Or use string accumulation:
issues=""
analyze_pair() { issues="${issues}shebang mismatch|"; }
```

## Shared Log Rotation Pattern

Create reusable rotation utilities in a `lib/` directory:

### Bash (`lib/log-rotate.sh`)

```bash
#!/usr/bin/env bash
# shellcheck shell=bash
# Usage: rotate_logs <log_file> [max_files=5] [max_age_days=30] [compress_after_days=7]

rotate_logs() {
  local log_file="$1"
  local max_files="${2:-5}"
  local max_age_days="${3:-30}"
  local compress_after_days="${4:-7}"
  local log_dir

  [ -f "$log_file" ] || return 0
  log_dir="$(dirname "$log_file")"

  # Compress files older than compress_after_days
  find "$log_dir" -maxdepth 1 -name "$(basename "$log_file").*" -mtime +"$compress_after_days" \
    ! -name "*.gz" -exec gzip {} \; 2>/dev/null || true

  # Delete files older than max_age_days
  find "$log_dir" -maxdepth 1 -name "$(basename "$log_file")*" -mtime +"$max_age_days" -delete 2>/dev/null || true

  # Rotate current log with timestamp
  local timestamp
  timestamp="$(date +%Y-%m-%d)"
  cp "$log_file" "${log_file}.${timestamp}"
  : > "$log_file"

  # Enforce max_files by deleting oldest
  local count=0
  while IFS= read -r -d '' f; do
    count=$((count + 1))
    if [ "$count" -gt "$max_files" ]; then
      rm -f "$f"
    fi
  done < <(find "$log_dir" -maxdepth 1 -name "$(basename "$log_file").*" -print0 | sort -z)
}
```

### PowerShell (`lib/log-rotate.ps1`)

```powershell
#!/usr/bin/env pwsh
function Rotate-Logs {
    param(
        [Parameter(Mandatory)] [string]$Path,
        [int]$MaxFiles = 5,
        [int]$MaxAgeDays = 30,
        [int]$CompressAfterDays = 7
    )
    if (-not (Test-Path $Path)) { return }
    $dir = Split-Path $Path -Parent
    $base = Split-Path $Path -Leaf
    $now = Get-Date

    # Compress old files
    Get-ChildItem "$dir/$base.*" | Where-Object {
        -not $_.Name.EndsWith('.gz') -and $_.LastWriteTime -lt $now.AddDays(-$CompressAfterDays)
    } | ForEach-Object { gzip $_.FullName }

    # Delete old files
    Get-ChildItem "$dir/$base*" | Where-Object {
        $_.LastWriteTime -lt $now.AddDays(-$MaxAgeDays)
    } | Remove-Item -Force

    # Rotate current
    $timestamp = Get-Date -Format 'yyyy-MM-dd'
    Copy-Item $Path "$Path.$timestamp"
    Set-Content $Path -Value ''

    # Enforce max files
    $files = Get-ChildItem "$dir/$base.*" | Sort-Object LastWriteTime
    while ($files.Count -gt $MaxFiles) {
        $files[0] | Remove-Item -Force
        $files = $files[1..($files.Count - 1)]
    }
}
```

Call from any script that writes logs:

```bash
# In Bash scripts:
source "$(cd "$(dirname "$0")" && pwd)/../lib/log-rotate.sh"
rotate_logs "$LOG_FILE"
```

```powershell
# In PowerShell scripts:
. "$PSScriptRoot/../lib/log-rotate.ps1"
Rotate-Logs -Path "$LOG_FILE"
```

## Modular Shell Refactoring Pattern

When splitting a monolithic shell script (1000+ lines), use numbered modules for ordered sourcing:

```
lib/
  00-config.sh      — Configurable variables and defaults
  01-utils.sh        — Helper functions (logging, error handling, string ops)
  02-paths.sh        — Directory resolution and environment path setup
  03-deps.sh         — Dependency checks (which, version checks)
  04-registry.sh     — Component/tool registry (often 80+ entries)
  05-selection.sh    — Interactive or programmatic selection logic
  06-modes.sh        — Mode switching (install, update, verify)
  07-preview.sh      — Dry-run / preview output generators
  08-install.sh      — Actual installation/copy/execution logic
```

**Orchestrator pattern** (the new thin script):

```bash
#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
for mod in "$script_dir"/lib/0*-*.sh; do
  source "$mod"
done

main "$@"
```

**Validation**: After refactoring, run `bash -n lib/*.sh` across all modules and the orchestrator. The original script's exit paths, argument parsing, and side effects must be identical.

## Verification Checklist

After applying a batch of fixes, verify:

- [ ] Files are syntactically valid (shell: `bash -n`, TypeScript: `tsc --noEmit`)
- [ ] Shebangs are correct (`#!/usr/bin/env bash`, `#!/usr/bin/env pwsh`)
- [ ] No stale JSDoc placeholders remain
- [ ] Shell error handling uses `set -euo pipefail` (not just `set -e` or `set -o pipefail`)
- [ ] ShellCheck `shell=bash` directive present on all bash files
- [ ] No hardcoded absolute user paths
- [ ] Cross-referenced fix claims vs actual disk state
