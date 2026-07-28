from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(r"C:\Users\Alexa\Desktop\SandBox")
PROMPTS_DIR = REPO_ROOT / ".github" / "prompts"
REPORT_PATH = REPO_ROOT / ".github" / "scripts" / "gh-prompt-frontmatter-normalization-report.json"

VERIFY_REPORT = REPO_ROOT / ".github" / "scripts" / "gh-prompt-frontmatter-normalization-verification.json"

# Find a frontmatter segment between the first --- block and the next --- block.
VERIFY_RE = re.compile(
    r"\A(?:[^\n]*\n)*?---\s*\n(?P<yaml>.*?)\n---\s*\n",
    re.DOTALL,
)


def parse_frontmatter(text: str):
    m = VERIFY_RE.match(text)
    if not m:
        return None, None
    raw = m.group("yaml")
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return None, raw
    if not isinstance(data, dict):
        return None, raw
    return data, raw


def main() -> int:
    files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    report = {
        "repo": str(REPO_ROOT),
        "target_glob": str(PROMPTS_DIR / "*.prompt.md"),
        "summary": {
            "verified_total": len(files),
            "parse_pass": 0,
            "parse_fail": 0,
        },
        "failed_files": [],
        "sample_failures": [],
    }

    for path in files:
        text = path.read_text(encoding="utf-8")
        data, raw = parse_frontmatter(text)
        rel = str(path.relative_to(REPO_ROOT))
        if data is None:
            report["summary"]["parse_fail"] += 1
            report["failed_files"].append(rel)
            report["sample_failures"].append({"file": rel, "raw_head": raw.splitlines()[:8] if raw else []})
        else:
            report["summary"]["parse_pass"] += 1

    VERIFY_REPORT.parent.mkdir(parents=True, exist_ok=True)
    VERIFY_REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Verification report written to {VERIFY_REPORT}")
    print(
        f"verified_total={report['summary']['verified_total']} "
        f"parse_pass={report['summary']['parse_pass']} "
        f"parse_fail={report['summary']['parse_fail']}"
    )
    print("failed_files=" + json.dumps(report["failed_files"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
