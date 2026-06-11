"use client";

import { BookmarkX, MoreVertical, Trash2 } from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import { useState } from "react";

import { Button } from "@/components/ui/button";

import type { BookmarkCardData } from "@/types/bookmark";

interface BookmarkCardProps {
  bookmark: BookmarkCardData;
  isListView?: boolean;
  onRemove?: (comicId: number) => void;
}

export function BookmarkCard({ bookmark, onRemove, isListView = false }: BookmarkCardProps) {
  const [isLoading, setIsLoading] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  const handleRemove = async () => {
    setIsLoading(true);
    try {
      onRemove?.(bookmark.comicId);
    } finally {
      setIsLoading(false);
      setShowMenu(false);
    }
  };

  if (isListView) {
    return (
      <div className="flex gap-4 rounded-lg border border-gray-200 p-4 transition-shadow hover:shadow-md dark:border-gray-700 dark:hover:bg-gray-800/50">
        {/* Cover Image */}
        <Link className="shrink-0" href={`/comics/${bookmark.comicSlug}`}>
          <div className="relative h-24 w-16 overflow-hidden rounded">
            {bookmark.coverImage ? (
              <Image alt={bookmark.comicTitle} className="object-cover" fill src={bookmark.coverImage} />
            ) : (
              <div className="h-full w-full bg-gray-200 dark:bg-gray-700" />
            )}
          </div>
        </Link>

        {/* Comic Info */}
        <div className="flex-1">
          <div className="flex items-start justify-between gap-4">
            <div className="flex-1">
              <Link className="group" href={`/comics/${bookmark.comicSlug}`}>
                <h3 className="text-lg font-semibold group-hover:text-blue-600 dark:group-hover:text-blue-400">
                  {bookmark.comicTitle}
                </h3>
              </Link>
              <p className="text-sm text-gray-600 dark:text-gray-400">by {bookmark.authorName}</p>
              <div className="mt-2 flex items-center gap-2">
                <span
                  className={`inline-block rounded px-2 py-1 text-xs font-medium ${
                    bookmark.status === "Reading"
                      ? "bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400"
                      : bookmark.status === "Completed"
                        ? "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400"
                        : "bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-400"
                  }`}
                >
                  {bookmark.status}
                </span>
                {bookmark.lastReadChapter && (
                  <span className="text-xs text-gray-600 dark:text-gray-400">
                    Stopped at <span className="font-medium">Chapter {bookmark.lastReadChapter}</span>
                  </span>
                )}
              </div>
            </div>

            {/* More Menu */}
            <div className="relative">
              <Button className="h-8 w-8 p-0" onClick={() => setShowMenu(!showMenu)} size="sm" variant="ghost">
                <MoreVertical className="h-4 w-4" />
              </Button>
              {showMenu && (
                <div className="absolute top-8 right-0 z-10 overflow-hidden rounded-lg bg-white shadow-lg dark:bg-gray-800">
                  <button
                    className="flex w-full items-center gap-2 px-4 py-2 text-sm text-red-600 hover:bg-red-50 dark:text-red-400 dark:hover:bg-red-900/20"
                    disabled={isLoading}
                    onClick={() => void handleRemove()}
                  >
                    <Trash2 className="h-4 w-4" />
                    Remove
                  </button>
                </div>
              )}
            </div>
          </div>

          {/* Progress */}
          <div className="mt-3">
            <div className="mb-1 flex items-center justify-between">
              <span className="text-xs font-medium text-gray-600 dark:text-gray-400">Progress</span>
              <span className="text-xs font-medium text-gray-600 dark:text-gray-400">
                {Math.round(bookmark.progressPercent)}%
              </span>
            </div>
            <div className="h-1.5 w-full overflow-hidden rounded-full bg-gray-200 dark:bg-gray-700">
              <div className="h-full bg-blue-600 transition-all" style={{ width: `${bookmark.progressPercent}%` }} />
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Grid view
  return (
    <div className="group relative overflow-hidden rounded-lg border border-gray-200 transition-shadow hover:shadow-lg dark:border-gray-700 dark:hover:border-gray-600">
      {/* Cover Image */}
      <Link className="block" href={`/comics/${bookmark.comicSlug}`}>
        <div className="relative aspect-2/3 overflow-hidden bg-gray-100 dark:bg-gray-800">
          {bookmark.coverImage ? (
            <Image
              alt={bookmark.comicTitle}
              className="object-cover transition-transform group-hover:scale-105"
              fill
              src={bookmark.coverImage}
            />
          ) : (
            <div className="h-full w-full bg-linear-to-br from-gray-300 to-gray-200 dark:from-gray-600 dark:to-gray-700" />
          )}

          {/* Overlay */}
          <div className="absolute inset-0 bg-linear-to-t from-black/80 via-transparent opacity-0 transition-opacity group-hover:opacity-100" />
        </div>
      </Link>

      {/* Content */}
      <div className="p-3">
        <Link href={`/comics/${bookmark.comicSlug}`}>
          <h3 className="line-clamp-2 text-sm font-semibold group-hover:text-blue-600 dark:group-hover:text-blue-400">
            {bookmark.comicTitle}
          </h3>
        </Link>
        <p className="mt-1 line-clamp-1 text-xs text-gray-600 dark:text-gray-400">{bookmark.authorName}</p>

        {/* Status Badge */}
        <div className="mt-2">
          <span
            className={`inline-block rounded px-2 py-0.5 text-xs font-medium ${
              bookmark.status === "Reading"
                ? "bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400"
                : bookmark.status === "Completed"
                  ? "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400"
                  : "bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-400"
            }`}
          >
            {bookmark.status}
          </span>
        </div>

        {/* Progress Bar */}
        <div className="mt-3">
          <div className="mb-1 flex items-center justify-between">
            <span className="text-xs text-gray-600 dark:text-gray-400">Progress</span>
            <span className="text-xs font-medium text-gray-600 dark:text-gray-400">
              {Math.round(bookmark.progressPercent)}%
            </span>
          </div>
          <div className="h-1.5 w-full overflow-hidden rounded-full bg-gray-200 dark:bg-gray-700">
            <div className="h-full bg-blue-600 transition-all" style={{ width: `${bookmark.progressPercent}%` }} />
          </div>
        </div>

        {/* Last Read */}
        {bookmark.lastReadChapter && (
          <p className="mt-2 text-xs text-gray-500 dark:text-gray-500">Ch. {bookmark.lastReadChapter}</p>
        )}
      </div>

      {/* Delete Button (visible on hover) */}
      <div className="absolute top-2 right-2 opacity-0 transition-opacity group-hover:opacity-100">
        <Button
          className="h-8 w-8 bg-red-600/90 p-0 text-white hover:bg-red-700"
          disabled={isLoading}
          onClick={() => void handleRemove()}
          size="sm"
          title="Remove bookmark"
          variant="ghost"
        >
          <BookmarkX className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
