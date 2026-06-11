"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

interface UIState {
  searchOpen: boolean;
  setSearchOpen: (open: boolean) => void;
  setSidebarOpen: (open: boolean) => void;
  setTheme: (theme: UIState["theme"]) => void;
  sidebarOpen: boolean;
  theme: "dark" | "light" | "system";
  toggleSidebar: () => void;
}

export const useUIStore = create<UIState>()(
  devtools(
    persist(
      (set) => ({
        sidebarOpen: true,
        searchOpen: false,
        theme: "system",
        setSidebarOpen: (sidebarOpen) => set({ sidebarOpen }, false, "setSidebarOpen"),
        toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen }), false, "toggleSidebar"),
        setSearchOpen: (searchOpen) => set({ searchOpen }, false, "setSearchOpen"),
        setTheme: (theme) => set({ theme }, false, "setTheme"),
      }),
      { name: "ui-preferences", partialize: (s) => ({ theme: s.theme, sidebarOpen: s.sidebarOpen }) }
    ),
    { name: "UIStore" }
  )
);
