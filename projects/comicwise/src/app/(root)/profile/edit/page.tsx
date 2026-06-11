/**
 * Edit Profile Page
 * Allow users to edit their profile information
 * Route: /profile/edit
 */

import { ChevronLeft } from "lucide-react";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Suspense } from "react";

import { getUserProfileAction } from "@/actions/profile.actions";
import { auth } from "@/auth";
import { ProfileEditForm } from "@/components/profile";
import { Button } from "@/components/ui/button";

export const metadata = {
  title: "Edit Profile | ComicWise",
  description: "Update your ComicWise profile information",
};

async function EditProfileContent() {
  const session = await auth();
  if (!session?.user) {
    redirect("/auth/sign-in" as never);
  }

  const profileResult = await getUserProfileAction();

  if (!profileResult.ok) {
    return (
      <div className="py-12 text-center">
        <h1 className="mb-2 text-2xl font-bold">Error loading profile</h1>
        <p className="text-muted-foreground">{profileResult.error}</p>
        <Link href="/profile">
          <Button className="mt-4">Return to Profile</Button>
        </Link>
      </div>
    );
  }

  const profile = profileResult.data;

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
        <h1 className="text-3xl font-bold">Edit Profile</h1>
        <p className="mt-2 text-muted-foreground">Update your profile information</p>
      </div>

      {/* Edit Form */}
      <div className="rounded-lg border border-border bg-card p-8">
        <ProfileEditForm
          initialData={{
            name: profile.name || "",
            email: profile.email || "",
            bio: profile.bio || "",
            image: profile.image || "",
          }}
        />
      </div>
    </div>
  );
}

export default function EditProfilePage() {
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
        <EditProfileContent />
      </Suspense>
    </main>
  );
}
