"use client";
import { create } from "zustand";
import { devtools } from "zustand/middleware";

interface BookmarkEntry {
  comicId: number;
  lastReadChapterId: null | number;
  status: string;
}

interface BookmarkState {
  addBookmark: (entry: BookmarkEntry) => void;
  bookmarks: Record<number, BookmarkEntry>;
  isBookmarked: (comicId: number) => boolean;
  isLoaded: boolean;
  removeBookmark: (comicId: number) => void;
  setBookmarks: (bookmarks: BookmarkEntry[]) => void;
  updateBookmark: (comicId: number, data: Partial<BookmarkEntry>) => void;
}

export const useBookmarkStore = create<BookmarkState>()(
  devtools(
    (set, get) => ({
      bookmarks: {},
      isLoaded: false,
      setBookmarks: (bookmarks) =>
        set(
          { bookmarks: Object.fromEntries(bookmarks.map((b) => [b.comicId, b])), isLoaded: true },
          false,
          "setBookmarks"
        ),
      addBookmark: (entry) =>
        set((s) => ({ bookmarks: { ...s.bookmarks, [entry.comicId]: entry } }), false, "addBookmark"),
      removeBookmark: (comicId) =>
        set(
          (s) => {
            const b = { ...s.bookmarks };
            delete b[comicId];
            return { bookmarks: b };
          },
          false,
          "removeBookmark"
        ),
      updateBookmark: (comicId, data) =>
        set(
          (s) => ({
            bookmarks: { ...s.bookmarks, [comicId]: { ...s.bookmarks[comicId], ...data } },
          }),
          false,
          "updateBookmark"
        ),
      isBookmarked: (comicId) => !!get().bookmarks[comicId],
    }),
    { name: "BookmarkStore" }
  )
);
