/**
 * Seed System Exports
 * Central export point for all seeders and orchestrator
 * Used by CLI and REST API endpoints
 */

// Core exports
export { dataLoader } from "./data-loader";
export { logger } from "./logger";
export { SeedOrchestrator } from "./seed-orchestrator";

// Seeder exports
export { ArtistSeeder } from "./seeders/artist-seeder";
export { AuthorSeeder } from "./seeders/author-seeder";
export { BaseSeeder } from "./seeders/base-seed";
export { BookmarkSeeder } from "./seeders/bookmark-seeder";
export { ChapterImageSeeder } from "./seeders/chapter-image-seeder";
export { ChapterSeeder } from "./seeders/chapter-seeder";
export { ComicImageSeeder } from "./seeders/comic-image-seeder";
export { ComicSeeder } from "./seeders/comic-seeder";
export { CommentSeeder } from "./seeders/comment-seeder";
export { FollowSeeder } from "./seeders/follow-seeder";
export { GenreSeeder } from "./seeders/genre-seeder";
export { NotificationSeeder } from "./seeders/notification-seeder";
export { PermissionSeeder } from "./seeders/permission-seeder";
export { RatingSeeder } from "./seeders/rating-seeder";
export { ReaderSettingsSeeder } from "./seeders/reader-settings-seeder";
export { ReadingGoalSeeder } from "./seeders/reading-goal-seeder";
export { ReadingHistorySeeder } from "./seeders/reading-history-seeder";
export { RoleSeeder } from "./seeders/role-seeder";
export { ShareSeeder } from "./seeders/share-seeder";
export { TypeSeeder } from "./seeders/type-seeder";
export { UserPreferenceSeeder } from "./seeders/user-preference-seeder";
export { UserRoleSeeder } from "./seeders/user-role-seeder";
export { UserSeeder } from "./seeders/user-seeder";

// Image helper exports
export {
  COMICWISE_BRAND,
  getChapterPageFallback,
  getComicWiseLogoPlaceholder,
  getCoverFallback,
  getPlaceholder,
} from "./helpers/image-fallback";
export { migrateImages } from "./helpers/image-migrator";
export { isValidImageUrl } from "./helpers/image-url-validator";

// Type exports
export type { EntityResult, SeedConfig, SeedOptions, SeedReport } from "./types";

// Helper exports
export { extractChapterNumber } from "./helpers/chapter-number-extractor";
export { normalizeCreatorName, splitCreators } from "./helpers/creator-name-resolver";
export { parseDate } from "./helpers/date-parser";
