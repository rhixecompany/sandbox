/**
 * Shared Types Index
 * Central export file for all shared TypeScript types
 */

// Re-export from individual type files
export type { ActionResult } from "./actions-types";
export type { BookmarkCardData, BookmarkFilter, BookmarksListResult } from "./bookmark";
export type {
  ChapterInfo,
  ComicDetail,
  ComicFilterOptions,
  ComicSummary,
  ComicWithType,
  GenreInfo,
  PersonInfo,
  RelatedComic,
} from "./comic";
export type {
  CommentData,
  CommentRatingData,
  CommentWithReplies,
  CreateCommentData,
  CreateRatingData,
  RatingWithComic,
  UpdateCommentData,
  UpdateRatingData,
} from "./comment";
export type { NotificationData, NotificationStats, NotificationType, NotificationTypeConfig } from "./notification";
export type { ChangePasswordData, EditProfileData, ProfileWrapperProps, UserProfile, UserStats } from "./profile";
