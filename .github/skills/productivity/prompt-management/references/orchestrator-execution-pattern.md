# Orchestrator Execution Pattern

Run multiple prompts sequentially as a pipeline, with "only then" constraints between each step. Each prompt executes to full completion before the next begins.

## When to Use

- You have 3+ prompts that form a pipeline or dependency chain
- Each prompt produces artifacts that later prompts consume
- The workflow enforces a strict sequential constraint ("only then")

## Structure

```
prompts/
  execute-all-prompts.prompt.md    # Orchestrator (entry point)
  phase-1-foo.prompt.md
  phase-2-bar.prompt.md
  phase-3-baz.prompt.md

templates/
  execute-all-prompts/
    phases.md                      # Detailed phase definitions

docs/
  orchestrator-progress.md         # Live status tracker
  orchestrator-verification.md     # Final verification artifact
```

## Orchestrator Prompt Anatomy

### Frontmatter
```yaml
name: execute-all-prompts
title: Execute All Prompts Orchestrator
trigger: /execute-all-prompts
dependencies:
  - skill:using-superpowers
  - skill:plans-and-specs
  - skill:executing-plans
  - skill:verification-before-completion
```

### Body sections

1. **Description** — State the strict sequential constraint explicitly. "Phase N+1 begins only after Phase N is fully verified complete."
2. **Skills Required** — Minimal: only the skills needed across ALL phases (`using-superpowers`, `plans-and-specs`, `executing-plans`, `verification-before-completion`).
3. **Rules** — Must include: strict sequential, phase integrity, verification gates, progress tracking, no reordering.
4. **Phases** — Reference a `templates/execute-all-prompts/phases.md` for detailed steps. Keep the orchestrator lean.
5. **Verification Checklist (Orchestrator Level)** — One checkbox per phase: "[ ] Phase N complete". Not a repeat of each sub-phase's checklist.
6. **Progress & Verification Artifacts** — Two docs tracked throughout:
   - `docs/orchestrator-progress.md` — Updated after each phase completes (status, duration, key results).
   - `docs/orchestrator-verification.md` — Final comprehensive report (prepped as template before execution, filled after all phases).

## Phase Template Design

Each sub-prompt's detailed phases go in its own template directory:

```
templates/phase-1-foo/
  phases.md                    # Single file with all phases
  -- or --
  phase_0_setup.md             # Individual phase files
  phase_1_analysis.md
  phase_2_execution.md
  README.md                    # Explains the layout convention
```

The orchestrator **must verify** which layout each sub-prompt uses before dispatching. Check with `ls templates/<sub-prompt>/`.

## Pre-Flight: Check Prior Session Completion

Before dispatching any phase, check whether a prior session already completed it:

```bash
# Check for Phase 1 completion artifacts
ls -la docs/final-verification.md 2>/dev/null
ls -la judge_results/all_results.tsv 2>/dev/null
```

If artifacts exist (dated before the current session), read the verification report to confirm full completion. If verified, **do not re-run** — mark Phase complete and proceed to the next. Only dispatch if the phase was never run or the artifacts are stale.

**Important:** The orchestrator-progress.md artifact in the workspace root may reflect a different session's orchestrator run. Always check sub-phase output artifacts (`docs/*.md`, `judge_results/`, etc.) for date-stamped proof of completion before deciding to re-run.

## Execution Flow

### Mode 1: Delegated (standalone prompts)

```python
# Dispatch ONE phase prompt at a time (strict sequential)
delegate_task(
    goal="Execute Phase N prompt fully",
    context=f"...Full context including prompt file path, templates, current state...",
    toolsets=["terminal", "file", "web", "skills"]
)
# Wait for result before dispatching Phase N+1
```

Each phase prompt is delegated as its own `delegate_task` call. The orchestrator agent:
1. **Check prior completion** — Look for signature output artifacts (verification reports, final reports) from the target phase. Check file dates.
2. Reads the sub-prompt file and its template(s) — only if dispatch is needed
3. Packages the full context (current state, artifact paths)
4. Spawns sub-agent
5. On completion, reads `docs/orchestrator-progress.md`, appends the result
6. Verifies the phase's checklist before dispatching the next

### Mode 2: Direct (sequential pipelines)

For strictly sequential multi-prompt pipelines, execute directly in the main agent. Sub-agents can silently stall for long-running chains and never return results.

```python
# Execute each phase directly, tracking progress
for phase in [phase1, phase2, phase3, phase4]:
    # 1. Read prompt + template files
    # 2. Execute all sub-phases sequentially
    # 3. Verify phase completion checklist
    # 4. Update docs/orchestrator-progress.md
    # 5. Only then proceed to next phase
```

**When to use direct vs delegated:**
- **Delegated:** Standalone prompts, independent research tasks, parallelizable work
- **Direct:** 3+ prompts chained with "only then" constraints, prompts where sub-agents have historically stalled, pipelines with shared progress-file tracking

## Progress File Management

To prevent sub-agent vs main agent contention on `docs/orchestrator-progress.md`:

- **Orchestrator** writes the **orchestrator-level summary** (which phases are complete, key results per phase, pipeline table)
- **Sub-agents** write to their own deterministic file: `docs/{entity}-progress.md`
- After a sub-agent completes: read its progress file, extract the phase result, then update the orchestrator-level summary
- Always `read_file` before `write_file` on the shared progress doc if both entities may touch it

## Verification Checklist (Orchestrator Level)

```
- [ ] Phase 1: complete — all sub-phases verified
- [ ] Phase 2: complete — all sub-phases verified
- [ ] Phase 3: complete — all sub-phases verified
- [ ] Phase 4: complete — all sub-phases verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`
```

## Pitfalls

- **Template structure mismatch** — Sub-prompts may use a single `phases.md` OR individual `phase_X.md` files. Always `ls templates/<sub-prompt>/` to confirm, rather than assuming a single file.
- **Sub-agent limits** — Each phase prompt is independent; use separate `delegate_task` calls so each gets its own context budget. A single monolithic sub-agent for all 4 phases risks hitting context limits. For sequential pipelines, prefer direct execution.
- **Progress doc contention** — Sub-agents write to `docs/orchestrator-progress.md` with their own format, overwriting the orchestrator's tracking. Use append-only convention or deterministic per-entity filenames. After sub-agent completes, always read back and reformat.
- **Missing template** — Not all sub-prompts have their template files under the expected path. Before dispatching, verify ALL referenced template paths exist.
- **Sub-agent not guaranteed to return** — `delegate_task` says "result re-enters the conversation as its own new message when it finishes", but sub-agents for long-running (5+ min) or multi-phase prompts may never deliver a result. **Mitigation:** Always check for signature output artifacts (verification reports, doc files, TSV results) on disk after a reasonable wait (2-5 min). If artifacts exist with timestamps after dispatch, verify them and proceed — even without the delegation result message. Never block indefinitely waiting for a sub-agent result.
- **Prior session work detection must check file dates** — A verification report from 3 days ago is valid completion evidence. Check both existence AND date of signature artifacts. Only re-run if artifacts are missing, clearly incomplete, or the user explicitly requests a re-run.
- **Direct execution can't be interrupted mid-phase** — When running directly, a phase that takes 10+ minutes occupies the main agent. If you need to context-switch, delegate independent sub-phases and keep only the sequential gating in the main agent.
