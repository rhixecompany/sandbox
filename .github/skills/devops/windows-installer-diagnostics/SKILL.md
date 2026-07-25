---
name: windows-installer-diagnostics
title: "Windows Installer Diagnostics"
description: "Diagnose and fix Windows package installer failures — exit codes, installer logs, process blockers, background execution, and retry strategies. Complements windows-package-management (happy path)."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [windows, winget, installer, troubleshooting, diagnostics]
related_skills:
  - windows-package-management
---
# Windows Installer Diagnostics

Diagnose and fix Windows package installer failures. Use when winget upgrades fail, MSI installers abort, or setup programs return non-zero exit codes.

## When to Use

- `winget upgrade --all` exits non-zero (especially code 44)
- Installer fails silently with exit code 1
- Inno Setup / MSI installer aborts mid-install
- Installer reports "process(es) use [program]" and refuses to proceed
- Any Windows software install/upgrade that returns a non-success exit code

**Complements:** `windows-package-management` (happy-path list/install/upgrade/migrate) — use that for normal operations, this for failures.

## Workflow

### Phase 1: Capture the Failure

Run the operation in background so output isn't lost:

```bash
terminal(command="winget upgrade --all --include-unknown --force --purge",
         background=true, notify_on_complete=true, timeout=1200)
```

On notification, get full output:
```bash
process(action="log", session_id="<id>")
```

### Phase 2: Identify Exit Code

Winget exit codes:
| Code | Meaning |
|------|---------|
| 0 | All upgrades succeeded |
| 44 | INSTALL_FAILURE — one or more packages failed |
| Other | General error |

For exit code 44, scan the output for per-package failure lines:
```
Installer failed with exit code: 1
Installer log available at: ...\DiagOutputDir\<Package>.<Version>-<timestamp>.log
```

### Phase 3: Read Installer Log

The log is an Inno Setup log (for Git, AnyDesk, and many winget packages). Format:
- First ~165 lines: DLL-import boilerplate (skip)
- Last ~10 lines: actual failure reason

```bash
# Read from near the end:
read_file(path="<log-path>", offset=120, limit=60)
```

Search output for **"Defaulting to Cancel"** — this is the suppressed message box text that contains the real reason.

### Phase 4: Process-Blocker Diagnosis

Common pattern — installer detects a process holding the binary:

```
The following process(es) use Git for Windows:
bash.exe (PID 18800)
Please terminate those processes and retry.
```

| Blocker Process | Why | Fix |
|----------------|-----|-----|
| `bash.exe` | Git Bash holds handles on git.exe | Kill with `taskkill /F /PID <n>` |
| `git.exe` | Active git operation | Wait or kill |

### Phase 5: Fix and Retry

**If the blocker is NOT your agent session:**
```bash
taskkill /F /PID <blocker-pid>
winget upgrade <Package.Id> --accept-package-agreements --force
```

**If the blocker IS your agent session** (you're running in bash and bash is the blocker):
The circular dependency means you can't upgrade Git without killing your own shell.

Options:
1. **Schedule for next boot** — runs before any interactive bash:
   ```cmd
   schtasks /create /tn "Git Upgrade <version>" ^
     /tr "winget upgrade Git.Git --accept-package-agreements --force" ^
     /sc onstart /delay 0000:30 /f /ru "<username>"
   ```
2. **Skip and notify user** — report the blocker, let them close bash and retry manually.

### Phase 6: Verify

After successful retry:
```bash
winget list --source winget --name Git  # verify new version
```

## Pitfalls

- **Inno Setup logs look like noise.** The first 165 lines are DLL import boilerplate every time. Scroll to the end for the real failure. The default "Cancel" for a suppressed message box is the actual reason.
- **Exit code 44 ≠ all failed.** One package failing triggers exit 44 while others may have installed fine. Check per-package results.
- **`--force` doesn't bypass process checks.** winget's `--force` bypasses hash verification, not running-process detection. That's the installer itself (Inno Setup) refusing.
- **Killing bash.exe may kill the agent.** When running in Git Bash, `taskkill /F /IM bash.exe` terminates the agent session along with all other bash processes. Use `schtasks` instead.

## Flag Reference

| Flag | Effect | Risk |
|------|--------|------|
| `--include-unknown` | Packages from untrusted sources | Security: vet unknown sources |
| `--force` | Bypass hash verification | Can install tampered packages |
| `--purge` | Delete manifests after success | Can't reinstall same version |
| `--accept-package-agreements` | Auto-accept license prompts | Safe for non-interactive |

## Verification Checklist

- [ ] Exit code captured and interpreted
- [ ] Installer log read and root cause identified
- [ ] Blocker process resolved (killed or scheduled)
- [ ] Failed package retried successfully
- [ ] New version verified with `winget list`

## References

- `windows-package-management` — Happy-path winget/choco operations
- See `references/winget-exit-codes.md` for a complete winget exit code reference
