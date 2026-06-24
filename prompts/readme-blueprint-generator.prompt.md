---
license: MIT
author: Hermes Agent
version: 1.0.0
title: README Generator Prompt
name: readme-blueprint-generator
description: "Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot directory files and copilot-instructions.md to extract project information, technology stack, architecture, development workflow, coding standards, and testing approaches while generating well-structured markdown documentation with proper formatting, cross-references, and developer-focused content."

agent: "agent"
---

## Goal

Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot directory files and copilot-instructions.md to extract project information, technology stack, architecture, development workflow, coding standards, and testing approaches while generating well-structured markdown documentation with proper formatting, cross-references, and developer-focused content.

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

## Project Name and Description

- Extract the project name and primary purpose from the documentation
- Include a concise description of what the project does

## Technology Stack

- List the primary technologies, languages, and frameworks used
- Include version information when available
- Source this information primarily from the Technology_Stack file

## Project Architecture

- Provide a high-level overview of the architecture
- Consider including a simple diagram if described in the documentation
- Source from the Architecture file

## Getting Started

- Include installation instructions based on the technology stack
- Add setup and configuration steps
- Include any prerequisites

## Project Structure

- Brief overview of the folder organization
- Source from Project_Folder_Structure file

## Key Features

- List main functionality and features of the project
- Extract from various documentation files

## Development Workflow

- Summarize the development process
- Include information about branching strategy if available
- Source from Workflow_Analysis file

## Coding Standards

- Summarize key coding standards and conventions
- Source from the Coding_Standards file

## Testing

- Explain testing approach and tools
- Source from Unit_Tests file

## Contributing

- Guidelines for contributing to the project
- Reference any code exemplars for guidance
- Source from Code_Exemplars and copilot-instructions

## License

- Include license information if available

Format the README with proper Markdown, including:

- Clear headings and subheadings
- Code blocks where appropriate
- Lists for better readability
- Links to other documentation files
- Badges for build status, version, etc. if information is available

Keep the README concise yet informative, focusing on what new developers or users would need to know about the project.


## Template References

Templates in `templates/readme-blueprint-generator/`:
- `legacy_prompt_details.md`
- `phases.md`
