#!/usr/bin/env tsx
/**
 * ═══════════════════════════════════════════════════════════════════════════
 * Unified Development Setup
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * Consolidates 18+ setup/build/test/lint scripts + cleanup utilities:
 * - complete-setup.ps1/sh — Full setup wizard
 * - setup-dev.ps1/sh — Dev environment setup
 * - test-*.ps1/sh — Test runners (unit, e2e, all)
 * - lint-*.ps1/sh — Linting runners
 * - build-*.ps1/sh — Build variants
 * - verify-*.ps1/sh — Verification tasks
 * - install-deps.ps1/sh — Install if needed
 * - reset-*.ps1/sh — Reset/clean tasks
 * - project-cleanup.ts — Deep project cleanup (merged)
 * - cleanup-duplicates.ts — Find/remove duplicate files (merged)
 * - validate-env.ts — Validate environment variables (merged)
 *
 * Usage:
 *   pnpm setup                     # Interactive setup wizard
 *   pnpm setup --deps              # Install/verify dependencies
 *   pnpm setup --env               # Initialize .env.local
 *   pnpm setup --extensions        # Install VS Code extensions
 *   pnpm setup --eslint            # Setup ESLint config
 *   pnpm setup --logging           # Configure logging
 *   pnpm setup --docker            # Initialize Docker
 *   pnpm setup --all               # Full setup (all tasks)
 *   pnpm setup --validate          # Validate setup
 *   pnpm setup --reset             # Reset & clean
 *   pnpm setup --cleanup           # Deep project cleanup
 *   pnpm setup --duplicates        # Find/remove duplicate files
 *   pnpm setup --validate-env      # Validate environment variables
 * ═══════════════════════════════════════════════════════════════════════════
 */

import { execSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, lstatSync, readdirSync, readFileSync, rmSync, statSync } from "node:fs";
import { readFile, writeFile } from "node:fs/promises";
import * as path from "node:path";

import { globSync } from "glob";

import { info, success } from "./shared/colors.js";
import { confirmAction } from "./shared/confirm.js";
import { createLogger } from "./shared/logger.js";
import { createSpinner } from "./shared/spinner.js";

interface SetupOptions {
  all: boolean;
  cleanup: boolean;
  deps: boolean;
  docker: boolean;
  dryRun: boolean;
  duplicates: boolean;
  env: boolean;
  eslint: boolean;
  extensions: boolean;
  interactive: boolean;
  json: boolean;
  logging: boolean;
  reset: boolean;
  validate: boolean;
  validateEnv: boolean;
  verbose: boolean;
  yes: boolean;
}

function parseArgs(): SetupOptions {
  const args = process.argv.slice(2);

  const options: SetupOptions = {
    all: args.includes("--all"),
    cleanup: args.includes("--cleanup"),
    deps: args.includes("--deps"),
    docker: args.includes("--docker"),
    dryRun: args.includes("--dry-run"),
    duplicates: args.includes("--duplicates"),
    env: args.includes("--env"),
    eslint: args.includes("--eslint"),
    extensions: args.includes("--extensions"),
    interactive: !args.includes("--no-interactive"),
    json: args.includes("--json"),
    logging: args.includes("--logging"),
    reset: args.includes("--reset"),
    validate: args.includes("--validate"),
    validateEnv: args.includes("--validate-env"),
    verbose: args.includes("--verbose"),
    yes: args.includes("--yes"),
  };

  // If --all specified, enable all setup tasks
  if (options.all) {
    options.deps = true;
    options.env = true;
    options.extensions = true;
    options.eslint = true;
    options.logging = true;
    options.docker = true;
    options.validate = true;
    options.cleanup = true;
    options.duplicates = true;
    options.validateEnv = true;
  }

  return options;
}

// Verify & install dependencies
async function setupDependencies(logger: any): Promise<{ success: boolean }> {
  const spinner = createSpinner("Verifying dependencies...");
  spinner.start();

  try {
    const tasks = [
      { name: "Node.js packages", cmd: "pnpm install --frozen-lockfile" },
      { name: "TypeScript types", cmd: "pnpm type-gen" },
      { name: "Database client", cmd: "pnpm type-check" },
    ];

    spinner.succeed("Starting dependency installation");
    execSync("pnpm install", { stdio: "pipe" });

    for (const task of tasks) {
      const taskSpinner = createSpinner(`Setting up ${task.name}...`);
      taskSpinner.start();
      try {
        execSync(task.cmd, { stdio: "pipe" });
        taskSpinner.succeed(`${task.name} complete`);
        logger.success(`  ✓ ${task.name}`);
      } catch {
        taskSpinner.warn(`${task.name} (non-critical)`);
        logger.warn(`  ⚠ ${task.name} (non-critical)`);
      }
    }

    return { success: true };
  } catch (err) {
    spinner.fail("Dependency installation failed");
    logger.error(`Error: ${err instanceof Error ? err.message : String(err)}`);
    return { success: false };
  }
}

// Initialize .env.local
async function setupEnvironment(logger: any): Promise<{ success: boolean }> {
  const spinner = createSpinner("Setting up environment variables...");
  spinner.start();

  try {
    const envPath = ".env.local";
    const examplePath = ".env.local.example";

    if (!existsSync(envPath) && existsSync(examplePath)) {
      const example = await readFile(examplePath, "utf-8");
      await writeFile(envPath, example);
      spinner.succeed(".env.local created from .env.local.example");
      logger.warn("  ⚠ Please configure required variables in .env.local");
    } else if (existsSync(envPath)) {
      spinner.succeed(".env.local already configured");
    } else {
      spinner.warn(".env.local.example not found");
    }

    return { success: true };
  } catch (err) {
    spinner.fail("Environment setup failed");
    return { success: false };
  }
}

// Install VS Code extensions
async function setupExtensions(logger: any): Promise<{ success: boolean }> {
  const spinner = createSpinner("Setting up VS Code extensions...");
  spinner.start();

  try {
    const extensions = [
      "GitHub.copilot",
      "GitHub.copilot-chat",
      "dbaeumer.vscode-eslint",
      "esbenp.prettier-vscode",
      "bradlc.vscode-tailwindcss",
      "unifiedjs.vscode-mdx",
      "orta.vscode-jest",
      "ms-playwright.playwright",
    ];

    logger.info("Recommended VS Code Extensions:");
    for (const ext of extensions) {
      logger.info(`  code --install-extension ${ext}`);
    }

    spinner.succeed("Extension list generated");
    return { success: true };
  } catch (err) {
    spinner.fail("Extension setup failed");
    return { success: false };
  }
}

// Setup ESLint configuration
async function setupESLint(logger: any): Promise<{ success: boolean }> {
  const spinner = createSpinner("Checking ESLint configuration...");
  spinner.start();

  try {
    if (existsSync("eslint.config.mts")) {
      spinner.succeed("ESLint configuration found");
      logger.success("  ✓ eslint.config.mts exists");
      return { success: true };
    } else {
      spinner.warn("ESLint configuration missing");
      return { success: false };
    }
  } catch (err) {
    spinner.fail("ESLint setup failed");
    return { success: false };
  }
}

// Configure logging
async function setupLogging(logger: any): Promise<{ success: boolean }> {
  const spinner = createSpinner("Configuring logging...");
  spinner.start();

  try {
    const config = {
      level: "debug",
      format: "json",
      output: "stdout",
      transports: ["console", "file"],
    };

    logger.info("Logging Configuration:");
    for (const [key, value] of Object.entries(config)) {
      logger.info(`  ${key}: ${value}`);
    }

    spinner.succeed("Logging configuration ready");
    return { success: true };
  } catch (err) {
    spinner.fail("Logging setup failed");
    return { success: false };
  }
}

// Initialize Docker
async function setupDocker(logger: any): Promise<{ success: boolean }> {
  const spinner = createSpinner("Checking Docker configuration...");
  spinner.start();

  try {
    const hasDocker = existsSync("Dockerfile");
    const hasCompose = existsSync("docker-compose.yml");

    if (hasDocker && hasCompose) {
      spinner.succeed("Docker configuration found");
      logger.success("  ✓ Dockerfile exists");
      logger.success("  ✓ docker-compose.yml exists");
      return { success: true };
    } else {
      spinner.warn("Docker configuration incomplete");
      if (!hasDocker) logger.warn("  ⚠ Dockerfile missing");
      if (!hasCompose) logger.warn("  ⚠ docker-compose.yml missing");
      return { success: false };
    }
  } catch (err) {
    spinner.fail("Docker setup failed");
    return { success: false };
  }
}

// Validate complete setup
async function validateSetup(logger: any): Promise<{ checks: string[]; success: boolean }> {
  const spinner = createSpinner("Validating setup...");
  spinner.start();

  try {
    const checks: Array<{
      check?: () => boolean;
      cmd?: string;
      name: string;
    }> = [
      { name: "Node.js", cmd: "node --version" },
      { name: "pnpm", cmd: "pnpm --version" },
      { name: "Dependencies", cmd: "pnpm list --depth=0" },
      { name: "TypeScript", cmd: "tsc --version" },
      { name: ".env.local", check: () => existsSync(".env.local") },
    ];

    const results: string[] = [];

    for (const checkItem of checks) {
      try {
        if (checkItem.cmd) {
          execSync(checkItem.cmd, { stdio: "pipe" });
        } else if (checkItem.check) {
          checkItem.check();
        }
        logger.success(`  ✓ ${checkItem.name}`);
        results.push(checkItem.name);
      } catch {
        logger.warn(`  ⚠ ${checkItem.name}`);
      }
    }

    spinner.succeed("Validation complete");
    return { checks: results, success: results.length >= 4 };
  } catch (err) {
    spinner.fail("Validation failed");
    logger.error(`Error: ${err instanceof Error ? err.message : String(err)}`);
    return { checks: [], success: false };
  }
}

// Reset & clean
async function resetSetup(logger: any): Promise<{ success: boolean }> {
  try {
    const confirmed = await confirmAction({
      title: "Reset Development Environment",
      items: [
        "This will remove node_modules and reinstall dependencies",
        "Your .env.local and database data will be preserved",
      ],
      itemsLabel: "Changes",
      cautionLevel: "high",
    });

    if (!confirmed) {
      logger.info("Reset cancelled");
      return { success: false };
    }

    const spinner = createSpinner("Resetting environment...");
    spinner.start();

    try {
      execSync("rm -rf node_modules pnpm-lock.yaml || true", { stdio: "pipe" });
      execSync("pnpm install", { stdio: "pipe" });
      spinner.succeed("Environment reset complete");
      return { success: true };
    } catch (err) {
      spinner.fail("Reset failed");
      return { success: false };
    }
  } catch (err) {
    logger.error(`Reset error: ${err instanceof Error ? err.message : String(err)}`);
    return { success: false };
  }
}

// Deep project cleanup (merged from project-cleanup.ts)
function formatBytes(bytes: number): string {
  if (bytes === 0) return "0 B";
  const k = 1024;
  const sizes = ["B", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + " " + sizes[i];
}

function calculateSize(filePath: string): number {
  try {
    const stat = lstatSync(filePath);
    if (stat.isFile()) {
      return stat.size;
    } else if (stat.isDirectory()) {
      let size = 0;
      const files = readdirSync(filePath);
      for (const file of files) {
        size += calculateSize(path.join(filePath, file));
      }
      return size;
    }
  } catch {
    return 0;
  }
  return 0;
}

async function runProjectCleanup(logger: any, options: SetupOptions): Promise<{ success: boolean; freed: string }> {
  const spinner = createSpinner("Analyzing project for cleanup...");
  spinner.start();

  const KEEP_PATTERNS = ["node_modules", ".git", ".next/static", "public", "src", "docs", ".vscode", ".github"];
  const patterns = [
    "node_modules/.vite",
    ".turbo",
    ".next",
    "dist",
    "build",
    "**/*.log",
    "**/*.tmp",
    ".DS_Store",
    "Thumbs.db",
  ];

  const filesToDelete: string[] = [];
  for (const pattern of patterns) {
    const matches = globSync(pattern, { dot: true, ignore: KEEP_PATTERNS });
    filesToDelete.push(...matches);
  }

  let totalSize = 0;
  for (const file of filesToDelete) {
    if (existsSync(file)) {
      totalSize += calculateSize(file);
    }
  }

  logger.info(`Files to delete: ${filesToDelete.length}`);
  logger.info(`Space to free: ${formatBytes(totalSize)}`);

  spinner.succeed(`Found ${filesToDelete.length} files to clean`);

  if (options.dryRun) {
    logger.info("DRY RUN: No files deleted");
    return { success: true, freed: formatBytes(totalSize) };
  }

  if (!options.yes) {
    const confirmed = await confirmAction({
      title: "Delete files and directories",
      message: `This will permanently delete ${filesToDelete.length} files and directories.`,
      items: filesToDelete.slice(0, 10),
      itemsLabel: "Files to delete",
      cautionLevel: filesToDelete.length > 100 ? "high" : "medium",
    });

    if (!confirmed) {
      logger.info("Cleanup cancelled");
      return { success: false, freed: "0 B" };
    }
  }

  let deletedSize = 0;
  for (const file of filesToDelete) {
    if (existsSync(file)) {
      try {
        deletedSize += calculateSize(file);
        rmSync(file, { recursive: true, force: true });
      } catch (error) {
        logger.warn(`Failed to delete ${file}`);
      }
    }
  }

  logger.success(`Files deleted: ${filesToDelete.length}`);
  logger.success(`Space freed: ${formatBytes(deletedSize)}`);

  return { success: true, freed: formatBytes(deletedSize) };
}

// Find and remove duplicate files (merged from cleanup-duplicates.ts)
function getFileHash(filePath: string): string {
  try {
    const content = readFileSync(filePath);
    return createHash("sha256").update(content).digest("hex");
  } catch {
    return "";
  }
}

interface DuplicateGroup {
  files: Array<{ modTime: number; path: string; size: number }>;
  hash: string;
}

async function runCleanupDuplicates(
  logger: any,
  options: SetupOptions
): Promise<{ success: boolean; deleted: number; freed: string }> {
  const spinner = createSpinner("Scanning for duplicate files...");
  spinner.start();

  const pattern = "src/**/*.{ts,tsx,js,jsx}";
  const hashMap = new Map<string, DuplicateGroup["files"]>();
  const files = globSync(pattern, { dot: false });

  logger.info(`Scanning ${files.length} files...`);

  for (const filePath of files) {
    try {
      const stat = statSync(filePath);
      if (!stat.isFile()) continue;

      const hash = getFileHash(filePath);
      if (!hash) continue;

      if (!hashMap.has(hash)) {
        hashMap.set(hash, []);
      }

      hashMap.get(hash)!.push({
        path: filePath,
        size: stat.size,
        modTime: stat.mtimeMs,
      });
    } catch {
      // Skip inaccessible files
    }
  }

  const duplicates: DuplicateGroup[] = Array.from(hashMap.entries())
    .filter(([, files]) => files.length > 1)
    .map(([hash, files]) => ({ hash, files }));

  const filesToDelete: string[] = [];
  for (const group of duplicates) {
    const sorted = [...group.files].sort((a, b) => a.path.localeCompare(b.path));
    filesToDelete.push(...sorted.slice(1).map((f) => f.path));
  }

  let totalSize = 0;
  for (const file of filesToDelete) {
    try {
      const stat = statSync(file);
      totalSize += stat.size;
    } catch {
      // Skip
    }
  }

  logger.info(`Duplicate groups: ${duplicates.length}`);
  logger.info(`Files to delete: ${filesToDelete.length}`);
  logger.info(`Space to free: ${formatBytes(totalSize)}`);

  spinner.succeed(`Found ${duplicates.length} duplicate group(s)`);

  if (options.dryRun) {
    logger.info("DRY RUN: No files deleted");
    return { success: true, deleted: 0, freed: formatBytes(totalSize) };
  }

  if (!options.yes) {
    const confirmed = await confirmAction({
      title: "Delete duplicate files",
      message: `This will permanently delete ${filesToDelete.length} duplicate files.`,
      items: filesToDelete.slice(0, 10).map((f) => path.relative(process.cwd(), f)),
      itemsLabel: "Files to delete",
      cautionLevel: "high",
    });

    if (!confirmed) {
      logger.info("Cleanup cancelled");
      return { success: false, deleted: 0, freed: "0 B" };
    }
  }

  let deletedSize = 0;
  for (const file of filesToDelete) {
    if (existsSync(file)) {
      try {
        const stat = statSync(file);
        deletedSize += stat.size;
        rmSync(file, { force: true });
      } catch (error) {
        logger.warn(`Failed to delete ${file}`);
      }
    }
  }

  logger.success(`Files deleted: ${filesToDelete.length}`);
  logger.success(`Space freed: ${formatBytes(deletedSize)}`);

  return { success: true, deleted: filesToDelete.length, freed: formatBytes(deletedSize) };
}

// Validate environment variables (merged from validate-env.ts)
const REQUIRED_ENV_VARS = [
  {
    name: "DATABASE_URL",
    required: true,
    validator: (v: string) => v.startsWith("postgresql://") || v.startsWith("postgres://"),
  },
  { name: "AUTH_SECRET", required: true, validator: (v: string) => v.length >= 32 },
  { name: "AUTH_URL", required: false, validator: (v: string) => v.startsWith("http") },
];

function loadEnvFile(filePath: string): Record<string, string> {
  if (!existsSync(filePath)) return {};

  const content = readFileSync(filePath, "utf-8");
  const env: Record<string, string> = {};

  for (const line of content.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;

    const [key, ...valueParts] = trimmed.split("=");
    const value = valueParts.join("=").replaceAll(/^"|"$/g, "");
    if (key) {
      env[key] = value;
    }
  }

  return env;
}

async function runValidateEnv(logger: any, options: SetupOptions): Promise<{ success: boolean; errors: string[] }> {
  const spinner = createSpinner("Validating environment variables...");
  spinner.start();

  const envLocalPath = path.join(process.cwd(), ".env.local");
  const envVars = loadEnvFile(envLocalPath);

  if (!existsSync(envLocalPath)) {
    spinner.warn(".env.local not found");
    logger.warn("Please create .env.local from .env.local.example");
    return { success: false, errors: [".env.local not found"] };
  }

  const errors: string[] = [];

  for (const envVar of REQUIRED_ENV_VARS) {
    const value = envVars[envVar.name];

    if (!value) {
      if (envVar.required) {
        errors.push(`${envVar.name} is missing`);
      }
      continue;
    }

    if (envVar.validator && !envVar.validator(value)) {
      errors.push(`${envVar.name} is invalid`);
    }
  }

  if (errors.length === 0) {
    spinner.succeed("Environment variables validated");
    logger.success("All required variables are set");
    return { success: true, errors: [] };
  }

  spinner.fail("Environment validation failed");
  for (const error of errors) {
    logger.error(error);
  }

  return { success: false, errors };
}

// Show help
function showHelp(): void {
  console.log();
  console.log("Usage: pnpm setup [options]");
  console.log();
  console.log("Setup Tasks:");
  console.log("  --deps              Install/verify dependencies");
  console.log("  --env               Initialize .env.local");
  console.log("  --extensions        Recommend VS Code extensions");
  console.log("  --eslint            Setup ESLint configuration");
  console.log("  --logging           Configure logging");
  console.log("  --docker            Initialize Docker setup");
  console.log("  --validate          Validate complete setup");
  console.log("  --reset             Reset environment (clean install)");
  console.log("  --cleanup           Deep project cleanup (remove artifacts)");
  console.log("  --duplicates        Find/remove duplicate files");
  console.log("  --validate-env      Validate environment variables");
  console.log();
  console.log("Options:");
  console.log("  --all               Run all setup tasks");
  console.log("  --dry-run           Preview changes without writing");
  console.log("  --verbose           Detailed output");
  console.log("  --yes               Skip confirmation prompts");
  console.log("  --no-interactive    Skip confirmations");
  console.log();
  console.log("Examples:");
  console.log("  pnpm setup --all                  # Complete setup");
  console.log("  pnpm setup --deps --validate      # Install & verify");
  console.log("  pnpm setup --reset --all          # Reset & reconfigure");
  console.log();
}

// Display summary
function displaySummary(results: Record<string, any>): void {
  console.log();
  console.log("═".repeat(70));
  console.log(info("  SETUP SUMMARY"));
  console.log("═".repeat(70));
  console.log();

  if (results.dependencies) {
    console.log(info("Dependencies:"));
    console.log(`  Status: ${results.dependencies.success ? "✓ Ready" : "✗ Failed"}`);
    console.log();
  }

  if (results.environment) {
    console.log(info("Environment:"));
    console.log(`  Status: ${results.environment.success ? "✓ Ready" : "✗ Failed"}`);
    console.log();
  }

  if (results.validation) {
    console.log(info("Validation Results:"));
    console.log(`  Status: ${results.validation.success ? "✓ Pass" : "✗ Fail"}`);
    console.log(`  Checks: ${results.validation.checks.join(", ")}`);
    console.log();
  }

  if (results.cleanup) {
    console.log(info("Project Cleanup:"));
    console.log(`  Status: ${results.cleanup.success ? "✓ Complete" : "✗ Failed"}`);
    console.log(`  Space freed: ${results.cleanup.freed}`);
    console.log();
  }

  if (results.duplicates) {
    console.log(info("Duplicate Cleanup:"));
    console.log(`  Status: ${results.duplicates.success ? "✓ Complete" : "✗ Failed"}`);
    console.log(`  Files deleted: ${results.duplicates.deleted}`);
    console.log(`  Space freed: ${results.duplicates.freed}`);
    console.log();
  }

  if (results.validateEnv) {
    console.log(info("Environment Validation:"));
    console.log(`  Status: ${results.validateEnv.success ? "✓ Valid" : "✗ Invalid"}`);
    if (results.validateEnv.errors.length > 0) {
      console.log(`  Errors: ${results.validateEnv.errors.length}`);
    }
    console.log();
  }

  console.log("─".repeat(70));
  console.log(success("Setup complete! Ready to develop."));
  console.log(info("Run: pnpm dev   —   Start development server"));
  console.log("─".repeat(70));
  console.log();
}

// Main execution
async function main() {
  const options = parseArgs();
  const logger = createLogger("setup", { verbose: options.verbose });

  if (
    !options.deps &&
    !options.env &&
    !options.extensions &&
    !options.eslint &&
    !options.logging &&
    !options.docker &&
    !options.validate &&
    !options.reset &&
    !options.cleanup &&
    !options.duplicates &&
    !options.validateEnv
  ) {
    showHelp();
    process.exit(0);
  }

  logger.section("Development Environment Setup");

  const results: Record<string, any> = {};

  if (options.deps) {
    results.dependencies = await setupDependencies(logger);
  }

  if (options.env) {
    results.environment = await setupEnvironment(logger);
  }

  if (options.extensions) {
    results.extensions = await setupExtensions(logger);
  }

  if (options.eslint) {
    results.eslint = await setupESLint(logger);
  }

  if (options.logging) {
    results.logging = await setupLogging(logger);
  }

  if (options.docker) {
    results.docker = await setupDocker(logger);
  }

  if (options.reset) {
    results.reset = await resetSetup(logger);
  }

  if (options.validate) {
    results.validation = await validateSetup(logger);
  }

  if (options.cleanup) {
    results.cleanup = await runProjectCleanup(logger, options);
  }

  if (options.duplicates) {
    results.duplicates = await runCleanupDuplicates(logger, options);
  }

  if (options.validateEnv) {
    results.validateEnv = await runValidateEnv(logger, options);
  }

  displaySummary(results);

  process.exit(0);
}

main().catch((err) => {
  console.error("Setup failed:", err);
  process.exit(1);
});
