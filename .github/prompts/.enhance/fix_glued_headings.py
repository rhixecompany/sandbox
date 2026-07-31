#!/usr/bin/env python3
"""
fix_glued_headings.py — De-glue collapsed markdown headings in prompt files.

Bug: enhancement pass collapsed `## Heading\n\ncontent` into `## Headingcontent`
(single line). Later passes re-split only at `## ` boundaries, leaving headings
glued to their content (e.g. `## GoalAdd educational...`).

Fix: for each `## `/`### `/`# ` line, find the longest trusted heading name that
is a prefix of the text with NO space after it (the collapse removed the
newline AND the space between heading and first content word). Split into
`## <name>` + blank line + content, and restore sub-structure (bullets,
blockquotes, numbered lists, code fences) lost to newline collapse.

SAFE: dry-run by default. Pass --apply to write changes. Preserves CRLF/LF.
"""
import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

# ---------------------------------------------------------------------------
# Heading dictionary
# ---------------------------------------------------------------------------
def load_heading_names():
    """Trusted heading names = names seen as EXACT heading lines across the library
    plus canonical standard section names."""
    names = set()
    # 1) names that appear as exact heading lines (## X with nothing after)
    for f in PROMPTS_DIR.glob("*.md"):
        text = f.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            line = line.rstrip("\r\n")
            for marker in ("## ", "### ", "# "):
                if line.startswith(marker):
                    rest = line[len(marker):]
                    if rest and not rest[0].isspace() and len(rest) <= 60:
                        names.add(rest)
    # 2) canonical standard section names
    std = [
        "Goal", "Context", "Inputs", "Outputs", "Rules", "Phases", "Role",
        "Objectives", "Workflow", "Personas", "Personality", "Best Practices",
        "Verification Checklist", "Dependencies", "Subgoals", "Skills Required",
        "MCP Servers & Tools", "Tasks", "Template References",
        "Configuration Variables", "Generated Prompt", "Description",
        "Actions", "Actions Summary", "Project", "Output", "Implementation",
        "Test", "Quality", "Overview", "Purpose", "Core Requirements",
        "Success Criteria", "Anti-Patterns", "Domain Rules", "Standing Rules",
        "Educational Commenting Rules", "Workflow Steps", "Input", "Method",
        "Examples", "Notes", "References", "Prerequisites", "Deliverables",
        "Constraints", "Acceptance Criteria", "Primary Objective",
        "Severity Definitions", "Evidence Standard", "Instructions", "Steps",
        "Configuration Reference", "Final Checklist", "Key Findings",
        "Investigation Plan", "Integration Points", "Access Pattern Mapping",
        "Additional Considerations", "Advanced Use Cases", "Available Tools",
        "Build", "Change Management", "Code Review Findings",
        "Common Issues", "Completion Checklist", "Completion Report",
        "Consequences", "Contract", "Decision", "Error Handling",
        "Execution Constraints", "Failure Handling", "Gate Results",
        "Generation Modes", "Governance and Compliance", "Input/Output Contracts",
        "Requirements", "Assumptions", "Decisions", "Risks", "Open Questions",
        "Next Steps", "Phase 1: Intake", "Phase 2: Execute", "Phase 3: Verify",
        "Phase 4: Hand Off", "Phase 1: Discovery", "Phase 2: Analysis",
        "Phase 3: Generation", "Phase 4: Verification", "Phase 1", "Phase 2",
        "Phase 3", "Phase 4", "Phase 5", "Phase 6", "Step 1", "Step 2", "Step 3",
        "License", "Feature", "Progress Tracking", "Scope", "Testing",
        "Troubleshooting", "Edge Cases & Exceptions", "Anti-Patterns to Avoid",
        "Primary Objective", "Deliverable", "Response Semantics",
        "Common Patterns", "Error Handling", "Validation Checklist",
        "Implementation Details", "Implementation Status", "Invocation Order",
        "Invocation", "Branching", "Template Structure", "What You Should Do First When Run",
    ]
    names.update(std)
    # 3) domain-specific H3 names harvested from glued lines themselves:
    #    `### <Name>- <content...` or `### <Name>> <content...` -> candidate
    #    name is the text before the structural marker
    for f in PROMPTS_DIR.glob("*.md"):
        text = f.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            line = line.rstrip("\r\n")
            if not line.startswith("### "):
                continue
            rest = line[4:]
            m = re.match(r"^(.*?)(?:- |> |>> |\d+\. )", rest)
            if m:
                cand = m.group(1).strip()
                # plausible heading: starts uppercase, ends word char, short,
                # no sentence-ending punctuation, no code fences
                if (cand and cand[0].isupper() and len(cand) <= 60
                        and not re.search(r"[.!?]$", cand)
                        and "```" not in cand and "`" not in cand
                        and not re.search(r"[a-z][A-Z]", cand)):
                    names.add(cand)
            # also: heading glued directly to a code fence `### Name```text`
            m2 = re.match(r"^(.*?)```", rest)
            if m2:
                cand = m2.group(1).strip()
                if cand and cand[0].isupper() and len(cand) <= 60 and "`" not in cand:
                    names.add(cand)
    # drop names that clearly contain content OR are obvious garbage
    bad = re.compile(
        r"[-–] [a-z]|> |```|\$\{|\{\{|\#\{|[a-z][A-Z]|^\d"  # original patterns
        r"|^Go'?$|^Task'?$|^Tasks'?$|^Example'?$|^Examples'?$"  # truncated forms
        r"|^Best Practice'?$|^Do'?$|^Don'?t'?$|^Do Not'?$|^DO NOT'?$"
        r"|^Best'?$|^Good'?$|^Bad'?$|^Run'?$|^Go'?$|^Stop'?$"
        r"|^Phases>$|^Steps>$|^Tasks>$|^Tasks:$|^Steps:$"
        r"|^tool1$|^event$|^code$|^img$|^FAQ$|^css$|^E2E$|^DO$|^DO NOT$"
        r"|^Tips$|^Tips'$|^TODO$|^resx$|^Tags$|^C #$|^img$"
        r"|^\S+❌$|^\S+✅$|^\S+❌$"
        r"|^C #$|^C# 的指針$|^ルール$"
    )
    clean = {n for n in names if not bad.search(n) and not n.startswith(("-", ">", "`", "1.", "2."))}
    return sorted(clean, key=len, reverse=True)


HEADING_NAMES = load_heading_names()

# ---------------------------------------------------------------------------
# Content re-splitting helpers
# ---------------------------------------------------------------------------
# Split BEFORE a bullet marker that follows non-whitespace (glued list item).
# Zero-width lookahead keeps the "- " marker on the continuation item.
BULLET_SPLIT = re.compile(r"(?<=\S)(?=- [A-Z\[`*#])")
# Split BEFORE a numbered marker glued after non-whitespace.
NUM_SPLIT = re.compile(r"(?<=\S)(?=\d+\. [A-Z\[`*#])")


def split_bullets(text):
    parts = [p.strip() for p in BULLET_SPLIT.split(text) if p.strip()]
    if len(parts) <= 1:
        return [text.strip()]
    # ensure each item has its marker
    out = []
    for p in parts:
        out.append(p if p.startswith("- ") else "- " + p)
    return out


def split_numbered(text):
    parts = [p.strip() for p in NUM_SPLIT.split(text) if p.strip()]
    if len(parts) <= 1:
        return [text.strip()]
    return parts


def split_content(rest):
    """Restore sub-structure in collapsed content. Returns list of body lines."""
    rest = rest.strip()
    if not rest:
        return []
    # Code fence: ```lang...```  -> fence open, content, fence close
    if rest.startswith("```"):
        # NON-lazy language capture: ```text[...] must yield ```text + content,
        # never ``` + text[...] (lazy [^\n]*? swallowed the language token).
        m = re.match(r"^(```[a-zA-Z0-9+#.\-]*)(.*?)(```)\s*$", rest, re.DOTALL)
        if m and m.group(2).strip():
            return [m.group(1), m.group(2).strip("\n"), m.group(3)]
        return [rest]
    # Blockquote run: > A> B  (or >> A)  -> each > starts a line
    if rest.startswith(">"):
        rest = re.sub(r"^>+ ", "> ", rest)  # collapse >> artifact to single >
        # split at each "> " boundary
        parts = [p.strip() for p in re.split(r"(?=> )", rest) if p.strip()]
        out = []
        for p in parts:
            if p.startswith("> "):
                inner = p[2:].strip()
                # table glued after blockquote content -> split table rows out
                if "||" in inner:
                    chunks = [c.strip() for c in re.split(r"(?<=\|)(?=\| )", inner) if c.strip()]
                    if len(chunks) > 1:
                        out.append("> " + chunks[0])
                        out.extend(chunks[1:])
                        continue
                # bullets glued after blockquote content -> split out
                chunks = [c.strip() for c in BULLET_SPLIT.split(inner) if c.strip()]
                if len(chunks) > 1:
                    out.append("> " + chunks[0])
                    for c in chunks[1:]:
                        out.append(c if c.startswith("- ") else "- " + c)
                else:
                    # numbered list glued after blockquote content -> split out
                    nchunks = [c.strip() for c in NUM_SPLIT.split(inner) if c.strip()]
                    if len(nchunks) > 1:
                        out.append("> " + nchunks[0])
                        out.extend(nchunks[1:])
                    else:
                        out.append("> " + inner)
            else:
                out.append(p)
        return out
    # Bullet run: - A- B  -> each - item
    if rest.startswith("- "):
        return split_bullets(rest)
    # Numbered run: 1. A2. B -> each N. item
    if re.match(r"^\d+\. ", rest):
        return split_numbered(rest)
    # Plain paragraph
    return [rest]


def fix_line(line, marker):
    """If line is a glued heading, return (fixed_lines, changed). Else (None, False)."""
    text = line[len(marker):]
    for name in HEADING_NAMES:
        if text.startswith(name) and len(text) > len(name):
            rest = text[len(name):]
            # GLUE signature: collapse removed the space between heading and
            # content, so the next char touches the name (no space).
            if rest[0] != " ":
                # "Phase 2: X" - a colon means the real heading continues
                # (matched name was a prefix of a longer heading)
                if rest[0] == ":":
                    continue
                # orphan blockquote artifact "## Phases>" -> drop the bare >
                if rest.strip() in (">", ">>"):
                    return [f"{marker}{name}"], True
                body = split_content(rest)
                fixed = [f"{marker}{name}", ""] + body
                return fixed, True
    return None, False


def fix_file(path):
    """Returns (changed_count, new_text) or (0, None)."""
    raw = path.read_bytes()
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8", errors="replace")

    fm_match = re.match(r"^---\r?\n.*?\r?\n---\r?\n", text, re.DOTALL)
    if not fm_match:
        return 0, None
    head = fm_match.group(0)
    body = text[fm_match.end():]
    lines = body.split("\n")

    out = []
    changed = 0
    for line in lines:
        line = line.rstrip("\r\n")
        if line.startswith("## ") or line.startswith("### "):
            marker = "## " if line.startswith("## ") else "### "
            fixed, is_change = fix_line(line, marker)
            if fixed is not None:
                out.extend(fixed)
                changed += 1
                continue
        out.append(line)

    if changed == 0:
        return 0, None

    new_body = "\n".join(out)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    new_text = head + new_body
    if not new_text.endswith("\n"):
        new_text += "\n"
    # Normalize to LF (matches .gitattributes `*.md text eol=lf`).
    # Never re-apply CRLF on top of existing CRLF — that double-encodes.
    new_text = new_text.replace("\r\n", "\n").replace("\r", "\n")
    return changed, new_text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    ap.add_argument("--file", help="Process only this filename")
    args = ap.parse_args()

    files = sorted(PROMPTS_DIR.glob("*.md"))
    total_changed = 0
    total_fixed = 0
    for f in files:
        if args.file and args.file not in f.name:
            continue
        changed, new_text = fix_file(f)
        if changed and new_text is not None:
            total_changed += 1
            total_fixed += changed
            if args.apply:
                f.write_text(new_text, encoding="utf-8", newline="")
                print(f"FIXED {f.name}: {changed} headings")
            else:
                print(f"WOULD FIX {f.name}: {changed} headings")
    print(f"\n{total_changed} files, {total_fixed} heading fixes ({'APPLIED' if args.apply else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
