# Dev Init Constraint Line Findings

Date: 2026-05-27
Purpose: Line-level evidence map for constraint checklist validation.

## Findings by Prompt

### [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md)

- Metadata anchors: [title](../Prompts/dev-init.prompts.md#L2), [trigger](../Prompts/dev-init.prompts.md#L3), [tags](../Prompts/dev-init.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/dev-init.prompts.md#L11), [Goal](../Prompts/dev-init.prompts.md#L20), [Deliverables](../Prompts/dev-init.prompts.md#L39)
- Constraint anchors: [Template dependency verification](../Prompts/dev-init.prompts.md#L50), [Constraint preservation audit](../Prompts/dev-init.prompts.md#L64), [Output validation](../Prompts/dev-init.prompts.md#L73), [Idempotent execution](../Prompts/dev-init.prompts.md#L81)
- Finding: Core constraints present and structurally intact.

### [Prompts/bash-scripts-fix.prompts.md](../Prompts/bash-scripts-fix.prompts.md)

- Metadata anchors: [title](../Prompts/bash-scripts-fix.prompts.md#L2), [trigger](../Prompts/bash-scripts-fix.prompts.md#L3), [tags](../Prompts/bash-scripts-fix.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/bash-scripts-fix.prompts.md#L11), [Skills Required](../Prompts/bash-scripts-fix.prompts.md#L31)
- Constraint anchors: [Bash canonical policy](../Prompts/bash-scripts-fix.prompts.md#L17), [Seed exception policy](../Prompts/bash-scripts-fix.prompts.md#L19), [Safety section](../Prompts/bash-scripts-fix.prompts.md#L97)
- Finding: Migration and safety constraints present with explicit exception handling.

### [Prompts/agents-fix.prompts.md](../Prompts/agents-fix.prompts.md)

- Metadata anchors: [title](../Prompts/agents-fix.prompts.md#L2), [trigger](../Prompts/agents-fix.prompts.md#L3), [tags](../Prompts/agents-fix.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/agents-fix.prompts.md#L11), [Phase 1](../Prompts/agents-fix.prompts.md#L24), [Phase 2](../Prompts/agents-fix.prompts.md#L37), [Phase 3](../Prompts/agents-fix.prompts.md#L46)
- Constraint anchors: [Safety section](../Prompts/agents-fix.prompts.md#L57), [Critical access validation](../Prompts/agents-fix.prompts.md#L59)
- Finding: Phase and safety constraints present.

### [Prompts/commands-fix.prompts.md](../Prompts/commands-fix.prompts.md)

- Metadata anchors: [title](../Prompts/commands-fix.prompts.md#L2), [trigger](../Prompts/commands-fix.prompts.md#L3), [tags](../Prompts/commands-fix.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/commands-fix.prompts.md#L11), [Phase 1](../Prompts/commands-fix.prompts.md#L24), [Phase 2](../Prompts/commands-fix.prompts.md#L37), [Phase 3](../Prompts/commands-fix.prompts.md#L46)
- Constraint anchors: [Safety section](../Prompts/commands-fix.prompts.md#L57), [Critical backward compatibility](../Prompts/commands-fix.prompts.md#L59)
- Finding: Workflow and safety constraints present.

### [Prompts/general.prompts.md](../Prompts/general.prompts.md)

- Metadata anchors: [title](../Prompts/general.prompts.md#L2), [trigger](../Prompts/general.prompts.md#L3), [tags](../Prompts/general.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/general.prompts.md#L11), [Skills Required](../Prompts/general.prompts.md#L15)
- Constraint anchors: [Safety section](../Prompts/general.prompts.md#L53), [Critical credential prevention](../Prompts/general.prompts.md#L55)
- Finding: Core safety and workflow constraints present.

### [Prompts/repo.prompts.md](../Prompts/repo.prompts.md)

- Metadata anchors: [title](../Prompts/repo.prompts.md#L2), [trigger](../Prompts/repo.prompts.md#L3), [tags](../Prompts/repo.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/repo.prompts.md#L11), [Phase 1](../Prompts/repo.prompts.md#L29), [Phase 2](../Prompts/repo.prompts.md#L41), [Phase 3](../Prompts/repo.prompts.md#L53), [Phase 4](../Prompts/repo.prompts.md#L63)
- Constraint anchors: [Safety section](../Prompts/repo.prompts.md#L75), [Critical backup and rollback protocol](../Prompts/repo.prompts.md#L77)
- Finding: Migration controls and safety constraints present.

### [Prompts/skills-fix.prompts.md](../Prompts/skills-fix.prompts.md)

- Metadata anchors: [title](../Prompts/skills-fix.prompts.md#L2), [trigger](../Prompts/skills-fix.prompts.md#L3), [tags](../Prompts/skills-fix.prompts.md#L4)
- Scope anchors: [Overview](../Prompts/skills-fix.prompts.md#L11), [Phase 1](../Prompts/skills-fix.prompts.md#L24), [Phase 2](../Prompts/skills-fix.prompts.md#L38), [Phase 3](../Prompts/skills-fix.prompts.md#L47)
- Constraint anchors: [Safety section](../Prompts/skills-fix.prompts.md#L58), [Critical active skill protection](../Prompts/skills-fix.prompts.md#L60)
- Finding: Skills workflow constraints and safety controls present.

## Checklist Mapping

Use this file as evidence when checking items in [docs/dev-init-constraint-preservation-checklist.md](dev-init-constraint-preservation-checklist.md).
