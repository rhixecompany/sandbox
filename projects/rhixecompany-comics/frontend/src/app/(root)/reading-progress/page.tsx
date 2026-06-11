/**
 * Reading Progress Page (Continue Reading)
 * Route: /reading-progress
 * Shows user's "Continue Reading" list with idempotent upsert pattern
 */

import { redirect } from "next/navigation";

import { auth } from "@/auth";
import { ContinueReadingSection } from "@/components/reading";

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Continue Reading | ComicWise",
  description: "Your reading history and continue reading list",
};

export default async function ReadingProgressPage() {
  // Protect page - require authentication
  const session = await auth();
  if (!session?.user?.id) {
    redirect("/sign-in");
  }

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <div className="border-b bg-white">
        <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
          <h1 className="mb-2 text-4xl font-bold">Continue Reading</h1>
          <p className="text-muted-foreground">Your reading history and bookmarks</p>
        </div>
      </div>

      {/* Content */}
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        {/* Continue Reading List */}
        <div className="space-y-6">
          <ContinueReadingSection />
        </div>
      </div>
    </main>
  );
}
