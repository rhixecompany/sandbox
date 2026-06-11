"use client";
import { create } from "zustand";
import { devtools } from "zustand/middleware";

interface ProgressEntry {
  chapterId: number;
  comicId: number;
  currentImageIndex: number;
  progressPercent: number;
  scrollPercentage: number;
  updatedAt: Date;
}

interface ReadingProgressState {
  bulkSetProgress: (entries: ProgressEntry[]) => void;
  getProgress: (comicId: number) => ProgressEntry | undefined;
  progress: Record<number, ProgressEntry>;
  setProgress: (comicId: number, entry: Omit<ProgressEntry, "comicId" | "updatedAt">) => void;
}

export const useReadingProgressStore = create<ReadingProgressState>()(
  devtools(
    (set, get) => ({
      progress: {},
      setProgress: (comicId, entry) =>
        set(
          (s) => ({
            progress: { ...s.progress, [comicId]: { ...entry, comicId, updatedAt: new Date() } },
          }),
          false,
          "setProgress"
        ),
      getProgress: (comicId) => get().progress[comicId],
      bulkSetProgress: (entries) =>
        set({ progress: Object.fromEntries(entries.map((e) => [e.comicId, e])) }, false, "bulkSetProgress"),
    }),
    { name: "ReadingProgressStore" }
  )
);
