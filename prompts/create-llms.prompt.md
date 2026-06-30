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
title: Create LLMs.txt File from Repository Structure
name: create-llms
description: "Create an llms.txt file from scratch based on repository structure following the llms.txt specification at https://llmstxt.org/"
tags:
  - generator
  - ml
  - prompts
  - specification
  - typescript
  - documentation
  - generator
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - create-llms.prompt

trigger: create-llms

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - create-llms.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - create-llms.prompt

## Goal

Create an llms.txt file from scratch based on repository structure following the llms.txt specification at https://llmstxt.org/.

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
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

Create a comprehensive `llms.txt` file that serves as an entry point for LLMs to understand and navigate the repository effectively. The file must comply with the llms.txt specification and be optimized for LLM consumption while remaining human-readable.

## Analysis and Planning Phase

> Before creating the `llms.txt` file, you must complete a thorough analysis:
> ### Step 1: Review llms.txt Specification

> **Full content:** `templates/create-llms/analysis_and_planning_phase.md`

## Implementation Requirements

> ### Format Compliance
> The `llms.txt` file must follow this exact structure per the specification:

> **Full content:** `templates/create-llms/implementation_requirements.md`

## Execution Steps

> ### Step 1: Repository Analysis
> 1. Examine the repository structure completely

> **Full content:** `templates/create-llms/execution_steps.md`

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

## Example Structure Template

```txt
# [Repository Name]

> [Concise description of the repository's purpose and scope]

[Optional additional context paragraphs without headings]

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
````

## Success Criteria

The created `llms.txt` file should:

1. Enable LLMs to quickly understand the repository's purpose
2. Provide clear navigation to essential documentation
3. Follow the official llms.txt specification exactly
4. Be comprehensive yet concise
5. Serve both human and machine readers effectively
6. Include all critical files for project understanding
7. Use clear, unambiguous language throughout
8. Organize content logically for easy consumption


## Template References

Detailed templates in `templates/create-llms/`:
- `analysis_and_planning_phase.md`
- `execution_steps.md`
- `implementation_requirements.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
