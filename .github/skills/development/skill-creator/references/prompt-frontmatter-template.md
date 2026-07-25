---
# Canonical prompt frontmatter template for repository prompts
# Use YAML frontmatter with fields that are both human- and machine-friendly.
# Required fields: name, trigger, title, description, author, created, version, compatibility, tags
# Optional fields: dependencies, mcp_servers, backup_before_edit, notes

name: short-identifier
trigger: /command-trigger
title: Human-friendly title
description: >-
  Longer human description suitable for both readers and LLM ingestion.
author: Alexa
created: 2026-05-25T00:00:00Z
version: 1.0.0
compatibility:
  - hermes
  - copilot
  - opencode
tags:
  - one
  - two
dependencies:
  skills:
    - skill-name
  subagents:
    - subagent-name
mcp_servers: []
backup_before_edit: true
notes: |
  Any special notes about running environment, required file paths, or non-sensitive caveats.
---

Guidance:
- Keep the frontmatter small and machine-parseable. Put longer human-readable context in the body below.
- Avoid absolute system secrets or API keys in frontmatter; redact them if present.
- When converting existing prompts, prefer migrating the original trigger and description to the new fields rather than inventing new ones.
- Use `compatibility` to indicate which runners the prompt is safe for; tools can filter by this field.
