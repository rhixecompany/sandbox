import fs from 'fs/promises';
import path from 'path';

const base = 'C:\\Users\\Alexa\\Desktop\\SandBox\\judge_results';
const tsvContent = await fs.readFile(path.join(base, 'all_results.tsv'), 'utf8');
const needsWorkContent = await fs.readFile(path.join(base, 'needs_work_list.txt'), 'utf8');

// Parse needs work list - get (score, name) pairs
const needsWorkEntries = new Map(); // name -> score from needs_work_list
for (const line of needsWorkContent.split('\n')) {
  if (!line.trim()) continue;
  const match = line.match(/^(\d+)\s+(.+)$/);
  if (match) {
    const score = parseInt(match[1]);
    const name = match[2].trim();
    needsWorkEntries.set(name, score);
  }
}

console.log(`Needs work entries: ${needsWorkEntries.size}`);
for (const [name, score] of needsWorkEntries) {
  if (score >= 80) {
    console.log(`  WARNING: ${name} has score ${score} (>=80)`);
  }
}

// Parse TSV - only include skills from needs_work_list
const skillMap = new Map();
for (const line of tsvContent.split('\n')) {
  if (!line.trim()) continue;
  const parts = line.split('|');
  if (parts.length < 10) continue;
  
  const name = parts[0].trim();
  const tsvPath = parts[1].trim();
  const score = parseInt(parts[2].trim());
  const dim1 = parseInt(parts[4].trim());
  const dim2 = parseInt(parts[5].trim());
  const dim3 = parseInt(parts[6].trim());
  const dim4 = parseInt(parts[7].trim());
  const dim5 = parseInt(parts[8].trim());
  const lines = parseInt(parts[9].trim());
  
  if (!needsWorkEntries.has(name)) continue;
  
  // Keep the entry with the highest score for each unique skill
  if (!skillMap.has(name) || score > skillMap.get(name).score) {
    skillMap.set(name, { name, path: tsvPath, score, dim1, dim2, dim3, dim4, dim5, lines });
  }
}

// Convert to array and sort by score ascending (worst first)
const skills = Array.from(skillMap.values()).sort((a, b) => a.score - b.score);

// Filter to only score <= 79
const filtered = skills.filter(s => s.score <= 79);
console.log(`\nFiltered to score <= 79: ${filtered.length} skills`);

// Save as JSON
await fs.writeFile(path.join(base, 'remediation_list.json'), JSON.stringify(filtered, null, 2));
console.log('Saved remediation_list.json');

// Save text list
const output = filtered.map(s => 
  `${s.score}|${s.name}|${s.path}|${s.dim1}|${s.dim2}|${s.dim3}|${s.dim4}|${s.dim5}|${s.lines}`
).join('\n');
await fs.writeFile(path.join(base, 'remediation_list.txt'), output);
console.log('Saved remediation_list.txt');

console.log('\nScore distribution:');
const dist = new Map();
for (const s of filtered) {
  dist.set(s.score, (dist.get(s.score) || 0) + 1);
}
for (const [score, count] of [...dist.entries()].sort((a,b) => a[0]-b[0])) {
  console.log(`  Score ${score}: ${count} skills`);
}
