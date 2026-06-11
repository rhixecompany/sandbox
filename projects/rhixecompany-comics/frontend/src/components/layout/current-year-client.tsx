"use client";
import { useCurrentYear } from "@/hooks/use-now";

// Client-only year display: reads the year after mount via `useCurrentYear`.
export default function CurrentYearClient() {
  const year = useCurrentYear();
  return <>{year ?? null}</>;
}
