---
name: dispatching-parallel-agents
title: "Dispatching Parallel Agents"
description: "Dispatch batched work to Hermes delegate_task subagents for parallel independent workstreams. Covers batch strategy, context injection, concurrent limits, collection, and verification."
version: 2.0.0
author: Hermes Agent
license: MIT
tags: [parallel, agents, orchestration, workflow, delegation, batching]
---

# Dispatching Parallel Agents

Dispatch work to Hermes `delegate_task` subagents in parallel batches. Use when you have N independent work items that each need web research, analysis, report writing, or any task with no shared mutable state.

**Core principle:** Parallelism wins when tasks share no data. Batch + inject everything in context — never make subagents read plans or configs.

## When to Use

- N independent research items (multi-project web research)
- N independent file updates (update N reports, fix N configs)
- N independent code-generation tasks (scaffold N components)
- Any workload where items don't share state or write to the same files

**Not for:** Tasks that modify the same file (race condition), share a database, or need sequential ordering.

## The Dispatch Pattern

### Step 1: Know Your Limits

Hermes caps concurrent `delegate_task` subagents per user:
- **Max concurrent:** 3 (configurable via `delegation.max_concurrent_children`)
- **Max spawn depth:** 2 (`orchestrator` role can dispatch 1 more level)

Drain a batch before dispatching the next one. Subagents run in the background — you don't poll; results arrive as new messages automatically.

### Step 2: Batch Your Work

Divide N items into batches of ≤3. Each batch = up to 3 `delegate_task` calls in the same turn.

```
N items ÷ 3 per batch = ceil(N/3) rounds
Example: 16 projects → 6 rounds of 3, 3, 3, 3, 3, 1
```

### Step 3: Inject Everything in Context

**Critical rule:** Subagents have no memory of your conversation and cannot read your loaded skills or plan files. Provide EVERYTHING they need inline in the `context` parameter:

```python
delegate_task(
    goal="Research <project> — web search for best practices, similar projects, guides",
    context="""
    PROJECT: <name>
    TECH STACK: <framework>, <db>, <services>
    
    QUERY IDEAS:
    - <topic 1> best practices 2026
    - <topic 2> integration patterns
    - <topic 3> security hardening

    TASK:
    1. Run 3-4 web searches
    2. Extract useful content from top results
    3. Return structured findings with URLs

    TARGET REPORT PATH: <absolute path>
    """,
    toolsets=["web", "file", "terminal"]
)
```

**Don't make subagents:** read plan files, read project READMEs, infer tech stacks, or load skills. Put it all in context.

### Step 4: Dispatch Entire Batch in One Turn

Fire all 3 `delegate_task` calls in the same assistant response. They run concurrently. Each returns independently as a new message.

```python
# Batch 1 — 3 projects
delegate_task(goal="research A", context="...", toolsets=["web","file"])
delegate_task(goal="research B", context="...", toolsets=["web","file"])
delegate_task(goal="research C", context="...", toolsets=["web","file"])

# Wait for batch 1 results to arrive as messages
# Then dispatch batch 2
```

### Step 5: Collect and Process

Subagent results appear as messages in the conversation automatically. Each contains the structured findings the subagent produced.

**Do NOT:**
- Poll or wait after dispatch — just continue other work
- Process results manually in the controller (context pollution)
- Dispatch next batch before previous batch's results arrive

### Step 6: Verify Outputs Exist

Subagents self-report their work, but always verify artifacts on disk before claiming completion:

```python
# Verify file exists
terminal("wc -c projects/X/RESEARCH_REPORT.md")
# Confirm content has expected sections
terminal("grep -c '^## ' projects/X/RESEARCH_REPORT.md")
```

## Batch Strategies by Workload Size

| Size | Strategy | Rounds |
|------|----------|--------|
| 1-3 items | Single batch, dispatch all | 1 |
| 4-12 items | Multiple batches of 3 | 2-4 |
| 13-48 items | Batches of 3, track via todo | 5-16 |
| 49+ items | Consider cron job or script instead | — |

For 13+ items, maintain a `todo` list tracking which batch is in progress and which remain.

## Context Injection Template

Use this structure for each subagent:

```
PROJECT: <name>
TECH STACK: <key technologies>

QUERY IDEAS:
- <search query 1>
- <search query 2>
- <search query 3>

TASK:
1. Run 3 search queries via web_search
2. Extract top 2-3 results per query via web_extract
3. Return structured markdown with: key findings, URLs, cheatsheets, best practices, pitfalls

TARGET REPORT PATH: <absolute path>
```

## Toolsets Per Task Type

| Task Type | toolsets |
|-----------|----------|
| Web research | `["web", "file", "terminal"]` |
| Code generation | `["terminal", "file"]` |
| File analysis | `["file", "terminal"]` |
| Report writing | `["file"]` |

## Propagation Pattern (identical content → N sibling files)

When the goal is to push the SAME block (a config snippet, a memory section, a rule) into N sibling files — e.g., syncing a memory section across all profile `MEMORY.md` files, or a setting into N `.vscode/settings.json` files — the batch strategy differs from independent research:

- **Inject the EXACT verbatim content** into every subagent's `context`. Children share no state, so without the literal text each one paraphrases and you get N inconsistent files. Paste the block, don't describe it.
- **Give each child its absolute target path** plus a precise edit instruction (append after a blank line; never delete existing content).
- **Add a verification instruction:** the child must confirm the target file now contains a known anchor line (e.g., a section heading) and report the final char count.
- **Keep toolsets minimal:** `file` only for pure file edits (no terminal/web needed) — fewer tools, less misbehavior.
- **Drain in batches of ≤3** (default concurrency cap). 6 targets → 2 rounds of 3.

This reuses the same dispatch mechanics; the only difference from research fan-out is the context payload is identical content + per-target path instead of per-item queries.

## Pitfalls

- **Context starvation.** The #1 failure mode. Subagents that don't know the project name, tech stack, or task structure produce useless output. Over-inject context.
- **Race conditions on shared files.** Never dispatch two subagents that write to the same file. Use independent target paths or serialize.
- **Subagent hallucination.** Subagents claim success but files don't exist. Always verify artifact paths with `ls` before advancing.
- **Too-large batches.** Dispatching 6 calls to beat the limit doesn't work — the extra calls are silently dropped. Respect the concurrency cap.
- **Orchestrator skill collision.** When this skill is loaded alongside `subagent-driven-development`, they overlap. Use this skill for pure parallel dispatch (independent items); use subagent-driven-development for the per-task implement → spec-review → quality-review pipeline (serial within task).
- **Subagent language contamination.** If the user's conversation is in a non-English language, add an explicit language instruction in context: `"Respond in Japanese"`, `"Return output in French"`. Subagents default to English.
- **Don't re-dispatch after partial results.** Wait for all subagents in a batch to complete before starting the next batch. Partial batch results create inconsistent state.
- **Delegation IDs are not process IDs.** The `delegation_id` returned by `delegate_task` cannot be passed to `process(action='wait'|'poll')` — that tool tracks terminal sessions only and returns `not_found`. Subagent completion is signaled by async messages that re-enter the conversation automatically; you cannot (and must not) wait on a delegation handle. Enforce the concurrency cap by draining batches of ≤3, not by polling.
- **Inject the EXACT file list, not just a count.** When fanning out file work, paste the literal list of target filenames/paths into each subagent's `context`. An under-injected list (e.g. "70 files" with only 29 paths, or a truncated slice) causes the subagent to analyze a subset — observed: a batch analyzed 27 of 70, missing 2 files entirely ("slice discrepancy"). Always enumerate the full disjoint file set per batch and verify the subagent's analyzed count matches the slice size. For large slices, have the child read a written file list (e.g. `/tmp/slice.json`) rather than embedding inline.
- **Stalled batches are a real failure mode, not just slowness.** A background fan-out can produce ZERO output far past its expected duration (observed: 0/32 deliverables after 20+ min for small repos that should finish in ~4). The "don't poll" rule assumes completion signals arrive — a silently-stalled batch never signals, so indefinite waiting is wrong. Recovery: if a batch has produced no deliverables well past expected time, RE-DISPATCH with tighter context rather than keep waiting. Common stall causes: an unnecessary `web` toolset on a local-only task (drop it — web calls burn the budget), referenced slice/helper files that don't exist (create them first or state the explicit derivation scheme, e.g. "slice N = entries [100*(N-1):100*N] of the master list"), and MSYS/Windows path mismatches (subagents on Windows need `git -C <dir>` or `/c/Users/...`, not bare `C:\...`); verify with `find` because `search_files` may lag on freshly written files. The re-dispatched run supersedes the dead one.
- **Git contributor-stats quirk.** `git shortlog -sn` returns EMPTY in some repos (author identity not collapsed). Use `git log --format="%an <%ae>"` (or `git shortlog -sne`) for contributor counts. Do NOT report "no contributors" from an empty `shortlog -sn`.
- **Destructive ops hit a runtime approval gate the subagent CANNOT self-grant.** Commands like `git branch -D`, `git push --delete`, `git reset --hard`, `rm -rf`, or `gh repo edit --default-branch` are intercepted by the host safety guard and require an interactive human approval click. A subagent cannot click it, so the command sits in "pending approval" inside its session and never runs — and when the batch ends, the queued command is lost. Observed: a repo-management Phase-1 fan-out "completed" but the branch-delete / default-branch-flip never actually executed; only the GitHub-side push that had ALREADY gone through stuck. RECOVERY: when a subagent reports a destructive step "pending approval" / "blocked," do NOT re-dispatch blindly (hammering the guard won't help). Surface it to the user as an explicit approval request with the exact command + impact, and run it yourself in the parent terminal (where the approval prompt surfaces to the user) if they consent. Record pre-state (`git branch -a`, `gh repo view --json defaultBranch`, target file mtimes) BEFORE any destructive step so rollback is possible.
- **Windows bash heredoc mangles Python regex.** Passing a Python script via a `terminal` heredoc (`python - << 'PY' ... PY`) double-escapes backslashes, so `r"\*\*(...)\*\*"` arrives as `\\*\\*(...)\\*\\*` and regexes silently fail to match. This burned a 16-row index build (0 of 16 tech-stack cells extracted) until rewritten as a standalone `.py` file run via `python file.py`. RULE: for any Python with regex/special chars, WRITE the script to a `.py` file (write_file) and run `python path.py` — never inline it through a bash heredoc. Also: prefer `git -C <dir>` / MSYS paths (`/c/Users/...`) over bare `C:\...` in subagent contexts.

## Verification Checklist

- [ ] Max concurrent dispatched (≤3 per user limit)
- [ ] Every subagent has complete context (name, stack, queries, path)
- [ ] No two subagents write to the same file
- [ ] Results verified on disk (not just subagent self-report)
- [ ] Batch results collected before dispatching next batch
