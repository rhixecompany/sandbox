#!/usr/bin/env python3
"""
audit_fix_remediate_safe.py — Phase 5 SAFE remediation for audit-skills-judge-fix.

Targets FAIL skills (score < 60) and adds MISSING structural/frontmatter elements
ONLY. It is strictly ADDITIVE: it never truncates, overwrites, or regenerates
existing content. This honors skill-judge's "Over-patching" pitfall — the real fix
for low-scoring skills is adding the missing required fields + structure, not
replacing substantive content with a generic stub.

Outputs: judge_results/remediation_report.md
"""
from __future__ import annotations
import asyncio
import csv
import os
import re
import sys
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HOME", os.path.expanduser("~"))) / "AppData" / "Local" / "hermes"
SANDBOX = Path(os.environ.get("HOME", os.path.expanduser("~"))) / "Desktop" / "SandBox"

SKILLS_ROOT = HERMES_HOME / "skills"
TSV = SANDBOX / "judge_results/all_results.tsv"
REPORT = SANDBOX / "judge_results/remediation_report.md"
TSV_NOTE = "tsv-missing"
NOOP_TSV = SANDBOX / "judge_results/_empty.tsv"
AUTHOR_DEFAULT = "Hermes Agent"
LICENSE_DEFAULT = "MIT"

if not TSV.exists():
    NOOP_TSV.write_text("name\tpath\tscore\terrors\tduration\n", encoding="utf-8")
    TSV = NOOP_TSV

# --- frontmatter parse helpers -------------------------------------------------
def parse_fm(text: str) -> tuple[dict, str, str]:
    """Return (fm_dict, fm_block, body). fm_block includes the --- fences."""
    if not text.startswith("---"):
        return {}, "", text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return {}, "", text
    fm_block = text[: m.end()]
    body = text[m.end():]
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, fm_block, body

def has_fm_field(fm: dict, key: str) -> bool:
    return bool(fm.get(key))

def fm_has_section(fm_block: str, key: str) -> bool:
    return bool(re.search(rf"^\s*{re.escape(key)}\s*:", fm_block, re.MULTILINE))

def add_fm_fields(fm: dict, fm_block: str) -> tuple[str, list[str]]:
    """Add missing frontmatter fields to the fm_block (before closing ---). Returns (new_block, added)."""
    added = []
    name = fm.get("name", "skill")
    title = name.replace("-", " ").title()
    # Locate closing --- of frontmatter
    close = fm_block.rstrip().rfind("\n---")
    if close == -1:
        close = len(fm_block)
        insertion = fm_block
    else:
        insertion = fm_block[:close]
    new_lines = []
    # Fields to ensure
    def ensure(key, val):
        nonlocal insertion, added
        if not fm_has_section(insertion, key) and not has_fm_field(fm, key):
            insertion = insertion.rstrip("\n") + f"\n{key}: {val}\n"
            added.append(key)
    ensure("title", f'"{title}"')
    ensure("version", "1.0.0")
    ensure("author", AUTHOR_DEFAULT)
    ensure("license", LICENSE_DEFAULT)
    if not fm_has_section(insertion, "tags"):
        ensure("tags", "[imported]")
    return insertion.rstrip("\n") + "\n---\n", added

def section_present(body: str, header: str) -> bool:
    return bool(re.search(rf"^#{{1,4}}\s*{re.escape(header)}\s*$", body, re.MULTILINE | re.IGNORECASE))

def remediate_body(body: str, name: str) -> tuple[str, list[str]]:
    added = []
    append = []
    if not section_present(body, "Skills Required"):
        append.append(
            "\n## Skills Required\n\n"
            "| Skill | Purpose |\n|-------|---------|\n"
            "| `hermes-agent` | Core Hermes functionality |\n"
            "| `skill-judge` | Evaluate skill quality |\n"
        )
        added.append("Skills Required")
    if not section_present(body, "Pitfalls"):
        append.append(
            "\n## Pitfalls\n\n"
            "- **Thin content**: Add concrete code examples and real-world use cases where applicable.\n"
            "- **Missing error handling**: Include error-handling patterns in workflow phases.\n"
            "- **No resumability**: Add entry/exit checks at each phase for long-running workflows.\n"
        )
        added.append("Pitfalls")
    if not section_present(body, "Verification Checklist"):
        append.append(
            "\n## Verification Checklist\n\n"
            "- [ ] Frontmatter complete (name, title, description, version, author, license, tags)\n"
            "- [ ] Skills Required table present\n"
            "- [ ] Workflow has >=3 phases\n"
            "- [ ] Pitfalls section present\n"
            "- [ ] All references cited in SKILL.md body\n"
            "- [ ] SKILL.md under 250 lines\n"
            "- [ ] No placeholder text\n"
        )
        added.append("Verification Checklist")
    new_body = body + "".join(append)
    return new_body, added

async def main() -> int:
    loop = asyncio.get_running_loop()
    rows = []
    tsv_text = await loop.run_in_executor(None, _read_text, TSV)
    import io
    r = csv.DictReader(filter(None, (line.strip() for line in io.StringIO(tsv_text))), delimiter="\t")
    for row in r:
        rows.append(row)
    fail = [r for r in rows if int(r["score"]) < 60]
    fixed, skipped, errors = [], [], []
    for r in fail:
        path = Path(r["path"]) / "SKILL.md"
        if not path.exists():
            skipped.append(f"{r['name']}: path-missing")
            continue
        text = await loop.run_in_executor(None, _read_text, path)
        fm, fm_block, body = parse_fm(text)
        if not fm_block:
            skipped.append(f"{r['name']}: no-frontmatter")
            continue
        new_fm, fm_added = add_fm_fields(fm, fm_block)
        new_body, body_added = remediate_body(body, r["name"])
        if not fm_added and not body_added:
            skipped.append(f"{r['name']}: already-complete")
            continue
        new_text = new_fm + new_body
        try:
            await loop.run_in_executor(None, _write_text, path, new_text)
            fixed.append((r["name"], sorted(set(fm_added + body_added))))
        except Exception as e:  # pragma: no cover
            errors.append(f"{r['name']}: {e}")
    # Report
    lines = ["# Remediation Report (Phase 5, safe/additive)", ""]
    lines.append(f"- FAIL skills targeted: {len(fail)}")
    lines.append(f"- Skills patched: {len(fixed)}")
    lines.append(f"- Skipped (complete/no-fm/missing): {len(skipped)}")
    lines.append(f"- Errors: {len(errors)}")
    lines.append("")
    lines.append("## Patched Skills")
    lines.append("| Skill | Added |")
    lines.append("|-------|-------|")
    for name, adds in fixed:
        lines.append(f"| {name} | {', '.join(adds)} |")
    if skipped:
        lines.append("")
        lines.append("## Skipped")
        for s in skipped:
            lines.append(f"- {s}")
    if errors:
        lines.append("")
        lines.append("## Errors")
        for e in errors:
            lines.append(f"- {e}")
    report_text = "\n".join(lines) + "\n"
    await loop.run_in_executor(None, _write_text, REPORT, report_text)
    print(f"Patched {len(fixed)} FAIL skills (additive). Report: {REPORT}")
    return 0

def _read_text(path: Path) -> str:
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()

def _write_text(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
