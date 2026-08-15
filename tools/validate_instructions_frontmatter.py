import sys
import os
import re
import yaml
import json

INSTRUCTIONS_DIR = r"C:\Users\Alexa\Desktop\instructions"
REQUIRED = ["description","applyTo"]
# more precise secret detection: assignments or long base64 strings
ASSIGN_PATTERNS = [re.compile(r"(?i)(api[_-]?key)\s*[:=]\s*([A-Za-z0-9\-\._]{8,})"), re.compile(r"(?i)(secret)\s*[:=]\s*([A-Za-z0-9\-\._]{8,})")]
LONG_BASE64 = re.compile(r"[A-Za-z0-9+/]{40,}={0,2}")

results = {}

for root, dirs, files in os.walk(INSTRUCTIONS_DIR):
    for f in files:
        if not f.lower().endswith('.md'):
            continue
        path = os.path.join(root, f)
        status = {"path": path, "ok": True, "errors": [], "warnings": []}
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                text = fh.read()
            fm = None
            if text.startswith('---'):
                parts = text.split('---', 2)
                if len(parts) >= 3:
                    fm_text = parts[1]
                    try:
                        fm = yaml.safe_load(fm_text)
                    except Exception as e:
                        status['ok'] = False
                        status['errors'].append(f'frontmatter_yaml_error: {e}')
            if fm is None:
                status['ok'] = False
                status['errors'].append('missing_frontmatter')
            else:
                for r in REQUIRED:
                    if r not in fm or (isinstance(fm[r], str) and not fm[r].strip()):
                        status['ok'] = False
                        status['errors'].append(f'missing_required:{r}')
                # normalize applyTo
                if 'applyTo' in fm:
                    if isinstance(fm['applyTo'], str):
                        # allow comma-separated
                        arr = [s.strip() for s in fm['applyTo'].split(',') if s.strip()]
                        fm['applyTo'] = arr
                        status['warnings'].append('normalized_applyTo:converted_string_to_array')
                    elif isinstance(fm['applyTo'], list):
                        pass
                    else:
                        status['ok'] = False
                        status['errors'].append('invalid_applyTo_type')
                # check examples section
                if fm.get('examples_section'):
                    # look for Examples header
                    if not re.search(r"^##+\s*Examples", text, re.IGNORECASE | re.MULTILINE):
                        status['ok'] = False
                        status['errors'].append('examples_section_true_but_no_examples_header')
                # detect secrets more precisely
                secret_found = False
                for pat in ASSIGN_PATTERNS:
                    m = pat.search(text)
                    if m:
                        # if value looks like placeholder (e.g., <REDACTED>) ignore
                        val = m.group(2)
                        if val.lower() not in ('<redacted>','<placeholder>','REDACTED','PLACEHOLDER') and len(val) >= 8:
                            secret_found = True
                            break
                if not secret_found and LONG_BASE64.search(text):
                    secret_found = True
                if secret_found:
                    status['ok'] = False
                    status['errors'].append('possible_secret_found')
        except Exception as e:
            status['ok'] = False
            status['errors'].append(f'exception:{e}')
        results[path] = status

out = {"summary": {"total": len(results), "ok": sum(1 for v in results.values() if v['ok']), "fail": sum(1 for v in results.values() if not v['ok'])}, "details": list(results.values())}
print(json.dumps(out, indent=2))
