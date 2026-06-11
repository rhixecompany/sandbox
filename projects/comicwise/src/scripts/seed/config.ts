/**
 * CLI configuration parser and environment validation
 * @module config
 */

import { Command } from "commander";
import { z } from "zod";

import type { SeedConfig, SeedOptions } from "./types";

/**
 * Zod schema for environment variable validation
 */
const envSchema = z.object({
  DATABASE_URL: z.string().url("DATABASE_URL must be a valid URL"),
  NODE_ENV: z.enum(["development", "production"]).default("development"),
  IMAGEKIT_PUBLIC_KEY: z.string().optional(),
  IMAGEKIT_PRIVATE_KEY: z.string().optional(),
  IMAGEKIT_URL_ENDPOINT: z.string().url().optional(),
});

/**
 * Parse and validate environment variables
 * @returns Validated environment configuration
 * @throws Error if validation fails
 */
export function validateEnv(): z.infer<typeof envSchema> {
  try {
    return envSchema.parse(process.env);
  } catch (error) {
    if (error instanceof z.ZodError) {
      console.error("Environment validation failed:");
      for (const issue of error.issues) {
        console.error(`  ${issue.path.join(".")}: ${issue.message}`);
      }
    }
    throw error;
  }
}

/**
 * Parse CLI arguments and create seed configuration
 * @returns Populated SeedConfig object
 */
export function parseCliArgs(): SeedConfig {
  const program = new Command();

  let config: null | SeedConfig = null;

  program.name("seed").description("Database seeding system for ComicWise").version("1.0.0");

  program
    .command("seed [entities...]")
    .description("Seed database entities")
    .option("--batch-size <number>", "Number of records per batch (default: 500)", "500")
    .option("--concurrency <number>", "Concurrent batch operations (default: 10)", "10")
    .option("--verbose", "Enable verbose logging")
    .option("--dry-run", "Validate data without persisting to database")
    .option("--force", "Force overwrite existing data (full upsert mode)")
    .option(
      "--update <mode>",
      'Update mode: "smart" (update if different), "full" (overwrite all), "none" (skip existing)',
      "smart"
    )
    .option("--no-dedupe", "Disable image deduplication (download all images even if duplicate)")
    .option("--no-transaction", "Disable transaction wrapping")
    .option("--skip-validation", "Skip Zod schema validation")
    .option(
      "--image-strategy <mode>",
      'Image handling strategy: "urls", "local", or "imagekit" (default: urls)',
      "urls"
    )
    .action((entities: string[], options: Record<string, unknown>) => {
      // Validate environment
      const env = validateEnv();

      // Validate image strategy
      const validStrategies = ["urls", "local", "imagekit"];
      if (!validStrategies.includes(options.imageStrategy as string)) {
        throw new Error(
          `Invalid image-strategy: ${options.imageStrategy}. Must be one of: ${validStrategies.join(", ")}`
        );
      }

      // Validate batch size and concurrency are positive integers
      const batchSize = parseInt(options.batchSize as string, 10);
      if (isNaN(batchSize) || batchSize < 1) {
        throw new Error("--batch-size must be a positive integer");
      }

      const concurrency = parseInt(options.concurrency as string, 10);
      if (isNaN(concurrency) || concurrency < 1) {
        throw new Error("--concurrency must be a positive integer");
      }

      // Validate update mode
      const validUpdateModes = ["none", "smart", "full"];
      const updateMode = (options.update as string) || "smart";
      if (!validUpdateModes.includes(updateMode)) {
        throw new Error(`--update must be one of: ${validUpdateModes.join(", ")}`);
      }

      // Determine deduplication setting (default: true for local strategy)
      const enableDedupe = options.dedupe !== false;

      // Validate image strategy for required env vars
      if (options.imageStrategy === "imagekit") {
        if (!env.IMAGEKIT_PUBLIC_KEY || !env.IMAGEKIT_PRIVATE_KEY) {
          throw new Error(
            "ImageKit strategy requires IMAGEKIT_PUBLIC_KEY and IMAGEKIT_PRIVATE_KEY environment variables"
          );
        }
      }

      // Build seed options
      const seedOptions: SeedOptions = {
        batchSize,
        concurrency,
        verbose: options.verbose === true,
        dryRun: options.dryRun === true,
        useTransaction: options.transaction !== false,
        skipValidation: options.skipValidation === true,
        forceOverwrite: options.force === true,
        imageStrategy: options.imageStrategy as "imagekit" | "local" | "urls",
        updateMode: updateMode as "full" | "none" | "smart",
        enableDeduplication: enableDedupe,
      };

      // Determine entities to seed
      const entitiesToSeed: SeedConfig["entities"] =
        entities.length === 0 ? ["all"] : (entities as SeedConfig["entities"]);

      // Create config object
      config = {
        entities: entitiesToSeed,
        options: seedOptions,
        timestamp: new Date(),
      };
    });

  // Parse command line arguments
  program.parse(process.argv);

  if (!config) {
    // If no command was run, show help
    program.outputHelp();
    process.exit(1);
  }

  return config;
}

/**
 * Format seed config for logging
 */
export function formatConfig(config: SeedConfig): string {
  return `
Seed Configuration:
  Entities: ${config.entities.join(", ")}
  Batch Size: ${config.options.batchSize}
  Concurrency: ${config.options.concurrency}
  Update Mode: ${config.options.updateMode || "none"}
  Deduplication: ${config.options.enableDeduplication !== false ? "enabled" : "disabled"}
  Dry Run: ${config.options.dryRun}
  Verbose: ${config.options.verbose}
  Image Strategy: ${config.options.imageStrategy}
  Transactions: ${config.options.useTransaction}
`;
}
