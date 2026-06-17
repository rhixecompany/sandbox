import fs from 'fs/promises';
import path from 'path';

const base = 'C:\\Users\\Alexa\\Desktop\\SandBox\\judge_results';
const needsWorkContent = await fs.readFile(path.join(base, 'needs_work_list.txt'), 'utf8');

// Debug: print first few lines raw
const lines = needsWorkContent.split('\n');
console.log('First 3 lines raw:');
for (let i = 0; i < 3 && i < lines.length; i++) {
  console.log(`  [${i}] "${lines[i]}" (len=${lines[i].length})`);
}

// Try different regex patterns
for (const line of lines.slice(0, 3)) {
  if (!line.trim()) continue;
  const m1 = line.match(/^\d+\|\d+\s+(.+)$/);
  const m2 = line.match(/^\d+\|(\d+)\s+(.+)$/);
  const m3 = line.match(/^(.+)\|(.+)$/);
  console.log(`Line: "${line}"`);
  console.log(`  m1: ${m1 ? m1[1] : 'null'}`);
  console.log(`  m2: ${m2 ? `score=${m2[1]}, name=${m2[2]}` : 'null'}`);
  console.log(`  m3: ${m3 ? `a=${m3[1]}, b=${m3[2]}` : 'null'}`);
}
