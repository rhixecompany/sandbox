# Dev Imp (Development Implementation Manager) Pattern

## What It Is

A multi-phase execution workflow for running generator prompts against target projects with strict sequential gates. Each phase completes fully before the next begins — no overlap, no shortcuts.

## When to Use

- You have a set of `.prompt.md` generator files (blueprint analysis, code scaffolding, etc.)
- You need to apply them across multiple target projects
- The workflow demands verification, code review, and debugging gates between generation and delivery
- You need a crisp summary report at the end

## Workflow Phases

```
discover generators → user selects subset → implement each sequentially
  → (only then) verify implementation status
  → (only then) code-review all changed files
  → (only then) debug and fix all issues
  → (only then) re-verify all fixes
  → (only then) generate implementation report
```

### Phase 1: Discover & Select
- List generator files matching `prompts/*-generator.prompt.md`
- Present to user for selection (numbers, ranges, or "all")
- Confirm selection before proceeding

### Phase 2: Implement (Sequential per Generator)
- Read each generator prompt fully
- Determine target project context
- Execute against each target (can parallelize targets within a generator)
- Collect results and errors
- **Must wait for each generator to complete before starting the next**

### Phase 3: Verify (After All Generators)
- Check expected files exist
- Check expected modifications applied
- Build/compile the project(s)
- Run test suite
- Report gaps or failures

### Phase 4: Code Review (After Verification Passes)
- Read every file changed by generators
- Check: correctness, style, edge cases, security, dependencies
- Classify findings: Critical, Important, Minor

### Phase 5: Debug & Fix (After Review)
- Root-cause each Critical/Important issue
- Apply fix and verify it resolved the issue
- Re-run tests after all fixes
- Zero Critical/Important issues = gate passed

### Phase 6: Report (After All Fixes Verified)
- Generate `dev-imp-report.md` at workspace root
- "Crispy" format: compact tables, emoji status indicators, scannable pass/fail

## Strict Sequential Rule

The phrase **"only then"** is non-negotiable. Phases cannot overlap, run in parallel, or start before the prior phase is verified complete. This prevents half-reviewed code from entering the verification stage and keeps the report accurate.

## Adaptation Patterns

| Scenario | Handling |
|----------|----------|
| No generators exist | Report "No generators available", skip to Phase 6 with partial report |
| Generator fails mid-run | Log error, mark as ❌, continue to next generator |
| Zero generators selected | Confirm intent, skip to Phase 6 |
| Target project doesn't exist | Scaffold minimal structure before running generator |
| Code review finds no issues | Skip Phase 5, go directly to Phase 6 |
| Build/tests fail post-fix | Loop back to Phase 5 until passing or escalate |
| No git repo | `git init` before first generator run to enable change tracking |

## Report Style ("Crispy")

- Compact tables for structured data
- Emoji indicators: ✅ ❌ ⚠️ ➕ 📝
- No prose paragraphs where bullets suffice
- Total under 80 lines typical
- Clear pass/fail at a glance

## Pitfalls

- **Generator sprawl**: 19 generators × 18 targets = 342 runs. Batch within each generator to avoid combinatorial explosion.
- **Sequential vs parallel within a generator**: Generators run sequentially (per phase spec), but targets can be parallelized inside a single generator via delegate_task subagents.
- **Context overload**: Subagents processing many targets need concise, focused context — don't dump full generator prompts + 18 project trees. Provide the generator's core instruction + the target list.
- **No progress reporting**: The user sees nothing while subagents churn. Send intermediate status updates after each generator completes.

## Subagent Execution Patterns

### Multi-Target Subagent Dispatch

When a single generator must run against N targets (e.g. 18), do NOT dispatch one subagent for all N. Single subagents handling 18+ targets stall due to tool-call limits and context window exhaustion.

**Preferred pattern:** Split targets into batches of 5-6 per subagent:

```
# BAD — single subagent for 18 targets
delegate_task(goal="run generator against all 18 targets")  # ← stalls mid-way

# GOOD — 3 subagents with 6 targets each
delegate_task(goal="run generator against targets 1-6")
delegate_task(goal="run generator against targets 7-12")
delegate_task(goal="run generator against targets 13-18")
```

**When generators must run sequentially** (per strict gates): dispatch each generator as a batch of subagents (one per target group), then verify ALL completed before proceeding to next generator.

### Progress Verification via Filesystem

Subagent self-reports can over-state completion. Always verify via filesystem:

```bash
# After dispatching subagent for generator Foo producing output type Bar
find ~/SandBox -name "Bar.md" -type f | wc -l
# Compare against expected target count
```

This catches:
- Subagents that claim completion but actually stalled
- Subagents that hit tool-call limits before processing all targets
- Filesystem-level divergence from subagent's internal tracking

### Stalled Subagent Recovery

When a subagent produces M < N outputs and stops responding:

1. Check filesystem for actual output count (see above)
2. Identify which targets are missing outputs (iterate through target list)
3. Dispatch a new subagent with just the remaining targets
4. Accept that the straggler subagent may race with the new one on some files
5. Verify final count after both complete

```bash
# Check which targets are missing
for dir in target1 target2 target3; do
  f="./$dir/docs/Arch/Foo.md"
  [ -f "$f" ] && echo "✅ $dir" || echo "⏳ $dir"
done
```

### Sibling Agent Race Conditions

When two subagents write to the same file path, you may get an overwrite warning. This is safe for idempotent generator outputs (docs that are overwritten with similar content) but risky for stateful files. Handle by:

- **For idempotent outputs (doc generation):** Accept the race — the last write wins, and content is similar enough
- **For stateful files:** Sequence subagents by target group to avoid overlap
- **Detection:** Look for `_warning: "was modified by sibling subagent"` in write_file results

### Standing-Goal Subagent Chaining

Under `[Continuing toward your standing goal]` continuation, do not passively wait for subagent completion messages. Instead:

1. Dispatch subagent for current generator
2. Actively poll filesystem every 30-60s for output files
3. When progress stalls (no new files in 90s), handle as stalled recovery
4. When all targets confirmed via filesystem, dispatch next generator
5. Report progress concisely at each transition

This prevents the workflow from stalling on a single hung subagent under the standing-goal pattern where the user expects continuous forward progress.
