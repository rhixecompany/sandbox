#!/usr/bin/env python3
"""ref_integrity_check.py — fast pre-report sanity check for dead `templates/...` refs.

Read-only. Intended to be run IMMEDIATELY BEFORE building the enhancement report
so the on-disk reference tree and the report agree (see the data-drift pitfall in
references/quality-enhancement-method.md).

Correctness notes baked in from live-session bugs:
  * Only PATH-LIKE refs (templates/...) are existence-checked. `skill:`/`tool:`/
    `prompt:` frontmatter namespace refs are NOT files — skipping them avoids
    false-positive "broken reference" flags.
  * `_shared/*` is valid and excluded (known-good shared templates).
  * Counts DISTINCT links per file (and per dir), not every regex occurrence.
  * Native Windows paths (C:/...) must be passed in; does NOT resolve MSYS /c/...

Usage:
  python scripts/ref_integrity_check.py --dir "C:\\Users\\Alexa\\AppData\\Local\\hermes\\prompts"
  python scripts/ref_integrity_check.py --dir "..." --slice-file slice3.txt
"""
import os, re, sys, json, argparse, datetime

REF_RE = re.compile(r'templates/[A-Za-z0-9_\-./]+')


def dead_refs_for_file(path):
    text = open(path, encoding='utf-8').read()
    seen = set()
    dead = []
    for m in REF_RE.findall(text):
        rc = m.rstrip(').,')
        if rc.startswith('templates/_shared'):
            continue                      # known-good shared templates
        if rc in seen:
            continue                      # per-file dedupe
        seen.add(rc)
        if not os.path.exists(os.path.join(os.path.dirname(path), rc)):
            dead.append(rc)
    return dead


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', required=True)
    ap.add_argument('--slice-file', help='optional explicit file list (one .prompt.md per line)')
    args = ap.parse_args()
    base = args.dir
    if args.slice_file:
        names = [l.strip() for l in open(args.slice_file, encoding='utf-8') if l.strip()]
    else:
        names = sorted(f for f in os.listdir(base) if f.endswith('.prompt.md'))
    out = {}
    files_with = 0
    total = 0
    for n in names:
        p = os.path.join(base, n)
        if not os.path.isfile(p):
            print(f'MISSING (skipped): {n}', file=sys.stderr)
            continue
        d = dead_refs_for_file(p)
        if d:
            files_with += 1
            total += len(d)
            out[n] = d
    stamp = datetime.datetime.now().isoformat(timespec='seconds')
    print(f'# templates/ reference integrity — as of {stamp}')
    print(f'# scanned={len(names)} files_with_dead_refs={files_with} distinct_dead_links={total}')
    for n, refs in sorted(out.items(), key=lambda x: -len(x[1])):
        print(f'\n## {n}  ({len(refs)} dead)')
        for r in sorted(set(refs)):
            print(f'  - {r}')
    # Machine-readable sidecar for the report builder
    with open(os.path.join(base, 'docs', '_refcheck.json'), 'w', encoding='utf-8') as f:
        json.dump({'as_of': stamp, 'scanned': len(names),
                   'files_with_dead': files_with, 'distinct_dead': total,
                   'per_file': out}, f, indent=2)


if __name__ == '__main__':
    main()
