#!/usr/bin/env python3
"""Generate proper script wrapper skill files for Hermes."""

import asyncio
import os

SCRIPTS_DIR = r"C:\Users\Alexa\AppData\Local\hermes\scripts"
SKILLS_DIR = r"C:\Users\Alexa\AppData\Local\hermes\skills\development"

EXCLUDE = {"__pycache__", "skill_name_to_path.json", "memory_repair_artifacts"}

scripts = sorted(
    [
        f
        for f in os.listdir(SCRIPTS_DIR)
        if f not in EXCLUDE and not f.startswith(".") and os.path.isfile(os.path.join(SCRIPTS_DIR, f))
    ]
)


def script_to_skill_name(filename):
    base = os.path.splitext(filename)[0]
    name = base.replace("_", "-").replace(".", "-").lower()
    # Handle .cjs and .js duplicate names
    if filename.endswith(".cjs") and name.endswith("-cjs"):
        pass  # already has -cjs suffix
    elif filename.endswith(".cjs"):
        name = name + "-cjs"
    if filename.endswith(".js") and name.endswith("-js"):
        pass  # already has -js suffix
    elif filename.endswith(".js") and not name.endswith("-js"):
        name = name + "-js"
    return name


def title_case(name):
    """Convert snake_case/kebab-case to Title Case."""
    words = name.replace("-", " ").replace("_", " ").split()
    return " ".join(w.capitalize() for w in words)


def get_short_desc(filename):
    """Generate a short description based on the filename content."""
    base = os.path.splitext(filename)[0].lower()
    ext = os.path.splitext(filename)[1].lower()  # noqa: F841

    # Check common prefixes
    if base.startswith("add_"):
        return "Adds configuration entries or hooks to Hermes setup"
    if base.startswith("analyze_"):
        return "Analyzes HuggingFace model metadata and configurations"
    if base.startswith("apply_"):
        return "Applies VS Code customizations from templates"
    if base.startswith("audit_"):
        rest = base.replace("audit_", "").replace("_", " ")
        return f"Audits {rest} for issues and quality concerns"
    if base.startswith("audit-"):
        rest = base.replace("audit-", "").replace("_", " ")
        return f"Audit script for {rest} analysis"
    if base.startswith("batch_"):
        rest = base.replace("batch_", "").replace("_", " ")
        return f"Batch processing for {rest}"
    if base.startswith("batch-"):
        rest = base.replace("batch-", "").replace("_", " ")
        return f"Batch operation for {rest}"
    if base.startswith("benchmark_"):
        return "Benchmarks LLM models for performance comparison"
    if base.startswith("boost_"):
        return "Boosts quality scores for near-passing skill references"
    if base.startswith("build_"):
        return "Builds path mappings between script and skill locations"
    if base.startswith("categorize_"):
        return "Categorizes skills by content and tags"
    if base.startswith("check_"):
        return "Checks for handle or resource availability"
    if base.startswith("configure_"):
        return "Configures Hermes settings and provider integrations"
    if base.startswith("consolidate_"):
        return "Consolidates duplicate or overlapping skills"
    if base.startswith("copilot_"):
        return "Sets up Copilot MCP server integration"
    if base.startswith("create_missing_"):
        rest = base.replace("create_missing_", "").replace("_", " ")
        return f"Creates missing {rest} files for profiles"
    if base.startswith("dedupe_"):
        return "Deduplicates overlapping or redundant skills"
    if base.startswith("dev-init-"):
        return "Initializes development code samples for reference"
    if base.startswith("docs-inventory"):
        return "Generates documentation inventory reports"
    if base.startswith("find_"):
        rest = base.replace("find_", "").replace("_", " ")
        return f"Finds {rest} in the system"
    if base.startswith("fix_"):
        rest = base.replace("fix_", "").replace("_", " ")
        return f"Fixes {rest} issues across files"
    if base.startswith("fix-"):
        rest = base.replace("fix-", "").replace("_", " ")
        return f"Fixes {rest} issues"
    if base.startswith("generate_"):
        rest = base.replace("generate_", "").replace("_", " ")
        return f"Generates {rest}"
    if base.startswith("generate-"):
        rest = base.replace("generate-", "").replace("_", " ")
        return f"Generates {rest}"
    if base.startswith("hello"):
        return "Simple example script for testing purposes"
    if base.startswith("inventory_"):
        rest = base.replace("inventory_", "").replace("_", " ")
        return f"Creates inventory of {rest} in the system"
    if base.startswith("inventory-"):
        rest = base.replace("inventory-", "").replace("_", " ")
        return f"Inventories {rest}"
    if base.startswith("lcs"):
        return "Longest common subsequence utility for string comparison"
    if base.startswith("list-"):
        rest = base.replace("list-", "").replace("_", " ")
        return f"Lists available {rest}"
    if base.startswith("memory_"):
        return "Repairs or manages memory files for profiles"
    if base.startswith("merge_"):
        rest = base.replace("merge_", "").replace("_", " ")
        return f"Merges {rest} files or configurations"
    if base.startswith("model_"):
        return "Discovers or validates available LLM models"
    if base.startswith("normalize_"):
        rest = base.replace("normalize_", "").replace("_", " ")
        return f"Normalizes {rest} formatting"
    if base.startswith("patch_"):
        rest = base.replace("patch_", "").replace("_", " ")
        return f"Patches {rest} in skill files"
    if base.startswith("phase4-"):
        return "Phase 4 reconstruction script for skill auditing"
    if base.startswith("prompt_"):
        rest = base.replace("prompt_", "").replace("_", " ")
        return f"Performs {rest} on prompt files"
    if base.startswith("prompt-"):
        rest = base.replace("prompt-", "").replace("_", " ")
        return f"Performs {rest} on prompts"
    if base.startswith("quarantine_"):
        return "Quarantines low-quality or failing skills"
    if base.startswith("repair-"):
        return "Repairs frontmatter closure issues in YAML"
    if base.startswith("score-"):
        return "Scores documentation quality metrics"
    if base.startswith("session-"):
        return "Session audit script for Hermes sessions"
    if base.startswith("skill_"):
        rest = base.replace("skill_", "").replace("_", " ")
        return f"Script for skill {rest}"
    if base.startswith("skills-"):
        rest = base.replace("skills-", "").replace("_", " ")
        return f"Performs {rest} on skill files"
    if base.startswith("test_"):
        return "Tests LLM model availability and response quality"
    if base.startswith("trim_"):
        rest = base.replace("trim_", "").replace("_", " ")
        return f"Trims {rest} content from files"
    if base.startswith("update_"):
        return "Updates agents.md file with current configuration"
    if base.startswith("validate_"):
        rest = base.replace("validate_", "").replace("_", " ")
        return f"Validates {rest} for correctness"
    if base.startswith("validate-"):
        rest = base.replace("validate-", "").replace("_", " ")
        return f"Validates {rest}"
    if base.startswith("verify-"):
        return "Verifies frontmatter correctness across skill files"
    return f"Script for {title_case(base)} operations"


def get_tags(filename):
    base = filename.lower()
    ext = os.path.splitext(filename)[1].lower()
    tags = []
    if ext == ".py":
        tags.append("python")
    elif ext in (".js", ".cjs"):
        tags.append("javascript")
    elif ext == ".ps1":
        tags.append("powershell")
    elif ext == ".sh":
        tags.append("bash")
    if "audit" in base:
        tags.append("audit")
    if "vscode" in base:
        tags.append("vscode")
    if "fix" in base or "patch" in base or "repair" in base:
        tags.append("remediation")
    if "skill" in base and "skills" not in tags:
        tags.append("skills")
    if "prompt" in base:
        tags.append("prompts")
    if "config" in base:
        tags.append("configuration")
    if "validate" in base or "verify" in base:
        tags.append("validation")
    if "trim" in base:
        tags.append("cleanup")
    if "batch" in base:
        tags.append("batch")
    if "model" in base:
        tags.append("models")
    if "frontmatter" in base or "yaml" in base:
        tags.append("frontmatter")
    if "memory" in base:
        tags.append("memory")
    if "merge" in base:
        tags.append("merge")
    if "normalize" in base:
        tags.append("normalization")
    if "inventory" in base:
        tags.append("inventory")
    if "generate" in base:
        tags.append("generation")
    if "hello" in base:
        tags.append("example")
    if "hook" in base:
        tags.append("hooks")
    if "profile" in base:
        tags.append("profiles")
    if "categorize" in base or "consolidate" in base or "dedupe" in base:
        tags.append("organization")
    if "copilot" in base:
        tags.append("copilot")
    if "lcs" in base:
        tags.append("utility")
    if "quarantine" in base:
        tags.append("quarantine")
    if "score" in base or "benchmark" in base or "test" in base:
        tags.append("evaluation")
    if "session" in base:
        tags.append("sessions")
    if "dev-init" in base:
        tags.append("development")
    tags.append("scripts")
    # Dedupe preserving order
    seen = set()
    return [t for t in tags if not (t in seen or seen.add(t))]


def get_tool_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    mapping = {
        ".py": "Python",
        ".js": "Node.js",
        ".cjs": "Node.js (CommonJS)",
        ".ps1": "PowerShell",
        ".sh": "Bash",
    }
    return mapping.get(ext, filename)


def get_run_cmd(filename):
    ext = os.path.splitext(filename)[1].lower()
    mapping = {
        ".py": "python",
        ".js": "node",
        ".cjs": "node",
        ".ps1": "powershell -File",
        ".sh": "bash",
    }
    return mapping.get(ext, "python")


def generate_skill(filename):
    skill_name = script_to_skill_name(filename)
    title = title_case(os.path.splitext(filename)[0].replace("_", " ").replace("-", " "))
    desc = get_short_desc(filename)
    tags = get_tags(filename)
    tool_type = get_tool_type(filename)
    run_cmd = get_run_cmd(filename)

    tags_yaml = "\n  - " + "\n  - ".join(tags)

    content = f"""---
name: {skill_name}
title: {title}
description: {desc}
version: 1.0.0
author: Hermes Agent
license: MIT
tags:{tags_yaml}
---

# {title}

## Overview

Wrapper skill for the `{filename}` script in `~/AppData/Local/hermes/scripts/`.

The script is located at `~/AppData/Local/hermes/scripts/{filename}`.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/{filename}`

**Type:** {tool_type}

**Usage:**
```bash
{run_cmd} {filename} [options]
```

Run from the scripts directory or use the full path:
```bash
cd ~/AppData/Local/hermes/scripts && {run_cmd} {filename} [options]
```

## When to Use

- When you need to perform {title.lower()} as part of your workflow
- When automating batch operations that involve this script
- When you need the specific functionality this script provides

## When NOT to Use

- When you are looking for a more general-purpose tool for the same task
- When the environment does not support {tool_type} execution
- When the specific task is better handled by Hermes built-in commands

## Workflow

### Phase 1: Setup
Ensure the Hermes scripts directory is accessible and all dependencies for this script are installed. Verify the script exists at the expected path. For Python scripts, check that required packages are installed. For PowerShell scripts, ensure execution policy permits running scripts.

### Phase 2: Run
Execute the script with the appropriate arguments. Review any usage/help output if needed by passing `--help` or no arguments.

### Phase 3: Verify
Check the script output for correctness. Verify any files that were modified or created. Confirm the script completed with exit code 0.

## Verification Checklist

- [ ] Script executes without errors (exit code 0)
- [ ] Output matches expected format
- [ ] Any file changes are as anticipated
- [ ] Script arguments work as documented
- [ ] No unintended side effects were introduced
- [ ] Help/usage text displays correctly
- [ ] Exit codes are handled appropriately

## Pitfalls

- Always run Python scripts from within a virtual environment to avoid dependency conflicts
- PowerShell scripts on Windows may be blocked by execution policy (`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)
- Node.js scripts may require `npm install` for dependencies before running
- Some scripts modify files in-place; always back up before running
- The script path must be absolute or run from the scripts directory
"""
    return skill_name, content


def get_tags_suffix(filename):
    # Legacy - not used
    return ""


async def main():
    count = 0
    for script in scripts:
        skill_name, content = generate_skill(script)
        skill_dir = os.path.join(SKILLS_DIR, skill_name)
        os.makedirs(skill_dir, exist_ok=True)
        skill_path = os.path.join(skill_dir, "SKILL.md")
        with open(skill_path, "w", newline="\r\n") as f:
            f.write(content)
        count += 1
        print(f"  ✓ {skill_name} ← {script}")

    print(f"\n{'=' * 50}")
    print(f"Total skills created: {count}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    asyncio.run(main())
