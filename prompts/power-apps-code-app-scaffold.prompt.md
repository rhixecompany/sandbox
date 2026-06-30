---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - problems
  - search
license: MIT
author: Hermes Agent
version: 1.0.0
title: Power Apps Code Apps Project Scaffolding
name: power-apps-code-app-scaffold
description: "Scaffold a complete Power Apps Code App project with PAC CLI setup, SDK integration, and connector configuration"
tags:
  - audit
  - configuration
  - frontend
  - prompts
  - specification
  - database
  - drizzle
  - planning
  - power-platform
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - power-apps-code-app-scaffold.prompt

trigger: power-apps-code-app-scaffold

---
metadata:
  hermes:
    related_skills: []
    tags:
    - power-apps-code-app-scaffold.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - power-apps-code-app-scaffold.prompt

# Power Apps Code Apps Project Scaffolding

You are an expert Power Platform developer who specializes in creating Power Apps Code Apps. Your task is to scaffold a complete Power Apps Code App project following Microsoft's best practices and current preview capabilities.

## Context

Power Apps Code Apps (preview) allow developers to build custom web applications using code-first approaches while integrating with Power Platform capabilities. These apps can access 1,500+ connectors, use Microsoft Entra authentication, and run on managed Power Platform infrastructure.

## Task

> Create a complete Power Apps Code App project structure with the following compo
> ### 1. Project Initialization

> **Full content:** `templates/power-apps-code-app-scaffold/task.md`

## Implementation Guidelines

> ### Prerequisites to Mention
> - Visual Studio Code with Power Platform Tools extension

> **Full content:** `templates/power-apps-code-app-scaffold/implementation_guidelines.md`

## Deliverables

1. Complete project scaffolding with all necessary files
2. Working sample application with connector integration
3. Comprehensive documentation and setup instructions
4. Development and deployment scripts
5. TypeScript configuration optimized for Power Apps Code Apps
6. Best practices implementation examples

Ensure the generated project follows Microsoft's official Power Apps Code Apps documentation and samples from https://github.com/microsoft/PowerAppsCodeApps, and can be successfully deployed to Power Platform using the `pac code push` command.


## Template References

Detailed templates in `templates/power-apps-code-app-scaffold/`:
- `implementation_guidelines.md`
- `task.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
