#!/usr/bin/env python3
"""Read-only prompt-quality slice analysis for a Hermes prompts/ library.

Scans *.prompt.md (optionally a numeric slice of the sorted list, or an
explicit slice-file list), parses frontmatter WITHOUT external deps, scores
each prompt on a fixed weakness rubric, and resolves every templates/...
reference against the real templates/ tree to flag dead includes.

Strictly read-only. Pass --check-readonly to assert SHA-256 of every scanned
.prompt.md is byte-identical before vs after the run (proves non-destructive).

Usage:
  python prompt_quality_slice.py --dir "C:/Users/Alexa/AppData/Local/hermes/prompts"
  python prompt_quality_slice.py --dir "..." --slice-start 141 --slice-end 211
  python prompt_quality_slice.py --dir "..." --slice-file slice3.txt --top 15
  python prompt_quality_slice.py --dir "..." --check-readonly
"""
import os, re, sys, argparse, hashlib

CANON = {
    'goal': ('goal', 'objective', 'purpose'),
    'context': ('context',),
    'workflow': ('workflow', 'steps', 'phase', 'process', 'procedure', 'approach'),
    'rules': ('rule', 'guideline', 'constraint', "don't", 'do not'),
    'verification': ('verif', 'validation', 'check', 'test'),
}

def parse_frontmatter(text):
    """Return (fm_dict, body). Dependency-free top-level key extraction."""
    fm = {}
    body = text
    if text.startswith('---'):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.DOTALL)
        if m:
            fmb, body = m.group(1), m.group(2)
            desc = re.search(r'^description:\s*(.+)$', fmb, re.MULTILINE)
            fm['description'] = desc.group(1).strip().strip('"\'') if desc else ''
            tags = re.search(r'^tags:\s*\[([^\]]*)\]', fmb, re.MULTILINE)
            if tags:
                fm['tags'] = [t.strip().strip('"\'') for t in tags.group(1).split(',') if t.strip()]
            else:
                blk = re.search(r'^tags:\s*\n((?:[ \t]*-.+\n)+)', fmb, re.MULTILINE)
                fm['tags'] = [t.strip()[1:].strip().strip('"\'') for t in blk.group(1).splitlines()] if blk else []
            plan = re.search(r'^plan:\s*(\S.*)$', fmb, re.MULTILINE)
            plan_block = re.search(r'^plan:\s*\n', fmb, re.MULTILINE)
            if plan:
                fm['plan'] = plan.group(1).strip()
            elif plan_block:
                fm['plan'] = '[block]'
            else:
                fm['plan'] = ''
            fmt = re.search(r'^formatter:\s*(\S.*)$', fmb, re.MULTILINE)
            fm['formatter'] = fmt.group(1).strip() if fmt else ''
    return fm, body

def resolve_tmpl(base, t):
    p = os.path.join(base, t.replace('/', os.sep))
    if t.endswith('/'):
        return os.path.isdir(p)
    if os.path.isfile(p):
        return True
    if '*' in t or '...' in t:
        return None  # pattern, unknown
    return False

def analyze(path, prompts_dir):
    name = os.path.basename(path)
    text = open(path, encoding='utf-8', errors='replace').read()
    fm, body = parse_frontmatter(text)
    bl = body.lower()
    has_desc = bool(fm.get('description'))
    has_tags = bool(fm.get('tags'))
    has_plan = bool(fm.get('plan')) and fm['plan'] not in ('', '[]', '[]')
    has_fmt = bool(fm.get('formatter'))
    has_do = bool(re.search(r"\b(do|don'?t|do not|never|always|must|avoid|ensure)\b", bl))
    has_acc = bool(re.search(r'acceptance criteria|definition of done|done when|success criteria', bl))
    has_ver = bool(re.search(r'verif|check that|confirm that|test that|run .*and confirm|self[- ]?check', bl))
    headers = re.findall(r'^#{1,3}\s+(.+)$', body, re.MULTILINE)
    htext = ' | '.join(headers).lower()
    sec = {k: any(c in htext for c in keys) for k, keys in CANON.items()}
    tmpl = re.findall(r'(templates/[^\s\)\]\"\'`]+)', body)
    dead = []
    for t in set(tmpl):
        if '*' in t or '...' in t or t.endswith('/'):
            continue
        if not resolve_tmpl(prompts_dir, t):
            dead.append(t)
    lines = [l for l in body.splitlines() if l.strip()]
    n_lines = len(lines)
    weak = []
    if not has_plan: weak.append('missing plan')
    if not has_acc: weak.append('no acceptance criteria')
    if not sec['goal']: weak.append('no Goal section')
    if not sec['workflow']: weak.append('no Workflow/Phases')
    if not sec['rules']: weak.append('no Rules section')
    if not has_do: weak.append("no explicit Do/Don't rules")
    if not has_ver: weak.append('no verification step')
    if dead: weak.append('dead template refs')
    if n_lines < 20: weak.append('very thin (<20 lines)')
    elif n_lines < 30: weak.append('thin (<30 lines)')
    return dict(name=name, score=len(weak), weak=weak, n_lines=n_lines, n_hdr=len(headers),
                dead=dead, has_plan=has_plan, has_acc=has_acc, **sec,
                has_tags=has_tags, has_fmt=has_fmt, has_do=has_do, has_ver=has_ver)

def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(8192), b''):
            h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', default='C:/Users/Alexa/AppData/Local/hermes/prompts')
    ap.add_argument('--slice-start', type=int, default=1, help='1-indexed inclusive start of sorted slice')
    ap.add_argument('--slice-end', type=int, default=0, help='1-indexed inclusive end (0 = last)')
    ap.add_argument('--slice-file', default='', help='explicit newline list of absolute paths')
    ap.add_argument('--top', type=int, default=0, help='print only top-N weakest')
    ap.add_argument('--check-readonly', action='store_true', help='assert SHA256 unchanged before/after')
    a = ap.parse_args()

    if a.slice_file:
        with open(a.slice_file) as f:
            files = [l.strip() for l in f if l.strip()]
    else:
        allf = [os.path.join(a.dir, f) for f in os.listdir(a.dir) if f.endswith('.prompt.md')]
        allf.sort()
        s, e = a.slice_start, (a.slice_end or len(allf))
        files = allf[s-1:e]
    if not files:
        print('no files selected'); sys.exit(1)

    before = {p: sha256(p) for p in files} if a.check_readonly else {}
    rows = [analyze(p, a.dir) for p in files]
    after = {p: sha256(p) for p in files} if a.check_readonly else {}

    rows.sort(key=lambda r: (-r['score'], r['name']))
    print("=== WEAKEST (score desc) ===")
    for r in (rows[:a.top] if a.top else rows):
        print(f"{r['score']:2d}  {r['name']:55s} lines={r['n_lines']:3d} hdr={r['n_hdr']:2d} weak={' ; '.join(r['weak'])}")
        if r['dead']:
            print(f"       DEAD: {r['dead']}")
    print(f"\nTotal={len(rows)}  with_plan={sum(1 for r in rows if r['has_plan'])}  with_acc={sum(1 for r in rows if r['has_acc'])}  dead_ref_files={sum(1 for r in rows if r['dead'])}")

    if a.check_readonly:
        diffs = [p for p in files if before[p] != after[p]]
        assert not diffs, f"NON-DESTRUCTIVE CHECK FAILED: {diffs}"
        print("READ-ONLY VERIFIED: 0 files modified.")

if __name__ == '__main__':
    main()
