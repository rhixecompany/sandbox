import os, sys, re
from pathlib import Path
root = Path('/c/Users/Alexa/Desktop/SandBox')
required = [
    'docs/phase1-skills-audit.md',
    'docs/phase2-mcp-research-log.md',
    'docs/phase3-hermes-docs-extraction-log.md',
    'docs/phase4-profiles-log.md',
    'docs/phase5-docs-inventory-log.md',
    'docs/phase6-config-hierarchy-audit.md',
]
for rel in required:
    p = root / rel
    print(f'CHECK {rel} EXISTS={p.exists()} SIZE={p.stat().st_size if p.exists() else -1}')
# light heuristic validation
phase1 = root / 'docs/phase1-skills-audit.md'
text = phase1.read_text(encoding='utf-8', errors='replace') if phase1.exists() else ''
print('PHASE1_HAS_TOTAL', 'Total' in text and '664' in text)
config_hits = {
    'CLAUDE.md': False,
    '.cursorrules_exact': False,
    '.vscode_settings': False,
    '.hermes': False,
}
for p in root.rglob('CLAUDE.md'):
    config_hits['CLAUDE.md'] = True
for p in root.rglob('.cursorrules'):
    config_hits['.cursorrules_exact'] = True
for p in root.rglob('settings.json'):
    config_hits['.vscode_settings'] = True
for name in ['.hermes.md', '.hermes', 'AGENTS.md', 'CLAUDE.md']:
    p = root / name
    if p.exists():
        config_hits['.hermes'] = True
        break
for k,v in config_hits.items():
    print('CONFIG', k, v)
print('VALIDATION_COMPLETE')
