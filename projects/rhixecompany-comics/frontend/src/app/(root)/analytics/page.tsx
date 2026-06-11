/**
 * Analytics Page
 * Main reading analytics dashboard page
 */

import { ArrowLeft } from "lucide-react";
import Link from "next/link";

import { ReadingDashboard } from "@/components/analytics/reading-dashboard";
import { Button } from "@/components/ui/button";

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Reading Analytics",
  description: "View your reading statistics, history, and goals",
};

interface AnalyticsPageProps {
  searchParams: Promise<{
    period?: string;
  }>;
}

export default async function AnalyticsPage({ searchParams }: AnalyticsPageProps) {
  const params = await searchParams;
  const timePeriod = params.period || "all";

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold tracking-tight text-foreground dark:text-foreground">Reading Analytics</h1>
          <p className="text-sm text-muted-foreground dark:text-muted-foreground">
            Monitor your reading progress and manage your reading goals
          </p>
        </div>

        <Link href="/profile">
          <Button className="gap-2" size="sm" variant="outline">
            <ArrowLeft className="h-4 w-4" />
            Back to Profile
          </Button>
        </Link>
      </div>

      {/* Time period selector */}
      <div className="flex gap-2 border-b border-muted-foreground/20 pb-4 dark:border-muted-foreground/10">
        <Button asChild size="sm" variant={timePeriod === "all" ? "default" : "outline"}>
          <Link href="/analytics">All Time</Link>
        </Button>
        <Button asChild size="sm" variant={timePeriod === "30days" ? "default" : "outline"}>
          <Link href="/analytics?period=30days">Last 30 Days</Link>
        </Button>
        <Button asChild size="sm" variant={timePeriod === "7days" ? "default" : "outline"}>
          <Link href="/analytics?period=7days">Last 7 Days</Link>
        </Button>
      </div>

      {/* Dashboard content */}
      <ReadingDashboard timePeriod={timePeriod} />
    </div>
  );
}
