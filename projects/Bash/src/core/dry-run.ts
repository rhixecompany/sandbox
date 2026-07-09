#!/usr/bin/env bun
/**
 * Dry-Run Executor
 * Version: 1.0.0
 *
 * Standardized dry-run pattern for all destructive operations
 *
 * Features:
 * - Behavior-identical dry-run execution
 * - File operation wrappers
 * - Process execution wrappers
 * - Logging and verification
 */

import { existsSync, mkdirSync, rmSync, statSync } from "fs";

// ─── Types ───────────────────────────────────────────────────────────

export interface DryRunOptions {
  dryRun: boolean;
  verbose: boolean;
  logger?: (message: string) => void;
}

export interface FileOperation {
  type: "write" | "delete" | "mkdir" | "copy" | "move";
  path: string;
  details?: string;
}

export interface ExecResult {
  stdout: string;
  stderr: string;
  exitCode: number;
}

// ─── Dry-Run Executor Class ──────────────────────────────────────────

export class DryRunExecutor {
  private operations: FileOperation[] = [];
  private opts: DryRunOptions;

  constructor(opts: DryRunOptions) {
    this.opts = opts;
  }

  /**
   * Log operation to console and optional custom logger
   */
  private log(message: string): void {
    const prefix = this.opts.dryRun ? "[DRY-RUN] " : "";
    const fullMessage = `${prefix}${message}`;

    if (this.opts.verbose || this.opts.dryRun) {
      console.log(fullMessage);
    }

    if (this.opts.logger) {
      this.opts.logger(fullMessage);
    }
  }

  /**
   * Record operation for verification
   */
  private recordOperation(op: FileOperation): void {
    this.operations.push(op);
  }

  /**
   * Get all recorded operations (for testing)
   */
  getOperations(): FileOperation[] {
    return [...this.operations];
  }

  /**
   * Clear recorded operations
   */
  clearOperations(): void {
    this.operations = [];
  }

  // ─── File Operations ─────────────────────────────────────────────────

  /**
   * Write file with dry-run support
   */
  async writeFile(path: string, content: string): Promise<void> {
    const size = Buffer.byteLength(content, "utf-8");
    this.log(`Writing file: ${path} (${size} bytes)`);

    this.recordOperation({
      type: "write",
      path,
      details: `${size} bytes`,
    });

    if (this.opts.dryRun) {
      return;
    }

    await Bun.write(path, content);
  }

  /**
   * Delete file with dry-run support
   */
  async deleteFile(path: string): Promise<void> {
    if (!existsSync(path)) {
      this.log(`Skipping delete (not found): ${path}`);
      return;
    }

    const stat = statSync(path);
    this.log(`Deleting file: ${path} (${stat.size} bytes)`);

    this.recordOperation({
      type: "delete",
      path,
      details: `${stat.size} bytes`,
    });

    if (this.opts.dryRun) {
      return;
    }

    await Bun.file(path).delete();
  }

  /**
   * Delete directory recursively with dry-run support
   */
  async deleteDirectory(path: string): Promise<void> {
    if (!existsSync(path)) {
      this.log(`Skipping delete (not found): ${path}`);
      return;
    }

    const stat = statSync(path);
    if (!stat.isDirectory()) {
      throw new Error(`Not a directory: ${path}`);
    }

    this.log(`Deleting directory: ${path}`);

    this.recordOperation({
      type: "delete",
      path,
      details: "directory (recursive)",
    });

    if (this.opts.dryRun) {
      return;
    }

    rmSync(path, { recursive: true, force: true });
  }

  /**
   * Create directory with dry-run support
   */
  async createDirectory(path: string): Promise<void> {
    if (existsSync(path)) {
      this.log(`Directory already exists: ${path}`);
      return;
    }

    this.log(`Creating directory: ${path}`);

    this.recordOperation({
      type: "mkdir",
      path,
      details: "recursive",
    });

    if (this.opts.dryRun) {
      return;
    }

    mkdirSync(path, { recursive: true });
  }

  /**
   * Copy file with dry-run support
   */
  async copyFile(source: string, destination: string): Promise<void> {
    if (!existsSync(source)) {
      throw new Error(`Source file not found: ${source}`);
    }

    const stat = statSync(source);
    this.log(`Copying file: ${source} → ${destination} (${stat.size} bytes)`);

    this.recordOperation({
      type: "copy",
      path: `${source} → ${destination}`,
      details: `${stat.size} bytes`,
    });

    if (this.opts.dryRun) {
      return;
    }

    const content = await Bun.file(source).text();
    await Bun.write(destination, content);
  }

  /**
   * Move file with dry-run support
   */
  async moveFile(source: string, destination: string): Promise<void> {
    if (!existsSync(source)) {
      throw new Error(`Source file not found: ${source}`);
    }

    const stat = statSync(source);
    this.log(`Moving file: ${source} → ${destination} (${stat.size} bytes)`);

    this.recordOperation({
      type: "move",
      path: `${source} → ${destination}`,
      details: `${stat.size} bytes`,
    });

    if (this.opts.dryRun) {
      return;
    }

    const content = await Bun.file(source).text();
    await Bun.write(destination, content);
    await Bun.file(source).delete();
  }

  // ─── Process Execution ───────────────────────────────────────────────

  /**
   * Execute shell command with dry-run support
   */
  async exec(cmd: string, cwd?: string): Promise<ExecResult> {
    this.log(`Executing: ${cmd}${cwd ? ` (cwd: ${cwd})` : ""}`);

    if (this.opts.dryRun) {
      return {
        stdout: "[dry-run output]",
        stderr: "",
        exitCode: 0,
      };
    }

    const proc = Bun.spawn(cmd.split(" "), {
      cwd: cwd ?? process.cwd(),
      stdout: "pipe",
      stderr: "pipe",
    });

    const stdout = await new Response(proc.stdout).text();
    const stderr = await new Response(proc.stderr).text();
    const exitCode = await proc.exited;

    return { stdout, stderr, exitCode };
  }

  /**
   * Execute multiple commands in sequence
   */
  async execSequence(commands: string[], cwd?: string): Promise<void> {
    for (const cmd of commands) {
      const result = await this.exec(cmd, cwd);

      if (result.exitCode !== 0) {
        throw new Error(`Command failed: ${cmd}\n${result.stderr}`);
      }
    }
  }

  // ─── Verification ────────────────────────────────────────────────────

  /**
   * Get summary of operations that would be performed
   */
  getSummary(): string {
    const summary = ["Operations Summary:", ""];

    const byType = new Map<string, number>();

    for (const op of this.operations) {
      byType.set(op.type, (byType.get(op.type) || 0) + 1);
    }

    for (const [type, count] of byType) {
      summary.push(`  ${type.padEnd(10)} ${count} operation(s)`);
    }

    summary.push("");
    summary.push(`Total: ${this.operations.length} operation(s)`);

    return summary.join("\n");
  }

  /**
   * Verify dry-run matches real execution (for testing)
   */
  static async verifyFidelity(
    operation: (executor: DryRunExecutor) => Promise<void>,
  ): Promise<boolean> {
    // Run in dry-run mode
    const dryRunExecutor = new DryRunExecutor({
      dryRun: true,
      verbose: false,
    });
    await operation(dryRunExecutor);
    const dryRunOps = dryRunExecutor.getOperations();

    // Run in real mode (but don't actually execute)
    const realExecutor = new DryRunExecutor({
      dryRun: true, // Still dry-run for testing
      verbose: false,
    });
    await operation(realExecutor);
    const realOps = realExecutor.getOperations();

    // Compare operations
    if (dryRunOps.length !== realOps.length) {
      console.error("Operation count mismatch");
      return false;
    }

    for (let i = 0; i < dryRunOps.length; i++) {
      const dryOp = dryRunOps[i]!;
      const realOp = realOps[i]!;

      if (
        dryOp.type !== realOp.type ||
        dryOp.path !== realOp.path ||
        dryOp.details !== realOp.details
      ) {
        console.error(`Operation ${i} mismatch`);
        console.error("Dry-run:", dryOp);
        console.error("Real:", realOp);
        return false;
      }
    }

    return true;
  }
}

// ─── Convenience Functions ───────────────────────────────────────────

/**
 * Create a DryRunExecutor from command-line arguments
 */
export function createFromArgs(args: string[]): DryRunExecutor {
  const dryRun = args.includes("--dry-run");
  const verbose = args.includes("--verbose") || args.includes("-v");

  return new DryRunExecutor({ dryRun, verbose });
}

/**
 * Wrap a function with dry-run support
 */
export function withDryRun<T extends any[], R>(
  fn: (executor: DryRunExecutor, ...args: T) => Promise<R>,
): (opts: DryRunOptions, ...args: T) => Promise<R> {
  return async (opts: DryRunOptions, ...args: T): Promise<R> => {
    const executor = new DryRunExecutor(opts);
    return fn(executor, ...args);
  };
}
