/*
 * ts-morph helper template for AST-safe transforms
 * Usage: node ts-morph-helper.js <file>
 */

import { Project } from 'ts-morph';

const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: ts-node ts-morph-helper.ts <file>');
  process.exit(2);
}

const p = new Project();
const sf = p.addSourceFileAtPath(filePath);

sf.getFunctions().forEach(fn => {
  if (!fn.isExported()) return;
  const params = fn.getParameters();
  const hasOpts = params.some(p => p.getName() === 'opts');
  if (!hasOpts) {
    fn.insertParameter(0, {
      name: 'opts',
      type: '{ dryRun?: boolean; verbose?: boolean }',
      initializer: '{ dryRun: true }'
    });
  }
});

sf.saveSync();
console.log('updated', filePath);
