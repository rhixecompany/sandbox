# Frontmatter Template Reference

## Standard Skill Frontmatter

```yaml
name: skill-name
title: Human Readable Title
description: "Use when [specific triggering conditions] — keep under 500 chars, start with 'Use when...'"
version: 1.0.0
author: Your Name
license: MIT
tags: [category, tag1, tag2]
metadata:
  hermes:
    tags: [category, tag1, tag2]
    related_skills: [skill-1, skill-2]
```

## Field Requirements

| Field | Required | Format | Example |
|-------|----------|--------|---------|
| `name` | Yes | lowercase, hyphens only | `my-skill` |
| `title` | Yes | Human-readable | `My Skill Title` |
| `description` | Yes | ≤500 chars, starts "Use when..." | `Use when debugging memory leaks in Node.js` |
| `version` | Yes | Semantic version | `1.0.0` |
| `author` | Yes | Name or handle | `Hermes Agent` |
| `license` | Yes | SPDX identifier | `MIT` |
| `tags` | Yes | Array of strings | `[debugging, nodejs, memory]` |
| `metadata.hermes.tags` | Yes | Same as tags | `[debugging, nodejs, memory]` |
| `metadata.hermes.related_skills` | No | Array of skill names | `[systematic-debugging, node-inspect-debugger]` |

## Description Field Rules

1. **Must start with "Use when..."** — describes triggering conditions, not what the skill does
2. **≤500 characters** — keep concise for search optimization
3. **Third person** — injected into system prompt
4. **Technology-agnostic triggers** unless skill is tech-specific
5. **No workflow summary** — the skill body contains the process

**✅ Good:** `Use when tests have race conditions, timing dependencies, or pass/fail inconsistently`
**❌ Bad:** `Use for async testing — write test first, watch it fail, write minimal code, refactor`
**❌ Bad:** `I can help you with async tests when they're flaky`

## Tags Best Practices

- Use 3-5 tags per skill
- Use category tag + specific tags
- Category tags: `debugging`, `development`, `devops`, `creative`, `mlops`, `research`, `qa`, `planning`, `productivity`, `software-development`
- Specific tags: technology, tool, technique, or problem type