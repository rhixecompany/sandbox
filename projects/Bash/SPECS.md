# Sandbox/Bash Scripts — Technical Specifications

**Version**: 1.0.0 | **Status**: Draft | **Updated**: 2026-05-27

---

## Overview

Technical specifications for 15 scripts (4 shell, 8 PowerShell, 3 batch) with shared TypeScript implementations. All scripts must support standard flags, environment variables, error handling, and logging.

---

## Script Inventory & Specs

### GROUP 1: Package Manager Operations

#### 1.1 upgrade.sh / upgrade.ps1 / upgrade.bat

**Purpose**: Wrapper to upgrade system packages (winget + chocolatey)

**Implementation**: Forwards to `src/upgrade.ts`

**Flags**:

```
--help, -h                Show usage
--debug, -d               Verbose output
--skip-winget            Skip winget, run choco only
--skip-choco             Skip choco, run winget only
```

**Environment Variables**:

```
LOG_DIR             Log directory (default: ./logs)
DEBUG_MODE          Set to 1 for debug output
SKIP_WINGET         Set to 1 to skip winget
SKIP_CHOCO          Set to 1 to skip choco
```

**Exit Codes**:

```
0 - Success (at least one package manager succeeded)
1 - Failure (all package managers failed)
2 - Usage error
```

**Error Handling**:

- [ ] Check bun/bunx availability
- [ ] Check PowerShell version (5.1+)
- [ ] Graceful degradation if winget/choco missing
- [ ] Report which manager failed
- [ ] Log all output to ./logs/upgrade\_\*.log

**Acceptance Criteria**:

- [ ] `upgrade.sh --help` shows usage
- [ ] `upgrade.ps1 -Help` shows usage
- [ ] `upgrade.bat --help` shows usage
- [ ] Missing package managers skipped without error
- [ ] Log file created with timestamp

---

#### 1.2 upgrade-native.ps1

**Purpose**: Native PowerShell package upgrade (no bash required)

**Implementation**: Direct PowerShell (not wrapped)

**Flags**:

```
-Help               Show usage
-DebugMode          Verbose output
-SkipWinget         Skip winget
-SkipChoco          Skip choco
```

**Features**:

- Colored output (red/green/yellow/cyan)
- Progress indicators
- Timestamped logging to ./logs/upgrade*native*\*.log
- Log rotation (keep 10, delete older)

**Exit Codes**:

```
0 - Success
1 - All operations failed
```

**Acceptance Criteria**:

- [ ] `upgrade-native.ps1 -Help` works
- [ ] Colors output correctly
- [ ] Log files created with proper timestamp
- [ ] Old logs deleted (keep max 10)

---

### GROUP 2: Cache Management

#### 2.1 cache-clean.sh / cache-clean.ps1 / cache-clean.bat

**Purpose**: Interactive cache cleaner (14+ cache types)

**Implementation**: Forwards to `src/cache-clean.ts`

**Cache Types Supported**:

```
winget              WinGet cache + DesktopAppInstaller temp
choco               Chocolatey cache + temp
docker              Docker system prune + builder prune
npm                 npm cache + npm-cache folder
pnpm                pnpm store prune
bun                 bun pm cache rm
git-lfs             git lfs prune
nuget               nuget cache
maven               maven repository cache
gradle              gradle cache
rust                cargo/rustup cache
python              pip cache
yarn                yarn cache
golang              go cache
```

**Flags**:

```
--help, -h          Show usage
--all               Clean ALL cache types
--caches X,Y,Z      Clean specific caches (comma-separated)
--auto, -a          Skip confirmations
--dry-run, -n       Preview only (no deletions)
```

**Environment Variables**:

```
LOG_DIR             Log directory (default: ./logs)
CACHES              Comma-separated cache list to clean
AUTO_MODE           Set to 1 to skip confirmations
```

**Interactive Mode**: Prompt per cache type (if not --auto)

**Output**:

- Cache name
- Status (✓/⚠/✗)
- Size/count before/after
- Time elapsed

**Acceptance Criteria**:

- [ ] `cache-clean.sh --all --dry-run` shows what would be deleted
- [ ] `cache-clean.ps1 -caches npm,docker -auto` cleans without prompts
- [ ] Log file created with all operations
- [ ] Graceful skip if cache manager not available

---

### GROUP 3: Dependency Folder Cleanup

#### 3.1 clean_dependency_folders.sh / clean-dependency-folders.ps1/.bat

**Purpose**: Recursive cleanup of dependency folders (node_modules, venv, etc.)

**Implementation**: Forwards to `src/clean-dep.ts`

**Target Types**:

```
node                node_modules, .npm, .pnpm-store, .yarn
python              venv, .venv, __pycache__, .pytest_cache, .mypy_cache
dotnet              bin/, obj/
java                target/, build/
golang              vendor/, go.mod.sum
rust                target/
ruby                Gemfile.lock
php                 vendor/
```

**Flags**:

```
--help, -h          Show usage
--auto, -a          Skip confirmations
--dry-run, -n       Preview only
--paths X,Y,Z       Custom scan paths (comma-separated)
--targets node,py   Specific target types
--max-depth N       Max recursion depth (default: 4)
```

**Environment Variables**:

```
LOG_DIR             Log directory (default: ./logs)
SCAN_PATHS          Comma-separated paths to scan
TARGETS             Comma-separated target types
MAX_DEPTH           Max recursion depth
```

**Output per Scan**:

```
PATH: C:\path\to\scan
FOUND: N folders, XXX.X MB
  target_type       count folders, size
```

**Acceptance Criteria**:

- [ ] `clean-dep.ts --dry-run` shows what would be deleted without deleting
- [ ] Correctly counts folders and sizes
- [ ] Respects max-depth parameter
- [ ] Skips if confirmations required but not --auto
- [ ] Log file created with detailed report

**KNOWN ISSUE**: Import error (FIXED in Phase 2)

```
Was: import { cwd, homedir } from "process";
Now: import { cwd } from "process"; import { homedir } from "os";
```

---

#### 3.2 verify_cleanup.ps1

**Purpose**: Verify that cleanup was successful (no target folders remain)

**Implementation**: Native PowerShell

**Flags**:

```
-Paths X,Y,Z        Custom scan paths
-Targets node,py    Target folder names
-Depth N            Max recursion depth (default: 10)
-Help               Show usage
```

**Environment Variables**:

```
SCAN_PATHS          Semicolon-separated paths
```

**Default Paths** (if not specified):

```
$env:USERPROFILE\Desktop\SandBox
E:\Development
C:\Projects
```

**Output**:

```
=== C:\path\to\scan ===
FOUND: 3 remaining folders
  C:\path\to\scan\node_modules
  C:\path\to\scan\venv
CLEAN: No target folders found
```

**Acceptance Criteria**:

- [ ] Shows remaining target folders (if any)
- [ ] Uses custom paths from -Paths parameter
- [ ] Respects max depth
- [ ] Shows "CLEAN" if all targets removed

---

### GROUP 4: Git Operations

#### 4.1 git-commit-batches.sh / git-commit-batches.ps1

**Purpose**: Batch commit unchanged files in numbered batches

**Implementation**: Forwards to `src/git-commit-batches.ts`

**Flags**:

```
--help, -h          Show usage
--list              List batches only (no commit)
--batch 1-5         Commit batches 1 through 5
--dry-run, -n       Preview only
```

**Environment Variables**:

```
LOG_DIR             Log directory
DRY_RUN             Set to true for dry-run mode
```

**Output**:

```
Batch 1: 5 files, msg=".gitignore + scripts"
Batch 2: 8 files, msg="consolidate wrappers"
...
```

**Acceptance Criteria**:

- [ ] `--list` shows all batches without committing
- [ ] `--batch 1` commits batch 1 only
- [ ] `--dry-run` shows what would be committed
- [ ] Proper git commit messages

---

### GROUP 5: Disk Analysis & Creation

#### 5.1 disk-analysis.ps1

**Purpose**: Scan and report disk space usage by dependency types

**Implementation**: Native PowerShell

**Flags**:

```
-Paths X,Y,Z        Custom scan paths
-MaxDepth N         Max recursion depth (default: 4)
-OutputFile file    Save report to file
-Help               Show usage
```

**Report Contents**:

```
=== Disk Analysis Report ===
Generated: 2026-05-27 21:30:00

SUMMARY
Total Directories: 1,234
Total Size: 45.2 GB
Largest Type: node_modules (22.5 GB)

BREAKDOWN BY TYPE
node_modules        234 dirs,  22.5 GB  (49.7%)
.next               45 dirs,   8.3 GB  (18.3%)
venv                12 dirs,   5.1 GB  (11.2%)
__pycache__         34 dirs,   3.2 GB  (7.1%)
...

TOP 10 LARGEST
C:\path1\node_modules                    2.3 GB
C:\path2\node_modules                    1.9 GB
...
```

**Acceptance Criteria**:

- [ ] Scans multiple paths correctly
- [ ] Calculates sizes accurately
- [ ] Outputs to file or console
- [ ] Respects max-depth

---

#### 5.2 create_skills.ps1

**Purpose**: Create skill stub files for all known skills

**Implementation**: Native PowerShell

**Behavior**:

- Reads hardcoded list of 58 skill names
- For each skill, creates directory: `.opencode/skills/{skill}/`
- Creates stub SKILL.md file with template

**Known Issues** (FIXED):

```
Was: Set-Content on nonexistent directory (error)
Now: Create directory with New-Item before Set-Content
```

**Acceptance Criteria**:

- [ ] Creates 58 skill directories
- [ ] Creates SKILL.md in each
- [ ] Template has structure (description, when to use, workflow, best practices)
- [ ] No errors on repeated execution (idempotent)

---

## Cross-Cutting Standards

### A. Error Handling

All scripts must:

1. **Check Dependencies**

   ```
   - Validate bun/bunx in PATH (shell/batch)
   - Validate PowerShell 5.1+ (ps1)
   - Check git, winget, choco availability (with graceful skip)
   ```

2. **Exit Codes**

   ```
   0 - Success
   1 - General failure
   2 - Usage error (bad flags)
   127 - Command not found
   ```

3. **Error Messages**

   ```
   Format: [ERROR] {context}: {message}
   Example: [ERROR] cache-clean npm: npm not found in PATH
   ```

4. **Graceful Degradation**
   ```
   - If winget missing, skip and try choco
   - If docker missing, skip docker cleanup
   - Report what succeeded, what was skipped
   ```

---

### B. Logging

All scripts must:

1. **Log Directory**

   ```
   Default: ./logs/
   Env var: LOG_DIR
   Created automatically if missing
   ```

2. **Log File Naming**

   ```
   Format: {script}_{timestamp}.log
   Example: cache-clean_20260527_213000.log
   Encoding: UTF-8
   ```

3. **Log Rotation**

   ```
   Keep: Last 10 log files per script
   Delete: Older files automatically
   ```

4. **Log Content**
   ```
   [2026-05-27 21:30:00] Starting cache-clean --all
   [2026-05-27 21:30:01] Checking npm cache...
   [2026-05-27 21:30:02] npm cache: 234 MB freed
   [2026-05-27 21:30:15] All operations complete
   ```

---

### C. Help/Usage

All scripts must support:

**Shell/Batch**: `script.sh --help` or `script.bat /help`

**PowerShell**: `Get-Help .\script.ps1` or `.\script.ps1 -Help`

**Output Format**:

```
{Script Name} v{version}

Usage:
  script [FLAGS] [ARGS]

Flags:
  --help, -h          Show this help
  --debug, -d         Verbose output
  --dry-run, -n       Preview only
  --auto, -a          Skip confirmations

Examples:
  script --help
  script --dry-run
  script --auto

Environment:
  LOG_DIR             Log directory (default: ./logs)
  DEBUG_MODE          Set to 1 for debug

Exit codes:
  0 - Success
  1 - Failure
  2 - Usage error
```

---

### D. Timeout Handling

Scripts with long operations must:

1. **Detect Hangs**

   ```
   - Add timeout flags (--timeout 300)
   - Report progress every 30 seconds
   - Allow user to interrupt (Ctrl+C)
   ```

2. **Signal Handling**
   ```
   - Trap SIGINT (Ctrl+C)
   - Trap SIGTERM
   - Cleanup temp files on exit
   ```

---

## Testing Checklist

### Phase 5 Execution Tests

| Test | Command | Expected |
| --- | --- | --- |
| upgrade help | `bash upgrade.sh --help` | Show usage, exit 0 |
| cache-clean dry | `bash cache-clean.sh --all --dry-run` | List caches, exit 0 |
| clean-dep dry | `bash clean_dependency_folders.sh --dry-run` | Show folders, exit 0 |
| verify cleanup | `pwsh verify_cleanup.ps1` | Show any remaining dirs |
| disk analysis | `pwsh disk-analysis.ps1` | Show size report |
| create skills | `pwsh create_skills.ps1` | Create 58 skill stubs |

---

## Acceptance Criteria (Master)

- [x] All scripts execute --help without error
- [ ] All scripts support --dry-run (preview mode)
- [ ] All scripts support --debug (verbose output)
- [ ] All scripts create ./logs/ directory
- [ ] All scripts log their operations
- [ ] All scripts use consistent error messages
- [ ] All exit codes match specification
- [ ] All TypeScript imports valid
- [ ] All PowerShell syntax valid
- [ ] README.md created with all examples

---

## References

- **PLAN.md**: Phases, timeline, dependencies
- **src/\*.ts**: TypeScript implementations
- **src/lib/**: Shared CLI parsing, colors, errors
- **logs/**: Script execution logs (auto-created)

---

## Sign-Off

- **Created**: 2026-05-27 by Alexa
- **Status**: Draft (awaiting Phase 2 completion)
- **Next**: Begin Phase 2 debugging
