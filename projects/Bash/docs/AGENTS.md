---
title: Agent Configurations — Bash Toolkit
status: active
updated: 2026-05-27
tags: [agents, routing, mindmodel, bash, ai-development]
---

## Scope
Local guidance for `Bash/docs/`. Follow `../AGENTS.md` and `../../.github/copilot-instructions.md` for toolkit-wide rules. Root Hermes assets: `../../.github/agents/hermes.agent.md`, `../../.github/prompts/`.

# Agent Configurations

## Registry

### Core Analysis
| Agent | Purpose | Triggers |
|---|---|---|
| `mm-stack-detector` | Identify stack | stack |
| `mm-dependency-mapper` | Map deps | imports, packages |
| `mm-convention-extractor` | Extract style | conventions |
| `mm-domain-extractor` | Domain terms | business logic |
| `mm-code-clusterer` | Group patterns | clustering |
| `mm-pattern-discoverer` | Architecture patterns | design, structure |
| `mm-anti-pattern-detector` | Find issues | bugs, inconsistencies |

### Utility
| Agent | Purpose |
|---|---|
| `mm-constraint-writer` | Assemble mindmodel |

## Routing

### By Task
- Code review/bugs → `mm-anti-pattern-detector`
- Dependencies → `mm-dependency-mapper`
- Architecture → `mm-pattern-discoverer`
- Docs/comments → `mm-convention-extractor`

### By File
| Type | Primary | Secondary |
|---|---|---|
| `.sh`, `.ps1`, `.bat` | `mm-stack-detector` | `mm-convention-extractor` |
| `.md` | `mm-convention-extractor` | `mm-domain-extractor` |
| `.log` | `mm-anti-pattern-detector` | `mm-dependency-mapper` |

## Workflows

### Phase 1 — Analysis
Run all 7 analysis agents concurrently:

```javascript
spawn_agent({
  agents: [
    { agent: "mm-stack-detector", prompt: "...", description: "..." },
    { agent: "mm-dependency-mapper", prompt: "...", description: "..." },
    { agent: "mm-convention-extractor", prompt: "...", description: "..." },
    { agent: "mm-domain-extractor", prompt: "...", description: "..." },
    { agent: "mm-code-clusterer", prompt: "...", description: "..." },
    { agent: "mm-pattern-discoverer", prompt: "...", description: "..." },
    { agent: "mm-anti-pattern-detector", prompt: "...", description: "..." }
  ]
});
```

### Phase 2 — Assembly
```javascript
spawn_agent({
  agents: [
    { agent: "mm-constraint-writer", prompt: "Assemble all findings...", description: "Write constraints" }
  ]
});
```

## Prompt Template
```
Analyze {files} for {purpose}.
Focus areas:
- {requirement 1}
- {requirement 2}
Output: { "findings": [...], "summary": "..." }
```

## Mindmodel
`.mindmodel/` stores Markdown constraint files by category:
```
manifest.md
stack/dependencies.md
style/config.md
style/naming.md
patterns/*.md
examples/
```

```javascript
mindmodel_lookup({ query: "create upgrade function" });
```

## Flags
| Flag | Default |
|---|---|
| `parallel_execution` | `true` |
| `timeout_seconds` | `120` |
| `retry_on_failure` | `true` |
| `verbose_logging` | `false` |
| `cache_results` | `true` |
| `incremental_update` | `true` |

## Anti-Patterns
- Running agents sequentially when parallel is possible
- Skipping Phase 1 before Phase 2
- Ignoring agent errors
- Overwriting `.mindmodel` without analysis
- Missing progress output during long operations
