/**
 * Change Password Page
 * Route: /profile/change-password
 */

import { ChevronLeft } from "lucide-react";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Suspense } from "react";

import { auth } from "@/auth";
import { ChangePasswordForm } from "@/components/profile";

export const metadata = {
  title: "Change Password | ComicWise",
  description: "Update your password to keep your account secure",
};

async function ChangePasswordContent() {
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
        <h1 className="text-3xl font-bold">Change Password</h1>
        <p className="mt-2 text-muted-foreground">Update your password to keep your account secure</p>
      </div>

      {/* Change Password Form */}
      <ChangePasswordForm />
    </div>
  );
}

export default function ChangePasswordPage() {
  return (
    <main className="min-h-screen bg-background py-12">
      <Suspense
        fallback={
          <div className="mx-auto max-w-2xl px-4 sm:px-6 lg:px-8">
            <div className="mb-4 h-12 animate-pulse rounded-lg bg-muted" />
            <div className="h-96 animate-pulse rounded-lg bg-muted" />
          </div>
        }
      >
        <ChangePasswordContent />
      </Suspense>
    </main>
  );
}
