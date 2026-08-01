# Generator Orchestrator Prompt Document

> **A dependency-aware orchestrator that coordinates the 11 root blueprint/MCP generator prompts with strict stage gates and consistency validation.**

---

## Quick Reference

| Property | Value |
|----------|-------|
| **Orchestrator** | `generator-orchestrator.prompt.md` |
| **Generators Coordinated** | 11 root prompts |
| **Stages** | A → B → C → D → E |
| **Modes** | `full` \| `quick` \| `custom` |
| **Output** | Manifest + Validation Report + Handoff Decision |

---

## Usage

```bash
# Full run (all stages, all MCP generators per detected stack)
/generator-orchestrator --mode full

# Quick run (Stage A only)
/generator-orchestrator --mode quick

# Custom stages with explicit flags
/generator-orchestrator --mode custom --stages A,B,C --include-code-generation true --validation-level strict
```

---

## 1. Generator Inventory (Phase 1: Discovery)

The orchestrator manages **exactly 11** root generator prompts. Each is confirmed by filename, frontmatter, and trigger.

| # | Generator | Trigger | Role | Toolsets |
|---|-----------|---------|------|----------|
| 1 | technology-stack-blueprint-generator | `/technology-stack-blueprint-generator` | **Analysis** | file, terminal |
| 2 | folder-structure-blueprint-generator | `/folder-structure-blueprint-generator` | **Analysis** | file, terminal |
| 3 | architecture-blueprint-generator | `/architecture-blueprint-generator` | **Documentation** | file, terminal |
| 4 | project-workflow-analysis-blueprint-generator | `/project-workflow-analysis-blueprint-generator` | **Documentation** | file, terminal |
| 5 | code-exemplars-blueprint-generator | `/code-exemplars-blueprint-generator` | **Documentation** | file, terminal |
| 6 | copilot-instructions-blueprint-generator | `/copilot-instructions-blueprint-generator` | **Documentation** | file, terminal |
| 7 | readme-blueprint-generator | `/readme-blueprint-generator` | **Documentation** | file, terminal |
| 8 | typescript-mcp-server-generator | `/typescript-mcp-server-generator` | **Code-gen** | file, terminal, web |
| 9 | python-mcp-server-generator | `/python-mcp-server-generator` | **Code-gen** | file, terminal, web |
| 10 | swift-mcp-server-generator | `/swift-mcp-server-generator` | **Code-gen** | file, terminal, web |
| 11 | mcp-copilot-studio-server-generator | `/mcp-copilot-studio-server-generator` | **Code-gen** | file, terminal |

**Invariant:** Inventory count must equal 11. Any drift → `inventory_drift` error → halt.

---

## 2. Dependency Graph & Stage Architecture (Phase 2: Contract Design)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            STAGE A (Parallel)                                │
│  ┌─────────────────────────────┐    ┌─────────────────────────────────────┐ │
│  │ technology-stack-blueprint  │    │ folder-structure-blueprint          │ │
│  │ - Detects languages,        │    │ - Maps project tree                 │ │
│  │   frameworks, versions      │    │ - Naming conventions                │ │
│  │ - Output: stack blueprint   │    │ - File placement patterns           │ │
│  └──────────────┬───────────────┘    └────────────────────┬───────────────┘ │
└─────────────────┼─────────────────────────────────────────┼─────────────────┘
                  │                                         │
                  ▼                                         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            STAGE B (Gated, Ordered)                          │
│  1. architecture-blueprint-generator  ◄── reads Stage A outputs             │
│  2. project-workflow-analysis-blueprint-generator ◄── reads A + arch        │
│  3. code-exemplars-blueprint-generator  ◄── reads Stage A outputs           │
│     Gate B: All three complete, no forward refs                             │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            STAGE C (Gated, Parallel)                         │
│  ┌─────────────────────────────┐    ┌─────────────────────────────────────┐ │
│  │ copilot-instructions-       │    │ readme-blueprint-generator          │ │
│  │ blueprint-generator         │    │ - Reads ALL prior outputs           │ │
│  │ - Reads A + B outputs       │    │ - Cross-doc consistency critical    │ │
│  └──────────────┬───────────────┘    └────────────────────┬───────────────┘ │
└─────────────────┼─────────────────────────────────────────┼─────────────────┘
                  │                                         │
                  ▼                                         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            STAGE D (Conditional)                             │
│  Triggered by Stage A stack detection + include-code-generation flag        │
│                                                                              │
│  Stack indicators → MCP Generator                                           │
│  ─────────────────────────────────────                                      │
│  TypeScript/Node.js    → typescript-mcp-server-generator                   │
│  Python                → python-mcp-server-generator                       │
│  Swift                 → swift-mcp-server-generator                        │
│  Power Platform/CS     → mcp-copilot-studio-server-generator               │
│  Ambiguous/None        → default: TypeScript MCP                           │
│                                                                              │
│  All matching generators run in parallel                                    │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            STAGE E (Final)                                   │
│  • Cross-document consistency validation (ALL stages)                       │
│  • Manifest generation (orchestrator-manifest.json)                         │
│  • Validation report (orchestrator-validation-report.md)                    │
│  • Handoff decision: PASS / FAIL                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Prerequisite Matrix

| Downstream | Requires |
|------------|----------|
| architecture-blueprint | technology-stack, folder-structure |
| project-workflow-analysis | technology-stack, folder-structure, architecture |
| code-exemplars-blueprint | technology-stack, folder-structure |
| copilot-instructions-blueprint | technology-stack, folder-structure, architecture, workflow-analysis, code-exemplars |
| readme-blueprint-generator | ALL prior (A+B+C) |
| All MCP generators | technology-stack (for detection) |

---

## 3. Execution Modes

| Mode | Stages Run | MCP Gen | Validation | Use Case |
|------|------------|---------|------------|----------|
| `full` (default) | A→B→C→D→E | Per stack | strict | Complete aligned generation |
| `quick` | A only | none | normal | Fast stack + folder check |
| `custom` | User-specified | `--include-code-generation` | `--validation-level` | Targeted runs |

**Custom mode auto-injects prerequisites:** If user requests `stages=C`, orchestrator auto-prepends `A,B` because C depends on them.

---

## 4. Stage Gate Definitions

### Gate A (Post Stage A)

**Must pass:**

- [ ] `blueprints/technology-stack-blueprint.md` exists
- [ ] Contains `## Stack Summary` with at least one language entry
- [ ] `blueprints/folder-structure-blueprint.md` exists
- [ ] Contains `## Folder Structure` with tree listing
- [ ] Both pass Markdown lint (no broken fences, valid headers)

**Retry:** Once with `validation-level=stricter` if either fails lint.

### Gate B (Post Stage B)

**Must pass:**

- [ ] All three Stage B outputs exist
- [ ] `architecture-blueprint.md` has `## Component Diagram` with diagram (Mermaid/PlantUML/ASCII)
- [ ] `workflow-analysis-blueprint.md` has `## Data Flow` section
- [ ] No forward references to Stage C/D/E outputs (dependency trace clean)

**Retry:** Once with stricter constraints if sections missing.

### Gate C (Post Stage C)

**Must pass:**

- [ ] `copilot-instructions.md` exists
- [ ] `README.md` exists
- [ ] **Cross-doc consistency** — project name, stack, version identical across:
  - Stage A (stack blueprint)
  - Stage B (arch, workflow, exemplars)
  - Stage C (copilot-instructions, README)
- [ ] Any mismatch = **HARD FAIL** with remediation checklist

### Gate D (Post Stage D)

**Must pass per generator:**

- [ ] Output directory exists with project config (`package.json`, `pyproject.toml`, `Package.swift`, or equivalent)
- [ ] At least one tool definition present (MCP tool registration)
- [ ] Valid syntax for target language

### Gate E (Final — always runs)

**Consistency validation matrix:**

| Check | Pass Criterion |
|-------|----------------|
| Stack identity | Exactly one stack string across all artifacts |
| Framework versions | Identical version strings for detected frameworks |
| Project name | Single canonical name everywhere |
| Dependency trace | No artifact references outputs from later stages |
| Forward refs | Zero forward references |

**Handoff decision:** PASS only if ALL gates A-E pass with zero hard failures.

---

## 5. Input Normalization (Deterministic Defaults)

```python
def normalize_inputs(raw: dict) -> dict:
    return {
        "mode": raw.get("mode", "full"),
        "validation_level": raw.get("validation_level", "strict"),
        "include_code_generation": raw.get("include_code_generation",
            True if raw.get("mode", "full") == "full" else False),
        "stages": resolve_stages(raw.get("mode", "full"), raw.get("stages")),
    }
```

---

## 6. Failure & Degraded-Mode Policy

| Scenario | Action | Gate Result |
|----------|--------|-------------|
| Generator produces no output | Retry once with `validation_level=stricter` | Blocked until retry |
| Retry also fails | Emit `degraded_warning`, use generic fallback template | Gate passes with warning |
| Stack detection ambiguous | Record `ambiguous`, use generic-safe defaults, continue | Gate passes with warning |
| Cross-doc inconsistency (Gate C) | Emit targeted remediation checklist | **HARD FAIL** |
| Gate A/B/C fail after retry | Record failure, continue degraded | Gate passes with warning |
| Gate E finds inconsistency | **HANDOFF FAIL** with remediation | FAIL |

---

## 7. Output Artifacts

### Per-Stage Outputs

| Stage | Files |
|-------|-------|
| A | `blueprints/technology-stack-blueprint.md`, `blueprints/folder-structure-blueprint.md` |
| B | `blueprints/architecture-blueprint.md`, `blueprints/workflow-analysis-blueprint.md`, `blueprints/code-exemplars-blueprint.md` |
| C | `copilot-instructions.md`, `README.md` |
| D | `mcp-servers/typescript/`, `mcp-servers/python/`, `mcp-servers/swift/`, `mcp-servers/copilot-studio/` |
| E | `orchestrator-manifest.json`, `orchestrator-validation-report.md` |

### Manifest Schema (Stage E)

```json
{
  "name": "generator-orchestrator-manifest",
  "version": "1.0.0",
  "mode": "full",
  "validation_level": "strict",
  "timestamp": "2026-07-28T...",
  "stages": { "A": {...}, "B": {...}, "C": {...}, "D": {...}, "E": {...} },
  "handoff_decision": "PASS|FAIL",
  "handoff_reason": "..."
}
```

### Validation Report (Stage E)

```markdown
# Orchestrator Validation Report

## Gate Results
| Gate | Status | Notes |
|------|--------|-------|
| A | PASS/FAIL/DEGRADED | ... |
| B | PASS/FAIL/DEGRADED | ... |
| C | PASS/FAIL | Cross-doc: PASS/FAIL |
| D | PASS/FAIL/DEGRADED | ... |
| E | PASS/FAIL | Consistency: PASS/FAIL |

## Warnings
- ...

## Remediation Checklist (if FAIL)
- [ ] Fix stack mismatch in README.md vs copilot-instructions.md
- [ ] ...
```

---

## 8. Stack Detection Logic (Stage D Trigger)

```python
def select_mcp_generators(stack_blueprint: dict, include_code_gen: bool) -> list:
    if not include_code_gen:
        return []
    
    detected = []
    languages = stack_blueprint.get("languages", [])
    
    if "typescript" in languages or "javascript" in languages:
        detected.append("typescript-mcp-server-generator")
    if "python" in languages:
        detected.append("python-mcp-server-generator")
    if "swift" in languages:
        detected.append("swift-mcp-server-generator")
    if "power-platform" in stack_blueprint.get("frameworks", []) or \
       "copilot-studio" in stack_blueprint.get("tools", []):
        detected.append("mcp-copilot-studio-server-generator")
    
    if not detected:
        detected.append("typescript-mcp-server-generator")  # safe default
    
    return detected
```

---

## 9. Invocation Order Summary

```
1. [Parallel] technology-stack-blueprint-generator + folder-structure-blueprint-generator
2. [Gate A] Verify both outputs → RETRY once if fail → DEGRADED if still fail
3. [Sequential] architecture-blueprint-generator
4. [Sequential] project-workflow-analysis-blueprint-generator (reads arch)
5. [Sequential] code-exemplars-blueprint-generator
6. [Gate B] Verify all three + dependency trace clean
7. [Parallel] copilot-instructions-blueprint-generator + readme-blueprint-generator
8. [Gate C] Cross-doc consistency → HARD FAIL if mismatch
9. [Parallel] Run selected MCP generators per stack detection
10. [Gate D] Verify MCP outputs valid
11. [Final] Stage E: Full consistency validation → manifest + report → handoff
```

---

## 10. Verification Checklist (Pre-Run)

- [ ] All 11 generator prompts present in `.github/prompts/`
- [ ] Template placeholders populated (`phases.md`, `rules.md`, `steps.md`)
- [ ] Manifest template valid JSON
- [ ] Validation report template valid Markdown
- [ ] No circular dependencies in graph
- [ ] Mode defaults deterministic
- [ ] Failure policy covers all generator failure modes
- [ ] Cross-doc consistency check covers all shared fields

---

## 11. Maintenance

When adding/removing a root generator:

1. Update inventory table in this document
2. Update prerequisite matrix
3. Update stage assignment (A/B/C/D)
4. Update stack detection logic (if code-generator)
5. Update manifest schema
6. Re-run verification checklist

---

**This orchestrator document is the single source of truth for coordinating the 11 root generator prompts. All execution logic, gates, and contracts are defined here.**
