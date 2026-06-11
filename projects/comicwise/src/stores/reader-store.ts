"use client";

import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

export interface ReaderSettings {
  autoScroll: boolean;
  brightness: number;
  contrast: number;
  viewMode: "double" | "single";
}

export interface ReaderState {
  resetSettings: () => void;
  settings: ReaderSettings;
  updateSettings: (partial: Partial<ReaderSettings>) => void;
}

const DEFAULT_SETTINGS: ReaderSettings = {
  brightness: 100,
  contrast: 100,
  viewMode: "single",
  autoScroll: false,
};

export const useReaderStore = create<ReaderState>()(
  devtools(
    persist(
      (set) => ({
        settings: DEFAULT_SETTINGS,
        updateSettings: (partial) =>
          set((state) => ({
            settings: { ...state.settings, ...partial },
          })),
        resetSettings: () =>
          set({
            settings: DEFAULT_SETTINGS,
          }),
      }),
      {
        name: "reader-settings",
      }
    ),
    { name: "ReaderStore" }
  )
);
