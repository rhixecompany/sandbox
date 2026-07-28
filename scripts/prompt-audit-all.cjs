const fs = require('fs');
const path = require('path');
const root = 'C:/Users/Alexa/Desktop/SandBox/prompts';
const files = fs.readdirSync(root).filter((f) => f.endsWith('.prompt.md'));
const issues = [];
for (const file of files) {
  const full = path.join(root, file);
  const content = fs.readFileSync(full, 'utf8');
  const lines = content.split(/\r?\n/);
  let broken = false;
  let reasons = [];
  if (!content.startsWith('---')) {
    broken = true;
    reasons.push('missing-frontmatter-start');
  } else {
    const end = content.indexOf('\n---', 3);
    if (end === -1) {
      broken = true;
      reasons.push('missing-frontmatter-end');
    } else {
      const fm = content.slice(3, end).trim();
      if (fm.length === 0) reasons.push('empty-frontmatter');
      if (fm.startsWith('{') || fm.startsWith('[')) {
        broken = true;
        reasons.push('frontmatter-is-json');
      }
    }
  }
  if (content.includes('\ufffd') || content.includes('\u0000')) {
    broken = true;
    reasons.push('null-bytes');
  }
  if (file === 'pl.md' || file.endsWith('.prompt.txt')) {
    broken = true;
    reasons.push('non-standard-extension');
  }
  if (broken) issues.push({ file, reasons });
}
console.log('PROMPT_COUNT ' + files.length);
console.log('ISSUE_COUNT ' + issues.length);
for (const row of issues) {
  console.log('ISSUE ' + row.file + ' :: ' + row.reasons.join(','));
}
