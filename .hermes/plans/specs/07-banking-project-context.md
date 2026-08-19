# SPEC: Banking Project Context Loading

**Workstream:** 07-banking-project-context
**Priority:** P2 - Project Work
**Dependencies:** 01-config-foundation-repair, 02-mcp-server-suite
**Profile:** code-architect

---

## Problem Statement

Banking project (`projects/Banking/`) has AGENTS.md as canonical agent guidance, but context loading is flaky. Sessions 221823, 222027, 222231 reported context loading issues. Need to ensure AGENTS.md loads reliably as project context before any .github/prompts/.

## Current State

- Banking project at `~/Desktop/SandBox/projects/Banking/`
- AGENTS.md exists and is comprehensive (Next.js 16, Drizzle, Plaid, Dwolla)
- `.github/prompts/` has project-specific prompts
- Context loading should: AGENTS.md → .github/prompts/ → project specs

## Requirements

### Functional
- [ ] `projects/Banking/AGENTS.md` loads as project context in new Banking sessions
- [ ] AGENTS.md recognized before .github/prompts/ (canonical guidance first)
- [ ] Project-specific specs reference `.github/instructions/` templates
- [ ] Context loading works for both CLI and desktop sessions
- [ ] Banking project stack recognized: Next.js 16, Drizzle ORM, Plaid, Dwolla, TypeScript strict

### Non-Functional
- [ ] Context load time < 3 seconds
- [ ] No duplicate context loading
- [ ] Works across profile switches

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| AGENTS.md readable | `read_file ~/Desktop/SandBox/projects/Banking/AGENTS.md` | Returns full content |
| Context loads | New session in Banking dir → check loaded context | AGENTS.md referenced |
| Prompts load | `ls ~/Desktop/SandBox/projects/Banking/.github/prompts/` | Project prompts listed |
| Stack recognized | Context mentions Next.js 16, Drizzle, Plaid, Dwolla | Found |

## Implementation Approach

```bash
# 1. Verify AGENTS.md exists and is readable
read_file ~/Desktop/SandBox/projects/Banking/AGENTS.md

# 2. Check project structure
ls -la ~/Desktop/SandBox/projects/Banking/
ls -la ~/Desktop/SandBox/projects/Banking/.github/prompts/
ls -la ~/Desktop/SandBox/projects/Banking/.github/instructions/

# 3. Verify context loading mechanism
# - Hermes should auto-load AGENTS.md when cwd is in Banking/
# - Check .hermes.md at workspace root for project overrides
# - Check CLAUDE.md/.cursorrules are thin stubs deferring to AGENTS.md

# 4. Test in new session context
# (Would need new session to fully verify)
```

## Banking Project Stack (from AGENTS.md)

| Layer | Technology |
|-------|------------|
| Framework | Next.js 16 |
| Database | Drizzle ORM |
| Auth/Payments | Plaid, Dwolla |
| Language | TypeScript strict |
| Package Manager | Bun |
| Testing | Vitest |
| Linting | ESLint 10 flat config, Prettier 3 |
| CI/CD | GitHub Actions |

## Verification Steps

```bash
# 1. Read AGENTS.md
read_file ~/Desktop/SandBox/projects/Banking/AGENTS.md | head -50

# 2. Verify project structure
find ~/Desktop/SandBox/projects/Banking -name "AGENTS.md" -o -name "*.prompt.md" | head -20

# 3. Check workspace .hermes.md for Banking overrides
read_file ~/Desktop/SandBox/.hermes.md

# 4. Verify stubs defer to AGENTS.md
read_file ~/Desktop/SandBox/projects/Banking/CLAUDE.md 2>/dev/null || echo "No CLAUDE.md"
read_file ~/Desktop/SandBox/projects/Banking/.cursorrules 2>/dev/null || echo "No .cursorrules"
```

## Risks

- **Context loading order** — AGENTS.md must load before prompts
- **Workspace vs project context** — Root .hermes.md may override
- **Profile-specific context** — Different profiles may load different context
- **Session continuity** — Context must persist across session restarts

## References

- `~/Desktop/SandBox/AGENTS.md` — Workspace canonical guidance
- `~/Desktop/SandBox/projects/Banking/AGENTS.md` — Banking project guidance
- `~/Desktop/SandBox/.hermes.md` — Hermes-specific project overrides
- MEMORY.md: "Directory Map: projects/Banking/ — Next.js 16, Drizzle ORM, Plaid, Dwolla"