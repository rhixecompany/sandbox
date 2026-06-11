import type { FullConfig } from "@playwright/test";
import * as dotenv from "dotenv";
import { exec } from "node:child_process";
import path from "node:path";
import { promisify } from "node:util";

dotenv.config({ path: path.resolve(process.cwd(), ".env.local") });
dotenv.config();

const { db } = await import("@/database/db");
const { SeedOrchestrator } = await import("@/scripts/seed/seed-orchestrator");

const execAsync = promisify(exec);

async function pushSchema(): Promise<void> {
  console.log("Pushing database schema...");

  try {
    const { stdout, stderr } = await execAsync("pnpm db:push", {
      cwd: process.cwd(),
      env: { ...process.env },
    });

    if (stdout) {
      console.log("Schema push output:", stdout.trim());
    }
    if (stderr) {
      console.warn("Schema push warnings:", stderr.trim());
    }

    console.log("Schema push completed successfully");
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error("Schema push failed:", message);
    const err = new Error(`Failed to push database schema: ${message}`);
    err.cause = error;
    throw err;
  }
}

async function globalSetup(_config: FullConfig) {
  console.log("Running E2E database setup...");

  try {
    // Step 1: Push schema to ensure tables exist
    await pushSchema();

    // Step 2: Seed data
    const orchestrator = new SeedOrchestrator({
      timestamp: new Date(),
      entities: ["all"],
      options: {
        verbose: false,
        useTransaction: false,
        forceOverwrite: false,
        skipValidation: false,
      },
    });

    const result = await orchestrator.execute();

    if (!result.success) {
      console.error("Seeding failed:", result.errors);
      throw new Error(`Database seeding failed: ${result.errors.join(", ")}`);
    }

    console.log(`E2E setup complete: ${result.summary.totalInserted} inserted, ${result.summary.totalUpdated} updated`);
  } catch (error) {
    console.error("E2E setup error:", error);
    throw error;
  } finally {
    await db.$client.end();
  }
}

export default globalSetup;
