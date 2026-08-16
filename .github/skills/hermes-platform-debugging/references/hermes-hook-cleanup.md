---
name: hermes-hook-cleanup
category: devops
title: "Hermes Hook Cleanup"
description: "Use when auditing, deduplicating, or repairing Hermes shell hook artifacts and stale wrapper scripts on Windows. Covers canonical hook paths, stale `scripts/` wrappers, __pycache__ cleanup, approval documentation, and config-reregistration gaps."
version: 1.0.0
author: Hermes Assistant
license: MIT
tags: [hermes, hooks, cleanup, windows, audit]
---
# Hermes Hook Cleanup

Windows-specific cleanup workflow for Hermes hook directories, wrapper scripts, and stale references.

## Overview

Automated reasoning and workflow tool for `hermes-hook-cleanup`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Auditing Hermes hook directories for stale wrappers or duplicates
- Removing leftover wrapper scripts after migration to canonical hook paths
- Cleaning compiled Python artifacts from hook trees
- Documenting hook cleanup approvals and reregistration gaps

## When NOT to Use

- Linux/macOS environments with different path conventions
- Protected bundled skill editing for hook internals
- General skill-library curation outside the hook/plugin surface

## Goal

Keep the canonical hook tree clean and aligned with live config without duplicating hook entrypoints.

## Prerequisites

- Hermes hook directory exists at `C:/Users/Alexa/AppData/Local/hermes/hooks/`
- At least one of: session-logger, session-auto-commit, governance-audit
- Repo-side `.github/scripts/` may contain stale wrapper copies

## Workflow

### Phase 1: Inspect Live State

```bash
hermes hooks list
hermes hooks doctor
```

Inspect the canonical hook tree:

```bash
find "C:/Users/Alexa/AppData/Local/hermes/hooks" -maxdepth 2 -type f | sort

for name in session-logger session-auto-commit governance-audit; do
  echo "== $name ==";
  ls -la "C:/Users/Alexa/AppData/Local/hermes/hooks/$name";
done
```

Check wrapper scripts in live Hermes scripts dir:

```bash
HERMES_SCRIPTS="$LOCALAPPDATA/../Local/hermes/scripts"
for name in session-logger session-auto-commit governance-audit; do
  echo "== $name ==";
  ls -la "$HERMES_SCRIPTS/$name" 2>/dev/null || echo "missing wrapper";
done
```

Compare wrapper to canonical entrypoint:

```bash
for name in session-logger session-auto-commit governance-audit; do
  diff -u \
    "$LOCALAPPDATA/../Local/hermes/scripts/$name" \
    "C:/Users/Alexa/AppData/Local/hermes/hooks/$name/hook.sh" || true;
done
```

Check repo-local stale copies:

```bash
ls -la .github/scripts/session-logger .github/scripts/session-auto-commit .github/scripts/governance-audit 2>/dev/null || true
```

### Phase 2: Record Approval

Create `.hermes/approvals/<timestamp>_<short-title>.md` with:

- Request/Action summary
- Scope
- Authorized route
- Verification commands
- Approval fields

For this cleanup, typical scope covers:
- Removing stale wrapper scripts in `.github/scripts/`
- Removing stale wrapper scripts in `~/AppData/Local/hermes/scripts/`
- Removing `__pycache__` directories under hook trees
- Normalizing repo docs/workflows/instructions references to canonical hook paths
- Noting config reregistration status or blockers

### Phase 3: Cleanup

Remove repo wrapper copies:

```bash
rm -f .github/scripts/session-logger \
      .github/scripts/session-auto-commit \
      .github/scripts/governance-audit
```

Remove stale live wrappers:

```bash
HERMES_SCRIPTS="$LOCALAPPDATA/../Local/hermes/scripts"
for name in session-logger session-auto-commit governance-audit; do
  rm -f "$HERMES_SCRIPTS/$name";
done
```

Remove compiled Python caches from hook trees:

```bash
HERMES_HOOKS="$LOCALAPPDATA/../Local/hermes/hooks"
for name in session-logger session-auto-commit governance-audit; do
  rm -rf "$HERMES_HOOKS/$name/__pycache__";
done
```

### Phase 4: Verify

Temporary ad-hoc verification script outline:

```python
from pathlib import Path

LOCALAPPDATA = "C:/Users/Alexa/AppData/Local"
ROOT = Path("C:/Users/Alexa/Desktop/SandBox")
HOOKS = Path(LOCALAPPDATA) / "hermes" / "hooks"
SCRIPTS = ROOT / ".github" / "scripts"
LIVE_SCRIPTS = Path(LOCALAPPDATA) / "hermes" / "scripts"
CHECKS = []

def ok_or_fail(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status}\t{name}{(' | ' + detail) if detail else ''}")
    CHECKS.append((name, condition))

for name in ("session-logger", "session-auto-commit", "governance-audit"):
    repo_paths = [SCRIPTS / name]
    repo_missing = not any(p.exists() for p in repo_paths)
    ok_or_fail(f"repo/{name}/removed", repo_missing, str(repo_paths) if not repo_missing else "")
    canonical = HOOKS / name / "hook.sh"
    ok_or_fail(f"canonical/{name}/hook.sh/exists", canonical.exists(), str(canonical))
    live = LIVE_SCRIPTS / name
    ok_or_fail(f"live/scripts/{name}/removed", not live.exists(), str(live) if live.exists() else "")
    meta = HOOKS / name / "hooks.json"
    ok_or_fail(f"hook/{name}/hooks.json/exists", meta.exists(), str(meta))
    pc = HOOKS / name / "__pycache__"
    ok_or_fail(f"hook/{name}/__pycache__/removed", not pc.exists(), str(pc) if pc.exists() else "")

if any(condition is False for _, condition in CHECKS):
    raise SystemExit("VERIFY_FAILED")
print("VERIFY_OK")
```

Run Hermes validation:

```bash
hermes hooks list
hermes hooks doctor
grep -A 20 "^hooks:" "$LOCALAPPDATA/hermes/config.yaml"
```

### Phase 5: Document Session State

Update `SESSION_REPORT.md` with:

- Current hook state
- Exact files removed
- Approval file path
- Remaining config/reregistration blocker, if any

## Pitfalls

- **Protected config edits:** direct edits to `config.yaml` may be blocked by Hermes security tooling; use approved Hermes config workflow when possible.
- **Missing CLI register path:** this install may not expose a local `hermes hooks register/add` command; document the gap and keep approval notes current.
- **Wrapper drift:** thin wrapper scripts in multiple locations drift independently; prefer one canonical entrypoint plus thin deploy-time launchers.
- **Backup pollution:** never create `.bak` or timestamped copies during hook cleanup; use git or approval notes instead.

## Verification Checklist

- [ ] Approval file recorded before destructive removal
- [ ] Stale wrapper scripts removed from repo and live Hermes scripts dir
- [ ] `__pycache__` removed from each affected hook dir
- [ ] Canonical `hook.sh`, `hook.py`, and `hooks.json` remain
- [ ] `hermes hooks list` and `hermes hooks doctor` reviewed
- [ ] `SESSION_REPORT.md` reflects exact changed artifacts
