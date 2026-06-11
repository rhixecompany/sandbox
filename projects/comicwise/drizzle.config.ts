import path from "node:path";

import * as dotenv from "dotenv";
import { defineConfig } from "drizzle-kit";

import type { Config } from "drizzle-kit";

// Load .env files for local dev/migration runs. Non-destructive.
dotenv.config({ path: path.resolve(process.cwd(), ".env.local") });
dotenv.config();

// Resolve DB URL with multiple fallbacks and helpful error message
const resolveDatabaseUrl = (): string => {
  let envUrl = process.env["DATABASE_URL"] ?? process.env["NEON_DATABASE_URL"];

  if (!envUrl) {
    try {
      // Try to read validated env from the project's env helper (if present)
      // Prefer dynamic import for compatibility and type safety
      const environmentModule = import("./appConfig") as {
        env?: { DATABASE_URL?: string };
      };
      if (environmentModule?.env?.DATABASE_URL) {
        envUrl = environmentModule.env.DATABASE_URL;
      }
    } catch {
      // ignore - will throw below if still missing
    }
  }

  if (!envUrl) {
    throw new Error(
      "DATABASE_URL or NEON_DATABASE_URL must be defined in environment variables (set in .env.local or environment)."
    );
  }

  return envUrl;
};

// Drizzle config with connection pooling hints for production
const cfg: Config = {
  schema: "src/database/schema.ts",
  out: "src/database/drizzle",
  dialect: "postgresql",
  dbCredentials: {
    url: resolveDatabaseUrl(),
    // Optional: additional connection info supported by some drivers
    pool: { max: 20, min: 2 }, // Drizzle will use underlying driver's pooling
  },
  // Verbose migration output for CI and local runs
  verbose: process.env["VERBOSE_DRIZZLE"] === "true" || process.env.NODE_ENV !== "production",
  strict: true,
} as Config;

export default defineConfig(cfg);
