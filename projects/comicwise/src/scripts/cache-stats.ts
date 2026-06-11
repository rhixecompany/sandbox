#!/usr/bin/env tsx
/**
 * Cache Statistics Script
 * Provides detailed Redis cache statistics including key counts, memory usage, and patterns
 */

import chalk from "chalk";
import { Command } from "commander";
import IORedis from "ioredis";

import appConfig from "appConfig";

import { createLogger } from "./shared/logger.js";
import { createSpinner } from "./shared/spinner.js";

/**
 * Parse CLI arguments
 */
const program = new Command()
  .name("cache-stats")
  .description("Display Redis cache statistics")
  .option("--json", "Output results in JSON format")
  .option("--verbose", "Show detailed output")
  .option("--pattern <pattern>", "Filter keys by pattern", "*")
  .parse(process.argv);

interface CacheStatsOptions {
  json?: boolean;
  pattern?: string;
  verbose?: boolean;
}

const rawOpts = program.opts();
const json = rawOpts.json ?? false;
const verbose = rawOpts.verbose ?? false;
const pattern = rawOpts.pattern ?? "*";

interface CacheStats {
  connectedClients: number;
  keyPatterns: Record<string, number>;
  largestKeys: Array<{ key: string; size: number }>;
  memoryUsed: string;
  oldestKeys: Array<{ key: string; ttl: number }>;
  totalKeys: number;
}

async function getCacheStats(): Promise<CacheStats | null> {
  const spinner = createSpinner("Connecting to Redis...");
  spinner.start();

  try {
    const redis = new IORedis({
      host: appConfig.redis.host || "localhost",
      port: Number(appConfig.redis.port) || 6379,
      password: appConfig.redis.password || undefined,
      lazyConnect: true,
    });

    await redis.connect();
    spinner.succeed("Connected to Redis");

    const logger = createLogger("cache-stats", { verbose });
    logger.section("Cache Statistics");

    // Get all keys matching pattern
    const redisPattern: string = pattern === "*" ? "*" : (pattern ?? "*");
    const allKeys = await redis.keys(redisPattern);
    const totalKeys = allKeys.length;

    // Get memory info
    const info = await redis.info("memory");
    const memoryMatch = info.match(/used_memory_human:(\S+)/);
    const memoryUsed = memoryMatch ? memoryMatch[1] : "unknown";

    // Get connected clients
    const clientInfo = await redis.info("clients");
    const clientsMatch = clientInfo.match(/connected_clients:(\d+)/);
    const connectedClients = clientsMatch ? parseInt(clientsMatch[1], 10) : 0;

    // Analyze key patterns
    const keyPatterns: Record<string, number> = {};
    for (const key of allKeys) {
      const prefix = key.split(":")[0] || "other";
      keyPatterns[prefix] = (keyPatterns[prefix] || 0) + 1;
    }

    // Get TTL info for sample keys
    const largestKeys: Array<{ key: string; size: number }> = [];
    const oldestKeys: Array<{ key: string; ttl: number }> = [];

    const sampleSize = Math.min(100, allKeys.length);
    const sampledKeys = allKeys.slice(0, sampleSize);

    for (const key of sampledKeys) {
      try {
        const ttl = await redis.ttl(key);
        const size = (await redis.memory("USAGE", key)) || 0;

        if (ttl > 0) {
          oldestKeys.push({ key, ttl });
        }
        if (size > 0) {
          largestKeys.push({ key, size });
        }
      } catch {
        // Skip keys that can't be queried
      }
    }

    // Sort and limit
    oldestKeys.sort((a, b) => b.ttl - a.ttl);
    largestKeys.sort((a, b) => b.size - a.size);

    await redis.quit();

    return {
      totalKeys,
      memoryUsed,
      connectedClients,
      keyPatterns,
      largestKeys: largestKeys.slice(0, 10),
      oldestKeys: oldestKeys.slice(0, 10),
    };
  } catch (error) {
    const err = error instanceof Error ? error.message : String(error);
    if (!json) {
      console.error(chalk.red("Error connecting to Redis:"), err);
    }
    return null;
  }
}

async function main() {
  if (!json) {
    console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
    console.log(chalk.cyan("  📊 Cache Statistics"));
    console.log(chalk.cyan("═══════════════════════════════════════════════════════════\n"));
  }

  const stats = await getCacheStats();

  if (!stats) {
    if (json) {
      console.log(JSON.stringify({ success: false, error: "Failed to connect to Redis" }, null, 2));
    }
    process.exit(1);
  }

  if (json) {
    console.log(
      JSON.stringify(
        {
          success: true,
          timestamp: new Date().toISOString(),
          ...stats,
        },
        null,
        2
      )
    );
  } else {
    // Summary section
    console.log(chalk.blue("  Summary"));
    console.log(chalk.gray("  ─────────────────────────────────────────────────────"));
    console.log(`  Total Keys:     ${chalk.yellow(stats.totalKeys.toLocaleString())}`);
    console.log(`  Memory Used:    ${chalk.yellow(stats.memoryUsed)}`);
    console.log(`  Connected:      ${chalk.yellow(stats.connectedClients)} clients`);
    console.log();

    // Key patterns
    console.log(chalk.blue("  Key Patterns"));
    console.log(chalk.gray("  ─────────────────────────────────────────────────────"));
    const sortedPatterns = Object.entries(stats.keyPatterns).sort((a, b) => b[1] - a[1]);
    for (const [prefix, count] of sortedPatterns.slice(0, 10)) {
      const percentage = ((count / stats.totalKeys) * 100).toFixed(1);
      console.log(`  ${prefix.padEnd(20)} ${count.toLocaleString().padStart(8)} keys (${percentage}%)`);
    }
    if (sortedPatterns.length > 10) {
      console.log(chalk.gray(`  ... and ${sortedPatterns.length - 10} more patterns`));
    }
    console.log();

    // Largest keys (if verbose)
    if (verbose && stats.largestKeys.length > 0) {
      console.log(chalk.blue("  Largest Keys (sample)"));
      console.log(chalk.gray("  ─────────────────────────────────────────────────────"));
      for (const { key, size } of stats.largestKeys.slice(0, 5)) {
        const sizeStr = size > 1024 * 1024 ? `${(size / 1024 / 1024).toFixed(2)} MB` : `${(size / 1024).toFixed(2)} KB`;
        console.log(`  ${key.substring(0, 40).padEnd(40)} ${chalk.red(sizeStr)}`);
      }
      console.log();
    }

    // Keys with longest TTL (if verbose)
    if (verbose && stats.oldestKeys.length > 0) {
      console.log(chalk.blue("  Keys with Longest TTL (sample)"));
      console.log(chalk.gray("  ─────────────────────────────────────────────────────"));
      for (const { key, ttl } of stats.oldestKeys.slice(0, 5)) {
        const ttlStr = ttl > 86400 ? `${(ttl / 86400).toFixed(1)} days` : `${(ttl / 3600).toFixed(1)} hours`;
        console.log(`  ${key.substring(0, 40).padEnd(40)} ${chalk.cyan(ttlStr)}`);
      }
      console.log();
    }

    console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
  }

  process.exit(0);
}

main();
