/**
 * Analytics Layout
 * Shared layout for analytics routes
 */

import type { ReactNode } from "react";

interface AnalyticsLayoutProps {
  children: ReactNode;
}

export default function AnalyticsLayout({ children }: AnalyticsLayoutProps) {
  return (
    <div className="p-6 md:p-8">
      <div className="mx-auto max-w-7xl">{children}</div>
    </div>
  );
}
