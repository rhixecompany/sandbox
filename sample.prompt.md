---
name: sample-prompt
title: Sample Prompt Template
description: "Reference template for creating new .prompt.md files. Shows expected structure: frontmatter, skills table, phased workflow, and verification checklist."
trigger: /sample-prompt
tags: [template, reference, meta]
version: "1.0.0"
author: "Hermes Agent"
license: "MIT"
metadata:
  hermes:
    related_skills: [skill-creator, writing-skills, plans-and-specs]
---

# Sample Prompt Template

## Description

This is a reference `.prompt.md` file that demonstrates the expected structure for prompt files in this workspace. Copy this template when creating new prompts.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Authoring new skill files |
| `writing-skills` | Procedural documentation patterns |
| `plans-and-specs` | Phased workflow design |

## Workflow

### Phase 1: Inventory

1. Read the source material (requirements, existing code, or plaintext draft)
2. Identify the goal, scope, and constraints
3. List all prerequisite skills and tools

### Phase 2: Structure & Format

1. Write YAML frontmatter with `name`, `title`, `description`, `trigger`, `tags`
2. Add a `## Skills Required` table
3. Design phased workflow (`Phase 1:Title` with numbered steps)
4. Include verification checklist at the end
5. Apply uniform header levels (H1 for title, H2 for sections, H3 for phases)
6. Use code blocks with language annotations
7. Add verification checklist as `- [ ]` bullets
8. Ensure no placeholder text remains

### Phase 3: Verify

- [ ] Frontmatter has all required fields (`name`, `title`, `description`, `trigger`, `tags`)
- [ ] `Skills Required` table is present and populated
- [ ] Phases are sequentially numbered and have clear goals
- [ ] Verification checklist is at the end of the file
- [ ] No `[Add ... here]` placeholder text remains
- [ ] File uses `.prompt.md` extension matching trigger
- [ ] Trigger matches filename stem (e.g., `trigger: /my-task` → `my-task.prompt.md`) (current: `/sample-prompt` → `sample-prompt.md`)

## Key Patterns

**Frontmatter first:**
```yaml
---
name: my-prompt
title: My Prompt Title
description: "What this prompt does."
trigger: /my-prompt
tags: [domain, workflow-type]
---
```
- **Trigger match:** The `trigger:` value should match the filename stem
- **Phased structure:** Use `Phase N: Title` with numbered steps
- **Verification checklist:** Always end with acceptance criteria

## Example Output

After running this template, the resulting file should have:
- Valid YAML frontmatter
- Skills table
- 3-6 phases with clear goals
- Verification checklist
- No placeholder text
