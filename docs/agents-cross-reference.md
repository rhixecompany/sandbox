---
title: Agent Cross-Reference — Copilot, Hermes, OpenCode
description:
  Maps agent definitions across three platforms with format details, purpose,
  and inconsistencies found.
tags: [agents, copilot, hermes, opencode, cross-reference]
---

## Agent Cross-Reference

## Runtime Truth Snapshot (2026-05-30)

### Confirmed working

- `hermes doctor`
- `hermes --version` → 0.15.1
- `opencode --version` → 1.15.12
- `opencode auth list` → 3 providers
- `copilot --version` → 1.0.56
- `qwen --version` → 0.17.0
- `acpx --version` → 0.10.0
- `acpx qwen exec "Reply with exactly: QWEN_ALIVE"`
- `acpx opencode exec "Reply with exactly: OPENCODE_ALIVE"`
- `copilot -p "Reply with exactly: COPILOT_ALIVE"`

### Confirmed broken or degraded

- `acpx opencode exec` may log NDJSON parse warnings when OpenCode plugin output
  includes non-JSON preamble lines.

### Documented but unverified

- Hermes-mediated OpenCode provider routing (`opencode-acp`) in the current
  machine configuration.

## Overview

Comprehensive inventory and mapping of agent definitions across all three AI
platforms used in this workspace.

---

## Platform Inventory

### Copilot — `.github/agents/` (5 agents)

| Agent     | File                 | Tools                                   | Model                          | Purpose                                                                                |
| --------- | -------------------- | --------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------- |
| Architect | `architect.agent.md` | search, githubRepo, web/fetch           | Auto (copilot)                 | Architecture planning — generate impl plans with scope, requirements, sequencing       |
| Debugger  | `debugger.agent.md`  | runCommands, search, githubRepo         | Auto (copilot)                 | Interactive debugging — diagnose runtime/integration issues                            |
| Reviewer  | `reviewer.agent.md`  | search, githubRepo, changes             | Auto (copilot)                 | Code review — correctness, security, regressions, test gaps                            |
| Qwen Code | `qwen-code.agent.md` | terminal, search, filesystem            | qwen/qwen3.6-plus (OpenRouter) | Large codebase automation, headless batch tasks via ACPX (`acpx qwen exec`)            |
| Hermes    | `hermes.agent.md`    | terminal, search, filesystem, web/fetch | Auto (Hermes fallback chain)   | Orchestration, delegation, platform integrations, memory via ACPX (`acpx hermes exec`) |

**Format:** `.agent.md` with YAML frontmatter (description, tools, model) +
markdown body. **Location:** Project-specific (`SandBox/.github/agents/`)
**Source:** Based on
[GitHub Awesome Copilot](https://github.com/github/awesome-copilot)

### Hermes — Profiles (6 profiles)

| Profile           | Model        | Alias             | Status | Purpose (inferred)              |
| ----------------- | ------------ | ----------------- | ------ | ------------------------------- |
| adminbot          | big-pickle   | adminbot          | Found  | Admin/infrastructure automation |
| code-architect    | gpt-5.4-mini | code-architect    | Found  | Architecture and code design    |
| creative-director | big-pickle   | creative-director | Found  | Creative/content generation     |
| exec-assistant    | big-pickle   | exec-assistant    | Found  | Executive/administrative tasks  |
| patient-tutor     | big-pickle   | patient-tutor     | Found  | Educational/teaching tasks      |
| research-analyst  | big-pickle   | research-analyst  | Found  | Research and analysis           |

**Format:** YAML config entries + profile directories under
`~/AppData/Local/hermes/profiles/`. **Location:** `~/AppData/Local/hermes/config.yaml` +
`~/AppData/Local/hermes/profiles/`

### OpenCode — `~/.config/opencode/agents/` (19+ agents)

| Agent               | File                       | Mode     | Purpose                                                                    |
| ------------------- | -------------------------- | -------- | -------------------------------------------------------------------------- |
| OpenCoder           | `opencoder.md`             | primary  | Orchestration agent — complex coding, architecture, multi-file refactoring |
| OpenCoderWorkflows  | `opencoder-workflows.md`   | subagent | 6-stage workflow definitions                                               |
| OpenCoderExamples   | `opencoder-examples.md`    | subagent | Execution patterns and examples                                            |
| CoderAgent          | `coder-agent.md`           | subagent | Individual coding subtask execution                                        |
| Reviewer            | `reviewer.md`              | subagent | Code review                                                                |
| TestEngineer        | `test-engineer.md`         | subagent | Testing after implementation                                               |
| BuildAgent          | `build-agent.md`           | subagent | Build and compilation tasks                                                |
| DevOpsSpecialist    | `devops-specialist.md`     | subagent | DevOps/infrastructure automation                                           |
| FrontendSpecialist  | `frontend-specialist.md`   | subagent | Frontend/UI development                                                    |
| ContextScout        | `contextscout.md`          | subagent | Context file discovery                                                     |
| ExternalScout       | `externalscout.md`         | subagent | External documentation fetching                                            |
| TaskManager         | `task-manager.md`          | subagent | Task decomposition and tracking                                            |
| Documentation       | `documentation.md`         | subagent | Documentation generation                                                   |
| WebSearchResearcher | `web-search-researcher.md` | subagent | Web research                                                               |
| CodebaseAnalyzer    | `codebase-analyzer.md`     | subagent | Codebase analysis                                                          |
| ThoughtAnalyzer     | `thoughts-analyzer.md`     | subagent | Thought/context analysis                                                   |
| ContextOrganizer    | `context-organizer.md`     | subagent | Context file organization                                                  |
| **QwenCode**        | `qwen-code.md`             | subagent | **Delegate to Qwen Code via ACPX (`acpx qwen exec`)**                      |
| **HermesAgent**     | `hermes-agent.md`          | subagent | **Delegate to Hermes via ACPX (`acpx hermes exec`)**                       |

**Format:** `.md` with YAML frontmatter (name, description, mode, temperature,
permission). **Location:** `~/.config/opencode/agents/`

---

## Cross-Reference Mapping

### Equivalent Agents Across Platforms

| Function              | Copilot (`.github/agents/`)        | Hermes Profile          | OpenCode (`~/.config/opencode/agents/`) |
| --------------------- | ---------------------------------- | ----------------------- | --------------------------------------- |
| Architecture/Planning | `architect`                        | `code-architect`        | `OpenCoder` (primary)                   |
| Code Review           | `reviewer`                         | —                       | `Reviewer`                              |
| Debugging             | `debugger`                         | —                       | `CoderAgent` (subagent)                 |
| Testing               | —                                  | —                       | `TestEngineer`, `CodebaseAnalyzer`      |
| DevOps                | —                                  | `adminbot`              | `DevOpsSpecialist`                      |
| Frontend              | —                                  | —                       | `FrontendSpecialist`                    |
| Documentation         | —                                  | —                       | `Documentation`                         |
| General Dev           | —                                  | `default` (big-pickle)  | `CoderAgent`                            |
| Creative              | —                                  | `creative-director`     | —                                       |
| Executive/Admin       | —                                  | `exec-assistant`        | —                                       |
| Education             | —                                  | `patient-tutor`         | —                                       |
| Research              | —                                  | `research-analyst`      | `WebSearchResearcher`                   |
| Context/Discovery     | —                                  | —                       | `ContextScout`, `ExternalScout`         |
| Task Management       | —                                  | —                       | `TaskManager`                           |
| **ACPX → Qwen Code**  | **`qwen-code`** (`acpx qwen exec`) | **`qwen-code` skill**   | **`QwenCode`** (`acpx qwen exec`)       |
| **ACPX → Hermes**     | **`hermes`** (`acpx hermes exec`)  | _(self)_                | **`HermesAgent`** (`acpx hermes exec`)  |
| **ACPX → OpenCode**   | —                                  | **`opencode` skill**    | _(self)_                                |
| **ACPX → Copilot**    | _(self)_                           | **`copilot-cli` skill** | —                                       |

### Inconsistencies Found

| #   | Issue                                                                                   | Severity | Fix                                                                         |
| --- | --------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------- |
| 1   | **No cross-references** — Copilot instructions don't mention Hermes or OpenCode agents  | Medium   | Added cross-reference section to copilot-instructions.md                    |
| 2   | **No agent inventory document** — no single source of truth for which agents exist      | Medium   | Created this document (`docs/agents-cross-reference.md`)                    |
| 3   | **Format mismatch** — Copilot uses `.agent.md`, OpenCode uses `.md`, Hermes uses YAML   | Low      | Documented for awareness; unified format would break platform compatibility |
| 4   | **Missing agent descriptions** — Hermes profiles only have model name, no purpose field | Low      | Added inferred purposes above                                               |

### Coverage Gaps

- Copilot has no equivalent for: Testing, DevOps, Frontend, Documentation, Task
  Management
- Hermes has no equivalent for: Code Review, Debugging, Testing, Frontend,
  Documentation, Context Discovery
- OpenCode has no equivalent for: Creative direction, Executive assistant,
  Patient tutor

---

## Recommendations

1. **Keep platform-native formats** — Each platform's agent format is dictated
   by the platform. Normalizing to one format isn't practical, but
   cross-referencing is.

2. **Add Hermes profile descriptions** — Add a `description` field to each
   Hermes profile in config.yaml or the profile's metadata for
   self-documentation.

3. **Extend Copilot agents** — Consider adding `.github/agents/tester.agent.md`
   and `.github/agents/devops.agent.md` to close the biggest coverage gaps on
   the Copilot side.

4. **Cross-reference in copilot-instructions.md** — ✅ Done (see below update).

5. **Update AGENTS.md** — Add a section noting which platform agents are
   available and how they map.

---

## File Locations

```text
# Copilot agents (per-project)
.github/agents/architect.agent.md
.github/agents/debugger.agent.md
.github/agents/reviewer.agent.md

# Copilot instructions (references agents)
.github/copilot-instructions.md

# Hermes profiles (global)
~/AppData/Local/hermes/config.yaml
~/AppData/Local/hermes/profiles/{name}/

# OpenCode agents (global)
~/.config/opencode/agents/opencoder.md
~/.config/opencode/agents/coder-agent.md
~/.config/opencode/agents/reviewer.md
~/.config/opencode/agents/test-engineer.md
~/.config/opencode/agents/build-agent.md
~/.config/opencode/agents/devops-specialist.md
~/.config/opencode/agents/frontend-specialist.md
~/.config/opencode/agents/contextscout.md
~/.config/opencode/agents/externalscout.md
~/.config/opencode/agents/task-manager.md
~/.config/opencode/agents/documentation.md
~/.config/opencode/agents/web-search-researcher.md
~/.config/opencode/agents/codebase-analyzer.md
~/.config/opencode/agents/thoughts-analyzer.md
~/.config/opencode/agents/context-organizer.md

# OpenCode config (references agents + instructions)
~/.config/opencode/opencode.json
```
