---
name: disk-space-cleanup
title: Disk Space Cleanup
description: 'Free disk space by safely deleting reinstallable artifacts across repos, subrepos, Hermes roots, caches, logs, and temp files with dry-run-first verification.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
  - cleanup
  - disk
  - hermes
  - ops
  - workflow
trigger: /disk-space-cleanup
formatter: default
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:verification-before-completion
  - skill:disk-space-cleanup
toolsets:
  - clarify
  - file
  - terminal
scripts:
  - ~/Desktop/SandBox/scripts/cleanup_disk.py
skills:
  - using-superpowers
  - user-communication-preferences
  - verification-before-completion
  - disk-space-cleanup
plan: None
metadata:
  hermes: {}
---

## Goal

Free disk space on the host by safely deleting stale, reinstallable artifacts across repository roots, subrepos, the Hermes agent root, and the `hermes-profiles` mirror — then verify the reclaimed space and report the before/after delta.

## Context

- Host: Windows 11 with MSYS2/git-bash.
- Native Windows Python prefers `C:/...` paths; set `MSYS_NO_PATHCONV=1` when invoking Windows-native Python from git-bash.
- Canonical script: `scripts/cleanup_disk.py`.
- Scope usually includes repo roots, `projects/`, `hermes-profiles/`, and `~/AppData/Local/hermes`.

## Workflow

1. Measure first:
   - `df -h /c`
   - `du -sh <candidate roots>`
2. Dry-run first with the canonical script:
   - `python scripts/cleanup_disk.py --verify --min-size 5 <Windows-style root paths...>`
3. Review the reclaimable total and the per-category breakdown.
4. Ask for explicit approval before any destructive apply.
5. If approved, rerun with `--apply` and the narrowest safe category set.
6. For the Hermes root, keep the sweep conservative: prefer `--cats cache,logs,archive` so runtime deps are preserved.
7. For OS temp folders, delete age-qualified files only; do not rmtree the whole directory.
8. For bloated `.git` directories, `git gc --prune=now` is allowed; history-rewriting commands are not.
9. For installed apps, inventory first with `winget list`, present a deletion list, and stop for approval before uninstalling.
10. Measure after:
    - `df -h /c`
    - report bytes reclaimed, items freed, and any locked/error items.

## Verification Checklist

- [ ] Dry-run output reviewed before deletion.
- [ ] User approval captured before `--apply`.
- [ ] `df -h /c` shows measurable free-space gain.
- [ ] Locked files or skipped targets are documented.
- [ ] `results/cleanup_disk.log` contains the deletion audit trail.

## Guardrails

- Never delete a `.git` directory or a configured root itself.
- Never uninstall an app without an approved list.
- Never run history-rewriting git commands without explicit approval.
- Dry-run is the default; `--apply` only after full-sweep intent is confirmed.
