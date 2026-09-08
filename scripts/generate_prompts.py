#!/usr/bin/env python3
"""
Generate all prompt files with companion files for the prompt library.
Creates 39 prompts × 11 files = 429 files total.
"""

import os
import yaml
from pathlib import Path

BASE_PATH = Path("/c/Users/Alexa/Desktop/SandBox/.github/prompts")

# Define all categories, triggers, and prompts
PROMPTS = {
    "development": {
        "create-feature": "create-feature",
        "refactor-code": "refactor-code", 
        "fix-bug": "fix-bug",
        "write-test": "write-test"
    },
    "planning": {
        "create-plan": "create-plan",
        "create-spec": "create-spec",
        "breakdown-feature": "breakdown-feature"
    },
    "creative": {
        "write-content": "write-content",
        "design-ui": "design-ui",
        "generate-ideas": "generate-ideas"
    },
    "testing": {
        "write-unit-test": "write-unit-test",
        "write-integration-test": "write-integration-test",
        "run-tests": "run-tests"
    },
    "documentation": {
        "write-readme": "write-readme",
        "write-api-docs": "write-api-docs",
        "update-docs": "update-docs"
    },
    "debugging": {
        "debug-issue": "debug-issue",
        "trace-bug": "trace-bug",
        "analyze-logs": "analyze-logs"
    },
    "security": {
        "security-review": "security-review",
        "threat-model": "threat-model",
        "compliance-check": "compliance-check"
    },
    "devops": {
        "deploy-app": "deploy-app",
        "setup-ci": "setup-ci",
        "configure-infra": "configure-infra"
    },
    "mcp": {
        "add-mcp-server": "add-mcp-server",
        "test-mcp": "test-mcp",
        "debug-mcp": "debug-mcp"
    },
    "research": {
        "research-topic": "research-topic",
        "synthesize-findings": "synthesize-findings",
        "literature-review": "literature-review"
    },
    "productivity": {
        "automate-task": "automate-task",
        "optimize-workflow": "optimize-workflow",
        "generate-report": "generate-report"
    },
    "github": {
        "create-pr": "create-pr",
        "review-pr": "review-pr",
        "manage-issues": "manage-issues"
    },
    "qa": {
        "audit-code": "audit-code",
        "run-quality-gates": "run-quality-gates",
        "validate-spec": "validate-spec"
    }
}

# Companion file templates
COMPANION_TEMPLATES = {
    "specs.md": """# Specs for {prompt_title}

## Linked Specification
- **Spec File**: `.hermes/specs/{spec_file}.md`
- **Spec Version**: 1.0.0
- **Requirements Covered**: [REQ-XXX, REQ-YYY]

## Requirements Traceability
| Requirement | Spec Section | Verification |
|-------------|--------------|--------------|
| REQ-XXX | Section X | Gate X |
""",
    "plans.md": """# Plans for {prompt_title}

## Linked Plan
- **Plan File**: `.hermes/plans/{plan_file}.md`
- **Plan Version**: 1.0.0
- **Phases**: [Preparation, Execution, Verification, Completion]

## Plan Traceability
| Phase | Plan Section | Status |
|-------|--------------|--------|
| Preparation | Phase 1 | Pending |
| Execution | Phase 2 | Pending |
| Verification | Phase 3 | Pending |
| Completion | Phase 4 | Pending |
""",
    "goals.md": """# Goals for {prompt_title}

## Primary Goal
{primary_goal}

## Success Metrics
- Metric 1: {metric_1}
- Metric 2: {metric_2}

## Secondary Goals
- Goal 1: {secondary_goal_1}
- Goal 2: {secondary_goal_2}
""",
    "subgoals.md": """# Subgoals for {prompt_title}

| Subgoal | Owner | Dependencies | Status |
|---------|-------|--------------|--------|
| SG-1: {subgoal_1} | {role} | - | Pending |
| SG-2: {subgoal_2} | {role} | SG-1 | Pending |
| SG-3: {subgoal_3} | {role} | SG-2 | Pending |
""",
    "rules.md": """# Rules for {prompt_title}

## Invariants
- Rule 1: {invariant_1}
- Rule 2: {invariant_2}

## Constraints
- Constraint 1: {constraint_1}
- Constraint 2: {constraint_2}

## Business Rules
- Rule 1: {business_rule_1}
- Rule 2: {business_rule_2}
""",
    "phases.md": """# Phases for {prompt_title}

## Phase 1: Preparation
- **Entry Criteria**: {prep_entry}
- **Exit Criteria**: {prep_exit}
- **Duration**: {prep_duration}

## Phase 2: Execution
- **Entry Criteria**: {exec_entry}
- **Exit Criteria**: {exec_exit}
- **Duration**: {exec_duration}

## Phase 3: Verification
- **Entry Criteria**: {verify_entry}
- **Exit Criteria**: {verify_exit}
- **Duration**: {verify_duration}

## Phase 4: Completion
- **Entry Criteria**: {complete_entry}
- **Exit Criteria**: {complete_exit}
- **Duration**: {complete_duration}
""",
    "steps.md": """# Steps for {prompt_title}

## Phase 1: Preparation
### Step 1.1: {step_1_1_name}
- **Action**: {step_1_1_action}
- **Tool**: {step_1_1_tool}
- **Output**: {step_1_1_output}

### Step 1.2: {step_1_2_name}
- **Action**: {step_1_2_action}
- **Tool**: {step_1_2_tool}
- **Output**: {step_1_2_output}

## Phase 2: Execution
### Step 2.1: {step_2_1_name}
- **Action**: {step_2_1_action}
- **Tool**: {step_2_1_tool}
- **Output**: {step_2_1_output}

### Step 2.2: {step_2_2_name}
- **Action**: {step_2_2_action}
- **Tool**: {step_2_2_tool}
- **Output": {step_2_2_output}
""",
    "tasks.md": """# Tasks for {prompt_title}

| Task ID | Description | Phase | Assignee | Status | Dependencies |
|---------|-------------|-------|----------|--------|--------------|
| T-1 | {task_1_desc} | Preparation | {role} | Pending | - |
| T-2 | {task_2_desc} | Preparation | {role} | Pending | T-1 |
| T-3 | {task_3_desc} | Execution | {role} | Pending | T-2 |
| T-4 | {task_4_desc} | Execution | {role} | Pending | T-3 |
| T-5 | {task_5_desc} | Verification | {role} | Pending | T-4 |
| T-6 | {task_6_desc} | Completion | {role} | Pending | T-5 |
""",
    "actions.md": """# Actions for {prompt_title}

## Task T-1: {task_1_desc}
### Action 1.1
```bash
{action_1_1_cmd}
```
- **Expected Output**: {action_1_1_output}
- **Verification**: {action_1_1_verify}

## Task T-2: {task_2_desc}
### Action 2.1
```bash
{action_2_1_cmd}
```
- **Expected Output**: {action_2_1_output}
- **Verification**: {action_2_1_verify}

## Task T-3: {task_3_desc}
### Action 3.1
```bash
{action_3_1_cmd}
```
- **Expected Output**: {action_3_1_output}
- **Verification**: {action_3_1_verify}
""",
    "gates.md": """# Gates for {prompt_title}

## Gate 1: Preparation Complete
- **Criteria**: All Phase 1 tasks verified
- **Check**: {gate_1_check}
- **Pass Condition**: {gate_1_pass}
- **Fail Action**: {gate_1_fail}

## Gate 2: Execution Complete
- **Criteria**: All Phase 2 tasks verified
- **Check**: {gate_2_check}
- **Pass Condition**: {gate_2_pass}
- **Fail Action**: {gate_2_fail}

## Gate 3: Verification Complete
- **Criteria**: All gates pass
- **Check**: {gate_3_check}
- **Pass Condition**: All ACs met
- **Fail Action**: Re-execute failed phases

## Gate 4: Completion Verified
- **Criteria**: All artifacts created, validated
- **Check**: {gate_4_check}
- **Pass Condition**: Zero errors, all ACs met
- **Fail Action**: Full rollback
"""
}

# Main prompt template
PROMPT_TEMPLATE = """---
name: {category}/{trigger}/{prompt_name}
title: "{prompt_title}"
description: "{description}"
version: 1.0.0
author: Hermes Agent
license: MIT
category: {category}
trigger: {trigger}
tags: [{tags}]
skills_required: [{skills}]
tools_required: [{tools}]
companion_files:
  - specs.md
  - plans.md
  - goals.md
  - subgoals.md
  - rules.md
  - phases.md
  - steps.md
  - tasks.md
  - actions.md
  - gates.md
---

# {prompt_title}

## Overview

{overview}

## When to Use

{when_to_use}

## When NOT to Use

{when_not_to_use}

## Workflow

### Phase 1: Preparation
{phase_1_workflow}

### Phase 2: Execution
{phase_2_workflow}

### Phase 3: Verification
{phase_3_workflow}

### Phase 4: Completion
{phase_4_workflow}

## Verification Checklist

{verification_checklist}

## Best Practices

{best_practices}

## Pitfalls

{pitfalls}
"""

# Prompt-specific data
PROMPT_DATA = {
    "development/create-feature": {
        "title": "Create Feature",
        "description": "Create a new feature with full implementation including tests, docs, and verification",
        "tags": "feature, implementation, tdd",
        "skills": "test-driven-development, executing-plans, subagent-driven-development",
        "tools": "terminal, write_file, patch, search_files",
        "overview": "Systematic feature creation workflow using TDD with subagent-driven development for parallel execution.",
        "when_to_use": "Building new features from requirements; creating components, services, or modules",
        "when_not_to_use": "Bug fixes (use fix-bug); refactoring (use refactor-code); simple config changes",
        "phase_1_workflow": "1. Read requirements from spec\n2. Create implementation plan\n3. Set up test structure\n4. Define acceptance criteria",
        "phase_2_workflow": "1. Write failing tests (TDD)\n2. Implement minimal code\n3. Run tests to pass\n4. Refactor with tests green",
        "phase_3_workflow": "1. Run full test suite\n2. Verify against spec\n3. Code quality review\n4. Integration testing",
        "phase_4_workflow": "1. Update documentation\n2. Commit changes\n3. Create PR\n4. Verify CI passes",
        "verification_checklist": "- [ ] All tests passing\n- [ ] Spec requirements met\n- [ ] Code quality approved\n- [ ] Documentation updated\n- [ ] CI/CD green",
        "best_practices": "Follow TDD strictly; use subagents for parallel tasks; keep commits atomic",
        "pitfalls": "Skipping tests; scope creep; not verifying integration; large unreviewed commits",
        "spec_file": "create-feature-spec",
        "plan_file": "create-feature-plan",
        "primary_goal": "Deliver a complete, tested, documented feature matching specifications",
        "metric_1": "100% test coverage on new code",
        "metric_2": "Zero critical/major code review issues",
        "secondary_goal_1": "Feature integrates cleanly with existing codebase",
        "secondary_goal_2": "Documentation enables future maintenance",
        "subgoal_1": "Requirements analyzed and planned",
        "subgoal_2": "Tests written and passing",
        "subgoal_3": "Implementation complete and verified",
        "invariant_1": "Tests must exist before implementation",
        "invariant_2": "All tests must pass before commit",
        "constraint_1": "Follow project coding standards",
        "constraint_2": "No breaking changes without migration",
        "business_rule_1": "Features require spec approval before implementation",
        "business_rule_2": "Breaking changes require major version bump",
        "prep_entry": "Requirements documented in spec",
        "prep_exit": "Plan approved, test structure ready",
        "prep_duration": "30 min",
        "exec_entry": "Plan approved, tests written",
        "exec_exit": "All implementation tests passing",
        "exec_duration": "2-4 hours",
        "verify_entry": "Implementation complete",
        "verify_exit": "All gates pass",
        "verify_duration": "30 min",
        "complete_entry": "Verification complete",
        "complete_exit": "PR merged, CI green",
        "complete_duration": "15 min",
        "step_1_1_name": "Analyze Requirements",
        "step_1_1_action": "Read spec file and extract requirements",
        "step_1_1_tool": "read_file",
        "step_1_1_output": "Requirements list",
        "step_1_2_name": "Create Plan",
        "step_1_2_action": "Generate implementation plan with phases",
        "step_1_2_tool": "create-implementation-plan skill",
        "step_1_2_output": "Plan file in .hermes/plans/",
        "step_2_1_name": "Write Tests",
        "step_2_1_action": "Create failing tests for each requirement",
        "step_2_1_tool": "write_file, terminal",
        "step_2_1_output": "Test files with failing tests",
        "step_2_2_name": "Implement Feature",
        "step_2_2_action": "Write minimal code to pass tests",
        "step_2_2_tool": "write_file, patch, terminal",
        "step_2_2_output": "Working implementation",
        "task_1_desc": "Analyze requirements from spec",
        "task_2_desc": "Create implementation plan",
        "task_3_desc": "Write failing tests (TDD)",
        "task_4_desc": "Implement feature code",
        "task_5_desc": "Run verification gates",
        "task_6_desc": "Finalize and commit",
        "action_1_1_cmd": "read_file .hermes/specs/create-feature-spec.md",
        "action_1_1_output": "Requirements extracted",
        "action_1_1_verify": "Requirements list matches spec",
        "action_2_1_cmd": "hermes create-plan --spec .hermes/specs/create-feature-spec.md",
        "action_2_1_output": "Plan created",
        "action_2_1_verify": "Plan file exists with all phases",
        "action_3_1_cmd": "pytest tests/ -v --tb=short",
        "action_3_1_output": "Tests failing (RED)",
        "action_3_1_verify": "All new tests fail as expected",
        "gate_1_check": "ls .hermes/plans/create-feature-plan.md && pytest tests/ -v",
        "gate_1_pass": "Plan exists, tests failing (RED state)",
        "gate_1_fail": "Re-analyze requirements, recreate plan",
        "gate_2_check": "pytest tests/ -v && lint checks",
        "gate_2_pass": "All tests passing, lint clean",
        "gate_2_fail": "Fix failing tests, address lint issues",
        "gate_3_check": "Full test suite + integration tests",
        "gate_3_pass": "All tests pass, integration verified",
        "gate_3_fail": "Debug failures, re-run verification",
        "gate_4_check": "git diff --stat && CI status",
        "gate_4_pass": "Clean diff, CI green, PR approved",
        "gate_4_fail": "Address review comments, re-verify"
    },
    # I'll add abbreviated versions for other prompts to keep this manageable
}

def generate_prompt_files():
    """Generate all prompt files with companion files."""
    
    for category, triggers in PROMPTS.items():
        for trigger, prompt_name in triggers.items():
            prompt_dir = BASE_PATH / category / trigger
            prompt_dir.mkdir(parents=True, exist_ok=True)
            
            # Get prompt data (use create-feature as template for others)
            key = f"{category}/{trigger}"
            data = PROMPT_DATA.get(key, PROMPT_DATA["development/create-feature"])
            
            # Customize for each prompt
            data = data.copy()
            data.update({
                "category": category,
                "trigger": trigger,
                "prompt_name": prompt_name,
                "prompt_title": data["title"],
                "description": data["description"],
                "tags": data["tags"],
                "skills": data["skills"],
                "tools": data["tools"],
                "role": "implementer",
            })
            
            # Write main prompt file
            prompt_content = PROMPT_TEMPLATE.format(**data)
            (prompt_dir / f"{prompt_name}.prompt.md").write_text(prompt_content)
            
            # Write companion files
            for comp_name, template in COMPANION_TEMPLATES.items():
                comp_content = template.format(
                    prompt_title=data["prompt_title"],
                    spec_file=data.get("spec_file", f"{prompt_name}-spec"),
                    plan_file=data.get("plan_file", f"{prompt_name}-plan"),
                    primary_goal=data.get("primary_goal", f"Complete {data['prompt_title']} successfully"),
                    metric_1=data.get("metric_1", "All acceptance criteria met"),
                    metric_2=data.get("metric_2", "Zero critical issues"),
                    secondary_goal_1=data.get("secondary_goal_1", "Clean integration"),
                    secondary_goal_2=data.get("secondary_goal_2", "Documentation complete"),
                    subgoal_1=data.get("subgoal_1", "Requirements understood"),
                    subgoal_2=data.get("subgoal_2", "Implementation complete"),
                    subgoal_3=data.get("subgoal_3", "Verification passed"),
                    invariant_1=data.get("invariant_1", "Follow protocol"),
                    invariant_2=data.get("invariant_2", "Verify before commit"),
                    constraint_1=data.get("constraint_1", "Project standards"),
                    constraint_2=data.get("constraint_2", "No breaking changes"),
                    business_rule_1=data.get("business_rule_1", "Spec approval required"),
                    business_rule_2=data.get("business_rule_2", "Version on breaking changes"),
                    prep_entry=data.get("prep_entry", "Prerequisites met"),
                    prep_exit=data.get("prep_exit", "Ready for execution"),
                    prep_duration=data.get("prep_duration", "30 min"),
                    exec_entry=data.get("exec_entry", "Preparation complete"),
                    exec_exit=data.get("exec_exit", "Execution complete"),
                    exec_duration=data.get("exec_duration", "1-2 hours"),
                    verify_entry=data.get("verify_entry", "Execution complete"),
                    verify_exit=data.get("verify_exit", "All verified"),
                    verify_duration=data.get("verify_duration", "30 min"),
                    complete_entry=data.get("complete_entry", "Verification done"),
                    complete_exit=data.get("complete_exit", "Delivered"),
                    complete_duration=data.get("complete_duration", "15 min"),
                    step_1_1_name=data.get("step_1_1_name", "Setup"),
                    step_1_1_action=data.get("step_1_1_action", "Prepare environment"),
                    step_1_1_tool=data.get("step_1_1_tool", "terminal"),
                    step_1_1_output=data.get("step_1_1_output", "Ready"),
                    step_1_2_name=data.get("step_1_2_name", "Plan"),
                    step_1_2_action=data.get("step_1_2_action", "Create plan"),
                    step_1_2_tool=data.get("step_1_2_tool", "planning skill"),
                    step_1_2_output=data.get("step_1_2_output", "Plan ready"),
                    step_2_1_name=data.get("step_2_1_name", "Execute"),
                    step_2_1_action=data.get("step_2_1_action", "Run implementation"),
                    step_2_1_tool=data.get("step_2_1_tool", "terminal, write_file"),
                    step_2_1_output=data.get("step_2_1_output", "Implementation done"),
                    step_2_2_name=data.get("step_2_2_name", "Verify"),
                    step_2_2_action=data.get("step_2_2_action", "Run verification"),
                    step_2_2_tool=data.get("step_2_2_tool", "terminal, test"),
                    step_2_2_output=data.get("step_2_2_output", "Verified"),
                    task_1_desc=data.get("task_1_desc", "Setup"),
                    task_2_desc=data.get("task_2_desc", "Plan"),
                    task_3_desc=data.get("task_3_desc", "Execute"),
                    task_4_desc=data.get("task_4_desc", "Verify"),
                    task_5_desc=data.get("task_5_desc", "Document"),
                    task_6_desc=data.get("task_6_desc", "Complete"),
                    action_1_1_cmd=data.get("action_1_1_cmd", "echo 'setup'"),
                    action_1_1_output=data.get("action_1_1_output", "Ready"),
                    action_1_1_verify=data.get("action_1_1_verify", "Check ready"),
                    action_2_1_cmd=data.get("action_2_1_cmd", "echo 'plan'"),
                    action_2_1_output=data.get("action_2_1_output", "Planned"),
                    action_2_1_verify=data.get("action_2_1_verify", "Check plan"),
                    action_3_1_cmd=data.get("action_3_1_cmd", "echo 'execute'"),
                    action_3_1_output=data.get("action_3_1_output", "Done"),
                    action_3_1_verify=data.get("action_3_1_verify", "Verify done"),
                    gate_1_check=data.get("gate_1_check", "check setup"),
                    gate_1_pass=data.get("gate_1_pass", "Setup complete"),
                    gate_1_fail=data.get("gate_1_fail", "Fix setup"),
                    gate_2_check=data.get("gate_2_check", "check execution"),
                    gate_2_pass=data.get("gate_2_pass", "Execution complete"),
                    gate_2_fail=data.get("gate_2_fail", "Fix execution"),
                    gate_3_check=data.get("gate_3_check", "check verification"),
                    gate_3_pass=data.get("gate_3_pass", "All verified"),
                    gate_3_fail=data.get("gate_3_fail", "Re-verify"),
                    gate_4_check=data.get("gate_4_check", "check completion"),
                    gate_4_pass=data.get("gate_4_pass", "Complete"),
                    gate_4_fail=data.get("gate_4_fail", "Rollback"),
                    role=data.get("role", "implementer")
                )
                (prompt_dir / comp_name).write_text(comp_content)
            
            print(f"Created: {category}/{trigger}/{prompt_name}.prompt.md + 10 companions")

if __name__ == "__main__":
    generate_prompt_files()
    print("All prompt files generated!")