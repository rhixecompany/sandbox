/**
 * Delete Account Page
 * Route: /profile/delete-account
 * Allows users to permanently delete their account with confirmation
 */

import { AlertTriangle, ChevronLeft } from "lucide-react";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Suspense } from "react";

import { auth } from "@/auth";
import { DeleteAccountForm } from "@/components/profile";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

export const metadata = {
  title: "Delete Account | ComicWise",
  description: "Permanently delete your account and all associated data",
};

async function DeleteAccountContent() {
  const session = await auth();
  if (!session?.user?.id) {
    redirect("/auth/sign-in" as never);
  }

  return (
    <div className="mx-auto max-w-2xl px-4 sm:px-6 lg:px-8">
      {/* Header */}
      <div className="mb-8">
        <Link href="/profile">
          <button className="mb-4 flex items-center gap-2 text-muted-foreground transition-colors hover:text-foreground">
            <ChevronLeft className="h-4 w-4" />
            Back to Profile
          </button>
        </Link>
        <h1 className="text-3xl font-bold">Delete Account</h1>
        <p className="mt-2 text-muted-foreground">Permanently remove your account from ComicWise</p>
      </div>

      {/* Warning Alert */}
      <Alert className="mb-6 border-destructive/50 bg-destructive/5">
        <AlertTriangle className="h-4 w-4 text-destructive" />
        <AlertTitle className="text-destructive">Warning: This action cannot be undone</AlertTitle>
        <AlertDescription>
          Deleting your account will permanently remove all your data including:
          <ul className="mt-2 list-inside list-disc space-y-1">
            <li>Your profile information</li>
            <li>All bookmarks and reading progress</li>
            <li>Comments and ratings</li>
            <li>Reading history</li>
          </ul>
        </AlertDescription>
      </Alert>

      {/* Delete Account Form */}
      <DeleteAccountForm userEmail={session.user.email ?? ""} userId={session.user.id} />
    </div>
  );
}

export default function DeleteAccountPage() {
  return (
    <main className="min-h-screen bg-background py-12">
      <Suspense
        fallback={
          <div className="mx-auto max-w-2xl px-4 sm:px-6 lg:px-8">
            <div className="h-96 animate-pulse rounded-lg bg-muted" />
          </div>
        }
      >
        <DeleteAccountContent />
      </Suspense>
    </main>
  );
}
