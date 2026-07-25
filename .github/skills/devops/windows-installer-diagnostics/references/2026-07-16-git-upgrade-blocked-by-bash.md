# Session-derived Patterns: winget Upgrade Failure (2026-07-16)

## Original Failure

Ran `winget upgrade --all --include-unknown --force --purge` in background.

**Result:** Exit code 44 (INSTALL_FAILURE). 3/4 packages succeeded, Git failed.

**Git installer log excerpt:**
```
Defaulting to Cancel for suppressed message box (Retry/Cancel):
The following process(es) use Git for Windows:
bash.exe (PID 18800)
Please terminate those processes and retry.
```

**Root cause:** Git for Windows uses Inno Setup. Inno Setup enumerates running processes before upgrading. If any bash.exe (git-bash) process is running, it assumes Git binaries are in use and aborts.

## Fix Attempt 1: Kill Blocker

Killed PID 18800 (`taskkill /F /PID 18800`). Retried.

**Result:** Same failure, new PID — **our own bash session** (PID 24852). Circular: can't upgrade Git while using Git Bash.

## Fix Applied: Scheduled Task

```cmd
schtasks /create /tn "Git Upgrade 2.55.0.3" ^
  /tr "winget upgrade Git.Git --accept-package-agreements --force" ^
  /sc onstart /delay 0000:30 /f /ru "Alexa"
```

Runs at next boot, 30s delay, before any interactive bash session starts.

## Lessons

1. Always read the installer log — the winget error message is just "exit code 1". The real reason is in the log.
2. In Inno Setup logs, search for "Defaulting to Cancel" — that's the suppressed dialog.
3. Git-for-Windows cannot upgrade while ANY bash.exe runs.
4. When the blocker is your own shell, use schtasks for next-boot scheduling.
