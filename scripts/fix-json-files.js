#!/usr/bin/env node
import fs from 'fs';
import path from 'path';

const roots = [
  'C:/Users/Alexa/Desktop/SandBox/.vscode',
  'C:/Users/Alexa/Desktop/SandBox',
];

const changed = [];
const failed = [];

function walk(dir, out) {
  if (!fs.existsSync(dir)) return;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (['node_modules', '.git', 'dist', 'build'].includes(entry.name)) continue;
      walk(full, out);
    } else if (entry.isFile() && full.toLowerCase().endsWith('.json')) {
      out.push(full);
    }
  }
}

for (const root of roots) {
  const files = [];
  walk(root, files);
  for (const file of files) {
    try {
      const raw = fs.readFileSync(file, 'utf-8');
      const trimmed = raw.replace(/^\uFEFF/, '').replace(/[ \r]+$/g, '').trimEnd();
      if (!trimmed) {
        fs.writeFileSync(file, '{}\n');
        changed.push(`${file} -> empty object`);
        continue;
      }
      // Preserve empty string for non-config files, otherwise enforce valid JSON.
      let parsed;
      try {
        parsed = JSON.parse(trimmed);
      } catch (err) {
        failed.push(`${file}: ${err.message}`);
        continue;
      }
      const next = JSON.stringify(parsed, null, 2) + '\n';
      if (next !== raw) {
        fs.writeFileSync(file, next);
        changed.push(file);
      }
    } catch (err) {
      failed.push(`${file}: ${err.message}`);
    }
  }
}

console.log('Changed:', changed.length);
for (const item of changed) console.log('-', item);
if (failed.length) {
  console.log('Failed:', failed.length);
  for (const item of failed) console.log('-', item);
} else {
  console.log('All JSON files passed or were repaired.');
}
