---
author: Hermes Agent
description: Use when creating a new skill from scratch — provides the standard SKILL.md
  structure with frontmatter, sections, and format guidelines. Copy this file and
  fill in the content.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: template
tags:
- skill-creation
- scaffolding
- template
- reference
title: Skill Template
version: 1.1.0

---
# Skill Template

## Overview

This is the **reference template** for creating new skills. It demonstrates the standard structure, required sections, and formatting conventions. Copy this file to a new skill directory and replace the example content.

## When to Use

- Creating a new skill from scratch
- Adding a new process, pattern, or reference guide
- Standardizing skill format across a team

## When NOT to Use

- As an executable skill (this is a template, not a workflow)
- For evaluating skill quality (use skill-judge)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Full TDD-based skill creation process |
| `skill-judge` | Evaluate skill quality before deployment |
| `writing-skills` | Documentation best practices |

## Standard SKILL.md Structure

### Frontmatter (Required)

Every SKILL.md must start with YAML frontmatter:

```yaml
---
name: skill-name
title: Human-Readable Title
description: "Use when [specific triggering conditions] — keep under 500 chars, start with 'Use when...'"
version: 1.0.0
author: Your Name
license: MIT
tags: [category, tag1, tag2]
metadata:
  hermes:
    tags: [category, tag1, tag2]
    related_skills: [related-skill-1, related-skill-2]
---
```

**Required fields:**
- `name` — lowercase, hyphens only (e.g., `my-skill`)
- `title` — human-readable title
- `description` — starts with "Use when...", under 500 chars
- `version` — semantic version (1.0.0)
- `author` — your name or handle
- `license` — MIT recommended
- `tags` — array of category tags

### Body Sections (Required)

#### 1. Overview (1-2 sentences)
What this skill does and why it exists.

#### 2. When to Use
Specific triggers, symptoms, or use cases. Be precise — this is how the agent decides whether to load the skill.

#### 3. When NOT to Use
Clarify boundaries. What does this skill NOT cover?

#### 4. Skills Required (table)
| Skill | Purpose |
|-------|---------|
| `skill-name` | What it's used for |

#### 5. Workflow (phased)
Break the process into clear phases:

**Phase 1: [Name]**
- Step 1
- Step 2

**Phase 2: [Name]**
- Step 1
- Step 2

#### 6. Best Practices
Numbered list of 5-10 best practices.

#### 7. Pitfalls
Common mistakes and how to avoid them.

#### 8. Verification Checklist
- [ ] Checklist item 1
- [ ] Checklist item 2

### Optional Sections

- **Quick Reference** — Tables or bullets for scanning
- **Examples** — Before/after code comparisons
- **Real-World Impact** — Concrete results/benefits
- **References** — Links to reference files, templates, scripts

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| File | `SKILL.md` (uppercase) | `SKILL.md` |
| Directory | Match skill name | `my-skill/SKILL.md` |
| name field | lowercase, hyphens | `my-skill` |
| Description | Start with "Use when..." | "Use when converting..." |

## Quality Standards

A well-written skill should score ≥70/100 on skill-judge:

| Dimension | Target | Key Criteria |
|-----------|--------|--------------|
| Frontmatter | 17-20 | All required fields present |
| Structure | 16-20 | Skills Required, phases, pitfalls, verification |
| Content | 16-20 | Concrete examples, no placeholder text |
| DRY | 16-20 | <250 lines, no duplication |
| References | 12-20 | Verified reference files |

## Tips

1. **Keep descriptions under 500 characters** — concise triggers load faster
2. **Use flowcharts for decision trees** — Mermaid diagrams help agents navigate complex logic
3. **Include before/after code comparisons** — concrete examples beat abstract descriptions
4. **Cross-reference other skills** — use `**REQUIRED SUB-SKILL:** skill-name` pattern
5. **Store long content in references/** — keep SKILL.md under 250 lines
6. **Add real-world impact** — concrete results help agents understand value
7. **Test with skill-judge** — validate quality before publishing

## Example Minimal Skill

```markdown
---
name: my-example
title: My Example Skill
description: "Use when you need to demonstrate a minimal skill structure."
version: 1.0.0
author: Example Author
license: MIT
tags: [example, template]
---

# My Example Skill

## Overview
A minimal example of a well-structured skill.

## When to Use
- Demonstrating skill structure
- Testing skill loading

## Workflow

### Phase 1: Setup
1. Verify prerequisites

### Phase 2: Execute
1. Perform the main action

### Phase 3: Verify
1. Check the output


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist
- [ ] Output matches expected result
```

## See Also

- `writing-skills` skill for detailed TDD-based skill creation process
- `skill-judge` skill for evaluating skill quality
- `skill-creator` skill for authoring, scaffolding, and validating SKILL.md files
