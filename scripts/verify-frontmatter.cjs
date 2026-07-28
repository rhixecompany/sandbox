const fs = require('fs')
const path = require('path')

const base = process.cwd()
const targets = [
  'Prompts/apple-appstore-reviewer.prompt.md',
  'Prompts/create-github-action-workflow-specification.prompt.md',
  'Prompts/database.prompt.md',
  'Prompts/dev-init.prompt.md',
  'Prompts/features.prompt.md',
  'Prompts/general.prompt.md',
  'Prompts/pl.md',
  'Prompts/repo.prompt.md',
  'Prompts/workspace-consolidate.prompt.md'
]

function analyzeFrontmatter(text) {
  const first60 = text.slice(0, 60)
  const matches = [...text.matchAll(/^---$/gm)]
  const openCount = first60.split(/^---$/gm).length - 1
  const openIdx = text.indexOf('---')
  const closingIdx = text.indexOf('---', openIdx + 3)
  const unclosed = openIdx !== -1 && closingIdx === -1
  const extraBeforeClose = openCount > 2
  const hasDoubleFence = openCount > 2 && !unclosed
  return {
    openCount,
    unclosed,
    hasDoubleFence,
    first60Fences: openCount
  }
}

const results = []
for (const rel of targets) {
  const full = path.join(base, rel)
  if (!fs.existsSync(full)) {
    results.push({ file: rel, exists: false })
    continue
  }
  const raw = fs.readFileSync(full, 'utf8')
  const fm = analyzeFrontmatter(raw)
  const issues = []
  if (fm.unclosed) issues.push('Unclosed frontmatter fence')
  if (fm.hasDoubleFence) issues.push('Double frontmatter fences')
  results.push({ file: rel, exists: true, issues, frontmatter: fm })
}
fs.writeFileSync('docs/frontmatter-gate-report.json', JSON.stringify(results, null, 2))
console.log(JSON.stringify(results, null, 2))
