---
name: suggest-awesome-github-copilot-skills-version-comparison-process
title: Suggest Awesome Copilot Skills — Version Comparison Process
description: Procedure for detecting outdated local skills vs awesome-copilot
version: 1.0.0
tags: [template, suggest-awesome-github-copilot-skills]
---

## Version Comparison Process

1. For each local skill folder, construct the raw GitHub URL to fetch the remote `SKILL.md`:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/<skill-name>/SKILL.md`
2. Fetch the remote version using the `#fetch` tool
3. Compare entire file content (including front matter and body)
4. Identify specific differences:
   - **Front matter changes** (name, description)
   - **Instruction updates** (guidelines, examples, best practices)
   - **Bundled asset changes** (new, removed, or modified assets)
5. Document key differences for outdated skills
6. Calculate similarity to determine if update is needed
