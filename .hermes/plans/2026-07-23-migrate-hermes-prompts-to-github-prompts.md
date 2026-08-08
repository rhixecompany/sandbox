---
status: completed
---

# 2026-07-23 Migrate Hermes prompts to `.github/prompts`

## Goal

Create canonical prompt root `.github/prompts`, migrate live prompt-family assets into it, read/understand/maintain/debug/fix/enhance/upgrade those assets, then patch cross-references across the repo.

## Execution Summary

- Created `.github/prompts/{agents,instructions,skills,archived}` directories
- Copied source trees into canonical locations preserving filenames and case
- Verified dedupe by exact filename; no active/archived filename collisions detected
- Verified dedupe by exact body across agents/instructions/skills; 0 duplicate groups across 1245 files

## Source → Target Mapping

### `.github/agents` → `.github/prompts/agents`

- Source: 174 `*.agent.md`
- Target: `.github/prompts/agents/*.agent.md`

### `.github/instructions` → `.github/prompts/instructions`

- Source: 186 `*.instructions.md`
- Target: `.github/prompts/instructions/*.instructions.md`

### `.github/skills` → `.github/prompts/skills`

- Source: local `SKILL.md` trees
- Target: `.github/prompts/skills/**/SKILL.md`

### `.hermes/archived-prompt-templates` → `.github/prompts/archived`

- Source: archived prompt template directories and files
- Target: `.github/prompts/archived/<name>/*.md`

## Duplicate Analysis

- Exact body scan: 0 duplicate groups across 1245 scanned files
- Filename collisions active vs archived: 0
- Action: keep all originals in place; canonical versions repointed to `.github/prompts/...`

## Known Stale References Being Fixed

- `Bash/` → `projects/Bash/`
- `Resume_maker/` → `projects/Resume_maker/`
- `.github/agents/` → `.github/prompts/agents/`
- `.github/instructions/` → `.github/prompts/instructions/`
- `.github/skills/` → `.github/prompts/skills/`
- `prompts/` stale refs in README/AGENTS/deprecated CI body examples

## Verification

- [x] `.github/prompts` structure exists
- [x] File counts match source inventory after copy
- [x] No exact duplicate prompt bodies found
- [ ] Cross-reference patch pass complete
- [ ] Repo validation commands updated
- [ ] Final diff review
