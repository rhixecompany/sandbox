/**
 * Logging utilities with rotation support
 */

import { dim } from "./colors.js";

export type LogLevel = "debug" | "info" | "warn" | "error";

const LOG_LEVELS: Record<LogLevel, number> = {
  debug: 0,
  info: 1,
  warn: 2,
  error: 3,
};

let currentLevel: LogLevel = "info";

export function setLogLevel(level: LogLevel) {
  currentLevel = level;
}

function shouldLog(level: LogLevel): boolean {
  return LOG_LEVELS[level] >= LOG_LEVELS[currentLevel];
}

function timestamp(): string {
  return new Date().toISOString();
}

export const log = {
  debug: (msg: string) =>
    shouldLog("debug") && console.error(dim(`[${timestamp()}] DEBUG: ${msg}`)),
  info: (msg: string) =>
    shouldLog("info") && console.log(`[${timestamp()}] ${msg}`),
  warn: (msg: string) =>
    shouldLog("warn") && console.warn(`[${timestamp()}] WARN: ${msg}`),
  error: (msg: string) =>
    shouldLog("error") && console.error(`[${timestamp()}] ERROR: ${msg}`),
};

/**
 * Simple file logger — appends to a log file
 * For full rotation, use log-rotate.sh
 */
export class FileLogger {
  private path: string;
  private lines: string[] = [];

  constructor(path: string) {
    this.path = path;
  }

  append(level: LogLevel, msg: string) {
    const line = `[${timestamp()}] [${level.toUpperCase()}] ${msg}`;
    this.lines.push(line);
  }

  async flush() {
    if (this.lines.length === 0) return;
    const { writeFile, appendFile } = await import("fs/promises");
    if (this.lines.length > 50) {
      await writeFile(this.path, this.lines.join("\n") + "\n", { flag: "a" });
    } else {
      await appendFile(this.path, this.lines.join("\n") + "\n");
    }
    this.lines = [];
  }
}
