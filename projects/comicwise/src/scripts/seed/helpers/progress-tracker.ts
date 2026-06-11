/**
 * Progress tracking for batch seeding operations with metrics logging
 * @module progressTracker
 */

import chalk from "chalk";

import type { ProgressMetrics } from "../types";

/**
 * ProgressTracker monitors and logs progress of seeding operations
 * Logs metrics every 50 items or every 5 seconds, whichever comes first
 */
export class ProgressTracker {
  private taskName: string;
  private total: number;
  private inserted: number = 0;
  private updated: number = 0;
  private skipped: number = 0;
  private errors: number = 0;
  private startTime: number;
  private lastLogTime: number;
  private lastLogCount: number = 0;
  private lastLogInterval: NodeJS.Timeout | null = null;

  /**
   * Create a new ProgressTracker instance
   * @param taskName - Name of the task being tracked
   * @param total - Total number of items to process
   */
  constructor(taskName: string, total: number) {
    this.taskName = taskName;
    this.total = total;
    this.startTime = Date.now();
    this.lastLogTime = this.startTime;

    // Set up 5-second interval logging
    this.lastLogInterval = setInterval(() => {
      this.maybeLog();
    }, 5000);
  }

  /**
   * Record a successful insertion
   */
  recordInsert(count: number = 1): void {
    this.inserted += count;
    this.maybeLog();
  }

  /**
   * Record an update to existing record
   */
  recordUpdate(count: number = 1): void {
    this.updated += count;
    this.maybeLog();
  }

  /**
   * Record a skipped item (duplicate or validation failure)
   */
  recordSkip(count: number = 1): void {
    this.skipped += count;
    this.maybeLog();
  }

  /**
   * Record an error
   */
  recordError(count: number = 1): void {
    this.errors += count;
    this.maybeLog();
  }

  /**
   * Get current progress count
   */
  private getCurrentCount(): number {
    return this.inserted + this.updated + this.skipped + this.errors;
  }

  /**
   * Log progress if thresholds are met (50 items or 5 seconds)
   */
  private maybeLog(): void {
    const currentCount = this.getCurrentCount();
    const now = Date.now();
    const itemsSinceLastLog = currentCount - this.lastLogCount;
    const timeSinceLastLog = now - this.lastLogTime;

    // Log if we've processed 50 items or 5+ seconds have passed
    if (itemsSinceLastLog >= 50 || timeSinceLastLog >= 5000) {
      this.logProgress();
      this.lastLogCount = currentCount;
      this.lastLogTime = now;
    }
  }

  /**
   * Create ASCII progress bar
   */
  private createBar(current: number, total: number): string {
    const barLength = 40;
    const filledLength = Math.round((current / total) * barLength);
    const emptyLength = barLength - filledLength;
    return chalk.green("█".repeat(filledLength)) + chalk.gray("░".repeat(emptyLength));
  }

  /**
   * Log current progress with metrics
   */
  private logProgress(): void {
    const currentCount = this.getCurrentCount();
    const percentage = Math.round((currentCount / this.total) * 100);
    const elapsedSeconds = (Date.now() - this.startTime) / 1000;
    const itemsPerSecond = currentCount > 0 ? (currentCount / elapsedSeconds).toFixed(1) : "0";

    const bar = this.createBar(currentCount, this.total);
    const progressLine = `${bar} ${percentage}% (${currentCount}/${this.total})`;

    console.log(`  ${progressLine}`);
    console.log(
      `  Inserted: ${this.inserted} | Updated: ${this.updated} | Skipped: ${this.skipped} | Errors: ${this.errors} | Speed: ${itemsPerSecond}/sec`
    );
  }

  /**
   * Complete tracking and return final metrics
   * @returns ProgressMetrics with calculated rates and duration
   */
  complete(): ProgressMetrics {
    // Clear the interval
    if (this.lastLogInterval) {
      clearInterval(this.lastLogInterval);
    }

    const duration = (Date.now() - this.startTime) / 1000;
    const totalProcessed = this.getCurrentCount();
    const itemsPerSecond = totalProcessed > 0 ? totalProcessed / duration : 0;
    const successCount = this.inserted + this.updated;
    const successRate = totalProcessed > 0 ? (successCount / totalProcessed) * 100 : 0;

    return {
      taskName: this.taskName,
      total: this.total,
      inserted: this.inserted,
      updated: this.updated,
      skipped: this.skipped,
      errors: this.errors,
      duration,
      itemsPerSecond: parseFloat(itemsPerSecond.toFixed(2)),
      successRate: parseFloat(successRate.toFixed(2)),
    };
  }

  /**
   * Get current metrics without completing
   */
  getCurrentMetrics(): Partial<ProgressMetrics> {
    const duration = (Date.now() - this.startTime) / 1000;
    const totalProcessed = this.getCurrentCount();
    const itemsPerSecond = totalProcessed > 0 ? totalProcessed / duration : 0;

    return {
      taskName: this.taskName,
      total: this.total,
      inserted: this.inserted,
      updated: this.updated,
      skipped: this.skipped,
      errors: this.errors,
      duration,
      itemsPerSecond: parseFloat(itemsPerSecond.toFixed(2)),
    };
  }
}
