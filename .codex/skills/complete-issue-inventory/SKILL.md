---
name: complete-issue-inventory
title: "Complete Issue Inventory"
description: "Use when the task is to debug/fix ALL issues, errors, warnings. Ensures every discovered issue is fixed or escalated with evidence — no non-blocking dismissals."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [qa, verification, debugging, workflow]
---
# Complete Issue Inventory

## Overview

Automated reasoning and workflow tool for `complete-issue-inventory`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

The user says "debug/fix all issues, errors, warnings" — for code, config, markdown, project context, tooling, or any inspection scope. The deliverable is a fully-resolved issue list, not a categorized report with dismissed buckets.

## The Rule

Every issue discovered gets one of three statuses:

| Status | Meaning | Required Evidence |
|--------|---------|-------------------|
| ✅ FIXED | Fix applied and confirmed | Diff, lint pass, or command output |
| 🔴 BLOCKED | Genuinely unfixable | Exact error + alternative tried |
| 🟡 PENDING | Needs user decision | Justification in summary |

## Anti-Pattern: The "Non-Blocking" Dismissal

Writing "Remaining observations (non-blocking): X can't be installed" without attempting a fix **will trigger a user correction**. The user reads this as "gave up without trying."

If a tool can't be installed via one method, try alternatives before labeling it blocked. Only escalate with specific reproduction evidence.

## Workflow

1. **Run all investigation tools** first (lint, type-check, test, shellcheck)
2. **Capture every distinct issue** — one row per file or error code
3. **Attempt a fix for each** — partial fix is better than a label
4. **If fix fails, reproduce the failure** — capture exact error output
5. **Only then label it blocked** — with evidence attached
6. **Zero labels without fix attempts** — every issue gets a fix or an escalation

## Why This Works

- "Non-blocking" in a full-fix context means "skipping without consent"
- Environment issues (missing binary, network timeout) are addressed, not dismissed
- Zero unresolved issues after a "fix all" pass builds trust


## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Reference

- `references/real-world-example.md` — full inventory workflow applied to a real project
- `references/batch-frontmatter-audit-pattern.md` — batch YAML frontmatter audit/fix pattern used on a 213-file prompt library

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Complete Issue Inventory" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
