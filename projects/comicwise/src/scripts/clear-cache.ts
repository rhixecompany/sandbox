#!/usr/bin/env tsx
/**
 * Clear Cache Script
 * Clears Redis cache with options for dry-run and detailed reporting
 */

import chalk from "chalk";
import { Command } from "commander";
import IORedis from "ioredis";

import appConfig from "appConfig";

import { confirmAction } from "./shared/confirmAction";

/**
 * Parse CLI arguments
 */
const program = new Command()
  .name("clear-cache")
  .description("Clear Redis cache with pattern matching")
  .argument("[pattern]", "Key pattern to clear (default: all)", "*")
  .option("--dry-run", "Preview what would be deleted without actually deleting", false)
  .option("--verbose", "Show detailed output", false)
  .option("--json", "Output results in JSON format", false)
  .option("--yes", "Skip confirmation prompt and proceed", false)
  .parse(process.argv);

const pattern = program.args[0] || "*";
const opts = program.opts();
const { dryRun = false, verbose = false, json = false, yes = false } = opts;

async function clearCache() {
  try {
    if (!json) {
      console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
      console.log(chalk.cyan("  🧹 Clear Cache") + chalk.gray(dryRun ? " (DRY RUN)" : ""));
      console.log(chalk.cyan("═══════════════════════════════════════════════════════════\n"));
    }

    const isAll = pattern === "*" || pattern === "all";

    const redis = new IORedis({
      host: appConfig.redis.host || "localhost",
      port: Number(appConfig.redis.port) || 6379,
      password: appConfig.redis.password || undefined,
    });

    if (isAll) {
      const keys = await redis.keys("*");
      if (!json) {
        console.log(chalk.yellow(`Found ${keys.length} total keys in cache`));
      }

      if (!dryRun && keys.length > 0) {
        // Request confirmation before deleting all cache
        const confirmed = await confirmAction({
          title: "Clear All Cache",
          message: "This will delete ALL cache entries. This action cannot be undone.",
          affectedCount: keys.length,
          affectedType: "cache entries",
          yesFlag: yes,
          cautionLevel: "high",
        });

        if (!confirmed) {
          if (!json) {
            console.log(chalk.yellow("Operation cancelled by user.\n"));
          } else {
            console.log(JSON.stringify({ success: false, reason: "cancelled" }, null, 2));
          }
          await redis.quit();
          process.exit(0);
        }

        await redis.flushdb();
        if (!json) {
          console.log(chalk.green(`✅ Cleared ${keys.length} cache entries\n`));
        }
      } else if (dryRun) {
        if (!json) {
          console.log(chalk.cyan(`[DRY-RUN] Would delete ${keys.length} entries\n`));
        }
      } else if (!json) {
        console.log(chalk.gray("ℹ️  Cache is empty\n"));
      }

      if (json) {
        console.log(
          JSON.stringify(
            {
              success: true,
              dryRun,
              pattern,
              keysFound: keys.length,
              keysDeleted: dryRun ? 0 : keys.length,
            },
            null,
            2
          )
        );
      }
    } else {
      if (!json && verbose) {
        console.log(chalk.blue(`🔍 Clearing pattern: ${chalk.bold(pattern)}\n`));
      }

      const keys = await redis.keys(pattern);

      if (keys.length === 0) {
        if (!json) {
          console.log(chalk.yellow("⚠️  No keys found matching pattern\n"));
        } else {
          console.log(JSON.stringify({ success: true, dryRun, pattern, keysFound: 0, keysDeleted: 0 }, null, 2));
        }
      } else {
        if (!json) {
          console.log(chalk.blue(`📦 Found ${keys.length} matching keys`));
          if (verbose) {
            console.log(chalk.gray("Keys:"));
            for (const k of keys.slice(0, 10)) {
              console.log(chalk.gray(`  - ${k}`));
            }
            if (keys.length > 10) {
              console.log(chalk.gray(`  ... and ${keys.length - 10} more`));
            }
          }
        }

        if (!dryRun) {
          // Request confirmation before deleting
          const confirmed = await confirmAction({
            title: "Delete Cache Keys",
            message: `This will delete ${keys.length} cache key(s) matching pattern: ${pattern}`,
            affectedCount: keys.length,
            affectedType: "keys",
            yesFlag: yes,
            cautionLevel: "medium",
            details: keys.length <= 10 ? keys : keys.slice(0, 5),
          });

          if (!confirmed) {
            if (!json) {
              console.log(chalk.yellow("Operation cancelled by user.\n"));
            } else {
              console.log(JSON.stringify({ success: false, reason: "cancelled" }, null, 2));
            }
            await redis.quit();
            process.exit(0);
          }

          await redis.del(...keys);
          if (!json) {
            console.log(chalk.green(`✅ Deleted ${keys.length} keys\n`));
          }
        } else if (!json) {
          console.log(chalk.cyan(`[DRY-RUN] Would delete ${keys.length} keys\n`));
        }

        if (json) {
          console.log(
            JSON.stringify(
              {
                success: true,
                dryRun,
                pattern,
                keysFound: keys.length,
                keysDeleted: dryRun ? 0 : keys.length,
                sampleKeys: keys.slice(0, 10),
              },
              null,
              2
            )
          );
        }
      }
    }

    if (!json && !dryRun) {
      console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
    } else if (!json && dryRun) {
      console.log(chalk.yellow("⚠️  This was a dry run. Run without --dry-run to apply changes."));
      console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
    }

    await redis.quit();
    process.exit(0);
  } catch (error) {
    const errorMsg = error instanceof Error ? error.message : String(error);
    if (json) {
      console.log(JSON.stringify({ success: false, error: errorMsg }, null, 2));
    } else {
      console.error(chalk.red("❌ Error:"), errorMsg);
    }
    process.exit(1);
  }
}

clearCache();
