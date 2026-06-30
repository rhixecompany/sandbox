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
pat = re.compile(r'^---\s*\n---\s*#', re.MULTILINE)
for name in files:
  p=root/name
  txt=p.read_text(encoding='utf-8')
  fixed = pat.sub('---\n#', txt, count=1)
  if fixed != txt:
    p.write_text(fixed, encoding='utf-8')
    print('FIXED', name)
print('done')
