# Phase 9A: Zustand Stores (7 new files)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 9A: Zustand Stores (7 new files)

> Directory: `src/stores/` — must be created. All stores use `devtools(persist(...))`.

### Pattern for all stores:

```ts
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";
```

### 9A.1 — `src/stores/use-comic-filters-store.ts`

```ts
"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

type ComicStatusEnum =
  | "Ongoing"
  | "Hiatus"
  | "Completed"
  | "Dropped"
  | "Season End"
  | "Coming Soon";

interface ComicFiltersState {
  search: string;
  status: ComicStatusEnum | "";
  genreIds: number[];
  typeId: number | null;
  page: number;
  limit: number;
  setSearch: (search: string) => void;
  setStatus: (status: ComicStatusEnum | "") => void;
  toggleGenre: (genreId: number) => void;
  setTypeId: (typeId: number | null) => void;
  setPage: (page: number) => void;
  reset: () => void;
}

const initialState = {
  search: "",
  status: "" as const,
  genreIds: [],
  typeId: null,
  page: 1,
  limit: 20
};

export const useComicFiltersStore = create<ComicFiltersState>()(
  devtools(
    persist(
      set => ({
        ...initialState,
        setSearch: search =>
          set({ search, page: 1 }, false, "setSearch"),
        setStatus: status =>
          set({ status, page: 1 }, false, "setStatus"),
        toggleGenre: genreId =>
          set(
            s => ({
              genreIds: s.genreIds.includes(genreId)
                ? s.genreIds.filter(id => id !== genreId)
                : [...s.genreIds, genreId],
              page: 1
            }),
            false,
            "toggleGenre"
          ),
        setTypeId: typeId =>
          set({ typeId, page: 1 }, false, "setTypeId"),
        setPage: page => set({ page }, false, "setPage"),
        reset: () => set(initialState, false, "reset")
      }),
      { name: "comic-filters" }
    ),
    { name: "ComicFiltersStore" }
  )
);
```

### 9A.2 — `src/stores/use-reader-store.ts`

```ts
"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

interface ReaderState {
  currentPage: number;
  totalPages: number;
  scrollPercentage: number;
  zoom: number;
  layout: "single" | "double" | "strip";
  direction: "ltr" | "rtl";
  setCurrentPage: (page: number) => void;
  setTotalPages: (total: number) => void;
  setScrollPercentage: (pct: number) => void;
  setZoom: (zoom: number) => void;
  setLayout: (layout: ReaderState["layout"]) => void;
  setDirection: (direction: ReaderState["direction"]) => void;
  nextPage: () => void;
  prevPage: () => void;
  reset: () => void;
}

export const useReaderStore = create<ReaderState>()(
  devtools(
    persist(
      (set, get) => ({
        currentPage: 1,
        totalPages: 0,
        scrollPercentage: 0,
        zoom: 100,
        layout: "single",
        direction: "ltr",
        setCurrentPage: page =>
          set({ currentPage: page }, false, "setCurrentPage"),
        setTotalPages: total =>
          set({ totalPages: total }, false, "setTotalPages"),
        setScrollPercentage: scrollPercentage =>
          set({ scrollPercentage }, false, "setScrollPercentage"),
        setZoom: zoom =>
          set(
            { zoom: Math.min(200, Math.max(50, zoom)) },
            false,
            "setZoom"
          ),
        setLayout: layout => set({ layout }, false, "setLayout"),
        setDirection: direction =>
          set({ direction }, false, "setDirection"),
        nextPage: () =>
          set(
            s => ({
              currentPage: Math.min(s.currentPage + 1, s.totalPages)
            }),
            false,
            "nextPage"
          ),
        prevPage: () =>
          set(
            s => ({ currentPage: Math.max(s.currentPage - 1, 1) }),
            false,
            "prevPage"
          ),
        reset: () =>
          set({ currentPage: 1, scrollPercentage: 0 }, false, "reset")
      }),
      {
        name: "reader-settings",
        partialize: s => ({
          zoom: s.zoom,
          layout: s.layout,
          direction: s.direction
        })
      }
    ),
    { name: "ReaderStore" }
  )
);
```

### 9A.3 — `src/stores/use-bookmark-store.ts`

```ts
"use client";
import { create } from "zustand";
import { devtools } from "zustand/middleware";

interface BookmarkEntry {
  comicId: number;
  status: string;
  lastReadChapterId: number | null;
}

interface BookmarkState {
  bookmarks: Record<number, BookmarkEntry>;
  isLoaded: boolean;
  setBookmarks: (bookmarks: BookmarkEntry[]) => void;
  addBookmark: (entry: BookmarkEntry) => void;
  removeBookmark: (comicId: number) => void;
  updateBookmark: (
    comicId: number,
    data: Partial<BookmarkEntry>
  ) => void;
  isBookmarked: (comicId: number) => boolean;
}

export const useBookmarkStore = create<BookmarkState>()(
  devtools(
    (set, get) => ({
      bookmarks: {},
      isLoaded: false,
      setBookmarks: bookmarks =>
        set(
          {
            bookmarks: Object.fromEntries(
              bookmarks.map(b => [b.comicId, b])
            ),
            isLoaded: true
          },
          false,
          "setBookmarks"
        ),
      addBookmark: entry =>
        set(
          s => ({
            bookmarks: { ...s.bookmarks, [entry.comicId]: entry }
          }),
          false,
          "addBookmark"
        ),
      removeBookmark: comicId =>
        set(
          s => {
            const b = { ...s.bookmarks };
            delete b[comicId];
            return { bookmarks: b };
          },
          false,
          "removeBookmark"
        ),
      updateBookmark: (comicId, data) =>
        set(
          s => ({
            bookmarks: {
              ...s.bookmarks,
              [comicId]: { ...s.bookmarks[comicId], ...data }
            }
          }),
          false,
          "updateBookmark"
        ),
      isBookmarked: comicId => !!get().bookmarks[comicId]
    }),
    { name: "BookmarkStore" }
  )
);
```

### 9A.4 — `src/stores/use-notification-store.ts`

```ts
"use client";
import { create } from "zustand";
import { devtools } from "zustand/middleware";

interface NotificationItem {
  id: number;
  title: string;
  message: string;
  read: boolean;
  createdAt: Date;
}

interface NotificationState {
  notifications: NotificationItem[];
  unreadCount: number;
  setNotifications: (items: NotificationItem[]) => void;
  markRead: (id: number) => void;
  markAllRead: () => void;
  addNotification: (item: NotificationItem) => void;
}

export const useNotificationStore = create<NotificationState>()(
  devtools(
    set => ({
      notifications: [],
      unreadCount: 0,
      setNotifications: notifications =>
        set(
          {
            notifications,
            unreadCount: notifications.filter(n => !n.read).length
          },
          false,
          "setNotifications"
        ),
      markRead: id =>
        set(
          s => {
            const notifications = s.notifications.map(n =>
              n.id === id ? { ...n, read: true } : n
            );
            return {
              notifications,
              unreadCount: notifications.filter(n => !n.read).length
            };
          },
          false,
          "markRead"
        ),
      markAllRead: () =>
        set(
          s => ({
            notifications: s.notifications.map(n => ({
              ...n,
              read: true
            })),
            unreadCount: 0
          }),
          false,
          "markAllRead"
        ),
      addNotification: item =>
        set(
          s => ({
            notifications: [item, ...s.notifications],
            unreadCount: item.read ? s.unreadCount : s.unreadCount + 1
          }),
          false,
          "addNotification"
        )
    }),
    { name: "NotificationStore" }
  )
);
```

### 9A.5 — `src/stores/use-ui-store.ts`

```ts
"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

interface UIState {
  sidebarOpen: boolean;
  searchOpen: boolean;
  theme: "light" | "dark" | "system";
  setSidebarOpen: (open: boolean) => void;
  toggleSidebar: () => void;
  setSearchOpen: (open: boolean) => void;
  setTheme: (theme: UIState["theme"]) => void;
}

export const useUIStore = create<UIState>()(
  devtools(
    persist(
      set => ({
        sidebarOpen: true,
        searchOpen: false,
        theme: "system",
        setSidebarOpen: sidebarOpen =>
          set({ sidebarOpen }, false, "setSidebarOpen"),
        toggleSidebar: () =>
          set(
            s => ({ sidebarOpen: !s.sidebarOpen }),
            false,
            "toggleSidebar"
          ),
        setSearchOpen: searchOpen =>
          set({ searchOpen }, false, "setSearchOpen"),
        setTheme: theme => set({ theme }, false, "setTheme")
      }),
      {
        name: "ui-preferences",
        partialize: s => ({
          theme: s.theme,
          sidebarOpen: s.sidebarOpen
        })
      }
    ),
    { name: "UIStore" }
  )
);
```

### 9A.6 — `src/stores/use-reading-progress-store.ts`

```ts
"use client";
import { create } from "zustand";
import { devtools } from "zustand/middleware";

interface ProgressEntry {
  comicId: number;
  chapterId: number;
  progressPercent: number;
  currentImageIndex: number;
  scrollPercentage: number;
  updatedAt: Date;
}

interface ReadingProgressState {
  progress: Record<number, ProgressEntry>;
  setProgress: (
    comicId: number,
    entry: Omit<ProgressEntry, "comicId" | "updatedAt">
  ) => void;
  getProgress: (comicId: number) => ProgressEntry | undefined;
  bulkSetProgress: (entries: ProgressEntry[]) => void;
}

export const useReadingProgressStore = create<ReadingProgressState>()(
  devtools(
    (set, get) => ({
      progress: {},
      setProgress: (comicId, entry) =>
        set(
          s => ({
            progress: {
              ...s.progress,
              [comicId]: { ...entry, comicId, updatedAt: new Date() }
            }
          }),
          false,
          "setProgress"
        ),
      getProgress: comicId => get().progress[comicId],
      bulkSetProgress: entries =>
        set(
          {
            progress: Object.fromEntries(
              entries.map(e => [e.comicId, e])
            )
          },
          false,
          "bulkSetProgress"
        )
    }),
    { name: "ReadingProgressStore" }
  )
);
```

### 9A.7 — `src/stores/index.ts` (barrel)

```ts
export { useComicFiltersStore } from "./use-comic-filters-store";
export { useReaderStore } from "./use-reader-store";
export { useBookmarkStore } from "./use-bookmark-store";
export { useNotificationStore } from "./use-notification-store";
export { useUIStore } from "./use-ui-store";
export { useReadingProgressStore } from "./use-reading-progress-store";
```

---
