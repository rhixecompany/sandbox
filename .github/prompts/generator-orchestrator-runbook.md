# Generator Orchestrator — Dependency-Aware Runbook

> **Version:** 1.0.0  
> **Coordinates:** 11 root generator prompts  
> **Stage gates:** Strict dependency ordering with consistency validation  
> **Execution modes:** `full`, `quick`, `custom`

---

## Table of Contents

1. [Generator Inventory & Classification](#1-generator-inventory--classification)
2. [Dependency Graph & Stage Architecture](#2-dependency-graph--stage-architecture)
3. [Input/Output Contracts](#3-inputoutput-contracts)
4. [Stage Gate Definitions](#4-stage-gate-definitions)
5. [Execution Mode Matrix](#5-execution-mode-matrix)
6. [Failure & Degraded-Mode Policy](#6-failure--degraded-mode-policy)
7. [Consistency Validation Framework](#7-consistency-validation-framework)
8. [Manifest Template](#8-manifest-template)
9. [Validation Report Template](#9-validation-report-template)

---

## 1. Generator Inventory & Classification

### Inventory Confirmation

**Set:** Exactly 11 root generator prompts as declared in `generator-orchestrator.prompt.md`.

| # | Prompt File | Role | Tags (Primary) |
|---|-------------|------|----------------|
| 1 | `technology-stack-blueprint-generator.prompt.md` | **Analysis** | architecture, python, typescript, dotnet, java, javascript, react |
| 2 | `folder-structure-blueprint-generator.prompt.md` | **Analysis** | architecture, typescript, python, java, react, dotnet |
| 3 | `architecture-blueprint-generator.prompt.md` | **Documentation** | architecture, documentation, typescript |
| 4 | `project-workflow-analysis-blueprint-generator.prompt.md` | **Documentation** | architecture, workflow, documentation, testing |
| 5 | `code-exemplars-blueprint-generator.prompt.md` | **Documentation** | architecture, configuration, documentation |
| 6 | `copilot-instructions-blueprint-generator.prompt.md` | **Documentation** | ai-assistant, architecture, specification, typescript |
| 7 | `readme-blueprint-generator.prompt.md` | **Documentation** | documentation, markdown, workflow, testing |
| 8 | `typescript-mcp-server-generator.prompt.md` | **Code-generation** | mcp, typescript, backend, specification |
| 9 | `python-mcp-server-generator.prompt.md` | **Code-generation** | mcp, python, backend, specification |
| 10 | `swift-mcp-server-generator.prompt.md` | **Code-generation** | mcp, swift, backend, specification |
| 11 | `mcp-copilot-studio-server-generator.prompt.md` | **Code-generation** | mcp, ai-assistant, backend, specification |

### Frontmatter Validation

Each prompt was checked for required frontmatter fields:

| Field | Status |
|-------|--------|
| `name` | ✅ All 11 present |
| `title` | ✅ All 11 present |
| `description` | ✅ All 11 present |
| `version` | ✅ All 11 = `1.0.0` |
| `tags` | ✅ All 11 present |
| `trigger` | ✅ All 11 present |
| `toolsets` | ✅ All 11 = `file, terminal` (+ `web` for TypeScript, Python, Swift MCP) |

---

## 2. Dependency Graph & Stage Architecture

### Graphical Representation

```
Stage A (Parallel)                  Stage B (Gated, Ordered)       Stage C (Gated, Parallel)
┌─────────────────────┐            ┌─────────────────────┐        ┌─────────────────────┐
│ technology-stack     │ ─────────>│ architecture         │ ──────>│ copilot-instructions │
│ blueprint-generator  │            │ blueprint-generator  │        │ blueprint-generator  │
└──────────┬──────────┘            └─────────────────────┘        └─────────────────────┘
           │                        ┌─────────────────────┐        ┌─────────────────────┐
           │                        │ project-workflow-    │ ──────>│ readme-blueprint     │
           │                        │ analysis-blueprint-  │        │ -generator           │
           │                        │ generator            │        └─────────────────────┘
           │                        └─────────────────────┘
           │                        ┌─────────────────────┐
           │                        │ code-exemplars-      │
           │                        │ blueprint-generator  │
           │                        └─────────────────────┘
           │
Stage D (Conditional — fires based on stack detection)
           │
           ├── TypeScript detected ─────────────> typescript-mcp-server-generator
           ├── Python detected ─────────────────> python-mcp-server-generator
           ├── Swift detected ──────────────────> swift-mcp-server-generator
           ├── Power Platform / CS detected ────> mcp-copilot-studio-server-generator
           └── No clear detection ─────────────> default: TypeScript MCP

Stage E (Always runs — final consolidation)
           │
           └──> Consistency validation + manifest + handoff decision
```

### Dependency Edges — Prerequisite Matrix

| Downstream Generator | Depends On |
|----------------------|------------|
| `architecture-blueprint-generator` | technology-stack, folder-structure |
| `project-workflow-analysis-blueprint-generator` | technology-stack, folder-structure, architecture |
| `code-exemplars-blueprint-generator` | technology-stack, folder-structure |
| `copilot-instructions-blueprint-generator` | technology-stack, folder-structure, architecture, workflow-analysis, code-exemplars |
| `readme-blueprint-generator` | technology-stack, folder-structure, architecture, workflow-analysis, code-exemplars, copilot-instructions |
| All Stage D (MCP generators) | technology-stack (for stack detection) |

### Stage Dependency Table

| Stage | Contains | Parallel | Gate Before Next | Conditional |
|-------|----------|----------|------------------|-------------|
| **A** | technology-stack, folder-structure | ✅ Yes (both) | ✅ Gate A | ❌ No |
| **B** | architecture, workflow-analysis, code-exemplars | ❌ No (ordered: arch → workflow → exemplars) | ✅ Gate B | ❌ No |
| **C** | copilot-instructions, readme | ✅ Yes (both) | ✅ Gate C | ❌ No |
| **D** | MCP generators (4) | ✅ Yes (all matching) | ✅ Gate D | ✅ Stack-dependent |
| **E** | Consolidation & handoff | N/A | ❌ Final | ❌ No |

---

## 3. Input/Output Contracts

### Stage A

#### technology-stack-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | Root project directory, source files |
| **Output file** | `blueprints/technology-stack-blueprint.md` |
| **Required sections** | `## Stack Summary`, `## Languages & Runtimes`, `## Frameworks & Libraries`, `## Build Tooling`, `## Deployment Target` |
| **Gate criterion** | All required sections present and populated |

#### folder-structure-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | Root project directory, source files |
| **Output file** | `blueprints/folder-structure-blueprint.md` |
| **Required sections** | `## Folder Structure`, `## Naming Conventions`, `## File Placement Patterns` |
| **Gate criterion** | `## Folder Structure` contains at least a tree listing |

### Stage B

#### architecture-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | technology-stack-blueprint.md, folder-structure-blueprint.md, source files |
| **Output file** | `blueprints/architecture-blueprint.md` |
| **Required sections** | `## Architecture Overview`, `## Component Diagram`, `## Data Flow`, `## Pattern Decisions` |
| **Gate criterion** | Has at least one diagram reference (Mermaid/PlantUML/ASCII) and no forward references to Stage C outputs |

#### project-workflow-analysis-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | technology-stack-blueprint.md, folder-structure-blueprint.md, architecture-blueprint.md, source files |
| **Output file** | `blueprints/workflow-analysis-blueprint.md` |
| **Required sections** | `## Entry Points`, `## Service Layer`, `## Data Access`, `## Error Handling`, `## Testing Strategy` |
| **Gate criterion** | Has a data-flow section and references only Stage A + Stage B (architecture) outputs |

#### code-exemplars-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | technology-stack-blueprint.md, folder-structure-blueprint.md, source files |
| **Output file** | `blueprints/code-exemplars-blueprint.md` |
| **Required sections** | `## Exemplar Categories`, `## Code Samples by Pattern`, `## Standards Recommendations` |
| **Gate criterion** | Lists at least 3 exemplar categories and references at least one per category |

### Stage C

#### copilot-instructions-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | All Stage A + Stage B outputs |
| **Output file** | `.github/copilot-instructions.md` |
| **Required sections** | `## Technology Stack`, `## Architecture Patterns`, `## Workflow Conventions`, `## Code Standards`, `## Testing Approach` |
| **Gate criterion** | Cross-doc consistency: stack/version/project-name must match Stage A exactly |

#### readme-blueprint-generator

| Field | Value |
|-------|-------|
| **Input** | All Stage A + Stage B + Stage C outputs |
| **Output file** | `README.md` |
| **Required sections** | `## Overview`, `## Tech Stack`, `## Getting Started`, `## Project Structure`, `## Architecture`, `## Contributing` |
| **Gate criterion** | Cross-doc consistency: all referenced names, versions, paths match prior artifacts |

### Stage D

#### MCP Server Generators (all four)

| Field | Value |
|-------|-------|
| **Input** | technology-stack-blueprint.md (stack detection) |
| **Output dir** | `servers/<language>/` |
| **Required files (TypeScript)** | `package.json`, `src/index.ts`, `tsconfig.json` |
| **Required files (Python)** | `pyproject.toml`, `src/server.py`, `src/__init__.py` |
| **Required files (Swift)** | `Package.swift`, `Sources/` |
| **Required files (CS Studio)** | `package.json`, `src/`, Copilot Studio manifest |
| **Gate criterion** | Language-specific project config exists + at least one tool definition |

---

## 4. Stage Gate Definitions

### Gate A — After Stage A

**Pass if all:**
- [ ] `blueprints/technology-stack-blueprint.md` exists
- [ ] `blueprints/folder-structure-blueprint.md` exists
- [ ] Tech stack file has all required sections (see contract)
- [ ] Folder structure file has `## Folder Structure` with content
- [ ] Stack detection is unambiguous (or if ambiguous, degraded mode recorded)

**Fail — retry then degrade:**
1. Retry failed generator once with `validation-level=stricter`
2. If retry fails, record degraded warning in the manifest
3. Continue with generic-safe defaults

### Gate B — After Stage B

**Pass if all:**
- [ ] `blueprints/architecture-blueprint.md` exists with diagram
- [ ] `blueprints/workflow-analysis-blueprint.md` exists with data-flow section
- [ ] `blueprints/code-exemplars-blueprint.md` exists with ≥3 categories
- [ ] No forward references to Stage C or Stage D outputs
- [ ] Dependency trace: each artifact references only prior completed outputs

**Fail — hard block:**
- Architecture missing diagram → retry once, then fail handoff
- Forward reference detected → fail handoff immediately

### Gate C — After Stage C

**Pass if all:**
- [ ] `.github/copilot-instructions.md` exists
- [ ] `README.md` exists
- [ ] **Cross-document consistency check:**
  - [ ] Stack name matches across all 7 documents (A+B+C)
  - [ ] Framework versions match
  - [ ] Project name is identical
  - [ ] No contradictory conventions

**Fail — hard block:**
- Any cross-doc inconsistency → emit remediation checklist → FAIL handoff
- Inconsistencies are NOT automatically fixable — orchestrator emits targeted items

### Gate D — After Stage D

**Pass if all:**
- [ ] For each detected technology, MCP server project exists
- [ ] Language-specific project config is valid (parseable)
- [ ] At least one tool definition exists per generated server
- [ ] MCP server name does not conflict with any other generated server

**Fail — retry then degrade:**
- Missing project config → retry once
- No tool definitions → retry with explicit tool spec
- Retry fails → record degraded, include server skeleton with TODOs

### Final Gate — Stage E Handoff

**PASS** = All gates A, B, C, D passed (warnings allowed, no hard failures)
**FAIL** = Any gate has an unresolved hard failure

---

## 5. Execution Mode Matrix

| Mode | Stage A | Stage B | Stage C | Stage D | Stage E | Default `validation-level` |
|------|---------|---------|---------|---------|---------|---------------------------|
| `full` | ✅ | ✅ | ✅ | ✅ (conditional) | ✅ | `strict` |
| `quick` | ✅ | ❌ | ❌ | ❌ | ✅ (reduced) | `normal` |
| `custom` | ✅ (auto-injected if B/C/D selected) | As specified | As specified | As specified + `include-code-generation` flag | ✅ | As specified |

### Custom Mode Flags

| Flag | Values | Default | Effect |
|------|--------|---------|--------|
| `stages` | e.g. `A,B` | A–E (full) | Select stages; prerequisites auto-injected |
| `include-code-generation` | `true`/`false` | Derived from mode | Controls Stage D |
| `validation-level` | `strict`/`normal`/`skip` | `strict` | Gate strictness |
| `stack-override` | e.g. `python,typescript` | auto-detect | Bypass stack detection |

---

## 6. Failure & Degraded-Mode Policy

| Scenario | Action | Gate Impact | Output Marker |
|----------|--------|-------------|---------------|
| Generator produces no output | Retry once with stricter constraints | Blocked until retry | `status: degraded` |
| Retry also fails | Continue with generic fallback | Gate passes (degraded) | `status: degraded_warning` |
| Cross-document inconsistency | Emit remediation checklist items | Gate FAILS | `status: failed` |
| Stack detection ambiguous | Use generic-safe defaults, continue | Gate passes (warning) | `status: ambiguous_stack` |
| Stage D (MCP) no technologies detected | Skip Stage D silently | N/A (no-op) | `status: skipped` |
| Lint/parse error on artifact | Retry generator once | Gate passes (warning) | `status: lint_warning` |

---

## 7. Consistency Validation Framework

### Field-Level Consistency Matrix

The following fields must be identical across ALL generated artifacts:

| Consistency Key | Source Generator | Checked In |
|-----------------|-----------------|------------|
| `project.name` | technology-stack | All docs in B, C, E |
| `stack.primary_language` | technology-stack | architecture, workflow, exemplars, copilot-instructions, readme |
| `stack.framework_versions` | technology-stack | architecture, copilot-instructions, readme |
| `folder.root` | folder-structure | architecture, readme |
| `architecture.pattern` | architecture | workflow, copilot-instructions, readme |

### Automated Check Script (Conceptual)

```
for each key in consistency_keys:
    values = [extract(artifact, key) for artifact in all_artifacts]
    unique = set(values)
    if len(unique) > 1:
        emit_failure(f"Key '{key}' inconsistent: {unique}")
```

### Remediation Checklist Template

When inconsistencies are found, emit items like:

```
- [ ] FIX: project.name in architecture-blueprint.md says "MyApp" but readme says "my-app"
- [ ] FIX: stack.primary_language in copilot-instructions.md says "TypeScript" but tech-stack says "Python"
- [ ] FIX: framework_versions mismatch between workflow-analysis and arch-blueprint
```

---

## 8. Manifest Template

The orchestrator writes an execution manifest (`orchestrator-manifest.json`) after Stage E:

```json
{
  "orchestrator_version": "1.0.0",
  "run_timestamp": "<ISO-8601>",
  "mode": "full|quick|custom",
  "execution": {
    "stages_executed": ["A", "B", "C", "D", "E"],
    "stage_results": {
      "A": {
        "status": "passed|degraded|failed",
        "warnings": [],
        "prompts": {
          "technology-stack-blueprint-generator": {
            "status": "success|degraded|failed",
            "output": "blueprints/technology-stack-blueprint.md",
            "sections_present": 5,
            "sections_expected": 5
          },
          "folder-structure-blueprint-generator": {
            "status": "success|degraded|failed",
            "output": "blueprints/folder-structure-blueprint.md",
            "sections_present": 3,
            "sections_expected": 3
          }
        }
      },
      "B": { "...": "..." },
      "C": { "...": "..." },
      "D": {
        "detected_technologies": ["typescript"],
        "servers_generated": [
          { "language": "typescript", "path": "servers/typescript/", "status": "success" }
        ]
      },
      "E": {
        "consistency_checks_passed": 5,
        "consistency_checks_failed": 0,
        "inconsistencies": []
      }
    }
  },
  "handoff_decision": "PASS|FAIL",
  "handoff_reason": "All gates passed|Cross-document inconsistency: ..."
}
```

---

## 9. Validation Report Template

The orchestrator writes a validation report (`orchestrator-validation-report.md`) after Stage E:

```markdown
# Generator Orchestrator — Validation Report

**Run:** <ISO-8601>
**Mode:** full
**Decision:** PASS / FAIL

---

## Gate Results

| Gate | Status | Details |
|------|--------|---------|
| A | ✅ PASS | Both analysis prompts completed |
| B | ✅ PASS | All three documentation prompts passed |
| C | ✅ PASS | Cross-doc consistency verified |
| D | ✅ PASS | 2 MCP servers generated (TypeScript, Python) |
| E | ✅ PASS | 5/5 consistency checks passed |

---

## Warnings

- [ ] Stack detection was ambiguous — generic TypeScript defaults used
- [ ] python-mcp-server-generator retried once due to missing pyproject.toml

---

## Remediation Checklist (∅ if PASS)

- [ ] FIX: project.name mismatch: "MyApp" vs "my-app"

---

## Artifact Summary

| Path | Size | Status |
|------|------|--------|
| blueprints/technology-stack-blueprint.md | 4.2 KB | ✅ |
| blueprints/folder-structure-blueprint.md | 3.1 KB | ✅ |
| blueprints/architecture-blueprint.md | 8.7 KB | ✅ |
| blueprints/workflow-analysis-blueprint.md | 6.4 KB | ✅ |
| blueprints/code-exemplars-blueprint.md | 5.2 KB | ✅ |
| .github/copilot-instructions.md | 12.1 KB | ✅ |
| README.md | 3.8 KB | ✅ |
| servers/typescript/ (2 files) | 1.4 KB | ✅ |
| servers/python/ (2 files) | 1.2 KB | ✅ |
| orchestrator-manifest.json | 1.8 KB | ✅ |
```

---

## Appendix A: CLI Invocation Reference

```bash
# Full run (all stages, strict validation)
hermes run generator-orchestrator mode=full

# Quick run (Stage A only, normal validation)
hermes run generator-orchestrator mode=quick

# Custom: Stage A + B + D, skip C, no code gen
hermes run generator-orchestrator mode=custom stages=A,B include-code-generation=false

# Custom: Full with bypassed validation
hermes run generator-orchestrator mode=full validation-level=skip

# Custom: Stack override (bypass auto-detection)
hermes run generator-orchestrator mode=full stack-override=python,swift
```

## Appendix B: Directory Structure After Full Run

```
project-root/
├── blueprints/
│   ├── technology-stack-blueprint.md      # Stage A
│   ├── folder-structure-blueprint.md       # Stage A
│   ├── architecture-blueprint.md           # Stage B
│   ├── workflow-analysis-blueprint.md      # Stage B
│   └── code-exemplars-blueprint.md         # Stage B
├── .github/
│   └── copilot-instructions.md             # Stage C
├── servers/
│   ├── typescript-mcp-server/              # Stage D (optional)
│   ├── python-mcp-server/                  # Stage D (optional)
│   ├── swift-mcp-server/                   # Stage D (optional)
│   └── mcp-copilot-studio-server/          # Stage D (optional)
├── README.md                               # Stage C
├── orchestrator-manifest.json              # Stage E
└── orchestrator-validation-report.md       # Stage E
```

---

*This runbook is generated by the generator-orchestrator prompt.  
All stage gates, failure policies, and consistency checks as defined in `templates/generator-orchestrator/` apply.*
