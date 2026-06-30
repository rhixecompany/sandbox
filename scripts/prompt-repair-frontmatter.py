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
pat_close_merge = re.compile(r'^---\s*\n---\s*#', re.MULTILINE)
fixed=[]
for name in files:
  path=root/name
  text=path.read_text(encoding='utf-8')
  new=pat_open_merge.sub('---\n#', text, count=1)
  if new==text:
    new=pat_close_merge.sub('---\n#', text, count=1)
  if new != text:
    path.write_text(new, encoding='utf-8')
    fixed.append(name)
print('fixed_count', len(fixed))
for n in fixed:
  print(n)
