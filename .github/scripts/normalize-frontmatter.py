from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(r"C:\Users\Alexa\Desktop\SandBox")
PROMPTS_DIR = REPO_ROOT / ".github" / "prompts"
REPORT_PATH = REPO_ROOT / ".github" / "scripts" / "gh-prompt-frontmatter-normalization-report.json"
VERIFY_REPORT = REPO_ROOT / ".github" / "scripts" / "gh-prompt-frontmatter-normalization-verification.json"

# Match first leading frontmatter fence pair including embedded `---` lines.
VERIFY_RE = re.compile(
    r"\A(?P<head>---\s*\n)(?P<yaml>.*?)(?P<tail>\n---\s*\n)(?P<body>.*)\Z",
    re.DOTALL,
)


def extract_frontmatter(text: str):
    m = VERIFY_RE.match(text)
    if not m:
        return None, None, None
    return m.group("yaml"), m.group("tail"), m.group("body")


def is_indented_line(line: str) -> bool:
    return line.startswith(" ") or line.startswith("\t")


def strip_document_end_markers(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        stripped = line.rstrip()
        if stripped == "...":
            continue
        out.append(stripped)
    return out


def normalize_raw_yaml(lines: list[str]) -> tuple[list[str], list[str]]:
    # Remove document-end markers.
    lines = strip_document_end_markers(lines)
    issues = []
    # Remove blank key/value placeholder lines like '...:'.
    cleaned = []
    for line in lines:
        stripped = line.rstrip()
        if re.match(r"^\.\.\.\s*:\s*$", stripped):
            issues.append("removed_blank_dotdotdot_key")
            continue
        cleaned.append(stripped)
    return cleaned, issues


def frontmatter_is_clean(lines: list[str]) -> bool:
    for line in lines:
        if line == "...":
            return False
        if re.match(r"^\.\.\.\s*:\s*$", line):
            return False
    return True


def try_parse_yaml(text: str):
    lines = text.splitlines()
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        cleaned_lines, issues = normalize_raw_yaml(lines)
        if cleaned_lines:
            try:
                data = yaml.safe_load("\n".join(cleaned_lines))
                issues.append("repaired_from_yaml_error")
                return data, issues
            except Exception:
                pass
        return None, [f"yaml_error:{exc}"]
    if not isinstance(data, dict):
        return None, ["frontmatter_not_mapping"]
    return data, []


def try_dump_frontmatter(data: dict) -> str:
    out = "---\n"
    out += yaml.dump(
        data,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        explicit_start=False,
        explicit_end=False,
    )
    if not out.endswith("---"):
        out += "---\n"
    return out


def repair_block(text: str, raw: str, tail: str, body: str):
    data, parse_issues = try_parse_yaml(raw)
    if data is None:
        return None, parse_issues
    dumped = try_dump_frontmatter(data)
    repaired = dumped + ("\n" + body if body else "")
    return repaired, parse_issues


def main() -> int:
    if not PROMPTS_DIR.is_dir():
        print(f"Prompts dir not found: {PROMPTS_DIR}")
        return 1

    files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    if not files:
        print("No prompt files found.")
        return 0

    report = {
        "repo": str(REPO_ROOT),
        "target_glob": str(PROMPTS_DIR / "*.prompt.md"),
        "summary": {
            "total": len(files),
            "passed_before": 0,
            "failed_before": 0,
            "passed_after": 0,
            "failed_after": 0,
            "changed": 0,
            "unchanged": 0,
            "skipped": 0,
        },
        "files": [],
        "changed_files": [],
        "failed_files": [],
    }
    changed_files = []
    failures = []

    for path in files:
        rel = str(path.relative_to(REPO_ROOT))
        original = path.read_text(encoding="utf-8")
        raw, tail, body = extract_frontmatter(original)
        entry = {
            "file": rel,
            "status_before": "unknown",
            "status_after": "unknown",
            "changed": False,
            "issues": [],
            "parse_before": None,
            "parse_after": None,
        }

        if raw is None:
            entry.update(
                {
                    "status_before": "failed",
                    "status_after": "failed",
                    "issues": ["missing_frontmatter"],
                    "parse_before": False,
                    "parse_after": False,
                }
            )
            report["summary"]["failed_before"] += 1
            report["summary"]["failed_after"] += 1
            report["summary"]["skipped"] += 1
            failures.append(rel)
            report["files"].append(entry)
            continue

        lines = raw.splitlines()
        clean_lines, pre_issues = normalize_raw_yaml(lines)
        pre_text = "\n".join(clean_lines)
        parse_before = False
        try:
            data = yaml.safe_load(pre_text)
            parse_before = isinstance(data, dict)
        except Exception:
            parse_before = False
        entry["parse_before"] = parse_before
        issues = list(pre_issues)
        if parse_before:
            entry["status_before"] = "passed"
            report["summary"]["passed_before"] += 1
        else:
            entry["status_before"] = "failed"
            entry["issues"].append("unparseable_frontmatter")
            report["summary"]["failed_before"] += 1
            failures.append(rel)
            report["files"].append(entry)
            continue

        repaired_text, repair_issues = repair_block(original, pre_text, tail or "\n---\n", body or "")
        repaired_text = repaired_text or original
        issues.extend(repair_issues)
        if not frontmatter_is_clean(clean_lines):
            issues.append("cleaned_document_markers")

        parse_after = False
        try:
            m2 = VERIFY_RE.match(repaired_text)
            if m2:
                data2 = yaml.safe_load(m2.group("yaml"))
                parse_after = isinstance(data2, dict)
        except Exception:
            parse_after = False
        entry["parse_after"] = parse_after

        if not parse_after:
            entry["status_after"] = "failed"
            entry["issues"].append("repair_failed")
            report["summary"]["failed_after"] += 1
            report["files"].append(entry)
            failures.append(rel)
            continue

        if repaired_text != original:
            path.write_text(repaired_text, encoding="utf-8")
            entry["changed"] = True
            entry["status_after"] = "passed"
            entry["issues"] = issues or ["repaired_frontmatter"]
            report["summary"]["changed"] += 1
            changed_files.append(rel)
        else:
            entry["changed"] = False
            entry["status_after"] = "passed"
            report["summary"]["unchanged"] += 1

        report["summary"]["passed_after"] += 1
        report["files"].append(entry)

    report["changed_files"] = changed_files
    report["failed_files"] = failures
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    verify = {
        "repo": str(REPO_ROOT),
        "target_glob": str(PROMPTS_DIR / "*.prompt.md"),
        "summary": {
            "verified_total": len(files),
            "parse_pass": sum(1 for e in report["files"] if e.get("parse_after")),
            "parse_fail": sum(1 for e in report["files"] if not e.get("parse_after")),
        },
        "failed_files": failures,
    }
    VERIFY_REPORT.write_text(
        json.dumps(verify, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Report written to {REPORT_PATH}")
    print(f"Verification report written to {VERIFY_REPORT}")
    print(
        f"total={report['summary']['total']} "
        f"passed_before={report['summary']['passed_before']} "
        f"failed_before={report['summary']['failed_before']} "
        f"changed={report['summary']['changed']} "
        f"unchanged={report['summary']['unchanged']} "
        f"passed_after={report['summary']['passed_after']} "
        f"failed_after={report['summary']['failed_after']} "
        f"skipped={report['summary']['skipped']}"
    )
    print("changed_files=" + json.dumps(changed_files, ensure_ascii=False))
    print("failures=" + json.dumps(failures, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())