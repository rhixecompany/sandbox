"use client";
import { useCurrentYear } from "@/hooks/use-now";

export const CurrentYear = () => {
  const year = useCurrentYear();
  return <>{year ?? null}</>;
};
