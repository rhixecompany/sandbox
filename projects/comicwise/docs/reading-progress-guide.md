# Reading Progress Tracking Implementation

**Purpose:** Complete guide to implementing user reading progress tracking for ComicWise

**Framework:** Next.js 16 | **Database:** PostgreSQL | **Real-time:** Optimistic updates

**Last Updated:** March 1, 2026

---

## Table of Contents

1. [Overview](#overview)
2. [Database Schema](#database-schema)
3. [Data Access Layer](#data-access-layer)
4. [Server Actions](#server-actions)
5. [Reading Progress Components](#reading-progress-components)
6. [Chapter Reader Integration](#chapter-reader-integration)
7. [Progress Synchronization](#progress-synchronization)
8. [Testing](#testing)

---

## Overview

Reading progress tracking enables:

- ✅ **Track Chapter Progress** - Current page/position within chapter
- ✅ **Resume Reading** - Remember where user left off
- ✅ **Progress Visualization** - Show reading % and position
- ✅ **Update History** - Log when chapters were read
- ✅ **Device Sync** - Progress synced across devices
- ✅ **Continue Reading** - Quick link to last read chapter
- ✅ **Reading Stats** - Total chapters read, reading streaks

---

## Database Schema

### ReadingProgress Table

**Existing in `src/database/schema.ts`:**

```typescript
export const readingProgress = pgTable(
  "readingProgress",
  {
    // Composite Primary Key: User + Comic
    userId: text("userId")
      .notNull()
      .references(() => user.id, { onDelete: "cascade" }),

    comicId: integer("comicId")
      .notNull()
      .references(() => comic.id, { onDelete: "cascade" }),

    // Current Position
    currentChapterId: integer("currentChapterId").references(
      () => chapter.id,
      { onDelete: "set null" }
    ),

    currentPageNumber: integer("currentPageNumber").default(0),
    currentPosition: decimal("currentPosition", {
      precision: 5,
      scale: 2
    }).default("0.00"),

    // Statistics
    totalPagesRead: integer("totalPagesRead").default(0),
    totalChaptersRead: integer("totalChaptersRead").default(0),
    progressPercent: decimal("progressPercent", {
      precision: 5,
      scale: 2
    }).default("0.00"),

    // Timeline
    lastReadAt: timestamp("lastReadAt"),
    startedAt: timestamp("startedAt").defaultNow(),
    completedAt: timestamp("completedAt"),

    // Status
    status: text("status").default("Reading"), // Reading, Paused, Completed, Dropped

    // Metadata
    readingSpeed: text("readingSpeed"), // Slow, Normal, Fast (calculated)
    deviceLastUsed: text("deviceLastUsed"), // Mobile, Desktop, Tablet
    notesCount: integer("notesCount").default(0),

    // Timestamps
    createdAt: timestamp("createdAt").defaultNow().notNull(),
    updatedAt: timestamp("updatedAt").defaultNow().notNull()
  },
  table => [
    // Primary key
    primaryKey({
      columns: [table.userId, table.comicId],
      name: "readingProgress_pk"
    }),

    // Indexes for common queries
    index("readingProgress_userId_idx").on(table.userId),
    index("readingProgress_comicId_idx").on(table.comicId),
    index("readingProgress_updatedAt_idx").on(table.updatedAt),
    index("readingProgress_lastReadAt_idx").on(table.lastReadAt),

    // Composite index for "continue reading"
    index("readingProgress_user_lastRead_idx").on(
      table.userId,
      table.lastReadAt
    )
  ]
);
```

### Related Tables

**Chapter Table** (for chapter info):

```typescript
export const chapter = pgTable("chapter", {
  id: serial("id").primaryKey(),
  comicId: integer("comicId")
    .notNull()
    .references(() => comic.id, { onDelete: "cascade" }),
  chapterNumber: integer("chapterNumber").notNull(),
  title: text("title").notNull(),
  releaseDate: timestamp("releaseDate").notNull(),
  pageCount: integer("pageCount").notNull() // Total pages in chapter
  // ... other fields
});
```

---

## Data Access Layer

**File:** `src/dal/reading-progress-dal.ts`

```typescript
import { BaseDal } from "./base-dal";
import { db } from "@/database/db";
import { readingProgress, chapter, comic } from "@/database/schema";
import { eq, and, desc } from "drizzle-orm";

export interface UpdateProgressInput {
  userId: string;
  comicId: number;
  currentChapterId?: number;
  currentPageNumber?: number;
  currentPosition?: string;
  status?: string;
}

export class ReadingProgressDal extends BaseDal<ReadingProgress> {
  /**
   * Get reading progress for a user on a specific comic
   */
  async getProgress(
    userId: string,
    comicId: number
  ): Promise<ReadingProgress | null> {
    const [result] = await db
      .select()
      .from(readingProgress)
      .where(
        and(
          eq(readingProgress.userId, userId),
          eq(readingProgress.comicId, comicId)
        )
      );

    return result ?? null;
  }

  /**
   * Get user's "continue reading" list - last read chapters for multiple comics
   * Used for dashboard quick links
   */
  async getContinueReadingList(userId: string, limit: number = 10) {
    return db
      .select({
        comicId: readingProgress.comicId,
        comicTitle: comic.title,
        comicSlug: comic.slug,
        currentChapterId: readingProgress.currentChapterId,
        currentPageNumber: readingProgress.currentPageNumber,
        progressPercent: readingProgress.progressPercent,
        lastReadAt: readingProgress.lastReadAt,
        chapterNumber: chapter.chapterNumber,
        chapterTitle: chapter.title
      })
      .from(readingProgress)
      .innerJoin(comic, eq(readingProgress.comicId, comic.id))
      .leftJoin(
        chapter,
        eq(readingProgress.currentChapterId, chapter.id)
      )
      .where(eq(readingProgress.userId, userId))
      .orderBy(desc(readingProgress.lastReadAt))
      .limit(limit);
  }

  /**
   * Update reading progress (idempotent upsert)
   * Called frequently when user reads chapters
   */
  async updateProgress(
    data: UpdateProgressInput
  ): Promise<ReadingProgress> {
    const [result] = await db
      .insert(readingProgress)
      .values({
        userId: data.userId,
        comicId: data.comicId,
        currentChapterId: data.currentChapterId,
        currentPageNumber: data.currentPageNumber ?? 0,
        currentPosition: data.currentPosition ?? "0",
        status: data.status ?? "Reading",
        lastReadAt: new Date(),
        updatedAt: new Date()
      })
      .onConflictDoUpdate({
        target: [readingProgress.userId, readingProgress.comicId],
        set: {
          currentChapterId: data.currentChapterId,
          currentPageNumber: data.currentPageNumber ?? undefined,
          currentPosition: data.currentPosition ?? undefined,
          status: data.status ?? undefined,
          lastReadAt: new Date(),
          updatedAt: new Date()
        }
      })
      .returning();

    return result;
  }

  /**
   * Mark comic as completed
   */
  async markCompleted(
    userId: string,
    comicId: number
  ): Promise<ReadingProgress | null> {
    const [result] = await db
      .update(readingProgress)
      .set({
        status: "Completed",
        completedAt: new Date(),
        progressPercent: "100.00",
        updatedAt: new Date()
      })
      .where(
        and(
          eq(readingProgress.userId, userId),
          eq(readingProgress.comicId, comicId)
        )
      )
      .returning();

    return result ?? null;
  }

  /**
   * Get reading statistics for a user
   */
  async getUserStats(userId: string) {
    const stats = await db
      .select({
        totalComicsReading: count(readingProgress.comicId),
        totalComicsCompleted: count(
          eq(readingProgress.status, "Completed") ? 1 : null
        ),
        totalPagesRead: sum(readingProgress.totalPagesRead),
        averageProgressPercent: avg(readingProgress.progressPercent)
      })
      .from(readingProgress)
      .where(eq(readingProgress.userId, userId));

    return (
      stats[0] ?? {
        totalComicsReading: 0,
        totalComicsCompleted: 0,
        totalPagesRead: 0,
        averageProgressPercent: 0
      }
    );
  }

  // Required by BaseDal (not used for reading progress)
  async list(): Promise<ReadingProgress[]> {
    throw new Error("Use getContinueReadingList() instead");
  }

  async getById(): Promise<ReadingProgress | null> {
    throw new Error("Use getProgress(userId, comicId) instead");
  }

  async create(): Promise<ReadingProgress> {
    throw new Error("Use updateProgress() instead");
  }

  async update(): Promise<ReadingProgress | null> {
    throw new Error("Use updateProgress() instead");
  }
}

export const readingProgressDal = new ReadingProgressDal();
```

---

## Server Actions

**File:** `src/actions/reading-progress.actions.ts`

```typescript
"use server";

import { auth } from "@/auth";
import { readingProgressDal } from "@/dal/reading-progress-dal";
import { revalidatePath } from "next/cache";

type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

/**
 * Update reading progress for a comic
 * Called frequently - optimized for idempotent upserts
 */
export async function updateProgressAction(
  comicId: number,
  chapterId: number,
  pageNumber: number,
  position: string
): Promise<ActionResult<ReadingProgress>> {
  const session = await auth();

  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const progress = await readingProgressDal.updateProgress({
      userId: session.user.id,
      comicId,
      currentChapterId: chapterId,
      currentPageNumber: pageNumber,
      currentPosition: position
    });

    // Revalidate reading dashboard
    revalidatePath("/dashboard/reading");

    return { ok: true, data: progress };
  } catch (error) {
    console.error("[updateProgressAction]", error);
    return { ok: false, error: "Failed to update progress" };
  }
}

/**
 * Get user's continue reading list
 * Used for dashboard and "resume" functionality
 */
export async function getContinueReadingAction(): Promise<
  ActionResult<any[]>
> {
  const session = await auth();

  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const continueReading =
      await readingProgressDal.getContinueReadingList(
        session.user.id,
        10
      );

    return { ok: true, data: continueReading };
  } catch (error) {
    console.error("[getContinueReadingAction]", error);
    return { ok: false, error: "Failed to fetch reading list" };
  }
}

/**
 * Mark comic as completed
 */
export async function markComicCompletedAction(
  comicId: number
): Promise<ActionResult<ReadingProgress>> {
  const session = await auth();

  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const progress = await readingProgressDal.markCompleted(
      session.user.id,
      comicId
    );

    if (!progress) {
      return { ok: false, error: "Progress record not found" };
    }

    revalidatePath("/dashboard/reading");
    revalidatePath(`/comics/${comicId}`);

    return { ok: true, data: progress };
  } catch (error) {
    console.error("[markComicCompletedAction]", error);
    return { ok: false, error: "Failed to mark as completed" };
  }
}

/**
 * Get user's reading statistics
 */
export async function getUserReadingStatsAction(): Promise<
  ActionResult<any>
> {
  const session = await auth();

  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const stats = await readingProgressDal.getUserStats(
      session.user.id
    );
    return { ok: true, data: stats };
  } catch (error) {
    console.error("[getUserReadingStatsAction]", error);
    return { ok: false, error: "Failed to fetch stats" };
  }
}
```

---

## Reading Progress Components

### Progress Bar Component

**File:** `src/components/reading/ProgressBar.tsx`

```typescript
"use client";

import { useEffect, useState } from "react";

interface ProgressBarProps {
  percent: number;
  pageNumber?: number;
  totalPages?: number;
  showLabel?: boolean;
}

export function ProgressBar({
  percent,
  pageNumber,
  totalPages,
  showLabel = true,
}: ProgressBarProps) {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return null; // Avoid hydration mismatch
  }

  const clampedPercent = Math.min(100, Math.max(0, percent));

  return (
    <div className="space-y-2">
      <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
        <div
          className="h-full bg-blue-600 transition-all duration-500"
          style={{ width: `${clampedPercent}%` }}
        />
      </div>

      {showLabel && (
        <div className="flex justify-between items-center text-sm text-gray-600">
          <span>{clampedPercent.toFixed(0)}% read</span>
          {pageNumber && totalPages && (
            <span>
              Page {pageNumber} of {totalPages}
            </span>
          )}
        </div>
      )}
    </div>
  );
}
```

### Continue Reading Card

**File:** `src/components/reading/ContinueReadingCard.tsx`

```typescript
"use client";

import Link from "next/link";
import Image from "next/image";
import { ProgressBar } from "./ProgressBar";

interface ContinueReading {
  comicId: number;
  comicTitle: string;
  comicSlug: string;
  comicCover?: string;
  currentChapterId?: number;
  currentPageNumber?: number;
  progressPercent?: number;
  lastReadAt?: Date;
  chapterNumber?: number;
  chapterTitle?: string;
}

interface ContinueReadingCardProps {
  reading: ContinueReading;
}

export function ContinueReadingCard({ reading }: ContinueReadingCardProps) {
  const progressPercent = Number(reading.progressPercent ?? 0);
  const lastReadDate = reading.lastReadAt
    ? new Date(reading.lastReadAt).toLocaleDateString()
    : "Never";

  return (
    <Link href={`/comics/${reading.comicSlug}`}>
      <div className="flex gap-4 p-4 border rounded-lg hover:shadow-lg transition-shadow cursor-pointer">
        {/* Comic Cover */}
        <div className="w-16 h-24 shrink-0 relative bg-gray-200 rounded">
          {reading.comicCover ? (
            <Image
              src={reading.comicCover}
              alt={reading.comicTitle}
              fill
              className="object-cover rounded"
            />
          ) : (
            <div className="w-full h-full flex items-center justify-center text-gray-400">
              <span className="text-xs">No image</span>
            </div>
          )}
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-gray-900 truncate">
            {reading.comicTitle}
          </h3>

          <p className="text-sm text-gray-600 mt-1">
            Chapter {reading.chapterNumber}: {reading.chapterTitle}
          </p>

          <div className="mt-3">
            <ProgressBar
              percent={progressPercent}
              showLabel={true}
            />
          </div>

          <p className="text-xs text-gray-500 mt-2">
            Last read: {lastReadDate}
          </p>
        </div>
      </div>
    </Link>
  );
}
```

### Reading Stats Component

**File:** `src/components/reading/ReadingStatsCard.tsx`

```typescript
"use client";

import { useEffect, useState } from "react";
import { getUserReadingStatsAction } from "@/actions/reading-progress.actions";
import { BookOpen, CheckCircle, TrendingUp } from "lucide-react";

export function ReadingStatsCard() {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchStats() {
      const result = await getUserReadingStatsAction();
      if (result.ok) {
        setStats(result.data);
      }
      setLoading(false);
    }

    fetchStats();
  }, []);

  if (loading) {
    return <div className="h-32 bg-gray-200 rounded-lg animate-pulse" />;
  }

  if (!stats) {
    return null;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {/* Currently Reading */}
      <div className="bg-white border rounded-lg p-6">
        <div className="flex items-center gap-3">
          <BookOpen className="text-blue-600" size={24} />
          <div>
            <p className="text-gray-600 text-sm">Currently Reading</p>
            <p className="text-3xl font-bold text-gray-900">
              {stats.totalComicsReading}
            </p>
          </div>
        </div>
      </div>

      {/* Completed */}
      <div className="bg-white border rounded-lg p-6">
        <div className="flex items-center gap-3">
          <CheckCircle className="text-green-600" size={24} />
          <div>
            <p className="text-gray-600 text-sm">Completed</p>
            <p className="text-3xl font-bold text-gray-900">
              {stats.totalComicsCompleted}
            </p>
          </div>
        </div>
      </div>

      {/* Pages Read */}
      <div className="bg-white border rounded-lg p-6">
        <div className="flex items-center gap-3">
          <TrendingUp className="text-purple-600" size={24} />
          <div>
            <p className="text-gray-600 text-sm">Pages Read</p>
            <p className="text-3xl font-bold text-gray-900">
              {stats.totalPagesRead?.toLocaleString() ?? 0}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## Chapter Reader Integration

**File:** `src/components/chapter/ChapterReader.tsx`

```typescript
"use client";

import { useState, useEffect } from "react";
import { updateProgressAction } from "@/actions/reading-progress.actions";

interface ChapterReaderProps {
  chapterId: number;
  comicId: number;
  pageCount: number;
  content: string; // HTML content of all pages
}

export function ChapterReader({
  chapterId,
  comicId,
  pageCount,
  content,
}: ChapterReaderProps) {
  const [currentPage, setCurrentPage] = useState(1);
  const [isSaving, setIsSaving] = useState(false);

  // Auto-save progress every 10 seconds or on page change
  useEffect(() => {
    let timeout: NodeJS.Timeout;

    const saveProgress = async () => {
      setIsSaving(true);
      await updateProgressAction(
        comicId,
        chapterId,
        currentPage,
        ((currentPage / pageCount) * 100).toFixed(2)
      );
      setIsSaving(false);
    };

    // Save immediately on page change
    saveProgress();

    // Then set up auto-save every 10 seconds
    timeout = setTimeout(saveProgress, 10000);

    return () => clearTimeout(timeout);
  }, [chapterId, comicId, currentPage, pageCount]);

  const progressPercent = (currentPage / pageCount) * 100;

  return (
    <div className="max-w-4xl mx-auto py-8">
      {/* Reader Header */}
      <div className="mb-6">
        <div className="flex justify-between items-center mb-4">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">Chapter {chapterId}</h2>
            <p className="text-gray-600">
              Page {currentPage} of {pageCount}
            </p>
          </div>
          {isSaving && <span className="text-sm text-blue-600">Saving...</span>}
        </div>

        {/* Progress Bar */}
        <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-blue-600 transition-all"
            style={{ width: `${progressPercent}%` }}
          />
        </div>
      </div>

      {/* Content */}
      <div className="bg-white rounded-lg p-8 mb-6">
        <div dangerouslySetInnerHTML={{ __html: content }} />
      </div>

      {/* Navigation */}
      <div className="flex justify-between items-center">
        <button
          onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
          disabled={currentPage === 1}
          className="px-6 py-2 border rounded-lg disabled:opacity-50"
        >
          ← Previous
        </button>

        <span className="text-gray-600">
          {currentPage} / {pageCount}
        </span>

        <button
          onClick={() => setCurrentPage(Math.min(pageCount, currentPage + 1))}
          disabled={currentPage === pageCount}
          className="px-6 py-2 bg-blue-600 text-white rounded-lg disabled:opacity-50"
        >
          Next →
        </button>
      </div>
    </div>
  );
}
```

---

## Progress Synchronization

### Optimistic Updates

For a better user experience, update UI immediately while server saves:

```typescript
"use client";

import { useState } from "react";
import { updateProgressAction } from "@/actions/reading-progress.actions";

export function PageNavigator({ pageCount }: { pageCount: number }) {
  const [currentPage, setCurrentPage] = useState(1);
  const [pendingPage, setPendingPage] = useState(currentPage);

  const handleNextPage = async () => {
    const nextPage = Math.min(pageCount, currentPage + 1);

    // Optimistic update: Update UI immediately
    setCurrentPage(nextPage);
    setPendingPage(nextPage);

    // Save to server in background
    const result = await updateProgressAction(
      comicId,
      chapterId,
      nextPage,
      ((nextPage / pageCount) * 100).toFixed(2)
    );

    if (!result.ok) {
      // Revert on error
      setCurrentPage(currentPage);
      console.error("Failed to save progress");
    }
  };

  return (
    <button onClick={handleNextPage} disabled={pendingPage === pageCount}>
      Next Page
    </button>
  );
}
```

---

## Testing

```typescript
// src/tests/reading-progress.spec.ts
import { describe, it, expect } from "vitest";
import { readingProgressDal } from "@/dal/reading-progress-dal";

describe("Reading Progress", () => {
  const userId = "test-user";
  const comicId = 1;

  it("creates reading progress on first update", async () => {
    const result = await readingProgressDal.updateProgress({
      userId,
      comicId,
      currentChapterId: 1,
      currentPageNumber: 5
    });

    expect(result).toBeDefined();
    expect(result.currentPageNumber).toBe(5);
  });

  it("updates existing progress (idempotent)", async () => {
    // First update
    await readingProgressDal.updateProgress({
      userId,
      comicId,
      currentPageNumber: 5
    });

    // Second update - should replace, not duplicate
    const result = await readingProgressDal.updateProgress({
      userId,
      comicId,
      currentPageNumber: 10
    });

    expect(result.currentPageNumber).toBe(10);
  });

  it("marks comic as completed", async () => {
    const progress = await readingProgressDal.markCompleted(
      userId,
      comicId
    );

    expect(progress?.status).toBe("Completed");
    expect(progress?.progressPercent).toBe("100.00");
  });
});
```

---

## Summary

✅ **Complete Reading Progress Implementation:**

1. **Database** - Idempotent upsert pattern with composite key
2. **DAL** - Optimized queries for common operations
3. **Server Actions** - Protected, async progress updates
4. **Components** - Reusable, performant UI components
5. **Auto-save** - Background progress tracking
6. **Stats** - User reading analytics
7. **Device Sync** - Cross-device reading continuation

---

**Version:** 1.0.0 | **Updated:** March 1, 2026 | **Framework:** Next.js 16
