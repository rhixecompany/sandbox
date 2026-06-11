/**
 * Simple Terminal Spinner
 * =======================
 * Non-blocking spinner for progress indication without external dependencies
 */

import { ANSI } from "./colors.js";

import type { WriteStream } from "node:tty";

const FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"];

export interface SpinnerOptions {
  message?: string;
  stream?: WriteStream;
  symbol?: string;
}

export class Spinner {
  private message: string;
  private symbol: string;
  private stream: WriteStream;
  private frameIndex: number = 0;
  private intervalId: NodeJS.Timeout | null = null;
  private isRunning: boolean = false;

  constructor(options: SpinnerOptions = {}) {
    this.message = options.message || "Loading...";
    this.symbol = options.symbol || "⏳";
    this.stream = options.stream || process.stderr;
  }

  start(message?: string): void {
    if (this.isRunning) return;

    if (message) {
      this.message = message;
    }

    this.isRunning = true;
    this.frameIndex = 0;

    // Only show spinner if attached to TTY
    if (!this.stream.isTTY) {
      this.stream.write(`${this.message}\n`);
      return;
    }

    this.intervalId = setInterval(() => {
      const frame = FRAMES[this.frameIndex % FRAMES.length];
      const text = `${frame} ${this.message}${ANSI.RESET}`;

      this.stream.write(`\r${text}`);
      this.frameIndex++;
    }, 80);
  }

  succeed(message?: string): void {
    this.stop(message || this.message, "✓");
  }

  fail(message?: string): void {
    this.stop(message || this.message, "✖");
  }

  warn(message?: string): void {
    this.stop(message || this.message, "⚠");
  }

  info(message?: string): void {
    this.stop(message || this.message, "ℹ");
  }

  private stop(message: string, symbol: string): void {
    if (!this.isRunning) return;

    this.isRunning = false;
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }

    if (this.stream.isTTY) {
      this.stream.write(`\r${symbol} ${message}${ANSI.RESET}\n`);
    }
  }

  clear(): void {
    if (!this.isRunning || !this.stream.isTTY) return;

    this.stream.write("\r" + " ".repeat(this.message.length + 3) + "\r");
  }

  destroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
    this.isRunning = false;
  }
}

export function createSpinner(message: string, stream?: WriteStream): Spinner {
  return new Spinner({ message, stream });
}
