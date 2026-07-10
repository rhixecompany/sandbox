---
name: suggest-awesome-github-copilot-skills-update-handling
title: Suggest Awesome Copilot Skills — Update Handling
description: How to handle outdated skills when the user requests an update
version: 1.0.0
tags: [template, suggest-awesome-github-copilot-skills]
---

## Update Handling

When outdated skills are identified:

1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local skill folder with remote version
5. Preserve folder location in `.github/skills/` directory
6. Ensure all bundled assets are downloaded alongside the updated `SKILL.md`
