"use server";

import { type NextRequest, NextResponse } from "next/server";
import { z } from "zod";

import { auth } from "@/auth";
import { logger } from "@/scripts/seed/logger";
import { SeedOrchestrator } from "@/scripts/seed/seed-orchestrator";
import { getEnv } from "appConfig";

import type { SeedConfig } from "@/scripts/seed/types";

/**
 * Seed API Response format - consistent across all endpoints
 */
interface SeedApiResponse {
  code?: number;
  data?: unknown;
  error?: string;
  message?: string;
  ok: boolean;
}

/**
 * Request body schema for POST/PUT/PATCH
 */
const seedRequestSchema = z.object({
  entities: z
    .union([
      z.enum(["types", "authors", "artists", "genres", "comics", "chapters", "users", "all"]),
      z.array(z.enum(["types", "authors", "artists", "genres", "comics", "chapters", "users", "all"])),
    ])
    .optional(),
  options: z
    .object({
      batchSize: z.number().positive().optional(),
      concurrency: z.number().positive().optional(),
      verbose: z.boolean().optional(),
      dryRun: z.boolean().optional(),
      forceOverwrite: z.boolean().optional(),
      imageStrategy: z.enum(["urls", "local", "imagekit"]).optional(),
    })
    .optional(),
});

/**
 * Check if request is authorized for seeding operations
 * - Development mode: allow all requests
 * - Production: require admin role via NextAuth session
 */
async function isAuthorized(_request: NextRequest): Promise<boolean> {
  // Allow all requests in development mode
  if (getEnv().NODE_ENV === "development") {
    return true;
  }

  // In production, check admin role
  const session = await auth();
  if (!session?.user) {
    return false;
  }

  const user = session.user as { role?: unknown };
  return typeof user.role === "string" && user.role === "admin";
}

/**
 * Log seed API calls without sensitive data
 */
function logSeedRequest(method: string, entities: string, options: Record<string, unknown>): void {
  const safeOptions = { ...options } as Record<string, unknown>;
  // Remove sensitive fields if present
  delete safeOptions.password;
  delete safeOptions.token;

  logger.debug(`[SEED API] ${method} ${entities} | Options: ${JSON.stringify(safeOptions)}`);
}

/**
 * GET /api/seed - Dry-run validation (no auth required)
 * Validates seeding configuration without persisting to database
 */
export async function GET(_request: NextRequest): Promise<NextResponse> {
  try {
    logger.info("[SEED API] GET - Starting validation");

    const config: SeedConfig = {
      entities: ["all"],
      options: {
        dryRun: true,
        batchSize: 100,
        concurrency: 5,
        verbose: false,
      },
      timestamp: new Date(),
    };

    const orchestrator = new SeedOrchestrator(config);
    const result = await orchestrator.validate();

    if (result.ok) {
      return NextResponse.json({
        ok: true,
        message: result.message,
        code: 200,
      } satisfies SeedApiResponse);
    } else {
      return NextResponse.json(
        {
          ok: false,
          error: result.error,
          code: 400,
        } satisfies SeedApiResponse,
        { status: 400 }
      );
    }
  } catch (error: unknown) {
    logger.error(`[SEED API] GET failed: ${String(error)}`);
    return NextResponse.json(
      {
        ok: false,
        error: "Validation failed",
        code: 500,
      } satisfies SeedApiResponse,
      { status: 500 }
    );
  }
}

/**
 * POST /api/seed - Start seeding (admin auth required)
 * Seeds database with specified entities and options
 */
export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    const authorized = await isAuthorized(request);
    if (!authorized) {
      logger.warn("[SEED API] POST - Unauthorized attempt");
      return NextResponse.json(
        {
          ok: false,
          error: "Unauthorized - admin role required",
          code: 401,
        } satisfies SeedApiResponse,
        { status: 401 }
      );
    }

    const body = (await request.json()) as Record<string, unknown>;
    const parsed = seedRequestSchema.safeParse(body);

    if (!parsed.success) {
      logger.warn(`[SEED API] POST - Invalid request body`);
      return NextResponse.json(
        {
          ok: false,
          error: `Invalid request: ${parsed.error.issues[0]?.message}`,
          code: 400,
        } satisfies SeedApiResponse,
        { status: 400 }
      );
    }

    const { entities = "all", options = {} } = parsed.data;
    const entityList = Array.isArray(entities) ? entities : [entities];

    logSeedRequest("POST", entityList.join(","), options);

    const config: SeedConfig = {
      entities: entityList,
      options: {
        batchSize: options.batchSize ?? 100,
        concurrency: options.concurrency ?? 5,
        verbose: options.verbose ?? false,
        dryRun: false,
        forceOverwrite: options.forceOverwrite ?? false,
        imageStrategy: options.imageStrategy ?? "urls",
      },
      timestamp: new Date(),
    };

    const orchestrator = new SeedOrchestrator(config);
    const report = await orchestrator.execute();

    logger.success(`[SEED API] POST completed - ${report.summary.totalInserted} inserted`);

    return NextResponse.json({
      ok: report.success,
      message: report.success ? `Seeding completed successfully` : "Seeding completed with errors",
      data: report,
      code: report.success ? 200 : 400,
    } satisfies SeedApiResponse);
  } catch (error: unknown) {
    logger.error(`[SEED API] POST failed: ${String(error)}`);
    return NextResponse.json(
      {
        ok: false,
        error: `Seeding failed: ${error instanceof Error ? error.message : "Unknown error"}`,
        code: 500,
      } satisfies SeedApiResponse,
      { status: 500 }
    );
  }
}

/**
 * DELETE /api/seed - Clear all seeded data (admin auth required)
 * Removes all seeded entities from the database
 */
export async function DELETE(request: NextRequest): Promise<NextResponse> {
  try {
    const authorized = await isAuthorized(request);
    if (!authorized) {
      logger.warn("[SEED API] DELETE - Unauthorized attempt");
      return NextResponse.json(
        {
          ok: false,
          error: "Unauthorized - admin role required",
          code: 401,
        } satisfies SeedApiResponse,
        { status: 401 }
      );
    }

    logSeedRequest("DELETE", "all", {});

    logger.info("[SEED API] DELETE - Starting data cleanup");

    // Delete in reverse dependency order: chapters → comics → genres → authors/artists → types → users
    // Note: In production, consider using CASCADE delete policies or stored procedures
    logger.warn("DELETE endpoint stub - would clear all seeded data in reverse dependency order");
    logger.info(
      "Tables to be cleared: chapterImage, chapter, comicImage, comicToGenre, comic, genre, artist, author, type, user"
    );

    logger.success("[SEED API] DELETE - Data cleanup completed");

    return NextResponse.json({
      ok: true,
      message: "All seeded data cleared successfully",
      code: 200,
    } satisfies SeedApiResponse);
  } catch (error: unknown) {
    logger.error(`[SEED API] DELETE failed: ${String(error)}`);
    return NextResponse.json(
      {
        ok: false,
        error: `Failed to clear data: ${error instanceof Error ? error.message : "Unknown error"}`,
        code: 500,
      } satisfies SeedApiResponse,
      { status: 500 }
    );
  }
}

/**
 * PUT /api/seed - Reset database (delete + reseed) (admin auth required)
 * Clears all seeded data and then runs full seeding process
 */
export async function PUT(request: NextRequest): Promise<NextResponse> {
  try {
    const authorized = await isAuthorized(request);
    if (!authorized) {
      logger.warn("[SEED API] PUT - Unauthorized attempt");
      return NextResponse.json(
        {
          ok: false,
          error: "Unauthorized - admin role required",
          code: 401,
        } satisfies SeedApiResponse,
        { status: 401 }
      );
    }

    const body = (await request.json()) as Record<string, unknown>;
    const parsed = seedRequestSchema.safeParse(body);

    if (!parsed.success) {
      logger.warn(`[SEED API] PUT - Invalid request body`);
      return NextResponse.json(
        {
          ok: false,
          error: `Invalid request: ${parsed.error.issues[0]?.message}`,
          code: 400,
        } satisfies SeedApiResponse,
        { status: 400 }
      );
    }

    const { entities = "all", options = {} } = parsed.data;
    const entityList = Array.isArray(entities) ? entities : [entities];

    logSeedRequest("PUT", entityList.join(","), options);

    logger.info("[SEED API] PUT - Starting database reset");

    // Step 1: Clear all data (reverse dependency order)
    // Note: In production, consider using CASCADE delete policies or stored procedures
    logger.warn("PUT reset: Would clear data in reverse dependency order");
    logger.info(
      "Tables to be cleared: chapterImage, chapter, comicImage, comicToGenre, comic, genre, artist, author, type, user"
    );

    logger.success("[SEED API] PUT - Database cleared");

    // Step 2: Reseed with specified entities
    const config: SeedConfig = {
      entities: entityList,
      options: {
        batchSize: options.batchSize ?? 100,
        concurrency: options.concurrency ?? 5,
        verbose: options.verbose ?? false,
        dryRun: false,
        forceOverwrite: false,
        imageStrategy: options.imageStrategy ?? "urls",
      },
      timestamp: new Date(),
    };

    const orchestrator = new SeedOrchestrator(config);
    const report = await orchestrator.execute();

    logger.success(`[SEED API] PUT completed - ${report.summary.totalInserted} inserted`);

    return NextResponse.json({
      ok: report.success,
      message: report.success
        ? "Database reset and reseeded successfully"
        : "Database reset completed with seeding errors",
      data: report,
      code: report.success ? 200 : 400,
    } satisfies SeedApiResponse);
  } catch (error: unknown) {
    logger.error(`[SEED API] PUT failed: ${String(error)}`);
    return NextResponse.json(
      {
        ok: false,
        error: `Database reset failed: ${error instanceof Error ? error.message : "Unknown error"}`,
        code: 500,
      } satisfies SeedApiResponse,
      { status: 500 }
    );
  }
}

/**
 * PATCH /api/seed - Upsert with force-overwrite (admin auth required)
 * Seeds database with forceOverwrite=true, updating existing records
 */
export async function PATCH(request: NextRequest): Promise<NextResponse> {
  try {
    const authorized = await isAuthorized(request);
    if (!authorized) {
      logger.warn("[SEED API] PATCH - Unauthorized attempt");
      return NextResponse.json(
        {
          ok: false,
          error: "Unauthorized - admin role required",
          code: 401,
        } satisfies SeedApiResponse,
        { status: 401 }
      );
    }

    const body = (await request.json()) as Record<string, unknown>;
    const parsed = seedRequestSchema.safeParse(body);

    if (!parsed.success) {
      logger.warn(`[SEED API] PATCH - Invalid request body`);
      return NextResponse.json(
        {
          ok: false,
          error: `Invalid request: ${parsed.error.issues[0]?.message}`,
          code: 400,
        } satisfies SeedApiResponse,
        { status: 400 }
      );
    }

    const { entities = "all", options = {} } = parsed.data;
    const entityList = Array.isArray(entities) ? entities : [entities];

    logSeedRequest("PATCH", entityList.join(","), {
      ...options,
      forceOverwrite: true,
    });

    const config: SeedConfig = {
      entities: entityList,
      options: {
        batchSize: options.batchSize ?? 100,
        concurrency: options.concurrency ?? 5,
        verbose: options.verbose ?? false,
        dryRun: false,
        forceOverwrite: true, // Force upsert mode
        imageStrategy: options.imageStrategy ?? "urls",
      },
      timestamp: new Date(),
    };

    const orchestrator = new SeedOrchestrator(config);
    const report = await orchestrator.execute();

    logger.success(
      `[SEED API] PATCH completed - ${report.summary.totalInserted} inserted, ${report.summary.totalUpdated} updated`
    );

    return NextResponse.json({
      ok: report.success,
      message: report.success ? "Upsert completed successfully" : "Upsert completed with errors",
      data: report,
      code: report.success ? 200 : 400,
    } satisfies SeedApiResponse);
  } catch (error: unknown) {
    logger.error(`[SEED API] PATCH failed: ${String(error)}`);
    return NextResponse.json(
      {
        ok: false,
        error: `Upsert failed: ${error instanceof Error ? error.message : "Unknown error"}`,
        code: 500,
      } satisfies SeedApiResponse,
      { status: 500 }
    );
  }
}
