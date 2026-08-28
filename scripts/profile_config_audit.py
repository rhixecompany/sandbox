#!/usr/bin/env python3
"""
profile_config_audit.py — Audit SOUL.md/USER.md/MEMORY.md/.hermes.md/AGENTS.md/CLAUDE.md/.cursorrules
across all Hermes profiles and the repo root.

Non-destructive: reports drift/corruption, writes JSON report, exits 0.
Does NOT modify any files.

Usage:
    python scripts/profile_config_audit.py [--repo-root /path] [--profiles-dir /path]
"""
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

DEFAULT_REPO = Path(__file__).resolve().parent.parent
DEFAULT_PROFILES = Path.home() / "AppData/Local/hermes/profiles"

# Config files to audit
IDENTITY_FILES = ["SOUL.md", "USER.md", "MEMORY.md"]
CONTEXT_FILES = [".hermes.md", "AGENTS.md", "CLAUDE.md", ".cursorrules"]

# YAML frontmatter corruption patterns
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
COLLAPSED_ARRAY_RE = re.compile(r"^tags: - (.+)$", re.MULTILINE)


def find_profiles(profiles_dir: Path) -> list[str]:
    """Return list of profile directory names."""
    if not profiles_dir.exists():
        return []
    return sorted([d.name for d in profiles_dir.iterdir() if d.is_dir()])


def check_yaml_frontmatter(path: Path) -> dict:
    """Validate YAML frontmatter structure without importing yaml (stdlib only)."""
    issues = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"path": str(path), "issues": [f"read_error: {e}"], "frontmatter_present": False}

    frontmatter_present = text.startswith("---")
    if frontmatter_present:
        match = FRONTMATTER_RE.match(text)
        if not match:
            issues.append("frontmatter_unclosed_or_malformed")
        else:
            fm = match.group(1)
            # Check for collapsed multi-line arrays (common corruption)
            for line in fm.split("\n"):
                if COLLAPSED_ARRAY_RE.match(line):
                    issues.append(f"collapsed_array_detected: {line.strip()}")
            # Check for duplicate keys (simple heuristic)
            keys = [l.split(":", 1)[0] for l in fm.split("\n") if ":" in l and not l.startswith(" ")]
            if len(keys) != len(set(keys)):
                issues.append("duplicate_keys_in_frontmatter")
            # Check metadata.hermes.tags array format
            if "metadata:" in fm and "tags:" in fm:
                tags_line_idx = None
                lines = fm.split("\n")
                for i, line in enumerate(lines):
                    if "tags:" in line and "hermes" not in line.split(":")[0]:
                        tags_line_idx = i
                        break
                if tags_line_idx is not None:
                    next_line = lines[tags_line_idx + 1] if tags_line_idx + 1 < len(lines) else ""
                    if not next_line.strip().startswith("- "):
                        # tags on same line as key = collapsed
                        if not COLLAPSED_ARRAY_RE.match(lines[tags_line_idx]):
                            pass  # Could be inline list, acceptable

    return {
        "path": str(path),
        "frontmatter_present": frontmatter_present,
        "issues": issues,
        "size_bytes": path.stat().st_size if path.exists() else 0,
    }


def check_file_exists(path: Path) -> dict:
    """Check if a file exists and report basic stats."""
    exists = path.exists()
    result = {
        "path": str(path),
        "exists": exists,
        "size_bytes": path.stat().st_size if exists else 0,
        "issues": [] if exists else ["file_missing"],
    }
    return result


def audit_profile(profile_dir: Path, profile_name: str) -> dict:
    """Audit a single profile directory."""
    profile_result = {
        "name": profile_name,
        "path": str(profile_dir),
        "identity_files": {},
        "context_files": {},
        "issues": [],
    }

    # Check identity files
    for fname in IDENTITY_FILES:
        fpath = profile_dir / fname
        info = check_file_exists(fpath)
        if fpath.exists():
            yaml_info = check_yaml_frontmatter(fpath)
            info.update({k: v for k, v in yaml_info.items() if k not in ("path",)})
        profile_result["identity_files"][fname] = info
        if info["issues"]:
            profile_result["issues"].extend(f"{fname}: {i}" for i in info["issues"])

    # Check context files
    for fname in CONTEXT_FILES:
        fpath = profile_dir / fname
        info = check_file_exists(fpath)
        if fpath.exists():
            yaml_info = check_yaml_frontmatter(fpath)
            info.update({k: v for k, v in yaml_info.items() if k not in ("path",)})
        profile_result["context_files"][fname] = info
        if info["issues"]:
            profile_result["issues"].extend(f"{fname}: {i}" for i in info["issues"])

    return profile_result


def audit_repo_root(repo_dir: Path) -> dict:
    """Audit repo root context files."""
    repo_result = {
        "name": "repo-root",
        "path": str(repo_dir),
        "context_files": {},
        "identity_files": {},
        "issues": [],
    }

    for fname in CONTEXT_FILES:
        fpath = repo_dir / fname
        info = check_file_exists(fpath)
        if fpath.exists():
            yaml_info = check_yaml_frontmatter(fpath)
            info.update({k: v for k, v in yaml_info.items() if k not in ("path",)})
        repo_result["context_files"][fname] = info
        if info["issues"]:
            repo_result["issues"].extend(f"{fname}: {i}" for i in info["issues"])

    return repo_result


def detect_cross_profile_drift(profiles: list[dict]) -> list[str]:
    """Detect drift in provider/model routing across profiles."""
    issues = []
    # Check which profiles have model routing info in USER.md or MEMORY.md
    routing_patterns = []
    for p in profiles:
        for fname in ["USER.md", "MEMORY.md"]:
            info = p["identity_files"].get(fname, {})
            if info.get("exists"):
                try:
                    text = (Path(p["path"]) / fname).read_text(encoding="utf-8", errors="replace")
                    # Look for routing table or provider mappings
                    if "routing" in text.lower() or "provider" in text.lower():
                        routing_patterns.append((p["name"], fname, len(text)))
                except Exception:
                    pass

    # Simple drift check: if some profiles have routing and others don't
    has_routing = {name for name, _, _ in routing_patterns}
    all_profiles = {p["name"] for p in profiles}
    missing_routing = all_profiles - has_routing
    if missing_routing and has_routing:
        issues.append(f"Routing info present in {sorted(has_routing)} but missing in {sorted(missing_routing)}")

    return issues


def main():
    repo_root = DEFAULT_REPO
    profiles_dir = DEFAULT_PROFILES

    report = {
        "audit_timestamp": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(repo_root),
        "profiles_dir": str(profiles_dir),
        "profiles": [],
        "repo_root_audit": {},
        "cross_profile_drift": [],
        "summary": {
            "total_profiles": 0,
            "files_missing": 0,
            "frontmatter_issues": 0,
            "total_issues": 0,
        },
    }

    # Audit repo root
    repo_audit = audit_repo_root(repo_root)
    report["repo_root_audit"] = repo_audit
    report["summary"]["files_missing"] += len(repo_audit["issues"])
    report["summary"]["total_issues"] += len(repo_audit["issues"])

    # Audit each profile
    profile_names = find_profiles(profiles_dir)
    report["summary"]["total_profiles"] = len(profile_names)

    for pname in profile_names:
        pdir = profiles_dir / pname
        audit = audit_profile(pdir, pname)
        report["profiles"].append(audit)

        missing = sum(1 for f in audit["identity_files"].values() if not f["exists"])
        report["summary"]["files_missing"] += missing
        report["summary"]["total_issues"] += len(audit["issues"])
        fm_issues = sum(1 for f in list(audit["identity_files"].values()) + list(audit["context_files"].values())
                        if f.get("frontmatter_present") and f.get("issues"))
        report["summary"]["frontmatter_issues"] += fm_issues

    # Cross-profile drift detection
    report["cross_profile_drift"] = detect_cross_profile_drift(report["profiles"])

    # Write report
    report_dir = repo_root / ".hermes" / "plans" / "2026-08-28-unified-platform-remediation"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "profile-config-audit.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Summary to stdout
    print(f"Profile config audit complete.")
    print(f"  Profiles scanned: {report['summary']['total_profiles']}")
    print(f"  Files missing:    {report['summary']['files_missing']}")
    print(f"  Frontmatter issues: {report['summary']['frontmatter_issues']}")
    print(f"  Total issues:     {report['summary']['total_issues']}")
    print(f"  Drift issues:     {len(report['cross_profile_drift'])}")
    print(f"  Report written:   {report_path}")

    # Print issues per profile
    for p in report["profiles"]:
        if p["issues"]:
            print(f"\n  [{p['name']}] issues:")
            for issue in p["issues"]:
                print(f"    - {issue}")

    if report["cross_profile_drift"]:
        print("\n  Cross-profile drift:")
        for issue in report["cross_profile_drift"]:
            print(f"    - {issue}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
