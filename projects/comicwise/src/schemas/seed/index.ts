/**
 * Central export point for all seed schemas and inferred types
 * @module index
 */

import { artistSeedItemSchema, artistSeedSchema } from "./artist.seed";
import { authorSeedItemSchema, authorSeedSchema } from "./author.seed";
import { bookmarkSeedItemSchema, bookmarkSeedSchema } from "./bookmark.seed";
import { chapterSeedItemSchema, chapterSeedSchema } from "./chapter.seed";
import { comicSeedItemSchema, comicSeedSchema } from "./comic.seed";
import { commentSeedItemSchema, commentSeedSchema } from "./comment.seed";
import { followSeedItemSchema, followSeedSchema } from "./follow.seed";
import { genreSeedItemSchema, genreSeedSchema } from "./genre.seed";
import { notificationSeedItemSchema, notificationSeedSchema } from "./notification.seed";
import { permissionSeedItemSchema, permissionSeedSchema } from "./permission.seed";
import { ratingSeedItemSchema, ratingSeedSchema } from "./rating.seed";
import { readerSettingsSeedItemSchema, readerSettingsSeedSchema } from "./reader-settings.seed";
import { readingGoalSeedItemSchema, readingGoalSeedSchema } from "./reading-goal.seed";
import { readingHistorySeedItemSchema, readingHistorySeedSchema } from "./reading-history.seed";
import { roleSeedItemSchema, roleSeedSchema } from "./role.seed";
import { shareSeedItemSchema, shareSeedSchema } from "./share.seed";
import { typeSeedItemSchema, typeSeedSchema } from "./type.seed";
import { userPreferenceSeedItemSchema, userPreferenceSeedSchema } from "./user-preference.seed";
import { userRoleSeedItemSchema, userRoleSeedSchema } from "./user-role.seed";
import { userSeedItemSchema, userSeedSchema } from "./user.seed";

export type { AuthorSeed, AuthorSeedArray } from "./author.seed";
export { authorSeedItemSchema, authorSeedSchema };

export type { ArtistSeed, ArtistSeedArray } from "./artist.seed";
export { artistSeedItemSchema, artistSeedSchema };

export type { BookmarkSeed, BookmarkSeedItem } from "./bookmark.seed";
export { bookmarkSeedItemSchema, bookmarkSeedSchema };

export type { GenreSeed, GenreSeedArray } from "./genre.seed";
export { genreSeedItemSchema, genreSeedSchema };

export type { UserSeed, UserSeedItem } from "./user.seed";
export { userSeedItemSchema, userSeedSchema };

export type { ComicSeed, ComicSeedArray, ComicSeedItem } from "./comic.seed";
export { comicSeedItemSchema, comicSeedSchema };

export type { ChapterSeed, ChapterSeedArray } from "./chapter.seed";
export { chapterSeedItemSchema, chapterSeedSchema };

export type { TypeSeed, TypeSeedArray } from "./type.seed";
export { typeSeedItemSchema, typeSeedSchema };

export type { RoleSeed, RoleSeedItem } from "./role.seed";
export { roleSeedItemSchema, roleSeedSchema };

export type { PermissionSeed, PermissionSeedItem } from "./permission.seed";
export { permissionSeedItemSchema, permissionSeedSchema };

export type { UserRoleSeed, UserRoleSeedItem } from "./user-role.seed";
export { userRoleSeedItemSchema, userRoleSeedSchema };

export type { UserPreferenceSeed, UserPreferenceSeedItem } from "./user-preference.seed";
export { userPreferenceSeedItemSchema, userPreferenceSeedSchema };

export type { ReaderSettingsSeed, ReaderSettingsSeedItem } from "./reader-settings.seed";
export { readerSettingsSeedItemSchema, readerSettingsSeedSchema };

export type { ReadingGoalSeed, ReadingGoalSeedItem } from "./reading-goal.seed";
export { readingGoalSeedItemSchema, readingGoalSeedSchema };

export type { RatingSeed, RatingSeedItem } from "./rating.seed";
export { ratingSeedItemSchema, ratingSeedSchema };

export type { CommentSeed, CommentSeedItem } from "./comment.seed";
export { commentSeedItemSchema, commentSeedSchema };

export type { NotificationSeed, NotificationSeedItem } from "./notification.seed";
export { notificationSeedItemSchema, notificationSeedSchema };

export type { ReadingHistorySeed, ReadingHistorySeedItem } from "./reading-history.seed";
export { readingHistorySeedItemSchema, readingHistorySeedSchema };

export type { FollowSeed, FollowSeedItem } from "./follow.seed";
export { followSeedItemSchema, followSeedSchema };

export type { ShareSeed, ShareSeedItem } from "./share.seed";
export { shareSeedItemSchema, shareSeedSchema };

export const seedSchemas = {
  user: userSeedSchema,
  comic: comicSeedSchema,
  chapter: chapterSeedSchema,
  author: authorSeedSchema,
  artist: artistSeedSchema,
  genre: genreSeedSchema,
  type: typeSeedSchema,
  role: roleSeedSchema,
  permission: permissionSeedSchema,
  "user-role": userRoleSeedSchema,
  "user-preference": userPreferenceSeedSchema,
  "reader-settings": readerSettingsSeedSchema,
  "reading-goal": readingGoalSeedSchema,
  bookmark: bookmarkSeedSchema,
  rating: ratingSeedSchema,
  comment: commentSeedSchema,
  notification: notificationSeedSchema,
  "reading-history": readingHistorySeedSchema,
  follow: followSeedSchema,
  share: shareSeedSchema,
} as const;

export type SeedSchemaMap = {
  bookmark: typeof bookmarkSeedSchema;
  chapter: typeof chapterSeedSchema;
  comic: typeof comicSeedSchema;
  comment: typeof commentSeedSchema;
  follow: typeof followSeedSchema;
  notification: typeof notificationSeedSchema;
  permission: typeof permissionSeedSchema;
  rating: typeof ratingSeedSchema;
  "reader-settings": typeof readerSettingsSeedSchema;
  "reading-goal": typeof readingGoalSeedSchema;
  "reading-history": typeof readingHistorySeedSchema;
  role: typeof roleSeedSchema;
  share: typeof shareSeedSchema;
  type: typeof typeSeedSchema;
  user: typeof userSeedSchema;
  "user-preference": typeof userPreferenceSeedSchema;
  "user-role": typeof userRoleSeedSchema;
};
