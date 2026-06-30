from pathlib import Path
import re

root = Path('/c/Users/Alexa/Desktop/SandBox/prompts')
files = [
  'apple-appstore-reviewer.prompt.md',
  'bigquery-pipeline-audit.prompt.md',
  'comicwise-development.prompt.md',
  'create-architectural-decision-record.prompt.md',
  'create-oo-component-documentation.prompt.md',
  'create-technical-spike.prompt.md',
  'dotnet-upgrade.prompt.md',
  'features.prompt.md',
  'github-copilot-starter.prompt.md',
  'mkdocs-translations.prompt.md',
  'model-recommendation.prompt.md',
  'multi-agent-research-template.prompt.md',
  'prompt-management.prompt.md',
  'refactor-method-complexity-reduce.prompt.md',
  'repo.prompt.md',
  'setup-enhanced.prompt.md',
  'setup-nextjs-frontend-stack.prompt.md',
  'setup.prompt.md',
  'suggest-awesome-github-copilot-instructions.prompt.md',
  'suggest-awesome-github-copilot-skills.prompt.md',
  'test-providers-models.prompt.md',
]
pat_open_merge = re.compile(r'^---\s*\n---\s*#', re.MULTILINE)
pat_head_fence = re.compile(r'^---\s*\n(#|\'\'\')(?!/)', re.MULTILINE)
pat_missing_close = re.compile(r'^(---)\s*\n(---\s*\n)?(#|\'\'\')', re.MULTILINE)
pat_merged_fence = re.compile(r'^---\s*\n---\s*#', re.MULTILINE)
pat_extra_fence = re.compile(r'^(---)\s*\n\s*---\s*\n(?!$)', re.MULTILINE)

fixed=[]
for name in files:
  p=root/name
  txt=p.read_text(encoding='utf-8')
  if pat_open_merge.search(txt):
    txt=pat_open_merge.sub('---\n#', txt, count=1)
  if pat_head_fence.search(txt):
    txt=pat_head_fence.sub('---\n\\1', txt, count=1)
  m=pat_extra_fence.search(txt)
  if m:
    txt=txt[:m.start(1)] + m.group(1) + txt[m.end(2):]
  new=pat_merged_fence.sub('---\n#', txt, count=1)
  if new!=txt:
    txt=new
  if txt!=p.read_text(encoding='utf-8'):
    p.write_text(txt, encoding='utf-8')
    fixed.append(name)
print('fixed', len(fixed))
for n in fixed:
  print(n)
