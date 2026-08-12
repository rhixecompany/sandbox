#!/usr/bin/env python3
"""align_tables.py — re-align all markdown tables to aligned-pipe style.

Handles two shapes:
  1. Real tables: rows split on '|' (single/double-pipe rows already normalized).
  2. Pseudo-tables (regression from earlier plan): space-padded rows with NO
     internal pipes (e.g. repo.prompt.md). Column boundaries are recovered
     from the separator row's dash runs.

Output style (passes MD060 + renders as a real GFM table):
    | #     | Project                         | Type        |
    | ----- | ------------------------------- | ----------- |
    | 1     | Banking                         | Fintech     |

Usage: python align_tables.py [--apply] [--files a.md b.md ...]
Default is dry-run. --apply writes LF-only.
"""
import pathlib
import re
import sys

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
APPLY = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
files = [P / a for a in args] if args else sorted(P.glob("*.md"))

DASH_RUN = re.compile(r"-+")


def is_table_line(ln: str) -> bool:
    return ln.lstrip().startswith("|")


def split_real_row(row: str) -> list[str]:
    """Split a real table row (with internal pipes) into stripped cells."""
    return [c.strip() for c in row.strip().strip("|").split("|")]


def pseudo_boundaries(sep: str) -> list[int]:
    """Recover column boundary offsets from a pseudo separator row's dash runs."""
    runs = [(m.start(), m.end()) for m in DASH_RUN.finditer(sep)]
    if len(runs) < 2:
        return []
    return [(runs[i][1] + runs[i + 1][0]) // 2 for i in range(len(runs) - 1)]


def split_pseudo_row(row: str, bnds: list[int]) -> list[str]:
    cells = []
    prev = 1  # skip leading pipe at col 0
    for b in bnds:
        cells.append(row[prev:b].strip())
        prev = b
    cells.append(row[prev:].rstrip().rstrip("|").strip())
    return cells


def is_sep_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells)


def align_table(block: list[str]) -> list[str] | None:
    """Return re-aligned rows, or None if unchanged (or not alignable)."""
    # Detect shape
    n_pipes = [ln.count("|") for ln in block]
    is_pseudo = all(p == 2 for p in n_pipes)
    rows = []
    if is_pseudo:
        # find separator row (dash runs) for boundaries
        sep_idx = None
        for i, ln in enumerate(block):
            runs = DASH_RUN.findall(ln)
            if len(runs) >= 2 and all(len(r) >= 2 for r in runs):
                sep_idx = i
                break
        if sep_idx is None:
            return None
        bnds = pseudo_boundaries(block[sep_idx])
        if not bnds:
            return None
        rows = [split_pseudo_row(ln, bnds) for ln in block]
    else:
        rows = [split_real_row(ln) for ln in block]

    # Normalize column count to the widest row
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]

    # Column widths: content width per column (separator dashes follow content)
    sep_indices = [i for i, r in enumerate(rows) if is_sep_row(r)]
    widths = []
    for c in range(ncols):
        w = 0
        for i, r in enumerate(rows):
            if i in sep_indices:
                continue  # separator width derived from content below
            w = max(w, len(r[c]))
        widths.append(max(w, 1))

    # Separator cells span the content width of their column
    out = []
    for r in rows:
        cells_out = []
        for c, cell in enumerate(r):
            if is_sep_row([cell]):
                # rebuild dash run to column width, preserving alignment colons
                if cell.startswith(":") and cell.endswith(":") and len(cell) >= 3:
                    dash = ":" + "-" * max(widths[c] - 2, 1) + ":"
                elif cell.startswith(":"):
                    dash = ":" + "-" * max(widths[c] - 1, 1)
                elif cell.endswith(":"):
                    dash = "-" * max(widths[c] - 1, 1) + ":"
                else:
                    dash = "-" * max(widths[c], 1)
                cells_out.append(dash)
            else:
                cells_out.append(cell.ljust(widths[c]))
        out.append("| " + " | ".join(cells_out) + " |")

    if out == block:
        return None
    return out


def fix_file(path: pathlib.Path) -> tuple[int, int]:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return (0, 0)
    if "\r\n" in text:
        text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    changed_blocks = 0
    changed_lines = 0
    out = []
    i = 0
    n = len(lines)
    while i < n:
        if is_table_line(lines[i]):
            j = i
            block = []
            while j < n and is_table_line(lines[j]):
                block.append(lines[j].rstrip())
                j += 1
            new_block = align_table(block)
            if new_block is not None:
                changed_blocks += 1
                changed_lines += sum(1 for a, b in zip(block, new_block) if a != b)
                out.extend(new_block)
            else:
                out.extend(block)
            i = j
        else:
            out.append(lines[i])
            i += 1
    new_text = "\n".join(out)
    if new_text != text:
        if APPLY:
            path.write_text(new_text, encoding="utf-8", newline="\n")
        return (changed_blocks, changed_lines)
    return (0, 0)


def main() -> int:
    total_blocks = 0
    total_lines = 0
    affected = 0
    for p in files:
        b, l = fix_file(p)
        if b:
            affected += 1
            total_blocks += b
            total_lines += l
            if APPLY:
                print(f"{p.name}: blocks={b} lines={l}")
    print(f"---\n{'APPLIED' if APPLY else 'DRY-RUN'}: files_affected={affected} blocks_changed={total_blocks} lines_changed={total_lines}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
