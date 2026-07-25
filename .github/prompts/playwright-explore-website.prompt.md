---
name: playwright-explore-website
title: Playwright Explore Website
description: Explore a website with Playwright MCP, document core flows, and propose tests from
  the findings.
version: 1.0.0
license: MIT
author: Alexa
toolsets:
  - file
  - terminal
  - web
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - mcp
  - ml
  - playwright
  - prompts
  - specification
  - testing
  - typescript
  - mcp
  - ml
  - playwright
  - prompts
  - specification
  - testing
  - typescript
trigger: /playwright-explore-website
compatibility: null
created: '2026-05-25T10:50:21.952313Z'
mcp_generator: None
skill_stub: true
---

## GoalExplore a website with Playwright MCP, document core flows, and propose tests from the findings.## ContextUse when you need to playwright website exploration for the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## DescriptionExplore a website with Playwright MCP, document core flows, and propose tests from the findings.## Context- Use the provided URL; if none is provided, ask the user for one.- Focus on the main user journeys rather than exhaustive coverage.- Record locators and observed outcomes while exploring.## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- `webapp-testing` — navigate and exercise the live site with browser automation- `verification-before-completion` — confirm the exploration evidence before summarizing- `systematic-debugging` — trace UI behavior and interaction issues cleanly## Subagents| Subagent | Role | Phase || --- | --- | --- || `@explorer` | Navigates and exercises the site | Phase 2 || `@scribe` | Records locators, flows, and outcomes | Phase 3 || `@tester` | Turns exploration findings into test ideas | Phase 4 |## Personas### @explorerA careful site explorer who finds the main flows without over-driving the app.### @scribeA recorder who writes down locators, outcomes, and noteworthy UI behavior.### @testerA test-minded reviewer who turns exploration notes into concrete test cases.## Rules1. Navigate to the provided URL before exploring.2. If no URL is provided, ask for one instead of guessing.3. Inspect 3 to 5 core flows only.4. Capture useful locators and expected outcomes.5. Close the browser context when finished.6. Provide a concise summary and test ideas.## Phases> ### Phase 1: Start and orient>> **Goal:** load the site and identify the main areas worth exploring.> **Full content:** `templates/playwright-explore-website/phases.md`## Steps- Open the URL.- Explore 3 to 5 core flows.- Document locators and outcomes.- Propose tests and close the browser.## Tasks- Confirm the URL.- Exercise the main user journeys.- Record evidence.- Summarize and suggest tests.## Subtasks- Ask for a URL if missing.- Capture locators for key controls.- Note observed outcomes.- Close the browser context.## Actions Summary1. Navigate to the site.2. Interact with the core flows.3. Document locators and outcomes.4. Generate test ideas.```## Template ReferencesTemplates in `templates/playwright-explore-website/`:- `phases.md`