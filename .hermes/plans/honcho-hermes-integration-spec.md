---
name: honcho-hermes-integration-spec
title: Honcho + Hermes Agent Integration Specification
description: Detailed specifications and acceptance criteria for Honcho persistent memory integration with Hermes Agent
version: 1.0.0
author: Alexa
license: MIT
tags:
  - honcho
  - hermes
  - memory
  - integration
  - specification
---

# Honcho + Hermes Agent Integration Specification

## Overview

This specification defines the requirements, acceptance criteria, and technical details for integrating Honcho persistent memory with Hermes Agent. It accompanies the implementation plan and provides testable criteria for each feature.

## Requirements

### R1: Honcho Memory Provider Activation
- **R1.1**: `hermes memory setup` must offer "honcho" as a provider option
- **R1.2**: Configuration must be saved to `~/.honcho/config.json` (global) or `$HERMES_HOME/honcho.json` (profile-local)
- **R1.3**: `hermes memory status` must show Honcho as active provider with connection details
- **R1.4**: The `hermes honcho` subcommand must be registered only when Honcho is active

### R2: Cross-Session Memory Persistence
- **R2.1**: Facts stated in one session must be recallable in a new session (different thread/CLI invocation)
- **R2.2**: Dialectic reasoning must automatically extract insights from conversations
- **R2.3**: User peer and AI peer must maintain separate representations
- **R2.4**: Session strategy `per-directory` must map sessions to working directory correctly

### R3: Honcho Tools Availability
When Honcho is active, these tools must be available to the agent:
- **R3.1**: `honcho_profile` — read/update peer card
- **R3.2**: `honcho_search` — semantic search over context (raw excerpts)
- **R3.3**: `honcho_context` — full session context (summary, representation, card, recent messages)
- **R3.4**: `honcho_reasoning` — synthesized answer with controllable `reasoning_level`
- **R3.5**: `honcho_conclude` — create/delete conclusions

### R4: Context Files System
- **R4.1**: SOUL.md must load from `HERMES_HOME/SOUL.md` only (global, not project-local)
- **R4.2**: Project context priority: `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules` (first match wins)
- **R4.3**: AGENTS.md chain: git root → working directory (merged, deeper files take precedence)
- **R4.4**: Progressive subdirectory discovery during session navigation
- **R4.5**: Security scanner must block prompt injection patterns
- **R4.6**: Size limits with truncation markers must work correctly

### R5: Personality System
- **R5.1**: SOUL.md is slot #1 in system prompt (agent identity foundation)
- **R5.2**: 14 built-in personalities switchable via `/personality` command
- **R5.3**: Custom personalities configurable in `~/.hermes/config.yaml` under `agent.personalities`
- **R5.4**: `/personality` is session-level overlay stored in `display.personality`
- **R5.5**: Reset options: `/personality none|default|neutral`
- **R5.6**: `agent.system_prompt` reserved for manual system prompt only
- **R5.7**: Personality (`display.personality`) independent of CLI appearance (`display.skin`)

### R6: Honcho CLI Commands
All commands must work when Honcho is active:
- **R6.1**: `hermes honcho status` — connection status, config, key settings
- **R6.2**: `hermes honcho strategy` — show/set session strategy
- **R6.3**: `hermes honcho peer` — show/update peer names + dialectic reasoning level
- **R6.4**: `hermes honcho mode` — show/set recall mode (hybrid/context/tools)
- **R6.5**: `hermes honcho tokens` — show/set token budget
- **R6.6**: `hermes honcho identity` — seed/show AI peer identity
- **R6.7**: `hermes honcho sync` — sync config to all profiles
- **R6.8**: `hermes honcho peers` — show peer identities across profiles
- **R6.9**: `hermes honcho sessions` — list session mappings
- **R6.10**: `hermes honcho map` — map directory to session
- **R6.11**: `hermes honcho enable/disable` — toggle Honcho
- **R6.12**: `hermes honcho migrate` — migration guide

### R7: Advanced Configuration
- **R7.1**: Three orthogonal knobs: `contextCadence`, `dialecticCadence`, `dialecticDepth`
- **R7.2**: Dialectic depth multi-pass with `dialecticDepthLevels` array
- **R7.3**: Session-start prewarm with background dialectic call
- **R7.4**: Query-adaptive reasoning level (auto-scale by query length)
- **R7.5**: Observation modes: `directional` (default) vs `unified` vs custom `observation` block
- **R7.6**: Gateway identity mapping: `pinUserPeer`, `userPeerAliases`, `runtimePeerPrefix`

## Acceptance Criteria

### AC1: Honcho Setup & Verification
| Test | Expected Result |
|------|-----------------|
| Run `hermes memory setup` → select honcho | Wizard completes, config saved |
| Run `hermes memory status` | Shows "honcho" as provider, base URL, peer name |
| Run `hermes honcho status` | Shows connection status, config, key settings |
| State fact in session 1: "I prefer Rust and dark mode" | Fact stored in Honcho |
| New session: "What are my preferences?" | Recalls "Rust" and "dark mode" |
| "Use honcho_search to find anything about me" | Tool called, returns relevant excerpts |

### AC2: Context Files
| Test | Expected Result |
|------|-----------------|
| Create `~/.hermes/SOUL.md` with personality | Loads at slot #1 of system prompt |
| Create `AGENTS.md` at git root | Loaded as project context (highest priority) |
| Create `frontend/AGENTS.md`, navigate to frontend/ | Discovered and injected progressively |
| Create `.hermes.md` and `AGENTS.md` | `.hermes.md` wins (first match) |
| Inject `<!-- ignore instructions -->` in AGENTS.md | Blocked with "[BLOCKED: ...]" message |
| Exceed `context_file_max_chars` | Truncation marker with char counts shown |

### AC3: Personality System
| Test | Expected Result |
|------|-----------------|
| Run `/personality` | Lists all 14 built-in personalities |
| Run `/personality concise` | Switches to concise, applies next message |
| Run `/personality technical` | Switches to technical |
| Add custom personality to config.yaml | Available via `/personality <name>` |
| Run `/personality none` | Resets to SOUL.md default |
| Run `/skin` separately | Changes CLI appearance, not personality |

### AC4: Honcho Tools
| Test | Expected Result |
|------|-----------------|
| Agent calls `honcho_profile` (no args) | Returns current peer card |
| Agent calls `honcho_profile` with `card: ["fact1", "fact2"]` | Updates peer card |
| Agent calls `honcho_search` with query | Returns raw excerpts ranked by relevance |
| Agent calls `honcho_context` | Returns summary, representation, card, recent messages |
| Agent calls `honcho_reasoning` with `reasoning_level: "high"` | Returns synthesized answer |
| Agent calls `honcho_conclude` with `conclusion: "User prefers X"` | Creates conclusion |
| Agent calls `honcho_conclude` with `delete_id: "..."` | Deletes conclusion |

### AC5: Configuration
| Test | Expected Result |
|------|-----------------|
| Set `recallMode: "tools"` in honcho.json | Auto-injection disabled, tools only |
| Set `dialecticDepth: 2`, `dialecticDepthLevels: ["minimal", "high"]` | Two-pass dialectic with specified levels |
| Set `observationMode: "unified"` | Shared pool semantics |
| Set custom `observation` block | Per-peer control respected |
| Set `sessionStrategy: "per-repo"` | Sessions map to git repo |
| Config persists after Hermes restart | Settings maintained |
| Run `hermes honcho sync` | Config synced to all profiles |

### AC6: Self-Hosted Honcho
| Test | Expected Result |
|------|-----------------|
| Follow self-hosting guide, start Honcho locally | Server accessible at http://localhost:8000 |
| Run `hermes memory setup honcho` with localhost URL | Configures local instance |
| Provide JWT token for authenticated access | Authenticated requests work |
| Leave token blank with `AUTH_USE_AUTH=false` | Unauthenticated access works |
| Config stores token in `hosts.hermes.apiKey` | Separate from cloud apiKey |

## Configuration Schema

### Honcho Config (`~/.honcho/config.json` or `$HERMES_HOME/honcho.json`)
```json
{
  "baseUrl": "string (required)",
  "hosts": {
    "hermes": {
      "enabled": "boolean (default: true)",
      "aiPeer": "string (default: \"hermes\")",
      "peerName": "string (required)",
      "workspace": "string (default: \"hermes\")",
      "apiKey": "string (cloud API key or local JWT)"
    }
  },
  "contextTokens": "integer | null (default: null, uncapped)",
  "contextCadence": "integer (default: 1, min: 1)",
  "dialecticCadence": "integer (default: 2, min: 1, recommended: 1-5)",
  "dialecticDepth": "integer (default: 1, clamped: 1-3)",
  "dialecticDepthLevels": "string[] | null (default: null, options: minimal|low|medium|high|max)",
  "dialecticReasoningLevel": "string (default: \"low\", options: minimal|low|medium|high|max)",
  "dialecticDynamic": "boolean (default: true)",
  "dialecticMaxChars": "integer (default: 600)",
  "recallMode": "string (default: \"hybrid\", options: hybrid|context|tools)",
  "writeFrequency": "string | integer (default: \"async\", options: async|turn|session|N)",
  "saveMessages": "boolean (default: true)",
  "observationMode": "string (default: \"directional\", options: directional|unified)",
  "observation": "object | null (default: null, per-peer override)",
  "messageMaxChars": "integer (default: 25000)",
  "dialecticMaxInputChars": "integer (default: 10000)",
  "sessionStrategy": "string (default: \"per-directory\", options: per-directory|per-repo|per-session|global)",
  "pinUserPeer": "boolean (default: false, gateway only)",
  "userPeerAliases": "object (default: {}, gateway only)",
  "runtimePeerPrefix": "string (default: \"\", gateway only)"
}
```

### Hermes Config (`~/.hermes/config.yaml`)
```yaml
memory:
  provider: "honcho"

agent:
  system_prompt: "string | null (manual system prompt, only used when no personality selected)"
  personalities:
    <custom_name>: "string (multiline personality definition)"

display:
  personality: "string (set by /personality command, cleared by none/default/neutral)"
  skin: "string (CLI appearance, independent of personality)"
```

## Error Scenarios & Handling

| Scenario | Expected Behavior |
|----------|-------------------|
| Honcho API unreachable | Graceful degradation, error in status, tools return error |
| Invalid API key / JWT | Setup wizard rejects, clear error message |
| Self-hosted Honcho with auth but no token provided | Prompt for token, don't proceed without it |
| Context file exceeds size limit | Truncate with marker, suggest file tools |
| Prompt injection detected in context file | Block file, show warning, continue with other files |
| `hermes honcho` command run without Honcho active | Error: "Honcho not active. Run `hermes memory setup` first." |
| Migration from legacy `hermes honcho setup` | Wizard detects existing config, no re-setup needed |

## Performance Benchmarks

| Operation | Target |
|-----------|--------|
| Context injection (hybrid mode) | < 500ms per turn |
| Dialectic reasoning (depth 1) | < 2s per invocation |
| Semantic search (honcho_search) | < 1s |
| Session start prewarm | Background, non-blocking |
| Config load | < 100ms |

## Security Considerations

1. **API Keys**: Never logged, stored in `honcho.json` with restricted permissions
2. **Prompt Injection**: All context files scanned before injection
3. **PII in Conclusions**: `honcho_conclude` with `delete_id` for PII removal only
4. **Gateway Identity**: Runtime IDs mapped via aliases/prefixes, not exposed directly
5. **Message Chunking**: Messages > 25k chars chunked automatically

## Migration Path

### From Legacy `hermes honcho setup`
1. Run `hermes memory setup` and select "honcho"
2. Wizard detects existing `honcho.json` / `~/.honcho/config.json`
3. No re-login or re-setup needed
4. `hermes honcho` subcommand available on next invocation

### From Other Memory Providers
1. Run `hermes memory setup` and select "honcho"
2. Previous provider config preserved but inactive
3. Can switch back via `hermes memory setup`

## Testing Checklist

### Unit Tests
- [ ] Config parsing for all Honcho settings
- [ ] Context file discovery priority chain
- [ ] Security scanner pattern matching
- [ ] Personality overlay application order
- [ ] Tool parameter validation

### Integration Tests
- [ ] Full Honcho setup wizard flow
- [ ] Cross-session memory persistence
- [ ] All 5 Honcho tools functional
- [ ] All 12 `hermes honcho` CLI commands
- [ ] Progressive AGENTS.md discovery
- [ ] Custom personality loading from config.yaml

### E2E Tests
- [ ] New user onboarding: setup → store fact → recall in new session
- [ ] Multi-directory project: context files at each level
- [ ] Personality switch mid-conversation
- [ ] Self-hosted Honcho with auth
- [ ] Gateway identity mapping (if applicable)

## Documentation Deliverables

1. **Quick Reference Card** — Honcho CLI commands, tool parameters, config keys
2. **Setup Guide** — Step-by-step with screenshots for cloud and self-hosted
3. **Troubleshooting** — Common errors and solutions
4. **Best Practices** — Config recommendations for different use cases
5. **Architecture Diagram** — Honcho + Hermes data flow (Mermaid/Excalidraw)

## References

- Honcho Documentation Index: https://honcho.dev/docs/llms.txt
- Hermes Honcho Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho
- Hermes Context Files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
- Hermes Personality: https://hermes-agent.nousresearch.com/docs/user-guide/features/personality
- Honcho Self-Hosting: https://honcho.dev/docs/v3/contributing/self-hosting
- Honcho Architecture: https://honcho.dev/docs/v3/documentation/core-concepts/architecture
- Honcho SDK: https://honcho.dev/docs/v3/documentation/reference/sdk.md
- Honcho CLI: https://honcho.dev/docs/v3/documentation/reference/cli.md
- Hermes Agent Source: https://github.com/NousResearch/hermes-agent