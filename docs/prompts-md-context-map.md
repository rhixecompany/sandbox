# Prompts Markdown Context Map

Generated: 2026-05-25
Scope: `Prompts/*.prompts.md`

## Files To Modify

| File | Purpose | Primary Dependencies |
| --- | --- | --- |
| `Prompts/agents-fix.prompts.md` | Agent migration audit/plan/execute workflow | `brainstorming`, `plans-and-specs`, `dispatching-parallel-agents`, `subagent-driven-development`, `systematic-debugging`, `simplify` |
| `Prompts/bash-scripts-fix.prompts.md` | Script inventory and remediation workflow | Same as above |
| `Prompts/commands-fix.prompts.md` | Command migration audit/plan/execute workflow | `dispatching-parallel-commands` + common planning/debug skills |
| `Prompts/general.prompts.md` | General productivity workflow prompt | Common planning/debug skills + `context7`, `sequential-thinking` |
| `Prompts/repo.prompts.md` | Cross-folder project migration workflow | Common planning/debug skills |
| `Prompts/skills-fix.prompts.md` | Skills migration audit/plan/execute workflow | Common planning/debug skills |

## Dependency Map

- Shared pattern across all files:
  - Frontmatter (`trigger`, `description`, `tags`, `dependencies`)
  - Execution model (`Goal`, `Inputs`, `Outputs`, `Rules`, `Phases`, `Actions Summary`)
- Operational dependencies are mostly external skills, not local code symbols.
- No direct import/require relationships between files.

## Related Verification Targets

- Structural checks:
  - Presence of required sections: `Goal`, `Inputs`, `Outputs`, `Rules`, `Phases`, `Actions Summary`
  - Frontmatter consistency with trigger and dependency naming
- Behavioral checks:
  - Phase ordering constraints are explicit
  - Output artifacts are concrete and path-specific

## Reference Patterns

- Prompt template style from `.github/prompts/*.prompt.md`
- Existing context/audit docs under `docs/*prompt*context*.md`

## Risks

1. Dependency-name drift between plaintext source and markdown output can break execution assumptions.
2. Output path drift between phases can create dead workflow links.
3. Overly generic rules can reduce determinism in execution agents.

## Notes

- This context map is intentionally file-driven and stops before implementation details.
