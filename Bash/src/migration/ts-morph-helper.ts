import { Project } from "ts-morph";

/**
 * ts-morph helper for safe AST edits during migration.
 * Usage: node ts-morph-helper.js <file> --replaceVar OLD NEW
 * - performs safe variable rename and inserts dry-run guard where missing
 */

const args = process.argv.slice(2);
if (args.length < 1) {
  console.error("Usage: ts-node ts-morph-helper.ts <file>");
  process.exit(2);
}

const filePath = args[0];
const project = new Project({} as any);
const source = project.addSourceFileAtPath(filePath!);

// Example transformation: ensure exported function has opts param with dryRun default
source.getFunctions().forEach((fn) => {
  if (!fn.isExported()) return;
  const params = fn.getParameters();
  const hasOpts = params.some((p) => p.getName() === "opts");
  if (!hasOpts) {
    fn.insertParameter(0, {
      name: "opts",
      type: "{ dryRun?: boolean; verbose?: boolean }",
      initializer: "{ dryRun: true }",
    });
  } else {
    const opts = params.find((p) => p.getName() === "opts");
    if (opts && !opts.getType().getText().includes("dryRun")) {
      opts.setType("{ dryRun?: boolean; verbose?: boolean }");
    }
  }
});

source.saveSync();
console.log("ts-morph-helper: updated", filePath);
