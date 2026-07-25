# Shellcheck Verification Patterns

> Reusable shellcheck command patterns for verification-before-completion of shell script remediation plans.

## Install Shellcheck

```bash
# via npm (works on Windows, no admin needed)
npm install -g shellcheck

# or via package manager
choco install shellcheck      # Windows (admin)
brew install shellcheck       # macOS
apt install shellcheck        # Debian/Ubuntu
```

## Verify Shellcheck is Working

```bash
shellcheck --version
# Expect: ShellCheck - shell script analysis tool, version 0.11.0+
```

## Quick Error Count (All Files)

```bash
# Count only actual errors (exits 1 if none found — OK)
shellcheck -f gcc file1.sh file2.sh ... 2>&1 | grep -c "error:" || echo 0

# Separate counts for errors, warnings, notes
echo "=== ERRORS ==="
shellcheck -f gcc file1.sh ... 2>&1 | grep "^.*error:" | wc -l
echo "=== WARNINGS ==="
shellcheck -f gcc file1.sh ... 2>&1 | grep "^.*warning:" | wc -l
echo "=== NOTES ==="
shellcheck -f gcc file1.sh ... 2>&1 | grep "^.*note:" | wc -l
```

## Per-Category Shellcheck (Organized by Directory)

```bash
# Group scripts by area for cleaner reporting
BASH_FILES="Bash/scripts/phase-1-deep-triage.sh Bash/scripts/run-audit.sh Bash/upgrade.sh Bash/clean_dependency_folders.sh"
COMICWISE_FILES="Rhixe-company/comicwise/quality-gate.sh Rhixe-company/comicwise/dev.sh"
BANKING_FILES="rhixecompany/Banking/install.sh rhixecompany/Banking/install-agents.sh rhixecompany/Banking/scripts/orchestrator.sh rhixecompany/Banking/scripts/verify-agents.sh"

echo "--- Bash ---"
shellcheck -f gcc $BASH_FILES 2>&1 | grep -c "error:" || echo 0

echo "--- ComicWise ---"
shellcheck -f gcc $COMICWISE_FILES 2>&1 | grep -c "error:" || echo 0

echo "--- Banking ---"
shellcheck -f gcc $BANKING_FILES 2>&1 | grep -c "error:" || echo 0
```

## Full Shellcheck Output (for Debugging)

```bash
# Show all findings with file locations
shellcheck -f gcc file.sh

# SC#-filtered output (show only SC2155 warnings)
shellcheck -f gcc file.sh 2>&1 | grep "SC2155"

# Suppress notes, show only errors + warnings
shellcheck -f gcc -S warning file.sh
```

## Common Warning Codes

| Code | Meaning | Severity |
|------|---------|----------|
| SC2155 | `local` + assignment masks return value | warning |
| SC2086 | Double-quote to prevent globbing/word-splitting | note |
| SC2181 | Check exit code with `if ! cmd;` not `$?` | note |
| SC2129 | Use `{ cmd; } >> file` not individual redirects | note |
| SC2162 | `read -r` to prevent backslash mangling | note |
| SC2178 | Variable used as array but assigned string | warning |

## Verification Summary Table Template

```markdown
### Shellcheck Results

| Area | Files | Errors | Warnings | Notes |
|------|-------|--------|----------|-------|
| Bash/scripts/*.sh | 5 | 0 | 8 | 14 |
| Rhixe-company/comicwise/*.sh | 2 | 0 | 0 | 2 |
| rhixecompany/Banking/*.sh | 7 | 0 | 10 | 24 |
| **Total** | **14** | **0** | **18** | **40** |

> Shellcheck warnings are pre-existing style items (SC2155 declare-and-assign,
> SC2086 double-quoting) — not introduced by remediation.
```
