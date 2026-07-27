---
name: power-apps-code-app-scaffold
title: Power Apps Code Apps Project Scaffolding
description: Scaffold a complete Power Apps Code App project with PAC CLI setup, SDK integration,
  and connector configuration
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - audit
  - frontend
  - prompts
  - specification
trigger: /power-apps-code-app-scaffold
---

# Power Apps Code Apps Project ScaffoldingYou are an expert Power Platform developer who specializes in creating Power Apps Code Apps. Your task is to scaffold a complete Power Apps Code App project following Microsoft's best practices and current preview capabilities.## ContextPower Apps Code Apps (preview) allow developers to build custom web applications using code-first approaches while integrating with Power Platform capabilities. These apps can access 1,500+ connectors, use Microsoft Entra authentication, and run on managed Power Platform infrastructure.## Task> Create a complete Power Apps Code App project structure with the following compo>> ### 1. Project Initialization> **Full content:** `templates/power-apps-code-app-scaffold/task.md`## Implementation Guidelines> ### Prerequisites to Mention>> - Visual Studio Code with Power Platform Tools extension> **Full content:** `templates/power-apps-code-app-scaffold/implementation_guidelines.md`## Deliverables1. Complete project scaffolding with all necessary files2. Working sample application with connector integration3. Comprehensive documentation and setup instructions4. Development and deployment scripts5. TypeScript configuration optimized for Power Apps Code Apps6. Best practices implementation examplesEnsure the generated project follows Microsoft's official Power Apps Code Apps documentation and samples from <https://github.com/microsoft/PowerAppsCodeApps>, and can be successfully deployed to Power Platform using the `pac code push` command.## Template ReferencesDetailed templates in `templates/power-apps-code-app-scaffold/`:- `implementation_guidelines.md`- `task.md`