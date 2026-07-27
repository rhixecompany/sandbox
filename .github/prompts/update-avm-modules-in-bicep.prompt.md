---
name: update-avm-modules-in-bicep
title: Update Azure Verified Modules in Bicep Files
description: Update Azure Verified Modules (AVM) to latest versions in Bicep files.
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
  - azure
  - maintenance
  - ml
  - prompts
  - specification
  - testing
  - typescript
trigger: /update-avm-modules-in-bicep
---

## GoalUpdate Azure Verified Modules (AVM) to latest versions in Bicep files.## ContextUse when you need to work on the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## Process1. **Scan**: Extract AVM modules and current versions from `${file}`1. **Identify**: List all unique AVM modules used by matching `avm/res/{service}/{resource}` using `#search` tool1. **Check**: Use `#fetch` tool to get latest version of each AVM module from MCR: `https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`1. **Compare**: Parse semantic versions to identify AVM modules needing update1. **Review**: For breaking changes, use `#fetch` tool to get docs from: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`1. **Update**: Apply version updates and parameter changes using `#editFiles` tool1. **Validate**: Run `bicep lint` and `bicep build` using `#runCommands` tool to ensure compliance.1. **Output**: Summarize changes in a table format with summary of updates below.## Tool UsageAlways use tools `#search`, `#searchResults`,`#fetch`, `#editFiles`, `#runCommands`, `#todos` if available. Avoid writing code to perform tasks.## Breaking Change Policy⚠️ **PAUSE for approval** if updates involve:- Incompatible parameter changes- Security/compliance modifications- Behavioral changes## Output FormatOnly display results in table with icons:```markdown| Module | Current | Latest | Status | Action | Docs || --- | --- | --- | --- | --- | --- || avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Updated | [📖](link) || avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Current | [📖](link) |### Summary of UpdatesDescribe updates made, any manual reviews needed or issues encountered.```## Icons- 🔄 Updated- ✅ Current- ⚠️ Manual review required- ❌ Failed- 📖 Documentation## Requirements- Use MCR tags API only for version discovery- Parse JSON tags array and sort by semantic versioning- Maintain Bicep file validity and linting compliance## Template ReferencesTemplates in `templates/update-avm-modules-in-bicep/`:- `phases.md`