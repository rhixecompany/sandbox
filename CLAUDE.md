# CLAUDE.md

Claude-specific pointer. All workspace rules in `AGENTS.md`. Persona in `SOUL.md`.

## Multi-File Trigger

>6 file changes → load skill `multi-file-change-protocol`.

## Rules (pointers)

- File ops: prefer `filesystem` MCP, `ast-grep` for search, `sequential-thinking` for multi-step
- Toolchain/routing/conventions: see `AGENTS.md`
- Style/safety/DRY: see `user-communication-preferences` skill

## Profile Routing

| Task Type | Profile |
|---|---|
| Code implementation, debugging, refactoring | `code-architect` |
| Deep research, literature review, synthesis | `research-analyst` |
| Design, content creation, brainstorming | `creative-director` |
| Planning, coordination, admin | `exec-assistant` |
| Tutorials, explanations, teaching | `patient-tutor` |
| System operations, DevOps, infra | `adminbot` |
| General purpose | `default` |

Run `hermes profile use <name>` matching task type BEFORE execution.