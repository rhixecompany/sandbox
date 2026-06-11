# Sandbox Runbook Fill Guide

Use this guide to populate runtime and reporting files during migration execution.

## Files this guide covers

- docs/sandbox-projects-runtime-inventory.md
- docs/sandbox-patch-discovery.md
- docs/sandbox-patch-application-report.md
- docs/sandbox-migration-final-report.md

## Step 1: Generate runtime inventory

Run in PowerShell:

```powershell
Get-ChildItem "C:\Users\Alexa\Desktop\SandBox\projects" -Directory |
  Select-Object Name, FullName |
  Format-Table -AutoSize
```

Copy results into `docs/sandbox-projects-runtime-inventory.md`.

Required fields per project:

- project-name
- full-path
- has-git-repo
- language-hints
- notes

## Step 2: Generate patch discovery

Run in PowerShell:

```powershell
Get-ChildItem "C:\Users\Alexa\Desktop\SandBox" -Recurse -Filter *.patch |
  Select-Object Name, FullName |
  Sort-Object FullName
```

Copy results into `docs/sandbox-patch-discovery.md`.

For each patch, record:

- patch-file
- suggested-target-project
- mapping-confidence
- mapping-reason

## Step 3: Process patches and update patch report

For each mapped patch:

1. From target project root, run dry check:

```powershell
git apply --check "PATCH_FILE"
```

1. If pass, apply:

```powershell
git apply --index --3way "PATCH_FILE"
```

1. Update `docs/sandbox-patch-application-report.md` with terminal status:

- applied
- skipped-with-justification
- blocked-with-remediation

1. Add rollback checkpoint note.

## Step 4: Validate projects after patching

Use project-native checks when available:

- install/build/test
- lint/typecheck
- smoke run

Record outcomes in `docs/sandbox-migration-final-report.md`.

## Step 5: Finalize migration report

`docs/sandbox-migration-final-report.md` must include:

- project counts before and after
- generator-orchestrator matrix
- patch processing matrix
- remediation checklist
- final pass/fail decision

## Gate rules

- Stop if backup checklist is incomplete.
- Stop if any project fails generator-orchestrator consistency gate.
- Never force apply a patch that fails `git apply --check`.
- A PASS requires all patches to have terminal statuses and no unresolved critical failures.
