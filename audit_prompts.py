#!/usr/bin/env python3
"""Read-only content-structure + safety audit for Hermes prompt library."""

import json
import os
import re

PROMPT_DIR = r"C:\Users\Alexa\AppData\Local\hermes\prompts"
OUT = os.path.join(PROMPT_DIR, "docs", "content-safety-audit.md")

# --- Structure keywords (heading must contain one at H2/H3) ---
STRUCTURE_KEYWORDS = ["goal", "context", "workflow", "phase", "rule"]

# --- CRITICAL (injection / jailbreak) patterns ---
CRITICAL_PATTERNS = [
    (r"ignore (all |any |your |the )?previous instructions", "ignore previous instructions"),
    (r"pretend you are", "pretend you are"),
    (r"you are dan\b", "DAN jailbreak"),
    (r"\bDAN\b", "DAN"),
    (r"reveal your system prompt", "reveal system prompt"),
    (r"reveal (the )?system (message|instructions)", "reveal system prompt"),
    (r"exfiltrate", "exfiltrate"),
    (r"do anything now", "do anything now (jailbreak)"),
    (r"bypass (your |the )?(safety|content|guard)", "bypass safety"),
]

# --- HIGH: destructive operations ---
DESTRUCTIVE_PATTERNS = [
    r"rm\s+-rf?\b",
    r"rm\s+-fr\b",
    r"rm\s+-r\b",
    r"sudo\s+rm\b",
    r"del\s+/[fqs]",
    r"rmdir\s+/s",
    r"drop\s+(table|database)\b",
    r"git\s+push\s+--force",
    r"git\s+reset\s+--hard",
    r"git\s+clean\s+-f",
    r"truncate\s+table\b",
    r"mkfs",
    r"dd\s+if=",
    r">\s*/dev/sd",
    r"chmod\s+777",
    r"format\s+(the\s+)?(disk|drive|partition)",
    r"curl\s+[^\n]*\|\s*(sudo\s+)?(ba)?sh",
    r"wget\s+[^\n]*\|\s*(ba)?sh",
    r":\(\)\s*\{\s*:\s*\|\s*:",  # fork bomb
]

# --- HIGH: secrets/credentials EXPOSURE instructions (protective phrasing excluded) ---
SECRET_EXPOSE_PATTERNS = [
    r"(show|print|echo|output|reveal|exfiltrate|send|return|dump|leak)\b.{0,40}\b(password|secret|api[ _-]?key|token|credential)",
    r"\b(password|secret|api[ _-]?key|token|credential)\b.{0,40}\b(show|print|echo|output|reveal|exfiltrate|send|return|dump|leak)\b",
]
# Negation words marking a PROTECTIVE instruction (do NOT flag)
SECRET_NEGATION = [
    r"never",
    r"don'?t",
    r"do not",
    r"avoid",
    r"must not",
    r"should not",
    r"shall not",
    r"forbid",
    r"refuse",
    r"without permission",
    r"keep .{0,20}(secret|private)",
    r"stay (in|within)",
    r"store",
]

# Approval-gate words (presence anywhere in file neutralizes destructive HIGH)
APPROVAL_GATE = [
    r"approval",
    r"approve",
    r"confirm",
    r"consent",
    r"authoriz",
    r"ask (the )?(user|before)",
    r"before proceeding",
    r"get .{0,15}permission",
    r"must be confirmed",
    r"user .{0,15}confirm",
    r"verify with",
    r"requires?",
]


def split_frontmatter(text):
    """Return (body, ok). Body is text after the closing --- of frontmatter."""
    if not text.startswith("---"):
        return text, False
    # find second ---
    lines = text.split("\n")
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        return text, False
    return "\n".join(lines[close + 1 :]), True


def has_structure(body):
    """Return (has_any_heading, has_canonical_heading)."""
    any_h = False
    canon = False
    for line in body.split("\n"):
        if re.match(r"^#{2,3}\s+", line):  # H2 or H3
            any_h = True
            low = line.lower()
            for kw in STRUCTURE_KEYWORDS:
                if kw in low:
                    canon = True
                    break
    return any_h, canon


def find_patterns(body, patterns, with_label=False):
    """Return list of (line_no, snippet, label) for matches."""
    res = []
    for ln, line in enumerate(body.split("\n"), 1):
        low = line.lower()
        for p in patterns:
            if isinstance(p, tuple):
                pat, label = p
            else:
                pat, label = p, None
            if re.search(pat, low):
                snippet = line.strip()[:160]
                res.append((ln, snippet, label or pat))
    return res


files = sorted(f for f in os.listdir(PROMPT_DIR) if f.endswith(".prompt.md"))

structure_less = []  # no H2/H3 heading at all (true blob)
noncanonical = []  # has headings but no canonical keyword section
critical_findings = []  # (file, line, snippet, label)
high_findings = []  # (file, line, snippet, label)

for fn in files:
    path = os.path.join(PROMPT_DIR, fn)
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    body, _ = split_frontmatter(text)
    any_h, canon = has_structure(body)
    if not any_h:
        structure_less.append(fn)
    elif not canon:
        noncanonical.append(fn)

    # CRITICAL
    crit = find_patterns(body, CRITICAL_PATTERNS, with_label=True)
    seen = set()
    for ln, snip, label in crit:
        key = (fn, ln, label)
        if key not in seen:
            seen.add(key)
            critical_findings.append((fn, ln, snip, label))

    # HIGH destructive (only if no approval gate in whole file)
    has_gate = any(re.search(g, text.lower()) for g in APPROVAL_GATE)
    dest = []
    for ln, line in enumerate(body.split("\n"), 1):
        low = line.lower()
        for p in DESTRUCTIVE_PATTERNS:
            if re.search(p, low):
                dest.append((ln, line.strip()[:160]))
                break
    if dest and not has_gate:
        for ln, snip in dest:
            high_findings.append((fn, ln, snip, "destructive-without-gate"))

    # HIGH secret exposure (skip protective/negated phrasing)
    sec = []
    for ln, line in enumerate(body.split("\n"), 1):
        low = line.lower()
        matched = False
        for p in SECRET_EXPOSE_PATTERNS:
            if re.search(p, low):
                matched = True
                break
        if matched:
            protective = any(re.search(n, low) for n in SECRET_NEGATION)
            if not protective:
                snip = line.strip()[:160]
                if (fn, ln, snip) not in sec:
                    sec.append((fn, ln, snip))
    for fn2, ln, snip in sec:
        high_findings.append((fn2, ln, snip, "secret-exposure"))

summary = {
    "total": len(files),
    "structure_less_count": len(structure_less),
    "noncanonical_count": len(noncanonical),
    "critical_count": len(critical_findings),
    "high_count": len(high_findings),
}

print(json.dumps(summary, indent=2))
print("\nSTRUCTURE-LESS (no headings at all):")
for f in structure_less:
    print("  ", f)
print("\nNON-CANONICAL (has headings, no Goal/Context/Workflow/Phases/Rules):")
for f in noncanonical:
    print("  ", f)
print("\nCRITICAL:")
for f in critical_findings:
    print("  ", f)
print("\nHIGH:")
for f in high_findings:
    print("  ", f)

# Save intermediate for report build
with open("/c/Users/Alexa/Desktop/SandBox/_audit_data.json", "w") as fh:
    json.dump(
        {
            "summary": summary,
            "structure_less": structure_less,
            "noncanonical": noncanonical,
            "critical": critical_findings,
            "high": high_findings,
        },
        fh,
        indent=2,
    )
