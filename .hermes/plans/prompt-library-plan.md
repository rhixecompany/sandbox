---
name: prompt-library-plan
title: "Prompt Library Implementation Plan"
description: "Implementation plan for structured prompt library with category/trigger organization"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - implementation-plan
  - prompt-library
  - prompt-management
phases:
  - name: Phase 1 - Category Structure
    description: Create all 13 category directories
    tasks:
      - id: PL-T-1.1
        name: Create development category
        description: Create .github/prompts/development/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.2
        name: Create planning category
        description: Create .github/prompts/planning/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.3
        name: Create creative category
        description: Create .github/prompts/creative/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.4
        name: Create testing category
        description: Create .github/prompts/testing/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.5
        name: Create documentation category
        description: Create .github/prompts/documentation/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.6
        name: Create debugging category
        description: Create .github/prompts/debugging/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.7
        name: Create security category
        description: Create .github/prompts/security/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.8
        name: Create devops category
        description: Create .github/prompts/devops/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.9
        name: Create mcp category
        description: Create .github/prompts/mcp/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.10
        name: Create research category
        description: Create .github/prompts/research/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.11
        name: Create productivity category
        description: Create .github/prompts/productivity/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.12
        name: Create github category
        description: Create .github/prompts/github/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
      - id: PL-T-1.13
        name: Create qa category
        description: Create .github/prompts/qa/ directory
        phase: Phase 1 - Category Structure
        assignee: implementer
        status: pending
        dependencies: []
  - name: Phase 2 - Trigger Structure
    description: Create trigger directories for each category
    tasks:
      - id: PL-T-2.1
        name: Development triggers
        description: Create create-feature, refactor-code, fix-bug, write-test triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.1]
      - id: PL-T-2.2
        name: Planning triggers
        description: Create create-plan, create-spec, breakdown-feature triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.2]
      - id: PL-T-2.3
        name: Creative triggers
        description: Create write-content, design-ui, generate-ideas triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.3]
      - id: PL-T-2.4
        name: Testing triggers
        description: Create write-unit-test, write-integration-test, run-tests triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.4]
      - id: PL-T-2.5
        name: Documentation triggers
        description: Create write-readme, write-api-docs, update-docs triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.5]
      - id: PL-T-2.6
        name: Debugging triggers
        description: Create debug-issue, trace-bug, analyze-logs triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.6]
      - id: PL-T-2.7
        name: Security triggers
        description: Create security-review, threat-model, compliance-check triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.7]
      - id: PL-T-2.8
        name: DevOps triggers
        description: Create deploy-app, setup-ci, configure-infra triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.8]
      - id: PL-T-2.9
        name: MCP triggers
        description: Create add-mcp-server, test-mcp, debug-mcp triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.9]
      - id: PL-T-2.10
        name: Research triggers
        description: Create research-topic, synthesize-findings, literature-review triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.10]
      - id: PL-T-2.11
        name: Productivity triggers
        description: Create automate-task, optimize-workflow, generate-report triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.11]
      - id: PL-T-2.12
        name: GitHub triggers
        description: Create create-pr, review-pr, manage-issues triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.12]
      - id: PL-T-2.13
        name: QA triggers
        description: Create audit-code, run-quality-gates, validate-spec triggers
        phase: Phase 2 - Trigger Structure
        assignee: implementer
        status: pending
        dependencies: [PL-T-1.13]
  - name: Phase 3 - Prompt Files
    description: Create all prompt files with 10 companion files each
    tasks:
      - id: PL-T-3.1
        name: Create development prompts
        description: Create all 4 development prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.1]
      - id: PL-T-3.2
        name: Create planning prompts
        description: Create all 3 planning prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.2]
      - id: PL-T-3.3
        name: Create creative prompts
        description: Create all 3 creative prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.3]
      - id: PL-T-3.4
        name: Create testing prompts
        description: Create all 3 testing prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.4]
      - id: PL-T-3.5
        name: Create documentation prompts
        description: Create all 3 documentation prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.5]
      - id: PL-T-3.6
        name: Create debugging prompts
        description: Create all 3 debugging prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.6]
      - id: PL-T-3.7
        name: Create security prompts
        description: Create all 3 security prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.7]
      - id: PL-T-3.8
        name: Create devops prompts
        description: Create all 3 devops prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.8]
      - id: PL-T-3.9
        name: Create mcp prompts
        description: Create all 3 mcp prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.9]
      - id: PL-T-3.10
        name: Create research prompts
        description: Create all 3 research prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.10]
      - id: PL-T-3.11
        name: Create productivity prompts
        description: Create all 3 productivity prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.11]
      - id: PL-T-3.12
        name: Create github prompts
        description: Create all 3 github prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.12]
      - id: PL-T-3.13
        name: Create qa prompts
        description: Create all 3 qa prompts with companions
        phase: Phase 3 - Prompt Files
        assignee: implementer
        status: pending
        dependencies: [PL-T-2.13]
  - name: Phase 4 - Validation
    description: Validate all cross-references and structure
    tasks:
      - id: PL-T-4.1
        name: Validate specs.md references
        description: Verify all specs.md point to valid .hermes/specs/ files
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [PL-T-3.1, PL-T-3.2, PL-T-3.3, PL-T-3.4, PL-T-3.5, PL-T-3.6, PL-T-3.7, PL-T-3.8, PL-T-3.9, PL-T-3.10, PL-T-3.11, PL-T-3.12, PL-T-3.13]
      - id: PL-T-4.2
        name: Validate plans.md references
        description: Verify all plans.md point to valid .hermes/plans/ files
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [PL-T-3.1, PL-T-3.2, PL-T-3.3, PL-T-3.4, PL-T-3.5, PL-T-3.6, PL-T-3.7, PL-T-3.8, PL-T-3.9, PL-T-3.10, PL-T-3.11, PL-T-3.12, PL-T-3.13]
      - id: PL-T-4.3
        name: Validate companion file completeness
        description: Verify all 10 companion files exist per prompt
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [PL-T-3.1, PL-T-3.2, PL-T-3.3, PL-T-3.4, PL-T-3.5, PL-T-3.6, PL-T-3.7, PL-T-3.8, PL-T-3.9, PL-T-3.10, PL-T-3.11, PL-T-3.12, PL-T-3.13]
      - id: PL-T-4.4
        name: Validate frontmatter
        description: Verify all prompt frontmatter is valid YAML with required fields
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [PL-T-3.1, PL-T-3.2, PL-T-3.3, PL-T-3.4, PL-T-3.5, PL-T-3.6, PL-T-3.7, PL-T-3.8, PL-T-3.9, PL-T-3.10, PL-T-3.11, PL-T-3.12, PL-T-3.13]
gates:
  - name: Gate 1 - Categories Created
    phase: Phase 1 - Category Structure
    criteria:
      - All 13 category directories exist
    check: "ls .github/prompts/ | wc -l"
    pass_condition: "Count = 13"
    fail_action: "Create missing categories"
  - name: Gate 2 - Triggers Created
    phase: Phase 2 - Trigger Structure
    criteria:
      - Each category has ≥1 trigger directory
      - Total triggers ≥ 39 (13 categories × 3 average)
    check: "find .github/prompts -mindepth 2 -maxdepth 2 -type d | wc -l"
    pass_condition: "Count ≥ 39"
    fail_action: "Create missing triggers"
  - name: Gate 3 - Prompt Files Complete
    phase: Phase 3 - Prompt Files
    criteria:
      - Each trigger has 11 files (.prompt.md + 10 companions)
      - Total files ≥ 429 (39 triggers × 11)
    check: "find .github/prompts -name '*.md' | wc -l"
    pass_condition: "Count ≥ 429"
    fail_action: "Create missing companion files"
  - name: Gate 4 - Cross-References Valid
    phase: Phase 4 - Validation
    criteria:
      - All specs.md references resolve
      - All plans.md references resolve
      - All frontmatter valid
    check: "Custom validation script"
    pass_condition: "Zero broken references"
    fail_action: "Fix broken references"
dependencies:
  - prompt-library-spec.md
  - prompt-skill-spec-plan-management-system.md
---

# Prompt Library Implementation Plan

## Overview

Implements the complete prompt library structure at `.github/prompts/` with 13 categories, 39+ triggers, and 429+ prompt files (each with 11 files).

## Categories & Triggers

### Development (4 triggers)
- `create-feature` - Create new features
- `refactor-code` - Refactor existing code
- `fix-bug` - Fix bugs
- `write-test` - Write tests

### Planning (3 triggers)
- `create-plan` - Create implementation plans
- `create-spec` - Create specifications
- `breakdown-feature` - Break down features

### Creative (3 triggers)
- `write-content` - Write content/articles
- `design-ui` - Design UI/UX
- `generate-ideas` - Generate ideas

### Testing (3 triggers)
- `write-unit-test` - Write unit tests
- `write-integration-test` - Write integration tests
- `run-tests` - Execute test suites

### Documentation (3 triggers)
- `write-readme` - Write README files
- `write-api-docs` - Write API documentation
- `update-docs` - Update existing documentation

### Debugging (3 triggers)
- `debug-issue` - Debug issues
- `trace-bug` - Trace bug root cause
- `analyze-logs` - Analyze log files

### Security (3 triggers)
- `security-review` - Security code review
- `threat-model` - Create threat models
- `compliance-check` - Compliance validation

### DevOps (3 triggers)
- `deploy-app` - Deploy applications
- `setup-ci` - Set up CI/CD
- `configure-infra` - Configure infrastructure

### MCP (3 triggers)
- `add-mcp-server` - Add MCP servers
- `test-mcp` - Test MCP servers
- `debug-mcp` - Debug MCP issues

### Research (3 triggers)
- `research-topic` - Research topics
- `synthesize-findings` - Synthesize research
- `literature-review` - Literature reviews

### Productivity (3 triggers)
- `automate-task` - Automate tasks
- `optimize-workflow` - Optimize workflows
- `generate-report` - Generate reports

### GitHub (3 triggers)
- `create-pr` - Create pull requests
- `review-pr` - Review pull requests
- `manage-issues` - Manage GitHub issues

### QA (3 triggers)
- `audit-code` - Audit code quality
- `run-quality-gates` - Run quality gates
- `validate-spec` - Validate specifications

## Total Count
- **Categories**: 13
- **Triggers**: 39
- **Prompt Directories**: 39
- **Files per Prompt**: 11
- **Total Files**: 429

## Verification

All gates must pass before Phase 3 (Skill Enhancement) can begin.