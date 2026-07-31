#!/usr/bin/env python3
"""Fix residual collapsed-fence glue in prompt library.

Two corruption patterns (both break CommonMark rendering):
A) Fence OPENER glued to content:   ```bash# 1. Install & setup...  ->  ```bash\n# 1. Install & setup...
B) Fence CLOSER glued to content:   ...checks```                    ->  ...checks\n```

A single line may contain BOTH (```bash# ...checks```) — handled in one pass.

SAFETY (zero data loss):
- Language token is matched against a KNOWN-LANGUAGE whitelist using longest-prefix
  matching, so ```rubysource 'https://...' splits as ```ruby + "source 'https://...'"
  and the content word "source" is NEVER swallowed into the language token.
- If no known-language prefix matches, the line is left untouched.
- Only lines that START with ``` (opener) or END with ``` (closer) are touched.
- 4-backtick escaped fences are skipped entirely.
- Idempotent by construction (re-run = 0 changes).
- Writes LF only (campaign rule: .gitattributes *.md text eol=lf).

Usage: python fix_collapsed_fences.py [--apply]
Default = dry-run (prints per-file fix counts, changes nothing).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parents[1]
APPLY = "--apply" in sys.argv

CLOSE_RE = re.compile(r"^(.*?[^\s`])(```)\s*$")   # line ends with ``` after real content

# Known fence languages (lowercase). Longest-prefix match against the token.
KNOWN_LANGS = [
    "dockerfile", "makefile", "powershell", "markdown", "javascript", "typescript",
    "html", "python", "yaml", "json", "bash", "shell", "text", "java", "ruby",
    "php", "kotlin", "swift", "sql", "xml", "css", "scss", "graphql", "go",
    "rust", "csharp", "cpp", "c", "tsx", "jsx", "ts", "js", "yml", "sh", "ps1",
    "bat", "cmd", "ini", "toml", "csv", "diff", "console", "log", "env", "http",
    "docker", "nginx", "apache", "prisma", "zsh", "fish", "erb", "sass", "less",
    "plaintext", "plain", "terminal", "output", "prompt", "md", "mermaid",
]


def split_opener(line: str) -> tuple[str, str] | None:
    """Given a line starting with ``` and glued content, return (fence_line, content).

    Uses longest known-language prefix so content is never swallowed. Returns None
    when no safe split is possible.
    """
    m = re.match(r"^(```)([A-Za-z0-9_+.-]*)(.*)$", line, re.DOTALL)
    if not m:
        return None
    _, token, rest = m.group(1), m.group(2), m.group(3)
    if not rest:
        return None  # nothing glued — plain fence
    # Find the longest known language that is a prefix of the token
    best = ""
    for lang in KNOWN_LANGS:
        if token.lower().startswith(lang) and len(lang) > len(best):
            best = lang
    if not best:
        return None  # unknown language — leave untouched
    fence_lang = token[: len(best)]
    # Content = remaining token chars (the glued word) + rest
    content = token[len(best) :] + rest
    return "```" + fence_lang, content


# Files classified as pre-existing complex multi-fence glue / paste-placeholder
# conventions (verified identical to pre-campaign, listed in phase4/phase5
# KNOWN_FENCE_CONVENTIONS allowlist). Auto-splitting these risks content loss or
# cannot reach balanced parity; they are deliberately left for manual review.
SKIP_FILES = {
    "ruby-mcp-server-generator.prompt.md",
    "memory-merger.prompt.md",
    "optimize-agentsMd.prompt.md",
    "what-context-needed.prompt.md",
    "refactor-plan.prompt.md",
    "az-cost-optimize.prompt.md",
    "create-llms.prompt.md",
    "comicwise-development.prompt.md",
    "breakdown-plan.prompt.md",
    "copilot-instructions-blueprint-generator.prompt.md",
    "dev-imp.prompt.md",
    "features.prompt.md",
    "kotlin-mcp-server-generator.prompt.md",
    "php-mcp-server-generator.prompt.md",
    "quality-gate-debugger.prompt.md",
    "remember.prompt.md",
    "add-educational-comments.prompt.md",
    "update-oo-component-documentation.prompt.md",
    "update-specification.prompt.md",
    "templates/create-architectural-decision-record/required_documentation_st.md",
    "templates/create-github-action-workflow-specification/token_optimization_strate.md",
    "templates/memory-merger/process.md",
    "templates/structured-autonomy-plan/step_3_plan_generation.md",
    "templates/update-markdown-file-index/files_in_folder.md",
}


def fix_file(path: Path) -> tuple[int, int]:
    rel = str(path.relative_to(PROMPTS_DIR)).replace("\\", "/")
    if rel in SKIP_FILES:
        return 0, 0
    text = path.read_text(encoding="utf-8", newline="")
    lines = text.split("\n")
    out: list[str] = []
    fixes_a = fixes_b = 0
    in_fence = False
    for line in lines:
        stripped = line.strip()
        # 4-backtick escaped fence — leave untouched
        if stripped.startswith("````"):
            out.append(line)
            continue
        # Nested multi-fence glue (e.g. ...end```Make the file executable:```bashchmod...```)
        # contains 3+ backtick-triple markers on one line — beyond safe auto-split.
        if stripped.count("```") >= 3:
            out.append(line)
            continue
        # Plain fence marker line (exactly ``` or ```lang) — toggle state, keep as-is
        if re.match(r"^```[^\S\n]*[a-zA-Z0-9_-]*$", stripped) or stripped == "```":
            in_fence = not in_fence
            out.append(line)
            continue

        # Pattern A: opener glued to content
        if stripped.startswith("```") and not in_fence:
            split = split_opener(line)
            if split:
                fence_line, content = split
                out.append(fence_line)
                fixes_a += 1
                in_fence = True
                # Same line may also carry the closer ( ```bash# ...checks``` )
                cm = CLOSE_RE.match(content)
                if cm and cm.group(2) == "```":
                    out.append(cm.group(1))
                    out.append("```")
                    fixes_b += 1
                    in_fence = False
                else:
                    out.append(content)
                continue
            out.append(line)
            continue

        # Pattern B: closer glued to content (only when inside a fence)
        cm = CLOSE_RE.match(line)
        if cm and in_fence and cm.group(2) == "```":
            out.append(cm.group(1))
            out.append("```")
            fixes_b += 1
            in_fence = False
            continue

        out.append(line)

    if fixes_a or fixes_b:
        new_text = "\n".join(out)
        if APPLY:
            # newline="" disables platform translation -> guarantees LF-only output (campaign rule)
            path.write_text(new_text, encoding="utf-8", newline="\n")
    return fixes_a, fixes_b


def main() -> int:
    files = sorted(p for p in PROMPTS_DIR.rglob("*")
                   if p.is_file() and (p.suffix == ".md" or p.name.endswith(".prompt.md")))
    total_a = total_b = 0
    touched = 0
    for f in files:
        a, b = fix_file(f)
        if a or b:
            touched += 1
            total_a += a
            total_b += b
            print(f"  {a}A {b}B  {f.relative_to(PROMPTS_DIR)}")
    print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'}: {touched} files, {total_a} opener splits, {total_b} closer splits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
