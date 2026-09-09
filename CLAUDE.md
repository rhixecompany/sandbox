# CLAUDE.md

Claude-specific behavior. All workspace rules in `AGENTS.md`.

- Prefer `filesystem` MCP for file ops, `ast-grep` for search, `sequential-thinking` for multi-step tasks
- All toolchain, routing, and conventions: see `AGENTS.md`
- Multi-file protocol (≥5 files): see `SOUL.md` canonical block

## Profile Routing

| Task Type | Profile |
|-----------|---------|
| Code implementation, debugging, refactoring | `code-architect` |
| Deep research, literature review, synthesis | `research-analyst` |
| Design, content creation, brainstorming | `creative-director` |
| Planning, coordination, admin | `exec-assistant` |
| Tutorials, explanations, teaching | `patient-tutor` |
| System operations, DevOps, infra | `adminbot` |
| General purpose | `default` |

Run `hermes profile use <name>` matching task type BEFORE execution.
