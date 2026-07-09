const fs = require('fs');
const path = require('path');
const rootPrompts = 'C:/Users/Alexa/Desktop/SandBox/prompts';
const rootHermes = path.join(process.env.USERPROFILE || 'C:\Users\Alexa', 'AppData/Local/hermes');
const promptCandidates = [];
const memoryCandidates = [];
function walk(dir, rel='') {
  if (!fs.existsSync(dir)) return;
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const cur = rel ? rel + '/' + name : name;
    if (name === '.git') continue;
    const stat = fs.statSync(full);
    if (stat.isDirectory()) walk(full, cur);
    else {
      if (cur.startsWith('prompts/') && name.endsWith('.prompt.md')) promptCandidates.push(cur);
      if ((cur.startsWith('profiles/') || cur.startsWith('memories/') || cur.startsWith('USER.md') || cur.startsWith('SOUL.md') || cur.startsWith('MEMORY.md')) && /\.(md|MD)$/.test(name)) memoryCandidates.push(cur);
    }
  }
}
walk(rootPrompts);
walk(rootHermes);
const subset = (arr) => arr.filter((_, i) => i < 8).join('\n');
console.log('PROMPT_COUNT ' + promptCandidates.length);
console.log('MEMORY_COUNT ' + memoryCandidates.length);
console.log('COMBINED_COUNT ' + (promptCandidates.length + memoryCandidates.length));
console.log('--- PROMPT SAMPLE ---');
console.log(subset(promptCandidates) || '(none)');
console.log('--- MEMORY SAMPLE ---');
console.log(subset(memoryCandidates.map((x) => '~/.hermes/' + x.replace(/^.*?AppData\/Local\/hermes\//, ''))) || '(none)');
