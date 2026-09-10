---
name: rules-core
description: "Core execution rules — DRY, no backup files, MCP-first, verify after change, no secrets."
---

# Core Rules
- Read before edit. Patch with `patch`. Verify with syntax check or AST parse.
- No `.bak`, `.backup`, `.old`. Use git rollback.
- MCP-first: prefer filesystem/github/memory/playwright/sequential-thinking over native equivalents.
- No secrets printed; no placeholders in committed files.
- Profile routing verified: adminbot (ops/debug) + patient-tutor (teaching).
