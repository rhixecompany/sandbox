---
name: executing-prompt-workflows
description: "Executing Prompt Workflows"
---

---
name: executing-prompt-workflows
description: Execute a `.prompt.md` / trigger-style workflow file (agents-fix, bash-scripts-fix, skills-fix, workspace-consolidate, etc.) end-to-end and produce a REAL file-backed artifact. Use when the user says "execute the X prompt", "run /X", or points at a prompt-definition file in prompts/ that declares Goal/Phases/Outputs/Actions.
version: 1.0.0
tags: [prompts, workflow, agents, sync, dedup, artifact, hermes]
title: Executing Prompt Workflows
author: Hermes Skills Team---

# Executing Prompt Workflows

Prompt files (e.g. `prompts/agents-fix.prompt.md`) are workflow definitions with frontmatter
(`trigger`, `dependencies`, `skills`) and a body of `Goal / Context / Inputs / Outputs / Rules /
Phases / Steps / Tasks / Actions`. Executing one means running the phases against the REAL
workspace and writing the declared Outputs as an artifact — not describing what you would do.

## Overview

Comprehensive skill for working with the technology.

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

## Deliverable rule

The job is a working artifact backed by real tool output. Never fabricate discovery results or
file contents. If a template ref or dependency is missing, say so and proceed with the inline body —
do not stall.
