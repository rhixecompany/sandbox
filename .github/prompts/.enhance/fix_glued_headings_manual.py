#!/usr/bin/env python3
"""fix_glued_headings_manual.py — Class B manual repairs.

Explicit curated splits for ambiguous camelCase/bold-embedded glue that the
conservative splitter deliberately leaves alone. Each entry maps a file + a
unique heading prefix to the corrected (heading, body) pair. No fabrication —
only the heading/body boundary is moved.

Usage: python fix_glued_headings_manual.py [--apply]
Default: dry-run printing proposed edits.
"""
import pathlib
import re
import sys

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
APPLY = "--apply" in sys.argv

# file -> (unique-prefix, heading, body)
FIXES = {
    "bigquery-pipeline-audit.prompt.md": [
        ("## B) DRY RUN AND EXECUTION MODES", "## B) DRY RUN AND EXECUTION MODES",
         "Verify a `--mode` flag exists with at least `dry_run` and `execute` options."),
        ("## E) SAFE WRITES AND IDEMPOTENCY", "## E) SAFE WRITES AND IDEMPOTENCY",
         "Identify every write operation. Flag plain `INSERT`/append with no dedup logic."),
    ],
    "breakdown-plan.prompt.md": [
        ("## Labels`epic`,", "## Labels", "- `epic`,"),
        ("## Labels`feature`,", "## Labels", "- `feature`,"),
        ("## Labels`user-story`,", "## Labels", "- `user-story`,"),
        ("## Labels`enabler`,", "## Labels", "- `enabler`,"),
    ],
    "breakdown-test.prompt.md": [
        ("## Labels`test-strategy`", "## Labels", "- `test-strategy`, `istqb`, `iso25010`, `quality-gates`"),
        ("## Labels`playwright`", "## Labels", "- `playwright`, `e2e-test`, `quality-validation`"),
        ("## Labels`quality-assurance`", "## Labels", "- `quality-assurance`, `iso25010`, `quality-gates`"),
    ],
    "cosmosdb-datamodeling.prompt.md": [
        ("## Documentation Workflow🔴", "## Documentation Workflow",
         "🔴 CRITICAL FILE MANAGEMENT: You MUST maintain two markdown files throughout our conversation, treating cosmosdb_requirements as the source of truth."),
        ("### Consolidation Decision FrameworkFor", "### Consolidation Decision Framework",
         "For each pair of related containers, ask:"),
        ("## Container Consolidation AnalysisAfter", "## Container Consolidation Analysis",
         "After identifying aggregates, systematically review for consolidation opportunities:"),
        ("## Design Philosophy & Approach[", "## Design Philosophy & Approach",
         "[Explain the overall approach taken and key design principles applied]"),
        ("## Aggregate Design Decisions[", "## Aggregate Design Decisions",
         "[Explain how you identified aggregates based on access patterns and why certain data was grouped together]"),
        ("## Trade-offs and Optimizations[", "## Trade-offs and Optimizations",
         "[Explain the overall trade-offs made and optimizations used]"),
    ],
    "create-architectural-decision-record.prompt.md": [
        ("## Input ValidationIf", "## Input Validation",
         "If any of the required inputs are not provided or cannot be determined from the conversation history, ask the user to provide them."),
    ],
    "create-implementation-plan.prompt.md": [
        ("## AI-Optimized Implementation Standards-", "## AI-Optimized Implementation Standards",
         "- Use explicit, unambiguous language with zero interpretation required"),
    ],
    "create-technical-spike.prompt.md": [
        ("## File Naming ConventionsUse", "## File Naming Conventions",
         "Use descriptive, kebab-case names that indicate the category and specific unknown."),
        ("## Best Practices for AI Agents1.", "## Best Practices for AI Agents",
         "1. **One Question Per Spike:** Each document focuses on a single technical decision or research question"),
    ],
    "documentation-writer.prompt.md": [
        ("## WORKFLOWYou", "## WORKFLOW",
         "You will follow this process for every documentation request:"),
    ],
    "editorconfig.prompt.md": [
        ("## 📜 MISSIONYou", "## 📜 MISSION",
         "You are an **EditorConfig Expert**. Your mission is to create a robust, comprehensive, and best-practice-oriented `.editorconfig` file."),
    ],
    "java-refactoring-extract-method.prompt.md": [
        ("## TaskApply", "## Task",
         "Apply **Extract Method** to improve readability, testability, maintainability, reusability, modularity, cohesion, low coupling, and consistency."),
    ],
    "java-refactoring-remove-parameter.prompt.md": [
        ("## TaskApply", "## Task",
         "Apply **Remove Parameter** to improve readability, testability, maintainability, reusability, modularity, cohesion, and consistency."),
    ],
    "kotlin-mcp-server-generator.prompt.md": [
        ("## MultiplatformThis", "## Multiplatform",
         "This project uses Kotlin Multiplatform and can target JVM, Wasm, and iOS. See `build.gradle.kts` for platform configuration."),
    ],
    "mcp-deploy-manage-agents.prompt.md": [
        ("### Monitoring and ReportingTrack:", "### Monitoring and Reporting",
         "Track:"),
    ],
    "model-recommendation.prompt.md": [
        ("### Migration PlanningIf", "### Migration Planning",
         "If file specifies a deprecated model:"),
    ],
    "multi-agent-research-template.prompt.md": [
        ("## Phase N:`) not H3", "## Phase N:`)", "not H3"),
    ],
    "power-bi-dax-optimization.prompt.md": [
        ("## Request InstructionsTo", "## Request Instructions",
         "To use this prompt effectively, provide:"),
    ],
    "prompt-management.prompt.md": [
        ("### 5.3 Create missing scriptsIf", "### 5.3 Create missing scripts",
         "If no script exists for a pattern, create:"),
        ("### 6.2 Write validation reportWrite", "### 6.2 Write validation report",
         "Write/update:"),
        ("## DeliverStop", "## Deliver",
         "Stop only after the pipeline is complete and the registry confirms zero unresolved issues. By the end, produce:"),
    ],
    "quality-gate-debugger.prompt.md": [
        ("## ProblemThe", "## Problem",
         "The repository's quality gate failed: `pnpm lint:strict` returned errors and warnings which stopped the pipeline."),
        ("## Proposed approachFollow", "## Proposed approach",
         "Follow a structured, iterative fix loop:"),
        ("## Next actionRun", "## Next action",
         "Run the quality-gate script to generate fresh report files."),
    ],
    "refactor-method-complexity-reduce.prompt.md": [
        ("## ObjectiveRefactor", "## Objective",
         "Refactor the method to reduce its cyclomatic complexity while preserving behavior."),
        ("## ResultThe", "## Result",
         "The refactored method should:"),
    ],
    "seed-review-and-create.prompt.md": [
        ("## ArchitectureThe", "## Architecture",
         "The seed system uses the **Template Method Pattern**:"),
    ],
    "shuffle-json-data.prompt.md": [
        ("## Acceptable JSONWhen", "## Acceptable JSON",
         "When the default behavior is active, acceptable JSON resembles the following pattern:"),
        ("## VariablesWhen", "## Variables",
         "When provided, the following variables override the default state."),
        ("## ExamplesBelow", "## Examples",
         "Below are two sample interactions demonstrating an error case and a successful configuration."),
    ],
    "skills-fix.prompt.md": [
        ("## Reorganization Map (from 2026-06-04 session)Skills", "## Reorganization Map (from 2026-06-04 session)",
         "Skills moved to correct categories:"),
        ("## When to Use` or `", "## When to Use", "- ` or `"),
    ],
    "typespec-create-agent.prompt.md": [
        ("## ExamplesAsk", "## Examples",
         "Ask the user:"),
    ],
    "update-avm-modules-in-bicep.prompt.md": [
        ("### Summary of UpdatesDescribe", "### Summary of Updates",
         "Describe updates made, any manual reviews needed or issues encountered."),
    ],
    "workspace-consolidate.prompt.md": [
        ("### Phase 1: Verify Canonical Script Layout (LIGHT)All", "### Phase 1: Verify Canonical Script Layout (LIGHT)",
         "All 54 operational scripts must live under `projects/Bash/` in organized subdirectories."),
        ("### All Reports Under docs/All", "### All Reports Under docs/",
         "All workspace-level reports go under `docs/`."),
        ("### Required Frontmatter (YAML)Every", "### Required Frontmatter (YAML)",
         "Every `.md` file should have standard frontmatter:"),
        ("### AI-Readiness Scoring ScriptCreate", "### AI-Readiness Scoring Script",
         "Create `projects/Bash/scripts/score-docs.sh` that scores every `.md` file on AI-readiness:"),
    ],
}


def apply_fix(text: str, prefix: str, heading: str, body: str) -> tuple[str, bool]:
    """Replace the glued heading line starting with prefix."""
    lines = text.split("\n")
    changed = False
    out = []
    for ln in lines:
        if ln.startswith(prefix):
            # preserve trailing content after body? body is the full remainder
            out.append(heading)
            out.append(body)
            changed = True
        else:
            out.append(ln)
    return "\n".join(out), changed


def main() -> int:
    total = 0
    for fname, fixes in FIXES.items():
        path = P / fname
        if not path.exists():
            print(f"MISSING {fname}")
            continue
        text = path.read_text(encoding="utf-8")
        if "\r\n" in text:
            text = text.replace("\r\n", "\n")
        fchg = 0
        for prefix, heading, body in fixes:
            new_text, changed = apply_fix(text, prefix, heading, body)
            if changed:
                fchg += 1
                text = new_text
                if APPLY:
                    print(f"{fname}: {prefix}")
            else:
                print(f"  NOT FOUND {fname}: {prefix[:60]}")
        if fchg and APPLY:
            path.write_text(text, encoding="utf-8", newline="\n")
        total += fchg
    print(f"---\n{'APPLIED' if APPLY else 'DRY-RUN'}: total_fixes={total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
