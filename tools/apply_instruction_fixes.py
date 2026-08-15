import os
import re
import yaml

INSTRUCTIONS_DIR = r"C:\Users\Alexa\Desktop\instructions"

ASSIGN_PATTERNS = [re.compile(r"(?i)(api[_-]?key)\s*[:=]\s*([A-Za-z0-9\-\._]{8,})"), re.compile(r"(?i)(secret)\s*[:=]\s*([A-Za-z0-9\-\._]{8,})")]
LONG_BASE64 = re.compile(r"[A-Za-z0-9+/]{40,}={0,2}")

modified_files = []

for root, dirs, files in os.walk(INSTRUCTIONS_DIR):
    for f in files:
        if not f.lower().endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
        original = text
        fm = None
        has_frontmatter = text.startswith('---') and '---' in text[3:]
        if has_frontmatter:
            parts = text.split('---', 2)
            fm_text = parts[1]
            try:
                fm = yaml.safe_load(fm_text)
            except Exception:
                fm = None
        if not fm:
            # insert minimal frontmatter
            front = {
                'description': 'PLACEHOLDER: brief description required. Please update before merging.',
                'applyTo': '**'
            }
            fm_block = '---\n' + yaml.safe_dump(front, default_flow_style=False).strip() + '\n---\n\n'
            text = fm_block + text
        else:
            changed = False
            if 'description' not in fm or (isinstance(fm.get('description'), str) and not fm.get('description').strip()):
                # insert description
                # replace frontmatter block
                fm['description'] = 'PLACEHOLDER: brief description required. Please update before merging.'
                changed = True
            if 'applyTo' not in fm:
                fm['applyTo'] = '**'
                changed = True
            if changed:
                # reconstruct file
                parts = text.split('---',2)
                new_fm = yaml.safe_dump(fm, default_flow_style=False).strip()
                text = '---\n' + new_fm + '\n---' + parts[2]
        # sanitize secrets: replace assignment values
        for pat in ASSIGN_PATTERNS:
            def repl(m):
                key = m.group(1)
                return f"{key}: <REDACTED_PLACEHOLDER>"
            text = pat.sub(repl, text)
        text = LONG_BASE64.sub('<REDACTED_BLOB>', text)

        if text != original:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(text)
            modified_files.append(path)

print('Modified files:')
for p in modified_files:
    print(p)
