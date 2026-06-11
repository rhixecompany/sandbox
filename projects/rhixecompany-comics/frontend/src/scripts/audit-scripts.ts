#!/usr/bin/env tsx
/**
 * Audit all scripts for flag consistency and standard patterns
 * Generates detailed report of what needs updating
 */

import { readFileSync } from "node:fs";
import * as path from "node:path";

import { globSync } from "glob";

interface AuditResult {
  file: string;
  flags: {
    dryRun: boolean;
    json: boolean;
    verbose: boolean;
    yes: boolean;
  };
  issues: string[];
  uses: {
    chalk: boolean;
    commander: boolean;
    confirmAction: boolean;
    logger: boolean;
  };
}

function analyzeScript(filePath: string): AuditResult {
  const content = readFileSync(filePath, "utf-8");
  const fileName = path.basename(filePath);

  const flags = {
    dryRun: /--dry-run|dryRun|dry.run/i.test(content),
    verbose: /--verbose|verbose/i.test(content),
    yes: /--yes|yes/i.test(content),
    json: /--json|json/i.test(content),
  };

  const uses = {
    logger: /from ["'].*?\/shared\/logger["']|Logger|logger\./i.test(content),
    confirmAction: /from ["'].*?\/shared\/confirmAction["']|confirmAction/i.test(content),
    chalk: /import chalk|from ["']chalk["']/i.test(content),
    commander: /from ["']commander["']|new Command/i.test(content),
  };

  const issues: string[] = [];

  // Check for standard flag compliance
  if ((!flags.dryRun && content.includes("delete")) || content.includes("remove")) {
    issues.push("Destructive operation detected but --dry-run flag missing");
  }
  if (!flags.verbose) {
    issues.push("Missing --verbose flag for detailed output");
  }
  if (!flags.json) {
    issues.push("Missing --json flag for machine-readable output");
  }
  if (!flags.yes && (uses.confirmAction || content.includes("confirm"))) {
    issues.push("Confirmation logic detected but --yes flag missing");
  }

  // Check for standard utilities
  if (!uses.logger && uses.chalk) {
    issues.push("Uses chalk but should use Logger class instead");
  }
  if (!uses.logger && /console\.log|console\.warn|console\.error/i.test(content)) {
    issues.push("Uses raw console instead of Logger class");
  }

  // Check for parsing pattern
  if (!uses.commander && !content.includes("parseArgs()")) {
    issues.push("Missing standard flag parsing (Commander or parseArgs)");
  }

  return {
    file: fileName,
    flags,
    uses,
    issues,
  };
}

async function auditAllScripts() {
  const scripts = globSync("src/scripts/**/*.ts", {
    ignore: ["src/scripts/shared/**", "src/scripts/audit-scripts.ts"],
  });

  console.log("\n");
  console.log("═══════════════════════════════════════════════════════════════════");
  console.log("  📊 SCRIPT AUDIT REPORT");
  console.log("═══════════════════════════════════════════════════════════════════\n");

  const results: AuditResult[] = [];
  const flagCompliance = { compliant: 0, partial: 0, missing: 0 };

  for (const script of scripts) {
    const result = analyzeScript(script);
    results.push(result);

    const flagsPresent = Object.values(result.flags).filter(Boolean).length;
    if (flagsPresent === 4) flagCompliance.compliant++;
    else if (flagsPresent >= 2) flagCompliance.partial++;
    else flagCompliance.missing++;
  }

  // Summary
  console.log(`📈 TOTAL: ${scripts.length} scripts analyzed\n`);
  console.log(`  ✅ Fully compliant (all 4 flags):  ${flagCompliance.compliant} scripts`);
  console.log(`  🟡 Partial (2-3 flags):           ${flagCompliance.partial} scripts`);
  console.log(`  ❌ Missing flags (0-1 flags):      ${flagCompliance.missing} scripts`);

  console.log("\n═══════════════════════════════════════════════════════════════════\n");

  // Detailed results
  console.log("DETAILED RESULTS:\n");

  const sortedByCompliance = results.sort(
    (a, b) => Object.values(b.flags).filter(Boolean).length - Object.values(a.flags).filter(Boolean).length
  );

  for (const result of sortedByCompliance) {
    const flagsPresent = Object.values(result.flags).filter(Boolean).length;
    const status = flagsPresent === 4 ? "✅" : flagsPresent >= 2 ? "🟡" : "❌";

    console.log(`${status} ${result.file.padEnd(35)} [${flagsPresent}/4 flags]`);

    if (result.issues.length > 0) {
      for (const issue of result.issues.slice(0, 2)) {
        console.log(`     • ${issue}`);
      }
      if (result.issues.length > 2) {
        console.log(`     • +${result.issues.length - 2} more issues`);
      }
    }
    console.log();
  }

  console.log("═══════════════════════════════════════════════════════════════════\n");

  // Group by issues
  const issueMap = new Map<string, string[]>();
  for (const result of results) {
    for (const issue of result.issues) {
      if (!issueMap.has(issue)) {
        issueMap.set(issue, []);
      }
      issueMap.get(issue)!.push(result.file);
    }
  }

  console.log("ISSUES BY CATEGORY:\n");
  const sortedIssues = Array.from(issueMap.entries()).sort((a, b) => b[1].length - a[1].length);
  for (const [issue, files] of sortedIssues) {
    console.log(`⚠️  ${issue} (${files.length} scripts)`);
    // console.log(`     ${files.slice(0, 3).join(", ")}${files.length > 3 ? ` +${files.length - 3} more` : ""}`);
    console.log();
  }

  console.log("═══════════════════════════════════════════════════════════════════\n");
}

auditAllScripts().catch(console.error);
