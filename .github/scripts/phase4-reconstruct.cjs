const fs = require('fs');
const path = require('path');
const root = 'C:/Users/Alexa/Desktop/SandBox';
const targets = [
  'scripts/batch_skill_judge.py',
  'scripts/batch_remediate.py',
  'scripts/benchmark_models.py',
  'scripts/test_models.py',
  'docs/dedupe-report.md',
  'judge_results/remediation_report.md',
  'docs/consolidation-report.md',
  'docs/final-verification.md',
  'prompts/templates/test-providers-models/phase_0_auth__provider_invento.md',
  'prompts/templates/test-providers-models/phase_1_model_catalog_discover.md'
];
const results = [];
for (const rel of targets) {
  const full = path.join(root, rel);
  const exists = fs.existsSync(full);
  let note = exists ? 'exists' : 'missing';
  if (exists) {
    try {
      const stat = fs.statSync(full);
      note += ' ' + stat.size + 'B';
    } catch (e) {
      note += ' stat-error';
    }
  }
  results.push({ rel, exists, note });
}
console.log('TARGET_COUNT ' + targets.length);
for (const r of results) console.log('TARGET ' + r.rel + ' :: ' + r.note);
