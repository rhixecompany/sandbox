---
name: suggest-awesome-github-copilot-skills-process
title: Suggest Awesome Copilot Skills — Process
description: Core two-step process for the suggest-awesome-github-copilot-skills prompt
version: 1.0.0
tags: [template, suggest-awesome-github-copilot-skills]
---

## Process

1. **Fetch Available Skills** — Extract the skills list and descriptions from the
   `github/awesome-copilot` repository (`skills/` directory). Enumerate each skill
   with its name, description, and any bundled assets.
2. **Scan Local Skills** — Discover existing skill folders in `.github/skills/`
   (or the repository's equivalent skill location). Read each `SKILL.md` front
   matter to build a local inventory of names and descriptions.

> Full discovery procedure: `templates/suggest-awesome-github-copilot-skills/local_skills_discovery_pr.md`
