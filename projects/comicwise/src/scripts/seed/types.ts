/**
 * Core type definitions for the database seeding system
 * @module types
 */

/**
 * Update mode for existing records
 */
export type UpdateMode = "full" | "none" | "smart";

/**
 * Options for configuring seed behavior
 */
export interface SeedOptions {
  batchSize?: number;
  bcryptRounds?: number; // configurable bcrypt salt rounds (default: 10)
  checkpointDir?: string; // directory to store checkpoint files
  // New options for chunked seeding and checkpointing
  chunkSize?: number; // when set, enables chunked mode
  concurrency?: number;
  // Seeder-specific options
  count?: number; // target entity count (used by user seeder for synthetic generation)
  dryRun?: boolean;
  // Deduplication options
  enableDeduplication?: boolean; // enable content-based deduplication (default: true for local)
  failOnError?: boolean; // abort on first chunk error

  forceOverwrite?: boolean;
  imageQuality?: number; // image quality 1-100 (default: 75)
  imageStrategy?: "imagekit" | "local" | "urls";
  maxImageWidth?: number; // max image width in pixels (default: 1200)
  optimizeImages?: boolean; // enable image optimization (default: true for local strategy)
  pauseBetweenChunksMs?: number; // optional pause between chunks
  reprocessExisting?: boolean; // re-process existing downloaded images
  resume?: boolean; // if true, will attempt to resume from checkpoint
  skipValidation?: boolean;

  // Update mode: none (skip existing), smart (update if different), full (overwrite all)
  updateMode?: UpdateMode;

  useTransaction?: boolean;
  verbose?: boolean;
}

/**
 * Configuration object passed to SeedOrchestrator
 */
export interface SeedConfig {
  entities: (
    | "all"
    | "artists"
    | "authors"
    | "bookmarks"
    | "chapter-images"
    | "chapters"
    | "comic-images"
    | "comics"
    | "comments"
    | "follows"
    | "genres"
    | "notifications"
    | "permissions"
    | "ratings"
    | "reader-settings"
    | "reading-goals"
    | "reading-history"
    | "roles"
    | "shares"
    | "types"
    | "user-preferences"
    | "user-roles"
    | "users"
  )[];
  options: SeedOptions;
  timestamp: Date;
}

/**
 * Individual entity seeding result
 */
export interface EntityResult {
  duration: number;
  entityName: string;
  errors: SeedError[];
  inserted: number;
  skipped: number;
  success: boolean;
  updated: number;
}

/**
 * Information about a single seeding error
 */
export interface SeedError {
  itemIndex: number;
  message: string;
  value: unknown;
}

/**
 * Complete seeding report with aggregated metrics
 */
export interface SeedReport {
  errors: string[];
  results: EntityResult[];
  success: boolean;
  summary: {
    totalErrors: number;
    totalInserted: number;
    totalSkipped: number;
    totalUpdated: number;
  };
  timestamp: Date;
  totalDuration: number;
  warnings: string[];
}

/**
 * Per-entity breakdown in seed report
 */
export interface EntityBreakdown {
  duration: number;
  entity: string;
  errors: number;
  inserted: number;
  percentage: number;
  skipped: number;
  updated: number;
}

/**
 * Performance metrics for seed report
 */
export interface PerformanceMetrics {
  avgPerEntity: number;
  fastestDuration: number;
  fastestEntity: string;
  slowestDuration: number;
  slowestEntity: string;
  totalDuration: number;
  totalRecords: number;
}

/**
 * Comprehensive seed report with detailed breakdowns
 */
export interface ComprehensiveSeedReport extends SeedReport {
  details: {
    entityBreakdown: EntityBreakdown[];
    performanceMetrics: PerformanceMetrics;
  };
}

/**
 * Standard action result type for server operations
 */
export type ActionResult<T> = { data: T; ok: true } | { error: string; ok: false };

/**
 * Context for image processing strategy
 */
export interface ImageStrategyContext {
  concurrency?: number;
  imageKitConfig?: {
    privateKey: string;
    publicKey: string;
    urlEndpoint: string;
  };
  localPath?: string;
  mode: "imagekit" | "local" | "urls";
  optimization?: {
    enabled: boolean;
    maxWidth: number;
    maxHeight: number;
    quality: number;
  };
}

/**
 * Progress metrics for a batch operation
 */
export interface ProgressMetrics {
  duration: number;
  errors: number;
  inserted: number;
  itemsPerSecond: number;
  skipped: number;
  successRate: number;
  taskName: string;
  total: number;
  updated: number;
}

/**
 * Batch processing options
 */
export interface BatchProcessorOptions {
  batchSize: number;
  concurrency: number;
  onBatchComplete?: (result: { batchIndex: number; processed: number }) => Promise<void>;
  onError?: (error: Error, itemIndex: number) => Promise<void>;
}

/**
 * Result of a batch processing operation
 */
export interface BatchProcessorResult<T> {
  errors: Array<{ error: Error; index: number }>;
  results: T[];
  totalProcessed: number;
}

/**
 * Transaction context for database operations
 */
export interface TransactionContext {
  entityName: string;
  isolationLevel?: "read_committed" | "read_uncommitted" | "repeatable_read" | "serializable";
  useTransaction: boolean;
}

/**
 * Cache for storing looked-up entity IDs to avoid duplicate queries
 */
export interface LookupCache {
  artists: Map<string, { id: string; name: string }>;
  authors: Map<string, { id: string; name: string }>;
  comics: Map<string, number>; // slug → id
  genres: Map<string, number>; // name → id
  roles: Map<string, number>; // name → id
  types: Map<string, number>; // name → id
  users: Map<string, string>; // email → id
}

/**
 * Metadata describing a seeder's dependencies and characteristics
 */
export interface SeederMetadata {
  dependencies: string[]; // e.g., ["users", "types"]
  description: string; // human-readable purpose
  entityName: string;
  isOptional?: boolean; // if true, failure doesn't block dependents
  priority: number; // 1=highest, 10=lowest (for ordering when no deps)
  supportsRollback: boolean; // can be rolled back if needed
}

/**
 * Dependency graph node
 */
export interface DependencyGraphNode {
  dependents: string[]; // entities that depend on this one
  metadata: SeederMetadata;
}

/**
 * Complete dependency graph structure
 */
export interface DependencyGraph {
  edges: Map<string, Set<string>>; // entityA -> [entityB, entityC] (entityA depends on B, C)
  nodes: Map<string, DependencyGraphNode>;
  ordered: string[]; // topologically sorted order
}

/**
 * Validation error in dependency graph
 */
export interface DependencyValidationError {
  affectedEntities?: string[];
  entity: string;
  message: string;
  type: "circular" | "invalid-metadata" | "missing-dependency";
}

/**
 * Result of dependency graph validation
 */
export interface DependencyValidationResult {
  errors: DependencyValidationError[];
  valid: boolean;
  warnings: string[];
}

/**
 * Data Transfer Object for User seed data
 */
export interface UserSeedDTO {
  createdAt: Date;
  email: string;
  emailVerified?: Date | null;
  id?: string;
  image?: null | string;
  lastActivityDate?: Date | null;
  name: string;
  password: string;
  role: "admin" | "moderator" | "user";
  status: boolean;
  updatedAt: Date;
}

/**
 * Data Transfer Object for Comic seed data
 */
export interface ComicSeedDTO {
  artistId?: null | string;
  authorId?: null | string;
  coverImage?: null | string;
  description?: string;
  genres: string[]; // genre IDs
  images: string[]; // image URLs
  rating: number;
  serialization?: string;
  slug: string;
  status: "Coming Soon" | "Completed" | "Dropped" | "Hiatus" | "Ongoing" | "Season End";
  title: string;
  typeId?: string;
  updatedAt: Date;
  url?: string;
  views: number;
}

/**
 * Data Transfer Object for Chapter seed data
 */
export interface ChapterSeedDTO {
  chapterNumber: number;
  comicId: string;
  content?: string;
  images: string[]; // image URLs
  releaseDate?: Date;
  slug: string;
  title: string;
  updatedAt: Date;
  url?: string;
}

/**
 * Image download/upload result
 */
export interface ImageProcessingResult {
  duration: number;
  error?: string;
  originalUrl: string;
  processedUrl?: string;
  success: boolean;
}

/**
 * Status of a seeding operation
 */
export type SeedingStatus = "completed" | "failed" | "pending" | "running";
