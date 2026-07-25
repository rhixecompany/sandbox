---
name: prompt-sync
title: "Hermes Prompt Workspace Sync"
description: "Sync Hermes root prompt/support artifacts into the workspace repo, then recognize/register them."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - prompts
  - sync
  - workspace
  - docs
metadata:
  hermes:
    tags:
      - imported
---

# Hermes Prompt Workspace Sync

Use when the workspace `.github/prompts/...` workflow needs the Hermes root prompt library, plans, scripts, hooks, templates, or skills mirrored into the repo and verified as recognizable by Hermes.

## When to Use

- Copying `~/AppData/Local/hermes/{prompts,plans,scripts,hooks,templates,skills}` into `.github/prompts/`, `.github/plans/`, `.github/scripts/`, `.github/hooks/`, `.github/templates/`, or `.github/skills/`
- Resolving missing prompt references that block `/execute-all-prompts` or other orchestrators
- Verifying Hermes recognizes the synced prompt/support files

## Workflow

### 1. Generate a triage manifest

Create a concise markdown manifest under `docs/` with file counts and notable findings/missing refs.

### 2. Mirror folders

Sync these Hermes roots into the workspace:

| Source | Destination |
|--------|-------------|
| `prompts/` | `.github/prompts/` |
| `plans/` | `.github/plans/` |
| `scripts/` | `.github/scripts/` |
| `hooks/` | `.github/hooks/` |
| `templates/` | `.github/templates/` or prompt-family template dirs under `.github/prompts/templates/` |
| `skills/` | `.github/skills/` |

Preferred sync behavior:
- Preserve directory structure.
- Exclude runtime artifacts such as `__pycache__` and `.git`.
- Do not invent missing prompt files; create meaningful placeholder files with header/Purpose/TODO instead.

### 3. Verify prompt recognition

After sync:
- Confirm workspace prompt files exist.
- Confirm the orchestrator's referenced prompt files are present.
- Use `hermes skills list` or `hermes hooks list` to verify recognition/registration where applicable.
- Re-run prompt validation if size/schema limits apply.

### 4. Re-check references

Search for dead template/prompt references in the synced set and resolve them before declaring completion.

## Pitfalls

- **Do not conflate repo prompt files with Hermes root prompt files.** Hermes may read from the installed prompt library, not `.github/prompts/`.
- **Empty root `templates/`.** If `templates/` is missing at root, keep template content under prompt-family directories (e.g. `.github/prompts/templates/`).
- **Path-mismatch drift.** After migration, update paths in docs, workflows, and prompts before running jobs that depend on them.
- **Registry mismatch.** File presence alone is not enough; verify Hermes actually recognizes the synced prompt/support files.
- **Redundant overwrite.** Mirroring all folders blindly (without triage) can overwrite in-sync files harmlessly and wastes time. Worse, it can clobber .github-only additions never present in the root. Always triage first — generate the manifest, identify gaps, only sync what's missing.
- **Dangling reference file.** If SKILL.md references a `references/*.md` file, that file must exist on disk. Verify linked references before claiming the skill is complete. Create the reference alongside the SKILL.md.

## Reference

See `references/workspace-prompt-sync.md` for the concrete manifest schema and sync checklist used in recent sessions.
