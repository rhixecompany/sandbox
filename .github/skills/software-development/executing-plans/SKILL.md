---
name: executing-plans
title: "Executing Plans"
description: "Use when executing written implementation plans in separate sessions with review checkpoints. Guides multi-phase work with structured verification."
version: 1.0.0
author: Alexa
license: MIT
tags: [cross-platform, shell-scripting, remediation, batch-processing, verification]
---
## Goal
Use when executing written implementation plans in separate sessions with review checkpoints. Guides multi-phase work with structured verification.



## Description


Execute implementation plans in separate sessions with review checkpoints. Guides completion of multi-phase work with structured verification at each stage.

## When to Use

- Executing written implementation plans
- Multi-phase projects with checkpoints
- Work requiring review between phases
- Complex implementations needing verification
- Team-based implementation work
- Projects with clear milestones
- **Batch execution of multiple implementation plans**
- **Folder-based plan execution (all plans in a directory)**

## When NOT to Use

- Simple single-phase tasks
- Real-time collaborative work
- Tasks without clear plan
- Exploratory or experimental work

## Workflow

### Phase -1: Batch Discovery (Batch/Folder Modes Only)

**Entry check:** If `.hermes/plans/batch-execute-discovery.md` exists → skip to Phase 0.

1. **Discover targets** — Resolve plan file list from:
   - `--batch plan1.md plan2.md ...` explicit file arguments
   - `--folder .hermes/plans/` recursive scan for `*.md` files
   - `--pattern "*.md"` filter by glob pattern
   - `--status pending|in-progress` filter by plan status
2. **Validate targets** — Filter existing files, validate plan structure
3. **Write discovery artifact** → `.hermes/plans/batch-execute-discovery.md` with plan list and execution order

### Phase 0: Verify Live Inventory First (NEW — Critical)

**Entry check**: Before executing ANY plan, verify the live system state matches the plan's assumptions. Do not trust plan artifacts alone — they may be stale.

- Run inventory commands to capture current state:
  - `hermes hooks list` → verify hook registration & approval status
  - `hermes plugins list` → verify enabled/disabled plugins
  - `hermes mcp list` → verify MCP servers & tool discovery
  - `hermes skills audit` → verify skill health & blocking findings
  - `search_files` / `read_file` → verify file artifacts exist on disk
- Capture outputs to verification artifacts (e.g., `.hermes/plans/verification/*.txt`)
- Compare live state vs. plan assumptions — document discrepancies
- **Only proceed when inventory is verified** or discrepancies are explicitly accepted as known risks

**Rationale**: This session discovered that the master plan claimed "hooks not registered" while `hermes hooks list` showed 4 active hooks. Without Phase 0, execution would have "fixed" a non-issue. Live inventory is the source of truth; plan artifacts are hypotheses.

### Phase 1: Prepare Plan

**Entry check**: Verify the plan document exists and is readable. If no plan artifact is found, halt — cannot execute without a plan.

- Review implementation plan thoroughly
- Verify all requirements are clear
- Set up execution environment
- Identify review checkpoints
- Determine batch size for file-heavy plans (default: ≤7 files per batch)

**Batch mode:** Prepare all target plans in parallel. Use `execute_code` to load and validate all plans simultaneously. Create a combined execution order based on dependencies and priority.

### Phase 2: Execute Phase 1

**Entry check**: If the phase artifact (e.g., `docs/{task}-progress.md`) exists with a completion marker, skip this phase.

- Implement first phase — for file-heavy plans, process in batches of ≤7 files
- After each batch, verify changes are correct before proceeding
- Run tests and verification
- Document progress in the phase artifact
- Append batch results to a progress log (never overwrite)

### Phase 3: Review & Checkpoint

**Entry check**: If checkpoint approval was already logged in the artifact, skip this phase.

- Review phase 1 results against the plan
- Verify against requirements
- Get approval to proceed (or auto-approve if no decision needed)
- Document decisions
- Update the plan if new information was discovered

**User preference — auto-advance**: When the user provides all phases/tasks/subtasks upfront in a single request, do NOT pause after each phase to ask "continue?" or "ready for the next phase?" Execute all phases end-to-end without intermediate confirmation. The user already committed to the full scope — honor that commitment. Only pause if a phase fails critically (blocking error) or if the user explicitly asks for a checkpoint.

### Approval Gates for Destructive Changes (NEW)

When a plan step performs destructive or irreversible actions (skill deletion, config edits, MCP server changes, bulk plugin enable/disable, file/directory deletion), enforce an explicit approval gate **before** execution:

1. **Create approval request** at `.hermes/approvals/<timestamp>_<short-title>.md` with:
   - Requestor, Owner(s), Scope (files/skills/hooks/plugins/MCP servers changed)
   - Justification, Rollback plan (exact git/skill_manage commands), Verification steps
   - Explicit `+1` from each Owner, Approval valid until (ISO date)
2. **Wait for recorded approval** — do not proceed on mental/verbal consent
3. **Execute with traceability** — include approval filename in commit message
4. **Post-change verification** — run verification steps, append outputs to approval file
5. **Rollback on failure** — execute rollback plan, document remediation

**Source**: Master plan Section 9 pattern (2026-06-16 unified-ecosystem-master-plan.md)

### Phase 4: Execute Remaining Phases — Batch Processing

**Entry check**: Check which phases/batches are already complete via artifact scanning. Skip completed items.

- Implement subsequent phases in priority order
- Process each phase using the same batch-of-≤7 pattern
- Review after each phase
- Adjust plan if needed based on discoveries
- For each completed item, mark it as `[x]` in the plan
- On failure: log the failure with reason and continue — do not halt (unless the failure invalidates the approach)
- Finalize and run full verification

**Batch mode:** Execute multiple plans in parallel using `delegate_task` subagents. Each subagent handles one plan through all its phases. Use `delegate_task` with toolsets `['terminal', 'file', 'skills', 'delegation']` and `role: 'leaf'`. Aggregate progress to `.hermes/plans/batch-execution-progress.md`.

## Tools & References

- **Related Skills**: writing-plans, verification-before-completion
- **Plan Format**: Markdown with clear phases
- **Checkpoints**: Defined review points
- **References**:
  - `references/codebase-remediation-patterns.md` — concrete standardization patterns (shebangs, shellcheck, TypeScript fs.promises, JSDoc cleanup) captured from a cross-project script audit session
  - `references/cross-scope-script-remediation.md` — reusable execution pattern for multi-repo shell/PowerShell/BAT/TypeScript remediation with append-only logs and phase gates
  - `references/inventory-verification-pattern.md` — Phase 0 live inventory verification before plan execution (hermes hooks/plugins/mcp/skills audit)
  - `references/orchestrator-prompt-pattern.md` — Pattern for creating orchestrator prompts that sequentially execute multiple prompts/plans
  - `references/approval-gate-pattern.md` — Governance gate for destructive changes requiring explicit recorded approval
  - `references/subagent-batch-execution.md` — Multi-target generator execution via delegate_task, subagent stall detection & recovery, filesystem-based progress tracking

## Core Techniques

### Batch Processing

When a plan touches many files, process them in fixed-size groups to manage context limits:

- **Batch size**: ≤7 files per batch. Use fewer if the remaining set is smaller.
- **Priority order**: Process batches by priority — Critical before Major before Minor, Bug before Feature before Cleanup.
- **Batch 1 as proof-of-concept**: Verify first batch quality before proceeding further.
- **Failure tolerance**: Log batch failures with reasons and continue — never halt mid-plan unless the failure invalidates the approach entirely.

**Rationale**: Batches keep each tool invocation focused. Re-reading 7 files is fast; re-reading 70 is not. Small batches make it feasible to verify every fix at reasonable cost.

### Patch-First Editing

Prefer the `patch` tool over `write_file` for surgical edits:

- Use `patch` with exact `old_string`/`new_string` context matching — read the file first with `read_file` to capture exact text.
- Include 2-3 lines of surrounding context to ensure uniqueness.
- Use `replace_all=true` only when the same exact pattern must change everywhere in a file.
- Reserve `write_file` for new files or complete document rewrites.
- Never use `sed`/`awk` in terminal for file editing — `patch` is safer, produces a diff, and auto-runs syntax checks.

**Rationale**: Patch edits are idempotent, produce a unified diff you can review, won't accidentally strip unrelated content, and auto-validate syntax after each change.

### Artifact-Driven Progress Tracking

Write markdown artifacts at each phase to create a durable, resumable record:

| Artifact | Purpose | Written by Phase |
|----------|---------|-----------------|
| `docs/{task}-list-context.md` | Inventory of what was found | Discovery |
| `docs/{task}-issues-context.md` | Issues identified | Audit |
| `docs/{task}.prompt.md` | Remediation plan | Planning |
| `docs/{task}-fix-issues-context.md` | Fix progress log with batch results | Execution |
| `docs/{task}-verification-report.md` | Final pass/fail per issue | Verification |

Key rules:
- Append batch results to progress logs — never overwrite.
- Use the presence/absence of completed artifacts as entry checks for resumability.
- The final summary line of each artifact acts as a completion marker.

### Bulk Sweeps at Scale

When a single pattern (or a small set of patterns) needs to be applied across 50+ files, file-by-file `patch` calls are impractical. Use a **bulk sweep** instead.

### When to Bulk Sweep

- Same exact pattern to replace across 50+ files (e.g., `@author Adminbot` → `@author Alexa`)
- Same line to delete in 50+ files (e.g., `Description placeholder`, `CreatedBy: convert-scripts`)
- Multiple patterns can be combined into one sweep pass

### Bulk Sweep via execute_code (Preferred)

Use a Python script in `execute_code` that operates on the native filesystem:

```python
from hermes_tools import search_files

# Step 1: Find all affected files (non-docs)
files = [f for f in search_files("@author Adminbot",
         output_mode="files_only", limit=250)["files"]
         if not f.startswith("docs/")]

# Step 2: Apply replacements file-by-file
import re
for path in files:
    with open(path, "r") as f:
        content = f.read()
    content = content.replace("@author Adminbot", "@author Alexa")
    content = re.sub(r"^\s*\*\s*Description placeholder\n?", "", content, flags=re.MULTILINE)
    with open(path, "w") as f:
        f.write(content)

# Step 3: Verify
remaining = search_files("@author Adminbot", output_mode="files_only")
print(f"Remaining: {len(remaining['files'])}")
```

This avoids `find | xargs sed` timeout issues and is fully reproducible.

### Bulk Sweep via Terminal (sed)

For simple string replacements where you already have the exact file list, `sed` via `terminal` works but may time out on very large trees. Use targeted `grep -rl` to feed only affected files:

```bash
grep -rl '@author Adminbot' --include='*.ts' --include='*.tsx' \
  --exclude-dir=node_modules --exclude-dir=.next --exclude-dir=.git \
  . | xargs sed -i 's/@author Adminbot/@author Alexa/g'
```

**Important**: `sed` commands that time out in the foreground may still complete — the OS buffers I/O and the replacement happens even if the tool reports a timeout. Always verify with `search_files` afterward.

**Script template**: `scripts/bulk-placeholder-sweep.py` (in this skill's directory) — a reusable template for bulk pattern replacement.

### Multi-Pattern Sweeps

Combine related patterns in a single pass to minimize tool calls:

| Step | Action |
|------|--------|
| 1 | Search all 3 patterns to get combined file list |
| 2 | Apply all replacements in one Python script |
| 3 | Verify all 3 patterns at once |

This is the pattern used to clear ~346 placeholders across 189 files in the live-codebase remediation session.

## Cross-Project Scope

When a plan spans multiple independent repositories or project directories:

- Group fixes by project, not by issue type — minimizes context switching.
- Document which projects were touched and what conventions were applied to each.
- Consider each project's existing conventions before standardizing (e.g., shebang style, shell dialect, lint rules).
- Prefer environment-variable–based paths (`$HOME`, `%USERPROFILE%`) over hardcoded absolute paths.
- Use project-local instruction files (AGENTS.md, README.md, CLAUDE.md) to discover per-project conventions.

## Resumability & Phase Entry Checks

Multi-phase plans are often interrupted by context limits, timeouts, or user interjection. Design for resume from the start.

### Entry Check Pattern

Before starting any phase, check whether its primary artifact already exists and appears complete:

```
IF docs/{task}-issues-context.md EXISTS
  AND is complete (contains summary stats, no obvious truncation)
  → Phase complete, skip to next
ELSE → run this phase from scratch
```

### State Recovery

On resume after interruption:

1. **Scan artifacts** — check each artifact for existence and a completion marker (e.g., "## ✅ All batches complete" or a final summary line)
2. **Determine last checkpoint** — for incomplete artifacts, find where work stopped (last batch number, last marked-complete item)
3. **Resume from checkpoint** — do NOT re-read completed files or re-apply completed fixes
4. **Cross-reference claims vs reality** — before skipping a phase, quickly verify that its claimed output actually exists on disk

### Append-Only Convention

- Progress logs are append-only — never overwrite.
- Each batch entry includes: items attempted, items completed, items failed (with reasons).
- The final summary line is the completion marker used by entry checks.

## Cross-Platform Script Remediation

When a plan involves auditing or remediating scripts that exist as parallel implementations across shell languages (Bash, PowerShell, and/or BAT), several patterns apply beyond standard batch processing.

### Cross-Platform Drift Detection

Parallel implementations (e.g., `dev.sh` / `dev.ps1` / `dev.bat`) naturally drift apart over time. Detect drift by automating consistency checks:

| Check | What to look for |
|-------|-----------------|
| Shebangs | Bash: `#!/usr/bin/env bash` + `# shellcheck shell=bash`. PS: `#!/usr/bin/env pwsh`. BAT: `@echo off` |
| Error handling flags | Bash: `set -euo pipefail`. PS: `$ErrorActionPreference = "Stop"`. BAT: proper `if errorlevel` checks |
| ShellCheck directives | Every `.sh` file should have `# shellcheck shell=bash` |
| Version strings | Parallel files that embed a `Version: x.y.z` string should agree |
| Exit codes | Same exit-code conventions across all three languages |

**Implementation pattern**: Write a cross-ref script that defines parallel "pairs" (arrays of sh/ps1/bat paths), iterates each, and reports drift as WARN/FAIL per check. Include a `--fix` mode for auto-correctable items (version alignment, header formatting). Deploy it as `.sh` + `.ps1` so it runs in CI regardless of OS.

**Path resolution pitfall**: When a verify or cross-ref script resolves module/utility paths with `$(dirname "$0")/../../`, it expands relative to the script's own directory, not the repo root or the subproject root. If the script lives in `Bash/scripts/` but references modules in `rhixecompany/Banking/install/lib/`, the relative path must explicitly include the intermediate subproject directory. Prefer an environment variable or absolute basedir anchor derived from `SCRIPT_DIR` to avoid fragility.

### Git Bash (MSYS) Portability Pitfalls

On Windows, Git Bash ships with MSYS utilities that deviate from Linux bash in subtle ways:

- **`echo -e`**: Git Bash's `echo` typically interprets `-e` as a literal string argument, not a flag. Use `printf` for any output that needs escape-sequence interpretation (newlines, tabs, colors). This is the single most common "works on Linux, breaks on Windows" issue.
- **Array scoping in functions**: Indexed arrays assigned inside functions may not persist after the function exits, depending on `declare -g` usage. For portable output accumulation across functions, prefer string-based accumulation (`var="${var}item "`) over `array+=("item")`.
- **`set -o pipefail`**: Supported in Git Bash, but pipe behavior can differ due to MSYS path translation. Always include `set -euo pipefail` as a defensive baseline.

### Shared Log Rotation Pattern

Scripts that write log files should use a shared rotation utility rather than ad-hoc inline rotation:

- Create `lib/log-rotate.sh` (Bash) and `lib/log-rotate.ps1` (PowerShell) with a standard interface:
  - Bash: `rotate_logs "$log_file" [max_files=5] [max_age_days=30] [compress_after_days=7]`
  - PowerShell: `Rotate-Logs -Path "$log_file" [-MaxFiles 5] [-MaxAgeDays 30] [-CompressAfterDays 7]`
- Rotated files get a timestamp suffix (e.g., `script-2026-05-24.log`).
- After `max_files` are exceeded, delete the oldest.
- After `max_age_days`, delete regardless of count.
- After `compress_after_days`, gzip the file (and skip future rotation on compressed files).
- All scripts that write logs call the shared utility rather than implementing rotation inline.

### Modular Shell Refactoring

When refactoring a large shell script (1000+ lines) into a thin orchestrator + modules:

1. **Identify domains**: Config, utilities, path resolution, dependency checks, registry operations, selection logic, mode switching, preview, installation.
2. **Number modules** (`00-config.sh` through `08-install.sh`) to ensure deterministic sourcing order.
3. **Thin orchestrator** sources all modules via `source "${script_dir}/lib/00-config.sh"` etc. at startup, then delegates to a `main "$@"` function.
4. **Preserve interface**: The thin orchestrator must accept the same arguments, environment variables, and exit codes as the original monolith.
5. **Validate**: Run `bash -n` on every module and the orchestrator.

This pattern reduces a 1500-line monolith to ~200 lines of orchestrator with clear module boundaries — typically 85%+ reduction in the main file.

## Verification Phase

Every plan needs a dedicated verification step as its final phase:

### Verification Phase Every plan needs a dedicated verification step as its final phase: 1. **Re-read source files from disk** — do not rely on memory or the fix plan's self-reported claims
2. **Check each issue against current file state** — is the fix actually present in the file?
3. **Cross-reference claimed-fixed vs actually-fixed** — flag any discrepancies between what the plan claims was done and what is actually on disk
4. **Write a verification report** — pass/fail per issue with summary statistics
5. **If verification uncovers additional fixes**, patch the files, then append a follow-up note/addendum to the relevant progress and verification artifacts and re-run the targeted checks before claiming completion

### Cross-Reference Verification Pattern (Integrated from verification-before-completion)

Use when confirming that a multi-batch remediation or fix plan was fully applied.

**Process:**

1. **Read all artifacts** — Collect all related docs (list, issues, plan, summary, fix-specs). Understand the full document lifecycle — some documents may be superseded by newer ones.

2. **Build a cross-reference matrix** — Map each documented issue/fix batch onto a checklist. Note which documents reference each item.

3. **Verify both directions:**
   - **Forward** (issues → fixes): For each documented issue, check the actual file on disk for the fix.
   - **Backward** (fix batches → disk): For each plan batch, confirm every listed file was modified as described.

4. **Run automated checks** — Use available linters/syntax checkers:
   - Shell: `shellcheck -f gcc <files>` (install via `npm install -g shellcheck` if missing)
   - Check for errors (exit code, grep for `error:`), warnings, and notes separately.
   - Module structure: verify expected files exist with `ls` and `wc -l`.

5. **Handle environment gaps** — When type-check or lint tools fail because `node_modules` aren't installed or configs are stale, note it as "pre-existing / unrelated" rather than blocking the verification.

6. **Update summary** — Append a Phase 5 verification section with:
   - Shellcheck error/warning/note counts per area
   - On-disk cross-check results per issue category
   - Any pre-existing environment issues (skipped, not scoped)
   - Module/file structure verification results

7. **Handle overlapping documents** — When multiple plan docs exist (e.g., `fix-issues-context.md` from plan A, `prompt.md` from plan B), verify both independently. Items from superseded plans should still be on disk.

8. **If late fixes happen after initial verification**, append a short addendum to the verification artifact, re-read the changed files, and re-run the targeted checks before claiming the work is finished.

**Independence principle**: When verifying, read only the original requirements/issues catalog — do NOT read the fix plan first. This prevents confirmation bias (seeing what you expect to see rather than what's actually there). **After initial verification**: Optionally cross-check against the fix plan to catch anything the plan claimed but you missed. **Pitfall**: A completion summary may be accurate at the time it was written but still miss follow-up fixes applied later; always re-read the updated files and refresh the verification artifact if you make late changes.

**Signals that triggered this technique:**
- User asks to "implement remaining steps" of a prompt with explicit phases/tasks/subtasks/actions
- Multiple planning artifacts exist (list, issues, plan, summary) with overlapping scope
- A comprehensive fix plan was authored but verification state is unknown

**Pitfall:** Do not treat the first completion summary as final if you later patch files during the same session; refresh the verification artifact so the document trail matches the latest on-disk state.

## Best Practices

- Have a clear plan before starting
- Document progress at each checkpoint in durable artifacts
- Get reviews before proceeding (or self-review with fresh eyes)
- Adjust plan based on findings during execution
- Keep stakeholders informed of progress and decisions
- Maintain version control of both code and plan artifacts
- Archive completed phases — remove completed items from working context
- Prefer surgical `patch` edits over full rewrites
- Verify independently at the end — don't trust your own claims


## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

