#!/usr/bin/env python3
"""
Phase 1: Frontmatter Standardisation Script
Reads all 226 .prompt.md files, preserves existing good frontmatter fields,
adds missing required fields, adds 4-agent metadata, fixes duplicate frontmatter,
and preserves body content exactly.
"""

import yaml
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")
DRY_RUN = "--dry-run" in sys.argv

DEFAULT_TOOLSETS = ["file", "terminal"]
DEFAULT_FORMATTER = "default"
DEFAULT_HERMES_PROFILE = "default"
DEFAULT_TAGS = ["agent-type:hermes"]

DOMAIN_PROFILE_MAP = {
    "code": "code-architect", "debug": "code-architect", "refactor": "code-architect",
    "test": "code-architect", "typescript": "code-architect", "python": "code-architect",
    "rust": "code-architect", "go": "code-architect", "java": "code-architect",
    "csharp": "code-architect", "setup": "exec-assistant", "config": "exec-assistant",
    "deploy": "exec-assistant", "docker": "exec-assistant", "ci": "exec-assistant",
    "research": "research-analyst", "docs": "creative-director",
    "documentation": "creative-director", "readme": "creative-director",
    "design": "creative-director", "plan": "exec-assistant", "brainstorm": "creative-director",
    "security": "code-architect", "prompt": "exec-assistant", "skill": "exec-assistant",
    "agent": "exec-assistant", "workflow": "exec-assistant", "automation": "exec-assistant",
    "hermes": "exec-assistant", "copilot": "exec-assistant", "opencode": "exec-assistant",
    "codex": "exec-assistant", "mcp": "code-architect", "api": "code-architect",
    "web": "creative-director", "frontend": "creative-director", "nextjs": "code-architect",
    "react": "code-architect", "django": "code-architect", "database": "code-architect",
    "sql": "code-architect", "performance": "code-architect", "audit": "research-analyst",
    "review": "code-architect", "generate": "creative-director", "create": "creative-director",
    "write": "creative-director", "blueprint": "creative-director",
    "architecture": "code-architect", "template": "exec-assistant", "task": "exec-assistant",
    "sync": "exec-assistant", "migration": "exec-assistant", "consolidat": "exec-assistant",
    "index": "exec-assistant", "list": "exec-assistant",
}


def determine_profile(name, tags, title, description):
    text = (name + " " + " ".join(tags) + " " + title + " " + description).lower()
    for key, profile in DOMAIN_PROFILE_MAP.items():
        if key in text:
            return profile
    return DEFAULT_HERMES_PROFILE


def determine_context_size(body_len):
    if body_len > 5000:
        return "large"
    elif body_len > 2000:
        return "medium"
    return "small"


def determine_opencode_help(trigger, description):
    desc = description.strip().split("\n")[0].strip()
    if len(desc) > 80:
        desc = desc[:77] + "..."
    return desc


def parse_frontmatter(text):
    """Parse YAML frontmatter from a prompt file.
    Handles: standard frontmatter, duplicate Copilot blocks (3+ --- markers),
    and BOM-prefixed files. Uses line-based detection for robustness.
    Returns (frontmatter_dict, body_text).
    """
    if text.startswith("\ufeff"):
        text = text[1:]
    lines = text.splitlines()

    # Find ALL lines that are exactly "---" (after strip), skipping indented ones inside YAML blocks
    # A line is a frontmatter delimiter if it's "---" with no leading whitespace
    dash_indices = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "---":
            if line == line.lstrip() and not line.startswith(" "):
                # Only count "---" at column 0 (not indented inside YAML)
                dash_indices.append(i)

    if len(dash_indices) < 1:
        return None, text

    # First pair: open at dash_indices[0]
    fm_start = dash_indices[0]

    if len(dash_indices) >= 2:
        # Standard case: closing --- found
        fm_end = dash_indices[1]
    else:
        # Open-ended frontmatter (no closing ---):
        # Find where frontmatter ends — first markdown heading
        fm_end = len(lines)
        for i in range(fm_start + 1, len(lines)):
            stripped = lines[i].strip()
            if stripped.startswith("## ") or stripped.startswith("# "):
                fm_end = i
                break
            if stripped == "" and i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].strip().startswith("#"):
                fm_end = i
                break

    fm_text = "\n".join(lines[fm_start + 1:fm_end])
    # If there's no closing ---, body starts from fm_end (which is after the content)
    # Otherwise body starts after the closing ---
    body = "\n".join(lines[fm_end:])

    try:
        fm = yaml.safe_load(fm_text)
        if isinstance(fm, dict) and fm:
            return fm, body
        return None, text
    except yaml.YAMLError:
        return None, text


def build_canonical_frontmatter(existing_fm, name, body):
    def first_str(val):
        if val is None:
            return None
        if isinstance(val, str) and val.strip():
            return val
        if isinstance(val, list) and val:
            return str(val[0])
        return None

    resolved_name = first_str(existing_fm.get("name") if existing_fm else None) or name

    existing_trigger = existing_fm.get("trigger") if existing_fm else None
    if existing_trigger and isinstance(existing_trigger, str) and existing_trigger.startswith("/"):
        resolved_trigger = existing_trigger
    else:
        resolved_trigger = f"/{resolved_name}"

    resolved_title = first_str(existing_fm.get("title") if existing_fm else None) or resolved_name.replace("-", " ").replace("_", " ").title()

    existing_desc = existing_fm.get("description") if existing_fm else None
    if existing_desc:
        if isinstance(existing_desc, str) and existing_desc.strip():
            resolved_description = existing_desc.strip()
        elif isinstance(existing_desc, list):
            resolved_description = " ".join(str(d) for d in existing_desc if d).strip()
        else:
            resolved_description = f"Auto-generated prompt for {resolved_trigger}"
    else:
        resolved_description = f"Auto-generated prompt for {resolved_trigger}"

    resolved_version = first_str(existing_fm.get("version") if existing_fm else None) or "1.0.0"
    resolved_license = first_str(existing_fm.get("license") if existing_fm else None) or "MIT"
    resolved_author = first_str(existing_fm.get("author") if existing_fm else None) or "Hermes Agent"

    existing_toolsets = existing_fm.get("toolsets") if existing_fm else None
    if existing_toolsets and isinstance(existing_toolsets, list) and len(existing_toolsets) > 0:
        resolved_toolsets = [str(t) for t in existing_toolsets if t]
    else:
        resolved_toolsets = DEFAULT_TOOLSETS.copy()

    existing_skills = existing_fm.get("skills") if existing_fm else None
    if existing_skills and isinstance(existing_skills, list) and len(existing_skills) > 0:
        resolved_skills = [str(s) for s in existing_skills if s]
    else:
        resolved_skills = []
    seen = set()
    resolved_skills = [s for s in resolved_skills if not (s in seen or seen.add(s))]

    resolved_formatter = first_str(existing_fm.get("formatter") if existing_fm else None) or DEFAULT_FORMATTER

    existing_plan = existing_fm.get("plan") if existing_fm else None
    resolved_plan = first_str(existing_plan) if existing_plan else None

    existing_deps = existing_fm.get("dependencies") if existing_fm else None
    if existing_deps and isinstance(existing_deps, list) and len(existing_deps) > 0:
        resolved_dependencies = [str(d) for d in existing_deps if d]
    else:
        resolved_dependencies = []

    existing_tags = existing_fm.get("tags") if existing_fm else None
    if existing_tags and isinstance(existing_tags, list) and len(existing_tags) > 0:
        resolved_tags = [str(t) for t in existing_tags if t]
    else:
        resolved_tags = DEFAULT_TAGS.copy()
    seen_tags = set()
    resolved_tags = [t for t in resolved_tags if not (t in seen_tags or seen_tags.add(t))]
    if not any(t.startswith("agent-type:") for t in resolved_tags):
        resolved_tags.insert(0, "agent-type:hermes")

    existing_scripts = existing_fm.get("scripts") if existing_fm else None
    if existing_scripts and isinstance(existing_scripts, list):
        resolved_scripts = [str(s) for s in existing_scripts if s]
    else:
        resolved_scripts = []

    existing_metadata = existing_fm.get("metadata") if existing_fm else None
    preserved_meta = None
    if existing_metadata and isinstance(existing_metadata, dict):
        agents = ["hermes", "copilot", "opencode", "codex"]
        if all(existing_metadata.get(a) is not None for a in agents):
            preserved_meta = existing_metadata

    body_len = len(body)
    profile = determine_profile(resolved_name, resolved_tags, resolved_title, resolved_description)
    context_size = determine_context_size(body_len)

    new_metadata = {
        "hermes": {"profile": profile, "mcp_servers": [], "context_size": context_size},
        "copilot": {"context_size": context_size, "extensions": [], "keybinding": None},
        "opencode": {
            "command": f"opencode {resolved_trigger}",
            "flags": {},
            "help": determine_opencode_help(resolved_trigger, resolved_description),
        },
        "codex": {
            "model_override": None, "system_prompt_id": None,
            "temperature": None, "max_tokens": None,
        },
    }

    if preserved_meta:
        for agent in ["hermes", "copilot", "opencode", "codex"]:
            if agent in preserved_meta and isinstance(preserved_meta[agent], dict):
                new_metadata[agent].update(preserved_meta[agent])

    if not isinstance(new_metadata["hermes"].get("mcp_servers"), list):
        new_metadata["hermes"]["mcp_servers"] = []

    canonical = {
        "name": resolved_name,
        "title": resolved_title,
        "description": resolved_description,
        "version": resolved_version,
        "license": resolved_license,
        "author": resolved_author,
        "trigger": resolved_trigger,
        "toolsets": resolved_toolsets,
        "skills": resolved_skills,
        "dependencies": resolved_dependencies,
        "formatter": resolved_formatter,
        "plan": resolved_plan,
        "metadata": new_metadata,
        "tags": resolved_tags,
        "scripts": resolved_scripts,
    }
    return canonical


def frontmatter_to_yaml(fm):
    """
    Serialize frontmatter to clean YAML block style.
    Uses PyYAML dump with custom None representer.
    Filters out None values for cleaner output.
    """
    # Build a clean dict without None values (except where needed)
    clean = {}
    for k, v in fm.items():
        if v is None:
            continue  # Skip None values for cleaner YAML
        if isinstance(v, dict):
            # Filter None values from nested dicts
            filtered = {kk: vv for kk, vv in v.items() if vv is not None}
            if filtered:
                clean[k] = filtered
            elif k == "metadata":
                # Keep metadata even if empty (it's required)
                clean[k] = v
        else:
            clean[k] = v

    # Add back plan: null explicitly if it was None (not in clean dict)
    # But we skip None values, so plan won't appear if null — that's fine

    # Custom representer for None
    def represent_none(dumper, value):
        return dumper.represent_scalar('tag:yaml.org,2002:null', 'null')

    Dumper = yaml.Dumper

    class CustomDumper(Dumper):
        pass

    CustomDumper.add_representer(type(None), represent_none)

    output = yaml.dump(
        clean,
        Dumper=CustomDumper,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        width=100,
    )
    # Ensure the output starts with "---\n" (yaml.dump doesn't add document markers)
    if not output.startswith("---"):
        output = "---\n" + output
    else:
        # yaml.dump might produce "---\n..." already in some versions
        pass
    return output


def process_file(filepath):
    text = filepath.read_text(encoding='utf-8', errors='replace')
    name = filepath.stem

    existing_fm, body = parse_frontmatter(text)

    report = {
        "file": str(filepath),
        "name": name,
        "had_frontmatter": existing_fm is not None,
        "had_duplicate_fm": False,
        "changes": [],
    }

    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        dashes = [i for i, l in enumerate(lines) if l.strip() == "---"]
        if len(dashes) > 2:
            report["had_duplicate_fm"] = True
            report["changes"].append("Removed duplicate frontmatter")

    canonical = build_canonical_frontmatter(existing_fm, name, body)

    if existing_fm is None:
        report["changes"].append("Added frontmatter")
    else:
        for key in ["title", "description", "version", "license", "author",
                     "trigger", "toolsets", "skills", "dependencies",
                     "formatter", "plan", "tags", "scripts", "metadata"]:
            old_val = existing_fm.get(key)
            new_val = canonical.get(key)
            if old_val != new_val:
                report["changes"].append(f"Updated {key}")

    new_fm_yaml = frontmatter_to_yaml(canonical)
    new_content = new_fm_yaml.rstrip() + "\n" + body if body else new_fm_yaml.rstrip() + "\n"

    if DRY_RUN:
        report["dry_run"] = True
        return report

    filepath.write_text(new_content, encoding='utf-8')
    report["written"] = True
    return report


def main():
    print(f"=== Phase 1: Frontmatter Standardisation ===")
    print(f"Target: {PROMPTS_DIR}")
    print(f"Dry run: {DRY_RUN}")
    print()

    prompt_files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    print(f"Found {len(prompt_files)} prompt files\n")

    reports = []
    for pf in prompt_files:
        report = process_file(pf)
        reports.append(report)
        status = "✓" if report.get("written") or report.get("dry_run") else "✗"
        changes = ", ".join(report["changes"]) if report["changes"] else "no changes"
        dup = " [DUP]" if report.get("had_duplicate_fm") else ""
        print(f"{status} {pf.name}: {changes}{dup}")

    print(f"\n=== SUMMARY ===")
    print(f"Total: {len(reports)}")
    print(f"Had frontmatter: {sum(1 for r in reports if r['had_frontmatter'])}")
    print(f"Added frontmatter: {sum(1 for r in reports if not r['had_frontmatter'])}")
    print(f"Had duplicate FM: {sum(1 for r in reports if r.get('had_duplicate_fm'))}")
    print(f"Changed: {sum(1 for r in reports if r['changes'])}")
    if not DRY_RUN:
        print("\nAll files written.")
    else:
        print("\nDRY RUN — no files modified.")


if __name__ == "__main__":
    main()
