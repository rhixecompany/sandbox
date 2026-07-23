# MASTER_RULES.md — Universal Agent Rules

Core principles that apply across all Hermes agent interactions.

## 1. Session Startup Protocol

Before ANY task execution:

1. Read `SESSION_REPORT.md` in current working directory
2. Load and verify `user-communication-preferences`
3. Load and verify `session-audit-report`
4. Load and verify `hermes-profiles`
5. Load and verify `validate-memories`

**If any of the 5 mandatory skills fail to load → ABORT and surface error.**

## 2. Profile Selection (Per Task)

Always run `hermes profile use <name>` BEFORE execution:

| Task Type | Profile |
|-----------|---------|
| Code implementation, debugging, refactoring | `code-architect` |
| Deep research, literature review, synthesis | `research-analyst` |
| Design, content creation, brainstorming | `creative-director` |
| Planning, coordination, admin | `exec-assistant` |
| Tutorials, explanations, teaching | `patient-tutor` |
| System operations, DevOps, infra | `alexa` |
| General purpose | `default` |

## 3. MCP-First Tool Precedence

Before using native tools (`terminal`, `read_file`, `search_files`), check if MCP provides equivalent:

- `filesystem` → file operations
- `github` → GitHub API
- `ast-grep` → code search/replace
- `memory` → persistent memory
- `playwright` → browser automation
- `sequential-thinking` → structured reasoning
- `cli` → command execution
- `code-sandbox` → isolated Node.js
- `fetch` → HTTP requests

## 4. Strict Sequential on "only then"

Each phase is a hard dependency:

```
spec compliance → code quality review → approval → completion
```

No skipping phases. Verify each phase passes before proceeding.

## 5. Verification Before Claim

Never claim success without tool verification:

- File writes → re-read and verify
- Git operations → run `git status`
- Tests → run and confirm pass
- Deployments → verify endpoint responds

## 6. Safety Rules

- **No secrets in output** — Never read/print/commit `.env`/tokens
- **Destructive ops need approval** — Explain risks, get confirmation
- **MCP Security** — Least-privilege, OAuth 2.1+PKCE, SSRF blocks, no sudo
- **Honest blockers** — Report, never fabricate

## 7. Memory Policy

- **MEMORY.md** (<2,200 chars): Durable facts only
- **USER.md** (<1,375 chars): User profile only
- Never store task progress in memory (use `session_search`)
- Use `session_search` for recall, not memory

## 8. Skill Library Hygiene

- Prefer patching existing umbrella skills
- Create new skills only at class level
- Move detailed content to `references/` when SKILL.md > 250 lines
- Never create stub/duplicate/dead skills
- Verify on disk after all skill operations

## 9. Commit Format

```
<type>: <description>

feat: add new feature
fix: resolve bug
docs: update documentation
refactor: restructure code
test: add tests
chore: maintenance
perf: performance improvement
```

## 10. Path Safety (Windows/MSYS)

- Derive paths from `$HOME`/`$USERPROFILE`
- Never hardcode Windows paths
- Use POSIX syntax in terminal calls
- Pass native Windows paths to Python scripts