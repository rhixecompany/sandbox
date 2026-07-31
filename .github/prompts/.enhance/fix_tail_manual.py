#!/usr/bin/env python3
"""
fix_tail_manual.py — Surgical repair of the final genuine glue cases that
conservative pass guards deliberately left (31 flagged; ~20 real, 11 false
positives like template placeholders).

Each entry: (relpath, old_line_prefix, new_lines). Applied only when the line
starts with the exact old prefix (whitespace-sensitive), so no collateral
damage. Dry-run default; --apply writes. LF output.
"""
import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

FIXES = [
    # (relpath, old_prefix, [replacement lines])
    ("bigquery-pipeline-audit.prompt.md",
     "## C) BACKFILL AND LOOP DESIGN**Hard fail if:**",
     ["## C) BACKFILL AND LOOP DESIGN", "", "**Hard fail if:**"]),
    ("breakdown-plan.prompt.md",
     "## Story StatementAs a **{user type}**",
     ["## Story Statement", "", "As a **{user type}**"]),
    ("comicwise-development.prompt.md",
     "## Project State Summary**ComicWise**",
     ["## Project State Summary", "", "**ComicWise**"]),
    ("create-spring-boot-java-project.prompt.md",
     "## Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services- Create",
     ["## Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services", "", "- Create"]),
    ("declarative-agents.prompt.md",
     "## Workflow 1: Basic Agent Creation**Perfect for**:",
     ["## Workflow 1: Basic Agent Creation", "", "**Perfect for**:"]),
    ("declarative-agents.prompt.md",
     "## Workflow 2: Advanced Enterprise Agent Design**Perfect for**:",
     ["## Workflow 2: Advanced Enterprise Agent Design", "", "**Perfect for**:"]),
    ("dev-imp.prompt.md",
     "## ScriptsNo external scripts required",
     ["## Scripts", "", "No external scripts required"]),
    ("editorconfig.prompt.md",
     "## Rule-by-Rule Explanation- `root = true`:",
     ["## Rule-by-Rule Explanation", "", "- `root = true`:"]),
    ("java-junit.prompt.md",
     "## Data-Driven (Parameterized) Tests- Use `@ParameterizedTest`",
     ["## Data-Driven (Parameterized) Tests", "", "- Use `@ParameterizedTest`"]),
    ("mkdocs-translations.prompt.md",
     "## ObjectiveTranslate all documentation",
     ["## Objective", "", "Translate all documentation"]),
    ("model-recommendation.prompt.md",
     "## MissionAnalyze `.agent.md`",
     ["## Mission", "", "Analyze `.agent.md`"]),
    ("model-recommendation.prompt.md",
     "### Analyzing Multiple FilesIf user provides multiple files:",
     ["### Analyzing Multiple Files", "", "If user provides multiple files:"]),
    ("model-recommendation.prompt.md",
     "### Comparative AnalysisIf user asks",
     ["### Comparative Analysis", "", "If user asks"]),
    ("model-recommendation.prompt.md",
     "### Example 4: Free Tier User with Planning Mode**File**:",
     ["### Example 4: Free Tier User with Planning Mode", "", "**File**:"]),
    ("playwright-explore-website.prompt.md",
     "### @explorerA careful site explorer",
     ["### @explorer", "", "A careful site explorer"]),
    ("playwright-explore-website.prompt.md",
     "### @testerA test-minded reviewer",
     ["### @tester", "", "A test-minded reviewer"]),
    ("postgresql-code-review.prompt.md",
     "## 🎯 PostgreSQL-Specific Review Areas>",
     ["## 🎯 PostgreSQL-Specific Review Areas"]),
    ("postgresql-code-review.prompt.md",
     "## 🔍 PostgreSQL-Specific Anti-Patterns>",
     ["## 🔍 PostgreSQL-Specific Anti-Patterns"]),
    ("postgresql-code-review.prompt.md",
     "## 📝 PostgreSQL-Specific Review Guidelines1. **Data Type Optimization**",
     ["## 📝 PostgreSQL-Specific Review Guidelines", "", "1. **Data Type Optimization**"]),
    ("postgresql-optimization.prompt.md",
     "## � PostgreSQL-Specific Features",
     ["## PostgreSQL-Specific Features"]),
    ("power-bi-model-design-review.prompt.md",
     "### **Phase 1: Model Architecture Analysis**>> #",
     ["### **Phase 1: Model Architecture Analysis**"]),
    ("power-bi-performance-troubleshooting.prompt.md",
     "### **Immediate Performance Fixes**>> #",
     ["### **Immediate Performance Fixes**"]),
    ("remember.prompt.md",
     "### ApplyTo FrontmatterTarget specific file patterns",
     ["### Apply to Frontmatter", "", "Target specific file patterns"]),
    ("setup.prompt.md",
     "## 9. Next.js Configuration (`next.config.ts`)Key settings active",
     ["## 9. Next.js Configuration (`next.config.ts`)", "", "Key settings active"]),
    ("setup.prompt.md",
     "### Provider Order (`src/components/layout/layout-provider.tsx`)```SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → children + lazy Toaster```- `ReactQueryDevtools` rendered only in development- `Toaster` lazy-loaded- `ThemeProvider` receives theme config props---",
     ["### Provider Order (`src/components/layout/layout-provider.tsx`)", "", "```tsx", "SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → children + lazy Toaster", "```", "", "- `ReactQueryDevtools` rendered only in development", "- `Toaster` lazy-loaded", "- `ThemeProvider` receives theme config props", "---"]),
]


def fix_text(path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(PROMPTS_DIR).as_posix()
    rel_alt = path.name
    fixes = [f for f in FIXES if f[0] in (rel, rel_alt)]
    if not fixes:
        return text, 0
    changed = 0
    lines = text.split("\n")
    out = []
    for line in lines:
        stripped = line.rstrip("\r\n")
        applied = False
        for _, old, new_lines in fixes:
            if stripped.startswith(old):
                # preserve original indentation for heading
                indent = stripped[: len(stripped) - len(stripped.lstrip())]
                remainder = stripped[len(old):]
                out.extend(indent + n for n in new_lines)
                if remainder:
                    # append remainder to the LAST emitted line (prose/content
                    # continuation), never a fresh line
                    out[-1] = out[-1] + remainder
                changed += 1
                applied = True
                break
        if not applied:
            out.append(line)
    new_text = "\n".join(out)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    new_text = new_text.replace("\r\n", "\n").replace("\r", "\n")
    return new_text, changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    files = sorted(PROMPTS_DIR.glob("*.prompt.md")) + sorted(PROMPTS_DIR.glob("templates/**/*.md"))
    total_files = 0
    total_changes = 0
    for f in files:
        if not f.is_file():
            continue
        new_text, changes = fix_text(f)
        if changes:
            total_files += 1
            total_changes += changes
            if args.apply:
                f.write_text(new_text, encoding="utf-8", newline="")
                print(f"FIXED {f.relative_to(PROMPTS_DIR).as_posix()}: {changes}")
            else:
                print(f"WOULD FIX {f.relative_to(PROMPTS_DIR).as_posix()}: {changes}")
    print(f"\n{total_files} files, {total_changes} fixes ({'APPLIED' if args.apply else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
