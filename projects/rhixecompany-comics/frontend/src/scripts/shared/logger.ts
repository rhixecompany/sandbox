/**
 * Structured Logging Utility
 * ==========================
 * Simple logging functions with consistent formatting
 */

import { ANSI, error, info, muted, success, warning } from "./colors.js";

export interface LoggerOptions {
  prefix?: string;
  quiet?: boolean;
  verbose?: boolean;
}

export class Logger {
  private verbose: boolean;
  private quiet: boolean;
  private prefix: string;

  constructor(options: LoggerOptions = {}) {
    this.verbose = options.verbose ?? false;
    this.quiet = options.quiet ?? false;
    this.prefix = options.prefix ?? "";
  }

  private getPrefix(): string {
    return this.prefix ? `[${this.prefix}] ` : "";
  }

  success(message: string): void {
    if (!this.quiet) {
      console.log(success(`${this.getPrefix()}${message}`));
    }
  }

  error(message: string): void {
    console.error(error(`${this.getPrefix()}${message}`));
  }

  warn(message: string): void {
    if (!this.quiet) {
      console.log(warning(`${this.getPrefix()}${message}`));
    }
  }

  info(message: string): void {
    if (!this.quiet) {
      console.log(info(`${this.getPrefix()}${message}`));
    }
  }

  debug(message: string): void {
    if (this.verbose && !this.quiet) {
      console.log(muted(`${this.getPrefix()}[DEBUG] ${message}`));
    }
  }

  section(title: string): void {
    if (!this.quiet) {
      console.log(`\n${ANSI.BOLD}${ANSI.CYAN}${title}${ANSI.RESET}`);
    }
  }

  table(data: Record<string, unknown>[]): void {
    if (!this.quiet) {
      console.table(data);
    }
  }

  json(label: string, data: unknown): void {
    if (this.verbose && !this.quiet) {
      console.log(`${label}:`, JSON.stringify(data, null, 2));
    }
  }

  divider(): void {
    if (!this.quiet) {
      console.log(muted("─".repeat(50)));
    }
  }

  blank(): void {
    if (!this.quiet) {
      console.log();
    }
  }
}

export function createLogger(prefix: string, options: Omit<LoggerOptions, "prefix"> = {}): Logger {
  return new Logger({ ...options, prefix });
}
