/**
 * Fix line endings across codebase
 * Normalizes CRLF to LF across repo (Git standard)
 *
 * Usage:
 *   pnpm fix:line-endings --pattern src/ --dry-run
 *   pnpm fix:line-endings --pattern src/ --verbose --yes
 */

import { readFileSync, writeFileSync } from "node:fs";

import { globSync } from "glob";

import { confirmAction } from "./shared/confirmAction";
import { Logger } from "./shared/logger";

const logger = new Logger();

interface LineEndingOptions {
  dryRun: boolean;
  json?: boolean;
  pattern: string;
  verbose: boolean;
  yes: boolean;
}

interface LineEndingResult {
  duration: number;
  filesChanged: number;
  postStats: {
    crlf: number;
    lf: number;
    mixed: number;
  };
  preStats: {
    crlf: number;
    lf: number;
    mixed: number;
  };
  success: boolean;
}

/**
 * Parse CLI arguments
 */
function parseArgs(): LineEndingOptions {
  const args = process.argv.slice(2);
  const patternArg = args.find((a) => a.startsWith("--pattern"));
  const pattern = patternArg?.includes("=") ? patternArg.split("=")[1] : args[args.indexOf(patternArg!) + 1];

  return {
    pattern: pattern || "src/",
    dryRun: args.includes("--dry-run"),
    verbose: args.includes("--verbose"),
    yes: args.includes("--yes"),
    json: args.includes("--json"),
  };
}

/**
 * Detect line ending type
 */
function detectLineEnding(content: string): "crlf" | "lf" | "mixed" | "none" {
  const hasLF = content.includes("\n");
  const hasCRLF = content.includes("\r\n");

  if (hasCRLF && hasLF) return "mixed";
  if (hasCRLF) return "crlf";
  if (hasLF) return "lf";
  return "none";
}

/**
 * Convert line endings in a file to LF
 */
function convertLineEndings(filePath: string): boolean {
  const content = readFileSync(filePath, "utf-8");
  const currentEnding = detectLineEnding(content);

  if (currentEnding === "lf" || currentEnding === "none") {
    return false;
  }

  let fixed = content;
  fixed = fixed.replaceAll("\r\n", "\n");

  if (fixed !== content) {
    writeFileSync(filePath, fixed);
    return true;
  }

  return false;
}

/**
 * Main line ending fix function
 */
async function fixLineEndingsMain(options: LineEndingOptions): Promise<LineEndingResult> {
  const startTime = Date.now();
  const result: LineEndingResult = {
    success: false,
    filesChanged: 0,
    duration: 0,
    preStats: { crlf: 0, lf: 0, mixed: 0 },
    postStats: { crlf: 0, lf: 0, mixed: 0 },
  };

  logger.section("Line Ending Analysis");
  logger.info(`Pattern: ${options.pattern}`);

  const files = globSync(`${options.pattern}/**/*.{ts,tsx,js,jsx,css,json,md,yml,yaml,sh}`, { dot: false });
  logger.info(`Files found: ${files.length}`);

  if (files.length === 0) {
    logger.warn("No files matched pattern");
    result.success = true;
    result.duration = Date.now() - startTime;
    return result;
  }

  // Analyze current state
  logger.section("Pre-Conversion Stats");
  const filesToFix: string[] = [];

  for (const file of files) {
    try {
      const content = readFileSync(file, "utf-8");
      const ending = detectLineEnding(content);

      if (ending === "crlf") {
        result.preStats.crlf++;
        filesToFix.push(file);
      } else if (ending === "lf") {
        result.preStats.lf++;
      } else if (ending === "mixed") {
        result.preStats.mixed++;
        filesToFix.push(file);
      }
    } catch (error) {
      logger.warn(`Failed to read ${file}`);
    }
  }

  logger.info(`LF files: ${result.preStats.lf}`);
  logger.info(`CRLF files: ${result.preStats.crlf}`);
  logger.info(`Mixed files: ${result.preStats.mixed}`);
  logger.info(`Total to fix: ${filesToFix.length}`);

  if (filesToFix.length === 0) {
    logger.success("All files already use LF line endings");
    result.success = true;
    result.postStats = result.preStats;
    result.duration = Date.now() - startTime;
    return result;
  }

  logger.section("Fix Plan");
  logger.info(`Files to convert: ${filesToFix.length}`);

  if (options.dryRun) {
    logger.info("DRY RUN: No files modified");
    result.success = true;
    result.postStats = result.preStats;
    result.duration = Date.now() - startTime;
    return result;
  }

  if (!options.yes) {
    const confirmed = await confirmAction({
      title: "Convert line endings to LF",
      message: `This will convert ${filesToFix.length} files from CRLF to LF.`,
      details: filesToFix.slice(0, 10).map((f) => `  ${f}`),
      cautionLevel: "medium",
      yesFlag: options.yes,
    });

    if (!confirmed) {
      logger.info("Fix cancelled");
      return result;
    }
  }

  logger.section("Fixing Line Endings");

  for (const file of filesToFix) {
    if (convertLineEndings(file)) {
      result.filesChanged++;
      if (options.verbose) {
        logger.info(`Fixed: ${file}`);
      }
    }
  }

  // Analyze post-conversion state
  logger.section("Post-Conversion Stats");

  for (const file of files) {
    try {
      const content = readFileSync(file, "utf-8");
      const ending = detectLineEnding(content);

      if (ending === "crlf") {
        result.postStats.crlf++;
      } else if (ending === "lf") {
        result.postStats.lf++;
      } else if (ending === "mixed") {
        result.postStats.mixed++;
      }
    } catch {
      // Already reported above
    }
  }

  logger.info(`LF files: ${result.postStats.lf}`);
  logger.info(`CRLF files: ${result.postStats.crlf}`);
  logger.info(`Mixed files: ${result.postStats.mixed}`);

  logger.success(`Fixed ${result.filesChanged} files`);
  result.success = true;
  result.duration = Date.now() - startTime;

  logger.info(`Duration: ${(result.duration / 1000).toFixed(2)}s`);

  return result;
}

// Main execution
(async () => {
  try {
    const options = parseArgs();
    const result = await fixLineEndingsMain(options);

    if (options.json) {
      logger.info(JSON.stringify(result));
    }

    process.exit(result.success ? 0 : 1);
  } catch (error) {
    logger.error(`Line ending fix failed: ${error instanceof Error ? error.message : String(error)}`);
    process.exit(1);
  }
})();
