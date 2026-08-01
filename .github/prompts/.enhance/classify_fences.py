"""Classify remaining fence flags: campaign regression vs pre-existing convention."""

import subprocess
from pathlib import Path

files = [
    "add-educational-comments.prompt.md",
    "az-cost-optimize.prompt.md",
    "breakdown-plan.prompt.md",
    "comicwise-development.prompt.md",
    "copilot-instructions-blueprint-generator.prompt.md",
    "create-llms.prompt.md",
    "dev-imp.prompt.md",
    "features.prompt.md",
    "kotlin-mcp-server-generator.prompt.md",
    "optimize-agentsMd.prompt.md",
    "php-mcp-server-generator.prompt.md",
    "quality-gate-debugger.prompt.md",
    "refactor-plan.prompt.md",
    "remember.prompt.md",
    Path("templates") / "create-architectural-decision-record" / "required_documentation_st.md",
    Path("templates") / "create-github-action-workflow-specification" / "token_optimization_strate.md",
    Path("templates") / "memory-merger" / "process.md",
    Path("templates") / "structured-autonomy-plan" / "step_3_plan_generation.md",
    Path("templates") / "update-markdown-file-index" / "files_in_folder.md",
    "update-oo-component-documentation.prompt.md",
    "update-specification.prompt.md",
    "what-context-needed.prompt.md",
]


def fence_count(rev, path):
    if rev:
        r = subprocess.run(["git", "show", f"{rev}:.github/prompts/{path}"], capture_output=True, text=True)
        if r.returncode != 0:
            return None
        text = r.stdout
    else:
        text = Path(".github/prompts", path).read_text(encoding="utf-8", errors="replace")
    return text.count("```")


print(f"{'file':<62} {'pre':>4} {'now':>4}")
for f in files:
    pre = fence_count("845d623d", f)
    now = fence_count(None, f)
    if pre is None:
        marker = "  (new file)"
    elif pre % 2 == 0 and now % 2 != 0:
        marker = "  <-- REGRESSION"
    elif pre == now:
        marker = "  (pre-existing convention)"
    else:
        marker = "  (changed)"
    print(f"{f!s:<62} {pre!s:>4} {now:>4}{marker}")
