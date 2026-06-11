/**
 * CLI Entry Point for Database Seeding
 * Usage: tsx src/scripts/seed/run.ts [options]
 *
 * Examples:
 *   pnpm seed                          # Seed all entities
 *   pnpm seed types authors            # Seed specific entities
 *   pnpm seed --dry-run --verbose      # Validate without persisting
 *   pnpm seed comics --batch-size=50   # Custom batch size
 */
import chalk from "chalk";
import { Command } from "commander";
import { z } from "zod";

import { getEnv } from "appConfig";

import { Logger } from "./logger";
import { SeedOrchestrator } from "./seed-orchestrator";

import type { SeedConfig } from "./types";

/**
 * Environment variable validation with Zod
 */
const envSchema = z.object({
  DATABASE_URL: z.string().url("Invalid DATABASE_URL").optional(),
  NODE_ENV: z.enum(["development", "production", "test"]).default("development"),
  IMAGEKIT_PUBLIC_KEY: z.string().optional(),
  IMAGEKIT_PRIVATE_KEY: z.string().optional(),
});

/**
 * Parse CLI arguments and return SeedConfig
 */
function parseCliArgs(program: Command, logger: Logger): SeedConfig {
  const options = program.opts();
  const args = program.args;

  try {
    // Validate environment (just to ensure DB_URL exists)
    envSchema.parse(process.env);

    // Parse entities (default to "all" if empty)
    const entitiesToSeed = args.length === 0 ? ["all"] : args;

    // Validate entity names
    const validEntities = [
      "types",
      "authors",
      "artists",
      "genres",
      "comics",
      "chapters",
      "users",
      "roles",
      "permissions",
      "user-roles",
      "user-preferences",
      "reader-settings",
      "reading-goals",
      "bookmarks",
      "ratings",
      "comments",
      "notifications",
      "reading-history",
      "follows",
      "shares",
      "comic-images",
      "chapter-images",
      "all",
    ];
    for (const entity of entitiesToSeed) {
      if (!validEntities.includes(entity)) {
        throw new Error(`Invalid entity: ${entity}. Valid options: ${validEntities.join(", ")}`);
      }
    }

    // Validate options
    const batchSize = parseInt(String(options.batchSize || "100"), 10);
    const concurrency = parseInt(String(options.concurrency || "5"), 10);

    if (isNaN(batchSize) || batchSize < 1) {
      throw new Error("batch-size must be a positive number");
    }

    if (isNaN(concurrency) || concurrency < 1) {
      throw new Error("concurrency must be a positive number");
    }

    const imageStrategy = String(options.imageStrategy || "urls") as "imagekit" | "local" | "urls";
    if (!["urls", "local", "imagekit"].includes(imageStrategy)) {
      throw new Error("image-strategy must be: urls, local, or imagekit");
    }

    // Parse optional numeric flags
    const chunkSize = options.chunkSize ? parseInt(String(options.chunkSize), 10) : undefined;
    if (chunkSize !== undefined && (isNaN(chunkSize) || chunkSize < 1)) {
      throw new Error("chunk-size must be a positive number");
    }

    const count = options.count ? parseInt(String(options.count), 10) : undefined;
    if (count !== undefined && (isNaN(count) || count < 1)) {
      throw new Error("count must be a positive number");
    }

    const bcryptRounds = options.bcryptRounds ? parseInt(String(options.bcryptRounds), 10) : undefined;
    if (bcryptRounds !== undefined && (isNaN(bcryptRounds) || bcryptRounds < 1 || bcryptRounds > 31)) {
      throw new Error("bcrypt-rounds must be between 1 and 31");
    }

    const maxImageWidth = options.maxWidth ? parseInt(String(options.maxWidth), 10) : 1200;
    if (isNaN(maxImageWidth) || maxImageWidth < 100 || maxImageWidth > 4000) {
      throw new Error("--max-width must be between 100 and 4000");
    }

    const imageQuality = options.imageQuality ? parseInt(String(options.imageQuality), 10) : 75;
    if (isNaN(imageQuality) || imageQuality < 1 || imageQuality > 100) {
      throw new Error("--image-quality must be between 1 and 100");
    }

    const optimizeImages = options.optimizeImages !== false;
    const reprocessExisting = Boolean(options.reprocess);

    // Log validation success
    if (options.verbose) {
      logger.debug("Configuration validation passed", {
        entities: entitiesToSeed,
        batchSize,
        concurrency,
        imageStrategy,
      });
    }

    // Build config
    const config: SeedConfig = {
      entities: entitiesToSeed as Array<
        | "all"
        | "artists"
        | "authors"
        | "bookmarks"
        | "chapter-images"
        | "chapters"
        | "comic-images"
        | "comics"
        | "comments"
        | "follows"
        | "genres"
        | "notifications"
        | "permissions"
        | "ratings"
        | "reader-settings"
        | "reading-goals"
        | "reading-history"
        | "roles"
        | "shares"
        | "types"
        | "user-preferences"
        | "user-roles"
        | "users"
      >,
      options: {
        batchSize,
        concurrency,
        verbose: Boolean(options.verbose),
        dryRun: Boolean(options.dryRun),
        useTransaction: options.transaction !== false,
        skipValidation: Boolean(options.skipValidation),
        forceOverwrite: Boolean(options.force),
        imageStrategy,
        chunkSize,
        resume: Boolean(options.resume),
        count,
        bcryptRounds,
        optimizeImages,
        maxImageWidth,
        imageQuality,
        reprocessExisting,
      },
      timestamp: new Date(),
    };

    return config;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    const stack = error instanceof Error ? error.stack : undefined;
    logger.error(`Configuration error: ${message}`, {
      source: "parseCliArgs",
      suggestion: "Check your arguments and environment variables",
    });
    if (options.verbose && stack) {
      console.error(stack);
    }
    process.exit(1);
  }
}

/**
 * Main CLI execution entry point
 */
async function main() {
  try {
    const program = new Command();

    program
      .name("seed")
      .description("Seed ComicWise database with test data")
      .version("1.0.0")
      .argument(
        "[entities...]",
        "Entities to seed: types, authors, artists, genres, comics, chapters, or all (default: all)"
      )
      .option("--batch-size <number>", "Batch size for concurrent processing", "100")
      .option("--concurrency <number>", "Number of concurrent operations", "5")
      .option("--verbose", "Enable verbose logging (default: false)")
      .option("--dry-run", "Validate without persisting to database")
      .option("--force", "Force overwrite existing data (upsert mode, default: skip)")
      .option("--no-transaction", "Disable per-entity transactions")
      .option("--skip-validation", "Skip Zod schema validation")
      .option("--image-strategy <mode>", "Image handling strategy: urls (default), local, or imagekit", "urls")
      .option("--chunk-size <number>", "Enable chunked processing with given chunk size")
      .option("--resume", "Resume from last checkpoint (requires --chunk-size)")
      .option("--count <number>", "Target entity count for synthetic generation (e.g., user seeder)")
      .option("--bcrypt-rounds <number>", "Bcrypt salt rounds for password hashing (default: 10)")
      .option("--optimize-images", "Enable image optimization (default: true for local strategy)")
      .option("--no-optimize-images", "Disable image optimization")
      .option("--max-width <px>", "Max image width in pixels (default: 1200)", "1200")
      .option("--image-quality <1-100>", "Image quality 1-100 (default: 75)", "75")
      .option("--reprocess", "Re-process existing downloaded images");

    program.option("--json", "Output results as JSON");

    // Get options early for subcommand handling
    const cmdOptions = program.opts();

    // Handle migrate-images command
    const subcommands = ["migrate-images", "reprocess-images"];
    const firstArg = program.args[0];
    if (subcommands.includes(firstArg)) {
      const migrateLogger = new Logger(Boolean(cmdOptions.verbose), false);

      if (firstArg === "migrate-images") {
        migrateLogger.section("Image Migration");
        migrateLogger.info("Migrating from /public/comics → /public/uploads/comics");
        migrateLogger.info("Migrating from /public/chapters → /public/uploads/chapters");

        if (cmdOptions.dryRun) {
          migrateLogger.warn("DRY RUN: No files will be moved");
        }

        const { migrateImages } = await import("./helpers/image-migrator");
        const result = await migrateImages();

        if (result.success) {
          migrateLogger.success("Migration completed successfully");
        } else {
          migrateLogger.error("Migration completed with errors");
        }

        migrateLogger.info(
          `Results: ${result.stats.migrated} migrated, ${result.stats.skipped} skipped, ${result.stats.errors} errors, ${result.stats.dbUpdated} DB records updated`
        );

        process.exit(result.success ? 0 : 1);
      }

      if (firstArg === "reprocess-images") {
        migrateLogger.section("Image Reprocessing");
        migrateLogger.info("Re-processing existing images with optimization");

        const maxWidth = cmdOptions.maxWidth ? parseInt(String(cmdOptions.maxWidth), 10) : 1200;
        const imageQuality = cmdOptions.imageQuality ? parseInt(String(cmdOptions.imageQuality), 10) : 75;

        migrateLogger.info(`Settings: maxWidth=${maxWidth}, quality=${imageQuality}`);

        if (cmdOptions.dryRun) {
          migrateLogger.warn("DRY RUN: No files will be modified");
        }

        const { reprocessExistingImages } = await import("./helpers/image-migrator");
        const result = await reprocessExistingImages({
          maxWidth,
          maxHeight: 2000,
          quality: imageQuality,
          dryRun: cmdOptions.dryRun,
        });

        if (result.success) {
          migrateLogger.success("Reprocessing completed successfully");
        } else {
          migrateLogger.error("Reprocessing completed with errors");
        }

        migrateLogger.info(
          `Results: ${result.comicsProcessed} comics + ${result.chaptersProcessed} chapters processed, saved ${(result.totalSavedBytes / 1024 / 1024).toFixed(2)}MB`
        );

        if (result.errors.length > 0) {
          migrateLogger.warn(`Errors: ${result.errors.join(", ")}`);
        }

        process.exit(result.success ? 0 : 1);
      }
    }

    program.parse();

    // Create enhanced logger with dry-run mode
    const enhancedLogger = new Logger(Boolean(cmdOptions.verbose), Boolean(cmdOptions.dryRun));

    const config = parseCliArgs(program, enhancedLogger);

    enhancedLogger.section("ComicWise Database Seeding");
    enhancedLogger.info(`Node environment: ${getEnv().NODE_ENV}`, {
      nodeVersion: process.version,
    });
    enhancedLogger.info(`Timestamp: ${config.timestamp.toISOString()}`);

    if (config.options.verbose) {
      enhancedLogger.info(`Configuration:`, {
        entities: config.entities,
        batchSize: config.options.batchSize,
        concurrency: config.options.concurrency,
        dryRun: config.options.dryRun,
        forceOverwrite: config.options.forceOverwrite,
        useTransactions: config.options.useTransaction,
        imageStrategy: config.options.imageStrategy,
        chunkSize: config.options.chunkSize,
        resume: config.options.resume,
        count: config.options.count,
        bcryptRounds: config.options.bcryptRounds,
      });
    }

    // Create orchestrator and execute
    const orchestrator = new SeedOrchestrator(config);

    if (config.options.dryRun) {
      const validation = await orchestrator.validate();
      if (validation.ok) {
        enhancedLogger.success(validation.message);
        if (cmdOptions.json) {
          console.log(JSON.stringify({ dryRun: true, valid: true, message: validation.message }, null, 2));
        }
        process.exit(0);
      } else {
        enhancedLogger.error(validation.error);
        if (cmdOptions.json) {
          console.log(JSON.stringify({ dryRun: true, valid: false, error: validation.error }, null, 2));
        }
        process.exit(1);
      }
    } else {
      const report = await orchestrator.execute();

      // Print detailed results
      if (report.results.length > 0) {
        console.log("\n");
        enhancedLogger.section("Detailed Results");
        const stats: Record<string, number> = {};
        for (const result of report.results) {
          stats[result.entityName] = result.inserted + result.updated;
          enhancedLogger.info(
            `${result.entityName}: inserted=${result.inserted}, updated=${result.updated}, skipped=${result.skipped}, errors=${result.errors.length}`,
            { duration: `${(result.duration / 1000).toFixed(2)}s` }
          );
        }
        enhancedLogger.summary("Seed Results", stats);
      }

      // Print warnings if any
      if (report.warnings.length > 0) {
        console.log("\n");
        enhancedLogger.section("Warnings");
        for (const warning of report.warnings) {
          enhancedLogger.warn(warning);
        }
      }

      // Print errors if any
      if (report.errors.length > 0) {
        console.log("\n");
        enhancedLogger.section("Errors");
        for (const error of report.errors) {
          enhancedLogger.error(error);
        }
      }

      // Output JSON if requested
      if (cmdOptions.json) {
        console.log(JSON.stringify(report, null, 2));
      }

      // Exit with appropriate code
      process.exit(report.errors.length > 0 ? 1 : 0);
    }
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    const stack = error instanceof Error ? error.stack : undefined;
    console.error(chalk.red("✗ Fatal error:"), message);
    if (process.argv.includes("--verbose") && stack) {
      console.error("Stack:", stack);
    }
    process.exit(1);
  }
}

// Run main when script is executed directly
main();
