---
title: Skills Debug and Remediation Execution
trigger: /skills-debug
description: >
  Execute the skills remediation plan from docs/plan/skills-debug-plan.md.
  Fix F-grade skills first (boilerplate, missing frontmatter), then C-grade
  (unclosed fences, duplicate headings), then verify.
tags: [hermes, skills, remediation, fix]
---

## Goal

Apply fixes to all F-grade and C-grade skills identified in the audit.
Target: F=0, C≤5 after completion.

## Context

- **Skills root:** `C:\Users\Alexa\AppData\Local\hermes\skills\`
- **Audit results:** `docs/skills-audit-results.json`
- **Remediation plan:** `docs/plan/skills-debug-plan.md`
- **Master index:** `docs/skills-debug-context.md`

## Execution Steps

### Step 1: Fix F3/F3b Boilerplate (29 skills)

For each F3/F3b skill, read the file and fix the `## Goal` section:

**F3 pattern** — `## Goal\nUse when Use when <desc>`:
```
Replace: "## Goal\nUse when Use when "
With:    "## Goal\n"
```

**F3b pattern** — `## Goal\nUse when "<desc>" to accomplish...`:
```
Replace: '## Goal\nUse when "'
With:    "## Goal\n"
```

Skills to fix:
- autonomous-ai-agents: acpx-executor, copilot-cli, customize-opencode, dispatching-parallel-agents, hermes-agent, opencode, qwen-code, skill-creator, skill-judge, writing-skills
- github: git-gh-commands, git-helper, github-auth, github-pr-workflow, github-repo-management, using-git-worktrees
- planning: plans-and-specs
- qa: verification-before-completion, webapp-testing
- software-development: codemap, context7, executing-plans, plan, script-orchestration, simplify, spike, subagent-driven-development, systematic-debugging, test-driven-development, writing-plans

### Step 2: Fix F1 Missing Frontmatter (1 skill)

For `devops/rbac-audit-logging/SKILL.md`:
- Add `---\nname: rbac-audit-logging\ndescription: <extract from content>\n---\n` at the top

### Step 3: Fix C2 Unclosed Code Fences (5 skills)

For each C2 skill, append a closing ` ``` ` at the end of the file:
- autonomous-ai-agents/enhance-markdown
- autonomous-ai-agents/opencode
- devops/git-history-preserving-migration
- github/git-submodule-workflow
- mcp/native-mcp

### Step 4: Fix R1 Duplicate Headings (10 skills)

For each R1 skill, merge duplicate sections:
- Keep the first occurrence, remove subsequent duplicates
- Merge content if the duplicates have different content

### Step 5: Re-run Audit

Run the audit script from Phase 3 and verify:
- F-grade = 0
- C-grade ≤ 5 (only C1 pip warnings should remain)

### Step 6: Git Commit

```bash
git add -A
git commit -m "chore: skill library audit and remediation 2026-06-04"
```

## Tools

- `read_file(path)` — Read skill before fixing
- `patch(path, old_string, new_string)` — Apply targeted fix
- `write_file(path, content)` — Full rewrite if needed
- `execute_code(code)` — Re-run audit verification
