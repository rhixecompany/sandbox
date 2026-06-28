---
name: acpx-executor
description: Execute a prompt or workflow via any ACPX provider. Use when running prompts through ACPX-compatible executors (Copilot CLI, OpenCode, Codex) for validation, verification, or cross-platform execution.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - acpx
  - executor
  - workflow
  - automation
---

# ACPX Executor

Execute a prompt via any ACPX provider. Use when you need to run a prompt through a different agent platform (Copilot CLI, OpenCode, Codex) for quick validation or cross-platform verification.

## Usage

```bash
# Execute a prompt via ACPX
acpx-executor run <prompt-name>

# Quick validation
acpx-executor validate <prompt-name>
```

## When to use

- Cross-platform prompt execution testing
- Quick validation and verification
- Running prompts through ACPX-compatible providers

## Verification

- [ ] ACPX provider is configured and reachable
- [ ] Prompt resolves to an existing file
- [ ] Execution completes without unexpected exit code
- [ ] Output captured for verification
