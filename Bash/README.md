# Sandbox/Bash Scripts — Complete Reference

**Status**: Production Ready | **Version**: 3.1.0 | **Updated**: 2026-05-27

---

## Overview

Collection of 15 deployment and maintenance scripts for system administration:

- **4 Shell wrappers** (upgrade.sh, cache-clean.sh, clean_dependency_folders.sh, git-commit-batches.sh)
- **8 PowerShell scripts** (upgrade-native.ps1, upgrade.ps1, cache-clean.ps1, clean-dependency-folders.ps1, create_skills.ps1, disk-analysis.ps1, git-commit-batches.ps1, verify_cleanup.ps1)
- **3 Batch wrappers** (upgrade.bat, cache-clean.bat, clean-dependency-folders.bat)
- **5 TypeScript implementations** (src/upgrade.ts, cache-clean.ts, clean-dep.ts, git-commit-batches.ts)

All scripts follow DRY principles: thin wrappers forward to shared TypeScript implementations.

---

## Prerequisites

### Required

- **Bun 1.3.14+** (for shell/batch wrappers): https://bun.sh
  ```bash
  bun --version
  bunx --version
  ```
- **PowerShell 5.1+** (for .ps1 scripts)
  ```powershell
  $PSVersionTable.PSVersion
  ```
- **Git** (for commit batches)
  ```bash
  git --version
  ```

### Optional (Auto-skipped if Missing)

- **winget** (Windows Package Manager)
  ```bash
  winget --version
  ```
- **Chocolatey** (Package Manager)
  ```bash
  choco --version
  ```
- **Docker** (for cache cleanup)
  ```bash
  docker --version
  ```
- **npm, pnpm, yarn, bun** (for JavaScript/Node.js caches)

---

## Quick Start

### Shell Scripts (Bash)

```bash
cd ~/Desktop/Sandbox/Bash

# Show help
bash upgrade.sh --help
bash cache-clean.sh --help
bash clean_dependency_folders.sh --help
bash git-commit-batches.sh --help

# Run with --dry-run (preview only)
bash cache-clean.sh --all --dry-run
bash clean_dependency_folders.sh --dry-run

# Run with debug output
bash upgrade.sh --debug --skip-choco
```

### PowerShell Scripts

```powershell
cd C:\Users\Alexa\Desktop\Sandbox\Bash

# Show help
. ./upgrade-native.ps1 -Help
. ./cache-clean.ps1 -Help
. ./disk-analysis.ps1 -Help

# Run with parameters
. ./disk-analysis.ps1 -MaxDepth 5
. ./verify_cleanup.ps1 -Paths "C:\Projects","E:\Development"
```

### Batch Files (CMD)

```batch
cd C:\Users\Alexa\Desktop\Sandbox\Bash

upgrade.bat --help
cache-clean.bat --all --dry-run
```

---

## Scripts by Category

### 1. Package Management

#### upgrade.sh / upgrade.ps1 / upgrade.bat

**Purpose**: Upgrade system packages (winget + chocolatey)

**Usage**:

```bash
# Shell
bash upgrade.sh --help
bash upgrade.sh --skip-winget          # Choco only
bash upgrade.sh --skip-choco           # Winget only
bash upgrade.sh --debug                # Verbose output
```

```powershell
# PowerShell
. ./upgrade.ps1 -Help
. ./upgrade.ps1 -SkipWinget            # Skip winget
. ./upgrade.ps1 -SkipChoco             # Skip choco
```

**Options**:

- `--help, -h` — Show usage
- `--debug, -d` — Verbose output
- `--skip-winget` — Skip Windows Package Manager
- `--skip-choco` — Skip Chocolatey

**Environment**:

```bash
LOG_DIR=./logs        # Log directory
DEBUG_MODE=1          # Enable debug
SKIP_WINGET=1         # Skip winget
SKIP_CHOCO=1          # Skip choco
```

**Exit Codes**:

- `0` — Success (at least one manager succeeded)
- `1` — Failure (all managers failed)
- `2` — Usage error

---

#### upgrade-native.ps1

**Purpose**: Native PowerShell upgrade (no bash required)

**Usage**:

```powershell
. ./upgrade-native.ps1                 # Run
. ./upgrade-native.ps1 -Help           # Show help
. ./upgrade-native.ps1 -DebugMode      # Verbose
. ./upgrade-native.ps1 -SkipWinget     # Skip winget
. ./upgrade-native.ps1 -SkipChoco      # Skip choco
```

**Features**:

- Colored output (red/green/yellow/cyan)
- Timestamped logging to `./logs/upgrade_native_*.log`
- Automatic log rotation (keeps last 10)

---

### 2. Cache Management

#### cache-clean.sh / cache-clean.ps1 / cache-clean.bat

**Purpose**: Interactive cleaner for 14+ cache types

**Supported Caches**:

```
winget          Docker          npm             yarn
choco           git-lfs         pnpm            bun
nuget           maven           gradle          rust
python          golang
```

**Usage**:

```bash
# Shell
bash cache-clean.sh --help             # Show help
bash cache-clean.sh --all              # Clean all caches
bash cache-clean.sh --all --auto       # No prompts
bash cache-clean.sh --all --dry-run    # Preview only
bash cache-clean.sh --caches npm,docker # Specific caches
```

```powershell
# PowerShell
. ./cache-clean.ps1 -Help
. ./cache-clean.ps1 -All
. ./cache-clean.ps1 -Auto
. ./cache-clean.ps1 -Caches npm,docker
```

**Options**:

- `--help, -h` — Show usage
- `--all` — Clean ALL caches
- `--caches X,Y,Z` — Clean specific caches (comma-separated)
- `--auto, -a` — Skip confirmations
- `--dry-run, -n` — Preview only (no deletions)

**Output Example**:

```
Cache Cleaner v2 — TypeScript
14 cache type(s) selected

✓ WinGet cache (1ms)
✓ Chocolatey (2231ms)
✓ Docker system prune (511ms)
✓ npm cache cleaned (1879ms)
✓ PNPM store pruned (6575ms)
✓ Bun cache cleared (13031ms)
```

---

### 3. Dependency Cleanup

#### clean_dependency_folders.sh / clean-dependency-folders.ps1/.bat

**Purpose**: Recursively clean dependency folders (node_modules, venv, etc.)

**Target Types**:

```
node            node_modules, .npm, .pnpm-store, .yarn
python          venv, .venv, __pycache__, .pytest_cache
dotnet          bin/, obj/
java            target/, build/
golang          vendor/
rust            target/
ruby            Gemfile.lock
php             vendor/
```

**Usage**:

```bash
# Shell
bash clean_dependency_folders.sh --help        # Show help
bash clean_dependency_folders.sh --dry-run     # Preview only
bash clean_dependency_folders.sh --auto        # Skip confirmations
bash clean_dependency_folders.sh --targets node # Node only
bash clean_dependency_folders.sh --max-depth 3 # Limit depth
```

```powershell
# PowerShell
. ./clean-dependency-folders.ps1 -Help
. ./clean-dependency-folders.ps1 -DryRun
. ./clean-dependency-folders.ps1 -Auto
. ./clean-dependency-folders.ps1 -Targets "node"
```

**Options**:

- `--help, -h` — Show usage
- `--auto, -a` — Skip confirmations
- `--dry-run, -n` — Preview only
- `--paths X,Y,Z` — Custom scan paths (comma-separated)
- `--targets X,Y` — Specific target types (comma-separated)
- `--max-depth N` — Max recursion depth (default: 4)

**Output Example**:

```
Dependency Folder Cleanup v3.1 — TypeScript
Scanning 1 path(s) up to depth 4

  Scanning C:\Users\Alexa\Desktop\SandBox\Bash...
  Found 1 folder(s), 301.1 MB

  node_modules      1 folders, 301.1 MB

Delete these? [Y/n]
```

---

#### verify_cleanup.ps1

**Purpose**: Verify that cleanup was successful

**Usage**:

```powershell
. ./verify_cleanup.ps1                                    # Default
. ./verify_cleanup.ps1 -Paths "C:\Foo","E:\Bar"        # Custom paths
. ./verify_cleanup.ps1 -Targets "node_modules","venv"  # Custom targets
. ./verify_cleanup.ps1 -Depth 5                         # Limit depth
. ./verify_cleanup.ps1 -Help                            # Show help
```

**Output Example**:

```
=== Cleanup Verification ===

=== C:\Users\Alexa\Desktop\SandBox\Bash ===
CLEAN: No target folders found

=== E:\Development ===
FOUND: 2 remaining folders
  E:\Development\projects\node_modules
  E:\Development\venv
```

---

### 4. Disk Analysis

#### disk-analysis.ps1

**Purpose**: Scan and report disk space usage by dependency type

**Usage**:

```powershell
. ./disk-analysis.ps1                              # Default
. ./disk-analysis.ps1 -MaxDepth 5                  # Limit depth
. ./disk-analysis.ps1 -Paths "C:\Foo","E:\Bar"   # Custom paths
. ./disk-analysis.ps1 -OutputFile "report.txt"    # Save to file
. ./disk-analysis.ps1 -Help                       # Show help
```

**Output Example**:

```
===============================================
   Disk Space Analysis  v1.0.0
===============================================

SUMMARY
Total Directories: 1,234
Total Size: 45.2 GB
Largest Type: node_modules (22.5 GB)

BREAKDOWN BY TYPE
node_modules        234 dirs,  22.5 GB  (49.7%)
.next               45 dirs,   8.3 GB  (18.3%)
venv                12 dirs,   5.1 GB  (11.2%)
__pycache__         34 dirs,   3.2 GB  (7.1%)

TOP 10 LARGEST
C:\path1\node_modules                    2.3 GB
C:\path2\.next                           1.9 GB
```

---

### 5. Git Operations

#### git-commit-batches.sh / git-commit-batches.ps1

**Purpose**: Batch commit unchanged files

**Usage**:

```bash
# Shell
bash git-commit-batches.sh --help       # Show usage
bash git-commit-batches.sh --list       # List batches
bash git-commit-batches.sh --batch 1    # Commit batch 1
bash git-commit-batches.sh --batch 1-5  # Commit batches 1-5
bash git-commit-batches.sh --dry-run    # Preview only
```

```powershell
# PowerShell
. ./git-commit-batches.ps1 -Help
. ./git-commit-batches.ps1 -List
. ./git-commit-batches.ps1 -Batch 1
. ./git-commit-batches.ps1 -DryRun
```

**Options**:

- `--help, -h` — Show usage
- `--list` — List batches only (no commit)
- `--batch N` or `--batch N-M` — Commit specific batches
- `--dry-run, -n` — Preview only

**Output Example**:

```
Git Commit Batches

Batch 1: 5 files
  .gitignore + scripts (scripts/.gitignore, scripts/test.sh)
Batch 2: 8 files
  consolidate wrappers (src/*.ts)
```

---

### 6. Skill Creation

#### create_skills.ps1

**Purpose**: Create skill stub files for known skills

**Usage**:

```powershell
. ./create_skills.ps1
```

**Creates**: 58 skill directories with template SKILL.md files

**Output**:

```
Created 58 SKILL.md files
```

---

## Environment Variables

All scripts support these standard environment variables:

```bash
# Logging
LOG_DIR=./logs              # Log directory (created if missing)

# Behavior
DEBUG_MODE=1                # Enable verbose output
AUTO_MODE=1                 # Skip confirmations
DRY_RUN=1                   # Preview only (no mutations)

# Package Management
SKIP_WINGET=1               # Skip Windows Package Manager
SKIP_CHOCO=1                # Skip Chocolatey

# Cleanup
SCAN_PATHS=/path1:/path2    # Paths to scan (colon-separated on bash)
TARGETS=node,python         # Target types (comma-separated)
MAX_DEPTH=4                 # Max recursion depth
```

**Example**:

```bash
LOG_DIR=./my-logs DEBUG_MODE=1 bash upgrade.sh --skip-choco
```

---

## Exit Codes

### Standard Exit Codes

| Code | Meaning           | Example                       |
| ---- | ----------------- | ----------------------------- |
| 0    | Success           | All operations completed      |
| 1    | General failure   | At least one operation failed |
| 2    | Usage error       | Bad flags or arguments        |
| 127  | Command not found | Missing tool in PATH          |

### Script-Specific Codes

**upgrade.sh/ps1**:

- `0` = At least one manager succeeded
- `1` = All managers failed

**cache-clean.sh**:

- `0` = At least one cache cleaned
- `1` = No caches were cleaned

---

## Logging

All scripts create timestamped log files in `./logs/` directory.

### Log File Naming

```
{script}_{timestamp}.log
Example: cache-clean_20260527_213000.log
```

### Log Content

```
[2026-05-27 21:30:00] Starting cache-clean --all
[2026-05-27 21:30:01] Checking npm cache...
[2026-05-27 21:30:02] npm: 234 MB freed
[2026-05-27 21:30:15] Complete
```

### Log Rotation

- Automatic: Keep last 10 logs per script
- Older logs deleted automatically
- Manual cleanup: `rm logs/*.log`

---

## Troubleshooting

### "bunx: command not found"

**Solution**: Install Bun

```bash
curl -fsSL https://bun.sh/install | bash
# Restart terminal or add to PATH
```

### "PowerShell 5.1 required"

**Solution**: Update PowerShell

```powershell
# Check version
$PSVersionTable.PSVersion

# Windows 10/11: Update via Store or:
# Upgrade to PowerShell 7+
choco install powershell-core
```

### "winget/choco not found"

**Solution**: These are optional, scripts auto-skip if missing

```bash
# Install winget (Windows 10/11)
# Built-in, or download from Microsoft Store

# Install Chocolatey
choco install chocolatey
# Or: https://chocolatey.org/install
```

### Script hangs on execution

**Solution**: Use timeout and check logs

```bash
timeout 30 bash cache-clean.sh --help

# Check logs
cat logs/*.log

# Try with --debug for verbose output
bash cache-clean.sh --all --debug
```

### Permission denied

**Solution**: Fix file permissions

```bash
chmod +x *.sh
chmod +x src/*.ts
```

---

## Advanced Usage

### Custom Scan Paths

```bash
# Clean specific directories only
bash clean_dependency_folders.sh --paths /c/projects,/c/work --dry-run
```

### Combine Flags

```bash
# Debug output + dry-run + auto-confirm
bash cache-clean.sh --all --debug --dry-run --auto

# Limit depth for fast scan
bash clean_dependency_folders.sh --max-depth 2 --dry-run
```

### Programmatic Use

```bash
# Capture exit code
bash upgrade.sh --skip-choco
exit_code=$?

# Check result
if [ $exit_code -eq 0 ]; then
    echo "Upgrade succeeded"
else
    echo "Upgrade failed with code $exit_code"
fi
```

---

## Related Documentation

- **PLAN.md** — Phase-by-phase implementation plan
- **SPECS.md** — Detailed technical specifications
- **SUMMARY.md** — Completion report with test results
- **REAL-WORLD-EXAMPLES.md** — Actual execution output and metrics (2026-05-27)
- **test-all.sh** — Automated test suite

---

## Version History

| Version | Date       | Changes                                    |
| ------- | ---------- | ------------------------------------------ |
| 3.1.0   | 2026-05-27 | Consolidation complete; all scripts tested |
| 3.0.0   | 2026-05-25 | Initial implementation                     |

---

## Support

For issues or enhancements, see:

- PLAN.md (current status)
- SPECS.md (technical details)
- Log files in ./logs/ (execution details)

---

## License

MIT

---

**Created**: 2026-05-27 | **Owner**: Alexa | **Status**: Production Ready
