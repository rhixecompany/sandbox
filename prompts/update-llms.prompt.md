---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - extensions
  - web/fetch
  - githubRepo
  - openSimpleBrowser
  - problems
  - runTasks
  - search
  - search/searchResults
  - runCommands/terminalLastCommand
  - runCommands/terminalSelection
  - testFailure
  - usages
  - vscodeAPI
license: MIT
author: Hermes Agent
version: 1.0.0
title: Update LLMs.txt File
name: update-llms
description: "Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the llms.txt specification at https://llmstxt.org/"
---


## Goal

Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the llms.txt specification at https://llmstxt.org/.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Primary Directive

Update the existing `llms.txt` file to maintain accuracy and compliance with the llms.txt specification while reflecting current repository structure and content. The file must remain optimized for LLM consumption while staying human-readable.

## Analysis and Planning Phase

> Before updating the `llms.txt` file, you must complete a thorough analysis:
> ### Step 1: Review Current File and Specification

> **Full content:** `templates/update-llms/analysis_and_planning_phase.md`

## Implementation Requirements

> ### Format Compliance
> The updated `llms.txt` file must maintain this exact structure per the specifica

> **Full content:** `templates/update-llms/implementation_requirements.md`

## Execution Steps

> ### Step 1: Current State Analysis
> 1. Read the existing `llms.txt` file thoroughly

> **Full content:** `templates/update-llms/execution_steps.md`

## Quality Assurance

### Format Validation

- ✅ H1 header with project name
- ✅ Blockquote summary (if included)
- ✅ H2 sections for file lists
- ✅ Proper markdown link format
- ✅ No broken or invalid links
- ✅ Consistent formatting throughout

### Content Validation

- ✅ Clear, unambiguous language
- ✅ Comprehensive coverage of essential files
- ✅ Logical organization of content
- ✅ Appropriate file descriptions
- ✅ Serves as effective LLM navigation tool

### Specification Compliance

- ✅ Follows https://llmstxt.org/ format exactly
- ✅ Uses required markdown structure
- ✅ Implements optional sections appropriately
- ✅ File located at repository root (`/llms.txt`)

## Update Strategy

> When adding new content:
> 1. Identify the appropriate section for new files

> **Full content:** `templates/update-llms/update_strategy.md`

## Documentation

- [Main README](README.md): Primary project documentation and getting started guide
- [Contributing Guide](CONTRIBUTING.md): Guidelines for contributing to the project
- [Code of Conduct](CODE_OF_CONDUCT.md): Community guidelines and expectations

## Specifications

- [Technical Specification](spec/technical-spec.md): Detailed technical requirements and constraints
- [API Specification](spec/api-spec.md): Interface definitions and data contracts

## Examples

- [Basic Example](examples/basic-usage.md): Simple usage demonstration
- [Advanced Example](examples/advanced-usage.md): Complex implementation patterns

## Configuration

- [Setup Guide](docs/setup.md): Installation and configuration instructions
- [Deployment Guide](docs/deployment.md): Production deployment guidelines

## Optional

- [Architecture Documentation](docs/architecture.md): Detailed system architecture
- [Design Decisions](docs/decisions.md): Historical design decision records
```

## Success Criteria

The updated `llms.txt` file should:

1. Accurately reflect the current repository structure and content
2. Maintain compliance with the llms.txt specification
3. Provide clear navigation to essential documentation
4. Remove outdated or incorrect references
5. Include new important files and documentation
6. Maintain logical organization for easy LLM consumption
7. Use clear, unambiguous language throughout
8. Continue to serve both human and machine readers effectively


## Template References

Detailed templates in `templates/update-llms/`:
- `analysis_and_planning_phase.md`
- `execution_steps.md`
- `implementation_requirements.md`
- `update_strategy.md`
