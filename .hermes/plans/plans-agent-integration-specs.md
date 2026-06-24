---
title: "Plans Agent Integration Specs"
source: "docs/plans/agent-integration-specs.md"
---

# Feature Specification: Multi-Agent ACPX Integration

## 1. Overview

**Goal:** Integrate Qwen Code, OpenCode, and GitHub Copilot CLI as first-class ACPX coding agents within the Hermes Agent ecosystem, enabling seamless delegation of coding tasks to the optimal agent.

**Context:** The SandBox environment already has all three agents installed but lacks structured ACPX integration, unified configuration, and skill-based agent selection workflows.

**Acceptance Criteria:**
- Each agent can be invoked from Hermes via ACPX
- Each agent has a dedicated Hermes skill with workflow instructions
- All agents share common MCP servers where applicable
- Agent routing is documented and configurable
- All three pass a real coding task smoke test

---

## 2. Agent Specifications

### 2.1 Qwen Code

**Current State:**
- Version: 0.17.0
- Auth: Uses OpenRouter API key, need to verify active auth
- Config: `~/.qwen/settings.json` with OpenRouter models
- Default model: `z-ai/glm-4.5-air:free`

**Required Configuration:**
| Setting | Value | Source |
|---------|-------|--------|
| ACP Provider Name | `qwen-code` | Hermes config.yaml |
| Base URL | `acp://qwen` | ACP protocol |
| Default Model | `qwen3.6-plus` | Qwen settings |
| Auth Method | API key via env | `QWEN_CUSTOM_API_KEY` or OpenRouter |

**Verification Test:**
```bash
qwen -p "Write a hello world Python script"
```

**Skill Content Needed:**
- Installation/upgrade commands
- Auth setup steps
- ACPX integration pattern
- Usage examples
- Common pitfalls

### 2.2 OpenCode

**Current State:**
- Version: 1.15.12
- Auth: Provider-configured (OpenRouter shown in config)
- Config: `~/.config/opencode/opencode.json`
- Model: `opencode/qwen3.6-plus-free`
- Plugins: 19 active plugins including handoff, DCP, smart-codebase, etc.
- MCP: context7, exa, filesystem, gh_grep, playground, sequential-thinking, memory, next-devtools, MCP_DOCKER

**Required Configuration:**
| Setting | Value | Source |
|---------|-------|--------|
| ACP Provider Name | `opencode` | Hermes config.yaml |
| Default Agent | `build` | OpenCode agent |
| Model | Configurable via flag | `--model` flag |

**Verification Test:**
```bash
opencode run "Respond with exactly: OPENCODE_SMOKE_OK"
```

**Skill Updates Needed:**
- ACPX delegation pattern
- Plugin usage guidance
- Multi-agent (build/plan) switching

### 2.3 GitHub Copilot CLI

**Current State:**
- Version: 1.0.33
- Auth: Requires GitHub Copilot subscription
- Config: `~/.copilot/config.json`
- Default Model: Claude Sonnet 4.5
- Hermes already has `copilot-acp` provider configured

**Required Configuration:**
| Setting | Value | Source |
|---------|-------|--------|
| ACP Provider Name | `copilot-cli` | Hermes config.yaml |
| Auth | GH_TOKEN or interactive login | GitHub PAT |
| Default Model | claude-sonnet-4.5 | `/model` command |

**Verification Test:**
```bash
copilot -p "Explain what 'ls -la' does"
```

---

## 3. Hermes ACPX Configuration

### 3.1 Config.yaml Entries

```yaml
# Existing copilot-acp provider (already configured)
providers:
  copilot-acp:
    # Already in config.yaml

# New: OpenCode ACP provider
  opencode-acp:
    api_mode: chat_completions
    base_url: acp://opencode

# New: Qwen Code ACP provider  
  qwen-code:
    api_mode: chat_completions
    base_url: acp://qwen
```

### 3.2 Agent Routing Table

| Task Type | Recommended Agent | Fallback |
|-----------|------------------|----------|
| Quick explain/suggest | Copilot CLI | Qwen Code |
| Refactoring | OpenCode | Qwen Code |
| Code review | OpenCode (plan agent) | Copilot CLI |
| Large codebase exploration | Qwen Code | OpenCode |
| Test generation | OpenCode | Copilot CLI |
| Architecture/design | OpenCode (plan agent) | Qwen Code |

---

## 4. Shared Ecosystem

### 4.1 Common MCP Servers
All agents should share these MCP servers where protocol-compatible:
- filesystem (local)
- sequential-thinking
- context7 (documentation)

### 4.2 Shared Skills
Hermes skills that reference these agents should:
- Use consistent invocation patterns
- Document fallback chains
- Share environment variables where possible

### 4.3 Hook Integration
Hooks for:
- Pre-coding task setup (workdir creation, branch check)
- Post-coding task verification (test run, diff review)
- Error handling (agent fallback on failure)

---

## 5. Acceptance Criteria

### 5.1 Per-Agent
- [ ] Agent responds to direct CLI invocation
- [ ] Agent accepts ACPX-style prompts
- [ ] Agent can perform a real coding task (write + test code)
- [ ] Agent auth is verified and documented

### 5.2 Integration
- [ ] Hermes can delegate to each agent via ACPX
- [ ] Cross-agent task handoff works
- [ ] Common MCP servers accessible from all agents
- [ ] Skills exist for each agent with complete workflow docs

### 5.3 Documentation
- [ ] PLAN.md outlines implementation phases
- [ ] SPECS.md defines acceptance criteria
- [ ] Each agent has a skill with setup/usage/pitfalls
- [ ] AGENTS.md updated with agent integration notes
