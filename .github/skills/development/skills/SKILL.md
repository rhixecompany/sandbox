---
author: Hermes Agent
description: Use when discovering, installing, updating, configuring, or managing
  Hermes skills. Use during skill library maintenance, profile management, or when
  working with the skills CLI.
license: MIT
metadata:
  hermes:
    related_skills:
    - hermes-skills
    - skill-creator
    - skill-judge
    - hermes-setup
    tags:
    - skills
    - management
    - configuration
name: skills
tags:
- skills
- management
- configuration
- hermes
title: Skills Management
version: 1.0.0

---

# Skills Management

## Overview

Discover, install, update, configure, and manage Hermes skills across profiles. This skill provides workflows for maintaining the skill library quality and organization.

## When to Use

- Installing new skills from the community or custom sources
- Updating existing skills to latest versions
- Auditing skill library quality with skill-judge
- Managing skills across multiple Hermes profiles
- Creating or modifying skills (use skill-creator for authoring)
- Troubleshooting skill loading or configuration issues

## When NOT to Use

- Writing new skill content (use skill-creator)
- Evaluating skill quality (use skill-judge)
- Setting up Hermes from scratch (use hermes-setup)

## Workflow

### Phase 1: Discover Skills

```bash
# List all installed skills by source
hermes skills list --source local
hermes skills list --source community
hermes skills list --source all

# Search for skills by name or description
hermes skills list | grep -i "keyword"

# View skill details
hermes skills info <skill-name>
```

### Phase 2: Install & Update

```bash
# Install a skill from community
hermes skills install <skill-name>

# Update a specific skill
hermes skills update <skill-name>

# Update all skills
hermes skills update --all

# Install from a specific source
hermes skills install <skill-name> --source <path-or-url>
```

### Phase 3: Configure Per-Profile

Skills can be profile-specific:
```bash
# List profiles
hermes profiles list

# Switch profile
hermes profiles switch <profile-name>

# Skills are stored per-profile at:
# ~/.hermes/profiles/<profile>/skills/
```

### Phase 4: Quality Audit

1. Run skill-judge on all local skills:
   ```bash
   for skill in $(hermes skills list --source local); do
     skill-judge "$skill"
   done
   ```
2. Review scores and prioritize fixes
3. Patch failing skills with skill_manage(action='patch')
4. Re-audit patched skills to confirm improvement

## Best Practices

1. **Keep skills focused** — Each skill should do one thing well
2. **Version your skills** — Use semantic versioning in frontmatter
3. **Tag consistently** — Use metadata.tags for discoverability
4. **Reference related skills** — Use related_skills in frontmatter
5. **Store long content in references/** — Keep SKILL.md under 250 lines
6. **Test before deploying** — Use skill-judge to validate quality

## Verification Checklist

- [ ] All required skills installed and loading correctly
- [ ] Skill versions are current
- [ ] No duplicate skills across profiles
- [ ] All skills pass skill-judge audit (score ≥70)
- [ ] References are valid and accessible
- [ ] No orphaned skill directories

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-skills` | Core skills CLI reference |
| `skill-creator` | Author new skills |
| `skill-judge` | Evaluate skill quality |
| `hermes-setup` | Initial Hermes configuration |

## Pitfalls

- **Profile confusion:** Skills installed in one profile aren't visible in another — check active profile
- **Orphaned references:** Moving or deleting skills breaks cross-references — update related_skills when restructuring
- **Version drift:** Community skills update independently — pin versions for stability
- **Over-installing:** More skills ≠ better — each skill adds token overhead to context loading
- **Naming collisions:** Similar skill names across sources can cause confusion — use full qualified names
