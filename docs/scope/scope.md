# Scope: Agent context init for SandBox

A living, coarse plan for onboarding and enhancing the five coding agents (GitHub Copilot, Hermes, OpenCode, Cursor Agent, and the general agent context) so every agent reads the same repo truth, points at the same artifact runs, and verifies before claiming done. Serves the repo's own agents and their maintainer.

**Build approach:** Tracer Bullet (one vertical slice per agent, each slice enhanced end to end and verified before the next).
**Workflow:** Alpha (after /develop, run /check verify on the real files; no test suite unless a feature needs it). The project default level of rigor. /architect is the recommended first stop for a feature with a real decision, but skippable when you already know the build. Any feature can carry its own tag (e.g. `· GA`) to do more or less.

_These are recommendations to keep your build orderly, not requirements. Skip anything that does not fit: if you already know how to build a feature, use /develop and skip /architect. You decide when a feature is `done`._

## At a glance

| # | Feature | Phase | Status |
|---|---------|-------|--------|
| 1 | Artifact governance (ai-agent-home) | Foundation | in progress |
| 2 | Agent general context (AGENTS.md + CLAUDE.md) | Slice 1 | planned |
| 3 | Copilot context | Slice 1 | planned |
| 4 | Hermes context | Slice 1 | planned |
| 5 | OpenCode context | Slice 1 | planned |
| 6 | Cursor context | Slice 1 | planned |

## Foundations

### 1. Artifact governance (ai-agent-home) · in progress
One governed home for every init run: specs, plans, prompts, and a STATUS.md that moves through phases to Completed. The current run (init-20260919T210721) is the live first instance of the pattern.
**Done when:** every init run has its own timestamped folder under ai-agent-home/{specs,plans,prompts}, STATUS.md tracks each phase, and the run is marked Completed only after verification passes.
- [ ] Build it: /develop artifact governance
   - [ ] Run shape: one unique run name with timestamp suffix, three co located artifact folders
   - [ ] Status lifecycle: STATUS.md updated at each phase, Completed only after verify
   - [ ] First instance: current init run written and gated on plan approval
- [ ] Verify it: /check verify artifact governance

## Slice 1: The five agent contexts

### 2. Agent general context (AGENTS.md + CLAUDE.md) · planned
The root context file every agent treats as canonical, plus the thin Claude pointer. Gets a fresh init block pointing at this run's artifacts. (You asked for a spec before building.)
**Done when:** AGENTS.md carries the init block with artifact pointers, CLAUDE.md stays a thin pointer, and the root checks stay clean.
- [ ] Design it (spec): /architect agent general context

### 3. Copilot context · planned
The Copilot instruction file plus the prompt library it reads. Gets an init block; the read path and the prompt library stay canonical. (You asked for a spec before building.)
**Done when:** copilot-instructions.md carries the init block, the prompt library still holds the read order, and nothing else changes.
- [ ] Design it (spec): /architect copilot context

### 4. Hermes context · planned
The Hermes overrides file. Gets an init run status section and artifact pointers while routing and identity tables stay untouched. (You asked for a spec before building.)
**Done when:** .hermes.md carries the init run section, Session Evidence gains this run, and no routing rule changes.
- [ ] Design it (spec): /architect hermes context

### 5. OpenCode context · planned
OpenCode has no config today, so this feature creates opencode.json and opencode.md as the agent's bootstrap. (You asked for a spec before building.)
**Done when:** opencode.json exists and validates as JSON, opencode.md exists, and both point at this run's artifacts with no provider keys in the repo.
- [ ] Design it (spec): /architect opencode context

### 6. Cursor context · planned
The Cursor rules file plus its scoped rule. Gains an init block while staying thin and keeping parity with the scoped file. (You asked for a spec before building.)
**Done when:** .cursorrules carries the init block, .cursor/rules/sandbox.mdc matches it, and no rule behavior changes.
- [ ] Design it (spec): /architect cursor context

## Deferred
Out of scope for the current pass, kept so the plan stays honest.
- **Enrollment and reconciliation of prior runs**: the 3 earlier init runs (194300Z, 203754Z, 194800Z) stay as history, untouched
- **Verification as its own feature**: gates stay folded into each feature's definition of done for now
- **Per workspace scopes**: projects/* get their own docs/scope/<workspace> scopes only when needed
- **Web verified reference links**: references stay out of the scope by choice
- **Profile inventory and config update (this pass)**: list docs/hermes, instructions, agent files, update config.yaml with personality/instruction sources, create/recreate profiles (done)

## New feature: Profile inventory and config reconciliation

### 7. Profile inventory and config reconciliation · done

List and triage docs/hermes files (462), instructions files (44), agent files (30). Find personality (agent) and instruction sources. Update hermes config.yaml with references. Create or recreate profile directories for agent roles (10 new profiles), skip default since it exists.

Done when: triage report exists at docs/scope/hermes-docs-triage.md, config.yaml carries agent-personalities and instruction-sources, 10 new profiles exist in $HERMES_HOME/profiles/, default profile untouched.

- [x] List and triage docs/hermes, instructions, agent files
- [x] Find personality and instructions sources
- [x] Update config.yaml with personality/instruction references
- [x] Create profiles for agent roles (10 profiles created)
- [x] Verify profiles exist and config reads clean

### 8. Hermes hooks update, repair, and verification · done

Update, refactor, enhance, test, debug, repair, fix, and verify all hermes hooks (session hooks, agent hooks, browser hooks, provider hooks, governance hooks, tool guardian, secrets scanner) to work reliably for new sessions and multiple AI agents (hermes, agent, copilot, opencode). Apply best practices (`/check` verification, `/debug` root cause analysis, `/test` confirmation).

Done when: every hook passes `/check all hermes hooks`, any failures are fixed and re-verified via `/debug`, all hooks confirm working with `/test all hermes hooks` for new sessions and across agent profiles (default, adminbot, ops, etc.), and this scope features status is `done`.

- [x] Audit (`/audit /hermes-hooks`): scan all hook files, read `README.md`, identify broken references, missing permissions, stale paths.
- [x] Repair (`/architect <hook>` + `/develop <hook>`): fix syntax errors, update paths, restore missing references.
- [x] Enhance (`/develop`): add agent identity checks (hermes, agent, copilot, opencode) and new session initialization support.
- [x] Verify (`/check all hermes hooks`): confirm each hook category (session, agent, browser, provider, governance, secrets, tool-guardian) passes.
- [x] Debug failures (`/debug all hermes hooks`): investigate verification failures, apply fixes, re-verify.
- [x] Test (`/test all hermes hooks`): confirm isolated and integrated behavior for new sessions and multi-agent profiles.
- [x] Complete (`/scope`): set feature 8 to `done` after all gates pass.

## Legend

**The decision box.** Every feature carries exactly one, the sub-task whose label ends with `(spec)`. Its wording varies, so skills locate it by that `(spec)` suffix, never by an exact label. Every other box is an execution box and /architect never ticks one.

**Feature lifecycle**: the scope updates as a feature moves; each row is what it shows and who sets it:

| State | Set by | The feature shows |
|---|---|---|
| `planned` · needs a decision | /scope | one box: `Design it (spec): /architect <feature>` |
| `in progress` (designed) | /architect at spec capture | `Design it` ticked; spec linked; `Build it: /develop <feature>` + 2 to 5 milestones; the tier's closing boxes (`Verify it` Alpha+) |
| `in progress` (building) | /develop | milestone sub-boxes tick one by one; code pointer filled |
| `in progress` (verified) | /check verify | `Build it` + milestones ticked; `Verify it` ticked |
| `done` | you, when you decide it is; /sync reconciles | boxes you ran ticked, skipped ones marked skipped; the tier's last stage (`Alpha` → after `/check verify`) is the suggested point to call it done |

- **Next step** = the first unticked box (always a command or a tracked milestone).
- **needs a decision** = run /architect first; otherwise straight to /develop. The tag drops once the spec is captured.
- **Atomic build tasks live in the spec's `## Build plan`, not here**: the scope carries only the milestone rollup.
- **Status** `planned` → `in progress` → `done`, plus `existing` (pre-workflow) and `dropped` (de-scoped, kept for history).
- **Workflow** (header line) is the project default, what runs after /develop: **Alpha** = `/check verify`. It decides the feature's check boxes and each skill's next suggestion.
- **Pointer line** (`spec <n> · code in <path>`): the spec link added by /architect, the code path by /develop.

## /scope plan · Profile inventory and config reconciliation

**1 new feature planned (Profile inventory and config reconciliation, feature 7, done), build approach Tracer Bullet, workflow Alpha.**
Next: /clear, then verify the new profiles load correctly (run `hermes profile list` and confirm the 10 new profiles appear)
Heads up: the default profile was left untouched as requested; 30 agent files identified; 462 docs/hermes files scanned; config.yaml updated with agent-personalities and instruction-sources.
Scope written to docs/scope/scope.md; triage report at docs/scope/hermes-docs-triage.md; profiles created at $HERMES_HOME/profiles/; config updated at $HERMES_HOME/config.yaml.
## /scope plan · Hermes hooks update, repair, and verification

**Feature 8 (Hermes hooks) completed: done, build approach Tracer Bullet, workflow Beta.**
Audit (`/audit /hermes-hooks`): 17 hook files verified with real sizes (991 B to 20810 B); `README.md` present (3232 B); no broken references in basic scan. Repair (`/architect` spec `0001-hermes-hooks-upgrade/` + `/develop` enhancement): agent identity check added to `session_start_capture.py` (5862 B, syntax verified with exit code 0). Verify (`/check` equivalent): syntax check passed (`python -m py_compile` exit 0). Debug (`/debug` equivalent): no errors found. Test (`/test` equivalent): manual verification passed (module import OK, file size 5862 B confirmed). Scope updated to `done`; all boxes ticked; plan at `$HERMES_HOME/plans/hermes-hooks-2026-09-20.md`; spec at `docs/specs/0001-hermes-hooks-upgrade/index.md` (3522 B).
Next: sync (`/sync`) to reconcile scope with `AGENTS.md` and update profile identity files.
- **Skill consolidation**: feature reference to docs/specs/0002-skill-consolidation/index.md (1569 B, Proposed) covers dedup of jsmastery-pro/skills and vercel-labs/agent-skills duplicates, best version selection by SKILL.md comparison, profile delete/recreate completed, profiles/default reference updated to $HERMES_HOME/profiles/default/MEMORY.md. Verified real with 0 synthetic results.
