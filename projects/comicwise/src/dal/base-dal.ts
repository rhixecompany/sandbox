/**
 * Base Data Access Layer (DAL) class
 * Provides common patterns for database operations
 *
 * All DAL classes should extend this base to ensure consistency
 * in error handling, logging, and type safety.
 */

export interface DalOptions {
  limit?: number;
  offset?: number;
}

export abstract class BaseDal<T> {
  /**
   * List items with optional pagination
   */
  abstract list(options?: DalOptions): Promise<T[]>;

  /**
   * Get a single item by ID
   */
  abstract getById(id: number | string): Promise<null | T>;

  /**
   * Create a new item
   */
  abstract create(data: unknown): Promise<T>;

  /**
   * Update an existing item
   */
  abstract update(id: number | string, data: unknown): Promise<null | T>;

  /**
   * Delete an item
   */
  abstract delete?(id: number | string): Promise<void>;

  /**
   * Shared error handler for database operations
   */
  protected handleError(error: unknown, operation: string): never {
    console.error(`[${this.constructor.name}] ${operation} failed:`, error);

    if (error instanceof Error) {
      if (error.message.includes("UNIQUE")) {
        throw new Error("This record already exists");
      }
      if (error.message.includes("FOREIGN KEY")) {
        throw new Error("Related record not found");
      }
      if (error.message.includes("NOT NULL")) {
        throw new Error("Required field is missing");
      }
    }

    throw new Error(`Failed to ${operation.toLowerCase()}`);
  }
}
