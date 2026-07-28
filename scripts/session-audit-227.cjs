const Database = require('better-sqlite3');
const fs = require('fs');
const os = require('os');
const path = require('path');
const home = os.homedir();
const dbPath = path.join(home, 'AppData', 'Local', 'hermes', 'state.db');
if (!fs.existsSync(dbPath)) { console.error('Missing DB: ' + dbPath); process.exit(1); }
const db = new Database(dbPath, { readonly: true });
const rows = db.prepare('SELECT id, title, source, model, started_at, ended_at, message_count, tool_call_count, api_call_count, input_tokens, output_tokens FROM sessions ORDER BY started_at ASC').all();
const stats = db.prepare(`SELECT 
  COUNT(*) as total_sessions,
  COALESCE(SUM(message_count),0) as total_messages,
  COALESCE(SUM(tool_call_count),0) as total_tools,
  COALESCE(SUM(api_call_count),0) as total_api_calls,
  COALESCE(SUM(input_tokens),0) as total_input_tokens,
  COALESCE(SUM(output_tokens),0) as total_output_tokens,
  MIN(started_at) as first_ts,
  MAX(started_at) as last_ts
FROM sessions`).get();
const byModel = db.prepare('SELECT model, COUNT(*) as cnt FROM sessions GROUP BY model ORDER BY cnt DESC').all();
const bySource = db.prepare('SELECT source, COUNT(*) as cnt FROM sessions GROUP BY source ORDER BY cnt DESC').all();
const byDate = db.prepare("SELECT date(started_at,'unixepoch') as d, COUNT(*) as cnt FROM sessions GROUP BY d ORDER BY d ASC").all();
const top20 = db.prepare('SELECT id, title, message_count, tool_call_count, source, model FROM sessions WHERE title IS NOT NULL ORDER BY message_count DESC LIMIT 20').all();
const outPath = path.join(process.cwd(), 'SESSION_AUDIT_227.md');
const fmt = (n) => Number(n||0).toLocaleString();
const fmtDate = (ts) => { if (!ts) return '-'; const d = new Date(Number(ts)*1000); return d.toISOString().replace('T',' ').replace(/\.\d+Z$/,' UTC'); };
let md = [];
md.push('# Session History Audit (227 sessions)\n');
md.push('> Generated from: ' + dbPath);
md.push('> Count: ' + rows.length + '.\n');
md.push('## Overview');
md.push('| Metric | Value |');
md.push('|---|---|');
md.push('| Sessions | ' + fmt(stats.total_sessions) + ' |');
md.push('| Messages | ' + fmt(stats.total_messages) + ' |');
md.push('| Tool Calls | ' + fmt(stats.total_tools) + ' |');
md.push('| API Calls | ' + fmt(stats.total_api_calls) + ' |');
md.push('| Input Tokens | ' + fmt(stats.total_input_tokens) + ' |');
md.push('| Output Tokens | ' + fmt(stats.total_output_tokens) + ' |');
md.push('| First Seen | ' + fmtDate(stats.first_ts) + ' |');
md.push('| Last Seen | ' + fmtDate(stats.last_ts) + ' |\n');
md.push('## Source Breakdown');
md.push('| Source | Count |');
md.push('|---|---|');
for (const r of bySource) md.push('| ' + (r.source||'(null)') + ' | ' + fmt(r.cnt) + ' |');
md.push('');
md.push('## Model Distribution');
md.push('| Model | Count |');
md.push('|---|---|');
for (const r of byModel) md.push('| ' + (r.model||'(null)') + ' | ' + fmt(r.cnt) + ' |');
md.push('');
md.push('## Daily Activity');
md.push('| Date | Sessions |');
md.push('|---|---|');
for (const r of byDate) md.push('| ' + r.d + ' | ' + fmt(r.cnt) + ' |');
md.push('');
md.push('## Top 20 Largest Sessions');
md.push('| Session ID | Title | Source | Model | Messages | Tools |');
md.push('|---|---|---|---|---|---|');
for (const r of top20) {
  const title = (r.title||'').replace(/\|/g,'\|').trim();
  const short = title.length > 70 ? title.slice(0,67) + '...' : title;
  md.push('| ' + r.id + ' | ' + (short||'(untitled)') + ' | ' + (r.source||'') + ' | ' + (r.model||'') + ' | ' + fmt(r.message_count) + ' | ' + fmt(r.tool_call_count) + ' |');
}
md.push('');
md.push('## All Sessions');
md.push('| # | Session ID | Title | Source | Model | Started | Messages | Tools |');
md.push('|---|---|---|---|---|---|---|---|');
rows.forEach((r, idx) => {
  const title = (r.title||'').replace(/\|/g,'\|').trim();
  const short = title.length > 72 ? title.slice(0,69) + '...' : title;
  md.push('| ' + (idx+1) + ' | ' + r.id + ' | ' + (short||'(untitled)') + ' | ' + (r.source||'') + ' | ' + (r.model||'') + ' | ' + fmtDate(r.started_at) + ' | ' + fmt(r.message_count) + ' | ' + fmt(r.tool_call_count) + ' |');
});
fs.writeFileSync(outPath, md.join('\n'));
console.log('Wrote: ' + outPath);
console.log('Sessions: ' + rows.length);
console.log('Total messages: ' + fmt(stats.total_messages));
