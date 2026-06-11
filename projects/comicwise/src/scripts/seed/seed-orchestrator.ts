/**
 * SeedOrchestrator - Orchestrates seeding in dependency order
 * Manages LookupCache, coordinates seeders, aggregates results, and validates dependency graph
 */

import { configureImageDownloader } from "@/storages/image-downloader";
import { DependencyGraphBuilder, DependencyGraphValidator } from "./dependency-graph";
import { logger } from "./logger";
import { ArtistSeeder } from "./seeders/artist-seeder";
import { AuthorSeeder } from "./seeders/author-seeder";
import { BookmarkSeeder } from "./seeders/bookmark-seeder";
import { ChapterImageSeeder } from "./seeders/chapter-image-seeder";
import { ChapterSeeder } from "./seeders/chapter-seeder";
import { ComicImageSeeder } from "./seeders/comic-image-seeder";
import { ComicSeeder } from "./seeders/comic-seeder";
import { CommentSeeder } from "./seeders/comment-seeder";
import { FollowSeeder } from "./seeders/follow-seeder";
import { GenreSeeder } from "./seeders/genre-seeder";
import { NotificationSeeder } from "./seeders/notification-seeder";
import { PermissionSeeder } from "./seeders/permission-seeder";
import { RatingSeeder } from "./seeders/rating-seeder";
import { ReaderSettingsSeeder } from "./seeders/reader-settings-seeder";
import { ReadingGoalSeeder } from "./seeders/reading-goal-seeder";
import { ReadingHistorySeeder } from "./seeders/reading-history-seeder";
import { RoleSeeder } from "./seeders/role-seeder";
import { ShareSeeder } from "./seeders/share-seeder";
import { TypeSeeder } from "./seeders/type-seeder";
import { UserPreferenceSeeder } from "./seeders/user-preference-seeder";
import { UserRoleSeeder } from "./seeders/user-role-seeder";
import { UserSeeder } from "./seeders/user-seeder";

import type {
  ComprehensiveSeedReport,
  EntityBreakdown,
  EntityResult,
  LookupCache,
  SeedConfig,
  SeederMetadata,
} from "./types";

/**
 * SeedOrchestrator orchestrates seeding in dependency order
 * Manages shared LookupCache for entity deduplication
 * Validates dependency graph before seeding
 */
export class SeedOrchestrator {
  private config: SeedConfig;
  private cache: LookupCache;
  private results: EntityResult[] = [];
  private seeders: Map<
    string,
    InstanceType<
      | typeof ArtistSeeder
      | typeof AuthorSeeder
      | typeof BookmarkSeeder
      | typeof ChapterImageSeeder
      | typeof ChapterSeeder
      | typeof ComicImageSeeder
      | typeof ComicSeeder
      | typeof CommentSeeder
      | typeof FollowSeeder
      | typeof GenreSeeder
      | typeof NotificationSeeder
      | typeof PermissionSeeder
      | typeof RatingSeeder
      | typeof ReaderSettingsSeeder
      | typeof ReadingGoalSeeder
      | typeof ReadingHistorySeeder
      | typeof RoleSeeder
      | typeof ShareSeeder
      | typeof TypeSeeder
      | typeof UserPreferenceSeeder
      | typeof UserRoleSeeder
      | typeof UserSeeder
    >
  > = new Map();

  constructor(config: SeedConfig) {
    // Apply sensible defaults for seeding options, including chunk/resume defaults.
    const defaults: Partial<SeedConfig["options"]> = {
      batchSize: 1000,
      concurrency: 4,
      dryRun: false,
      forceOverwrite: false,
      skipValidation: false,
      useTransaction: true,
      verbose: false,
      // Chunking defaults
      chunkSize: 500,
      resume: false,
      checkpointDir: ".seed-checkpoints",
      pauseBetweenChunksMs: 0,
      failOnError: false,
    };

    this.config = {
      ...config,
      options: {
        ...(defaults as any),
        ...(config.options || {}),
      },
    };

    this.cache = this.initializeCache();
  }

  /**
   * Initialize empty cache for entity lookups
   */
  private initializeCache(): LookupCache {
    return {
      authors: new Map(),
      artists: new Map(),
      types: new Map(),
      genres: new Map(),
      comics: new Map(),
      users: new Map(),
      roles: new Map(),
    };
  }

  /**
   * Create all seeder instances and collect metadata
   */
  private createSeeders(): Map<string, SeederMetadata> {
    const seedersMetadata = new Map<string, SeederMetadata>();

    // Instantiate each seeder and collect metadata
    const typeSeeder = new TypeSeeder(this.cache, this.config.options);
    this.seeders.set("types", typeSeeder as never);
    seedersMetadata.set("types", typeSeeder.getMetadata());

    const authorSeeder = new AuthorSeeder(this.cache, this.config.options);
    this.seeders.set("authors", authorSeeder as never);
    seedersMetadata.set("authors", authorSeeder.getMetadata());

    const artistSeeder = new ArtistSeeder(this.cache, this.config.options);
    this.seeders.set("artists", artistSeeder as never);
    seedersMetadata.set("artists", artistSeeder.getMetadata());

    const genreSeeder = new GenreSeeder(this.cache, this.config.options);
    this.seeders.set("genres", genreSeeder as never);
    seedersMetadata.set("genres", genreSeeder.getMetadata());

    const comicSeeder = new ComicSeeder(this.cache, this.config.options);
    this.seeders.set("comics", comicSeeder as never);
    seedersMetadata.set("comics", comicSeeder.getMetadata());

    const comicImageSeeder = new ComicImageSeeder(this.cache, this.config.options);
    this.seeders.set("comic-images", comicImageSeeder as never);
    seedersMetadata.set("comic-images", comicImageSeeder.getMetadata());

    const chapterSeeder = new ChapterSeeder(this.cache, this.config.options);
    this.seeders.set("chapters", chapterSeeder as never);
    seedersMetadata.set("chapters", chapterSeeder.getMetadata());

    const chapterImageSeeder = new ChapterImageSeeder(this.cache, this.config.options);
    this.seeders.set("chapter-images", chapterImageSeeder as never);
    seedersMetadata.set("chapter-images", chapterImageSeeder.getMetadata());

    const userSeeder = new UserSeeder(this.cache, this.config.options);
    this.seeders.set("users", userSeeder as never);
    seedersMetadata.set("users", userSeeder.getMetadata());

    const roleSeeder = new RoleSeeder(this.cache, this.config.options);
    this.seeders.set("roles", roleSeeder as never);
    seedersMetadata.set("roles", roleSeeder.getMetadata());

    const permissionSeeder = new PermissionSeeder(this.cache, this.config.options);
    this.seeders.set("permissions", permissionSeeder as never);
    seedersMetadata.set("permissions", permissionSeeder.getMetadata());

    const userRoleSeeder = new UserRoleSeeder(this.cache, this.config.options);
    this.seeders.set("user-roles", userRoleSeeder as never);
    seedersMetadata.set("user-roles", userRoleSeeder.getMetadata());

    const userPreferenceSeeder = new UserPreferenceSeeder(this.cache, this.config.options);
    this.seeders.set("user-preferences", userPreferenceSeeder as never);
    seedersMetadata.set("user-preferences", userPreferenceSeeder.getMetadata());

    const readerSettingsSeeder = new ReaderSettingsSeeder(this.cache, this.config.options);
    this.seeders.set("reader-settings", readerSettingsSeeder as never);
    seedersMetadata.set("reader-settings", readerSettingsSeeder.getMetadata());

    const readingGoalSeeder = new ReadingGoalSeeder(this.cache, this.config.options);
    this.seeders.set("reading-goals", readingGoalSeeder as never);
    seedersMetadata.set("reading-goals", readingGoalSeeder.getMetadata());

    const bookmarkSeeder = new BookmarkSeeder(this.cache, this.config.options);
    this.seeders.set("bookmarks", bookmarkSeeder as never);
    seedersMetadata.set("bookmarks", bookmarkSeeder.getMetadata());

    const ratingSeeder = new RatingSeeder(this.cache, this.config.options);
    this.seeders.set("ratings", ratingSeeder as never);
    seedersMetadata.set("ratings", ratingSeeder.getMetadata());

    const commentSeeder = new CommentSeeder(this.cache, this.config.options);
    this.seeders.set("comments", commentSeeder as never);
    seedersMetadata.set("comments", commentSeeder.getMetadata());

    const notificationSeeder = new NotificationSeeder(this.cache, this.config.options);
    this.seeders.set("notifications", notificationSeeder as never);
    seedersMetadata.set("notifications", notificationSeeder.getMetadata());

    const readingHistorySeeder = new ReadingHistorySeeder(this.cache, this.config.options);
    this.seeders.set("reading-history", readingHistorySeeder as never);
    seedersMetadata.set("reading-history", readingHistorySeeder.getMetadata());

    const followSeeder = new FollowSeeder(this.cache, this.config.options);
    this.seeders.set("follows", followSeeder as never);
    seedersMetadata.set("follows", followSeeder.getMetadata());

    const shareSeeder = new ShareSeeder(this.cache, this.config.options);
    this.seeders.set("shares", shareSeeder as never);
    seedersMetadata.set("shares", shareSeeder.getMetadata());

    return seedersMetadata;
  }

  /**
   * Execute seeding in dependency order
   * Builds and validates dependency graph, then seeds in topological order
   *
   * Returns aggregated SeedReport across all seeders
   */
  async execute(): Promise<ComprehensiveSeedReport> {
    const startTime = Date.now();

    try {
      // Create all seeders and collect metadata
      const seedersMetadata = this.createSeeders();

      // Build dependency graph
      logger.section("Building Dependency Graph");
      const graphBuilder = new DependencyGraphBuilder(seedersMetadata);
      const { graph, errors: graphErrors } = graphBuilder.build();

      if (!graph || graphErrors.length > 0) {
        logger.error("Dependency graph validation failed:");
        for (const err of graphErrors) {
          logger.error(`  ${err.type}: ${err.message}`);
        }

        return {
          timestamp: this.config.timestamp,
          success: false,
          totalDuration: Date.now() - startTime,
          results: [],
          warnings: [],
          errors: graphErrors.map((e: (typeof graphErrors)[0]) => e.message),
          summary: {
            totalInserted: 0,
            totalUpdated: 0,
            totalSkipped: 0,
            totalErrors: graphErrors.length,
          },
          details: this.createEmptyDetails(),
        };
      }

      logger.success("Dependency graph built successfully");

      if (this.config.options.verbose) {
        logger.info(graphBuilder.generateASCIIGraph(graph));
      }

      // Validate seeding plan
      const plan = this.getSeededEntities();
      const validation = DependencyGraphValidator.validateSeedingPlan(graph, plan);

      if (!validation.valid) {
        logger.error("Seeding plan validation failed:");
        for (const err of validation.errors) {
          logger.error(`  ${err}`);
        }

        return {
          timestamp: this.config.timestamp,
          success: false,
          totalDuration: Date.now() - startTime,
          results: [],
          warnings: validation.warnings,
          errors: validation.errors,
          summary: {
            totalInserted: 0,
            totalUpdated: 0,
            totalSkipped: 0,
            totalErrors: validation.errors.length,
          },
          details: this.createEmptyDetails(),
        };
      }

      if (validation.warnings.length > 0) {
        for (const warn of validation.warnings) {
          logger.warn(warn);
        }
      }

      // Use validated ordered list
      const entitiesToSeed = validation.orderedActual;

      logger.section("Database Seeding");
      logger.info(
        `Seeding ${entitiesToSeed.length} entities: ${entitiesToSeed.join(", ")}${this.config.options.dryRun ? " (DRY RUN)" : ""}`
      );

      // Configure image downloader with optimization settings
      const shouldOptimize =
        this.config.options.optimizeImages !== false && this.config.options.imageStrategy === "local";

      if (shouldOptimize) {
        logger.info(
          `Image optimization enabled: maxWidth=${this.config.options.maxImageWidth}, quality=${this.config.options.imageQuality}`
        );
        configureImageDownloader({
          enabled: true,
          maxWidth: this.config.options.maxImageWidth || 1200,
          maxHeight: 2000,
          quality: this.config.options.imageQuality || 75,
        });
      }

      // Seed in dependency order
      for (const entity of entitiesToSeed) {
        const seeder = this.seeders.get(entity);
        if (seeder) {
          const result = await seeder.seed();
          this.results.push(result);
        } else {
          logger.warn(`No seeder found for entity: ${entity}`);
        }
      }

      const duration = Date.now() - startTime;
      return await this.generateReport(duration);
    } catch (error) {
      const duration = Date.now() - startTime;
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`Seeding failed: ${message}`);

      return {
        timestamp: this.config.timestamp,
        success: false,
        totalDuration: duration,
        results: this.results,
        warnings: [],
        errors: [message],
        summary: {
          totalInserted: 0,
          totalUpdated: 0,
          totalSkipped: 0,
          totalErrors: 1,
        },
        details: this.createEmptyDetails(),
      };
    }
  }

  /**
   * Create empty details for error cases
   */
  private createEmptyDetails() {
    return {
      entityBreakdown: [],
      performanceMetrics: {
        totalDuration: 0,
        avgPerEntity: 0,
        fastestEntity: "",
        fastestDuration: 0,
        slowestEntity: "",
        slowestDuration: 0,
        totalRecords: 0,
      },
    };
  }

  /**
   * Get list of entities to seed based on config
   */
  private getSeededEntities(): string[] {
    const allEntities = [
      "users",
      "roles",
      "permissions",
      "types",
      "authors",
      "artists",
      "genres",
      "comics",
      "comic-images",
      "chapters",
      "chapter-images",
      "bookmarks",
      "comments",
      "ratings",
      "notifications",
      "reader-settings",
      "user-roles",
      "user-preferences",
      "reading-history",
      "reading-goals",
      "follows",
      "shares",
    ];

    if (this.config.entities.includes("all") || this.config.entities.length === 0) {
      return allEntities;
    }

    return this.config.entities.filter((entity) => allEntities.includes(entity as never)) as string[];
  }

  /**
   * Generate comprehensive SeedReport with detailed breakdowns
   */
  private async generateReport(duration: number): Promise<ComprehensiveSeedReport> {
    const summary = {
      totalInserted: 0,
      totalUpdated: 0,
      totalSkipped: 0,
      totalErrors: 0,
    };

    const warnings: string[] = [];
    const errors: string[] = [];

    // Calculate totals and build breakdowns
    const entityBreakdown: EntityBreakdown[] = [];

    for (const result of this.results) {
      summary.totalInserted += result.inserted;
      summary.totalUpdated += result.updated;
      summary.totalSkipped += result.skipped;
      summary.totalErrors += result.errors.length;

      // Collect errors
      for (const error of result.errors) {
        errors.push(`${result.entityName}: ${error.message}`);
      }

      // Generate warnings for unusual patterns
      if (result.skipped > result.inserted && result.skipped > 0) {
        warnings.push(`${result.entityName}: High skip rate (${result.skipped} skipped, ${result.inserted} inserted)`);
      }

      // Build entity breakdown
      const total = result.inserted + result.updated + result.skipped;
      const percentage = total > 0 ? ((result.inserted + result.updated) / total) * 100 : 0;

      entityBreakdown.push({
        entity: result.entityName,
        inserted: result.inserted,
        updated: result.updated,
        skipped: result.skipped,
        errors: result.errors.length,
        duration: result.duration,
        percentage,
      });
    }

    // Calculate performance metrics
    const totalRecords = summary.totalInserted + summary.totalUpdated;
    const fastest = entityBreakdown.reduce((min, e) => (e.duration < min.duration ? e : min), {
      entity: "",
      duration: Infinity,
    } as EntityBreakdown);
    const slowest = entityBreakdown.reduce((max, e) => (e.duration > max.duration ? e : max), {
      entity: "",
      duration: 0,
    } as EntityBreakdown);

    const performanceMetrics = {
      totalDuration: duration,
      avgPerEntity: this.results.length > 0 ? duration / this.results.length : 0,
      fastestEntity: fastest.entity,
      fastestDuration: fastest.duration,
      slowestEntity: slowest.entity,
      slowestDuration: slowest.duration,
      totalRecords,
    };

    // ═══════════════════════════════════════════════════
    // CONSOLE OUTPUT
    // ═══════════════════════════════════════════════════

    logger.section("Seeding Summary");
    logger.success(
      `Total inserted: ${summary.totalInserted} | Updated: ${summary.totalUpdated} | Skipped: ${summary.totalSkipped}`
    );

    if (summary.totalErrors > 0) {
      logger.warn(`Total errors: ${summary.totalErrors} (see details below)`);
    }

    logger.info(`Total duration: ${(duration / 1000).toFixed(2)}s`);

    // ═══════════════════════════════════════════════════
    // DETAILED RESULTS (verbose)
    // ═══════════════════════════════════════════════════

    if (this.config.options.verbose) {
      logger.section("Detailed Results");

      for (const result of this.results) {
        const status = result.errors.length > 0 ? "⚠️" : "✓";
        logger.info(
          `${status} ${result.entityName}: inserted=${result.inserted}, updated=${result.updated}, skipped=${result.skipped}, errors=${result.errors.length} {duration:${result.duration}ms}`
        );
      }

      // Performance metrics
      logger.section("Performance Metrics");
      logger.info(`Fastest: ${performanceMetrics.fastestEntity} (${performanceMetrics.fastestDuration}ms)`);
      logger.info(`Slowest: ${performanceMetrics.slowestEntity} (${performanceMetrics.slowestDuration}ms)`);
      logger.info(`Average per entity: ${performanceMetrics.avgPerEntity.toFixed(2)}ms`);
    }

    // ═══════════════════════════════════════════════════
    // WARNINGS
    // ═══════════════════════════════════════════════════

    if (warnings.length > 0) {
      logger.section("Warnings");
      for (const warning of warnings) {
        logger.warn(warning);
      }
    }

    // ═══════════════════════════════════════════════════
    // ERRORS
    // ═══════════════════════════════════════════════════

    if (summary.totalErrors > 0) {
      logger.section("Errors");
      for (const error of errors) {
        logger.error(error);
      }
    }

    // ═══════════════════════════════════════════════════
    // SUCCESS/FAILURE
    // ═══════════════════════════════════════════════════

    const success = summary.totalErrors === 0;
    if (success) {
      logger.success("\n✓ Seeding completed successfully");
    } else {
      logger.error("\n✗ Seeding completed with errors");
    }

    // ═══════════════════════════════════════════════════
    // BUILD COMPREHENSIVE REPORT
    // ═══════════════════════════════════════════════════

    const comprehensiveReport: ComprehensiveSeedReport = {
      timestamp: this.config.timestamp,
      success,
      totalDuration: duration,
      results: this.results,
      warnings,
      errors,
      summary: {
        totalInserted: summary.totalInserted,
        totalUpdated: summary.totalUpdated,
        totalSkipped: summary.totalSkipped,
        totalErrors: summary.totalErrors,
      },
      details: {
        entityBreakdown,
        performanceMetrics,
      },
    };

    // ═══════════════════════════════════════════════════
    // JSON REPORT EXPORT
    // ═══════════════════════════════════════════════════

    const reportFilename = `seed-report-${new Date().toISOString().split("T")[0]}.json`;

    try {
      // Use dynamic import for ESM compatibility
      const { writeFileSync } = await import("node:fs");
      writeFileSync(reportFilename, JSON.stringify(comprehensiveReport, null, 2));
      logger.info(`\n📄 Full report saved to: ${reportFilename}`);
    } catch (writeError) {
      logger.warn(`Failed to write report file: ${writeError}`);
    }

    return comprehensiveReport;
  }

  /**
   * Validate seeding without persisting (dry-run)
   * Returns validation summary
   */
  async validate(): Promise<{ error: string; ok: false } | { message: string; ok: true }> {
    try {
      logger.section("Validation (Dry-Run)");
      logger.info("Validating seeding configuration...");

      const config = {
        ...this.config,
        options: {
          ...this.config.options,
          dryRun: true,
        },
      };

      const mockOrchestrator = new SeedOrchestrator(config);
      const report = await mockOrchestrator.execute();

      if (report.success) {
        return {
          ok: true,
          message: `Validation successful: would insert ${report.summary.totalInserted} records`,
        };
      } else {
        return {
          ok: false,
          error: `Validation failed: ${report.errors.join("; ")}`,
        };
      }
    } catch (error) {
      return {
        ok: false,
        error: error instanceof Error ? error.message : String(error),
      };
    }
  }

  /**
   * Export comprehensive report to JSON string
   */
  public exportToJson(report: ComprehensiveSeedReport): string {
    return JSON.stringify(report, null, 2);
  }

  /**
   * Export entity breakdown to CSV string
   */
  public exportToCsv(report: ComprehensiveSeedReport): string {
    const headers = ["Entity", "Inserted", "Updated", "Skipped", "Errors", "Duration(ms)", "Percentage(%)"];
    const rows = report.details.entityBreakdown.map((e: EntityBreakdown) => [
      e.entity,
      String(e.inserted),
      String(e.updated),
      String(e.skipped),
      String(e.errors),
      String(e.duration),
      e.percentage.toFixed(2),
    ]);

    return [headers.join(","), ...rows.map((r) => r.join(","))].join("\n");
  }

  /**
   * Export summary to CSV string (compact format)
   */
  public exportSummaryToCsv(report: ComprehensiveSeedReport): string {
    return [
      "Metric,Value",
      `Total Inserted,${report.summary.totalInserted}`,
      `Total Updated,${report.summary.totalUpdated}`,
      `Total Skipped,${report.summary.totalSkipped}`,
      `Total Errors,${report.summary.totalErrors}`,
      `Total Duration (ms),${report.totalDuration}`,
      `Total Records,${report.details.performanceMetrics.totalRecords}`,
      `Avg Per Entity (ms),${report.details.performanceMetrics.avgPerEntity.toFixed(2)}`,
      `Fastest Entity,${report.details.performanceMetrics.fastestEntity} (${report.details.performanceMetrics.fastestDuration}ms)`,
      `Slowest Entity,${report.details.performanceMetrics.slowestEntity} (${report.details.performanceMetrics.slowestDuration}ms)`,
    ].join("\n");
  }
}
