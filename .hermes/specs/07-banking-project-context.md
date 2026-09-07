---
name: 07-banking-project-context
title: Banking Project Context Loading
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Ensure the Banking project (`projects/Banking/`) AGENTS.md loads reliably as project context before any `.github/prompts/`. Fix context loading issues reported in sessions 221823, 222027, 222231 so that AGENTS.md is always recognized first.

## Requirements

### Functional
- [ ] `projects/Banking/AGENTS.md` loads as project context in new Banking sessions
- [ ] AGENTS.md recognized before `.github/prompts/` (canonical guidance first)
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
| Load time < 3s | Measure context loading | < 3 seconds |
| Cross-profile | Switch profile → Banking session | AGENTS.md still loads |

## Non-Functional Requirements

Context load time must be under 3 seconds. No duplicate context loading across sessions. Context must persist across profile switches. AGENTS.md must load before `.github/prompts/` (canonical guidance first). Banking project stack (Next.js 16, Drizzle ORM, Plaid, Dwolla, TypeScript strict) must be recognized in context.

## Verification

```bash
# 1. Read AGENTS.md
read_file ~/Desktop/SandBox/projects/Banking/AGENTS.md | head -50
# Expected: Returns full content

# 2. Verify project structure
find ~/Desktop/SandBox/projects/Banking -name "AGENTS.md" -o -name "*.prompt.md" | head -20
# Expected: Files found

# 3. Check workspace .hermes.md for Banking overrides
read_file ~/Desktop/SandBox/.hermes.md
# Expected: Banking overrides present

# 4. Verify stubs defer to AGENTS.md
read_file ~/Desktop/SandBox/projects/Banking/CLAUDE.md 2>/dev/null || echo "No CLAUDE.md"
read_file ~/Desktop/SandBox/projects/Banking/.cursorrules 2>/dev/null || echo "No .cursorrules"
# Expected: Stubs defer to AGENTS.md
```

## Linked Specs
- 07-banking-project-context.md

## Linked Plan
- ../2026-08-15_202608_four-agent-prompt-audit-plan.md
