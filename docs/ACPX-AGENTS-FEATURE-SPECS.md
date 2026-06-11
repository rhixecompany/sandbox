# ACPX Coding Agents — Feature Specifications

> Linked to: `docs/ACPX-AGENTS-COMPREHENSIVE-PLAN.md`
> Version: 1.0.0
> Status: Draft

---

## Feature 1: ACPX-Integrated Qwen Code Agent

**Plan Reference:** Phase 2 (Tasks 2.1–2.4)

### 1.1 Description
Qwen Code v0.17.0 installed via Bun, authenticated via OpenRouter API key, configured as a Hermes ACP provider (`qwen-code`), usable for all coding tasks via `qwen "prompt" --yolo` or optionally via Hermes ACPX routing.

### 1.2 Acceptance Criteria
| ID | Criterion | Verification Method |
|----|-----------|--------------------|
| F1-1 | `qwen --version` returns 0.17.0 | `terminal()` |
| F1-2 | `qwen "prompt" --yolo` works with OpenRouter | `terminal()` with `QWEN_CODE_SUPPRESS_YOLO_WARNING=1` |
| F1-3 | `~/.qwen/settings.json` has OpenRouter provider configured | `read_file()` |
| F1-4 | `~/.qwen/oauth_creds.json` NOT required (OpenRouter, not DashScope) | `test -f` returns false |
| F1-5 | Hermes `config.yaml` has `qwen-code` provider entry | grep config.yaml |
| F1-6 | `qwen-code` skill exists and is current | `skill_view()` |
| F1-7 | Research doc at `docs/research/qwen-code-research.md` | `read_file()` |
| F1-8 | Can generate working Python code (Fibonacci, merge sort, etc.) | `terminal()` test |
| F1-9 | Fallback chain defined for Qwen Code failures | Checked in acpx-agent-routing skill |

### 1.3 Configuration
- **Binary:** `~/.bun/bin/qwen` (installed via Bun)
- **Auth:** `OPENROUTER_API_KEY` in `~/.qwen/settings.json` → `env` section
- **Model:** `openai/gpt-oss-120b:free` (OpenRouter)
- **Headless flag:** `--yolo` required for non-interactive
- **ACP provider:** `qwen-code` → `base_url: acp://qwen`
- **Warning suppress:** `QWEN_CODE_SUPPRESS_YOLO_WARNING=1`

### 1.4 Dependencies
- Bun runtime (`~/.bun/bin/bun`)
- OpenRouter API key (sk-or-...)
- Internet connectivity

### 1.5 Usage Examples
```bash
# Direct usage
qwen "Write a Python function to merge two sorted lists" --yolo

# With env var to suppress yolo warning
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo "Implement LRU cache"

# From Hermes via terminal
terminal(command="qwen 'Explain the Singleton pattern in Python' --yolo", timeout=60)
```

---

## Feature 2: ACPX-Integrated OpenCode AI Agent

**Plan Reference:** Phase 3 (Tasks 3.1–3.5)

### 2.1 Description
OpenCode AI v1.15.12+ installed via npm, authenticated with at least one provider (GitHub Copilot, Google, OpenCode Zen), configured as a Hermes ACP provider (`opencode-acp`), usable for all coding tasks via `opencode run "prompt"`.

### 2.2 Acceptance Criteria
| ID | Criterion | Verification Method |
|----|-----------|--------------------|
| F2-1 | `opencode --version` returns 1.15.12+ | `terminal()` |
| F2-2 | `opencode auth list` shows ≥1 provider | `terminal()` |
| F2-3 | `opencode run "prompt"` works with model flag | `terminal()` with `--model opencode/...` |
| F2-4 | `opencode acp --help` shows ACP server options | `terminal()` |
| F2-5 | Hermes `config.yaml` has `opencode-acp` provider entry | grep config.yaml |
| F2-6 | `opencode` (autonomous-ai-agents) skill exists and is current | `skill_view()` |
| F2-7 | Research doc at `docs/research/opencode-research.md` | `read_file()` |
| F2-8 | Can generate working code with tests | `terminal()` test |
| F2-9 | Provider selection works (model prefix `opencode/`) | Verified in docs |

### 2.3 Configuration
- **Binary:** From npm global (`opencode`)
- **Auth:** `opencode auth login` or env vars
- **Model prefix:** `opencode/` required (e.g., `opencode/claude-haiku-4-5`)
- **ACP provider:** `opencode-acp` → `base_url: acp://opencode`
- **ACP mode:** `opencode acp` starts ACP server
- **Skip interactive:** `opencode run "prompt"` (no pty needed)

### 2.4 Dependencies
- Node.js 18+
- npm global install (`npm i -g opencode-ai@latest`)
- Provider credentials (Copilot subscription, Google AI key, or OpenCode Zen token)

### 2.5 Usage Examples
```bash
# One-shot coding task
opencode run "Add retry logic to API calls and update tests"

# With specific model
opencode run "Review this config for security issues" --model opencode/claude-haiku-4-5

# With context files
opencode run "Refactor this module" -f src/auth.py -f tests/test_auth.py

# ACP server mode
opencode acp --port 8080

# Code review (plan agent)
opencode run "Review PR for security issues" --agent plan
```

---

## Feature 3: ACPX-Integrated Copilot CLI Agent

**Plan Reference:** Phase 4 (Tasks 4.1–4.5)

### 3.1 Description
GitHub Copilot CLI v1.0.33+ installed via npm, authenticated via GH_TOKEN, configured as a Hermes ACP provider (`copilot-acp`), usable for quick explanations and GitHub-native tasks. Note: subject to weekly rate limits (~50 premium requests/week).

### 3.2 Acceptance Criteria
| ID | Criterion | Verification Method |
|----|-----------|--------------------|
| F3-1 | `copilot --version` returns 1.0.33+ | `terminal()` |
| F3-2 | `GH_TOKEN` or `GITHUB_TOKEN` env var set | `echo $GH_TOKEN` |
| F3-3 | `copilot -p "prompt"` responds (may be rate limited) | `terminal()` |
| F3-4 | Hermes `config.yaml` has `copilot-acp` provider entry | grep config.yaml |
| F3-5 | `copilot-cli` (autonomous-ai-agents) skill exists and is current | `skill_view()` |
| F3-6 | Research doc at `docs/research/copilot-cli-research.md` | `read_file()` |
| F3-7 | Rate limit status documented in skill | Check skill |
| F3-8 | Fallback agents defined for when Copilot is rate limited | Check acpx-agent-routing |

### 3.3 Configuration
- **Binary:** From npm global (`copilot`)
- **Auth:** `GH_TOKEN` env var with "Copilot Requests" permission
- **ACP provider:** `copilot-acp` → `base_url: acp://copilot`
- **Rate limit:** ~50 premium requests/week, resets Sunday/Monday UTC
- **Default model:** Claude Sonnet 4.5

### 3.4 Dependencies
- GitHub Copilot subscription (Free, Pro, Pro+, Business, or Enterprise)
- npm global install (`npm i -g @github/copilot`)
- GH_TOKEN with Copilot Requests scope

### 3.5 Usage Examples
```bash
# Quick explanation
copilot -p "Explain what 'git bisect' does"

# Code generation
copilot -p "Write a JavaScript debounce function"

# From Hermes via terminal
terminal(command="copilot -p 'Explain this shell command: find . -name *.py -exec wc -l {} +'", timeout=30)
```

---

## Feature 4: ACPX Agent Routing & Orchestration

**Plan Reference:** Phase 5 (Tasks 5.1–5.5)

### 4.1 Description
Centralized agent routing skill (`acpx-agent-routing`) that dispatches coding tasks to the optimal agent based on task type, current agent availability, and rate limit status.

### 4.2 Acceptance Criteria
| ID | Criterion | Verification Method |
|----|-----------|--------------------|
| F4-1 | `acpx-agent-routing` skill exists in autonomous-ai-agents | `skill_view()` |
| F4-2 | Routing table covers: code-gen, review, debug, explain, refactor | Read skill |
| F4-3 | Fallback chain defined for each task type | Read skill |
| F4-4 | Rate limit awareness integrated (Copilot CLI spillover) | Read skill |
| F4-5 | Hermes config.yaml has all 3 providers registered | grep config.yaml |
| F4-6 | All 3 agent skills reference the routing skill | grep in skills |

### 4.3 Agent Routing Table

| Task Type | Primary | Fallback 1 | Fallback 2 |
|-----------|---------|------------|------------|
| Quick explanation | Copilot CLI | Qwen Code | OpenCode |
| Code generation | OpenCode | Qwen Code | Copilot CLI |
| Refactoring | OpenCode | Copilot CLI | Qwen Code |
| Code review | OpenCode (plan) | Copilot CLI | Qwen Code |
| Large codebase exploration | Qwen Code | OpenCode | — |
| Test generation | OpenCode | Qwen Code | Copilot CLI |
| Architecture/design | OpenCode (plan) | Qwen Code | — |
| Debugging | OpenCode | Qwen Code | Copilot CLI |
| PR review | Copilot CLI | OpenCode | — |

---

## Feature 5: Research Documentation

**Plan Reference:** Phase 1 (Tasks 1.1–1.3)

### 5.1 Description
Three markdown research documents in `docs/research/` containing latest official documentation, guides, cheatsheets, and ACPX integration info extracted from web sources for each agent.

### 5.2 Acceptance Criteria
| ID | Criterion | Verification Method |
|----|-----------|--------------------|
| F5-1 | `docs/research/qwen-code-research.md` exists | `read_file()` |
| F5-2 | `docs/research/opencode-research.md` exists | `read_file()` |
| F5-3 | `docs/research/copilot-cli-research.md` exists | `read_file()` |
| F5-4 | Each doc has: overview, install, auth, config, usage, ACPX, pitfalls | Structure check |
| F5-5 | Content from at least 3 web sources per doc | Cross-check URLs |
| F5-6 | Docs reference latest versions | Version check |

---
