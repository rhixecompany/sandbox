# SPEC: Honcho Integration

**Workstream:** 06-honcho-integration
**Priority:** P2 - Enhancement
**Dependencies:** 02-mcp-server-suite (honcho MCP), 05-soul-user-memory-enhancement
**Profile:** code-architect

---

## Problem Statement

Integrate Honcho for persistent cross-session memory and user modeling. User has active Honcho hybrid mode (auto-inject + tools available). Need to implement honcho tools and verify cross-session recall works.

## Current State

- Honcho memory: Active (hybrid mode)
- Tools available: honcho_profile, honcho_context, honcho_reasoning, honcho_search, honcho_conclude
- User preferences known: TypeScript, VS Code dark theme, systematic skill-driven development, DRY best practices
- Peer card generation from session data needed

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

## Implementation Approach

```bash
# 1. Verify Honcho MCP connected
hermes mcp test honcho

# 2. Test each honcho tool
honcho_profile
honcho_context
honcho_reasoning level=high "summarize my working style and preferences"
honcho_search "TypeScript VS Code"
honcho_conclude "User prefers systematic, skill-driven development with stacked bundles and DRY best practices"

# 3. Verify cross-session
# Start new session, run honcho_profile, confirm preferences present

# 4. Verify profile switch
hermes profile use code-architect
honcho_profile
```

## Honcho Tool Specifications

### honcho_profile
Returns structured peer card:
```json
{
  "user": "Alexa",
  "preferences": {
    "language": "TypeScript",
    "editor": "VS Code",
    "theme": "dark",
    "methodology": "systematic skill-driven development",
    "principles": ["DRY", "stacked skill bundles", "MCP-first"]
  },
  "goals": ["prompt library maintenance", "full Hermes automation"],
  "working_style": "concise, action-first, blunt+technical"
}
```

### honcho_reasoning
Reasoning levels: minimal, low, medium, high, max
- high: Synthesizes patterns across sessions, identifies preferences, predicts needs
- max: Deep analysis with full context, generates actionable recommendations

### honcho_conclude
Saves structured observations for future retrieval:
- Fact type: preference, goal, working_style, project_context
- Confidence: high/medium/low
- Source sessions: list of session IDs

## Verification Steps

```bash
# Full honcho test suite
echo "=== Honcho MCP ==="
hermes mcp test honcho

echo "=== Profile ==="
honcho_profile

echo "=== Context ==="
honcho_context

echo "=== Reasoning (high) ==="
honcho_reasoning level=high "What are my coding preferences and working style?"

echo "=== Search ==="
honcho_search "TypeScript dark theme"

echo "=== Conclude ==="
honcho_conclude "User prefers TypeScript with VS Code dark theme, systematic skill-driven development, DRY principles, stacked skill bundles, MCP-first tool precedence"

# Cross-session test: would need new session
```

## Risks

- **Honcho MCP may not be configured** — Requires API key, endpoint setup
- **Hybrid mode complexity** — Auto-inject + tools may have conflicts
- **Memory bloat** — Need deduplication strategy
- **Profile isolation** — Memories should be accessible across profiles but respect profile context

## References

- MEMORY.md: "Honcho Memory: Active (hybrid mode). Use honcho_profile/context/reasoning/search as needed."
- `~/AppData/Local/hermes/scripts/verify_sync.py` — includes honcho checks
- Honcho docs: https://honcho.dev/docs/llms.txt