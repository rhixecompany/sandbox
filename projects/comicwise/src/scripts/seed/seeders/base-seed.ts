import { dataLoader } from "../data-loader";
import { BatchProcessor } from "../database/batch-processor";
import { TransactionManager } from "../database/transaction-manager";
import { ProgressTracker } from "../helpers/progress-tracker";
import { logger } from "../logger";

import type { z } from "zod";
import type { EntityResult, LookupCache, SeederMetadata, SeedError, SeedOptions } from "../types";

/**
 * Rollback strategy for a seeder
 */
export interface RollbackStrategy {
  conditions?: Record<string, unknown>; // WHERE clause
  tables: string[]; // affected tables
  type: "delete" | "none" | "restore" | "transaction";
}

/**
 * Abstract base seeder class implementing template method pattern.
 * All entity seeders (user, comic, chapter, etc.) extend this class.
 *
 * Template method flow:
 * 1. seed() - orchestrates entire seeding process
 * 2. loadData() - loads from JSON sources
 * 3. validateData() - validates with Zod schema
 * 4. processBatches() - inserts via BatchProcessor
 * 5. Returns aggregated EntityResult
 */
export abstract class BaseSeeder<T> {
  protected entityName: string;
  protected schema: z.ZodType;
  protected cache: LookupCache;
  protected options: SeedOptions;
  protected dependencies: string[] = [];

  constructor(entityName: string, schema: z.ZodType, cache: LookupCache, options: SeedOptions) {
    this.entityName = entityName;
    this.schema = schema;
    this.cache = cache;
    this.options = options;
  }

  /**
   * Get metadata for this seeder
   * Override in subclasses to declare dependencies
   */
  getMetadata(): SeederMetadata {
    return {
      entityName: this.entityName,
      dependencies: this.dependencies,
      priority: 5,
      supportsRollback: true,
      description: `Seeds ${this.entityName} entity`,
    };
  }

  /**
   * Get rollback strategy for this entity
   * Override in subclasses to customize rollback behavior
   */
  getRollbackStrategy(): RollbackStrategy {
    return {
      type: "delete",
      tables: [this.entityName],
      conditions: { createdAt: { $gte: new Date(Date.now() - 60000) } },
    };
  }

  /**
   * Template method: orchestrates entire seeding process
   * Load → Validate → Dry-run check → Insert → Return result
   */
  async seed(): Promise<EntityResult> {
    const startTime = Date.now();

    logger.section(`Seeding ${this.entityName}`);

    try {
      // Step 1: Load data from sources
      logger.progress(`Loading data...`);
      const rawData = await this.loadData();

      if (rawData.length === 0) {
        logger.warn(`No data found for ${this.entityName}`);
        return {
          entityName: this.entityName,
          inserted: 0,
          updated: 0,
          skipped: 0,
          errors: [],
          duration: Date.now() - startTime,
          success: true,
        };
      }

      logger.success(`Loaded ${rawData.length} records`);

      // Step 2: Validate data with schema
      logger.progress(`Validating ${rawData.length} records...`);
      const validatedData = await this.validateData(rawData);
      logger.success(
        `Validation complete: ${validatedData.length} valid, ${rawData.length - validatedData.length} errors`
      );

      // Step 3: Check dry-run mode
      if (this.options.dryRun) {
        logger.warn("DRY RUN: No data will be persisted to database");
        return {
          entityName: this.entityName,
          inserted: validatedData.length,
          updated: 0,
          skipped: 0,
          errors: [],
          duration: Date.now() - startTime,
          success: true,
        };
      }

      // Step 4: Process batches and insert
      logger.progress(
        `Processing in batches (batch-size=${this.options.batchSize}, concurrency=${this.options.concurrency})...`
      );

      // If chunked seeding is enabled, prefer chunked processing with checkpointing/resume support
      let result: { errors: import("../types").SeedError[]; inserted: number; skipped: number; updated: number };
      if (this.options.chunkSize && this.options.chunkSize > 0) {
        logger.progress(
          `Processing in chunks (chunkSize=${this.options.chunkSize}, batchSize=${this.options.batchSize})...`
        );
        result = await this.processInChunks(validatedData);
      } else {
        result = await this.processBatches(validatedData);
      }

      // Calculate and log final metrics
      const duration = Date.now() - startTime;

      logger.success(`${this.entityName} seeding completed`);
      logger.progress(
        `Inserted: ${result.inserted} | Updated: ${result.updated} | Skipped: ${result.skipped} | Errors: ${result.errors.length} | Duration: ${(duration / 1000).toFixed(1)}s`
      );

      return {
        entityName: this.entityName,
        inserted: result.inserted,
        updated: result.updated,
        skipped: result.skipped,
        errors: result.errors,
        duration,
        success: result.errors.length === 0,
      };
    } catch (error) {
      const duration = Date.now() - startTime;
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`Failed to seed ${this.entityName}: ${message}`);

      return {
        entityName: this.entityName,
        inserted: 0,
        updated: 0,
        skipped: 0,
        errors: [
          {
            itemIndex: 0,
            value: null,
            message: `Seeding failed: ${message}`,
          },
        ],
        duration,
        success: false,
      };
    }
  }

  /**
   * Load data from JSON sources with fallback pattern
   * Subclasses define sources via abstract getDataSources()
   */
  protected async loadData(): Promise<T[]> {
    const sources = this.getDataSources();

    if (sources.length === 0) {
      logger.debug(`${this.entityName} has no data sources (predefined data)`);
      return [] as T[];
    }

    const allData: T[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<T>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} records from ${source}`);
      } catch (error) {
        logger.warn(`Failed to load ${source}: ${error}`);
      }
    }

    return allData;
  }

  /**
   * Validate data against Zod schema
   * Returns only valid records; logs errors if verbose
   */
  protected async validateData(data: T[]): Promise<T[]> {
    if (this.options.skipValidation) {
      logger.debug(`Skipping validation for ${this.entityName}`);
      return data;
    }

    const validated: T[] = [];
    const validationErrors: SeedError[] = [];

    for (let i = 0; i < data.length; i++) {
      const result = this.schema.safeParse(data[i]);

      if (result.success) {
        validated.push(result.data as T);
      } else {
        const message = result.error.issues[0]?.message || "Validation failed";
        validationErrors.push({
          itemIndex: i,
          value: data[i],
          message,
        });

        if (this.options.verbose) {
          logger.debug(`Item ${i} validation error: ${message}`);
        }
      }
    }

    if (validationErrors.length > 0 && this.options.verbose) {
      logger.warn(`${validationErrors.length}/${data.length} records failed validation`);
    }

    return validated;
  }

  /**
   * Process validated data in batches with concurrency control
   * Uses BatchProcessor for parallel processing and ProgressTracker for metrics
   */
  protected async processBatches(data: T[]): Promise<{
    errors: SeedError[];
    inserted: number;
    skipped: number;
    updated: number;
  }> {
    const progressTracker = new ProgressTracker(this.entityName, data.length);
    let totalInserted = 0;
    let totalUpdated = 0;
    let totalSkipped = 0;
    const allErrors: SeedError[] = [];

    // Wrap insertBatch with transaction handling
    const processor = async (item: unknown, _index: number): Promise<void> => {
      const typedItem = item as T;
      try {
        const operation = async () => {
          const result = await this.insertBatch([typedItem]);
          totalInserted += result.inserted;
          totalUpdated += result.updated;
          totalSkipped += result.skipped;
          allErrors.push(...result.errors);
          progressTracker.recordInsert(1);
        };

        if (this.options.useTransaction) {
          await TransactionManager.withTransaction(this.entityName, this.options, operation);
        } else {
          await operation();
        }
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        progressTracker.recordError(1);
        allErrors.push({
          itemIndex: -1,
          value: typedItem,
          message,
        });

        if (this.options.verbose) {
          logger.debug(`Error processing item: ${message}`);
        }
      }
    };

    const batchProcessor = new BatchProcessor({
      batchSize: this.options.batchSize ?? 100,
      concurrency: this.options.concurrency ?? 5,
      onBatchComplete: async (result) => {
        logger.debug(`Batch ${result.batchIndex} processed`);
      },
      onError: async (error) => {
        if (this.options.verbose) {
          logger.debug(`Batch error: ${error.message}`);
        }
      },
    });

    const result = await batchProcessor.process(data, processor, this.entityName);

    return {
      inserted: totalInserted,
      updated: totalUpdated,
      skipped: totalSkipped,
      errors:
        allErrors.length > 0
          ? allErrors
          : result.errors.map((err) => ({
              itemIndex: err.index,
              value: data[err.index],
              message: err.error.message,
            })),
    };
  }

  /**
   * Process data in chunked mode with checkpointing and resume support.
   * This will split the validated data into chunks (this.options.chunkSize) and
   * process each chunk by delegating to processBatches. After each successful
   * chunk, a checkpoint file is written so the seeding process can be resumed.
   */
  protected async processInChunks(data: T[]): Promise<{
    errors: SeedError[];
    inserted: number;
    skipped: number;
    updated: number;
  }> {
    const chunkSize = this.options.chunkSize ?? 0;
    if (chunkSize <= 0) {
      // Fallback to batch processing
      return this.processBatches(data);
    }

    const fs = await import("node:fs");
    const path = await import("node:path");

    const checkpointDir = this.options.checkpointDir || path.join(process.cwd(), ".seed-checkpoints");
    const checkpointFile = path.join(checkpointDir, `${this.entityName}.checkpoint.json`);

    // Ensure checkpoint directory exists
    try {
      if (!fs.existsSync(checkpointDir)) {
        fs.mkdirSync(checkpointDir, { recursive: true });
      }
    } catch (err) {
      // Non-fatal, log and continue
      logger.warn(`Failed to create checkpoint directory ${checkpointDir}: ${String(err)}`);
    }

    // Load checkpoint if resume is requested
    let resumeIndex = 0;
    if (this.options.resume && fs.existsSync(checkpointFile)) {
      try {
        const raw = fs.readFileSync(checkpointFile, "utf8");
        const parsed = JSON.parse(raw) as { lastCompletedChunk?: number };
        resumeIndex = typeof parsed.lastCompletedChunk === "number" ? parsed.lastCompletedChunk + 1 : 0;
        logger.info(`Resuming ${this.entityName} seeding from chunk ${resumeIndex}`);
      } catch (err) {
        logger.warn(`Failed to load checkpoint file ${checkpointFile}: ${String(err)}`);
      }
    }

    const totalChunks = Math.ceil(data.length / chunkSize);
    let accumulatedInserted = 0;
    let accumulatedUpdated = 0;
    let accumulatedSkipped = 0;
    const accumulatedErrors: SeedError[] = [];

    for (let chunkIndex = resumeIndex; chunkIndex < totalChunks; chunkIndex++) {
      const start = chunkIndex * chunkSize;
      const end = Math.min(start + chunkSize, data.length);
      const chunk = data.slice(start, end);

      logger.section(
        `${this.entityName} - Processing chunk ${chunkIndex + 1}/${totalChunks} (${chunk.length} records)`
      );

      try {
        // Delegate to existing batch processor which respects batchSize/concurrency
        const res = await this.processBatches(chunk);
        accumulatedInserted += res.inserted;
        accumulatedUpdated += res.updated;
        accumulatedSkipped += res.skipped;
        accumulatedErrors.push(...res.errors);

        // Write checkpoint after successful chunk
        try {
          const checkpointData = {
            lastCompletedChunk: chunkIndex,
            timestamp: new Date().toISOString(),
            inserted: accumulatedInserted,
            updated: accumulatedUpdated,
            skipped: accumulatedSkipped,
            errors: accumulatedErrors.length,
          };
          fs.writeFileSync(checkpointFile, JSON.stringify(checkpointData, null, 2), "utf8");
        } catch (err) {
          logger.warn(`Failed to write checkpoint for ${this.entityName} chunk ${chunkIndex}: ${String(err)}`);
        }

        // If configured to pause between chunks, respect it (throttle large imports)
        if (this.options.pauseBetweenChunksMs && this.options.pauseBetweenChunksMs > 0) {
          await new Promise((resolve) => setTimeout(resolve, this.options.pauseBetweenChunksMs));
        }
      } catch (err) {
        const message = err instanceof Error ? err.message : String(err);
        logger.error(`Chunk ${chunkIndex} processing failed: ${message}`);
        accumulatedErrors.push({ itemIndex: -1, value: null, message });

        // On error, if failOnError is set, abort and return aggregated errors
        if (this.options.failOnError) {
          return {
            errors: accumulatedErrors,
            inserted: accumulatedInserted,
            skipped: accumulatedSkipped,
            updated: accumulatedUpdated,
          };
        }

        // Otherwise, continue with next chunk after logging
      }
    }

    // Cleanup checkpoint file on successful completion
    try {
      if (fs.existsSync(checkpointFile)) {
        fs.unlinkSync(checkpointFile);
      }
    } catch (err) {
      logger.warn(`Failed to remove checkpoint file ${checkpointFile}: ${String(err)}`);
    }

    return {
      errors: accumulatedErrors,
      inserted: accumulatedInserted,
      skipped: accumulatedSkipped,
      updated: accumulatedUpdated,
    };
  }

  /**
   * Abstract methods - must be implemented by subclasses
   */

  /**
   * Get data source file names (without extension)
   * Example: ["comic.json"] returns ["comic"]
   * Supports multi-file fallback: comic.json → comic-data1.json → comic-data2.json
   */
  protected abstract getDataSources(): string[];

  /**
   * Get the unique field for this entity
   * Used for deduplication and conflict resolution
   * Examples: "email" for users, "slug" for comics
   */
  protected abstract getUniqueField(): string;

  /**
   * Transform raw data to database-ready format
   * Resolves relations, extracts values, handles special cases
   */
  protected abstract transformData(raw: T): Promise<unknown>;

  /**
   * Insert batch of items to database
   * Handles conflict resolution, transactions, image processing
   * Called within processBatches
   */
  protected abstract insertBatch(data: T[]): Promise<EntityResult>;
}
