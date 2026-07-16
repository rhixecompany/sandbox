#!/usr/bin/env python3
import os, re, yaml

base = 'C:/Users/Alexa/AppData/Local/hermes/prompts'
with open('slice3.txt') as f:
    files = [l.strip() for l in f if l.strip()]

def resolve_tmpl(t):
    # t like templates/_shared/rules-core.md or templates/foo/bar.md
    p = os.path.join(base, t.replace('/', os.sep))
    if t.endswith('/'):
        return os.path.isdir(p)
    if os.path.isfile(p):
        return True
    # handle wildcard suffix (e.g. templates/suggest-awesome-github-copilot-*/)
    if '*' in t or '...' in t:
        return None  # unknown
    return False

rows = []
for path in files:
    name = os.path.basename(path)
    text = open(path, encoding='utf-8', errors='replace').read()
    fm = {}
    body = text
    if text.startswith('---'):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.DOTALL)
        if m:
            try: fm = yaml.safe_load(m.group(1)) or {}
            except: fm = {}
            body = m.group(2)
    bl = body.lower()
    has_desc = isinstance(fm.get('description'), str) and fm['description'].strip()!=''
    tags = fm.get('tags'); has_tags = isinstance(tags, list) and len(tags)>0
    has_plan = bool(fm.get('plan')) and str(fm.get('plan')).strip()!='' and str(fm.get('plan'))!='[]'
    has_fmt = bool(fm.get('formatter'))
    has_do = bool(re.search(r"\b(do|don'?t|do not|never|always|must|avoid|ensure|do not)\b", bl))
    has_acc = bool(re.search(r'acceptance criteria|acceptance\b|definition of done|done when|success criteria|definition of done', bl))
    has_ver = bool(re.search(r'verif|check that|confirm that|test that|run .*and confirm|self[- ]?check', bl))
    headers = re.findall(r'^#{1,3}\s+(.+)$', body, re.MULTILINE)
    htext = ' | '.join(headers).lower()
    has_goal = any(k in htext for k in ['goal','objective','purpose'])
    has_ctx = 'context' in htext
    has_wf = any(k in htext for k in ['workflow','steps','phase','process','procedure','approach'])
    has_rules = any(k in htext for k in ['rule','guideline','constraint',"don't",'do not'])
    has_vsec = any(k in htext for k in ['verif','validation','check','test'])
    tmpl = re.findall(r'(templates/[^\s\)\]\"\'`]+)', body)
    dead = []
    for t in set(tmpl):
        if '*' in t or '...' in t or t.endswith('/'):
            continue
        if not resolve_tmpl(t):
            dead.append(t)
    lines = [l for l in body.splitlines() if l.strip()]
    n_lines = len(lines)
    # score: count weaknesses
    weak = []
    if not has_plan: weak.append('missing plan')
    if not has_acc: weak.append('no acceptance criteria')
    if not has_goal: weak.append('no Goal section')
    if not has_wf: weak.append('no Workflow/Phases')
    if not has_rules: weak.append('no Rules section')
    if not has_do: weak.append('no explicit Do/Don\'t rules')
    if not has_ver: weak.append('no verification step')
    if dead: weak.append('dead template refs')
    if n_lines < 20: weak.append('very thin (<20 lines)')
    elif n_lines < 30: weak.append('thin (<30 lines)')
    score = len(weak)
    rows.append(dict(name=name, score=score, weak=weak, n_lines=n_lines, dead=dead,
                     has_plan=has_plan, has_acc=has_acc, has_goal=has_goal, has_wf=has_wf,
                     has_rules=has_rules, has_do=has_do, has_ver=has_ver, has_ctx=has_ctx,
                     has_vsec=has_vsec, n_hdr=len(headers)))

rows.sort(key=lambda r: (-r['score'], r['name']))
print("=== WEAKEST (score desc) ===")
for r in rows:
    print(f"{r['score']:2d}  {r['name']:55s} lines={r['n_lines']:3d} hdr={r['n_hdr']:2d} weak={' ; '.join(r['weak'])}")
    if r['dead']:
        print(f"       DEAD: {r['dead']}")
print(f"\nTotal={len(rows)}  with_plan={sum(1 for r in rows if r['has_plan'])}  with_acc={sum(1 for r in rows if r['has_acc'])}")
