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

function repairFrontmatter(text) {
  const lines = text.split(/\r?\n/)
  const openIdx = lines.findIndex((line) => line.trim() === '---')
  if (openIdx < 0) return text

  const closeIdx = lines.findIndex((line, idx) => idx > openIdx && line.trim() === '---')
  if (closeIdx >= 0) return text

  const frontmatterLines = lines.slice(openIdx + 1)
  if (!frontmatterLines.length) return text

  const insertBefore = frontmatterLines.findIndex(
    (line) => line.startsWith('#') || line.startsWith('- ') || line.startsWith('> ')
  )
  const insertAt = insertBefore >= 0 ? openIdx + 1 + insertBefore : openIdx + 1 + frontmatterLines.length
  lines.splice(insertAt, 0, '---')
  return lines.join('\n')
}

const report = { patched: [], skipped: [], errors: [] }
for (const rel of targets) {
  const full = path.join(base, rel)
  if (!fs.existsSync(full)) {
    report.skipped.push(rel)
    continue
  }
  try {
    const raw = fs.readFileSync(full, 'utf8')
    const repaired = repairFrontmatter(raw)
    if (repaired !== raw) {
      fs.writeFileSync(full, repaired, 'utf8')
      report.patched.push(rel)
    } else {
      report.skipped.push(rel)
    }
  } catch (error) {
    report.errors.push({ file: rel, message: error && error.message })
  }
}
fs.writeFileSync('docs/frontmatter-yaml-repair-report.json', JSON.stringify(report, null, 2))
console.log(JSON.stringify(report, null, 2))
