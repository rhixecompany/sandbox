#!/usr/bin/env tsx
/**
 * CamelCase Converter Script
 * Converts kebab-case and snake_case file names to camelCase
 *
 * Usage:
 *   pnpm optimize:camelcase           # Convert all matching files
 *   pnpm optimize:camelcase:dry      # Preview changes without renaming
 *
 * File name conversions:
 *   my-file.ts → myFile.ts
 *   my_long_file.ts → myLongFile.ts
 *   my--file.ts → myFile.ts
 */

import chalk from "chalk";
import { Command } from "commander";
import { readdir, rename } from "node:fs/promises";
import { join } from "node:path";

import { createLogger } from "./shared/logger.js";

/**
 * Convert kebab-case or snake_case to camelCase
 */
function toCamelCase(str: string): string {
  return str
    .replaceAll(/[-_]+/g, " ")
    .replaceAll(/(?:^\w|[A-Z]|\b\w)/g, (letter) => {
      return letter.toUpperCase();
    })
    .replaceAll(/\s+/g, "");
}

/**
 * Check if a file name needs conversion
 */
function needsConversion(filename: string): boolean {
  // Check for kebab-case (contains -)
  if (filename.includes("-")) return true;
  // Check for snake_case (contains _ but not leading underscore)
  if (filename.includes("_") && !filename.startsWith("_")) return true;
  return false;
}

/**
 * Scan directory recursively for files
 */
async function scanDirectory(dir: string): Promise<string[]> {
  const files: string[] = [];

  try {
    const entries = await readdir(dir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = join(dir, entry.name);

      if (entry.isDirectory()) {
        // Skip node_modules and hidden directories
        if (!entry.name.startsWith(".") && entry.name !== "node_modules") {
          const subFiles = await scanDirectory(fullPath);
          files.push(...subFiles);
        }
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
  } catch (error) {
    // Ignore permission errors
  }

  return files;
}

/**
 * Main conversion function
 */
async function convertFiles(dryRun: boolean, verbose: boolean) {
  const logger = createLogger("camelcase-converter", { verbose });
  const srcDir = join(process.cwd(), "src");

  logger.section("CamelCase File Name Converter");
  logger.info(`Scanning: ${srcDir}`);
  logger.info(`Mode: ${dryRun ? "DRY RUN (no changes)" : "LIVE (will rename files)"}`);
  console.log();

  // Scan for files
  const spinner = { succeed: (msg: string) => console.log(chalk.green("✓"), msg) };
  spinner.succeed("Scanning directories...");

  const allFiles = await scanDirectory(srcDir);

  // Filter files that need conversion
  const filesToConvert: Array<{ oldPath: string; newPath: string }> = [];

  for (const file of allFiles) {
    const ext = file.substring(file.lastIndexOf("."));
    const dir = file.substring(0, file.lastIndexOf("/"));
    const filename = file.substring(file.lastIndexOf("/") + 1, file.lastIndexOf("."));

    if (needsConversion(filename)) {
      const newFilename = toCamelCase(filename);
      const newPath = join(dir, `${newFilename}${ext}`);

      if (file !== newPath) {
        filesToConvert.push({ oldPath: file, newPath });
      }
    }
  }

  // Display results
  console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
  console.log(chalk.cyan(`  Found ${filesToConvert.length} file(s) to convert`));
  console.log(chalk.cyan("═══════════════════════════════════════════════════════════\n"));

  if (filesToConvert.length === 0) {
    logger.success("No files need conversion!");
    return;
  }

  // Show detailed list
  console.log(chalk.blue("  Files to convert:\n"));
  for (const { oldPath, newPath } of filesToConvert) {
    const oldName = oldPath.substring(oldPath.lastIndexOf("/") + 1);
    const newName = newPath.substring(newPath.lastIndexOf("/") + 1);
    console.log(`  ${chalk.red(oldName)} ${chalk.gray("→")} ${chalk.green(newName)}`);
  }
  console.log();

  if (dryRun) {
    console.log(chalk.yellow("  ⚠️  DRY RUN - No files were renamed"));
    console.log(chalk.gray("  Run without --dry-run to apply changes\n"));
  } else {
    // Perform conversions
    logger.section("Converting files...");

    let converted = 0;
    let errors = 0;

    for (const { oldPath, newPath } of filesToConvert) {
      try {
        await rename(oldPath, newPath);
        const filename = oldPath.substring(oldPath.lastIndexOf("/") + 1);
        console.log(`  ${chalk.green("✓")} ${filename} → ${newPath.substring(newPath.lastIndexOf("/") + 1)}`);
        converted++;
      } catch (error) {
        const err = error instanceof Error ? error.message : String(error);
        console.log(`  ${chalk.red("✗")} Failed: ${err}`);
        errors++;
      }
    }

    console.log();
    logger.success(`Converted ${converted} file(s)`);
    if (errors > 0) {
      logger.error(`${errors} file(s) failed to convert`);
    }
  }

  // Update import statements in files (only in live mode)
  if (!dryRun && filesToConvert.length > 0) {
    logger.section("Updating import statements...");
    console.log(chalk.yellow("  ⚠️  Import statements must be updated manually"));
    console.log(chalk.gray("  Run: pnpm imports:optimize to fix import paths\n"));
  }
}

/**
 * CLI Entry Point
 */
const program = new Command()
  .name("camelcase-converter")
  .description("Convert kebab-case and snake_case file names to camelCase")
  .option("--dry-run", "Preview changes without renaming files", false)
  .option("--verbose", "Show detailed output", false)
  .parse(process.argv);

const dryRun = program.opts<{ dryRun?: boolean; verbose?: boolean }>().dryRun ?? false;
const verbose = program.opts<{ dryRun?: boolean; verbose?: boolean }>().verbose ?? false;

convertFiles(dryRun, verbose).catch((error) => {
  const err = error instanceof Error ? error.message : String(error);
  console.error(chalk.red("Error:"), err);
  process.exit(1);
});
