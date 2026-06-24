---
title: "Acpx Agents Comprehensive Plan"
source: "docs/ACPX-AGENTS-COMPREHENSIVE-PLAN.md"
---

# ACPX Coding Agents — Comprehensive Implementation Plan

> **Goal:** Fully install, configure, authenticate, and verify three ACPX-enabled coding agents (Qwen Code, OpenCode AI, Copilot CLI) integrated with Hermes for all coding tasks via ACPX protocol. Create all supporting plugins, skills, hooks, MCP servers, and configuration changes. Document everything with live research data.

**Architecture:** Three independent ACPX agents each wire into Hermes via their respective ACP providers. Each agent gets a dedicated Hermes provider entry (`opencode-acp`, `copilot-acp`, `qwen-code`), ACPX routing skill updates, MCP server registration where applicable, and end-to-end smoke tests. The agent-routing skill (`acpx-agent-routing`) becomes the orchestrator that dispatches tasks to the right agent.

**Tech Stack:** Qwen Code v0.17.0 (Bun), OpenCode AI v1.15.12 (npm), Copilot CLI v1.0.33 (npm), Hermes Agent (config.yaml), OpenRouter API (auth bridge)

**Deliverables:**
- `docs/ACPX-AGENTS-COMPREHENSIVE-PLAN.md` — this plan
- `docs/ACPX-AGENTS-FEATURE-SPECS.md` — linked feature specifications
- `docs/research/qwen-code-research.md` — latest Qwen Code docs/guides
- `docs/research/opencode-research.md` — latest OpenCode AI docs/guides
- `docs/research/copilot-cli-research.md` — latest Copilot CLI docs/guides
- Updated Hermes `config.yaml` — all ACP providers registered
- Updated/created skills: `acpx-agent-routing`, `qwen-code` (skill), `opencode`, `copilot-cli`
- ACPX smoke test results for each agent
- Cross-reference verification report

---

## Phase 1: Research & Documentation (Phases 2–4)

### Task 1.1: Web search Qwen Code documentation

**Objective:** Find latest official docs, guides, cheatsheets, ACPX integration docs for Qwen Code v0.17.0

**Search queries:**
- "Qwen Code CLI ACPX setup guide"
- "Qwen Code v0.17.0 documentation"
- "Qwen Code headless usage OpenRouter"

**Deliverable:** `docs/research/qwen-code-research.md`

### Task 1.2: Web search OpenCode AI documentation

**Objective:** Find latest official docs, ACPX configuration, provider setup for OpenCode AI

**Search queries:**
- "OpenCode AI ACPX configuration"
- "OpenCode CLI setup guide providers"
- "opencode acp server mode documentation"

**Deliverable:** `docs/research/opencode-research.md`

### Task 1.3: Web search Copilot CLI documentation

**Objective:** Find latest Copilot CLI docs, rate limit info, ACPX integration

**Search queries:**
- "GitHub Copilot CLI ACPX setup"
- "copilot CLI authentication GH_TOKEN"
- "Copilot CLI rate limits weekly quota"

**Deliverable:** `docs/research/copilot-cli-research.md`

---

## Phase 2: Qwen Code Setup & ACPX Integration (Phase 5)

### Task 2.1: Verify current Qwen Code installation state

**Step 1:** Check version and binary
```
which qwen
qwen --version
```

**Step 2:** Check settings.json for OpenRouter config
```
cat ~/.qwen/settings.json
```

**Step 3:** Check auth state
```
qwen "Reply with exactly: QWEN_ALIVE" --yolo
```

**Expected:** Qwen v0.17.0 installed via Bun, OpenRouter configured, responds with "QWEN_ALIVE"

### Task 2.2: Integrate Qwen Code as ACPX provider in Hermes

**Step 1:** Check current Hermes config.yaml providers section
```
grep -A 5 'providers:' ~/AppData/Local/hermes/config.yaml
```

**Step 2:** Create Qwen Code ACP provider entry
Add to config.yaml providers:
```yaml
  qwen-code:
    base_url: acp://qwen
    api_mode: chat_completions
```

**Step 3:** Create Qwen Code model provider plugin
If `plugins/model-providers/qwen-oauth/` doesn't already have a proper ACP-compatible plugin, create one.

### Task 2.3: Create/update Qwen Code skill

**Step 1:** Check current qwen-code skill
```
skill_view(name="qwen-code")
```

**Step 2:** Update/create qwen-code SKILL.md with:
- OpenRouter auth method (not DashScope OAuth)
- ACPX integration instructions
- Headless usage patterns
- Common pitfalls (--yolo requirement, env vars)

### Task 2.4: Smoke test Qwen Code via ACPX

**Step 1:** Direct CLI test
```
qwen "Write a Python function to merge two sorted lists" --yolo
```

**Step 2:** Verify Hermes can route to qwen-code provider (if ACPX wired)

---

## Phase 3: OpenCode AI Setup & ACPX Integration (Phase 6)

### Task 3.1: Verify current OpenCode installation state

**Step 1:** Check version
```
opencode --version
```

**Step 2:** Check auth providers
```
opencode auth list
```

**Expected:** OpenCode v1.15.12+, at least one provider authenticated (GitHub Copilot, Google, or OpenCode Zen)

### Task 3.2: Verify OpenCode ACP provider in Hermes

**Step 1:** Check config.yaml for opencode-acp provider
```
grep -A 5 'opencode-acp' ~/AppData/Local/hermes/config.yaml
```

**Step 2:** Ensure ACP provider is properly configured:
```yaml
  opencode-acp:
    base_url: acp://opencode
    api_mode: chat_completions
```

### Task 3.3: Verify OpenCode ACP server mode

**Step 1:** Test ACP server help
```
opencode acp --help
```

**Step 2:** Quick one-shot test
```
opencode run "Reply with exactly: OPENCODE_ALIVE" --model opencode/claude-haiku-4-5
```

### Task 3.4: Create/update OpenCode skill

Update opencode skill at `autonomous-ai-agents/opencode/SKILL.md` with:
- Current ACPX configuration specifics
- Provider list and auth methods
- Model prefix requirements (opencode/)
- Parallel execution patterns
- Pitfalls from actual usage

### Task 3.5: Smoke test OpenCode via ACPX

```
opencode run 'Write a Python function to find all primes up to N' --model opencode/claude-haiku-4-5
```

---

## Phase 4: Copilot CLI Setup & ACPX Integration (Phase 7)

### Task 4.1: Verify current Copilot CLI installation state

**Step 1:** Check version
```
copilot --version
```

**Step 2:** Check GH_TOKEN / auth state
```
echo $GH_TOKEN | head -c 10
copilot -p "Explain what 'git stash' does"
```

**Expected:** Copilot CLI v1.0.33+, GH_TOKEN configured, responds to prompts (may be rate limited)

### Task 4.2: Verify Copilot ACP provider in Hermes

**Step 1:** Check config.yaml for copilot-acp provider
```
grep -A 5 'copilot-acp' ~/AppData/Local/hermes/config.yaml
```

### Task 4.3: Manage rate limits and fallback strategy

**Step 1:** Check current rate limit status
```
copilot -p "check my quota"
```

**Step 2:** Document fallback chain in acpx-agent-routing skill:
- Primary: OpenCode (no rate limit)
- Fallback: Qwen Code (OpenRouter)
- Tertiary: Copilot CLI (rate limited, use sparingly)

### Task 4.4: Update Copilot CLI skill

Update `autonomous-ai-agents/copilot-cli/SKILL.md` with:
- Current rate limit status
- Fallback agent configuration
- GH_TOKEN auth specifics
- ACPX integration verification steps

### Task 4.5: Smoke test Copilot CLI

```
copilot -p "Write a one-line Python function to check if a string is a palindrome"
```

---

## Phase 5: Plugin, Skill, Hook & MCP Integration (Phase 8)

### Task 5.1: Audit current Hermes plugins

**Step 1:** List enabled plugins
```
grep -A 50 'enabled_plugins:' ~/AppData/Local/hermes/config.yaml | head -30
```

**Step 2:** Check if qwen-oauth plugin needs update or replacement

### Task 5.2: Create/update ACPX agent-routing skill

Update `autonomous-ai-agents/acpx-agent-routing/SKILL.md`:
- Current agent status (verified working)
- Updated routing table with actual performance data
- Fallback chains
- ACPX delegation patterns

### Task 5.3: Create ACPX hooks (if applicable)

Check if Hermes hooks directory exists and add ACPX routing hooks:
```
ls ~/AppData/Local/hermes/hooks/
```

### Task 5.4: MCP server integration

Check if any of the three agents need MCP server registration:
- Qwen Code: was looking at `qwen mcp` commands (removed in v0.17.0)
- OpenCode: no native MCP server
- Copilot CLI: LSP integration possible
- Document findings

### Task 5.5: Update Hermes config.yaml comprehensively

Ensure all three ACP providers are registered:
```yaml
providers:
  opencode-acp:
    base_url: acp://opencode
    api_mode: chat_completions
  copilot-acp:
    base_url: acp://copilot
    api_mode: chat_completions
  qwen-code:
    base_url: acp://qwen
    api_mode: chat_completions
```

---

## Phase 6: Full End-to-End Testing (Phase 9)

### Task 6.1: Qwen Code — ACPX coding test

```
qwen "Implement a Fibonacci generator in Python with memoization" --yolo
```
Verify: actual Python code output, correct implementation

### Task 6.2: OpenCode — ACPX coding test

```
opencode run 'Implement a LRU cache in Python with unit tests' --model opencode/claude-haiku-4-5
```
Verify: code + tests written, passes

### Task 6.3: Copilot CLI — ACPX explanation test

```
copilot -p "Explain Python decorators with examples"
```
Verify: explanation received (even if rate limited)

### Task 6.4: Agent routing skill test

Document which agent to use for which task type based on actual test results

---

## Phase 7: Verification & Cross-Reference Sweep (Phase 10)

### Task 7.1: Verify plan document against actual state

Cross-reference every task in this plan against real files on disk:
- [ ] All 3 research docs exist in docs/research/
- [ ] Hermes config.yaml has all 3 providers
- [ ] All 3 skills updated with current info
- [ ] ACPX agent-routing skill updated
- [ ] Smoke test results documented
- [ ] Plan + Feature Specs linked

### Task 7.2: Verify feature specs

Read FEATURE_SPECS.md and verify each acceptance criterion is met.

### Task 7.3: Final sweep

- [ ] No stale backups (.bak files)
- [ ] No duplicate skill entries
- [ ] All docs reference up-to-date commands
- [ ] Git commit with descriptive message

---

## Acceptance Criteria Matrix

| Criterion | Qwen Code | OpenCode AI | Copilot CLI |
|-----------|-----------|-------------|-------------|
| Installed | v0.17.0+ | v1.15.12+ | v1.0.33+ |
| Authenticated | OpenRouter key | Provider list ok | GH_TOKEN set |
| ACPX provider in config | qwen-code | opencode-acp | copilot-acp |
| Skill exists & updated | ✓ | ✓ | ✓ |
| Smoke test passed | ✓ | ✓ | ✓/rate-limited |
| Research doc saved | ✓ | ✓ | ✓ |
| Fallback defined | → OpenCode | → Copilot CLI | → OpenCode |

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Copilot CLI rate limited | High | Can't test fully | Fallback to OpenCode |
| Qwen ACPX not supported | Medium | Can't route via ACP | Use direct CLI |
| OpenCode model fails | Low | Test times out | Use `--format json` |
| Plugins missing | Low | Manual creation | Follow existing patterns |
