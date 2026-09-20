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