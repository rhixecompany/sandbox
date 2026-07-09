#!/usr/bin/env bun
/**
 * Git Commit Batches — TypeScript implementation
 *
 * Reads batch definitions from Bash/src/lib/data/batches.json and
 * commits them sequentially. Replaces git-commit-batches.sh/.ps1.
 *
 * Usage:
 *   bun run src/git-commit-batches.ts              # All batches
 *   bun run src/git-commit-batches.ts --batch 1-5  # Batches 1-5
 *   bun run src/git-commit-batches.ts --list        # List batches only
 *   bun run src/git-commit-batches.ts --dry-run     # Preview only
 */

import { execSync } from "child_process";
import { existsSync, readFileSync } from "fs";
import { join } from "path";
import { cwd } from "process";
import { parseArgs, showHelp } from "./lib/cli.js";
import { bold, dim, fail, ok, warn } from "./lib/colors.js";
import { safeExec } from "./lib/errors.js";

interface BatchDef {
  id: number;
  message: string;
  files: string[];
}

const USAGE = `Git Commit Batches

Usage:
  git-commit-batches.ts                All batches
  git-commit-batches.ts --batch 1-5    Batches 1-5
  git-commit-batches.ts --list         List batches only
  git-commit-batches.ts --dry-run      Preview only
  git-commit-batches.ts --help         Show this help`;

function loadBatches(): BatchDef[] {
  const paths = [
    join(cwd(), "Bash", "scripts", "BATCHES.json"),
    join(cwd(), "scripts", "BATCHES.json"),
  ];

  for (const p of paths) {
    if (existsSync(p)) {
      const data = JSON.parse(readFileSync(p, "utf-8"));
      if (Array.isArray(data)) return data as BatchDef[];
      // Try common wrapper shapes
      if (data.batches) return data.batches;
      if (data.tasks) return data.tasks;
    }
  }

  // Fallback: auto-generate from .sh files in archive
  const archiveDir = join(cwd(), "Bash", "archive", "skills-commit-batches");
  if (existsSync(archiveDir)) {
    const { readdirSync } = require("fs");
    const files = readdirSync(archiveDir).filter((f: string) =>
      f.endsWith(".sh"),
    );
    return files.map((f: string) => {
      const match = f.match(/batch-(\d+)/);
      return {
        id: match ? parseInt(match[1]!, 10) : 0,
        message: `skills(batch ${match?.[1] || "?"})`,
        files: [f],
      };
    });
  }

  return [];
}

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.flags.has("help")) showHelp(USAGE);

  const dryRun = args.flags.has("dry-run");

  let batches = loadBatches();

  if (batches.length === 0) {
    console.log(
      warn(
        "No batch definitions found. Ensure BATCHES.json exists or archive has batch files.",
      ),
    );
    return;
  }

  // Filter by batch range
  if (args.named["batch"]) {
    const range = args.named["batch"];
    const [start, end] = range.split("-").map(Number);
    batches = batches.filter(
      (b) => b.id >= (start || 0) && b.id <= (end || start || 999),
    );
  }

  // List mode
  if (args.flags.has("list")) {
    console.log(bold(`\nAvailable Batches (${batches.length})`));
    console.log(dim("─".repeat(50)));
    for (const batch of batches) {
      console.log(
        `  Batch ${String(batch.id).padStart(2)}: ${batch.message} (${batch.files.length} file(s))`,
      );
    }
    return;
  }

  console.log(bold(`\nGit Commit Batches ${dryRun ? "(dry-run)" : ""}`));
  console.log(dim(`${batches.length} batch(es) to process\n`));

  let committed = 0;
  let skipped = 0;

  for (const batch of batches) {
    const fileList = batch.files.join(" ");

    if (dryRun) {
      console.log(
        `  Batch ${String(batch.id).padStart(2)}: ${dim(batch.message)}`,
      );
      for (const f of batch.files) {
        console.log(`    ${dim(f)}`);
      }
      skipped++;
      continue;
    }

    try {
      execSync(`git add ${fileList}`, { stdio: "pipe", timeout: 30000 });
      execSync(`git commit -m "${batch.message}"`, {
        stdio: "pipe",
        timeout: 30000,
      });
      console.log(
        ok(`Batch ${String(batch.id).padStart(2)}: ${batch.message}`),
      );
      committed++;
    } catch (err: any) {
      if (err.message?.includes("nothing to commit") || err.status === 1) {
        console.log(
          dim(`  Batch ${String(batch.id).padStart(2)}: nothing to commit`),
        );
        skipped++;
      } else {
        console.log(
          fail(
            `Batch ${String(batch.id).padStart(2)}: ${err.message || String(err)}`,
          ),
        );
        skipped++;
      }
    }
  }

  console.log(
    bold(
      `\nResult: ${ok(`${committed} committed`)}, ${dim(`${skipped} skipped`)}`,
    ),
  );
}

await safeExec(main);
