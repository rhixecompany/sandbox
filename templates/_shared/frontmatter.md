# Shared Templates — Frontmatter Patterns

Reusable YAML frontmatter blocks for `.prompt.md` files.

## Minimal Hermes Prompt Frontmatter

```yaml
---
trigger: /<prompt-name>
name: <prompt-name>
title: "<Human-Readable Title>"
description: >-
  One-paragraph description of what this prompt does.
version: 1.0.0
tags: [hermes, <category>]
dependencies:
  - skill:<skill-name>
skills:
  - <skill-name>
---
```

## Full Frontmatter with All Fields

```yaml
---
trigger: /<prompt-name>
name: <prompt-name>
title: "<Human-Readable Title>"
description: >-
  One-paragraph description of what this prompt does.
version: 1.0.0
author: "<Author>"
license: MIT
tags: [hermes, copilot, opencode, <category>]
dependencies:
  - skill:<skill-name-1>
  - skill:<skill-name-2>
skills:
  - <skill-name-1> — Description of purpose
  - <skill-name-2> — Description of purpose
metadata:
  hermes:
    tags: [<category>]
    related_skills: [<skill-name-1>, <skill-name-2>]
---
```
