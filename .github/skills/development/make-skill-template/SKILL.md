---
author: Hermes Agent
description: Scaffold and create new Agent Skills with proper SKILL.md frontmatter, directory structure, and bundled resources. Use when asked to create a skill, make a new skill, scaffold a skill, or when building specialized AI capabilities with bundled scripts, references, assets, or templates.
license: MIT
metadata:
  hermes:
    tags: [imported, scaffolding, templates, skill-authoring, developer-tools]
name: make-skill-template
tags:
- imported
- scaffolding
- templates
- skill-authoring
- developer-tools
- scripts
title: Make Skill Template
version: 1.0.0
---

# Make Skill Template

## Overview

A meta-skill for creating new Agent Skills. Use this skill when you need to scaffold a new skill folder, generate a SKILL.md file, or help users understand the Agent Skills specification.

## When to Use This Skill

- User asks to "create a skill", "make a new skill", or "scaffold a skill"
- User wants to add a specialized AI capability with bundled resources or scripts
- User needs help structuring a skill with references, templates, or assets
- User wants to validate an existing skill structure against the official spec
- User wants to duplicate this template as a starting point for a new skill

## When NOT to Use

- Evaluating skill quality (use `skill-judge`)
- Installing community skills (use `hermes-skills`)
- Managing skills across profiles (use `skills`)

## Prerequisites

- Understanding of what the skill should accomplish
- A clear, keyword-rich description of capabilities and triggers
- Knowledge of any bundled resources needed (scripts, references, assets, templates)

## Workflow

### Phase 1: Create the Skill Directory

Create a new folder with a lowercase, hyphenated name:

```
skills/<skill-name>/
└── SKILL.md          # Required
```

### Phase 2: Generate SKILL.md with Frontmatter

Every skill requires YAML frontmatter with `name` and `description`:

```yaml
---
name: <skill-name>
description: "<What it does>. Use when <specific triggers, scenarios, keywords users might say>."
---
```

#### Frontmatter Field Requirements

| Field | Required | Constraints |
| --- | --- | --- |
| `name` | **Yes** | 1-64 chars, lowercase letters/numbers/hyphens only, must match folder name |
| `description` | **Yes** | 1-1024 chars, must describe WHAT it does AND WHEN to use it |
| `license` | No | License name or reference to bundled LICENSE.txt |
| `compatibility` | No | 1-500 chars, environment requirements if needed |
| `metadata` | No | Key-value pairs for additional properties |
| `allowed-tools` | No | Space-delimited list of pre-approved tools (experimental) |

#### Description Best Practices

**CRITICAL**: The `description` is the PRIMARY mechanism for automatic skill discovery. Include:

1. **WHAT** the skill does (capabilities)
2. **WHEN** to use it (triggers, scenarios, file types)
3. **Keywords** users might mention in prompts

**Good example:**
```yaml
description: "Toolkit for testing local web applications using Playwright. Use when asked to verify frontend functionality, debug UI behavior, capture browser screenshots, or view browser console logs. Supports Chrome, Firefox, and WebKit."
```

**Poor example:**
```yaml
description: "Web testing helpers"
```

### Phase 3: Write the Skill Body

After the frontmatter, add markdown instructions. Recommended sections:

| Section | Purpose |
| --- | --- |
| `# Title` | Brief overview |
| `## When to Use This Skill` | Reinforces description triggers |
| `## Prerequisites` | Required tools, dependencies |
| `## Step-by-Step Workflows` | Numbered steps for tasks |
| `## Troubleshooting` | Common issues and solutions |
| `## References` | Links to bundled docs |

### Phase 4: Add Optional Directories (If Needed)

| Folder | Purpose | When to Use |
| --- | --- | --- |
| `scripts/` | Executable code (Python, Bash, JS) | Automation that performs operations |
| `references/` | Documentation agent reads | API references, schemas, guides |
| `assets/` | Static files used AS-IS | Images, fonts, templates |
| `templates/` | Starter code agent modifies | Scaffolds to extend |

### Phase 5: Validate

Run validation to ensure structure compliance:

```bash
npm run skill:validate
```

## Verification Checklist

- [ ] Folder name is lowercase with hyphens
- [ ] `name` field matches folder name exactly
- [ ] `description` is 10-1024 characters
- [ ] `description` explains WHAT and WHEN
- [ ] `description` is wrapped in single quotes
- [ ] Body content is under 500 lines
- [ ] Bundled assets are under 5MB each
- [ ] All referenced directories exist
- [ ] No placeholder text remains
- [ ] Validation passes without errors

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |
| `skill-judge` | Validate skill quality |

## Related Skills

- `skill-creator` — Author in-repo SKILL.md files
- `skill-judge` — Evaluate skill quality
- `writing-skills` — Create clear skill prose

## Quick Start: Duplicate This Template

1. Copy the `make-skill-template/` folder
2. Rename to your skill name (lowercase, hyphens)
3. Update `SKILL.md`:
   - Change `name:` to match folder name
   - Write a keyword-rich `description:`
   - Replace body content with your instructions
4. Add bundled resources as needed
5. Validate with `npm run skill:validate`

## Usage Examples

```bash
# Scaffold a new skill from this template
make-skill-template --name my-new-skill --description "Does X when Y"

# Validate an existing skill
make-skill-template --validate skills/my-skill/

# List all skill directories
make-skill-template --list
```

## Error Handling

- **Invalid name format:** Exits with code 1, prints specific validation error
- **Folder name mismatch:** Exits with code 2, shows expected vs actual
- **Description too short:** Warns, suggests keywords to add
- **Missing directories:** Creates empty directories automatically

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Skill not discovered | Improve description with more keywords and triggers |
| Validation fails on name | Ensure lowercase, no consecutive hyphens, matches folder |
| Description too short | Add capabilities, triggers, and keywords |
| Assets not found | Use relative paths from skill root |

## Pitfalls

- **Too-vague descriptions:** A generic description like "Web testing helpers" will not be discovered. Always include both WHAT and WHEN with specific trigger keywords.
- **Case-sensitive folder name:** Skills folder name must match the `name:` field exactly, be lowercase, and use hyphens only. Mismatches cause silent discovery failure.
- **Over-bloated skills:** Keep body content under 500 lines and bundled assets under 5MB each. Excessive length causes context window pressure during execution.
- **Missing resource directories:** If you reference files in `references/` or `templates/` from the skill body, ensure those directories exist. Broken relative paths degrade agent performance.
- **No validation step:** Always validate the new skill with `npm run skill:validate` or a manual checklist check after creation to catch structural issues early.

## References

- Agent Skills official spec: <https://agentskills.io/specification>
- `references/skill-spec.md` — Full specification details
- `references/validation-rules.md` — Validation checklist