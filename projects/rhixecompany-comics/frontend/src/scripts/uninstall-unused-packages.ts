#!/usr/bin/env tsx
/**
 * ═══════════════════════════════════════════════════════════════════════════
 * Uninstall Unused Packages Script
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * Analyzes the project to find unused dependencies and devDependencies,
 * then uninstalls them using pnpm.
 *
 * Usage:
 *   pnpm tsx src/scripts/uninstall-unused-packages.ts
 *   pnpm tsx src/scripts/uninstall-unused-packages.ts --dry-run
 *   pnpm tsx src/scripts/uninstall-unused-packages.ts --verbose
 */

import { exec } from "node:child_process";
import fs from "node:fs/promises";
import path from "node:path";
import { promisify } from "node:util";

import chalk from "chalk";
import ora from "ora";

const execAsync = promisify(exec);

// ═══════════════════════════════════════════════════════════════════════════
// CONFIGURATION
// ═══════════════════════════════════════════════════════════════════════════

const DRY_RUN = process.argv.includes("--dry-run");
const VERBOSE = process.argv.includes("--verbose");
const YES = process.argv.includes("--yes");
const JSON_OUTPUT = process.argv.includes("--json");
const ROOT_DIR = process.cwd();
const PACKAGE_JSON_PATH = path.join(ROOT_DIR, "package.json");

// Packages to always keep (even if not detected in code)
const ALWAYS_KEEP = new Set([
  "next",
  "react",
  "react-dom",
  "typescript",
  "eslint",
  "prettier",
  "@types/node",
  "@types/react",
  "@types/react-dom",
  "drizzle-orm",
  "drizzle-kit",
  "postgres",
  "next-auth",
  "zod",
  "tailwindcss",
  "tsx",
  "vitest",
  "@playwright/test",
]);

interface PackageInfo {
  isDev: boolean;
  isUsed: boolean;
  locations: string[];
  name: string;
  version: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

function log(message: string, level: "error" | "info" | "success" | "warning" = "info") {
  if (!VERBOSE && level === "info") return;

  switch (level) {
    case "success":
      console.log(chalk.green(message));
      break;
    case "warning":
      console.log(chalk.yellow(message));
      break;
    case "error":
      console.log(chalk.red(message));
      break;
    default:
      console.log(message);
  }
}

async function loadPackageJson() {
  try {
    const content = await fs.readFile(PACKAGE_JSON_PATH, "utf-8");
    return JSON.parse(content);
  } catch (error) {
    // eslint-disable-next-line n/no-unsupported-features/es-syntax
    throw new Error(`Failed to load package.json: ${error}`, { cause: error });
  }
}

async function searchInFiles(packageName: string): Promise<string[]> {
  try {
    // eslint-disable-next-line no-useless-escape
    const { stdout } = await execAsync(`git grep -l "from ['\"]${packageName}" || echo ""`, {
      cwd: ROOT_DIR,
      maxBuffer: 10 * 1024 * 1024,
    });

    return stdout
      .trim()
      .split("\n")
      .filter((f) => f && !f.includes("node_modules") && !f.includes(".next"));
  } catch {
    // If git grep fails, fall back to searching specific patterns
    return [];
  }
}

async function isPackageUsed(packageName: string): Promise<{ locations: string[]; used: boolean }> {
  // Always keep essential packages
  if (ALWAYS_KEEP.has(packageName)) {
    return { used: true, locations: ["[essential package]"] };
  }

  // Check if package is imported anywhere
  const locations = await searchInFiles(packageName);

  // Check package.json scripts
  const packageJson = await loadPackageJson();
  const scriptsContent = JSON.stringify(packageJson.scripts || {});
  const usedInScripts = scriptsContent.includes(packageName);

  if (usedInScripts) {
    locations.push("package.json scripts");
  }

  // Check config files
  const configFiles = [
    "next.config.ts",
    "tailwind.config.ts",
    "eslint.config.ts",
    "vitest.config.ts",
    "playwright.config.ts",
    "postcss.config.mjs",
    ".prettierrc.ts",
    "drizzle.config.ts",
  ];

  for (const configFile of configFiles) {
    try {
      const configPath = path.join(ROOT_DIR, configFile);
      const content = await fs.readFile(configPath, "utf-8");
      if (content.includes(packageName)) {
        locations.push(configFile);
      }
    } catch {
      // File doesn't exist, skip
    }
  }

  return {
    used: locations.length > 0,
    locations,
  };
}

async function analyzePackages(): Promise<PackageInfo[]> {
  const packageJson = await loadPackageJson();
  const packages: PackageInfo[] = [];

  const spinner = ora("Analyzing dependencies...").start();

  // Analyze dependencies
  const deps = (packageJson.dependencies as Record<string, string>) || {};
  for (const [name, version] of Object.entries(deps)) {
    spinner.text = `Analyzing ${name}...`;
    const { used, locations } = await isPackageUsed(name);

    packages.push({
      name,
      version,
      isDev: false,
      isUsed: used,
      locations,
    });

    log(`  ${name}: ${used ? "USED" : "UNUSED"}`, used ? "success" : "warning");
  }

  // Analyze devDependencies
  const devDeps = (packageJson.devDependencies as Record<string, string>) || {};
  for (const [name, version] of Object.entries(devDeps)) {
    spinner.text = `Analyzing ${name}...`;
    const { used, locations } = await isPackageUsed(name);

    packages.push({
      name,
      version,
      isDev: true,
      isUsed: used,
      locations,
    });

    log(`  ${name}: ${used ? "USED" : "UNUSED"}`, used ? "success" : "warning");
  }

  spinner.succeed(chalk.green("✓ Package analysis complete"));
  return packages;
}

async function uninstallPackage(packageName: string, isDev: boolean): Promise<boolean> {
  if (DRY_RUN) {
    log(`DRY RUN: Would uninstall ${packageName}`, "info");
    return true;
  }

  try {
    const cmd = isDev ? `pnpm remove -D ${packageName}` : `pnpm remove ${packageName}`;

    await execAsync(cmd, { cwd: ROOT_DIR });
    log(`  Uninstalled ${packageName}`, "success");
    return true;
  } catch (error) {
    log(`  Failed to uninstall ${packageName}: ${error}`, "error");
    return false;
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// MAIN EXECUTION
// ═══════════════════════════════════════════════════════════════════════════

async function main() {
  console.log(chalk.bold.cyan("\n═══════════════════════════════════════════════════════"));
  console.log(chalk.bold.cyan("   Unused Package Remover"));
  console.log(chalk.bold.cyan("═══════════════════════════════════════════════════════\n"));

  if (DRY_RUN) {
    console.log(chalk.yellow("🔍 DRY RUN MODE - No packages will be uninstalled\n"));
  }

  // Analyze packages
  const packages = await analyzePackages();

  // Separate unused packages
  const unusedPackages = packages.filter((pkg) => !pkg.isUsed);
  const usedPackages = packages.filter((pkg) => pkg.isUsed);

  console.log(chalk.bold.cyan("\n═══════════════════════════════════════════════════════"));
  console.log(chalk.bold.cyan("   Analysis Results"));
  console.log(chalk.bold.cyan("═══════════════════════════════════════════════════════\n"));

  console.log(chalk.white("Total packages:     "), chalk.green(packages.length));
  console.log(chalk.white("Used packages:      "), chalk.green(usedPackages.length));
  console.log(chalk.white("Unused packages:    "), chalk.yellow(unusedPackages.length));

  if (unusedPackages.length === 0) {
    console.log(chalk.green("\n✓ No unused packages found!\n"));
    return;
  }

  // Display unused packages
  console.log(chalk.bold.yellow("\n⚠ Unused Packages:\n"));
  for (const pkg of unusedPackages) {
    console.log(chalk.yellow(`  • ${pkg.name}`) + chalk.gray(` (${pkg.isDev ? "devDependency" : "dependency"})`));
  }

  // Uninstall unused packages
  if (!DRY_RUN) {
    console.log(chalk.bold("\n📦 Uninstalling unused packages...\n"));

    const spinner = ora("Uninstalling packages...").start();

    let successCount = 0;
    let failCount = 0;

    for (const pkg of unusedPackages) {
      spinner.text = `Uninstalling ${pkg.name}...`;
      if (await uninstallPackage(pkg.name, pkg.isDev)) {
        successCount++;
      } else {
        failCount++;
      }
    }

    spinner.succeed(chalk.green(`✓ Uninstalled ${successCount} packages`));

    if (failCount > 0) {
      console.log(chalk.yellow(`⚠ Failed to uninstall ${failCount} packages`));
    }
  }

  // Summary
  console.log(chalk.bold.cyan("\n═══════════════════════════════════════════════════════"));
  console.log(chalk.bold.cyan("   Summary"));
  console.log(chalk.bold.cyan("═══════════════════════════════════════════════════════\n"));

  if (DRY_RUN) {
    console.log(chalk.yellow("⚠ This was a DRY RUN - no packages were uninstalled"));
    console.log(chalk.yellow("Run without --dry-run to perform actual uninstallation\n"));
  } else {
    console.log(chalk.green("✓ Unused packages have been removed\n"));
    console.log(chalk.white("Run 'pnpm install' to ensure lock file is updated\n"));
  }
}

main().catch((error) => {
  console.error(chalk.red(`\n✗ Script failed: ${error}\n`));
  process.exit(1);
});
