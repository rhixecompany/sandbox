---
name: suggest-awesome-github-copilot
title: Suggest Awesome GitHub Copilot Content
description: Find GitHub Copilot content (agents, instructions, prompts, or skills) from the awesome-copilot
  repository that add coverage the repo lacks, and flag local duplicates or outdated
  copies.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - web
scripts: []
skills: []
formatter: default
plan: ''
dependencies: []
tags:
  - agents
  - ai-assistant
  - git
  - prompts
  - skills
  - typescript
  - copilot
  - agents
  - ai-assistant
  - git
  - prompts
  - skills
trigger: /suggest-awesome-github-copilot
---

## GoalSuggest [awesome-copilot](https://github.com/github/awesome-copilot) content that fills gaps in the local repository, and flag duplicates or outdated local copies.**Content type** — set `type` to one of: `agents`, `instructions`, `prompts`, or `skills`.## ContextUse when expanding the local Copilot content library with resources from the community awesome-copilot repository. The prompt adapts to the chosen content type.## Inputs- `type` — content type to suggest: `agents | instructions | prompts | skills`- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result matching the prompt's purpose.- A concise verification note when the task benefits from one.## Rules> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Parameters| Parameter | agents | instructions | prompts | skills || ----------- | -------- | -------------- | --------- | -------- || `awesome_dir` | `agents/` | `instructions/` | `.github/prompts/` | `skills/` || `local_dir` | `.github/agents/` | `.github/instructions/` | `.github/prompts/` | `.github/skills/` || `file_pattern` | `*.agent.md` | `*.instructions.md` | `*.prompt.md` | `SKILL.md` || `local_scan` | List all `*.agent.md` in `.github/agents/` | List all `*.instructions.md` in `.github/instructions/` | List all `*.prompt.md` in `.github/prompts/` | List all skill folders in `.github/skills/` || `remote_url` | `https://raw.githubusercontent.com/github/awesome-copilot/main/agents/` | `https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/` | `https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/` | `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/` |## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Determine the `type` (default: `agents` if unspecified).- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Fetch Awesome Content1. Fetch the available content list from [awesome-copilot](https://github.com/github/awesome-copilot/tree/main/`{awesome_dir}`) using `web`.2. For each item, extract its name and description.### Phase 4: Scan Local Content1. Scan the local `{local_dir}` directory for existing content matching `{file_pattern}`.2. Read front matter from each local file to extract `name`, `description`, and other fields.3. Build a comprehensive inventory of existing local content.### Phase 5: Compare and Analyze1. Compare the awesome-copilot list against the local inventory.2. Identify gaps (content not yet present locally).3. For content that exists locally, compare local vs remote versions to detect outdated copies.4. Flag items that are up-to-date vs outdated vs not installed.### Phase 6: Report- Display results in a structured table with columns: Name / Description / Status (✅ up-to-date, ⚠️ outdated, ❌ not installed) / Suggestion Rationale.- Provide clear rationale for each suggestion.- Include links to both the awesome-copilot source and similar local content.## Context Analysis Criteria🔍 **Repository Patterns**:- Programming languages used (e.g., .cs, .js, .py)- Framework indicators (ASP.NET, React, Azure, etc.)- Project types (web apps, APIs, libraries, tools)- Documentation needs (README, specs, ADRs)## Icons Reference- ✅ Already installed and up-to-date- ⚠️ Installed but outdated (update available)- ❌ Not installed in repo## Requirements- Fetch content from awesome-copilot repository using `web` (URL based on `{awesome_dir}`).- Scan local file system for existing content in `{local_dir}`.- Read YAML front matter from local files to extract descriptions.- Compare local with remote to detect outdated versions.- Compare against existing content to avoid duplicates.- Focus on gaps in current library coverage.- Validate that suggestions align with repository's purpose and standards.- Provide clear rationale for each suggestion.- Include links to both awesome-copilot source and similar local content.## Template ReferencesDetailed inline content is above. The individual per-type template dirs under `templates/suggest-awesome-github-copilot-*/` remain for reference.## Verification Checklist- [ ] `type` is one of: agents, instructions, prompts, skills- [ ] Awesome-copilot content fetched successfully- [ ] Local inventory scanned correctly- [ ] Comparison table is complete and accurate- [ ] Outdated items flagged with specific differences- [ ] Empty `{local_dir}` handled gracefully