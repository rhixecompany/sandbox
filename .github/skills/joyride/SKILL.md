---
name: joyride
description: Support tool for interactive workflow steps — clipboard copy, file output, confirmation dialogs. Used by prompts that need to produce copy-paste-ready output or interactive user handoffs.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - clipboard
  - interactive
  - workflow
  - support
---

# Joyride

Support tool for interactive workflow steps — clipboard copy, file output, confirmation dialogs. Used by prompts that need to produce copy-paste-ready output or interactive user handoffs.

## Usage

```bash
# Copy output to clipboard
joyride copy <file>

# Show confirmation dialog
joyride confirm "Ready to proceed?"
```

## When to use

- Prompt output should be copied to clipboard for user
- Interactive confirmation needed before destructive operations
- Handoff between workflow steps requires user attention

## Verification

- [ ] Output successfully copied/displayed
- [ ] User confirmation received
- [ ] Next step in workflow triggered
