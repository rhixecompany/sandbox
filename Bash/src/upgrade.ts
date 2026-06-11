#!/usr/bin/env bun
/**
 * Enhanced Package Manager Upgrade Script
 * Version: 3.1.0
 *
 * Consolidated TypeScript implementation replacing upgrade.sh/.ps1/.bat
 *
 * Usage:
 *   bun run src/upgrade.ts              # Run normal upgrade
 *   bun run src/upgrade.ts --debug      # Run with debug output
 *   bun run src/upgrade.ts --skip-winget  # Skip winget
 *   bun run src/upgrade.ts --skip-choco   # Skip chocolatey
 */

import { execSync } from "child_process";
import { existsSync, mkdirSync } from "fs";
import { join } from "path";
import { parseArgs, showHelp } from "./lib/cli.js";
import { bold, dim, fail, ok, warn } from "./lib/colors.js";
import { safeExec } from "./lib/errors.js";
import { FileLogger } from "./lib/logging.js";

// ─── Types ───────────────────────────────────────────────────────────

interface UpgradeResult {
  ok: boolean;
  manager: string;
  details: string;
  upgraded: number;
  failed: number;
}

// ─── Helpers ─────────────────────────────────────────────────────────

function runUpgrade(
  manager: string,
  cmd: string,
  timeout: number,
): UpgradeResult {
  try {
    const stdout = execSync(cmd, { stdio: "pipe", timeout, encoding: "utf-8" });
    const lines = stdout.split("\n").filter(Boolean);
    return {
      ok: true,
      manager,
      details: `${lines.length} lines output`,
      upgraded: lines.filter((l) => /upgraded|updated|installed/i.test(l))
        .length,
      failed: lines.filter((l) => /failed|error/i.test(l)).length,
    };
  } catch (err: any) {
    return {
      ok: false,
      manager,
      details: err.message || String(err),
      upgraded: 0,
      failed: 1,
    };
  }
}

function isToolAvailable(tool: string): boolean {
  try {
    execSync(`where ${tool} 2>nul || which ${tool} 2>/dev/null`, {
      stdio: "pipe",
      timeout: 5000,
    });
    return true;
  } catch {
    return false;
  }
}

function ensureDir(dir: string) {
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
}

// ─── Main ────────────────────────────────────────────────────────────

const USAGE = `Package Manager Upgrade v3.1 — TypeScript

Usage:
  upgrade.ts               Run normal upgrade (winget + choco)
  upgrade.ts --debug       Verbose debug output
  upgrade.ts --skip-winget Skip winget, only run chocolatey
  upgrade.ts --skip-choco  Skip chocolatey, only run winget
  upgrade.ts --help        Show this help

Environment:
  LOG_DIR     - Directory for log files (default: ./logs)
  DEBUG_MODE  - Set to "1" to enable debug output
  SKIP_WINGET - Set to "1" to skip winget
  SKIP_CHOCO  - Set to "1" to skip choco`;

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.flags.has("help")) showHelp(USAGE);

  const debug = args.flags.has("debug") || process.env["DEBUG_MODE"] === "1";
  const skipWinget =
    args.flags.has("skip-winget") || process.env["SKIP_WINGET"] === "1";
  const skipChoco =
    args.flags.has("skip-choco") || process.env["SKIP_CHOCO"] === "1";

  const logDir = process.env["LOG_DIR"] || join(process.cwd(), "logs");
  ensureDir(logDir);

  const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
  const logFile = join(logDir, `upgrade-${timestamp}.log`);
  const logger = new FileLogger(logFile);

  if (debug) (logger as any).setLogLevel("debug");

  console.log(bold("\nPackage Manager Upgrade"));
  console.log(dim(`Log: ${logFile}\n`));

  const managers: {
    name: string;
    cmd: string;
    timeout: number;
    skip: boolean;
  }[] = [
    {
      name: "WinGet",
      cmd: "winget upgrade --all",
      timeout: 300000,
      skip: skipWinget,
    },
    {
      name: "Chocolatey",
      cmd: "choco upgrade all -y",
      timeout: 300000,
      skip: skipChoco,
    },
  ];

  let totalUpgraded = 0;
  let totalFailed = 0;

  for (const mgr of managers) {
    if (mgr.skip) {
      console.log(dim(`  ${mgr.name.padEnd(15)} skipped`));
      continue;
    }

    if (!isToolAvailable(mgr.name === "WinGet" ? "winget" : "choco")) {
      console.log(warn(`  ${mgr.name.padEnd(15)} not installed`));
      continue;
    }

    process.stdout.write(`  ${mgr.name.padEnd(15)} `);
    const result = runUpgrade(mgr.name, mgr.cmd, mgr.timeout);

    if (result.ok) {
      console.log(ok(`${result.upgraded} upgraded, ${result.failed} failed`));
    } else {
      console.log(fail(result.details));
    }

    totalUpgraded += result.upgraded;
    totalFailed += result.failed;
    logger.append(
      result.ok ? "info" : "error",
      `${mgr.name}: ${result.upgraded} upgraded, ${result.failed} failed`,
    );
  }

  await logger.flush();

  console.log(
    bold(
      `\nResult: ${ok(`${totalUpgraded} upgraded`)}, ${totalFailed > 0 ? fail(`${totalFailed} failed`) : dim("0 failed")}`,
    ),
  );

  if (totalFailed > 0) {
    console.log(warn(`See ${logFile} for details`));
    process.exit(1);
  }
}

await safeExec(main);
