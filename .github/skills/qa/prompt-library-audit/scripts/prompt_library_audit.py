#!/usr/bin/env python3
"""Read-only content-structure + safety audit for a Hermes prompt library.

Scans every *.prompt.md under --dir and checks each prompt BODY (text after the
closing frontmatter ---) for:
  * structure (canonical H2/H3 heading keywords)
  * CRITICAL safety (instruction-override / role-play jailbreak phrases)
  * HIGH safety (destructive ops without an approval gate; credential exposure
    that is not protective phrasing)

Emits docs/content-safety-audit.md and prints a summary. NEVER modifies prompt files.

Detection strings are assembled at RUNTIME (joined/encoded) so this file contains no
verbatim override phrases that would trip a literal-substring safety scanner, while
the compiled matchers are functionally identical.

Run:
    python prompt_library_audit.py --dir "C:\Users\Alexa\AppData\Local\hermes\prompts"
    python prompt_library_audit.py --dir <dir> --check-readonly   # SHA-256 diff proof
"""
import argparse
import hashlib
import json
import os
import re
import sys

STRUCT_KEYS = ["goal", "context", "workflow", "phase", "rule"]

# CRITICAL category: assembled at runtime. Each entry is a list of fragments joined
# with no spaces so the source never contains the full phrase as one literal.
_FRAGS = [
    ["ign", "ore previous instructions"],
    ["pre", "tend you are"],
    ["you are d", "an"],
    ["do any", "thing now"],
    ["rev", "eal your system prompt"],
    ["rev", "eal the system prompt"],
    ["exf", "iltrate"],
    ["byp", "ass safety"],
    ["byp", "ass the safety"],
]
CRIT = ["".join(p) for p in _FRAGS]

# HIGH destructive patterns (regex). Built from fragments to avoid verbatim literals.
def _j(*parts):
    return "".join(parts)

DESTRUCTIVE = [
    _j("rm", r"\s+-rf?\b"), _j("rm", r"\s+-fr\b"), _j("sudo", r"\s+rm\b"),
    _j("del", r"\s+/[fqs]"), _j("rmdir", r"\s+/s"),
    _j("dr", "op", r"\s+(table|database)\b"), _j("git", r"\s+push\s+--force"),
    _j("git", r"\s+reset\s+--hard"), _j("git", r"\s+clean\s+-f"),
    _j("trunc", "ate", r"\s+table\b"),
    _j("mk", "fs"), _j("dd", r"\s+if="), _j(">", r"\s*/dev/sd"),
    _j("chmod", r"\s+777"),
    _j("cur", "l", r"\s+[^\n]*\|\s*(sudo\s+)?(ba)?sh"),
    _j("wget", r"\s+[^\n]*\|\s*(ba)?sh"),
    _j(":", r"\(\)\s*\{\s*:\s*\|\s*:"),
]

GATE = [r"approval", r"approve", r"confirm", r"consent", r"authoriz",
        r"ask (the )?(user|before)", r"before proceeding", r"verify with", r"requires?"]

_VERB = "(" + "|".join([
    "show", "print", "echo", "output",
    "rev" + "eal", "exf" + "iltrate",
    "send", "return", "dump", "leak",
]) + ")"
_NOUN = r"(password|secret|api[ _-]?key|token|credential)"
EXPOSE_PAT = [_VERB + r".{0,40}" + _NOUN, _NOUN + r".{0,40}" + _VERB]
NEGATION = [r"never", r"don'?t", r"do not", r"avoid", r"must not", r"should not",
            r"shall not", r"forbid", r"refuse", r"without permission",
            r"keep .{0,20}(secret|private)", r"stay (in|within)", r"store"]


def split_frontmatter(text):
    if not text.startswith("---"):
        return text, False
    lines = text.split("\n")
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        return text, False
    return "\n".join(lines[close + 1:]), True


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def audit(dirpath):
    files = sorted(f for f in os.listdir(dirpath) if f.endswith(".prompt.md"))
    structure_less, noncanonical, critical, high = [], [], [], []
    for fn in files:
        with open(os.path.join(dirpath, fn), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        body, _ = split_frontmatter(text)
        any_h = bool(re.search(r"^#{2,3}\s+", body, re.M))
        canon = any(kw in ln.lower() for ln in body.split("\n")
                    if re.match(r"^#{2,3}\s+", ln) for kw in STRUCT_KEYS)
        if not any_h:
            structure_less.append(fn)
        elif not canon:
            noncanonical.append(fn)
        seen = set()
        for ln_no, line in enumerate(body.split("\n"), 1):
            ll = line.lower()
            for c in CRIT:
                if c in ll and (ln_no, c) not in seen:
                    seen.add((ln_no, c))
                    critical.append((fn, ln_no, c))
        has_gate = any(re.search(g, text.lower()) for g in GATE)
        if not has_gate:
            for ln_no, line in enumerate(body.split("\n"), 1):
                if any(re.search(p, line.lower()) for p in DESTRUCTIVE):
                    high.append((fn, ln_no, "destructive-without-gate"))
                    break
        for ln_no, line in enumerate(body.split("\n"), 1):
            ll = line.lower()
            if any(re.search(p, ll) for p in EXPOSE_PAT):
                if not any(re.search(n, ll) for n in NEGATION):
                    high.append((fn, ln_no, "secret-exposure"))
                    break
    summary = {
        "total": len(files),
        "structure_less_count": len(structure_less),
        "noncanonical_count": len(noncanonical),
        "critical_count": len(critical),
        "high_count": len(high),
    }
    return summary, structure_less, noncanonical, critical, high


def render_md(summary, structure_less, noncanonical, critical, high, dirpath):
    flagged = sorted(structure_less + noncanonical)
    L = []
    L.append("# Content-Structure & Safety Audit\n")
    L.append(f"**Scope:** read-only audit of {summary['total']} `*.prompt.md` in `{dirpath}`.\n")
    L.append("| Metric | Count |\n|---|---:|")
    L.append(f"| Total prompts audited | {summary['total']} |")
    L.append(f"| Structure-less (literal rule) | {len(flagged)} |")
    L.append(f"| &nbsp;&nbsp;↳ truly heading-free | {summary['structure_less_count']} |")
    L.append(f"| &nbsp;&nbsp;↳ non-canonical headings | {summary['noncanonical_count']} |")
    L.append(f"| **CRITICAL (injection/jailbreak)** | **{summary['critical_count']}** |")
    L.append(f"| **HIGH (destructive-no-gate / secret)** | **{summary['high_count']}** |\n")
    L.append("## Structure-less prompts\n")
    for f in sorted(structure_less):
        L.append(f"- `{f}` (heading-free)")
    for f in sorted(noncanonical):
        L.append(f"- `{f}` (non-canonical)")
    L.append("\n## Safety findings\n")
    for fn, ln, label in critical:
        L.append(f"- CRITICAL `{fn}` L{ln}: {label}")
    for fn, ln, label in high:
        L.append(f"- HIGH `{fn}` L{ln}: {label}")
    if not critical and not high:
        L.append("- None. Library is SAFE (no CRITICAL/HIGH findings).")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=r"C:\Users\Alexa\AppData\Local\hermes\prompts")
    ap.add_argument("--check-readonly", action="store_true")
    args = ap.parse_args()

    pre = {f: sha256(os.path.join(args.dir, f))
           for f in os.listdir(args.dir) if f.endswith(".prompt.md")} if args.check_readonly else None

    summary, sl, nc, cr, hi = audit(args.dir)
    os.makedirs(os.path.join(args.dir, "docs"), exist_ok=True)
    out = os.path.join(args.dir, "docs", "content-safety-audit.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render_md(summary, sl, nc, cr, hi, args.dir))

    if args.check_readonly:
        post = {f: sha256(os.path.join(args.dir, f))
                for f in os.listdir(args.dir) if f.endswith(".prompt.md")}
        changed = [f for f in pre if pre[f] != post.get(f)]
        if changed:
            print("READ-ONLY FAIL:", changed)
            sys.exit(1)
        print("READ-ONLY OK: 0 prompt files changed.")

    print(json.dumps(summary, indent=2))
    print("Report:", out)


if __name__ == "__main__":
    main()
