#!/usr/bin/env tsx
/**
 * Update Any Types Script
 *
 * DEPRECATED: This script is now a wrapper around unified-schema-refactor.ts --types
 *
 * Usage:
 *   pnpm optimize:types        # Find and fix 'any' type annotations
 *   pnpm optimize:types:dry    # Preview changes without modifying
 *   pnpm optimize:types:backup # Create backup before modifying
 */

import chalk from "chalk";
import { spawn } from "node:child_process";
import { join } from "node:path";

function main() {
  console.log(chalk.yellow("⚠️  DEPRECATED: pnpm optimize:types is deprecated"));
  console.log(chalk.gray("    Use: pnpm refactor --types\n"));

  const scriptPath = join(process.cwd(), "src", "scripts", "unified-schema-refactor.ts");

  // Pass through all arguments, replacing --dry-run with appropriate flag
  const args = ["--types", ...process.argv.slice(2)];

  const child = spawn("npx", ["tsx", scriptPath, ...args], {
    stdio: "inherit",
    shell: true,
    cwd: process.cwd(),
  });

  child.on("exit", (code) => {
    process.exit(code ?? 0);
  });
}

main();
