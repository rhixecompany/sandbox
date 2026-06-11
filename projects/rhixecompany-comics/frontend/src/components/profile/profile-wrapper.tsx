"use client";

import { Bookmark, BookOpen, Heart, Lock, MessageSquare, Trash2 } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface ProfileData {
  email: null | string;
  image: null | string;
  name: null | string;
}

interface ProfileStats {
  bookmarks: number;
  chaptersRead: number;
  commentsMade: number;
  ratingsGiven: number;
}

interface ProfileWrapperProps {
  profile: ProfileData;
  stats: ProfileStats;
}

export function ProfileWrapper({ profile, stats }: ProfileWrapperProps) {
  return (
    <div className="mx-auto max-w-4xl space-y-6 px-4 py-8">
      {/* Profile Header */}
      <div className="rounded-lg border border-border bg-card p-6">
        <div className="flex items-start gap-6">
          {/* Avatar */}
          {profile.image && (
            <Image
              alt={profile.name || "User"}
              className="rounded-full object-cover"
              height={96}
              src={profile.image}
              width={96}
            />
          )}

          {/* Profile Info */}
          <div className="flex-1">
            <h1 className="text-3xl font-bold">{profile.name || "Anonymous"}</h1>
            <p className="text-muted-foreground">{profile.email}</p>

            {/* Action Buttons */}
            <div className="mt-4 flex flex-wrap gap-2">
              <Link href="/profile/edit">
                <Button size="sm" variant="outline">
                  Edit Profile
                </Button>
              </Link>
              <Link href="/profile/settings">
                <Button size="sm" variant="outline">
                  Settings
                </Button>
              </Link>
              <Link href="/profile/change-password">
                <Button size="sm" variant="outline">
                  <Lock className="mr-2 h-4 w-4" />
                  Change Password
                </Button>
              </Link>
              <Link href="/profile/delete-account">
                <Button className="text-destructive hover:text-destructive" size="sm" variant="outline">
                  <Trash2 className="mr-2 h-4 w-4" />
                  Delete Account
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* Statistics */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {/* Bookmarks */}
        <div className="rounded-lg border border-border bg-card p-4">
          <div className="flex items-center gap-3">
            <div className="rounded-lg bg-muted p-2">
              <Bookmark className="h-5 w-5 text-muted-foreground" />
            </div>
            <div>
              <p className="text-2xl font-bold">{stats.bookmarks}</p>
              <p className="text-sm text-muted-foreground">Bookmarks</p>
            </div>
          </div>
        </div>

        {/* Ratings */}
        <div className="rounded-lg border border-border bg-card p-4">
          <div className="flex items-center gap-3">
            <div className="rounded-lg bg-muted p-2">
              <Heart className="h-5 w-5 text-muted-foreground" />
            </div>
            <div>
              <p className="text-2xl font-bold">{stats.ratingsGiven}</p>
              <p className="text-sm text-muted-foreground">Ratings Given</p>
            </div>
          </div>
        </div>

        {/* Comments */}
        <div className="rounded-lg border border-border bg-card p-4">
          <div className="flex items-center gap-3">
            <div className="rounded-lg bg-muted p-2">
              <MessageSquare className="h-5 w-5 text-muted-foreground" />
            </div>
            <div>
              <p className="text-2xl font-bold">{stats.commentsMade}</p>
              <p className="text-sm text-muted-foreground">Comments</p>
            </div>
          </div>
        </div>

        {/* Chapters Read */}
        <div className="rounded-lg border border-border bg-card p-4">
          <div className="flex items-center gap-3">
            <div className="rounded-lg bg-muted p-2">
              <BookOpen className="h-5 w-5 text-muted-foreground" />
            </div>
            <div>
              <p className="text-2xl font-bold">{stats.chaptersRead}</p>
              <p className="text-sm text-muted-foreground">Chapters Read</p>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Links */}
      <div className="rounded-lg border border-border bg-card p-6">
        <h2 className="mb-4 text-xl font-bold">Quick Links</h2>
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
          <Link className="rounded-lg border border-border p-4 transition hover:bg-muted" href="/bookmarks">
            <h3 className="font-semibold">My Bookmarks</h3>
            <p className="text-sm text-muted-foreground">Manage your reading list</p>
          </Link>

          <Link className="rounded-lg border border-border p-4 transition hover:bg-muted" href="/comics">
            <h3 className="font-semibold">Browse Comics</h3>
            <p className="text-sm text-muted-foreground">Discover new titles</p>
          </Link>

          <Link className="rounded-lg border border-border p-4 transition hover:bg-muted" href="/profile/settings">
            <h3 className="font-semibold">Preferences</h3>
            <p className="text-sm text-muted-foreground">Customize your experience</p>
          </Link>

          <Link className="rounded-lg border border-border p-4 transition hover:bg-muted" href="/ratings">
            <h3 className="font-semibold">My Ratings</h3>
            <p className="text-sm text-muted-foreground">View rated content</p>
          </Link>
        </div>
      </div>
    </div>
  );
}
