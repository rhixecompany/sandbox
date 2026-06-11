"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

interface ReaderState {
  currentPage: number;
  direction: "ltr" | "rtl";
  layout: "double" | "single" | "strip";
  nextPage: () => void;
  prevPage: () => void;
  reset: () => void;
  scrollPercentage: number;
  setCurrentPage: (page: number) => void;
  setDirection: (direction: ReaderState["direction"]) => void;
  setLayout: (layout: ReaderState["layout"]) => void;
  setScrollPercentage: (pct: number) => void;
  setTotalPages: (total: number) => void;
  setZoom: (zoom: number) => void;
  totalPages: number;
  zoom: number;
}

export const useReaderStore = create<ReaderState>()(
  devtools(
    persist(
      (set, _get) => ({
        currentPage: 1,
        totalPages: 0,
        scrollPercentage: 0,
        zoom: 100,
        layout: "single",
        direction: "ltr",
        setCurrentPage: (page) => set({ currentPage: page }, false, "setCurrentPage"),
        setTotalPages: (total) => set({ totalPages: total }, false, "setTotalPages"),
        setScrollPercentage: (scrollPercentage) => set({ scrollPercentage }, false, "setScrollPercentage"),
        setZoom: (zoom) => set({ zoom: Math.min(200, Math.max(50, zoom)) }, false, "setZoom"),
        setLayout: (layout) => set({ layout }, false, "setLayout"),
        setDirection: (direction) => set({ direction }, false, "setDirection"),
        nextPage: () => set((s) => ({ currentPage: Math.min(s.currentPage + 1, s.totalPages) }), false, "nextPage"),
        prevPage: () => set((s) => ({ currentPage: Math.max(s.currentPage - 1, 1) }), false, "prevPage"),
        reset: () => set({ currentPage: 1, scrollPercentage: 0 }, false, "reset"),
      }),
      { name: "reader-settings", partialize: (s) => ({ zoom: s.zoom, layout: s.layout, direction: s.direction }) }
    ),
    { name: "ReaderStore" }
  )
);
