---
category: software-development
title: Codemap
name: codemap
description: "Use when onboarding to a new codebase, understanding unfamiliar repository structure, or documenting codebase architecture and dependencies."
---
## Goal
Use when onboarding to a new codebase, understanding unfamiliar repository structure, or documenting codebase architecture and dependencies.


## codemap

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Codemap operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Description

Generate comprehensive hierarchical codemaps for unfamiliar repositories. Provides detailed documentation of codebase structure, dependencies, and architecture.

## When to Use

- Onboarding to a new codebase
- Understanding unfamiliar repository structure
- Documenting codebase architecture
- Planning refactoring or migrations
- Analyzing large or complex projects

## When NOT to Use

- Quick file lookups (use glob/grep instead)
- Familiar codebases (use codebase-analyzer instead)
- Small projects with simple structure
- Real-time code changes (codemap is static)

## Workflow

### Phase 1: Scan Repository

- Identify project type and language
- List all directories and key files
- Detect dependencies and imports

### Phase 2: Build Hierarchy

- Create directory tree structure
- Identify module boundaries
- Map dependencies between modules

### Phase 3: Document Architecture

- Describe purpose of each major component
- Document data flows
- Identify key entry points

### Phase 4: Generate Output

- Create hierarchical codemap document
- Include visual diagrams if applicable
- Export in readable format

## Tools & References

- **Related Skills**: codebase-analyzer, codebase-locator
- **Output Format**: Markdown with tree structure
- **Visualization**: ASCII trees or Mermaid diagrams

## Best Practices

- Run on clean, built codebase
- Document assumptions about project structure
- Update codemap when architecture changes
- Use for onboarding new team members
- Keep codemap in version control
