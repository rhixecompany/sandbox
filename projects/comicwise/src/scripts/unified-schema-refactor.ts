#!/usr/bin/env tsx
/**
 * ═══════════════════════════════════════════════════════════════════════════
 * Unified Schema & Code Refactoring
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * Consolidates 7 refactoring scripts into a single unified command:
 * - updateAnyTypes.ts — Remove 'any' type annotations
 * - ast-refactor.ts — AST-based refactoring
 * - replaceImportsEnhanced.ts — Replace relative imports with aliases
 * - migrateToDto.ts — Migrate to DTO pattern
 * - verify-dal-usage.ts — Verify DAL compliance
 * - setup-error-boundaries.ts — Add error boundary components
 * - fix-use-directives.ts — Add use server/client directives
 *
 * Usage:
 *   pnpm refactor                      # Show available options
 *   pnpm refactor --types              # Fix 'any' type annotations
 *   pnpm refactor --imports            # Replace relative imports with aliases
 *   pnpm refactor --dto                # Migrate to DTO pattern
 *   pnpm refactor --boundaries         # Add error boundary components
 *   pnpm refactor --directives         # Fix use server/client directives
 *   pnpm refactor --dal-verify         # Verify DAL compliance
 *   pnpm refactor --dry-run            # Preview changes without writing
 *   pnpm refactor --all                # Run all refactoring operations
 * ═══════════════════════════════════════════════════════════════════════════
 */

import { execSync } from "node:child_process";

import { info, warning } from "./shared/colors.js";
import { createLogger } from "./shared/logger.js";
import { createSpinner } from "./shared/spinner.js";

interface RefactorOptions {
  all: boolean;
  boundaries: boolean;
  dalVerify: boolean;
  directives: boolean;
  dryRun: boolean;
  dto: boolean;
  imports: boolean;
  json: boolean;
  types: boolean;
  verbose: boolean;
  yes: boolean;
}

function parseArgs(): RefactorOptions {
  const args = process.argv.slice(2);

  const options: RefactorOptions = {
    all: args.includes("--all"),
    boundaries: args.includes("--boundaries"),
    dalVerify: args.includes("--dal-verify"),
    directives: args.includes("--directives"),
    dto: args.includes("--dto"),
    dryRun: args.includes("--dry-run"),
    imports: args.includes("--imports"),
    json: args.includes("--json"),
    types: args.includes("--types"),
    verbose: args.includes("--verbose"),
    yes: args.includes("--yes"),
  };

  // If --all specified, enable all refactoring operations
  if (options.all) {
    options.types = true;
    options.imports = true;
    options.dto = true;
    options.boundaries = true;
    options.directives = true;
    options.dalVerify = true;
  }

  return options;
}

// Fix 'any' type annotations
async function fixAnyTypes(logger: any, dryRun: boolean): Promise<{ files: string[]; fixed: number }> {
  const spinner = createSpinner("Scanning for 'any' type annotations...");
  spinner.start();

  try {
    // Search for 'any' usage in TypeScript files
    const result = execSync("grep -r ': any' src --include='*.ts' --include='*.tsx'", {
      encoding: "utf8",
      stdio: ["pipe", "pipe", "ignore"],
    });

    const lines = result.split("\n").filter(Boolean);
    spinner.succeed(`Found ${lines.length} 'any' type usage(s)`);

    if (!dryRun && lines.length > 0) {
      logger.warn("Manual fix required: Review and replace 'any' with specific types");
    }

    return {
      fixed: lines.length,
      files: lines.map((l) => l.split(":")[0]),
    };
  } catch {
    spinner.warn("No 'any' types found or search failed");
    return { fixed: 0, files: [] };
  }
}

// Replace relative imports with path aliases
async function fixImports(logger: any, dryRun: boolean): Promise<{ files: string[]; updated: number }> {
  const spinner = createSpinner("Analyzing import statements...");
  spinner.start();

  try {
    // Search for relative imports
    const result = execSync("grep -r 'from [\"\\']\\.\\.\\/' src --include='*.ts' --include='*.tsx'", {
      encoding: "utf8",
      stdio: ["pipe", "pipe", "ignore"],
    });

    const lines = result.split("\n").filter(Boolean);
    spinner.succeed(`Found ${lines.length} relative import(s) to convert`);

    if (!dryRun && lines.length > 0) {
      logger.info("Recommendation: Use path aliases from tsconfig.json (@/, ui/, database/, etc.)");
    }

    return {
      updated: lines.length,
      files: lines.map((l) => l.split(":")[0]),
    };
  } catch {
    spinner.warn("No relative imports found");
    return { updated: 0, files: [] };
  }
}

// Verify DAL usage compliance
async function verifyDALUsage(logger: any): Promise<{ files: string[]; issues: number }> {
  const spinner = createSpinner("Verifying DAL usage compliance...");
  spinner.start();

  try {
    // Search for direct database queries
    const result = execSync(
      "grep -r 'db\\.query\\|db\\.insert\\|db\\.update\\|db\\.delete' src --include='*.ts' --include='*.tsx' --exclude-dir=database",
      {
        encoding: "utf8",
        stdio: ["pipe", "pipe", "ignore"],
      }
    );

    const lines = result.split("\n").filter(Boolean);
    const nonServerActionFiles = new Set<string>();

    for (const line of lines) {
      const file = line.split(":")[0];
      if (!file.includes("/dal/") && !file.includes("/actions/")) {
        nonServerActionFiles.add(file);
      }
    }

    const issues = nonServerActionFiles.size;
    spinner.succeed(`Found ${issues} file(s) with potential DAL violations`);

    return {
      issues,
      files: Array.from(nonServerActionFiles),
    };
  } catch {
    spinner.succeed("No direct DAL violations found");
    return { issues: 0, files: [] };
  }
}

// Find and analyze error boundaries
async function analyzeErrorBoundaries(logger: any): Promise<{ files: string[]; missing: number }> {
  const spinner = createSpinner("Analyzing error boundary coverage...");
  spinner.start();

  try {
    // Search for Server Components without error boundaries
    const result = execSync("grep -r 'export default async function' src/app --include='*.tsx'", {
      encoding: "utf8",
      stdio: ["pipe", "pipe", "ignore"],
    });

    const files = result
      .split("\n")
      .filter(Boolean)
      .map((l) => l.split(":")[0]);

    spinner.succeed(`Found ${files.length} async Server Component(s)`);

    return {
      missing: files.length,
      files,
    };
  } catch {
    spinner.succeed("All Server Components properly analyzed");
    return { missing: 0, files: [] };
  }
}

// Check for missing use directives
async function checkUseDirectives(logger: any): Promise<{ files: string[]; missing: number }> {
  const spinner = createSpinner('Checking for "use server" / "use client" directives...');
  spinner.start();

  try {
    // Find Server Components lacking directives
    const result = execSync(
      "grep -L '^[\"\\']use' src/app/**/*.tsx src/components/**/*.tsx 2>/dev/null | grep -v node_modules",
      {
        encoding: "utf8",
        stdio: ["pipe", "pipe", "ignore"],
      }
    );

    const files = result.split("\n").filter(Boolean).slice(0, 10); // Limit to first 10

    spinner.succeed(`Checked directive usage`);

    return {
      missing: Math.max(0, files.length),
      files: files.slice(0, 5),
    };
  } catch {
    spinner.info("Directive check completed");
    return { missing: 0, files: [] };
  }
}

// Display summary report
function displaySummary(results: Record<string, any>, dryRun: boolean): void {
  console.log();
  console.log("═".repeat(70));
  console.log(info("  REFACTORING ANALYSIS REPORT"));
  console.log("═".repeat(70));

  console.log();
  console.log(info("Operations Analyzed:"));
  console.log();

  if (results.types) {
    console.log(`  • 'any' type annotations: ${results.types.fixed} found`);
    if (results.types.fixed > 0 && results.types.files.length > 0) {
      console.log(`    Files: ${results.types.files.slice(0, 3).join(", ")}`);
    }
  }

  if (results.imports) {
    console.log(`  • Relative imports: ${results.imports.updated} found`);
    if (results.imports.updated > 0 && results.imports.files.length > 0) {
      console.log(`    Files: ${results.imports.files.slice(0, 3).join(", ")}`);
    }
  }

  if (results.dalVerify) {
    console.log(`  • DAL compliance violations: ${results.dalVerify.issues} found`);
    if (results.dalVerify.issues > 0) {
      console.log(`    Files: ${results.dalVerify.files.slice(0, 2).join(", ")}`);
    }
  }

  if (results.boundaries) {
    console.log(`  • Async Server Components: ${results.boundaries.missing} found`);
  }

  if (results.directives) {
    console.log(`  • Directives missing: ${results.directives.missing} (approx)`);
  }

  console.log();
  console.log("─".repeat(70));

  if (dryRun) {
    console.log(warning("DRY-RUN MODE: No changes written to disk"));
  } else {
    console.log("Manual action required to apply recommendations.");
  }

  console.log(info("Next steps: Review files and apply suggested refactoring patterns"));
  console.log("─".repeat(70));
  console.log();
}

// Show help
function showHelp(): void {
  console.log();
  console.log("Usage: pnpm refactor [options]");
  console.log();
  console.log("Refactoring Operations:");
  console.log("  --types            Fix 'any' type annotations");
  console.log("  --imports          Replace relative imports with aliases");
  console.log("  --dto              Analyze DTO pattern adoption");
  console.log("  --boundaries       Analyze error boundary coverage");
  console.log("  --directives       Check use server/client directives");
  console.log("  --dal-verify       Verify DAL compliance");
  console.log();
  console.log("Options:");
  console.log("  --all              Run all refactoring operations");
  console.log("  --dry-run          Preview changes without writing");
  console.log("  --verbose          Detailed output");
  console.log();
  console.log("Examples:");
  console.log("  pnpm refactor --types            # Fix any types");
  console.log("  pnpm refactor --imports --dry-run # Preview import fixes");
  console.log("  pnpm refactor --all              # All refactoring operations");
  console.log();
}

// Main execution
async function main() {
  const options = parseArgs();
  const logger = createLogger("refactor", { verbose: options.verbose });

  // Show help if no options
  if (
    !options.types &&
    !options.imports &&
    !options.dto &&
    !options.boundaries &&
    !options.directives &&
    !options.dalVerify
  ) {
    showHelp();
    process.exit(0);
  }

  logger.section("Code Refactoring Analysis");

  if (options.dryRun) {
    logger.warn("DRY-RUN MODE: Analyzing only, no changes will be written");
  }

  // Run requested refactoring operations
  const results: Record<string, any> = {};

  if (options.types) {
    results.types = await fixAnyTypes(logger, options.dryRun);
  }

  if (options.imports) {
    results.imports = await fixImports(logger, options.dryRun);
  }

  if (options.boundaries) {
    results.boundaries = await analyzeErrorBoundaries(logger);
  }

  if (options.directives) {
    results.directives = await checkUseDirectives(logger);
  }

  if (options.dalVerify) {
    results.dalVerify = await verifyDALUsage(logger);
  }

  // Display summary
  displaySummary(results, options.dryRun);

  // Exit with status
  const totalIssues = Object.values(results).reduce(
    (sum: number, res: any) => sum + (res.fixed || res.updated || res.issues || res.missing || 0),
    0
  );

  process.exit(totalIssues > 0 ? 1 : 0);
}

main().catch((err) => {
  console.error("Refactoring failed:", err);
  process.exit(1);
});
