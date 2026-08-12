#!/usr/bin/env python3
"""fix_glued_headings_batch2.py — Class B manual repairs, second batch.

Curated explicit splits for the remaining true-glue cases (bold-embedded,
numbered-list, and fence-adjacent glue) plus one restoration.

Usage: python fix_glued_headings_batch2.py [--apply]
Default: dry-run printing proposed edits.
"""
import pathlib
import sys

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
APPLY = "--apply" in sys.argv

# file -> list of (old_prefix, replacement_lines)
FIXES = {
    "breakdown-test.prompt.md": [
        ("## ISTQB Test Case Design**Test Design Technique**:",
         ["## ISTQB Test Case Design", "**Test Design Technique**: {Selected ISTQB technique} **Test Type**: {Functional/Non-Functional/Structural/Change-Related}"]),
    ],
    "dev-imp.prompt.md": [
        ("### Phase 4: Code Review Changed Files (Only After Verification Passes)For EVERY file changed by any generator:",
         ["### Phase 4: Code Review Changed Files (Only After Verification Passes)",
          "For EVERY file changed by any generator:"]),
        ("### Phase 6: Generate Implementation Report (Only After All Fixes Verified)Write a file `dev-imp-report.md` at the PWD with crispy-format markdown:```markdown# ",
         ["### Phase 6: Generate Implementation Report (Only After All Fixes Verified)",
          "Write a file `dev-imp-report.md` at the PWD with crispy-format markdown:",
          "```markdown",
          "# "]),
    ],
    "dev-init.prompt.md": [
        ("### Step 5.2 — Run `context-map`1. Load `prompts/context-map.prompt.md`",
         ["### Step 5.2 — Run `context-map`",
          "1. Load `prompts/context-map.prompt.md`"]),
        ("### Step 5.3 — Run `convert-plaintext-to-md`For each `.github/prompts/*.txt` file:",
         ["### Step 5.3 — Run `convert-plaintext-to-md`",
          "For each `.github/prompts/*.txt` file:"]),
        ("### Step 5.4 — Run `boost-prompt`For each `.github/prompts/*.md` file:",
         ["### Step 5.4 — Run `boost-prompt`",
          "For each `.github/prompts/*.md` file:"]),
        ("### Step 5.5 — Run `ai-prompt-engineering-safety-review`For each `.github/prompts/*.md` and `.github/prompts/*.prompt.md`:",
         ["### Step 5.5 — Run `ai-prompt-engineering-safety-review`",
          "For each `.github/prompts/*.md` and `.github/prompts/*.prompt.md`:"]),
        ("### Step 5.6 — Run `prompt-builder`For any missing prompts:",
         ["### Step 5.6 — Run `prompt-builder`",
          "For any missing prompts:"]),
        ("### Step 5.7 — Run `update-implementation-plan`1. Load `prompts/update-implementation-plan.prompt.md`",
         ["### Step 5.7 — Run `update-implementation-plan`",
          "1. Load `prompts/update-implementation-plan.prompt.md`"]),
    ],
    "generate-custom-instructions-from-codebase.prompt.md": [
        ("### 🧠 **Artificial Intelligence Enhancement**Unlike",
         ["### 🧠 **Artificial Intelligence Enhancement**",
          "Unlike"]),
        ("### 🔄 **Knowledge Capitalization**Transforms",
         ["### 🔄 **Knowledge Capitalization**",
          "Transforms"]),
        ("### 🎯 **Context-Aware Precision**Instead",
         ["### 🎯 **Context-Aware Precision**",
          "Instead"]),
        ("### ⚡ **Automated Consistency**Ensures",
         ["### ⚡ **Automated Consistency**",
          "Ensures"]),
    ],
    "mcp-create-declarative-agent.prompt.md": [
        ("### Add Adaptive Cards (Optional)See the `mcp-create-adaptive-cards` prompt",
         ["### Add Adaptive Cards (Optional)",
          "See the `mcp-create-adaptive-cards` prompt"]),
    ],
    "model-recommendation.prompt.md": [
        ("## Quick Reference**TL;DR**:",
         ["## Quick Reference",
          "**TL;DR**: Use **[Primary Model]** for this task due to [one-sentence rationale]. Cost: [X]x multiplier."]),
    ],
    "multi-agent-research-template.prompt.md": [
        ("- [ ] Phase headings use H2 (`\n\n## Phase N:`)\nnot H3\n",
         ["- [ ] Phase headings use H2 (`## Phase N:`) not H3)"]),
        ("## Phase N:`)\nnot H3\n",
         ["- [ ] Phase headings use H2 (`## Phase N:`) not H3)"]),
    ],
    "multi-stage-dockerfile.prompt.md": [
        ("## Multi-Stage Structure- Use a builder stage",
         ["## Multi-Stage Structure",
          "- Use a builder stage"]),
    ],
    "power-platform-mcp-connector-suite.prompt.md": [
        ("### Mode 6: OAuth Security HardeningImplement",
         ["### Mode 6: OAuth Security Hardening",
          "Implement"]),
    ],
    "skills-fix.prompt.md": [
        ("### Phase 5: Execute Fixes (Priority Order)**F-grade first** — Fix critical issues (unclosed fences, missing frontmatter):````python# For unclosed code fences: append clo",
         ["### Phase 5: Execute Fixes (Priority Order)",
          "**F-grade first** — Fix critical issues (unclosed fences, missing frontmatter):",
          "```python",
          "# For unclosed code fences: append clo"]),
    ],
    "update-specification.prompt.md": [
        ("## 11. Related Specifications / Further Reading[Link to related spec 1] [Link to relevant external documentation]``````",
         ["## 11. Related Specifications / Further Reading",
          "[Link to related spec 1] [Link to relevant external documentation]"]),
    ],
    "write-coding-standards-from-file.prompt.md": [
        ("## 8. Contribution and Enforcement    *Explain how the standards are to be enforced",
         ["## 8. Contribution and Enforcement",
          "*Explain how the standards are to be enforced"]),
        ("## 8. Changes to This Guide    Style evolves.    Propose improvements",
         ["## 8. Changes to This Guide",
          "Style evolves.",
          "Propose improvements"]),
    ],
}


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
        for old, repl in fixes:
            if old in text:
                text = text.replace(old, "\n".join(repl), 1)
                fchg += 1
                if APPLY:
                    print(f"{fname}: {old[:70]}")
            else:
                print(f"  NOT FOUND {fname}: {old[:70]}")
        if fchg and APPLY:
            path.write_text(text, encoding="utf-8", newline="\n")
        total += fchg
    print(f"---\n{'APPLIED' if APPLY else 'DRY-RUN'}: total_fixes={total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
