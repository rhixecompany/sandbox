# Prompt Skill: Hermes Platform Setup & Diagnostics

This directory contains the `writing-prompt` skill for generating prompts related to the Hermes Platform Setup & Diagnostics workflow.

## Trigger

`platform-setup-diagnostics` — use when the user asks for prompts, prompt templates, or prompt generation related to Hermes platform setup, diagnostics, repair, plugin/hook/MCP enablement, git operations, or filesystem cleanup.

## Structure

```
hermes-platform-setup-diagnostics/
├── prompt.md              # Main prompt definition with frontmatter
├── templates/             # Prompt templates for recurring patterns
├── scripts/               # Automation scripts for prompt validation/generation
└── verification/          # Verification evidence that the prompt works
```

## Contents

### prompt.md

The main prompt file. It defines:

- **Frontmatter**: title, version, date_created, owner, status, tags
- **Context**: what situation this prompt is for
- **Instructions**: what the AI should do when this prompt is invoked
- **Constraints**: what the AI must not do
- **Output format**: what the AI should produce

### templates/

Reusable prompt templates for common patterns within the platform setup diagnostics domain:

- `diagnostic-run.template.md` — template for running a diagnostic suite
- `repair-session.template.md` — template for a repair session
- `verification-template.md` — template for verification evidence

### scripts/

Scripts that validate, generate, or transform prompts:

- `validate-prompt.py/ts/ps1/sh` — validate prompt frontmatter and structure
- `generate-promptMappedFiles.py/ts/ps1/sh` — generate prompt files from templates

### verification/

Evidence that the prompt produces correct, useful output:

- Validation script output
- Sample invocations and results
- Gate-pass evidence

## Conventions

- Prompt frontmatter must include all required fields
- Templates use `{{variable}}` syntax for substitution points
- Scripts must be platform-appropriate (Python, TypeScript, PowerShell, Bash)
- Verification evidence must be current and pass all checks

## Workflow Integration

This skill is invoked during the prompt-writing phase of the platform setup diagnostics plan. It feeds into the prompt validation gate.
