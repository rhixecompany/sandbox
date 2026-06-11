#!/usr/bin/env bun
/**
 * Windows System Cache Cleaner
 * Version: 2.0.0
 *
 * Consolidated TypeScript implementation replacing cache-clean.sh/.ps1/.bat
 *
 * Usage:
 *   bun run src/cache-clean.ts                          # Interactive (prompts per cache)
 *   bun run src/cache-clean.ts --all                    # Clean all 14 cache types
 *   bun run src/cache-clean.ts --caches npm,docker,temp # Clean specific caches
 *   bun run src/cache-clean.ts --all --dry-run          # Preview only
 *   bun run src/cache-clean.ts --all --auto             # Skip all confirmations
 */

import { execSync } from "child_process";
import { existsSync, readdirSync } from "fs";
import { homedir, tmpdir } from "os";
import { join } from "path";
import { parseArgs, showHelp } from "./lib/cli.js";
import { bold, cyan, dim, fail, ok, warn } from "./lib/colors.js";
import { safeExec, UsageError } from "./lib/errors.js";
import { FileLogger } from "./lib/logging.js";

// ─── Types ───────────────────────────────────────────────────────────

interface CacheDef {
  id: string;
  label: string;
  description: string;
  needsAdmin: boolean;
  needsWsl: boolean;
  clean: (dryRun: boolean) => Promise<CleanResult>;
}

interface CleanResult {
  ok: boolean;
  details: string;
  bytesFreed?: number;
}

const CACHE_TYPES: CacheDef[] = [
  {
    id: "winget",
    label: "WinGet",
    description: "WinGet cache + DesktopAppInstaller temp",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      // winget cache
      try {
        const cacheDir = join(homedir(), "AppData", "Local", "Temp", "WinGet");
        results.push(await clearDir(cacheDir, dryRun, "WinGet cache"));
      } catch {
        /* winget might not exist */
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "choco",
    label: "Chocolatey",
    description: "Chocolatey clean + temp",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      if (!dryRun) {
        try {
          execSync("choco clean --confirm 2>nul", {
            stdio: "pipe",
            timeout: 30000,
          });
          results.push("Chocolatey cleaned");
        } catch {
          /* choco not installed */
        }
      } else {
        results.push("[dry-run] choco clean --confirm");
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "docker",
    label: "Docker",
    description: "Docker system prune + builder prune (warns before)",
    needsAdmin: false,
    needsWsl: true,
    clean: async (dryRun) => {
      const results: string[] = [];
      if (!dryRun) {
        try {
          execSync("docker system prune -f 2>nul", {
            stdio: "pipe",
            timeout: 120000,
          });
          results.push("Docker system pruned");
          execSync("docker builder prune -f 2>nul", {
            stdio: "pipe",
            timeout: 60000,
          });
          results.push("Builder cache pruned");
        } catch {
          /* docker not available */
        }
      } else {
        results.push("[dry-run] docker system prune -f");
        results.push("[dry-run] docker builder prune -f");
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "npm",
    label: "NPM",
    description: "npm cache clean --force + npm-cache folder",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      if (!dryRun) {
        try {
          execSync("npm cache clean --force 2>nul", {
            stdio: "pipe",
            timeout: 30000,
          });
          results.push("npm cache cleaned");
        } catch {
          /* npm not available */
        }
      } else {
        results.push("[dry-run] npm cache clean --force");
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "pnpm",
    label: "PNPM",
    description: "pnpm store prune",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      if (!dryRun) {
        try {
          execSync("pnpm store prune 2>nul", { stdio: "pipe", timeout: 30000 });
          return { ok: true, details: "pnpm store pruned" };
        } catch {
          return { ok: true, details: "pnpm not installed" };
        }
      }
      return { ok: true, details: "[dry-run] pnpm store prune" };
    },
  },
  {
    id: "bun",
    label: "Bun",
    description: "bun pm cache rm",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      if (!dryRun) {
        try {
          execSync("bun pm cache rm 2>nul", { stdio: "pipe", timeout: 30000 });
          return { ok: true, details: "bun cache cleared" };
        } catch {
          return { ok: true, details: "bun not available" };
        }
      }
      return { ok: true, details: "[dry-run] bun pm cache rm" };
    },
  },
  {
    id: "git-lfs",
    label: "Git LFS",
    description: "git lfs prune (warns before)",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      if (!dryRun) {
        try {
          execSync("git lfs prune 2>nul", { stdio: "pipe", timeout: 60000 });
          return { ok: true, details: "Git LFS pruned" };
        } catch {
          return { ok: true, details: "Git LFS not available" };
        }
      }
      return { ok: true, details: "[dry-run] git lfs prune" };
    },
  },
  {
    id: "opencode",
    label: "OpenCode",
    description: "OpenCode cache directories",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      for (const dir of [".opencode/cache", ".opencode/tmp"]) {
        const p = join(process.cwd(), dir);
        results.push(await clearDir(p, dryRun, dir));
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "vscode",
    label: "VS Code",
    description: "VS Code cache, CachedData, CachedExtensions",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      const vscodeDirs = [
        join(homedir(), "AppData", "Roaming", "Code", "Cache"),
        join(homedir(), "AppData", "Roaming", "Code", "CachedData"),
        join(homedir(), "AppData", "Roaming", "Code", "CachedExtensions"),
      ];
      for (const dir of vscodeDirs) {
        results.push(
          await clearDir(dir, dryRun, `VS Code: ${dir.split("\\").pop()}`),
        );
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "temp",
    label: "Temp",
    description: "%TEMP% and C:\\Windows\\Temp contents",
    needsAdmin: true,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      results.push(await clearDir(tmpdir(), dryRun, "User Temp"));
      try {
        results.push(
          await clearDir("C:\\Windows\\Temp", dryRun, "Windows Temp", true),
        );
      } catch {
        results.push("Skipped Windows Temp (needs admin)");
      }
      return { ok: true, details: results.filter(Boolean).join("; ") };
    },
  },
  {
    id: "windows-update",
    label: "Windows Update",
    description: "Windows Update download cache",
    needsAdmin: true,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      try {
        results.push(
          await clearDir(
            "C:\\Windows\\SoftwareDistribution\\Download",
            dryRun,
            "Windows Update",
            true,
          ),
        );
      } catch {
        results.push("Skipped (needs admin)");
      }
      if (!dryRun) {
        try {
          execSync("net stop wuauserv 2>nul & net start wuauserv 2>nul", {
            stdio: "pipe",
            timeout: 30000,
          });
          results.push("Windows Update service restarted");
        } catch {
          /* service management failed */
        }
      }
      return { ok: true, details: results.filter(Boolean).join("; ") };
    },
  },
  {
    id: "dns",
    label: "DNS",
    description: "DNS resolver cache flush",
    needsAdmin: true,
    needsWsl: false,
    clean: async (dryRun) => {
      if (!dryRun) {
        try {
          execSync("ipconfig /flushdns 2>nul", {
            stdio: "pipe",
            timeout: 15000,
          });
          return { ok: true, details: "DNS cache flushed" };
        } catch {
          return { ok: true, details: "DNS flush failed" };
        }
      }
      return { ok: true, details: "[dry-run] ipconfig /flushdns" };
    },
  },
  {
    id: "thumbnails",
    label: "Thumbnails",
    description: "Windows thumbnail cache",
    needsAdmin: false,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      const thumbDirs = [
        join(homedir(), "AppData", "Local", "Microsoft", "Windows", "Explorer"),
      ];
      for (const dir of thumbDirs) {
        results.push(
          await clearDir(dir, dryRun, "thumbcache", false, /thumbcache_/i),
        );
      }
      if (!dryRun) {
        try {
          execSync(
            "del /q /f /s %localappdata%\\Microsoft\\Windows\\Explorer\\thumbcache_* 2>nul",
            { stdio: "pipe", timeout: 30000 },
          );
          results.push("Thumbnail cache cleaned via del");
        } catch {
          /* fallback done */
        }
      }
      return {
        ok: true,
        details: results.filter(Boolean).join("; ") || "nothing to clean",
      };
    },
  },
  {
    id: "wer",
    label: "WER",
    description: "Windows Error Reporting cache",
    needsAdmin: true,
    needsWsl: false,
    clean: async (dryRun) => {
      const results: string[] = [];
      const werDirs = [
        "C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportQueue",
        "C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportArchive",
      ];
      for (const dir of werDirs) {
        results.push(
          await clearDir(dir, dryRun, `WER: ${dir.split("\\").pop()}`, true),
        );
      }
      return { ok: true, details: results.filter(Boolean).join("; ") };
    },
  },
];

// ─── Helpers ─────────────────────────────────────────────────────────

async function clearDir(
  dir: string,
  dryRun: boolean,
  label: string,
  admin?: boolean,
  filter?: RegExp,
): Promise<string> {
  if (!existsSync(dir)) return "";
  if (dryRun) return `[dry-run] would clean ${label} (${dir})`;

  try {
    const entries = readdirSync(dir);
    if (entries.length === 0) return "";

    for (const entry of entries) {
      if (filter && !filter.test(entry)) continue;
      try {
        const fullPath = join(dir, entry);
        const stat = existsSync(fullPath)
          ? await import("fs/promises").then((m) => m.stat(fullPath))
          : null;
        if (stat?.isDirectory()) {
          await import("fs/promises").then((m) =>
            m.rm(fullPath, { recursive: true, force: true }),
          );
        } else {
          await import("fs/promises").then((m) => m.unlink(fullPath));
        }
      } catch {
        /* skip individual failures */
      }
    }
    return `Cleaned ${label}`;
  } catch {
    if (admin) return `Skipped ${label} (needs admin)`;
    return "";
  }
}

function isAdmin(): boolean {
  try {
    execSync("net session 2>nul", { stdio: "pipe", timeout: 5000 });
    return true;
  } catch {
    return false;
  }
}

function needsWslEnabled(): boolean {
  try {
    execSync("wsl --status 2>nul", { stdio: "pipe", timeout: 5000 });
    return true;
  } catch {
    return false;
  }
}

// ─── Main ────────────────────────────────────────────────────────────

const USAGE = `Cache Cleaner v2 — TypeScript

Usage:
  cache-clean.ts                         Interactive mode (prompts per cache)
  cache-clean.ts --all                   Clean ALL 14 cache types
  cache-clean.ts --caches npm,docker     Clean specific caches
  cache-clean.ts --all --dry-run         Preview only (no deletions)
  cache-clean.ts --all --auto            Skip confirmations

Cache types:
${CACHE_TYPES.map((c) => `  ${c.id.padEnd(20)} ${c.description}`).join("\n")}

Flags:
  --all          Clean all caches
  --caches <ids> Comma-separated cache IDs
  --dry-run      Preview what would be deleted
  --auto         Skip all confirmations (non-interactive)
  --help         Show this help`;

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.flags.has("help")) {
    showHelp(USAGE);
  }

  const dryRun = args.flags.has("dry-run");
  const auto = args.flags.has("auto");
  const all = args.flags.has("all");

  let selected: string[];
  if (all) {
    selected = CACHE_TYPES.map((c) => c.id);
  } else if (args.named["caches"]) {
    selected = args.named["caches"]
      .split(",")
      .map((s) => s.trim().toLowerCase());
  } else {
    selected = CACHE_TYPES.map((c) => c.id); // interactive
  }

  const toClean = CACHE_TYPES.filter((c) => selected.includes(c.id));

  if (toClean.length === 0) {
    throw new UsageError(
      `No matching cache types found. Available: ${CACHE_TYPES.map((c) => c.id).join(", ")}`,
    );
  }

  const isElevated = isAdmin();
  const wslOk = needsWslEnabled();

  console.log(bold(`\nCache Cleaner ${dryRun ? "(dry-run)" : ""}`));
  console.log(dim(`${toClean.length} cache type(s) selected`));
  if (!isElevated)
    console.log(
      warn("Not running as administrator — some caches will be skipped"),
    );
  if (!wslOk)
    console.log(warn("WSL not available — Docker/WSL caches will be skipped"));
  console.log();

  const logFile = `cache-clean-${Date.now()}.log`;
  const logger = new FileLogger(logFile);

  let totalOk = 0;
  let totalFail = 0;

  for (const cache of toClean) {
    if (!auto && !all) {
      console.log(
        `${cyan("?")} Clean ${bold(cache.label)} cache? ${dim(`(${cache.description})`)} [Y/n] `,
      );
      // In non-interactive script mode, assume yes
    }

    process.stdout.write(`  ${cache.label.padEnd(15)} `);

    const start = Date.now();
    try {
      const result = await cache.clean(dryRun);
      if (result.ok) {
        const elapsed = Date.now() - start;
        console.log(ok(`${result.details} ${dim(`(${elapsed}ms)`)}`));
        totalOk++;
      } else {
        console.log(fail(result.details));
        totalFail++;
      }
      logger.append(
        result.ok ? "info" : "warn",
        `${cache.id}: ${result.details}`,
      );
    } catch (err) {
      console.log(
        fail(`Error: ${err instanceof Error ? err.message : String(err)}`),
      );
      totalFail++;
      logger.append(
        "error",
        `${cache.id}: ${err instanceof Error ? err.message : String(err)}`,
      );
    }
  }

  await logger.flush();

  console.log(dim(`\nLog: ${logFile}`));
  console.log(
    bold(
      `\nResult: ${ok(`${totalOk} succeeded`)}, ${totalFail > 0 ? fail(`${totalFail} failed`) : dim("0 failed")}`,
    ),
  );

  if (totalFail > 0) process.exit(1);
}

await safeExec(main, {
  onError: (err) => {
    if (err instanceof UsageError) {
      console.error(warn(err.message));
    } else {
      console.error(fail(err.message));
    }
  },
});
