---
name: executing-prompt-workflows
description: "Executing Prompt Workflows"
title: Executing Prompt Workflows
version: 1.0.0
author: Hermes Agent
tags: [prompts, workflow, agents, sync, dedup, artifact, hermes]
---

# Executing Prompt Workflows

Prompt files (e.g. `prompts/agents-fix.prompt.md`) are workflow definitions with frontmatter
(`trigger`, `dependencies`, `skills`) and a body of `Goal / Context / Inputs / Outputs / Rules /
Phases / Steps / Tasks / Actions`. Executing one means running the phases against the REAL
workspace and writing the declared Outputs as an artifact — not describing what you would do.

## Overview

Comprehensive skill for working with the technology.

## Workflow

### Phase 1: Discovery and Understanding
Read the prompt file fully, resolve referenced templates, and perform discovery against the real filesystem to map generic instructions to concrete artifacts.

### Phase 2: Execution and Verification
Execute each phase declared in the prompt file in order, applying minimal intent-preserving changes. After each phase, verify correctness by re-parsing files and confirming structural integrity.

### Phase 3: Artifact Output and Reporting
Write the final artifact to the declared Outputs location. Include per-phase findings, a change log with before/after representations, flagged-but-not-edited items, and a verification summary.

## Core workflow

1. **Read the prompt file fully.** Note its `Phases`, `Outputs`, and `Rules` sections. The Outputs
   section tells you exactly what artifact(s) to produce.
2. **Resolve referenced templates/rules — but verify they exist.** Prompts reference shared files
   like `templates/_shared/rules-core.md` and `templates/_shared/skills-table-core.md#<prompt>`,
   and sometimes a per-prompt `templates/<prompt>/` dir. Read the ones that exist; the per-prompt
   dir often does NOT exist — fall back to the inline body + `_shared/` copies. Record which refs
   you skipped and why in the artifact frontmatter (transparency).
3. **Discovery against the real filesystem.** A generically-worded prompt ("sync agents across
   Hermes and Copilot") maps to concrete on-disk artifacts. Find them before assuming. See the
   discovery pitfalls below.
4. **Execute phases in order**, verifying after each (rules-core mandates "verify after each pass").
5. **Apply only minimal, intent-preserving changes.** Fix what is unambiguously broken; FLAG
   (don't auto-edit) anything requiring a judgment call (renames, deletions, missing-but-optional
   fields). This matches the near-universal "preserve intent / preserve registrations" rule.
6. **Write the artifact** to the Outputs location (this workspace convention: `results/<prompt>.output.md`).
   Include: per-phase findings, a cross-reference/registry table, changes-applied with before/after,
   flagged-but-not-edited items, a verification table, and a "skipped/not-applicable" section.

## Discovery pitfalls (the hard part)

- **Broad `search_files(pattern="*")` times out** on large workspaces. Use specific globs
  (`AGENTS.md`, `*.agent.md`, `verify-agents.*`) or `search_files target=content` with a real regex.
- **File-glob search needs a wildcard**: `pattern="*agent*"` works, `pattern="agents"` returns 0.
- **Reports/inventories drift from disk.** Stale audit reports may enumerate files
  (e.g. `projects/comicwise/.github/agents/*`) that no longer exist. Always confirm counts on disk
  (`find ... | wc -l`) before treating a report as ground truth — the mismatch is itself a finding.
- **Relative-path references break with directory depth.** A file at `projects/Bash/docs/AGENTS.md`
  referencing `../../.github` resolves to `projects/.github` (wrong); it needs `../../../.github`.
  Verify with `os.path.exists` or `ls -d` from the file's own directory before and after fixing.
- **"Duplicate" files are often drifted, not identical.** md5 the clusters. Three copies with three
  different hashes = manual consolidation task (pick the most complete as canonical), not a blind dedup.
- **`bash` on this Windows host is MSYS/git-bash.** Use POSIX syntax. Some `find` invocations with
  many `-o` branches can hang/time out — keep them bounded (`-maxdepth`, specific `-name`).

## Validating agent/frontmatter schema

Parse YAML frontmatter with Python + `yaml.safe_load` rather than grep, so you catch structural
bugs, e.g. `description: >` (block scalar) wrapping a single-quoted string bakes stray `'…'` quotes
into the value. Re-parse after any edit to confirm the fix. Scan the whole set for missing required
keys and report counts (e.g. "49 of 174 lack `tools:`").

## Pitfalls

- **Double frontmatter blocks cause parse errors.** Some SKILL.md files accumulate redundant YAML frontmatter blocks. Always validate that exactly one `---...---` block exists at the top of the file.
- **Inline YAML in descriptions can break parsers.** Multi-line descriptions using `>` or `|` block scalars may embed control characters. Always test with `yaml.safe_load` after editing.
- **Relative paths in prompt references may not resolve.** A prompt referencing `templates/<name>/` may find no directory exists — always check with `os.path.exists` before treating refs as authoritative.
- **Old audit reports become stale.** Cross-reference any inventory against the real filesystem before using it as ground truth.
- **Fabricated results undermine trust.** Never guess at file contents or produce synthetic output for missing data — report the blocker honestly.

## Deliverable rule

The job is a working artifact backed by real tool output. Never fabricate discovery results or
file contents. If a template ref or dependency is missing, say so and proceed with the inline body —
do not stall.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Executing Prompt Workflows operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## When to Use


- When you need to perform Executing Prompt Workflows operations or tasks
- When managing Executing Prompt Workflows infrastructure or configurations
- When automating or debugging Executing Prompt Workflows workflows
- **Triggers**: "executing prompt workflows" required for a project

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
