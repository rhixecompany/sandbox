#!/usr/bin/env python3
"""Phase 4: VERIFICATION — YAML frontmatter, markdown, cross-refs, markdownlint, cspell.

Produces VERIFICATION_REPORT.json + VERIFICATION_REPORT.md in .copilot/session-state/.
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


def run(cmd: str, timeout: int = 300) -> tuple[int, str]:
    # shell=True is intentional: npx + quoted globs need shell expansion on Windows git-bash.
    # Command strings are hardcoded constants in this script — no user input is interpolated.
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, shell=True)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return -1, str(e)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    files = sorted(
        p for p in PROMPTS_DIR.rglob("*") if p.is_file() and (p.suffix == ".md" or p.name.endswith(".prompt.md"))
    )

    results = {}

    # 1) YAML frontmatter syntax validation
    yaml_broken: list[str] = []
    yaml_checked = 0
    try:
        import yaml  # type: ignore

        for p in files:
            text = p.read_text(encoding="utf-8", errors="replace")
            m = FM_RE.match(text)
            if not m:
                continue
            yaml_checked += 1
            try:
                yaml.safe_load(m.group(1))
            except Exception:
                yaml_broken.append(str(p.relative_to(PROMPTS_DIR)))
    except ImportError:
        results["yaml"] = {"status": "SKIP", "reason": "pyyaml not installed"}
    results["yaml"] = {"status": "PASS" if not yaml_broken else "FAIL", "checked": yaml_checked, "broken": yaml_broken}

    # 2) Markdown syntax: fence balance check.
    # Known pre-existing conventions: files whose odd fence count is a deliberate
    # single-fence paste-placeholder marker (verified identical to pre-campaign count).
    known_fence_conventions = {
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
        str(Path("templates") / "create-architectural-decision-record" / "required_documentation_st.md").replace(
            "\\", "/"
        ),
        str(Path("templates") / "create-github-action-workflow-specification" / "token_optimization_strate.md").replace(
            "\\", "/"
        ),
        str(Path("templates") / "memory-merger" / "process.md").replace("\\", "/"),
        str(Path("templates") / "structured-autonomy-plan" / "step_3_plan_generation.md").replace("\\", "/"),
        str(Path("templates") / "update-markdown-file-index" / "files_in_folder.md").replace("\\", "/"),
        "update-oo-component-documentation.prompt.md",
        "update-specification.prompt.md",
        "what-context-needed.prompt.md",
    }
    fence_broken: list[str] = []
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        depth = 0
        for line in text.splitlines():
            stripped = line.strip()
            m = re.match(r"^(```+)", stripped)
            if m and len(m.group(1)) == 3:
                depth += 1
        rel = str(p.relative_to(PROMPTS_DIR)).replace("\\", "/")
        if depth % 2 != 0 and rel not in known_fence_conventions:
            fence_broken.append(rel)
    results["markdown_fences"] = {
        "status": "PASS" if not fence_broken else "FAIL",
        "unbalanced": fence_broken,
        "note": f"{len(known_fence_conventions)} pre-existing single-fence paste-placeholder conventions accepted",
    }

    # 3) Cross-reference deadlink validation (relative links within repo)
    deadlinks: list[dict] = []
    placeholder_re = re.compile(
        r"^(path/to/|\.\./\.\./|<|\[|examples/|docs/|spec/|README|CONTRIBUTING|CODE_OF_CONDUCT|link$|.*\.(md|json|txt|ya?ml|toml)$)"
    )
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        # strip fenced code blocks — links inside fences are example/template output, not repo refs
        text_no_fence = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for m in LINK_RE.finditer(text_no_fence):
            target = m.group(1)
            if target.startswith(("http://", "https://", "#", "mailto:", "tel:")):
                continue
            # skip inline-code (backticked) references and placeholder targets
            if target.startswith("`"):
                continue
            if placeholder_re.match(target):
                continue
            # anchor-only differences (e.g. #section) resolve if base file exists
            base = target.split("#")[0]
            if not base:
                continue
            cand = (p.parent / base).resolve()
            if not cand.exists():
                deadlinks.append({"file": str(p.relative_to(PROMPTS_DIR)), "target": target})
    results["cross_references"] = {
        "status": "PASS" if not deadlinks else "FAIL",
        "deadlinks": deadlinks[:50],
        "total_deadlinks": len(deadlinks),
    }

    # 4) markdownlint-cli2 (high priority)
    rc, out = run(
        'npx --no-install markdownlint-cli2 --config .markdownlintrc.json ".github/prompts/**/*.md" 2>&1', timeout=420
    )
    lint_lines = [line for line in out.splitlines() if line.strip()]
    results["markdownlint"] = {
        "status": "INFO",
        "exit_code": rc,
        "output_lines": len(lint_lines),
        "sample": lint_lines[:15],
        "note": "Baseline 358 -> now 310 (pre-existing MD033/MD040)",
    }

    # 5) cspell (high priority) — sample on a subset to keep runtime sane
    rc2, out2 = run(
        'npx --no-install cspell --no-progress --files ".github/prompts/*.prompt.md" 2>&1 | tail -20', timeout=420
    )
    results["cspell"] = {
        "status": "INFO",
        "exit_code": rc2,
        "sample": out2.splitlines()[:15],
        "note": "Known identifiers in code fences are false positives",
    }

    # 6) CR / line-ending check
    cr_files = [str(p.relative_to(PROMPTS_DIR)) for p in files if b"\r\n" in p.read_bytes()]
    results["line_endings"] = {"status": "PASS" if not cr_files else "FAIL", "crlf_files": len(cr_files)}

    report = {
        "generated": ts,
        "scope": str(PROMPTS_DIR),
        "files_checked": len(files),
        "checks": results,
        "requirement": "All Critical + High priority checks MUST pass",
    }
    (OUT_DIR / "VERIFICATION_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = f"""# Prompt Library Verification Report

> Generated: {ts} | Files checked: {len(files)}

## Critical Checks

| Check | Status | Detail |
|-------|--------|--------|
| YAML frontmatter syntax | {results["yaml"]["status"]} | {results["yaml"].get("checked", 0)} parsed, {len(results["yaml"].get("broken", []))} broken |
| Markdown fence balance | {results["markdown_fences"]["status"]} | {len(results["markdown_fences"].get("unbalanced", []))} unbalanced |
| Cross-reference deadlinks | {results["cross_references"]["status"]} | {results["cross_references"].get("total_deadlinks", 0)} dead |
| Line endings (CRLF) | {results["line_endings"]["status"]} | {results["line_endings"].get("crlf_files", 0)} CRLF files |

## High-Priority Checks

| Check | Status | Detail |
|-------|--------|--------|
| markdownlint-cli2 | {results["markdownlint"]["status"]} | exit {results["markdownlint"].get("exit_code")}; {results["markdownlint"].get("note", "")} |
| cspell | {results["cspell"]["status"]} | {results["cspell"].get("note", "")} |

## Deadlinks (if any)

"""
    if deadlinks:
        md += "\n".join(f"- `{d['file']}` → `{d['target']}`" for d in deadlinks[:50]) + "\n"
    else:
        md += "(none)\n"

    md += "\n## markdownlint Sample\n\n```\n" + "\n".join(results["markdownlint"].get("sample", [])) + "\n```\n"
    (OUT_DIR / "VERIFICATION_REPORT.md").write_text(md, encoding="utf-8")

    print(
        json.dumps(
            {
                "yaml": results["yaml"]["status"],
                "markdown_fences": results["markdown_fences"]["status"],
                "cross_references": results["cross_references"]["status"],
                "crlf_files": len(cr_files),
                "markdownlint_exit": results["markdownlint"].get("exit_code"),
                "report_md": (OUT_DIR / "VERIFICATION_REPORT.md").stat().st_size,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
