---
name: 06-honcho-integration
title: Honcho Integration
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Integrate Honcho for persistent cross-session memory and user modeling. Verify that all honcho tools function correctly and cross-session recall works across profile switches.

## Requirements

### Functional
- [ ] honcho_profile returns user peer card with preferences, goals, working style
- [ ] honcho_context returns raw peer context from recent sessions
- [ ] honcho_reasoning with reasoning_level=high synthesizes working style summary
- [ ] honcho_search finds relevant memories across sessions
- [ ] honcho_conclude saves conclusions about user for future sessions
- [ ] Cross-session preference recall: TypeScript/VS Code dark theme persists
- [ ] Memory persists across profile switches (default ↔ code-architect ↔ adminbot, etc.)

### Non-Functional
- [ ] Honcho MCP server connected and tested
- [ ] Tools respond in < 5 seconds
- [ ] No duplicate memory entries
- [ ] Privacy: only user-authorized data stored

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Honcho MCP | `hermes mcp test honcho` | ✓ Connected |
| Profile tool | `honcho_profile` | Returns peer card JSON |
| Context tool | `honcho_context` | Returns raw context |
| Reasoning high | `honcho_reasoning level=high "summarize working style"` | Synthesized summary |
| Search tool | `honcho_search "TypeScript"` | Finds relevant memories |
| Conclude tool | `honcho_conclude "User prefers systematic skill-driven development"` | Saved |
| Cross-session | New session → `honcho_profile` | Preferences recalled |
| Profile switch | `hermes profile use code-architect` → `honcho_profile` | Same preferences |

## Non-Functional Requirements

All honcho tools must respond in < 5 seconds. No duplicate memory entries across sessions. Privacy: only user-authorized data stored. Honcho MCP server must be connected and verified. Honcho hybrid mode (auto-inject + tools available) must function correctly across all 14 Hermes profiles.

## Verification

```bash
# Full honcho test suite
echo "=== Honcho MCP ==="
hermes mcp test honcho
# Expected: Connected

echo "=== Profile ==="
honcho_profile
# Expected: Returns peer card JSON

echo "=== Context ==="
honcho_context
# Expected: Returns raw context

echo "=== Reasoning (high) ==="
honcho_reasoning level=high "What are my coding preferences and working style?"
# Expected: Synthesized summary

echo "=== Search ==="
honcho_search "TypeScript dark theme"
# Expected: Finds relevant memories

echo "=== Conclude ==="
honcho_conclude "User prefers TypeScript with VS Code dark theme, systematic skill-driven development, DRY principles, stacked skill bundles, MCP-first tool precedence"
# Expected: Saved

# Cross-session test: would need new session
```

## Linked Specs
- 06-honcho-integration.md

## Linked Plan
- ../skill-implementation-master-plan.md
