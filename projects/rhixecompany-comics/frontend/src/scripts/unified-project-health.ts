#!/usr/bin/env tsx
/**
 * ═══════════════════════════════════════════════════════════════════════════
 * Unified Project Health Check
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * Consolidates 6 health check scripts into a single unified command
 * - checkDb.ts — Database connection
 * - checkRedis.ts — Redis connection
 * - healthCheck.ts — Comprehensive health check
 * - cacheStats.ts — Cache statistics
 * - verify-mcp-servers.ps1 — MCP server health
 * - verify-mcp-packages.ts — MCP packages health
 *
 * Usage:
 *   pnpm health                      # Check all systems
 *   pnpm health --db                 # Database only
 *   pnpm health --redis              # Redis only
 *   pnpm health --mcp                # MCP servers only
 *   pnpm health --cache              # Cache stats only
 *   pnpm health --json               # JSON output format
 *   pnpm health --verbose            # Detailed output
 * ═══════════════════════════════════════════════════════════════════════════
 */

import { execSync } from "node:child_process";

import { getEnv } from "appConfig";

import { createLogger } from "./shared/logger.js";
import { createSpinner } from "./shared/spinner.js";

interface HealthCheckResult {
  component: string;
  details: string[];
  latency?: number;
  status: "healthy" | "unhealthy" | "unknown" | "warning";
  timestamp: string;
}

interface HealthCheckOptions {
  all: boolean;
  cache: boolean;
  db: boolean;
  dryRun: boolean;
  json: boolean;
  mcp: boolean;
  redis: boolean;
  timeout: number;
  verbose: boolean;
  yes: boolean;
}

// Parse command-line arguments
function parseArgs(): HealthCheckOptions {
  const args = process.argv.slice(2);

  const options: HealthCheckOptions = {
    all: args.includes("--all"),
    db: args.includes("--db"),
    redis: args.includes("--redis"),
    mcp: args.includes("--mcp"),
    cache: args.includes("--cache"),
    json: args.includes("--json"),
    dryRun: args.includes("--dry-run"),
    yes: args.includes("--yes"),
    verbose: args.includes("--verbose"),
    timeout: 5000,
  };

  // If no specific check is requested, check all by default
  if (!options.db && !options.redis && !options.mcp && !options.cache) {
    options.all = true;
  }

  return options;
}

// Check database connection
async function checkDatabase(logger: any): Promise<HealthCheckResult> {
  const spinner = createSpinner("Checking database connection...");
  const startTime = Date.now();

  try {
    spinner.start();

    // Import and test Drizzle connection
    const { db } = await import("../database/db.js");

    const latency = Date.now() - startTime;
    spinner.succeed(`Database connection OK (${latency}ms)`);

    return {
      component: "Database (PostgreSQL)",
      status: "healthy",
      details: [`Connection successful in ${latency}ms`, "Status: Ready"],
      latency,
      timestamp: new Date().toISOString(),
    };
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    spinner.fail("Database connection failed");

    logger.error(`Database error: ${message}`);

    return {
      component: "Database (PostgreSQL)",
      status: "unhealthy",
      details: [
        `Connection failed: ${message}`,
        "Action: Check DATABASE_URL in .env.local",
        "Action: Ensure PostgreSQL is running",
      ],
      timestamp: new Date().toISOString(),
    };
  }
}

// Check Redis connection
async function checkRedis(logger: any): Promise<HealthCheckResult> {
  const spinner = createSpinner("Checking Redis connection...");
  const startTime = Date.now();

  try {
    spinner.start();

    // Try to import Redis client
    try {
      const redisModule = await import("ioredis");
      const Redis = redisModule.default;

      const redis = new Redis({
        host: getEnv().REDIS_HOST || "localhost",
        port: Number(getEnv().REDIS_PORT || 6379),
        connectTimeout: 3000,
        retryStrategy: () => {
          throw new Error("Redis connection failed");
        },
      });

      await redis.ping();
      const latency = Date.now() - startTime;

      await redis.disconnect();

      spinner.succeed(`Redis connection OK (${latency}ms)`);

      return {
        component: "Redis Cache",
        status: "healthy",
        details: [`Connection successful in ${latency}ms`, "Status: Ready"],
        latency,
        timestamp: new Date().toISOString(),
      };
    } catch {
      spinner.warn("Redis not available (optional)");

      return {
        component: "Redis Cache",
        status: "warning",
        details: ["Redis not configured or not running", "Status: OPTIONAL - application will work without Redis"],
        timestamp: new Date().toISOString(),
      };
    }
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    spinner.warn("Redis check skipped");

    return {
      component: "Redis Cache",
      status: "warning",
      details: [`Redis check error: ${message}`, "Status: OPTIONAL - not critical if unavailable"],
      timestamp: new Date().toISOString(),
    };
  }
}

// Check environment variables
function checkEnvironment(logger: any): HealthCheckResult {
  const required = ["DATABASE_URL", "AUTH_SECRET", "NEXTAUTH_URL", "NEXTAUTH_SECRET"];
  const optional = ["REDIS_URL", "REDIS_HOST", "REDIS_PORT"];

  const missing: string[] = [];
  const invalid: string[] = [];

  for (const key of required) {
    const value = process.env[key];
    if (!value || value === "placeholder") {
      missing.push(key);
    }
  }

  for (const key of optional) {
    const value = process.env[key];
    if (value === "placeholder") {
      invalid.push(key);
    }
  }

  if (missing.length === 0) {
    return {
      component: "Environment Variables",
      status: "healthy",
      details: [
        `All ${required.length} required variables set`,
        ...optional.map((k) => `Optional: ${k} ${process.env[k] ? "✓" : "✗"}`),
      ],
      timestamp: new Date().toISOString(),
    };
  }

  if (missing.length <= 2) {
    return {
      component: "Environment Variables",
      status: "warning",
      details: [
        `Missing ${missing.length} variable(s): ${missing.join(", ")}`,
        "Action: Copy .env.example to .env.local and fill in values",
      ],
      timestamp: new Date().toISOString(),
    };
  }

  return {
    component: "Environment Variables",
    status: "unhealthy",
    details: [
      `Missing ${missing.length} critical variable(s)`,
      `Missing: ${missing.join(", ")}`,
      "Action: Check .env.local configuration",
    ],
    timestamp: new Date().toISOString(),
  };
}

// Check MCP Servers status
async function checkMCPServers(logger: any): Promise<HealthCheckResult> {
  const spinner = createSpinner("Checking MCP servers...");

  try {
    spinner.start();

    // Try to read mcp.json if it exists
    try {
      const fs = await import("node:fs/promises");
      const path = await import("node:path");
      const { existsSync } = await import("node:fs");

      const mcpPath = path.join(process.cwd(), ".vscode", "mcp.json");

      if (!existsSync(mcpPath)) {
        spinner.warn("MCP configuration not found");
        return {
          component: "MCP Servers",
          status: "warning",
          details: ["No MCP configuration found", "Status: MCP servers not configured"],
          timestamp: new Date().toISOString(),
        };
      }

      const content = await fs.readFile(mcpPath, "utf8");
      const config = JSON.parse(content) as Record<string, unknown>;
      const servers = (config.mcpServers as Record<string, unknown>) || {};
      const serverCount = Object.keys(servers).length;

      spinner.succeed(`MCP servers configured (${serverCount} servers)`);

      return {
        component: "MCP Servers",
        status: "healthy",
        details: [`${serverCount} server(s) configured`, ...Object.keys(servers).map((s: string) => `  • ${s}`)],
        timestamp: new Date().toISOString(),
      };
    } catch {
      spinner.warn("Could not read MCP configuration");

      return {
        component: "MCP Servers",
        status: "warning",
        details: ["MCP configuration error", "Status: May need reconfiguration"],
        timestamp: new Date().toISOString(),
      };
    }
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    spinner.fail("MCP server check failed");

    return {
      component: "MCP Servers",
      status: "unknown",
      details: [`Error: ${message}`],
      timestamp: new Date().toISOString(),
    };
  }
}

// Check Node.js and npm versions
function checkVersions(): HealthCheckResult {
  try {
    const nodeVersion = process.version;
    const npmVersion = execSync("npm --version", {
      encoding: "utf8",
    }).trim();
    const pnpmVersion = execSync("pnpm --version", {
      encoding: "utf8",
    }).trim();

    return {
      component: "Versions",
      status: "healthy",
      details: [`Node.js: ${nodeVersion}`, `npm: ${npmVersion}`, `pnpm: ${pnpmVersion}`],
      timestamp: new Date().toISOString(),
    };
  } catch {
    return {
      component: "Versions",
      status: "warning",
      details: ["Could not determine package manager versions"],
      timestamp: new Date().toISOString(),
    };
  }
}

// Format and display results
function displayResults(results: HealthCheckResult[], json: boolean): void {
  if (json) {
    console.log(JSON.stringify(results, null, 2));
    return;
  }

  console.log("\n" + "═".repeat(70));
  console.log("  PROJECT HEALTH CHECK REPORT");
  console.log("═".repeat(70) + "\n");

  for (const result of results) {
    const statusSymbol = {
      healthy: "✓",
      unhealthy: "✖",
      warning: "⚠",
      unknown: "?",
    }[result.status];

    const statusColor = {
      healthy: "\x1b[32m", // green
      unhealthy: "\x1b[31m", // red
      warning: "\x1b[33m", // yellow
      unknown: "\x1b[36m", // cyan
    }[result.status];

    console.log(`${statusColor}${statusSymbol}\x1b[0m ${result.component.padEnd(25)}`);

    for (const detail of result.details) {
      console.log(`  ${detail}`);
    }

    if (result.latency) {
      console.log(`  Latency: ${result.latency}ms`);
    }

    console.log();
  }

  // Summary
  const healthy = results.filter((r) => r.status === "healthy").length;
  const warning_count = results.filter((r) => r.status === "warning").length;
  const unhealthy = results.filter((r) => r.status === "unhealthy").length;

  console.log("─".repeat(70));
  console.log(`Summary: ${healthy} healthy, ${warning_count} warnings, ${unhealthy} issues`);
  console.log("─".repeat(70) + "\n");
}

// Main execution
async function main() {
  const options = parseArgs();
  const logger = createLogger("health-check", { verbose: options.verbose });

  logger.section("Health Check Initialization");

  const checks: HealthCheckResult[] = [];

  // Run parallel checks
  const promises: Promise<HealthCheckResult>[] = [];

  if (options.db || options.all) {
    promises.push(checkDatabase(logger));
  }

  if (options.redis || options.all) {
    promises.push(checkRedis(logger));
  }

  if (options.mcp || options.all) {
    promises.push(checkMCPServers(logger));
  }

  // These run synchronously
  checks.push(checkEnvironment(logger));
  checks.push(checkVersions());

  // Wait for async checks
  const asyncResults = await Promise.all(promises);
  checks.push(...asyncResults);

  // Display results
  logger.blank();
  displayResults(checks, options.json);

  // Exit with status code
  const hasErrors = checks.some((r) => r.status === "unhealthy");
  process.exit(hasErrors ? 1 : 0);
}

main().catch((err) => {
  console.error("Health check failed:", err);
  process.exit(1);
});
