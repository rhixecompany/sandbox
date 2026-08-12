#!/usr/bin/env python3
"""Phase 3 (Class C) — repair collapsed/glued fence blocks using intact history.

Damage shapes handled:
  S1. Start-line glued opener:  ```lang<first code line>...   (newlines collapsed)
  S2. Glued opener + '>' continuation lines that complete the collapsed block
  S3. Odd fence parity (opener without closer, extra closers)

Repair strategy (never fabricate):
  - EXACT / PREFIX / TAIL match vs intact history (commit INTACT):
      replace the damaged region with the lossless intact block (+ followup).
  - NO match (content enhanced since INTACT): structural split only —
      fence opener on its own line, content preserved verbatim, flagged
      [MANUAL REVIEW] in the report.

Usage:
  python fix_collapsed_fences.py            # dry-run
  python fix_collapsed_fences.py --apply    # write changes
  python fix_collapsed_fences.py --files a.prompt.md b.prompt.md
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path.home() / "Desktop/SandBox"
PROMPTS = ROOT / ".github/prompts"
INTACT = "879b4532"

KNOWN_LANGS = [
    "ruby", "bash", "sh", "python", "py", "javascript", "js", "typescript",
    "ts", "json", "markdown", "md", "yaml", "yml", "kotlin", "java", "swift",
    "php", "csharp", "cs", "go", "rust", "rs", "html", "css", "sql",
    "dockerfile", "text", "console", "shell", "tsx", "jsx", "xml", "toml",
    "ini", "env", "graphql", "gql", "powershell", "ps1", "diff", "patch",
    "mermaid", "txt", "zsh", "makefile", "gradle", "properties",
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
    """Return [(lang, body, start_line, end_line, followup)] from intact version."""
    text = intact_text(name)
    if text is None:
        return []
    bodies = []
    ilines = text.split("\n")
    for m in re.finditer(
        r"^(`{3,})([^\s`]*)[ \t]*\n(.*?)^\1[ \t]*$", text, re.M | re.S
    ):
        start = text[: m.start()].count("\n") + 1
        end = start + m.group(3).count("\n")
        # followup: lines after the closing fence, up to the next fence or heading
        followup = ""
        k = end + 2  # 1-based line after the closing fence -> 0-based index
        while k < len(ilines):
            ln = ilines[k]
            if re.match(r"^(`{3,})", ln) or re.match(r"^#{1,6}\s", ln):
                break
            followup += ln + "\n"
            k += 1
            if k - (end + 2) > 12:  # cap
                break
        bodies.append((m.group(2), m.group(3), start, end, followup.rstrip("\n")))
    return bodies


def analyze_line(line: str):
    """Classify a damaged fence line. Returns (typ, lang, body, tail, has_close)."""
    m = re.match(r"^(`{3,})(\S*)(.*)$", line)
    if not m:
        return None
    opener, glue, rest = m.group(1), m.group(2), m.group(3)
    # Legitimate bare opener: ```lang with nothing glued -> not damage.
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
    if glue in KNOWN_LANGS:
        # ```bash <glued content> — lang is exactly known, rest is body
        lang = glue
        body = body.lstrip()
    else:
        lang, b2 = split_lang_glue(glue)
        if b2 is not None and glue != lang:
            body = b2 + body
        else:
            # glue is not a language marker — it's the start of the collapsed body
            body = glue + body
    if not body.strip() and not tail.strip():
        return None
    return ("T1" if has_close else "T2", lang or "", body, tail, has_close)


def find_repair(name: str, lines, idx: int, a) -> dict[str, Any] | None:
    """Determine repair for a damaged line at idx (0-based). Returns dict or None."""
    typ, lang, body, tail, has_close = a
    # Gather region: this line + following '>' continuation lines (raw, keep '>')
    region_lines = [lines[idx]]
    region_idx = [idx]
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
            region_idx.append(j)
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
        return {"action": "split", "reason": "no-intact", "region": region_lines, "region_idx": region_idx}

    best = None
    for ilang, ibody, istart, iend, ifollow in intact_bodies:
        ib_norm = norm(ibody)
        if ib_norm and (ib_norm == region_raw or ib_norm == region_stripped):
            best = ("exact", ilang, ibody, istart, iend, ifollow)
            break
    if best is None:
        # PREFIX: intact body starts with region content (recover lost tail)
        for ilang, ibody, istart, iend, ifollow in intact_bodies:
            ib_norm = norm(ibody)
            if ib_norm.startswith(region_raw) and len(ib_norm) > len(region_raw):
                best = ("prefix", ilang, ibody, istart, iend, ifollow)
                break
        if best is None:
            for ilang, ibody, istart, iend, ifollow in intact_bodies:
                ib_norm = norm(ibody)
                if ib_norm.startswith(region_stripped) and len(ib_norm) > len(region_stripped):
                    best = ("prefix", ilang, ibody, istart, iend, ifollow)
                    break
    if best is None:
        # TAIL: intact body is a prefix of the region content (extra glued on).
        # The extra may be (a) the block's followup text, (b) followup + one or
        # more subsequent intact fences, or (c) just a stray closing fence.
        for k, (ilang, ibody, istart, iend, ifollow) in enumerate(intact_bodies):
            ib_norm = norm(ibody)
            if not ib_norm:
                continue
            matched = None
            if region_raw.startswith(ib_norm):
                matched = region_raw
            elif region_stripped.startswith(ib_norm):
                matched = region_stripped
            if matched is None:
                continue
            extra_norm = matched[len(ib_norm):]
            # The extra often begins with the closing fence (```) that our
            # restore already provides; strip it before comparing.
            if extra_norm.startswith("```"):
                extra_norm = extra_norm[3:]
            if not extra_norm:
                best = ("tail", ilang, ibody, istart, iend, ifollow)
                break
            if ifollow and norm(ifollow) == extra_norm:
                best = ("tail", ilang, ibody, istart, iend, ifollow)
                break
            # (b) followup + subsequent fences (e.g. "Make the file
            # executable:" + a chmod bash block) — reconstruct from intact.
            extended = ifollow
            for ilang2, ibody2, istart2, iend2, ifollow2 in intact_bodies[k + 1:]:
                fence2 = "\n\n```" + (ilang2 + "\n" if ilang2 else "\n") + ibody2 + "\n```"
                extended += fence2
                if norm(extended) == extra_norm:
                    best = ("tail", ilang, ibody, istart, iend, extended)
                    break
                if norm(extended).startswith(extra_norm) and len(extra_norm) > 5:
                    best = ("tail", ilang, ibody, istart, iend, extended)
                    break
                # keep extending while extra_norm is longer than current
                if len(extra_norm) > len(norm(extended)):
                    continue
                break
            if best is not None:
                break
            # (c) tiny residue (<=4 chars: stray ```, artifact) — the region
            # is the intact body plus a glued fence closer: restore losslessly.
            if len(extra_norm) <= 4:
                best = ("tail", ilang, ibody, istart, iend, "")
                break

    if best is None:
        return {"action": "split", "reason": "no-match", "region": region_lines, "region_idx": region_idx}

    action, ilang, ibody, istart, iend, ifollow = best
    return {
        "action": "restore",
        "mode": action,
        "lang": ilang,
        "intact_body": ibody,
        "followup": ifollow,
        "tail": tail,
        "region": region_lines,
        "region_idx": region_idx,
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
        region = list(rep["region"])
        region_idx: list[int] = [int(x) for x in rep["region_idx"]]
        rspan = region_idx[-1] - region_idx[0] + 1  # full span incl. skipped blanks
        orig_start = orig_i + 1  # 1-based original line number of region start
        if rep["action"] == "restore":
            block = "```" + (str(rep["lang"]) + "\n" if str(rep["lang"]) else "\n")
            block += str(rep["intact_body"])
            if not block.endswith("\n"):
                block += "\n"
            block += "```"
            # keep trailing text glued after the closer as its own line
            if str(rep["tail"]).strip():
                block += "\n" + str(rep["tail"]).strip()
            # TAIL mode: append the intact followup text (e.g. "Make the file
            # executable:" + a second fence) so no content is lost.
            if rep["mode"] == "tail" and str(rep["followup"]).strip():
                block += "\n\n" + str(rep["followup"]).strip()
            replacement = block.split("\n")
            out[region_idx[0] : region_idx[-1] + 1] = replacement
            details.append(
                f"L{orig_start} restore({rep['mode']}, {rep['lang'] or 'none'}): "
                f"{len(region)} region line(s) -> {len(replacement)} line(s)"
            )
            changed += 1
            i = region_idx[0] + len(replacement)
            orig_i += rspan
        else:
            # structural split: use analyzed lang/body (never re-parse)
            lang, body, tail, has_close = a[1], a[2], a[3], a[4]
            opener = "```" + (lang + "\n" if lang else "\n")
            new_lines = [opener]
            if body.strip():
                new_lines.append(body.rstrip())
            if has_close:
                new_lines.append("```")  # normalize to 3 backticks
            elif tail.strip():
                # no closer on the line but trailing text — keep it
                new_lines.append(tail.rstrip())
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
