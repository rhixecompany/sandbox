"use client";

import { useState } from "react";

// Small client-only hook to expose the current timestamp and year after mount.
// Use this instead of calling Date.now() / new Date() synchronously in render.
export function useNow() {
  // Initialize with a function to avoid calling Date.now() during render
  const [now] = useState<number>(() => {
    // This will be null on server-side render, then set client-side
    if (typeof window === "undefined") return 0;
    return Date.now();
  });

  return now || null;
}

export function useCurrentYear() {
  const now = useNow();
  return now ? new Date(now).getFullYear() : null;
}
