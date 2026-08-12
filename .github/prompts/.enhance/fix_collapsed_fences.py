#!/usr/bin/env python3
"""Phase 3 (Class C) — repair collapsed/glued fence blocks using intact history.

Damage shapes handled:
  S1. Start-line glued opener:  ```lang<first code line>...   (newlines stripped)
       - Sometimes the rest of the block continues as '>' prefixed lines.
       - Sometimes the closing ``` and following text are glued on the same line.
  S3. Odd fence parity per file (fixed by the S1 restores).

Strategy (never fabricate):
  1. EXACT: current collapsed body (whitespace-normalized) == an intact fence
     body at 879b4532 -> replace the damaged region with the intact block.
  2. PREFIX: current body is a prefix of an intact body and the remainder of
     the intact body appears as the following '>' continuation lines ->
     replace region with the full intact block (lossless recovery).
  3. TAIL: current line has extra text glued AFTER the closing ``` -> keep
     that text as its own line after the restored fence.
  4. NO_MATCH: structural split only — put the opener on its own line, keep
     the collapsed content, flag for manual review.

Usage:
  python fix_collapsed_fences.py            # dry-run report
  python fix_collapsed_fences.py --apply    # write changes
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.home() / "Desktop/SandBox"
PROMPTS = ROOT / ".github/prompts"
INTACT = "879b4532"

KNOWN_LANGS = [
    "ruby", "bash", "sh", "python", "py", "javascript", "js", "typescript",
    "ts", "json", "markdown", "md", "yaml", "yml", "kotlin", "java", "swift",
    "php", "csharp", "cs", "go", "rust", "rs", "html", "css", "sql",
    "dockerfile", "text", "console", "shell", "tsx", "jsx", "xml", "toml",
    "ini", "env", "graphql", "gql", "powershell", "ps1", "diff", "patch",
]


def split_lang_glue(token: str):
    """Split a glued lang+body token like 'javapackage' -> ('java', 'package')."""
    for lang in sorted(KNOWN_LANGS, key=len, reverse=True):
        if token.startswith(lang) and len(token) > len(lang):
            rest = token[len(lang):]
            if rest and rest[0] != "`" and not rest[0].isspace():
                return lang, rest
    return None, token


def norm(s: str) -> str:
    """Whitespace-insensitive normalization for comparison."""
    return re.sub(r"\s+", "", s)


def intact_text(name: str):
    r = subprocess.run(
        ["git", "show", f"{INTACT}:.github/prompts/{name}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        cwd=ROOT,
    )
    return r.stdout if r.returncode == 0 else None


def intact_fence_bodies(name: str):
    """Return [(lang, body, start_line, end_line)] from intact version."""
    text = intact_text(name)
    if text is None:
        return []
    bodies = []
    for m in re.finditer(
        r"^(`{3,})([^\s`]*)[ \t]*\n(.*?)^\1[ \t]*$", text, re.M | re.S
    ):
        start = text[: m.start()].count("\n") + 1
        end = start + m.group(3).count("\n")
        bodies.append((m.group(2), m.group(3), start, end))
    return bodies


def analyze_line(line: str):
    """Classify a damaged fence line. Returns (typ, lang, body, tail, has_close)."""
    m = re.match(r"^(`{3,})(\S*)(.*)$", line)
    if not m:
        return None
    opener, glue, rest = m.group(1), m.group(2), m.group(3)
    # Legitimate bare opener: ```lang with nothing glued -> not damage.
    # Accepts ```, ```text, ```mermaid, ```graph TB, etc.
    if not rest.strip():
        if not glue or glue in KNOWN_LANGS or split_lang_glue(glue)[0] is not None \
                or re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,15}", glue):
            return None
    # trailing close marker
    m2 = re.search(r"(`{3,})\s*$", rest)
    tail = ""
    if m2:
        body = rest[: m2.start()]
        tail = rest[m2.end():]
        has_close = True
    else:
        body = rest
        has_close = False
    lang, b2 = split_lang_glue(glue)
    if b2 is not None and glue != lang:
        body = b2 + body
    else:
        # glue is not a language marker — it's the start of the collapsed body
        body = glue + body
    if not body.strip() and not tail.strip():
        return None
    return ("T1" if has_close else "T2", lang or "", body, tail, has_close)


def find_repair(name: str, lines, idx: int, a):
    """Determine repair for a damaged line at idx (0-based). Returns dict or None."""
    typ, lang, body, tail, has_close = a
    # Gather region: this line + following '>' continuation lines (raw, keep '>')
    region_lines = [lines[idx]]
    j = idx + 1
    while j < len(lines):
        nxt = lines[j]
        if nxt.strip() == "":
            # peek: next non-blank is '>' continuation?
            k = j
            while k < len(lines) and lines[k].strip() == "":
                k += 1
            if k < len(lines) and lines[k].lstrip().startswith(">"):
                j = k
                continue
            break
        if nxt.lstrip().startswith(">"):
            region_lines.append(nxt)
            j += 1
        else:
            break
    # Compare using the extracted body (not the raw line with ``` markers).
    # Continuation '>' lines may be (a) genuine code (List<Resource>, ->) so
    # keep them raw, or (b) corruption artifacts so strip them. Try both.
    cont_raw = "".join(x.lstrip() for x in region_lines[1:])
    cont_stripped = "".join(re.sub(r"^>\s?", "", x.lstrip(), count=1) for x in region_lines[1:])
    region_raw = norm(body + cont_raw)
    region_stripped = norm(body + cont_stripped)
    intact_bodies = intact_fence_bodies(name)
    if not intact_bodies:
        return {"action": "split", "reason": "no-intact", "region": region_lines}

    best = None
    for ilang, ibody, istart, iend in intact_bodies:
        ib_norm = norm(ibody)
        if ib_norm and (ib_norm == region_raw or ib_norm == region_stripped):
            best = ("exact", ilang, ibody, istart, iend)
            break
    if best is None:
        # PREFIX: intact body starts with region content (recover lost tail)
        for ilang, ibody, istart, iend in intact_bodies:
            ib_norm = norm(ibody)
            if ib_norm.startswith(region_raw) and len(ib_norm) > len(region_raw):
                best = ("prefix", ilang, ibody, istart, iend)
                break
        if best is None:
            for ilang, ibody, istart, iend in intact_bodies:
                ib_norm = norm(ibody)
                if ib_norm.startswith(region_stripped) and len(ib_norm) > len(region_stripped):
                    best = ("prefix", ilang, ibody, istart, iend)
                    break
    if best is None:
        # TAIL: intact body is a prefix of the region content (extra glued on)
        for ilang, ibody, istart, iend in intact_bodies:
            ib_norm = norm(ibody)
            if ib_norm and (region_raw.startswith(ib_norm) or region_stripped.startswith(ib_norm)):
                best = ("tail", ilang, ibody, istart, iend)
                break

    if best is None:
        return {"action": "split", "reason": "no-match", "region": region_lines}

    action, ilang, ibody, istart, iend = best
    return {
        "action": "restore",
        "mode": action,
        "lang": ilang,
        "intact_body": ibody,
        "tail": tail,
        "region": region_lines,
    }


def build_restored_text(name: str, lines):
    """Return (new_lines, changed_count, details)."""
    out: list[str] = list(lines)
    changed = 0
    details = []
    i = 0
    orig_i = 0  # original line position (before edits) of out[i]
    while i < len(out):
        cur: str = out[i]
        a = analyze_line(cur)
        if a is None:
            i += 1
            orig_i += 1
            continue
        rep = find_repair(name, out, i, a)
        if rep is None:
            i += 1
            orig_i += 1
            continue
        region = rep["region"]
        orig_start = orig_i + 1  # 1-based original line number of region start
        if rep["action"] == "restore":
            block = "```" + (rep["lang"] + "\n" if rep["lang"] else "\n")
            block += rep["intact_body"]
            if not block.endswith("\n"):
                block += "\n"
            block += "```"
            # keep trailing text glued after the closer as its own line
            if rep["tail"].strip():
                block += "\n" + rep["tail"].strip()
            replacement = block.split("\n")
            out[i : i + len(region)] = replacement
            details.append(
                f"L{orig_start} restore({rep['mode']}, {rep['lang'] or 'none'}): "
                f"{len(region)} region line(s) -> {len(replacement)} line(s)"
            )
            changed += 1
            i += len(replacement)
            orig_i += len(region)
        else:
            # structural split: opener on own line, keep content collapsed
            opener = out[i].split("```")[0] + "```"
            rest = out[i][len(opener):]
            # if the line ends with a close marker, separate it
            m2 = re.search(r"(`{3,})\s*$", rest)
            content = rest
            closer = ""
            if m2:
                content = rest[: m2.start()]
                closer = m2.group(1)
            new_lines = [opener]
            if content.strip():
                new_lines.append(content.rstrip())
            if closer:
                new_lines.append("```")  # normalize to 3 backticks
            out[i : i + 1] = new_lines
            details.append(
                f"L{orig_start} split (NO_MATCH: {rep['reason']}) -> "
                f"{len(new_lines)} line(s) [MANUAL REVIEW]"
            )
            changed += 1
            i += len(new_lines)
            orig_i += 1
    return out, changed, details


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--files", nargs="*", default=None)
    args = ap.parse_args()

    files = sorted(PROMPTS.glob("*.prompt.md"))
    if args.files:
        files = [PROMPTS / f for f in args.files]

    total_changed = 0
    restore_count = 0
    split_count = 0
    for path in files:
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        crlf = b"\r\n" in raw
        lines = text.replace("\r\n", "\n").split("\n")
        # drop trailing empty from split
        if lines and lines[-1] == "":
            lines = lines[:-1]
        new_lines, changed, details = build_restored_text(path.name, lines)
        if changed == 0:
            continue
        total_changed += changed
        for d in details:
            if "restore" in d:
                restore_count += 1
            else:
                split_count += 1
        if args.apply:
            out_text = "\n".join(new_lines) + "\n"
            # preserve original EOL style unless the file was already LF
            if crlf:
                out_text = out_text.replace("\n", "\r\n")
            path.write_text(out_text, encoding="utf-8", newline="")
        print(f"== {path.name}: {changed} fix(es)")
        for d in details:
            print(f"   {d}")

    print(f"\nSUMMARY: {total_changed} fixes "
          f"({restore_count} restores, {split_count} splits)")
    if not args.apply:
        print("DRY-RUN — re-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
