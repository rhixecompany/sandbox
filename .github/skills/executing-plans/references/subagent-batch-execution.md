# Subagent Batch Execution Patterns

## When to Use

When executing a multi-target operation where each unit of work is dispatched to a `delegate_task` subagent. This covers generator-prompt execution, blueprint generation across N repos, and any batch where a single workflow must run against many independent targets.

## Generator-Prompt Execution Pattern

A generator prompt (`.prompt.md` file with YAML frontmatter and phases) defines a self-contained class of work. Running it across multiple targets follows a strict sequential-per-generator, parallel-within-generator approach:

```
FOR EACH generator (strictly sequential):
  1. Read generator prompt in full
  2. Dispatch ONE subagent (delegate_task) with:
     - goal: "Run <generator> against all N targets"
     - context: Full generator prompt + target list + output path convention
     - toolsets: [terminal, file]
  3. WAIT for subagent to complete (do NOT proceed to next generator)
  4. VERIFY output files exist on disk for all N targets
  5. ONLY THEN proceed to next generator
```

### Key Constraints

- **Generators are sequential**: never dispatch Gen N+1 until Gen N has produced output for all targets
- **Targets within a generator CAN be parallel**: the subagent handles ordering internally
- **Subagents are leaf workers**: they cannot delegate further (role='leaf'), keeping the execution tree shallow

## Subagent Stall Detection & Recovery

Subagents processing 10+ targets may stall or complete only partially. Detect and recover via filesystem monitoring:

### Detection

Do NOT wait for the delegate_task result message alone. Instead, periodically check output files on disk:

```bash
# Check how many targets the subagent has completed
find <workspace> -path "*/docs/Project_Architecture/<output-file>" -type f | wc -l

# Check specific remaining targets
for dir in <remaining-targets>; do
  [ -f "$dir/<output-file>" ] && echo "DONE $dir" || echo "PENDING $dir"
done
```

### Recovery (When Subagent Stalls)

When a subagent produces output for only M of N targets and stops making progress:

1. **Verify** — confirm output files are actually on disk and non-empty
2. **Identify remaining** — build the list of targets without output
3. **Choose recovery strategy** — pick based on how many targets remain and how complex they are:
   - **≤2 remaining, simple output**: handle inline — create the output file yourself using what you know from similar completed targets. This is faster than dispatching and waiting on another subagent.
   - **>2 remaining or complex targets**: re-dispatch — new delegate_task with goal="Complete remaining targets for <generator>" and context listing only the remaining targets and their paths.
   - **Docs-only / no-code target**: if the stuck target has no code to analyze (e.g., a docs-only project), write a minimal output file directly rather than dispatching.
4. **Do NOT restart from scratch** — the first subagent's work is valid; only complete what's missing
5. **Continue waiting or verifying** — the Gen-level sequential gate applies across all recovery attempts

### When to Use Inline Fallback

Use inline handling (not re-dispatch) when ALL of these are true:
- Only 1-2 targets remain stuck
- The expected output format is known from other completed targets
- The stuck target is simple (documentation-only, minimal code, or well-understood structure)
- Creating the file directly takes less than 30 seconds

**Pitfall**: Don't guess at complex architecture for a stuck target — if you can't confidently produce the output from what you already know, re-dispatch instead.

### Root Cause

Subagents stall most often because:
- A single target's project inspection timed out (large directory, missing permissions)
- The subagent hit a tool limit (max 50 tool calls per execute_code, 5-min timeout)
- The target project had a structure the agent couldn't classify, causing indecision

The fix is not to increase limits — it's to dispatch smaller batches or retry the subset that failed.

## Progress Tracking via Filesystem

When running N subagents across a multi-gen workflow, track progress via filesystem artifacts rather than waiting for subagent messages:

| Check | Command |
|-------|---------|
| Gen-level count | `find . -name "<output-file>" -type d \| wc -l` |
| Per-gen diff since last check | `find . -name "<output-file>" -newer <timestamp-ref> -type f` |
| Per-target check | test existence per target path |

This avoids two problems:
- Subagent result messages may arrive after you've already checked and moved on
- A subagent may finish silently (tool limit, error, edge case) without delivering a result message

## Phase Artifacts for Multi-Gen Workflows

For a workflow with K generators × N targets, track progress at the generator level:

```
.hermes/plans/<workflow-name>-progress.md
```

Content:
```markdown
# Workflow Progress: <name>

| Gen | Generator | N targets | Status |
|-----|-----------|-----------|--------|
| 1 | architecture-blueprint | 18 | ✅ complete |
| 2 | folder-structure-blueprint | 18 | 🔄 running |
| 3 | ... | 18 | ⏳ queued |

## Current Gen Details
Gen 2: 12/18 targets complete. Remaining:
- project-A
- project-B
```

## Pitfalls

| Pitfall | Mitigation |
|---------|------------|
| Dispatching Gen N+1 before Gen N output verified | Always check filesystem before dispatching next gen |
| Subagent completes but result message lost | Check filesystem — if output files exist, gen is done |
| Subagent stalls silently on one problematic target | Periodically check filesystem count; re-dispatch remaining |
| Re-dispatching already-completed targets | Only include pending targets in the re-dispatch context |
| Overloading a single subagent with 15+ targets | Split into batches of 5-10 per subagent for reliability |
| **Sibling subagent file race**: two subagents modify the same file; the `write_file` warning `"was modified by sibling subagent '<id>' but this agent never read it"` means your write may have overwritten the sibling's changes | Before manual write to a file a subagent may also be targeting, read it first with `read_file` — if a sibling subagent message confirms it already wrote the file, skip your write. If you do overwrite, verify the final content is what you intended. |
