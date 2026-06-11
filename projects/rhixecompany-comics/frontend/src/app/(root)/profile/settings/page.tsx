/**
 * User Settings Page
 * Configure user preferences including theme, reading, display, notifications, and privacy
 * Route: /profile/settings
 */

import { ChevronLeft } from "lucide-react";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Suspense } from "react";

import { getUserPreferencesAction } from "@/actions/user-preferences.actions";
import { auth } from "@/auth";
import { SettingsForm } from "@/components/profile";
export const metadata = {
  title: "Settings | ComicWise",
  description: "Manage your ComicWise preferences and settings",
};

async function SettingsContent() {
  const session = await auth();
  if (!session?.user) {
    redirect("/auth/sign-in" as never);
  }

  const preferencesResult = await getUserPreferencesAction();

  let preferences = null;
  if (preferencesResult.ok) {
    preferences = preferencesResult.data;
  }

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
      {/* Header */}
      <div className="mb-8">
        <Link href="/profile">
          <button className="mb-4 flex items-center gap-2 text-muted-foreground transition-colors hover:text-foreground">
            <ChevronLeft className="h-4 w-4" />
            Back to Profile
          </button>
        </Link>
        <h1 className="text-3xl font-bold">Settings</h1>
        <p className="mt-2 text-muted-foreground">Manage your preferences and account settings</p>
      </div>

      {/* Settings Form */}
      {preferences ? (
        <SettingsForm initialData={preferences} />
      ) : (
        <div className="rounded-lg border border-border bg-card p-8">
          <p className="text-muted-foreground">Loading your settings...</p>
        </div>
      )}
    </div>
  );
}

export default function SettingsPage() {
  return (
    <main className="min-h-screen bg-background py-12">
      <Suspense
        fallback={
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <div className="mb-4 h-12 animate-pulse rounded-lg bg-muted" />
            <div className="space-y-6">
              {[1, 2, 3].map((i) => (
                <div className="h-96 animate-pulse rounded-lg bg-muted" key={i} />
              ))}
            </div>
          </div>
        }
      >
        <SettingsContent />
      </Suspense>
    </main>
  );
}
