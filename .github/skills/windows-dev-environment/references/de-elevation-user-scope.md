---
name: windows-deelevation
title: Windows De-elevation
description: "De-elevate user-scope Windows ops from an admin shell."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - devops
  - windows
  - elevation
  - winget
  - user-scope
---

## Overview

This skill provides a generic mechanism to de-elevate from an admin shell on Windows to run user-scope operations (winget/choco uninstall, user registry, user env vars) that fail with exit 125 when run elevated.

## Workflow

### Phase 1: Detect Elevation
- Run `net session >/dev/null 2>&1 && echo ELEVATED || echo NOT-elevated`
- Check registry for `FilterAdministratorToken` value

### Phase 2: Create Limited-Token Scheduled Task
- Register a Scheduled Task with `/RL LIMITED` pointing at a `.bat` file
- Run the task and poll for completion
- Delete the temporary task

### Phase 3: Verify De-elevation Success
- Check task log for `DONE` marker
- Verify target packages are uninstalled with `winget list --id <id>`
- Confirm disk space increased if uninstalling for space

---

## Detect elevation
You are running in an **elevated (admin)** shell on Windows and an operation that targets **user-scope** state fails because it must NOT run as admin. Canonical case: `winget uninstall` of a user-scope package → exit 125 "The package installed for user scope cannot be uninstalled when running with administrator privileges." Applies to any user-scope change (winget/choco uninstall, user registry, user env vars) that a non-elevated token requires.

## Detect elevation
```bash
net session >/dev/null 2>&1 && echo ELEVATED || echo NOT-elevated
```
Also check `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v FilterAdministratorToken` — value `0x1` means UAC applies to the admin token, confirming the privileged context that triggers the refusal.

## The problem
Machine-scope installs (e.g. EclipseAdoptium.Temurin.21.JDK, Erlang.ErlangOTP, GoLang.Go, BleachBit) uninstall fine *elevated*. **User-scope** packages (Dart SDK, Julia, GitHub.Copilot CLI, BtbN.FFmpeg.LGPL.7.1, NirSoft utils) are refused with exit 125 from an admin token. Retrying elevated always fails — you must de-elevate.

## The fix — limited-token one-shot scheduled task
Register a Scheduled Task with `/RL LIMITED` (runs as the logged-in user with a filtered/limited token, NOT admin), pointing at a small `.bat`; run it; delete it:
```bash
schtasks /Create /TN "HermesOp" /TR "cmd /c call C:\path\to\op.bat" /SC ONCE /ST 23:59 /RL LIMITED /F
schtasks /Run /TN "HermesOp"
# poll until done:  for i in $(seq 1 10); do sleep 3; tasklist /FI "IMAGENAME eq winget.exe" 2>/dev/null | grep -qi winget || break; done
schtasks /Delete /TN "HermesOp" /F
```

The `.bat` (one `winget uninstall --id <id> --silent --disable-interactivity` per package, each appending `rc=%errorlevel% <id>` to a log):
```bat
@echo off
set LOG=%USERPROFILE%\Desktop\SandBox\results\op.log
echo [%date% %time%] START > "%LOG%"
winget uninstall --id Julialang.Julia --silent --disable-interactivity >> "%LOG%" 2>&1
echo rc=%errorlevel% Julia >> "%LOG%"
echo [%date% %time%] DONE >> "%LOG%"
```
MSYS: for the log path / root args, use Windows-style `C:/...` paths and `MSYS_NO_PATHCONV=1` with native Windows exes.

---

## Pitfalls
- **Do NOT parse a comma-delimited inline list in `for /f` for package IDs.** The double-`%%` expansion plus comma `delims` mangles the tokens (you get literal `%a` and "No installed package found" false-negatives). Write one explicit `winget uninstall` line per package — clear and debuggable.
- Verify removal with `winget list --id <id>`; "No installed package found matching input criteria" = fully gone. Also trust the `.bat` log's `DONE` marker as run-completion proof.
- Clean up the temporary task (`schtasks /Delete`) after the run so it doesn't linger.
- If still refused, the package may need its owning app context (e.g. MSIX from Store) — check scope, don't force.

## Verification Checklist

- [ ] Task log reaches `DONE`
- [ ] `winget list --id <id>` for each target returns "No installed package found."
- [ ] `df`/disk free increases by the expected amount if uninstalling for space
- [ ] Temporary scheduled task cleaned up (`schtasks /Delete` confirmed)

## Skills Required

| Skill | Purpose |
| ------- | --------- |
| `devops/windows-package-management` | Winget/choco package operations |
| `devops/disk-space-cleanup` | Disk space verification after uninstall |

## Overlap note
Uninstall/size guidance also lives in `windows-package-management` and `disk-space-cleanup`; this skill is the generic token-elevation mechanism that unblocks user-scope ops from an admin shell.