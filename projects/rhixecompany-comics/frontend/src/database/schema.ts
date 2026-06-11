import { sql, type SQL } from "drizzle-orm";
import {
  boolean,
  decimal,
  index,
  integer,
  jsonb,
  pgEnum,
  pgTable,
  primaryKey,
  serial,
  text,
  timestamp,
  unique,
  varchar,
} from "drizzle-orm/pg-core";

import type { AdapterAccountType } from "next-auth/adapters";

// ═══════════════════════════════════════════════════
// CUSTOM SQL TYPES FOR FULL-TEXT SEARCH
// ═══════════════════════════════════════════════════

// tsvector type for PostgreSQL full-text search
export const tsvector: (name: string) => SQL<string> = (name: string) => {
  return sql<string>`${sql.raw(name)} tsvector`;
};

// ═══════════════════════════════════════════════════
// ENUMS
// ═══════════════════════════════════════════════════

export const userRole = pgEnum("user_role", ["user", "admin", "moderator"]);
export const comicStatus = pgEnum("comic_status", [
  "Ongoing",
  "Hiatus",
  "Completed",
  "Dropped",
  "Season End",
  "Coming Soon",
]);

// ═══════════════════════════════════════════════════
// AUTHENTICATION TABLES
// ═══════════════════════════════════════════════════

export const user = pgTable(
  "user",
  {
    id: text("id")
      .primaryKey()
      .notNull()
      .$defaultFn(() => crypto.randomUUID()),
    name: text("name"),
    email: text("email").unique().notNull(),
    emailVerified: timestamp("emailVerified", { mode: "date" }),
    image: text("image"),
    password: text("password"),
    role: userRole("role").default("user").notNull(),
    status: boolean("status").notNull().default(false),
    settings: jsonb("settings").$type<{
      emailNotifications?: boolean;
      profileVisibility?: "private" | "public";
      readingHistoryVisibility?: boolean;
    }>(),
    deletedAt: timestamp("deletedAt", { mode: "date" }),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [index("userEmailIdx").on(table.email), index("userRoleIdx").on(table.role)]
);

export const account = pgTable(
  "account",
  {
    userId: text("userId")
      .notNull()
      .references(() => user.id, { onDelete: "cascade" }),
    type: text("type").$type<AdapterAccountType>().notNull(),
    provider: text("provider").notNull(),
    providerAccountId: text("providerAccountId").notNull(),
    refresh_token: text("refresh_token"),
    access_token: text("access_token"),
    expires_at: integer("expires_at"),
    token_type: text("token_type"),
    scope: text("scope"),
    id_token: text("id_token"),
    session_state: text("session_state"),
  },
  (table) => ({
    pk: primaryKey({ columns: [table.provider, table.providerAccountId] }),
  })
);

export const session = pgTable("session", {
  sessionToken: text("sessionToken").primaryKey().notNull(),
  userId: text("userId")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" }),
  expires: timestamp("expires", { mode: "date" }).notNull(),
});

export const verificationToken = pgTable(
  "verificationToken",
  {
    identifier: text("identifier").notNull(),
    token: text("token").notNull(),
    expires: timestamp("expires", { mode: "date" }).notNull(),
  },
  (table) => ({
    pk: primaryKey({ columns: [table.identifier, table.token] }),
  })
);

export const authenticator = pgTable(
  "authenticator",
  {
    credentialID: text("credentialID").notNull().unique(),
    userId: text("userId")
      .notNull()
      .references(() => user.id, { onDelete: "cascade" }),
    providerAccountId: text("providerAccountId").notNull(),
    credentialPublicKey: text("credentialPublicKey").notNull(),
    counter: integer("counter").notNull(),
    credentialDeviceType: text("credentialDeviceType").notNull(),
    credentialBackedUp: boolean("credentialBackedUp").notNull(),
    transports: text("transports"),
  },
  (table) => ({
    pk: primaryKey({ columns: [table.userId, table.credentialID] }),
  })
);

export const passwordResetToken = pgTable("passwordResetToken", {
  id: text("id")
    .primaryKey()
    .$defaultFn(() => crypto.randomUUID()),
  email: text("email").notNull(),
  token: text("token").notNull().unique(),
  expires: timestamp("expires", { mode: "date" }).notNull(),
});

// ═══════════════════════════════════════════════════
// COMIC CONTENT TABLES (ORDERED FOR REFERENCES)
// ═══════════════════════════════════════════════════

export const type = pgTable("type", {
  id: serial("id").primaryKey(),
  name: text("name").notNull().unique(),
  description: text("description"),
  isActive: boolean("is_active").default(true).notNull(),
  createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
});

export const author = pgTable("author", {
  id: serial("id").primaryKey(),
  name: text("name").notNull().unique(),
  bio: text("bio"),
  image: text("image"),
  isActive: boolean("is_active").default(true).notNull(),
  createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  searchVector: text("searchVector"),
});

export const artist = pgTable("artist", {
  id: serial("id").primaryKey(),
  name: text("name").notNull().unique(),
  bio: text("bio"),
  image: text("image"),
  isActive: boolean("is_active").default(true).notNull(),
  createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  searchVector: text("searchVector"),
});

export const genre = pgTable("genre", {
  id: serial("id").primaryKey(),
  name: text("name").notNull().unique(),
  slug: text("slug").notNull().unique(),
  description: text("description"),
  isActive: boolean("is_active").default(true).notNull(),
  createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
});

export const comic = pgTable(
  "comic",
  {
    id: serial("id").primaryKey(),
    title: text("title").unique().notNull(),
    slug: text("slug").unique().notNull(),
    description: text("description").notNull(),
    coverImage: text("coverImage").notNull(),
    status: comicStatus("status").default("Ongoing").notNull(),
    publicationDate: timestamp("publicationDate", { mode: "date" }).notNull(),
    rating: decimal("rating", { precision: 10, scale: 1 }).default("0"),
    views: integer("views").default(0).notNull(),
    url: text("url").unique(), // External source URL
    serialization: text("serialization"), // Serialization info
    authorId: integer("authorId").references(() => author.id),
    artistId: integer("artistId").references(() => artist.id),
    typeId: integer("typeId").references(() => type.id),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
    searchVector: text("searchVector"),
  },
  (table) => [
    index("comicSlugIdx").on(table.slug),
    index("comicTitleIdx").on(table.title),
    index("comicStatusIdx").on(table.status),
    index("comicRatingIdx").on(table.rating),
    index("comicViewsIdx").on(table.views),
    index("comicAuthorIdx").on(table.authorId),
    index("comicArtistIdx").on(table.artistId),
    index("comicTypeIdx").on(table.typeId),
    index("comicCreatedAtIdx").on(table.createdAt),
  ]
);

export const chapter = pgTable(
  "chapter",
  {
    id: serial("id").primaryKey(),
    slug: text("slug").unique().notNull(),
    title: text("title").notNull(),
    chapterNumber: integer("chapterNumber").notNull(),
    releaseDate: timestamp("releaseDate", { mode: "date" }).notNull(),
    comicId: integer("comicId")
      .references(() => comic.id, { onDelete: "cascade" })
      .notNull(),
    views: integer("views").default(0).notNull(),
    url: text("url").unique(), // External source URL
    content: text("content"), // Chapter content/description
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("chapterSlugIdx").on(table.slug),
    index("chapterComicIdIdx").on(table.comicId),
    index("chapterNumberIdx").on(table.chapterNumber),
    index("chapterReleaseDateIdx").on(table.releaseDate),
    index("chapterComicChapterIdx").on(table.comicId, table.chapterNumber),
    // Unique constraint for upsert operations
    unique("chapter_comic_number_unique").on(table.comicId, table.chapterNumber),
  ]
);

export const comicImage = pgTable("comicImage", {
  id: serial("id").primaryKey(),
  comicId: integer("comicId")
    .references(() => comic.id, { onDelete: "cascade" })
    .notNull(),
  imageUrl: text("imageUrl").unique().notNull(),
  imageOrder: integer("imageOrder").notNull(),
  createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
});

export const chapterImage = pgTable(
  "chapterImage",
  {
    id: serial("id").primaryKey(),
    chapterId: integer("chapterId")
      .references(() => chapter.id, { onDelete: "cascade" })
      .notNull(),
    imageUrl: text("imageUrl").notNull(),
    pageNumber: integer("pageNumber").notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("chapterImageChapterIdIdx").on(table.chapterId),
    index("chapterImagePageNumberIdx").on(table.pageNumber),
    unique("chapterImage_chapterId_pageNumber_unique").on(table.chapterId, table.pageNumber),
  ]
);

export const comicToGenre = pgTable(
  "comicToGenre",
  {
    comicId: integer("comicId")
      .references(() => comic.id, { onDelete: "cascade" })
      .notNull(),
    genreId: integer("genreId")
      .references(() => genre.id, { onDelete: "cascade" })
      .notNull(),
  },
  (table) => ({
    pk: primaryKey({ columns: [table.comicId, table.genreId] }),
  })
);

// ═══════════════════════════════════════════════════
// USER INTERACTION TABLES
// ═══════════════════════════════════════════════════

export const bookmark = pgTable(
  "bookmark",
  {
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    comicId: integer("comicId")
      .references(() => comic.id, { onDelete: "cascade" })
      .notNull(),
    lastReadChapterId: integer("lastReadChapterId").references(() => chapter.id),
    status: text("status").default("Reading").notNull(),
    notes: text("notes"),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    primaryKey({ columns: [table.userId, table.comicId] }),
    index("bookmarkUserIdIdx").on(table.userId),
    index("bookmarkComicIdIdx").on(table.comicId),
  ]
);

export const comment = pgTable(
  "comment",
  {
    id: serial("id").primaryKey(),
    content: text("content").notNull(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    chapterId: integer("chapterId")
      .references(() => chapter.id, { onDelete: "cascade" })
      .notNull(),
    parentId: integer("parentId"),
    deletedAt: timestamp("deletedAt", { mode: "date" }),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("commentUserIdIdx").on(table.userId),
    index("commentChapterIdIdx").on(table.chapterId),
    index("commentParentIdIdx").on(table.parentId),
    index("commentCreatedAtIdx").on(table.createdAt),
  ]
);

export const readingProgress = pgTable(
  "readingProgress",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    comicId: integer("comicId")
      .references(() => comic.id, { onDelete: "cascade" })
      .notNull(),
    chapterId: integer("chapterId")
      .references(() => chapter.id, { onDelete: "cascade" })
      .notNull(),
    pageNumber: integer("pageNumber").default(0).notNull(),
    scrollPosition: integer("scrollPosition").default(0).notNull(),
    currentImageIndex: integer("currentImageIndex").default(0).notNull(),
    scrollPercentage: integer("scrollPercentage").default(0).notNull(),
    totalPages: integer("totalPages").default(0).notNull(),
    progressPercent: integer("progressPercent").default(0).notNull(),
    completedAt: timestamp("completedAt", { mode: "date" }),
    lastReadAt: timestamp("lastReadAt", { mode: "date" }).defaultNow().notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("readingProgressUserIdIdx").on(table.userId),
    index("readingProgressComicIdIdx").on(table.comicId),
    index("readingProgressChapterIdIdx").on(table.chapterId),
    index("readingProgressLastReadIdx").on(table.lastReadAt),
    index("readingProgressUserComicIdx").on(table.userId, table.comicId),
  ]
);

export const readerSettings = pgTable(
  "readerSettings",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .unique()
      .notNull(),
    backgroundMode: varchar("backgroundMode", { length: 16 }).default("white").notNull(),
    readingMode: varchar("readingMode", { length: 16 }).default("vertical").notNull(),
    defaultQuality: varchar("defaultQuality", { length: 16 }).default("medium").notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [index("readerSettingsUserIdIdx").on(table.userId)]
);

export const rating = pgTable(
  "rating",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    comicId: integer("comicId")
      .references(() => comic.id, { onDelete: "cascade" })
      .notNull(),
    rating: integer("rating").notNull(), // 1 to 5 stars
    review: text("review"),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    unique("userComicRatingUnique").on(table.userId, table.comicId),
    index("ratingUserIdIdx").on(table.userId),
    index("ratingComicIdIdx").on(table.comicId),
    index("ratingValueIdx").on(table.rating),
    index("ratingCreatedAtIdx").on(table.createdAt),
  ]
);

export const notification = pgTable(
  "notification",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    type: text("type").notNull(), // 'new_chapter', 'comment_reply', 'system'
    title: text("title").notNull(),
    message: text("message").notNull(),
    link: text("link"),
    read: boolean("read").default(false).notNull(),
    comicId: integer("comicId").references(() => comic.id, { onDelete: "cascade" }),
    chapterId: integer("chapterId").references(() => chapter.id, { onDelete: "cascade" }),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("notificationUserIdIdx").on(table.userId),
    index("notificationReadIdx").on(table.read),
    index("notificationTypeIdx").on(table.type),
    index("notificationCreatedAtIdx").on(table.createdAt),
    index("notificationUserReadIdx").on(table.userId, table.read),
  ]
);

// ═══════════════════════════════════════════════════
// RBAC TABLES (ROLE-BASED ACCESS CONTROL)
// ═══════════════════════════════════════════════════

export const resourceEnum = pgEnum("resource_type", [
  "comic",
  "chapter",
  "user",
  "comment",
  "rating",
  "bookmark",
  "notification",
  "author",
  "artist",
  "genre",
  "type",
  "system",
]);

export const actionEnum = pgEnum("action_type", ["create", "read", "update", "delete", "manage"]);

export const role = pgTable(
  "role",
  {
    id: serial("id").primaryKey(),
    name: text("name").notNull().unique(),
    description: text("description"),
    isSystem: boolean("isSystem").default(false).notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [index("roleNameIdx").on(table.name), index("roleIsSystemIdx").on(table.isSystem)]
);

export const permission = pgTable(
  "permission",
  {
    id: serial("id").primaryKey(),
    name: text("name").notNull().unique(),
    description: text("description"),
    resource: resourceEnum("resource").notNull(),
    action: actionEnum("action").notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("permissionNameIdx").on(table.name),
    index("permissionResourceIdx").on(table.resource),
    index("permissionActionIdx").on(table.action),
    unique("permissionResourceActionUnique").on(table.resource, table.action),
  ]
);

export const rolePermission = pgTable(
  "rolePermission",
  {
    roleId: integer("roleId")
      .references(() => role.id, { onDelete: "cascade" })
      .notNull(),
    permissionId: integer("permissionId")
      .references(() => permission.id, { onDelete: "cascade" })
      .notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    primaryKey({ columns: [table.roleId, table.permissionId] }),
    index("rolePermissionRoleIdIdx").on(table.roleId),
    index("rolePermissionPermissionIdIdx").on(table.permissionId),
  ]
);

export const userRole2 = pgTable(
  "userRole",
  {
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    roleId: integer("roleId")
      .references(() => role.id, { onDelete: "cascade" })
      .notNull(),
    assignedAt: timestamp("assignedAt", { mode: "date" }).defaultNow().notNull(),
    assignedBy: text("assignedBy").references(() => user.id),
  },
  (table) => [
    primaryKey({ columns: [table.userId, table.roleId] }),
    index("userRoleUserIdIdx").on(table.userId),
    index("userRoleRoleIdIdx").on(table.roleId),
  ]
);

// ═══════════════════════════════════════════════════
// AUDIT LOG TABLE
// ═══════════════════════════════════════════════════

export const auditLog = pgTable(
  "auditLog",
  {
    id: text("id")
      .primaryKey()
      .$defaultFn(() => crypto.randomUUID()),
    userId: text("userId").references(() => user.id, { onDelete: "set null" }),
    action: text("action").notNull(), // login, logout, create, update, delete, view, etc.
    resource: resourceEnum("resource").notNull(),
    resourceId: text("resourceId"),
    details: text("details"), // JSON string for flexibility
    oldValues: text("oldValues"), // JSON string of previous values
    newValues: text("newValues"), // JSON string of new values
    ipAddress: text("ipAddress"),
    userAgent: text("userAgent"),
    sessionId: text("sessionId"),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("auditLogUserIdIdx").on(table.userId),
    index("auditLogActionIdx").on(table.action),
    index("auditLogResourceIdx").on(table.resource),
    index("auditLogResourceIdIdx").on(table.resourceId),
    index("auditLogCreatedAtIdx").on(table.createdAt),
    index("auditLogUserActionIdx").on(table.userId, table.action),
    index("auditLogResourceActionIdx").on(table.resource, table.action),
  ]
);

/**
 * User Preferences Table
 * Stores user-specific preferences and settings
 */
export const userPreference = pgTable(
  "userPreference",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .unique()
      .notNull(),
    // Theme preferences
    theme: text("theme", { enum: ["light", "dark", "system"] })
      .default("system")
      .notNull(),
    // Reading preferences
    defaultLayout: text("defaultLayout", {
      enum: ["webtoon", "comic", "book"],
    })
      .default("webtoon")
      .notNull(),
    pageNavigationStyle: text("pageNavigationStyle", {
      enum: ["buttons", "swipe", "click"],
    })
      .default("buttons")
      .notNull(),
    // Display preferences
    fontSize: integer("fontSize").default(16).notNull(), // pixels
    lineHeight: text("lineHeight", { enum: ["compact", "normal", "relaxed"] })
      .default("normal")
      .notNull(),
    // Notification preferences
    notifyNewChapters: boolean("notifyNewChapters").default(true).notNull(),
    notifyComments: boolean("notifyComments").default(true).notNull(),
    notifyBookmarkUpdates: boolean("notifyBookmarkUpdates").default(false).notNull(),
    // Privacy preferences
    profilePublic: boolean("profilePublic").default(false).notNull(),
    showReadingHistory: boolean("showReadingHistory").default(false).notNull(),
    // Timestamps
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [index("userPreferenceUserIdIdx").on(table.userId)]
);

// ═══════════════════════════════════════════════════
// READING ANALYTICS TABLES
// Track user reading history and goals
// ═══════════════════════════════════════════════════

/**
 * Reading History Table
 * Tracks when users read chapters and time spent
 * Enables analytics dashboard and reading statistics
 */
export const readingHistory = pgTable(
  "readingHistory",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    comicId: integer("comicId")
      .references(() => comic.id, { onDelete: "cascade" })
      .notNull(),
    chapterId: integer("chapterId")
      .references(() => chapter.id, { onDelete: "cascade" })
      .notNull(),
    startedAt: timestamp("startedAt", { mode: "date" }).defaultNow().notNull(),
    completedAt: timestamp("completedAt", { mode: "date" }),
    timeSpentSeconds: integer("timeSpentSeconds").default(0).notNull(),
    progress: decimal("progress", { precision: 5, scale: 2 }).default("0").notNull(), // 0-100%
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("readingHistoryUserIdIdx").on(table.userId),
    index("readingHistoryComicIdIdx").on(table.comicId),
    index("readingHistoryChapterIdIdx").on(table.chapterId),
    index("readingHistoryStartedAtIdx").on(table.startedAt),
    index("readingHistoryUserComicIdx").on(table.userId, table.comicId),
    index("readingHistoryUserStartedIdx").on(table.userId, table.startedAt),
  ]
);

/**
 * Reading Goals Table
 * User goals for reading streaks and completion targets
 */
export const readingGoal = pgTable(
  "readingGoal",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    type: text("type", {
      enum: ["daily_chapters", "weekly_comics", "monthly_minutes"],
    }).notNull(),
    target: integer("target").notNull(), // target count
    currentCount: integer("currentCount").default(0).notNull(), // current progress
    startDate: timestamp("startDate", { mode: "date" }).notNull(),
    endDate: timestamp("endDate", { mode: "date" }).notNull(),
    isActive: boolean("isActive").default(true).notNull(),
    completedAt: timestamp("completedAt", { mode: "date" }),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("readingGoalUserIdIdx").on(table.userId),
    index("readingGoalTypeIdx").on(table.type),
    index("readingGoalIsActiveIdx").on(table.isActive),
    index("readingGoalStartDateIdx").on(table.startDate),
    index("readingGoalEndDateIdx").on(table.endDate),
    index("readingGoalUserTypeIdx").on(table.userId, table.type),
  ]
);

// ═══════════════════════════════════════════════════
// SEARCH INDEX TABLE
// Full-text search optimization table for PostgreSQL
// ═══════════════════════════════════════════════════

/**
 * Search Index Table
 * Denormalized table for efficient full-text search
 * Maintains searchable comic content with PostgreSQL tsvector
 */
export const searchIndex = pgTable(
  "searchIndex",
  {
    id: serial("id").primaryKey(),

    // Reference to comic
    comicId: integer("comicId")
      .unique()
      .notNull()
      .references(() => comic.id, { onDelete: "cascade" }),

    // Denormalized searchable fields
    title: text("title").notNull(),
    synopsis: text("synopsis"),
    authors: text("authors"), // Space-separated author names
    artists: text("artists"), // Space-separated artist names
    genres: text("genres"), // Space-separated genre names

    // Full-text search vector stored as text
    // Actual type: tsvector (created via trigger)
    searchVector: text("searchVector").notNull(),

    // Metadata for relevance boosts
    popularity: integer("popularity").notNull().default(0), // View count
    rating: decimal("rating", { precision: 10, scale: 1 }).notNull().default("0"),

    // Timestamps
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    // Index for comic lookups
    index("searchIndexComicIdIdx").on(table.comicId),

    // Index for popularity-based ranking
    index("searchIndexPopularityIdx").on(table.popularity),

    // Index for rating-based filtering
    index("searchIndexRatingIdx").on(table.rating),
  ]
);

// ═════════════════════════════════════════════════════════════════════════════
// SOCIAL TABLES (PHASE 6+)
// Follow system and sharing functionality
// ═════════════════════════════════════════════════════════════════════════════

/**
 * Follow Table
 * Users can follow other users - composite primary key (followerId, followingId)
 */
export const follow = pgTable(
  "follow",
  {
    followerId: text("followerId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    followingId: text("followingId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    primaryKey({ columns: [table.followerId, table.followingId] }),
    index("followFollowerIdx").on(table.followerId),
    index("followFollowingIdx").on(table.followingId),
  ]
);

/**
 * Share Table
 * Users can share comics or chapters to their activity feed
 */
export const share = pgTable(
  "share",
  {
    id: serial("id").primaryKey(),
    userId: text("userId")
      .references(() => user.id, { onDelete: "cascade" })
      .notNull(),
    resourceType: resourceEnum("resource_type").notNull(),
    resourceId: integer("resourceId").notNull(),
    message: text("message"),
    createdAt: timestamp("createdAt", { mode: "date" }).defaultNow().notNull(),
  },
  (table) => [
    index("shareUserIdx").on(table.userId),
    index("shareResourceIdx").on(table.resourceType, table.resourceId),
    index("shareCreatedAtIdx").on(table.createdAt),
  ]
);

// ═══════════════════════════════════════════════════
// RELATIONS (Required for .with() eager loading)
// ═══════════════════════════════════════════════════

import { relations } from "drizzle-orm";

export const userRelations = relations(user, ({ many }) => ({
  accounts: many(account),
  sessions: many(session),
  bookmarks: many(bookmark),
  comments: many(comment),
  ratings: many(rating),
  readingProgress: many(readingProgress),
  notifications: many(notification),
  userRoles: many(userRole2),
  auditLogs: many(auditLog),
  followers: many(follow, { relationName: "following" }),
  following: many(follow, { relationName: "follower" }),
}));

export const comicRelations = relations(comic, ({ one, many }) => ({
  author: one(author, { fields: [comic.authorId], references: [author.id] }),
  artist: one(artist, { fields: [comic.artistId], references: [artist.id] }),
  comicType: one(type, { fields: [comic.typeId], references: [type.id] }),
  chapters: many(chapter),
  comicImages: many(comicImage),
  bookmarks: many(bookmark),
  ratings: many(rating),
  readingProgress: many(readingProgress),
  readingHistory: many(readingHistory),
  genres: many(comicToGenre),
  searchIndex: one(searchIndex),
}));

export const chapterRelations = relations(chapter, ({ one, many }) => ({
  comic: one(comic, { fields: [chapter.comicId], references: [comic.id] }),
  images: many(chapterImage),
  comments: many(comment),
  readingProgress: many(readingProgress),
  readingHistory: many(readingHistory),
}));

export const authorRelations = relations(author, ({ many }) => ({
  comics: many(comic),
}));

export const artistRelations = relations(artist, ({ many }) => ({
  comics: many(comic),
}));

export const typeRelations = relations(type, ({ many }) => ({
  comics: many(comic),
}));

export const genreRelations = relations(genre, ({ many }) => ({
  comics: many(comicToGenre),
}));

export const comicToGenreRelations = relations(comicToGenre, ({ one }) => ({
  comic: one(comic, { fields: [comicToGenre.comicId], references: [comic.id] }),
  genre: one(genre, { fields: [comicToGenre.genreId], references: [genre.id] }),
}));

export const roleRelations = relations(role, ({ many }) => ({
  rolePermissions: many(rolePermission),
  userRoles: many(userRole2),
}));

export const permissionRelations = relations(permission, ({ many }) => ({
  rolePermissions: many(rolePermission),
}));

export const rolePermissionRelations = relations(rolePermission, ({ one }) => ({
  role: one(role, { fields: [rolePermission.roleId], references: [role.id] }),
  permission: one(permission, { fields: [rolePermission.permissionId], references: [permission.id] }),
}));

export const userRole2Relations = relations(userRole2, ({ one }) => ({
  user: one(user, { fields: [userRole2.userId], references: [user.id] }),
  role: one(role, { fields: [userRole2.roleId], references: [role.id] }),
}));

export const auditLogRelations = relations(auditLog, ({ one }) => ({
  user: one(user, { fields: [auditLog.userId], references: [user.id] }),
}));

export const followRelations = relations(follow, ({ one }) => ({
  follower: one(user, { fields: [follow.followerId], references: [user.id], relationName: "follower" }),
  following: one(user, { fields: [follow.followingId], references: [user.id], relationName: "following" }),
}));

export const commentRelations = relations(comment, ({ one, many }) => ({
  user: one(user, { fields: [comment.userId], references: [user.id] }),
  chapter: one(chapter, { fields: [comment.chapterId], references: [chapter.id] }),
  parent: one(comment, { fields: [comment.parentId], references: [comment.id] }),
  replies: many(comment),
}));

export const bookmarkRelations = relations(bookmark, ({ one }) => ({
  user: one(user, { fields: [bookmark.userId], references: [user.id] }),
  comic: one(comic, { fields: [bookmark.comicId], references: [comic.id] }),
  lastReadChapter: one(chapter, { fields: [bookmark.lastReadChapterId], references: [chapter.id] }),
}));

export const ratingRelations = relations(rating, ({ one }) => ({
  user: one(user, { fields: [rating.userId], references: [user.id] }),
  comic: one(comic, { fields: [rating.comicId], references: [comic.id] }),
}));

export const readingProgressRelations = relations(readingProgress, ({ one }) => ({
  user: one(user, { fields: [readingProgress.userId], references: [user.id] }),
  comic: one(comic, { fields: [readingProgress.comicId], references: [comic.id] }),
  chapter: one(chapter, { fields: [readingProgress.chapterId], references: [chapter.id] }),
}));

export const readingHistoryRelations = relations(readingHistory, ({ one }) => ({
  user: one(user, { fields: [readingHistory.userId], references: [user.id] }),
  comic: one(comic, { fields: [readingHistory.comicId], references: [comic.id] }),
  chapter: one(chapter, { fields: [readingHistory.chapterId], references: [chapter.id] }),
}));

export const notificationRelations = relations(notification, ({ one }) => ({
  user: one(user, { fields: [notification.userId], references: [user.id] }),
  comic: one(comic, { fields: [notification.comicId], references: [comic.id] }),
  chapter: one(chapter, { fields: [notification.chapterId], references: [chapter.id] }),
}));

export const chapterImageRelations = relations(chapterImage, ({ one }) => ({
  chapter: one(chapter, { fields: [chapterImage.chapterId], references: [chapter.id] }),
}));

export const comicImageRelations = relations(comicImage, ({ one }) => ({
  comic: one(comic, { fields: [comicImage.comicId], references: [comic.id] }),
}));

export const accountRelations = relations(account, ({ one }) => ({
  user: one(user, { fields: [account.userId], references: [user.id] }),
}));

export const sessionRelations = relations(session, ({ one }) => ({
  user: one(user, { fields: [session.userId], references: [user.id] }),
}));

export const authenticatorRelations = relations(authenticator, ({ one }) => ({
  user: one(user, { fields: [authenticator.userId], references: [user.id] }),
}));

export const searchIndexRelations = relations(searchIndex, ({ one }) => ({
  comic: one(comic, { fields: [searchIndex.comicId], references: [comic.id] }),
}));

export const shareRelations = relations(share, ({ one }) => ({
  user: one(user, { fields: [share.userId], references: [user.id] }),
}));
