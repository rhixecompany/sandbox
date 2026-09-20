# Scope: Skill registry cleanup and duplicate consolidation

**Feature**: Inspect and install skills from `jsmastery-pro/skills` and `vercel-labs/agent-skills`, then triage duplicates (best categorized version at `$HERMES_HOME/skills/`), consolidate, and delete extras.

**What it builds**: Clean registry with only best categorized versions; verified scope/plans/specs; no synthetic results.
**Who it's for**: Workspace agent profiles (default, adminbot, architect, analyst, creative, dev, ops, pm, security, tutor, exec-assistant).

**Build approach**: Tracer bullet — inspect all, ask per identifier, install confirmed, consolidate, delete.
**Workflow tier**: Alpha — verify after install; check profile-dir match before delete.

## At a glance

|| # | Feature | Phase | Status |
||---|---------|-------|--------|
|| 1 | Skill registry inspection and install | Foundation | in progress |
|| 2 | Duplicate triage and consolidation | Foundation | planned |
|| 3 | Best categorized version verification | Verification | planned |

## Feature

### 1. Skill registry inspection and install · in progress
Inspect `jsmastery-pro/skills` (13 results) and `vercel-labs/agent-skills` (10 results) via `hermes skills inspect`. Confirm per identifier before `install -y --force --category CATEGORY`.

**Done when**: All identifiers inspected; non-timeout skills confirmed for install; timeout skills (`architect`, `audit` from jsm; `vercel-composition-patterns`, `vercel-deploy`, `vercel-optimize` from vercel) resolved (re-inspect or skip).

- [ ] Inspect batch 1 (done: check, debug, develop, deploy-to-vercel, vercel-cli-with-tokens pass; 3 timeouts)
- [ ] Confirm install: check / debug / develop / deploy-to-vercel / vercel-cli-with-tokens
- [ ] Re-inspect timeout skills (architect, audit, vercel-composition-patterns, vercel-deploy, vercel-optimize)

### 2. Duplicate triage and consolidation · planned
Compare installed skills at `$HERMES_HOME/skills/` (162 installed) against new installs. Best categorized version = profile-directory match (profile dir empty; best = hub-installed match). Delete others.

**Done when**: Only best categorized versions remain; duplicates removed with verification.

- [ ] Identify duplicates (compare names/categories)
- [ ] Confirm best version for each duplicate group
- [ ] Delete duplicates (with user confirmation per group if needed)

### 3. Best categorized version verification · planned
Verify profile-dir or hub-dir contains only best categorized versions.

**Done when**: `ls $HERMES_HOME/skills/` shows no duplicate identifiers; `docs/scope/` and `.hermes/plans/` document the final registry state.

- [ ] Final registry audit (`hermes skills audit` or `find` comparison)
- [ ] Evidence saved (no synthetic artifacts)
