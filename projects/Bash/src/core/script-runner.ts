#!/usr/bin/env bun
/**
 * Script Runner
 * Version: 1.0.0
 *
 * Standardized utilities for shell script orchestration
 *
 * Features:
 * - Cross-platform script execution
 * - Dry-run support
 * - Logging and error handling
 * - Process management
 */

import { existsSync } from "fs";

// ─── Types ───────────────────────────────────────────────────────────

export interface ScriptOptions {
  dryRun: boolean;
  verbose: boolean;
  cwd?: string;
  env?: Record<string, string>;
  timeout?: number;
}

export interface ExecResult {
  stdout: string;
  stderr: string;
  exitCode: number;
  duration: number;
}

export interface CommandStep {
  name: string;
  command: string;
  description?: string;
  critical?: boolean; // If false, continue on failure
}

// ─── Script Runner Class ─────────────────────────────────────────────

export class ScriptRunner {
  private opts: ScriptOptions;
  private execLog: ExecResult[] = [];

  constructor(opts: ScriptOptions) {
    this.opts = opts;
  }

  /**
   * Log message to console
   */
  private log(message: string): void {
    const prefix = this.opts.dryRun ? "[DRY-RUN] " : "";

    if (this.opts.verbose || this.opts.dryRun) {
      console.log(`${prefix}${message}`);
    }
  }

  /**
   * Execute shell command
   */
  async exec(cmd: string): Promise<ExecResult> {
    const startTime = Date.now();

    this.log(`Executing: ${cmd}`);

    if (this.opts.dryRun) {
      return {
        stdout: "[dry-run output]",
        stderr: "",
        exitCode: 0,
        duration: 0,
      };
    }

    try {
      const spawnOpts = {
        cwd: this.opts.cwd || process.cwd(),
        env: { ...process.env, ...this.opts.env },
        stdout: "pipe",
        stderr: "pipe",
      };

      const proc = Bun.spawn(cmd.split(" "), spawnOpts as any);

      // Handle timeout if specified
      let timeoutId: Timer | undefined;
      if (this.opts.timeout) {
        timeoutId = setTimeout(() => {
          proc.kill();
        }, this.opts.timeout);
      }

      const stdout = await new Response(proc.stdout).text();
      const stderr = await new Response(proc.stderr).text();
      const exitCode = await proc.exited;

      if (timeoutId) {
        clearTimeout(timeoutId);
      }

      const duration = Date.now() - startTime;

      const result: ExecResult = {
        stdout,
        stderr,
        exitCode,
        duration,
      };

      this.execLog.push(result);

      if (this.opts.verbose) {
        if (stdout) console.log(`[stdout]\n${stdout}`);
        if (stderr) console.error(`[stderr]\n${stderr}`);
        console.log(`[exit code] ${exitCode} (${duration}ms)`);
      }

      return result;
    } catch (error) {
      const duration = Date.now() - startTime;

      const result: ExecResult = {
        stdout: "",
        stderr: String(error),
        exitCode: 1,
        duration,
      };

      this.execLog.push(result);

      return result;
    }
  }

  /**
   * Execute multiple commands in sequence
   */
  async execSequence(commands: string[]): Promise<void> {
    for (const cmd of commands) {
      const result = await this.exec(cmd);

      if (result.exitCode !== 0) {
        throw new Error(`Command failed: ${cmd}\n${result.stderr}`);
      }
    }
  }

  /**
   * Execute commands as a pipeline (A | B | C)
   */
  async execPipeline(commands: string[]): Promise<ExecResult> {
    const pipelineCmd = commands.join(" | ");
    return this.exec(pipelineCmd);
  }

  /**
   * Execute command with steps (structured workflow)
   */
  async execSteps(steps: CommandStep[]): Promise<Map<string, ExecResult>> {
    const results = new Map<string, ExecResult>();

    console.log(`\nExecuting ${steps.length} step(s)...\n`);

    for (const step of steps) {
      console.log(`Step: ${step.name}`);
      if (step.description) {
        console.log(`  ${step.description}`);
      }

      const result = await this.exec(step.command);
      results.set(step.name, result);

      if (result.exitCode !== 0) {
        console.error(`✗ Step failed: ${step.name}`);

        if (step.critical !== false) {
          throw new Error(
            `Critical step failed: ${step.name}\n${result.stderr}`,
          );
        } else {
          console.log(`  (non-critical, continuing...)`);
        }
      } else {
        console.log(`✓ Step completed: ${step.name}\n`);
      }
    }

    return results;
  }

  /**
   * Execute script file (bash, PowerShell, etc.)
   */
  async execScript(
    scriptPath: string,
    args: string[] = [],
  ): Promise<ExecResult> {
    if (!existsSync(scriptPath)) {
      throw new Error(`Script not found: ${scriptPath}`);
    }

    // Detect script type by extension
    const ext = scriptPath.split(".").pop()?.toLowerCase();

    let interpreter: string;
    switch (ext) {
      case "sh":
        interpreter = "bash";
        break;
      case "ps1":
        interpreter = "powershell.exe -NoProfile -File";
        break;
      case "bat":
        interpreter = "cmd.exe /c";
        break;
      case "ts":
        interpreter = "bunx tsx";
        break;
      default:
        throw new Error(`Unsupported script type: ${ext}`);
    }

    const cmd = `${interpreter} ${scriptPath} ${args.join(" ")}`;
    return this.exec(cmd);
  }

  /**
   * Get execution log
   */
  getExecLog(): ExecResult[] {
    return [...this.execLog];
  }

  /**
   * Clear execution log
   */
  clearExecLog(): void {
    this.execLog = [];
  }

  /**
   * Get summary of executions
   */
  getSummary(): string {
    const summary: string[] = ["Execution Summary:", ""];

    let totalDuration = 0;
    let successCount = 0;
    let failureCount = 0;

    for (const result of this.execLog) {
      totalDuration += result.duration;
      if (result.exitCode === 0) {
        successCount++;
      } else {
        failureCount++;
      }
    }

    summary.push(`Total executions: ${this.execLog.length}`);
    summary.push(`Successful:       ${successCount}`);
    summary.push(`Failed:           ${failureCount}`);
    summary.push(`Total duration:   ${totalDuration}ms`);

    return summary.join("\n");
  }
}

// ─── Convenience Functions ───────────────────────────────────────────

/**
 * Create ScriptRunner from command-line arguments
 */
export function createFromArgs(args: string[]): ScriptRunner {
  const dryRun = args.includes("--dry-run");
  const verbose = args.includes("--verbose") || args.includes("-v");

  return new ScriptRunner({ dryRun, verbose });
}

/**
 * Quick execute with default options
 */
export async function quickExec(
  cmd: string,
  opts?: Partial<ScriptOptions>,
): Promise<ExecResult> {
  const runner = new ScriptRunner({
    dryRun: false,
    verbose: false,
    ...opts,
  });

  return runner.exec(cmd);
}

/**
 * Execute with dry-run support
 */
export async function execWithDryRun(
  cmd: string,
  dryRun: boolean,
): Promise<ExecResult> {
  const runner = new ScriptRunner({
    dryRun,
    verbose: true,
  });

  return runner.exec(cmd);
}

// ─── Platform Detection ──────────────────────────────────────────────

export function getPlatform(): "windows" | "linux" | "darwin" {
  const platform = process.platform;

  if (platform === "win32") return "windows";
  if (platform === "darwin") return "darwin";
  return "linux";
}

export function getShellCommand(): string {
  const platform = getPlatform();

  switch (platform) {
    case "windows":
      return "powershell.exe";
    case "darwin":
    case "linux":
    default:
      return "bash";
  }
}

export function getScriptExtension(): string {
  const platform = getPlatform();

  switch (platform) {
    case "windows":
      return ".ps1";
    case "darwin":
    case "linux":
    default:
      return ".sh";
  }
}

// ─── Error Handling ──────────────────────────────────────────────────

export class ScriptExecutionError extends Error {
  constructor(
    message: string,
    public readonly result: ExecResult,
  ) {
    super(message);
    this.name = "ScriptExecutionError";
  }
}

/**
 * Throw error if command fails
 */
export function assertSuccess(result: ExecResult, cmd: string): void {
  if (result.exitCode !== 0) {
    throw new ScriptExecutionError(
      `Command failed: ${cmd}\n${result.stderr}`,
      result,
    );
  }
}
