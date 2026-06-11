/**
 * Settings Page
 * User preferences and settings management
 */

import { notFound } from "next/navigation";
import { Suspense } from "react";

import { getUserPreferencesAction } from "@/actions/user-preferences.actions";
import { auth } from "@/auth";
import { SettingsForm } from "@/components/settings";

export const metadata = {
  title: "Settings - ComicWise",
  description: "Manage your preferences and account settings",
};

async function SettingsContent() {
  const session = await auth();

  if (!session?.user?.id) {
    notFound();
  }

  const result = await getUserPreferencesAction();
  if (!result.ok || !result.data) {
    notFound();
  }

  return (
    <div className="mx-auto max-w-2xl">
      <h1 className="mb-2 text-3xl font-bold text-gray-900">Settings</h1>
      <p className="mb-8 text-gray-600">Manage your preferences and customize your reading experience</p>

      <SettingsForm initialPreferences={result.data} />
    </div>
  );
}

export default function SettingsPage() {
  return (
    <main className="min-h-screen bg-gray-50">
      <div className="mx-auto max-w-6xl px-4 py-8">
        <Suspense
          fallback={
            <div className="space-y-4">
              <div className="h-10 w-64 animate-pulse rounded bg-gray-200" />
              <div className="space-y-3">
                {Array.from({ length: 5 }).map((_, i) => (
                  <div className="h-12 animate-pulse rounded bg-gray-200" key={i} />
                ))}
              </div>
            </div>
          }
        >
          <SettingsContent />
        </Suspense>
      </div>
    </main>
  );
}
