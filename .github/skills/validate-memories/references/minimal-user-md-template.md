# Minimal default-profile USER.md template

Use this when repairing `~/AppData/Local/hermes/memories/USER.md`.

```md
---
user: Alexa
---
# USER.md — default profile

## Identity
- Name: Alexa
- Workspace: ~/Desktop/SandBox
- Profile: default

## Model
- gpt-5.4-mini (openai-codex)

## Execution Preferences
- Concise, action-first, DRY
- Read → patch → verify
- MCP-first; verify before claim
- No backup files; git rollback
- Full execution; no phase-gate pauses
```

Validation checklist:
- frontmatter present
- `## Identity`, `## Model`, `## Execution Preferences` headings present
- file stays compact (<1375 bytes)
- no session-progress / task-log content
