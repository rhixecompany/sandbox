---
name: sequential-orchestration
title: Sequential Orchestration Rescue & Verification
description: Workflow for blocked sequential pipelines that must reach zero validation errors before claiming done. Covers "only then" workflows, validation-failure recovery, and classifying true blockers vs repeatable patterns.
version: 1.0.0
author: Alexa (via OWL)
license: MIT
tags:
- orchestration
- validation
- sequential
- recovery
- planning
- prompts
metadata:
  hermes:
    related_skills:
    - plans-and-specs
    - writing-plans
    - verification-before-completion
    - systematic-debugging
---
# Sequential Orchestration Rescue & Verification

Use when:
- The previous phase is not really done, but someone claimed done.
- Validation output shows ≥1 issues and the exact same issues remain after a post-fix validation run.
- The user explicitly demands "fix all and any blockers", "dont stop", or "only then" sequencing.

Trigger phrases:
- `/execute-all-prompts` (or similar ordered-phase runbooks)
- "execute in order / only then"
- "do not stop until all phases executed"

## Default Behavior

1. Stop any blind retry on the same change pattern.
2. Validate the actual filesystem state first; do not rely on parsed/indexed views of the file tree.
3. Rebuild the file list from the current directory at the moment of action.
4. Classify the issue class before creating any new remediation ticket:
   - structural: exact same failure after patch, suggesting the patch target/scope was wrong
   - missing artifact: file/path the user expects does not exist yet
   - trigger/identity mismatch: trigger/name/title drift between filename and prompt metadata

## Recovery Loop

1. Inventory actual files vs expected files.
2. Print exact paths and line-level context for any failing item's header region.
3. Identify the error class.
4. Build one verified remediation action per error class.
5. Re-run validation.
6. Stop when validation returns 0 issues across the target scope.

## "Only Then" Enforcement

- Phase N verification is the *only* gate to start Phase N+1.
- Never declare Phase N done unless its validation gate returns scope-wide 0 issues.
- Partial fixes are transitional; they are not completions.
- If the user demands continuation, continue, not by repeating the same patch, but by switching to verified-path discovery.

## Prompt Pipeline Specifics

When validating a prompt tree:
- Enumerate files using filesystem enumeration.
- Expect valid frontmatter blocks: open `---`, close `---`, heading on next line.
- Invalid merged form: `---## Title` or repeated `---` inside frontmatter before its first closing fence.
- Expected command shape for checks: use native `terminal`/`read_file`/`search_files` with current workspace state.

## Pitfalls

- **None documented yet.**
- Add common pitfalls, edge cases, and failure modes specific to this skill.

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |
