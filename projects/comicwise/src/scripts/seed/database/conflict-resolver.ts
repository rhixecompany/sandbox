import type { SeedOptions } from "../types";

/**
 * Conflict resolution strategies for seed data operations
 * Handles onConflictDoUpdate patterns and forceOverwrite behavior
 */
export class ConflictResolver {
  /**
   * Should overwrite existing record on conflict?
   * Based on forceOverwrite flag and entity-specific rules
   */
  static shouldOverwrite(options: SeedOptions, _entityName: string): boolean {
    // Force overwrite flag takes precedence
    if (options.forceOverwrite) {
      return true;
    }

    // Default behavior: skip on conflict (don't update)
    return false;
  }

  /**
   * Prepare upsert-friendly data structure
   * Extracts fields that should be updated on conflict
   */
  static prepareUpsertData(original: Record<string, unknown>, updateFields: string[]): Record<string, unknown> {
    const upsertData: Record<string, unknown> = {};

    for (const field of updateFields) {
      if (field in original) {
        upsertData[field] = original[field];
      }
    }

    return upsertData;
  }

  /**
   * Handle unique constraint violation
   * Returns action: skip | update | error
   */
  static resolveUniqueViolation(options: SeedOptions, _entityName: string): "error" | "skip" | "update" {
    if (options.forceOverwrite) {
      return "update";
    }

    // Default: skip duplicate records
    return "skip";
  }

  /**
   * Handle foreign key violation
   * Missing parent record - examine and report
   */
  static resolveForeignKeyViolation(message: string): {
    field?: string;
    parentEntity?: string;
    suggestion?: string;
  } {
    // Parse common FK violation messages
    // Format: "insert or update on table "child" violates foreign key constraint "child_parent_id_fkey" on table "parent""

    const parentMatch = message.match(/on table "(\w+)"/);
    const parentEntity = parentMatch?.[1];

    return {
      parentEntity,
      suggestion: `Ensure ${parentEntity} records are seeded before this entity`,
    };
  }

  /**
   * Determine retry strategy for failed operations
   */
  static shouldRetry(error: unknown, attemptNumber: number, maxAttempts: number = 3): boolean {
    if (attemptNumber >= maxAttempts) {
      return false;
    }

    const message = error instanceof Error ? error.message.toLowerCase() : "";

    // Retryable errors: connection timeouts, deadlocks, etc.
    const retryablePatterns = ["timeout", "deadlock", "connection", "temporarily unavailable"];

    return retryablePatterns.some((pattern) => message.includes(pattern));
  }
}
