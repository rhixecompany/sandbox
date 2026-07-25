# Cross-Platform Agent Inventory — Worked Example

> From the agents-fix session (2026-05-29). Discover, audit, cross-reference, and normalize agent definitions across Copilot, Hermes, and OpenCode.

## Scenario

A project uses three AI coding platforms simultaneously:
- **Copilot** (proxied via `.github/` agent/prompt definitions)
- **Hermes Agent** (standalone AI agent with profile-based configuration)
- **OpenCode** (VS Code extension, the active session provider)

The task: "Sync all agent definitions across OpenCode, Hermes, and Copilot" — discover, audit for inconsistencies, fix, and normalize.

## Execution

### Phase 1: Discover

Locate agent definitions on each platform:

```bash
# Copilot agents (per-repo, project-specific)
ls .github/agents/*.agent.md
# → architect.agent.md, debugger.agent.md, reviewer.agent.md

# Hermes profiles (global)
hermes profile list
# → default, adminbot, code-architect, creative-director, ...

# OpenCode agents (global user config)
ls ~/.config/opencode/agents/*.md
# → opencoder.md, coder-agent.md, reviewer.md, test-engineer.md, ...
```

**Copilot agents read:**
- `architect.agent.md` — description: "Architecture planning mode", tools: [search, githubRepo, web/fetch]
- `debugger.agent.md` — description: "Interactive debugging assistant", tools: [runCommands, search, githubRepo]
- `reviewer.agent.md` — description: "Code review assistant", tools: [search, githubRepo, changes]

**OpenCode agents read (17 discovered):**
- Primary: `opencoder.md` (name: OpenCoder, mode: primary, orchestrator)
- Subagents: coder-agent, reviewer, test-engineer, build-agent, devops-specialist, frontend-specialist
- Discovery: contextscout, externalscout, codebase-analyzer, thoughts-analyzer, context-organizer
- Management: task-manager, documentation, web-search-researcher, openagent variants

**Hermes profiles read (7 discovered):**
- default (big-pickle, active), adminbot, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst
- No description/purpose field in config.yaml — inferred from profile names

### Phase 2: Inventory

Per-platform table capturing agent name, format, purpose:

```python
inventory = {
    "copilot": [
        {"name": "architect", "format": ".agent.md", "tools": ["search","githubRepo","web/fetch"]},
        {"name": "debugger",  "format": ".agent.md", "tools": ["runCommands","search","githubRepo"]},
        {"name": "reviewer",  "format": ".agent.md", "tools": ["search","githubRepo","changes"]},
    ],
    "hermes": [
        {"name": "default", "format": "yaml", "model": "big-pickle"},
        {"name": "code-architect", "format": "yaml", "model": "claude-haiku-4.5"},
        # ... etc
    ],
    "opencode": [
        {"name": "OpenCoder", "format": ".md", "mode": "primary"},
        {"name": "CoderAgent", "format": ".md", "mode": "subagent"},
        # ... etc
    ]
}
```

### Phase 3: Cross-Reference

Map agents by function:

| Function | Copilot | Hermes Profile | OpenCode Agent |
|----------|---------|----------------|----------------|
| Architecture/Planning | `architect` | `code-architect` | `OpenCoder` (primary) |
| Code Review | `reviewer` | — | `Reviewer` |
| Debugging | `debugger` | — | `CoderAgent` (implicit) |
| Testing | — | — | `TestEngineer` |
| DevOps | — | `adminbot` | `DevOpsSpecialist` |
| Frontend | — | — | `FrontendSpecialist` |
| General Dev | — | `default` | `CoderAgent` |
| Creative | — | `creative-director` | — |
| Research | — | `research-analyst` | `WebSearchResearcher` |
| Context/Discovery | — | — | `ContextScout`, `ExternalScout` |

### Phase 4: Audit Inconsistencies

| # | Issue | Severity |
|---|-------|----------|
| 1 | No cross-references between platforms — Copilot instructions don't mention Hermes or OpenCode | Medium |
| 2 | No agent inventory document — no single source of truth | Medium |
| 3 | Format mismatch — .agent.md vs .md vs YAML config | Low |
| 4 | Missing agent descriptions — Hermes profiles only have model, no purpose field | Low |

**Coverage gaps:**
- Copilot has no equivalent for: Testing, DevOps, Frontend, Documentation, Task Management
- Hermes has no equivalent for: Code Review, Debugging, Testing, Frontend, Documentation
- OpenCode has no equivalent for: Creative direction, Executive assistant, Patient tutor

### Phase 5: Fix & Document

**Fixes applied:**

1. Created `docs/agents-cross-reference.md` — full inventory with tables, mapping matrix, inconsistency severity ranking, coverage gap analysis, recommendations, file location references. Format: markdown with YAML frontmatter.

2. Updated `.github/copilot-instructions.md` — added Agent Cross-Platform Reference section with mapping table so project docs reference all three platforms.

### Verification Code

```python
from hermes_tools import terminal

# Verify cross-reference doc exists
r = terminal("head -3 docs/agents-cross-reference.md")
assert "---" in r["output"].split("\n")[0]

# Verify copilot-instructions has cross-ref section
r = terminal("grep 'Agent Cross-Platform Reference' .github/copilot-instructions.md")
assert int(r["output"]) >= 1

# Verify Copilot agents intact
r = terminal("for f in .github/agents/*.agent.md; do head -1 \"$f\"; done")
assert all("---" in line for line in r["output"].split("\n") if line)
```

## Key Takeaways

1. **Three platforms, three formats** — Copilot uses `.agent.md` (YAML frontmatter + markdown), OpenCode uses `.md` (full YAML), Hermes uses hierarchical YAML configs. Don't try to unify them — cross-reference instead.

2. **Global vs per-repo** — OpenCode agents are global (user home config), Copilot agents are per-repo, Hermes profiles are global. The cross-reference document belongs in the repo.

3. **Cross-reference is the primary deliverable** — the mapping table between platforms is more valuable than the raw inventory lists.

4. **Update instructions** — adding the cross-reference table to `.github/copilot-instructions.md` ensures any agent on any platform knows about its peers.

5. **Not all platforms have named agents** — Hermes "profiles" are model+setting bundles, not agents with instructions. This is a design gap worth documenting.

6. **Sweep for missing descriptions** — when inventorying agents, note which ones lack description fields. These are first candidates for normalization.
