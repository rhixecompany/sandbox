/**
 * Logging utility for the seeding system with colored terminal output
 * @module logger
 */

import chalk from "chalk";

/**
 * Structured log entry for JSON export
 */
export interface LogEntry {
  context?: Record<string, unknown>;
  dryRun?: boolean;
  level: "debug" | "error" | "info" | "success" | "warn";
  message: string;
  timestamp: string;
}

/**
 * Logger class with colored output, timestamps, and structured JSON support
 */
export class Logger {
  private verbose: boolean = false;
  private dryRun: boolean = false;
  private logs: LogEntry[] = [];
  private startTime = Date.now();

  /**
   * Create a new Logger instance
   * @param verbose - Enable debug/verbose output
   * @param dryRun - Indicate dry-run mode in logging
   */
  constructor(verbose: boolean = false, dryRun: boolean = false) {
    this.verbose = verbose;
    this.dryRun = dryRun;
  }

  /**
   * Internal logging method with timestamps and JSON recording
   */
  private log(level: LogEntry["level"], message: string, context?: Record<string, unknown>): void {
    const entry: LogEntry = {
      timestamp: new Date().toISOString(),
      level,
      message,
      context,
      dryRun: this.dryRun,
    };

    this.logs.push(entry);

    const icons: Record<string, string> = {
      info: chalk.blue("ℹ"),
      success: chalk.green("✓"),
      warn: chalk.yellow("⚠"),
      error: chalk.red("✗"),
      debug: chalk.gray("➤"),
    };

    const prefix = this.dryRun ? chalk.gray("[DRY-RUN]") : "";
    const timestamp = chalk.gray(`[${new Date().toLocaleTimeString()}]`);

    if (this.verbose || level !== "debug") {
      const contextStr = context ? " " + JSON.stringify(context) : "";
      console.log(`${prefix} ${icons[level]} ${timestamp} ${message}${contextStr}`);
    }
  }

  /**
   * Log an informational message (blue)
   */
  info(message: string, context?: Record<string, unknown>): void {
    this.log("info", message, context);
  }

  /**
   * Log a success message (green)
   */
  success(message: string, context?: Record<string, unknown>): void {
    this.log("success", message, context);
  }

  /**
   * Log a warning message (yellow)
   */
  warn(message: string, context?: Record<string, unknown>): void {
    this.log("warn", message, context);
  }

  /**
   * Log an error message (red)
   */
  error(message: string, context?: Record<string, unknown>): void {
    this.log("error", message, context);
  }

  /**
   * Log a debug message (gray) - only shown when verbose is true
   */
  debug(message: string, context?: Record<string, unknown>): void {
    if (this.verbose) {
      this.log("debug", message, context);
    }
  }

  /**
   * Log a section header with visual separator
   */
  section(title: string): void {
    console.log("\n" + chalk.cyan.bold("━".repeat(50)));
    console.log(chalk.cyan.bold(`  ${title}`));
    console.log(chalk.cyan.bold("━".repeat(50)) + "\n");
  }

  /**
   * Log a progress/action message (white)
   */
  progress(message: string): void {
    console.log(chalk.white("→"), message);
  }

  /**
   * Log a table of data
   */
  table(data: Record<string, unknown>[]): void {
    console.table(data);
  }

  /**
   * Get elapsed time since logger creation
   */
  elapsed(): string {
    const ms = Date.now() - this.startTime;
    if (ms < 1000) return `${ms}ms`;
    return `${(ms / 1000).toFixed(1)}s`;
  }

  /**
   * Export logs as JSON (for CI/CD pipelines and automation)
   */
  toJSON(): LogEntry[] {
    return this.logs;
  }

  /**
   * Print a summary report with statistics
   */
  summary(title: string, stats: Record<string, number>): void {
    console.log("\n" + chalk.bold(`━━━ ${title} ━━━`));
    for (const [key, value] of Object.entries(stats)) {
      console.log(`  ${key}: ${chalk.cyan(String(value))}`);
    }
    console.log(`  Duration: ${chalk.cyan(this.elapsed())}`);
    if (this.dryRun) {
      console.log(chalk.yellow(`  [DRY-RUN MODE – No changes persisted]`));
    }
    console.log();
  }

  /**
   * Set verbosity level
   */
  setVerbose(verbose: boolean): void {
    this.verbose = verbose;
  }
}

/**
 * Singleton instance of the Logger
 */
export const logger = new Logger();
