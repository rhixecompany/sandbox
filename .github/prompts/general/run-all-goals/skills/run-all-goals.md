---
name: run-all-goals
title: "Run All Goals — Unified Pipeline Skill (Tree-Primary)"
description: >
  Execute the unified run-all-goals pipeline with tree.prompt.txt as PRIMARY source.
  Cleanup-first execution: delete workspace clutter, update config files,
  convert mjs to mts, migrate source code, then sync agents and verify.
  Score >= 99 on all judge skills.
version: 3.0.0
author: Alexa (via OWL)
license: MIT
tags: [implementation, execution, unified, tree-primary, score-99, cleanup-first]
metadata:
  hermes:
    related_skills:
    - using-superpowers
    - brainstorming
    - subagent-driven-development
    - prompt-management
    - executing-plans
---

# Run All Goals — Unified Pipeline Skill (Tree-Primary)

## Overview
Execute the comprehensive run-all-goals pipeline with tree.prompt.txt as PRIMARY source.
Cleanup-first execution: delete workspace clutter, update config files, convert mjs to mts,
migrate source code, then sync agents and verify. 4 goals, 17 subgoals, 11 phases.

## Primary Source
**tree.prompt.txt** (C:\Users\Alexa\Desktop\SandBox\tree.prompt.txt) is the authoritative primary source.
All goals, subgoals, phases derive from tree.prompt.txt.

## Workflow (Tree-Cleanup-First)

### Phase 1: Cleanup
Delete workspace clutter per tree.prompt.txt:
- .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders
- *.json (except package.json, pyrightconfig.json), *-report.md files
- *.log, *.txt files (skip *.prompt.txt files)

### Phase 2: Config Files Update
Update/verify config files per tree.prompt.txt:
- .editorconfig, .git-blame-ignore-revs, .gitattributes, .gitignore, .gitmodules
- .markdownlint-cli2.jsonc, .markdownlint.jsonc, .pre-commit-config.yaml, .prettierignore, .prettierrc.json
- *.toml, *.yaml files
- requirements.txt, tsconfig.json
- package.json, pyrightconfig.json, *.json files

### Phase 3: mjs->mts Conversion
Convert all *.mjs files to *.mts per tree.prompt.txt

### Phase 4: Docs & Markdown Cleanup
Cleanup/update *.md files including PLAN.md, SOUL.md, SPEC.md, USER.md and all docs

### Phase 5: Source Migration
Update/verify *.py, *.mjs, *.mts files; create src directory and migrate files into src

### Phase 6: Agent Sync
Copy hooks, skills, plugins, instructions to ALL AI agent roots (.github, .copilot, .codex, .opencode, .hermes); ensure identical configs

### Phase 7: Config/scripts Sync
Sync profiles; verify quick_commands; sync .env/config.yaml

### Phase 8: Diagnostic Repair
hermes doctor --fix

### Phase 9: Judge Verification
Run judge skills; target score >= 99 on all

## Skills Required
| Skill | Purpose |
|---|---|
| using-superpowers | Foundational workflow |
| brainstorming | Idea generation |
| user-communication-preferences | Alexa's style |
| mcp-sequential-thinking | Chain-of-thought |
| systematic-debugging | Root cause |
| subagent-driven-development | 2-stage review |
| hermes-diagnostic-repair | Diagnostic |
| log-analysis-and-triage | Log analysis |
| plans-and-specs | Plans |
| create-implementation-plan | Plan creation |
| implementation-plan | Detailed plans |
| executing-plans | Multi-phase execution |
| writing-clearly-and-concisely | Clarity |
| prompt-management | Prompt workflow |
| skill-judge | Judge scoring |
| prompts-judge | Prompt scoring |
| plans-judge | Plans scoring |
| specs-judge | Specs scoring |

## Verification Checklist
- [ ] tree.prompt.txt verified as primary source
- [ ] Phase 1 Cleanup complete: .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts removed
- [ ] Phase 2 Cleanup: *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt cleaned
- [ ] Phase 3 Config files updated/verified (.editorconfig, .gitignore, etc.)
- [ ] Phase 4 mjs->mts conversion complete (no .mjs remains)
- [ ] Phase 5 *.md files cleaned and updated
- [ ] Phase 6 src directory created; *.py/*.mjs/*.mts migrated
- [ ] Agent sync: 5 AI agents identical
- [ ] All judge skills score >= 99
- [ ] Config files validated (package.json, pyrightconfig.json, tsconfig.json, requirements.txt)
- [ ] No placeholders in any artifact
- [ ] DRY enforced: rules reference shared templates
- [ ] Security: no embedded secrets; ${ENV_VAR} placeholders used
- [ ] Git push succeeded on clean-development, development, production

## Best Practices
- tree.prompt.txt is PRIMARY source — all goals/subgoals derive from it
- Cleanup-first: delete before constructing
- Use MCP servers first
- DRY: shared components in _shared/
- Concise, action-first responses
- Verify with tools, not memory
- Score >= 99 on all judge skills
- Use clarify tool when ambiguous
