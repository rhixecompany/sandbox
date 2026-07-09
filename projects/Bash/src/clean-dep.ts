#!/usr/bin/env bun
/**
 * Dependency Folder Cleanup Script
 * Version: 3.1.0
 *
 * Consolidated TypeScript implementation replacing
 * clean_dependency_folders.sh / clean-dependency-folders.ps1/.bat
 *
 * Usage:
 *   bun run src/clean-dep.ts                       # Interactive
 *   bun run src/clean-dep.ts --auto                # Skip confirmations
 *   bun run src/clean-dep.ts --dry-run             # Preview only
 *   bun run src/clean-dep.ts --paths /c/projects   # Custom paths
 *   bun run src/clean-dep.ts --targets node        # Specific targets
 *   bun run src/clean-dep.ts --max-depth 5         # Max recursion
 */

import { existsSync, readdirSync, rmSync, statSync } from "fs";
import { homedir } from "os";
import { join, resolve } from "path";
import { cwd } from "process";
import { parseArgs, showHelp } from "./lib/cli.js";
import { bold, dim, fail, ok, warn } from "./lib/colors.js";
import { safeExec, UsageError } from "./lib/errors.js";

// ─── Target Definitions ──────────────────────────────────────────────

interface TargetDef {
  id: string;
  label: string;
  folders: string[];
  description: string;
}

const TARGETS: TargetDef[] = [
  {
    id: "node",
    label: "Node.js",
    folders: ["node_modules", ".npm", ".pnpm-store", ".yarn"],
    description: "node_modules, npm cache, pnpm store, yarn",
  },
  {
    id: "python",
    label: "Python",
    folders: [
      "venv",
      "__pycache__",
      ".venv",
      ".pytest_cache",
      ".mypy_cache",
      ".ruff_cache",
    ],
    description: "venv, __pycache__, .venv, caches",
  },
  {
    id: "dotnet",
    label: ".NET",
    folders: ["bin", "obj", "Packages"],
    description: "bin, obj, Packages",
  },
  {
    id: "java",
    label: "Java",
    folders: [".gradle", "build", "target"],
    description: ".gradle, build, target",
  },
  { id: "go", label: "Go", folders: ["vendor"], description: "vendor" },
  {
    id: "build",
    label: "Build",
    folders: ["dist", "build", "out", ".next", ".nuxt"],
    description: "dist, build, out, .next, .nuxt",
  },
  {
    id: "cache",
    label: "Caches",
    folders: [".cache", ".turbo", ".vite", ".esbuild", ".swc"],
    description: ".cache, .turbo, .vite, .esbuild, .swc",
  },
  {
    id: "ide",
    label: "IDE",
    folders: [".idea", ".vscode"],
    description: ".idea, .vscode",
  },
];

// ─── Scanner ─────────────────────────────────────────────────────────

interface ScanResult {
  path: string;
  sizeBytes: number;
  folderType: string;
}

function humanSize(bytes: number): string {
  if (bytes === 0) return "0 B";
  const units = ["B", "KB", "MB", "GB"];
  const i = Math.min(
    Math.floor(Math.log(bytes) / Math.log(1024)),
    units.length - 1,
  );
  return `${(bytes / 1024 ** i).toFixed(1)} ${units[i]}`;
}

function scanDir(
  rootPath: string,
  targetFolders: Set<string>,
  maxDepth: number,
  currentDepth = 0,
): ScanResult[] {
  const results: ScanResult[] = [];

  if (currentDepth > maxDepth) return results;
  if (!existsSync(rootPath)) return results;

  let entries: string[];
  try {
    entries = readdirSync(rootPath);
  } catch {
    return results;
  }

  for (const entry of entries) {
    if (entry.startsWith(".") && entry === ".") continue;
    const fullPath = join(rootPath, entry);

    try {
      const stat = statSync(fullPath);
      if (!stat.isDirectory()) continue;

      if (targetFolders.has(entry)) {
        results.push({
          path: fullPath,
          sizeBytes: getDirSize(fullPath),
          folderType: entry,
        });
      } else if (currentDepth < maxDepth) {
        results.push(
          ...scanDir(fullPath, targetFolders, maxDepth, currentDepth + 1),
        );
      }
    } catch {
      continue;
    }
  }

  return results;
}

function getDirSize(dirPath: string): number {
  let size = 0;
  try {
    const entries = readdirSync(dirPath);
    for (const entry of entries) {
      const fullPath = join(dirPath, entry);
      try {
        const stat = statSync(fullPath);
        if (stat.isDirectory()) {
          size += getDirSize(fullPath);
        } else {
          size += stat.size;
        }
      } catch {
        /* skip */
      }
    }
  } catch {
    /* skip */
  }
  return size;
}

// ─── Main ────────────────────────────────────────────────────────────

const USAGE = `Dependency Folder Cleanup v3.1 — TypeScript

Usage:
  clean-dep.ts                    Interactive mode
  clean-dep.ts --auto             Skip confirmations
  clean-dep.ts --dry-run          Preview only
  clean-dep.ts --paths /c/proj    Custom scan paths (comma-separated)
  clean-dep.ts --targets node,python  Specific target types
  clean-dep.ts --max-depth 5      Max recursion depth (default: 4)
  clean-dep.ts --help             Show this help

Targets:
${TARGETS.map((t) => `  ${t.id.padEnd(10)} ${t.description}`).join("\n")}

Default scan paths: current directory, %USERPROFILE%\\source, %USERPROFILE%\\projects`;

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.flags.has("help")) showHelp(USAGE);

  const dryRun = args.flags.has("dry-run");
  const auto = args.flags.has("auto");
  const maxDepth = parseInt(args.named["max-depth"] || "4", 10);

  // Determine scan paths
  let scanPaths: string[];
  if (args.named["paths"]) {
    scanPaths = args.named["paths"].split(",").map((s) => resolve(s.trim()));
  } else {
    scanPaths = [
      cwd(),
      join(homedir(), "source"),
      join(homedir(), "projects"),
    ].filter((p) => existsSync(p));
  }

  // Determine target folders
  let activeTargets: TargetDef[];
  if (args.named["targets"]) {
    const targetIds = args.named["targets"]
      .split(",")
      .map((s) => s.trim().toLowerCase());
    activeTargets = TARGETS.filter((t) => targetIds.includes(t.id));
    if (activeTargets.length === 0) {
      throw new UsageError(
        `No matching targets. Available: ${TARGETS.map((t) => t.id).join(", ")}`,
      );
    }
  } else {
    activeTargets = TARGETS;
  }

  const targetFolderSet = new Set(activeTargets.flatMap((t) => t.folders));

  console.log(bold(`\nDependency Folder Cleanup ${dryRun ? "(dry-run)" : ""}`));
  console.log(
    dim(`Scanning ${scanPaths.length} path(s) up to depth ${maxDepth}`),
  );
  console.log(
    dim(`Looking for: ${activeTargets.map((t) => t.label).join(", ")}\n`),
  );

  // Scan
  const allResults: ScanResult[] = [];
  for (const scanPath of scanPaths) {
    console.log(`  Scanning ${dim(scanPath)}...`);
    const results = scanDir(scanPath, targetFolderSet, maxDepth);
    allResults.push(...results);
  }

  // Report
  if (allResults.length === 0) {
    console.log(ok("No dependency folders found."));
    return;
  }

  const totalSize = allResults.reduce((acc, r) => acc + r.sizeBytes, 0);
  console.log(
    `\n  Found ${bold(String(allResults.length))} folder(s), ${bold(humanSize(totalSize))}`,
  );
  console.log();

  // Group by type
  const byType = new Map<string, { count: number; size: number }>();
  for (const r of allResults) {
    const existing = byType.get(r.folderType) || { count: 0, size: 0 };
    existing.count++;
    existing.size += r.sizeBytes;
    byType.set(r.folderType, existing);
  }

  for (const [type, info] of byType) {
    console.log(
      `  ${dim(type.padEnd(20))} ${info.count.toString().padStart(4)} folders, ${humanSize(info.size)}`,
    );
  }

  // Delete
  if (!dryRun) {
    const shouldProceed = auto;
    if (!shouldProceed) {
      console.log(warn("Skipped (interactive)"));
      return;
    }

    let deleted = 0;
    let failed = 0;
    for (const r of allResults) {
      try {
        rmSync(r.path, { recursive: true, force: true });
        deleted++;
      } catch {
        failed++;
      }
    }
    console.log(
      `\n${ok(`${deleted} deleted`)}, ${failed > 0 ? fail(`${failed} failed`) : dim("0 failed")}`,
    );
  } else {
    console.log(dim("\n  (dry-run — no changes made)"));
  }
}

await safeExec(main);
