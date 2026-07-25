---
author: Hermes Agent
description: Use when creating a README.md file for a project. Generates a comprehensive, well-structured README with sections for overview, installation, usage, API, contributing, license, and more.
license: MIT
metadata:
  hermes:
    tags: [imported, documentation, readme, project-setup]
name: create-readme
tags:
- imported
- documentation
- readme
- project-setup
- scripts
title: Create README
version: 1.0.0
---

# Create README

## Overview

Generate a comprehensive, well-structured README.md file for a project with sections for overview, installation, usage, API, contributing, license, and more.

## When to Use

- Setting up a new project that needs documentation
- Adding a README to an existing project that lacks one
- Standardizing README format across multiple projects
- Onboarding contributors with clear project documentation

## When NOT to Use

- Projects that already have a comprehensive README
- Internal-only projects where README isn't needed
- When documentation lives elsewhere (wiki, docs site)

## Workflow

### Phase 1: Gather Project Information

```bash
# Detect project type and metadata
ls package.json Cargo.toml pyproject.toml go.mod 2>/dev/null

# Extract from existing files
grep -E "name|version|description|license" package.json 2>/dev/null | head -20
```

### Phase 2: Select Template

Based on project type, choose appropriate template:
- **Node.js/TypeScript:** `templates/readme-node.md`
- **Python:** `templates/readme-python.md`
- **Rust:** `templates/readme-rust.md`
- **Go:** `templates/readme-go.md`
- **Generic:** `templates/readme-generic.md`

### Phase 3: Populate & Write

Fill template with gathered information and write to `README.md`.

## Verification Checklist

- [ ] Project name and description present
- [ ] Installation instructions complete
- [ ] Usage examples provided
- [ ] API documentation included (if applicable)
- [ ] Contributing guidelines present
- [ ] License specified
- [ ] Badges relevant and accurate

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## Related Skills

- `documentation-writer` — Full documentation creation
- `writing-clearly-and-concisely` — Prose improvement

## Usage Examples

```bash
# Create README for current project
create-readme

# Specify project type
create-readme --type node

# Use custom template
create-readme --template ./custom-readme.md
```

## Error Handling

- **No project files found:** Warns, uses generic template
- **Permission denied:** Exits with code 2, prints path
- **Template not found:** Falls back to generic template

## Pitfalls

- **Over-templating:** One size doesn't fit all — customize after generation
- **Stale badges:** Badges must reflect actual CI/status — run CI before committing
- **Missing install steps:** Always verify install commands work in fresh environment

## References

- `references/readme-best-practices.md` — README structure guidelines
- `references/badge-guide.md` — Badge selection and maintenance