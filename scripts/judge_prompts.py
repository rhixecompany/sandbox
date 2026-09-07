#!/usr/bin/env python3
"""
Prompts Judge — score .github/prompts/**/*.prompt.md AND enforce structural rules.

STRUCTURE:
.github/prompts/
├── <category>/
│   ├── <trigger>/
│   │   ├── <trigger>.prompt.md           (prompt file in trigger dir)
│   │   ├── templates/                    (templates in same trigger dir)
│   │   │   └── *.md
│   │   └── scripts/                      (scripts in same trigger dir)
│   │       └── *.py|*.sh|*.js|*.ts

RULES:
1. Each prompt has a `category:` frontmatter matching its grandparent directory
2. Prompt file lives in `.github/prompts/<category>/<trigger>/<trigger>.prompt.md`
3. Templates in `.github/prompts/<category>/<trigger>/templates/` (≥1 .md file)
4. Scripts in `.github/prompts/<category>/<trigger>/scripts/` (if referenced)
5. Trigger name (without leading `/`) matches the directory name exactly
6. All referenced skills, scripts, specs, plans must exist on disk
7. Pass plans-judge AND specs-judge cross-validation gates

Usage:
    python judge.py --prompts-dir .github/prompts [--output PATH] [--threshold N]
    python judge.py --prompts-dir .github/prompts --migration-plan
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

FM_FIELDS = ["description", "trigger", "toolsets", "category"]
REQUIRED_SECTIONS = ["## Goal", "## Context", "## Workflow", "## Verification"]
FENCE_PATTERN = re.compile(r"^(`{3,}|~{3,})", re.MULTILINE)

VALID_CATEGORIES = [
    "architecture", "audit", "brainstorming", "ci-cd", "creative", "data",
    "database", "debugging", "deployment", "development", "documentation",
    "finance", "github", "hooks", "mcp", "migration", "mlops", "monitoring",
    "operations", "payments", "planning", "productivity", "qa", "reference",
    "research", "security", "testing", "tooling", "web"
]


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def fence_balance(text: str) -> tuple[int, bool]:
    """Count code fences; return (count, balanced)."""
    fences = FENCE_PATTERN.findall(text)
    balanced = len(fences) % 2 == 0
    return len(fences), balanced


def extract_trigger(filepath: Path) -> str:
    """Extract trigger value from YAML frontmatter."""
    text = filepath.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        # Fallback: use directory name
        return filepath.parent.name
    end = text.find("\n---", 4)
    if end < 0:
        return filepath.parent.name
    for line in text[4:end].splitlines():
        line = line.strip()
        if line.startswith("trigger:"):
            val = line.split(":", 1)[1].strip().strip('"').strip("'")
            if val.startswith("/"):
                val = val[1:]
            return val
    return filepath.parent.name


def extract_references(text: str) -> dict:
    """Extract all asset references from prompt text."""
    refs = {
        "skills": [],
        "scripts": [],
        "specs": [],
        "plans": [],
        "templates": [],
    }

    # Skill references: skill:name or skills/name
    skill_matches = re.findall(r'(?:skill:|skills/)([\w\-/]+)', text)
    refs["skills"] = [s for s in skill_matches if s]

    # Script references: scripts/name
    script_matches = re.findall(r'scripts/([\w\-/]+\.?(?:py|sh|js|ts)?)', text)
    refs["scripts"] = [s for s in script_matches if s]

    # Spec references: .hermes/specs/name.md or ../specs/name.md
    spec_matches = re.findall(r'(?:\.hermes/specs/|\.\./specs/)([\w\-]+\.md)', text)
    refs["specs"] = [s for s in spec_matches if s]

    # Plan references: .hermes/plans/name.md or ../plans/name.md
    plan_matches = re.findall(r'(?:\.hermes/plans/|\.\./plans/)([\w\-]+\.md)', text)
    refs["plans"] = [p for p in plan_matches if p]

    # Template references: templates/name
    template_matches = re.findall(r'templates/([\w\-/]+)', text)
    refs["templates"] = [t for t in template_matches if t]

    return refs


def verify_asset_exists(asset_type: str, asset_path: str, category: str, trigger: str, pdir: Path) -> bool:
    """Verify an asset exists on disk."""
    # Compute the project root once: prompts live at <root>/.github/prompts/...
    project_root = pdir.parent.parent
    if asset_type == "skills":
        skill_dir = Path("C:/Users/Alexa/AppData/Local/hermes/skills") / asset_path
        return (skill_dir / "SKILL.md").exists()
    elif asset_type == "scripts":
        # Scripts in .github/prompts/<category>/<trigger>/scripts/
        script_path = pdir / category / trigger / "scripts" / asset_path
        if script_path.exists():
            return True
        # Also check project root scripts/
        project_scripts = project_root / "scripts" / asset_path
        return project_scripts.exists()
    elif asset_type == "specs":
        spec_path = project_root / ".hermes" / "specs" / asset_path
        return spec_path.exists()
    elif asset_type == "plans":
        plan_path = project_root / ".hermes" / "plans" / asset_path
        return plan_path.exists()
    elif asset_type == "templates":
        # Templates in .github/prompts/<category>/<trigger>/templates/
        template_path = pdir / category / trigger / "templates" / asset_path
        return template_path.exists()
    return False


def check_structure(prompt_paths: list[Path], pdir: Path) -> dict:
    """Check structure enforcement for all prompts."""
    prompt_info = []
    valid_count = 0

    for pp in sorted(prompt_paths):
        # Expected: .github/prompts/<category>/<trigger>/<trigger>.prompt.md
        relative = pp.relative_to(pdir)
        parts = relative.parts
        
        if len(parts) < 3:
            prompt_info.append({
                "prompt": str(pp),
                "trigger": "",
                "category": "",
                "structure_valid": False,
                "error": f"Wrong depth: {len(parts)} parts, need 3+ (category/trigger/file)",
            })
            continue
        
        category = parts[0]
        trigger_dir = parts[1]
        filename = parts[2]
        
        trigger = extract_trigger(pp)
        text = pp.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        fm_category = fm.get("category", "")
        
        # Validate structure
        structure_valid = True
        errors = []
        
        # 1. Category must be valid
        if category not in VALID_CATEGORIES:
            structure_valid = False
            errors.append(f"Invalid category: {category}")
        
        # 2. Trigger dir must match trigger field
        if trigger != trigger_dir:
            structure_valid = False
            errors.append(f"Trigger mismatch: dir={trigger_dir}, fm={trigger}")
        
        # 3. Filename must be <trigger>.prompt.md
        expected_filename = f"{trigger}.prompt.md"
        if filename != expected_filename:
            structure_valid = False
            errors.append(f"Filename mismatch: got={filename}, expected={expected_filename}")
        
        # 4. Frontmatter category must match directory category
        if fm_category != category:
            structure_valid = False
            errors.append(f"Category mismatch: fm={fm_category}, dir={category}")
        
        # 5. Check templates dir exists with .md files
        templates_dir = pdir / category / trigger / "templates"
        has_templates = templates_dir.is_dir() and len(list(templates_dir.glob("*.md"))) > 0
        if not has_templates:
            structure_valid = False
            errors.append(f"Missing templates dir or no .md files: {templates_dir}")
        
        # 6. Check scripts dir exists if scripts referenced
        scripts_dir = pdir / category / trigger / "scripts"
        refs = extract_references(text)
        has_script_refs = len(refs["scripts"]) > 0
        if has_script_refs and not scripts_dir.is_dir():
            structure_valid = False
            errors.append(f"Scripts referenced but no scripts dir: {scripts_dir}")
        
        info = {
            "prompt": str(pp),
            "trigger": trigger,
            "category": category,
            "trigger_dir": trigger_dir,
            "structure_valid": structure_valid,
            "errors": errors,
            "has_templates": has_templates,
            "has_scripts_dir": scripts_dir.is_dir(),
            "template_dir": str(templates_dir),
            "scripts_dir": str(scripts_dir),
        }
        prompt_info.append(info)
        if structure_valid:
            valid_count += 1

    return {
        "details": prompt_info,
        "total": len(prompt_info),
        "valid": valid_count,
        "invalid": len(prompt_info) - valid_count,
    }


def score_one(path: Path, pdir: Path, run_cross_judges: bool = True) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    fm = parse_frontmatter(text)

    # Extract structural info
    relative = path.relative_to(pdir)
    parts = relative.parts
    category = parts[0] if len(parts) >= 1 else ""
    trigger_dir = parts[1] if len(parts) >= 2 else ""
    trigger = extract_trigger(path)

    # Frontmatter (10 pts)
    fm_pts = sum(2.5 for f in FM_FIELDS if f in fm)
    fm_pts = min(int(fm_pts), 10)

    # Category & Structure Enforcement (20 pts) — HARD GATE
    structure_pts = 0
    if category in VALID_CATEGORIES:
        structure_pts += 5
    if trigger == trigger_dir:
        structure_pts += 5
    if path.name == f"{trigger}.prompt.md":
        structure_pts += 5
    fm_category = fm.get("category", "")
    if fm_category == category:
        structure_pts += 5
    
    # Check templates dir
    templates_dir = pdir / category / trigger / "templates"
    if templates_dir.is_dir() and len(list(templates_dir.glob("*.md"))) > 0:
        structure_pts += 5
    
    # Check scripts dir if needed
    refs = extract_references(text)
    has_script_refs = len(refs["scripts"]) > 0
    scripts_dir = pdir / category / trigger / "scripts"
    if not has_script_refs or (has_script_refs and scripts_dir.is_dir()):
        structure_pts += 5

    # Structure (10 pts) - required sections
    struct_pts = sum(2.5 for s in REQUIRED_SECTIONS if s in text)
    struct_pts = min(int(struct_pts), 10)

    # Content (10 pts)
    content_pts = 10
    placeholder = "[Add " in text or "TODO" in text or "[TBD]" in text
    if placeholder:
        content_pts -= 6
    if "## Goal" in text:
        goal = text.split("## Goal", 1)[1].split("## ", 1)[0]
        if len(goal.strip()) < 30:
            content_pts -= 4

    # Code Quality (8 pts): fence balance
    fence_count, balanced = fence_balance(text)
    if balanced and fence_count > 0:
        cq_pts = 8
    elif balanced:
        cq_pts = 4
    else:
        cq_pts = 1

    # Asset Co-location (15 pts) — templates/scripts in correct trigger dir
    colocation_pts = 15
    
    # Check templates refs point to templates/ (local to trigger dir)
    template_refs = re.findall(r'templates/([\w\-/]+)', text)
    for tref in template_refs:
        # Should be templates/... (relative to trigger dir)
        if tref.startswith("../") or tref.startswith(".."):
            colocation_pts -= 5
    
    # Check scripts refs point to scripts/ (local to trigger dir)
    script_refs = re.findall(r'scripts/([\w\-/]+\.?(?:py|sh|js|ts)?)', text)
    for sref in script_refs:
        if sref.startswith("../") or sref.startswith(".."):
            colocation_pts -= 5
    
    colocation_pts = max(colocation_pts, 0)

    # Asset Verification (15 pts) — all referenced assets exist
    verification_pts = 15
    for asset_type, assets in refs.items():
        for asset in assets:
            if not verify_asset_exists(asset_type, asset, category, trigger, pdir):
                verification_pts -= 3
    verification_pts = max(verification_pts, 0)

    # Cross-judge Gates (15 pts) — run plans-judge and specs-judge
    cross_judge_pts = 15
    if run_cross_judges:
        # Compute the project root: prompts live at <root>/.github/prompts/...
        # so the root is two parents up from pdir.
        project_root = pdir.parent.parent
        plans_dir = str(project_root / ".hermes" / "plans")
        specs_dir = str(project_root / ".hermes" / "specs")
        try:
            result = subprocess.run([
                sys.executable,
                "C:/Users/Alexa/AppData/Local/hermes/skills/qa/plans-judge/scripts/judge.py",
                "--plans-dir", plans_dir,
                "--specs-dir", specs_dir,
                "--threshold", "70"
            ], capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                cross_judge_pts -= 8
        except Exception:
            cross_judge_pts -= 8

        try:
            result = subprocess.run([
                sys.executable,
                "C:/Users/Alexa/AppData/Local/hermes/skills/qa/specs-judge/scripts/judge.py",
                "--specs-dir", specs_dir,
                "--plans-dir", plans_dir,
                "--threshold", "70"
            ], capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                cross_judge_pts -= 7
        except Exception:
            cross_judge_pts -= 7

    cross_judge_pts = max(cross_judge_pts, 0)

    # DRY (2 pts)
    phase_headings = re.findall(r"^## Phase \d+:", text, re.MULTILINE)
    dry_pts = 2
    if len(phase_headings) > 6:
        dry_pts = 0

    total = fm_pts + structure_pts + struct_pts + content_pts + cq_pts + colocation_pts + verification_pts + cross_judge_pts + dry_pts
    
    # HARD FAIL: If structure < 25, cap at 50
    if structure_pts < 25:
        total = min(total, 50)
    # HARD FAIL: If templates missing, cap at 50
    if not (templates_dir.is_dir() and len(list(templates_dir.glob("*.md"))) > 0):
        total = min(total, 50)

    return {
        "file": str(path),
        "score": total,
        "rating": "PASS" if total >= 70 else "WARN" if total >= 50 else "FAIL",
        "dims": {
            "frontmatter": fm_pts,
            "structure_enforcement": structure_pts,
            "structure_sections": struct_pts,
            "content": content_pts,
            "code_quality": cq_pts,
            "asset_colocation": colocation_pts,
            "asset_verification": verification_pts,
            "cross_judge_gates": cross_judge_pts,
            "dry": dry_pts,
        },
        "fm_fields": sorted(fm.keys()),
        "fences": fence_count,
        "fences_balanced": balanced,
        "phases": len(phase_headings),
        "has_placeholder": placeholder,
        "category": category,
        "trigger": trigger,
        "trigger_dir": trigger_dir,
        "structure_valid": structure_pts >= 25,
        "refs": refs,
    }


def generate_migration_plan(structure_check: dict, pdir: Path) -> str:
    """Generate an actionable migration plan."""
    lines = []
    lines.append("# Structure Migration Plan")
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"Prompts dir: `{pdir}`")
    lines.append("")
    lines.append(f"**Summary:** {structure_check['valid']}/{structure_check['total']} valid, "
                 f"{structure_check['invalid']} invalid")
    lines.append("")

    if structure_check["invalid"] > 0:
        lines.append("## 1. Fix Invalid Structures")
        lines.append("")
        for info in structure_check["details"]:
            if not info["structure_valid"]:
                lines.append(f"### `{info['prompt']}`")
                lines.append("")
                lines.append(f"Category: `{info['category']}` | Trigger dir: `{info['trigger_dir']}` | Trigger fm: `{info['trigger']}`")
                lines.append("")
                for err in info["errors"]:
                    lines.append(f"- **Error:** {err}")
                lines.append("")
                lines.append("**Required structure:**")
                lines.append(f"```")
                lines.append(f"{pdir}/{info['category']}/{info['trigger']}/")
                lines.append(f"├── {info['trigger']}.prompt.md")
                lines.append(f"├── templates/")
                lines.append(f"│   └── *.md")
                lines.append(f"└── scripts/")
                lines.append(f"    └── *.py")
                lines.append(f"```")
                lines.append("")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Prompts Judge")
    ap.add_argument("--prompts-dir", default=".github/prompts")
    ap.add_argument("--output", default="judge_results/prompts_audit")
    ap.add_argument("--threshold", type=int, default=70)
    ap.add_argument("--migration-plan", action="store_true",
                    help="Generate migration plan for structure issues")
    ap.add_argument("--no-cross-judges", action="store_true",
                    help="Skip running plans-judge and specs-judge cross-validation")
    args = ap.parse_args()

    pdir = Path(args.prompts_dir)
    if not pdir.is_dir():
        print(f"ERR: prompts dir not found: {pdir}", file=sys.stderr)
        return 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    # Collect prompt files in category/trigger/ structure
    prompt_paths = list(pdir.rglob("*.prompt.md"))

    if args.migration_plan or not prompt_paths:
        structure = check_structure(prompt_paths, pdir)
        
        if args.migration_plan:
            plan = generate_migration_plan(structure, pdir)
            plan_path = out.with_suffix(".migration.md")
            plan_path.write_text(plan + "\n", encoding="utf-8")
            print(f"Migration plan: {plan_path}")
            print(f"  Valid: {structure['valid']}/{structure['total']}")
            print(f"  Invalid: {structure['invalid']}")
            return 0 if structure['invalid'] == 0 else 1

    run_cross = not args.no_cross_judges
    results = []
    for pp in prompt_paths:
        r = score_one(pp, pdir, run_cross_judges=run_cross)
        cat = r.get("category", "")
        trig = r.get("trigger", "")
        templates_dir = pdir / cat / trig / "templates" if cat and trig else None
        r["template_dir"] = str(templates_dir) if templates_dir else ""
        r["has_template_dir"] = templates_dir.is_dir() if templates_dir else False
        r["template_file_count"] = len(list(templates_dir.glob("*.md"))) if templates_dir and templates_dir.is_dir() else 0
        if not r["has_template_dir"] or r["template_file_count"] == 0:
            r["score"] = min(r["score"], 50)
            r["rating"] = "FAIL"
            r["template_missing"] = True
        results.append(r)

    avg = sum(r["score"] for r in results) / max(len(results), 1)
    passed = sum(1 for r in results if r["score"] >= args.threshold)
    unbalanced = sum(1 for r in results if not r.get("fences_balanced", True))

    structure = check_structure(prompt_paths, pdir)

    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "dir": str(pdir),
        "threshold": args.threshold,
        "count": len(results),
        "avg": round(avg, 1),
        "passed": passed,
        "unbalanced_fences": unbalanced,
        "structure_check": structure,
        "results": results,
    }

    (out.with_suffix(".json")).write_text(json.dumps(report, indent=2))

    md = [
        f"# Prompts Audit — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Dir: `{pdir}` | Threshold: {args.threshold}",
        f"Count: {len(results)} | Avg: {avg:.1f} | Passed: {passed}",
        f"Unbalanced-fence files: {unbalanced}",
        f"Structure: {structure['valid']}/{structure['total']} valid",
    ]

    md.append("")
    md.append("| File | Score | Rating | FM | Struct | Sections | Content | CQ | Coloc | Verify | Cross | DRY |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|---|")

    for r in results:
        d = r["dims"]
        tm_flag = " ⚠TMPL" if r.get("template_missing") else ""
        struct_flag = " ⚠STRUCT" if not r.get("structure_valid", True) else ""
        md.append(
            f"| `{Path(r['file']).name}`{tm_flag}{struct_flag} | {r['score']} | {r['rating']} | "
            f"{d['frontmatter']} | {d['structure_enforcement']} | {d['structure_sections']} | {d['content']} | "
            f"{d['code_quality']} | {d['asset_colocation']} | {d['asset_verification']} | "
            f"{d['cross_judge_gates']} | {d['dry']} |"
        )

    (out.with_suffix(".md")).write_text("\n".join(md) + "\n")

    struct_msg = f" | Structure: {structure['valid']}/{structure['total']} valid"
    print(f"Prompts Judge: {len(results)} files, avg {avg:.1f}, passed {passed}/{len(results)}{struct_msg}")
    print(f"Report: {out.with_suffix('.md')}")

    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())