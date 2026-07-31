#!/usr/bin/env python3
"""fix_prompt_artifacts.py — repair latent prompt-library defects.

Two defect classes introduced by earlier bulk scripts (commit 228eae32 era):

1. ORPHAN_S: glue-repair split plural headings (`## Inputs- ...`) into
   `## Input` + orphan `s` line + list. Merge the `s` back into the heading
   to restore the pre-corruption text.

2. BULLET_GLUE: body-text list items merged onto one line
   (`sentence.- Next item`). Split at the period-dash-space boundary.

3. DUP_SECTIONS: an older enhancer version appended standardized sections
   without checking whether the heading already existed, leaving duplicated
   Goal/Context/Rules/Phases/... blocks bolted onto legacy bodies. For the
   13 standard sections + Template References, keep the FIRST occurrence
   (domain content) and remove later appended duplicates.

Idempotent: re-running on a clean library produces zero changes.
Usage: python fix_prompt_artifacts.py [--apply]
"""
import re
import sys
import pathlib

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
DRY = "--apply" not in sys.argv

PLURALIZE = {
    "Input": "Inputs",
    "Output": "Outputs",
    "Quality Gate": "Quality Gates",
    "Reference": "References",
    "Deliverable": "Deliverables",
}

# Standard sections that must appear exactly once (keep first occurrence).
ALLOWED_DUP = {
    "Goal", "Subgoals", "Personas", "Personality", "Context", "Rules",
    "Phases", "Best Practices", "Verification Checklist",
    "Skills Required", "MCP Servers & Tools", "Tasks", "Dependencies",
    "Template References",
}

HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")


def fix_orphan_s(lines):
    """Merge `## Input\\n\\ns\\n\\n` -> `## Inputs\\n\\n`. Returns new lines + change count."""
    out = []
    changes = 0
    i = 0
    n = len(lines)
    while i < n:
        m = HEADING_RE.match(lines[i])
        if (
            m
            and m.group(1) in PLURALIZE
            and i + 3 < n
            and lines[i + 1] == ""
            and lines[i + 2].strip() == "s"
            and lines[i + 3] == ""
        ):
            out.append("## " + PLURALIZE[m.group(1)])
            out.append("")
            i += 4  # heading, blank, s, blank
            changes += 1
            continue
        out.append(lines[i])
        i += 1
    return out, changes


def fix_dups(lines):
    """Remove duplicate standard sections, keeping the first occurrence each."""
    heading_idx = [i for i, ln in enumerate(lines) if HEADING_RE.match(ln)]

    # count occurrences per allowed heading name
    counts = {}
    for i in heading_idx:
        name = HEADING_RE.match(lines[i]).group(1).strip()
        if name in ALLOWED_DUP:
            counts[name] = counts.get(name, 0) + 1

    # ranges to remove: occurrence >= 2, spanning to the next heading line
    ranges = []
    seen = {}
    for pos, i in enumerate(heading_idx):
        name = HEADING_RE.match(lines[i]).group(1).strip()
        if name not in ALLOWED_DUP:
            continue
        seen[name] = seen.get(name, 0) + 1
        if seen[name] >= 2:
            end = heading_idx[pos + 1] if pos + 1 < len(heading_idx) else len(lines)
            ranges.append((i, end))

    if not ranges:
        return lines, 0, []

    # merge overlapping/adjacent ranges
    ranges.sort()
    merged = [list(ranges[0])]
    for start, end in ranges[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    removed_names = []
    drop = set()
    for start, end in merged:
        for i in range(start, end):
            drop.add(i)
        removed_names.append(lines[start].strip())

    out = [ln for i, ln in enumerate(lines) if i not in drop]
    return out, len(merged), removed_names


def fix_bullet_glue(lines):
    """Split glued bullet text: 'sentence.- Next bullet' -> 'sentence.' + new bullet.

    Pattern: letter + '.' + '- ' (period-dash-space) with no space before the dash.
    This is the residual glue from the 228eae32-era corruption where list items
    were merged into a single line (e.g. '...practical.- Focus on reviewer mindset').
    A blank line separates the new bullet only when the next line continues the list.
    """
    out = []
    changed = 0
    for ln in lines:
        if re.search(r"[A-Za-z]\.- ", ln):
            new_ln = re.sub(r"([A-Za-z])\.- ", r"\1.\n- ", ln)
            out.extend(new_ln.split("\n"))
            changed += 1
        else:
            out.append(ln)
    return out, changed


def normalize_separation(lines):
    """Ensure every '## ' heading is preceded by a blank line (unless first line)."""
    out = []
    for i, ln in enumerate(lines):
        if HEADING_RE.match(ln) and out and out[-1].strip() != "":
            out.append("")
        out.append(ln)
    return out


def process(pf):
    text = pf.read_text(encoding="utf-8")
    crlf = "\r\n" in text
    lines = text.splitlines()

    lines, s_changes = fix_orphan_s(lines)
    lines, b_changes = fix_bullet_glue(lines)
    lines, dup_ranges, dup_names = fix_dups(lines)
    lines = normalize_separation(lines)

    body = "\n".join(lines)
    if crlf:
        body = body.replace("\n", "\r\n")
        trailing = "\r\n" if text.endswith("\r\n") else ""
    else:
        trailing = "\n" if text.endswith("\n") else ""
    new_text = body + trailing
    if new_text != text:
        return new_text, s_changes, b_changes, dup_ranges, dup_names
    return None, 0, 0, 0, []


def main():
    files = sorted(P.glob("*.prompt.md"))
    print(f"=== Prompt Artifact Fixer ===\nMode: {'DRY' if DRY else 'APPLY'}\nFiles: {len(files)}\n")
    total_s = total_b = total_dup = 0
    changed = []
    for pf in files:
        new_text, s_changes, b_changes, dup_ranges, dup_names = process(pf)
        if new_text is None:
            continue
        total_s += s_changes
        total_b += b_changes
        total_dup += dup_ranges
        changed.append((pf.name, s_changes, b_changes, dup_ranges, dup_names))
        if not DRY:
            pf.write_text(new_text, encoding="utf-8")

    print(f"Files with changes: {len(changed)}")
    print(f"Orphan-s merges: {total_s}")
    print(f"Bullet-glue splits: {total_b}")
    print(f"Duplicate section removals: {total_dup}")
    if changed:
        print("\n=== First 15 files ===")
        for name, s, b, d, names in changed[:15]:
            print(f"  {name}: s={s} b={b} dup={d} {names[:4]}")
    print(f"\n{'DRY RUN. Run with --apply to execute.' if DRY else 'APPLY COMPLETE.'}")


if __name__ == "__main__":
    main()
