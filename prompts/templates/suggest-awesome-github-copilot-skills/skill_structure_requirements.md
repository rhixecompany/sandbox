---
name: suggest-awesome-github-copilot-skills-skill-structure-requirements
title: Suggest Awesome Copilot Skills — Skill Structure Requirements
description: Agent Skills folder/structure spec referenced by the prompt
version: 1.0.0
tags: [template, suggest-awesome-github-copilot-skills]
---

## Skill Structure Requirements

Based on the Agent Skills specification, each skill is a folder containing:

- **`SKILL.md`**: Main instruction file with front matter (`name`, `description`) and detailed instructions
- **Optional bundled assets**: Scripts, templates, reference data, and other files referenced from `SKILL.md`
- **Folder naming**: Lowercase with hyphens (e.g., `azure-deployment-preflight`)
- **Name matching**: The `name` field in `SKILL.md` front matter must match the folder name
