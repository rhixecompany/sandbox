---
name: generator-first-doc-workflow
title: "Generator First Doc Workflow"
description: "Use when a project's own generator/CLI should be used to produce Markdown/PDF artifacts from structured JSON. Keeps user data in project-local inputs and avoids hand-written output files when a generator exists."
version: 1.0.0
author: Alexa
license: MIT
tags: [generator, docs, resume, cli, workflow]
---
# generator-first-doc-workflow

Generate project artifacts through the project's own entrypoint or CLI instead of creating output documents manually.

## Overview

Automated reasoning and workflow tool for `generator-first-doc-workflow`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Project has a generator entrypoint such as `index.ts`, `main.py`, or a documented CLI
- There are existing input files with structured data and documented output conventions
- README describes Markdown and/or PDF generation that is not yet represented in actual output files
- User requests resumes, cover letters, LinkedIn notes, interview prep, or similar repeatable docs

## When NOT to Use

- One-off documents that are intentionally outside the generator's scope
- Static hand-written reference files that should not be regenerated
- Projects without a maintained generator or documented generation workflow

## Workflow

### Phase 1: Inspect existing generator surface

- Check command entrypoints, available CLI flags, input/output paths, and sample inputs
- Read project-local instructions for conventions
- Confirm whether the requested document type is actually supported

### Phase 2: Use project-local structured input

- Store person-specific details in a project-local input file, such as `basil-input.json`
- Provide at least one complete experience entry, plus valid contact details
- When a required field is unknown, use a short placeholder instead of empty strings if the generator requires that key

### Phase 3: Generate with CLI flags

- Use verbose mode to inspect validation failures or output differences
- Use skip flags when the artifact should stay focused on core content rather than repo-derived sections
- Prefer paired Markdown plus PDF generation when the user wants a final deliverable

## Pitfalls

- Do not create output files by hand if the generator can produce them
- Do not modify shared examples or sample inputs unless the user explicitly asks
- Do not assume advertised document types are implemented; verify from the entrypoint

## Verification

- Confirm generated artifacts exist under the project's expected output directory
- Re-run generator with updated input if validation errors mention required fields
- If a requested artifact type is missing from the generator, tell the user before producing a manual substitute

## References

See `references/resume-maker-workflow.md` for concrete reproduction notes for the `Resume_maker` project.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Generator First Doc Workflow" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
