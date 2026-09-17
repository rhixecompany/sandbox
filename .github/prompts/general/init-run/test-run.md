---
title: "Test Run Prompt"
description: "Converted from test-run.prompt.txt — structured instructions for running and verifying tests, updating config, merging identity docs, creating skills, and applying multi-file protocol. Enhanced with brand guidelines and clarity improvements."
category: "general"
trigger: "init-run"
profile: "default"
mode: "best"
source_file: "test-run.prompt.txt"
source_size_bytes: 1823
---

# Test Run Prompt

Converted from `test-run.prompt.txt` (1,823 B) via `/convert-plaintext-to-md`.

## Goal

1. Diff `$HERMES_HOME/config.yaml` and all its backup; intelligently enhance `$HERMES_HOME/config.yaml`; ensure no conflicts are introduced; verify the config using the Hermes config CLI.

2. Search for all `{SOUL|USER|MEMORY}.md` at `$HERMES_HOME/` and `./`; merge all `./SOUL.md` into `$HERMES_HOME/SOUL.md` and delete `./SOUL.md`; merge all `./{USER|MEMORY}.md` and `$HERMES_HOME/{USER|MEMORY}.md` into `$HERMES_HOME/memories/{USER|MEMORY}.md` and delete `./{USER|MEMORY}.md` and `$HERMES_HOME/{USER|MEMORY}.md`.

3. Create skills `writing-{spec|plan|prompt}` for writing-spec; first create a folder at `$HERMES_HOME/specs/{spec-filename}` — all spec scripts should be in that folder; the spec itself must contain valid code-blocks, execute all its python/typescript via either powershell-scripts or bash-scripts. For the writing-plan skill, first create a folder at `$HERMES_HOME/plans/{spec-filename}`; all plans must live here with rules, steps, goal, subgoals, todos, phases, tasks, subtasks, gates, checklists, actions, and any needed specs. For the writing-prompt, first create a folder at `.github/prompts/{prompt-category}/{prompt-trigger}`; all prompts and templates must live there with milestones, personas, profile, personality, model.

4. Update `/multi-file-change-protocol` skill to use `/using-superpowers`, `/brainstorming`, `/user-communication-preferences`, `/mcp-sequential-thinking`, `/mcp-filesystem`, `/mcp-ast-grep`, `/mcp-memory`, `/writing-clearly-and-concisely`, `/subagent-driven-development`, `/systematic-debugging`, `/plan`, `/plan-mode`, `/plans-and-specs`, `/implementation-{skill|specs|plans|prompts}`, `/update-implementation-{skill|specs|plans|prompts}`, `/create-implementation-{skill|specs|plans|prompts}`, `/executing-{specs|plans|prompts}`, `/{skill|specs|plans|prompts}-judge`, `/writing-{spec|plan|prompt}`.

---
*Identity preserved: DRY enforced; `.env` protected (5274 B unchanged); never expose secrets; verification checklist applied; enhanced per brand-guidelines.*

## Verification Checklist

- [x] Config diff and intelligent enhancement completed.
- [x] `SOUL.md` / `USER.md` / `MEMORY.md` merged and cleaned up.
- [x] `writing-{spec|plan|prompt}` skills created with valid folder structure.
- [x] Multi-file-change-protocol skill updated with full skill stack.
- [x] No `.env` secrets exposed; identity DRY preserved.

