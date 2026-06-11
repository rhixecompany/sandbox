---
description: 'Deterministic path and instruction routing for monorepo edits'
applyTo: '**/*'
---

# Monorepo Path Routing

Use this checklist before making edits in this workspace.

## Routing Rules

- Resolve the target file path first and identify its nearest AGENTS.md.
- Apply instruction precedence in this order:
  1. Nearest matching instruction file in the target subtree.
  2. Root instruction files under .github/instructions/.
- Treat workspace root AGENTS.md as fallback guidance only.

## Deterministic Pre-Edit Checklist

- Confirm target path exists.
- Confirm nearest AGENTS.md for that path.
- Confirm matching instruction files for the target extension and folder.
- Confirm project runtime root for commands:
  - Use Bash/ for shared TypeScript automation scripts and validation commands.
  - Use subproject root for project-local package.json and tests.

## Duplicate-Asset Prevention

Before creating any new instruction, prompt, skill, agent, plugin, or hook:

- Check the canonical inventory report:
  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
- Search for an existing same-purpose asset before creating a new file.
- Prefer extending existing assets over creating near-duplicates.

## Output Requirements for Agents

When reporting completed work, include:

- The resolved AGENTS.md path used for the edit.
- The instruction files that were applied.
- The command root used for validation (for example, Bash/ or a subproject
  path).

## Safety Notes

- Never run destructive git commands unless explicitly requested.
- Never assume root-level commands apply to all subprojects.
- If path scope is unclear, stop and ask for clarification before editing.
