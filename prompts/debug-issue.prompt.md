---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Debug Issue
name: debug-issue
agent: "agent"
model: "Auto (copilot)"
tools: ["codebase", "search", "runCommands", "problems"]
description: "Debug an issue with reproducible analysis, root-cause isolation, and verification steps"
---

<!-- Based on/Inspired by: https://github.com/github/awesome-copilot/blob/main/prompts/debug-issue.prompt.md -->

## Goal

Diagnose and resolve a reported issue with the smallest safe fix and clear validation steps.

## Inputs

- Error message, logs, or failing behavior
- Relevant file paths or affected feature area
- Reproduction steps if available

## Steps

1. Reproduce the issue from available evidence.
2. Identify likely root causes and narrow to the primary cause.
3. Propose minimal code or config changes to fix the issue.
4. Validate with targeted checks and summarize results.

## Output

- Root cause summary
- Proposed or applied fix
- Verification checklist with commands executed
- Residual risks or follow-up recommendations


## Template References

Templates in `templates/debug-issue/`:
- `inputs.md`
- `output.md`
- `steps.md`
