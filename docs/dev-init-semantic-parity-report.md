# Dev Init Semantic Parity Report

Date: 2026-05-27
Scope: Semantic intent retention from Prompts plaintext sources to markdown targets.

## Method

1. Read each source file in Prompts/*.txt.
2. Identify core intent tokens per source: scope, phases, artifacts, and constraints.
3. Verify matching intent appears in the target Prompts/*.md.
4. Mark parity as Pass when source intent is preserved, even if markdown expands detail.

## Pair Results

| Source | Target | Key source intent retained | Evidence | Result |
|---|---|---|---|---|
| [Prompts/dev-init.prompts.txt](../Prompts/dev-init.prompts.txt) | [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md) | brainstorming plus plan-specs, convert plaintext workflow, context-map, boost-prompt, safety-review, update-plan, prompt-builder, deliverable planning | [Prompts/dev-init.prompts.md#L17](../Prompts/dev-init.prompts.md#L17), [Prompts/dev-init.prompts.md#L30](../Prompts/dev-init.prompts.md#L30), [Prompts/dev-init.prompts.md#L33](../Prompts/dev-init.prompts.md#L33), [Prompts/dev-init.prompts.md#L34](../Prompts/dev-init.prompts.md#L34), [Prompts/dev-init.prompts.md#L35](../Prompts/dev-init.prompts.md#L35), [Prompts/dev-init.prompts.md#L36](../Prompts/dev-init.prompts.md#L36), [Prompts/dev-init.prompts.md#L37](../Prompts/dev-init.prompts.md#L37), [Prompts/dev-init.prompts.md#L39](../Prompts/dev-init.prompts.md#L39) | Pass |
| [Prompts/bash-scripts-fix.prompts.txt](../Prompts/bash-scripts-fix.prompts.txt) | [Prompts/bash-scripts-fix.prompts.md](../Prompts/bash-scripts-fix.prompts.md) | script catalog, phase-based implementation, bash consolidation rules, db seed exception, ts-morph planning, safety controls | [Prompts/bash-scripts-fix.prompts.md#L40](../Prompts/bash-scripts-fix.prompts.md#L40), [Prompts/bash-scripts-fix.prompts.md#L58](../Prompts/bash-scripts-fix.prompts.md#L58), [Prompts/bash-scripts-fix.prompts.md#L79](../Prompts/bash-scripts-fix.prompts.md#L79), [Prompts/bash-scripts-fix.prompts.md#L17](../Prompts/bash-scripts-fix.prompts.md#L17), [Prompts/bash-scripts-fix.prompts.md#L19](../Prompts/bash-scripts-fix.prompts.md#L19), [Prompts/bash-scripts-fix.prompts.md#L70](../Prompts/bash-scripts-fix.prompts.md#L70), [Prompts/bash-scripts-fix.prompts.md#L97](../Prompts/bash-scripts-fix.prompts.md#L97) | Pass |
| [Prompts/agents-fix.prompts.txt](../Prompts/agents-fix.prompts.txt) | [Prompts/agents-fix.prompts.md](../Prompts/agents-fix.prompts.md) | migrate opencode agents, phase audit, phase plan, phase execute, docs output locations | [Prompts/agents-fix.prompts.md#L9](../Prompts/agents-fix.prompts.md#L9), [Prompts/agents-fix.prompts.md#L24](../Prompts/agents-fix.prompts.md#L24), [Prompts/agents-fix.prompts.md#L35](../Prompts/agents-fix.prompts.md#L35), [Prompts/agents-fix.prompts.md#L37](../Prompts/agents-fix.prompts.md#L37), [Prompts/agents-fix.prompts.md#L44](../Prompts/agents-fix.prompts.md#L44), [Prompts/agents-fix.prompts.md#L46](../Prompts/agents-fix.prompts.md#L46), [Prompts/agents-fix.prompts.md#L51](../Prompts/agents-fix.prompts.md#L51) | Pass |
| [Prompts/commands-fix.prompts.txt](../Prompts/commands-fix.prompts.txt) | [Prompts/commands-fix.prompts.md](../Prompts/commands-fix.prompts.md) | migrate opencode commands, phase audit, phase plan, phase execute, docs output locations | [Prompts/commands-fix.prompts.md#L9](../Prompts/commands-fix.prompts.md#L9), [Prompts/commands-fix.prompts.md#L24](../Prompts/commands-fix.prompts.md#L24), [Prompts/commands-fix.prompts.md#L35](../Prompts/commands-fix.prompts.md#L35), [Prompts/commands-fix.prompts.md#L37](../Prompts/commands-fix.prompts.md#L37), [Prompts/commands-fix.prompts.md#L44](../Prompts/commands-fix.prompts.md#L44), [Prompts/commands-fix.prompts.md#L46](../Prompts/commands-fix.prompts.md#L46), [Prompts/commands-fix.prompts.md#L51](../Prompts/commands-fix.prompts.md#L51) | Pass |
| [Prompts/general.prompts.txt](../Prompts/general.prompts.txt) | [Prompts/general.prompts.md](../Prompts/general.prompts.md) | Context7 and Sequential Thinking focus, GitHub and Atlassian automation, command execution workflow | [Prompts/general.prompts.md#L29](../Prompts/general.prompts.md#L29), [Prompts/general.prompts.md#L30](../Prompts/general.prompts.md#L30), [Prompts/general.prompts.md#L36](../Prompts/general.prompts.md#L36), [Prompts/general.prompts.md#L39](../Prompts/general.prompts.md#L39) | Pass |
| [Prompts/repo.prompts.txt](../Prompts/repo.prompts.txt) | [Prompts/repo.prompts.md](../Prompts/repo.prompts.md) | project inventory and triage, merge plan creation, execution and verification phases | [Prompts/repo.prompts.md#L29](../Prompts/repo.prompts.md#L29), [Prompts/repo.prompts.md#L38](../Prompts/repo.prompts.md#L38), [Prompts/repo.prompts.md#L41](../Prompts/repo.prompts.md#L41), [Prompts/repo.prompts.md#L51](../Prompts/repo.prompts.md#L51), [Prompts/repo.prompts.md#L53](../Prompts/repo.prompts.md#L53), [Prompts/repo.prompts.md#L58](../Prompts/repo.prompts.md#L58), [Prompts/repo.prompts.md#L63](../Prompts/repo.prompts.md#L63), [Prompts/repo.prompts.md#L68](../Prompts/repo.prompts.md#L68) | Pass |
| [Prompts/skills-fix.prompts.txt](../Prompts/skills-fix.prompts.txt) | [Prompts/skills-fix.prompts.md](../Prompts/skills-fix.prompts.md) | hermes skills inventory, audit and debug, plan generation, execution prompt | [Prompts/skills-fix.prompts.md#L29](../Prompts/skills-fix.prompts.md#L29), [Prompts/skills-fix.prompts.md#L30](../Prompts/skills-fix.prompts.md#L30), [Prompts/skills-fix.prompts.md#L36](../Prompts/skills-fix.prompts.md#L36), [Prompts/skills-fix.prompts.md#L38](../Prompts/skills-fix.prompts.md#L38), [Prompts/skills-fix.prompts.md#L45](../Prompts/skills-fix.prompts.md#L45), [Prompts/skills-fix.prompts.md#L47](../Prompts/skills-fix.prompts.md#L47), [Prompts/skills-fix.prompts.md#L52](../Prompts/skills-fix.prompts.md#L52) | Pass |

## Conclusion

Semantic parity status: Pass for 7 of 7 source-target pairs.

Observed transformation pattern:
- Plaintext shorthand was expanded into structured markdown workflows.
- No core source objective or phase contract was dropped in the inspected set.

## Related

- [docs/dev-init-conversion-pass-report.md](dev-init-conversion-pass-report.md)
- [docs/dev-init-pilot-conversion-verification.md](dev-init-pilot-conversion-verification.md)
- [docs/dev-init-constraint-preservation-checklist.md](dev-init-constraint-preservation-checklist.md)
