
from pathlib import Path
import re

root = Path(r'C:\Users\Alexa\Desktop\SandBox')
prompts_dir = root / 'prompts'
actions_text = """\n## Actions\n\n- Follow the prompt workflow as specified.\n- Produce the requested deliverable(s) in the exact structure requested.\n- Validate output against acceptance criteria before finishing.\n"""

count = 0
for path in sorted(prompts_dir.glob('*.prompt.md')):
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    if '## Actions' in text:
        continue
    if text.startswith('---'):
        m = re.match(r'^---\n.*?\n---\n', text, re.S)
        if m:
            new_text = m.group(0) + '\n' + actions_text + text[m.end():]
        else:
            new_text = actions_text + text
    else:
        new_text = actions_text + text
    path.write_text(new_text, encoding='utf-8')
    count += 1
print('NORMALIZED', count)
