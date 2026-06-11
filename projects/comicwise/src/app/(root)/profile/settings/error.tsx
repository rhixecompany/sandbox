/**
 * Settings Page Error Boundary
 * Error UI for settings page
 */

"use client";

import { AlertCircle } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface SettingsErrorProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function SettingsError({ error, reset }: SettingsErrorProps) {
  return (
    <main className="flex min-h-screen items-center justify-center bg-background">
      <div className="mx-auto max-w-md space-y-6 px-4 text-center">
        <div className="flex justify-center">
          <AlertCircle className="h-16 w-16 text-destructive" />
        </div>

        <div className="space-y-2">
          <h1 className="text-3xl font-bold">Error loading settings</h1>
          <p className="text-muted-foreground">{error.message || "An error occurred while loading your settings"}</p>
        </div>

        <div className="rounded-lg bg-muted/50 p-4 font-mono text-sm text-muted-foreground">
          {error.digest && `Error ID: ${error.digest}`}
        </div>

        <div className="flex flex-wrap justify-center gap-4">
          <Button onClick={reset}>Try Again</Button>
          <Link href="/profile">
            <Button variant="outline">Back to Profile</Button>
          </Link>
        </div>
      </div>
    </main>
  );
}
