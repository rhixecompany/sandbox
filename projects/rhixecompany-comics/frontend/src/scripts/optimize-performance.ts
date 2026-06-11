#!/usr/bin/env tsx
/**
 * Performance Optimization Script
 *
 * DEPRECATED: This script is now a wrapper around unified-performance-ops.ts
 *
 * Usage:
 *   pnpm optimize:performance      # Run performance optimizations
 *   pnpm optimize:performance --analyze   # Analyze without optimizing
 *   pnpm optimize:performance --json      # JSON output
 */

import chalk from "chalk";
import { spawn } from "node:child_process";
import { join } from "node:path";

function main() {
  console.log(chalk.yellow("⚠️  DEPRECATED: pnpm optimize:performance is deprecated"));
  console.log(chalk.gray("    Use: pnpm optimize --performance\n"));

  const scriptPath = join(process.cwd(), "src", "scripts", "unified-performance-ops.ts");

  // Pass through all arguments
  const args = ["--performance", ...process.argv.slice(2)];

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
