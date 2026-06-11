/**
 * Batch processor with concurrent operation support and error isolation
 * @module batchProcessor
 */

import type { BatchProcessorOptions, BatchProcessorResult } from "../types";

/**
 * BatchProcessor handles processing large arrays of items in batches
 * with configurable concurrency, supporting callbacks for progress/error handling
 */
export class BatchProcessor<T> {
  private batchSize: number;
  private concurrency: number;
  private onBatchComplete?: (result: { batchIndex: number; processed: number }) => Promise<void> | void;
  private onError?: (error: Error, itemIndex: number) => Promise<void> | void;

  /**
   * Create a new BatchProcessor instance
   * @param options - Configuration options
   */
  constructor(options: BatchProcessorOptions) {
    this.batchSize = options.batchSize || 100;
    this.concurrency = options.concurrency || 5;
    // Store callbacks as-is; handle both sync and async in caller
    this.onBatchComplete = options.onBatchComplete as unknown as (result: {
      batchIndex: number;
      processed: number;
    }) => Promise<void> | void;
    this.onError = options.onError as unknown as (error: Error, itemIndex: number) => Promise<void> | void;
  }

  /**
   * Process an array of items using batch processing with concurrency control
   * @param items - Array of items to process
   * @param processor - Async function to process each item
   * @param taskName - Name of the task for logging
   * @returns BatchProcessorResult with results and errors
   */
  async process<U>(
    items: T[],
    processor: (item: T, index: number) => Promise<U>,
    _taskName: string = "Batch Processing"
  ): Promise<BatchProcessorResult<U>> {
    const results: U[] = [];
    const errors: Array<{ error: Error; index: number }> = [];
    let totalProcessed = 0;

    // Split items into batches
    const batches: T[][] = [];
    for (let i = 0; i < items.length; i += this.batchSize) {
      batches.push(items.slice(i, i + this.batchSize));
    }

    // Process batches sequentially, but items within a batch concurrently
    for (let batchIndex = 0; batchIndex < batches.length; batchIndex++) {
      const batch = batches[batchIndex];
      const batchResults = await this.processBatchConcurrently(batch, processor, items.indexOf(batch[0]));

      // Collect results and errors
      for (const result of batchResults) {
        if (result.status === "fulfilled") {
          results.push(result.value);
        } else {
          const itemIndex = items.indexOf(batch[batchResults.indexOf(result)]);
          errors.push({
            index: itemIndex,
            error: new Error(
              `Processing failed: ${result.reason instanceof Error ? result.reason.message : String(result.reason)}`
            ),
          });

          // Call error handler if provided
          if (this.onError) {
            try {
              const result = this.onError(errors[errors.length - 1].error, itemIndex);
              if (result instanceof Promise) {
                await result;
              }
            } catch {
              // Silently ignore handler errors
            }
          }
        }
      }

      totalProcessed += batch.length;

      // Call batch completion handler if provided
      if (this.onBatchComplete) {
        try {
          const result = this.onBatchComplete({
            batchIndex,
            processed: totalProcessed,
          });
          if (result instanceof Promise) {
            await result;
          }
        } catch {
          // Silently ignore handler errors
        }
      }
    }

    return {
      results,
      errors,
      totalProcessed,
    };
  }

  /**
   * Process a batch of items concurrently with concurrency limit
   * @param batch - Array of items to process
   * @param processor - Function to process each item
   * @param batchStartIndex - Starting index for error reporting
   * @returns Array of PromiseSettledResult
   */
  private async processBatchConcurrently<U>(
    batch: T[],
    processor: (item: T, index: number) => Promise<U>,
    batchStartIndex: number
  ): Promise<PromiseSettledResult<U>[]> {
    const results: PromiseSettledResult<U>[] = [];

    // Process up to `concurrency` items at a time
    for (let i = 0; i < batch.length; i += this.concurrency) {
      const chunk = batch.slice(i, i + this.concurrency);
      const chunkPromises = chunk.map((item, chunkIndex) =>
        processor(item, batchStartIndex + i + chunkIndex).then((result) => result)
      );

      // Use Promise.allSettled to prevent one failure from stopping the batch
      const chunkResults = await Promise.allSettled(chunkPromises);
      results.push(...chunkResults);
    }

    return results;
  }

  /**
   * Get configuration
   */
  getConfig(): Readonly<{ batchSize: number; concurrency: number }> {
    return {
      batchSize: this.batchSize,
      concurrency: this.concurrency,
    };
  }
}
