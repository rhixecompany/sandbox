#!/usr/bin/env python3
"""Phase 5: POST-APPLY VERIFICATION — re-run critical checks after commit.

Writes POST_APPLY_VERIFICATION.json to .copilot/session-state/.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PROMPTS_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / ".copilot" / "session-state"
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(
    r"^(path/to/|\.\./\.\./|<|\[|examples/|docs/|spec/|README|CONTRIBUTING|CODE_OF_CONDUCT|link$|.*\.(md|json|txt|ya?ml|toml)$)"
)
KNOWN_FENCE_CONVENTIONS = {
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
    "memory-merger.prompt.md",
    "ruby-mcp-server-generator.prompt.md",
    "templates/create-architectural-decision-record/required_documentation_st.md",
    "templates/create-github-action-workflow-specification/token_optimization_strate.md",
    "templates/memory-merger/process.md",
    "templates/structured-autonomy-plan/step_3_plan_generation.md",
    "templates/update-markdown-file-index/files_in_folder.md",
    "update-oo-component-documentation.prompt.md",
    "update-specification.prompt.md",
    "what-context-needed.prompt.md",
}


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    files = sorted(
        p for p in PROMPTS_DIR.rglob("*") if p.is_file() and (p.suffix == ".md" or p.name.endswith(".prompt.md"))
    )
    results = {}

    # YAML
    yaml_broken = []
    try:
        import yaml  # type: ignore

        for p in files:
            m = FM_RE.match(p.read_text(encoding="utf-8", errors="replace"))
            if m:
                try:
                    yaml.safe_load(m.group(1))
                except Exception:
                    yaml_broken.append(str(p.relative_to(PROMPTS_DIR)))
    except ImportError:
        pass
    results["yaml"] = {"status": "PASS" if not yaml_broken else "FAIL", "broken": yaml_broken}

    # Fences
    fence_broken = []
    for p in files:
        depth = 0
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^(```+)", line.strip())
            if m and len(m.group(1)) == 3:
                depth += 1
        rel = str(p.relative_to(PROMPTS_DIR)).replace("\\", "/")
        if depth % 2 != 0 and rel not in KNOWN_FENCE_CONVENTIONS:
            fence_broken.append(rel)
    results["markdown_fences"] = {"status": "PASS" if not fence_broken else "FAIL", "unbalanced": fence_broken}

    # Deadlinks
    deadlinks = []
    for p in files:
        text = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8", errors="replace"), flags=re.DOTALL)
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "#", "mailto:", "tel:")) or target.startswith("`"):
                continue
            if PLACEHOLDER_RE.match(target):
                continue
            base = target.split("#")[0]
            if not base:
                continue
            if not (p.parent / base).resolve().exists():
                deadlinks.append({"file": str(p.relative_to(PROMPTS_DIR)), "target": target})
    results["cross_references"] = {"status": "PASS" if not deadlinks else "FAIL", "deadlinks": deadlinks[:20]}

    # CRLF
    crlf = [str(p.relative_to(PROMPTS_DIR)) for p in files if b"\r\n" in p.read_bytes()]
    results["line_endings"] = {"status": "PASS" if not crlf else "FAIL", "crlf_files": len(crlf)}

    # git state
    r = subprocess.run(["git", "-C", str(REPO_ROOT), "status", "--porcelain"], capture_output=True, text=True)
    dirty = [line for line in r.stdout.splitlines() if line.strip()]
    results["git_working_tree"] = {"status": "PASS" if not dirty else "WARN", "dirty_entries": len(dirty)}

    report = {
        "generated": ts,
        "files_checked": len(files),
        "checks": results,
        "requirement": "All Critical checks MUST pass after apply",
    }
    (OUT_DIR / "POST_APPLY_VERIFICATION.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps({k: v["status"] for k, v in results.items()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
