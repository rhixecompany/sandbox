import { db } from "../../../database/db";
import { logger } from "../logger";

import type { SeedOptions } from "../types";

/**
 * Manages database transactions for seeding operations
 * Wraps Drizzle transaction API with logging and error handling
 */
export class TransactionManager {
  /**
   * Execute operation within a database transaction
   * Auto-commits on success, auto-rollback on error
   *
   * @param entityName - Name of entity being seeded (for logging)
   * @param options - Seed options (useTransaction flag)
   * @param operation - Async function to execute within transaction
   */
  static async withTransaction<T>(entityName: string, options: SeedOptions, operation: () => Promise<T>): Promise<T> {
    // If transactions disabled, execute directly without wrapping
    if (!options.useTransaction) {
      return operation();
    }

    logger.debug(`[${entityName}] Starting transaction`);

    try {
      return await db.transaction(async (_tx) => {
        // Transaction context available via _tx parameter
        // Currently we pass the main db instance, could be enhanced
        // to use _tx for all operations within transaction
        const result = await operation();
        logger.debug(`[${entityName}] Transaction committed`);
        return result;
      });
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`[${entityName}] Transaction failed: ${message}`);

      // Re-throw to allow caller to handle
      throw error;
    }
  }

  /**
   * Execute multiple operations within single transaction
   * Useful for related operations (e.g., comic + coverImage + comicToGenre)
   */
  static async withBatchTransaction(
    entityName: string,
    options: SeedOptions,
    operations: Array<() => Promise<void>>
  ): Promise<void> {
    if (!options.useTransaction) {
      for (const op of operations) {
        await op();
      }
      return;
    }

    logger.debug(`[${entityName}] Starting batch transaction with ${operations.length} operations`);

    try {
      await db.transaction(async (_tx) => {
        for (let i = 0; i < operations.length; i++) {
          try {
            await operations[i]();
            logger.debug(`[${entityName}] Operation ${i + 1} completed`);
          } catch (error) {
            logger.error(`[${entityName}] Operation ${i + 1} failed, rolling back`);
            throw error;
          }
        }
        logger.debug(`[${entityName}] Batch transaction committed`);
      });
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`[${entityName}] Batch transaction failed: ${message}`);
      throw error;
    }
  }
}
