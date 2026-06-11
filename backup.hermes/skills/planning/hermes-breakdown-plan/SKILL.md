---
name: hermes-breakdown-plan
title: Hermes Breakdown Plan
description: "Generate a GitHub project plan (Epic > Feature > Story/Enabler > Test) and issue templates from PRD and technical artifacts."
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [planning, project-management, github]
    related_skills: [plan, subagent-driven-development]
---

# Hermes: Breakdown Plan

## Overview

Use when you want to convert Epic/Feature artifacts (PRD, technical breakdown, implementation plan, test strategy) into a GitHub-oriented Project Plan and Issue Creation checklist with templates and automation snippets.

## When to Use

- Preparing a feature for development and release
- Creating issue templates and automations for a new epic or feature
- When you need a reproducible, repository-stored project plan

## Inputs

- Path to Epic PRD: /docs/ways-of-work/plan/{epic-name}/epic.md
- Path to Feature PRD: /docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md
- Optional: technical-breakdown.md, implementation-plan.md, test-strategy.md

## Outputs

- /docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md
- /docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md
- Automation snippet (actions/github-script) example in the project plan

## Usage (delegate_task)

delegate_task({
  "goal": "Run hermes-breakdown-plan for {epic}/{feature}",
  "context": "epic_prd=/docs/ways-of-work/plan/payments/epic.md\nfeature_prd=/docs/ways-of-work/plan/payments/merchant-onboarding/prd.md",
  "toolsets": ["file"]
})

## Programmatic usage (execute_code)

- Read PRD with read_file()
- Interpolate PRD sections into the prompt templates in this skill
- Write outputs with write_file()

## Verification

- project-plan.md exists and contains: Project Overview, Work Item Hierarchy (Mermaid), Issues Breakdown with templates
- issues-checklist.md exists and lists per-level checklists

## Notes

This skill intentionally produces markdown and small automation snippets only; it does not perform GitHub API calls by default. For automated issue creation, connect the generated snippet to a GitHub Actions workflow and run from the repository.



