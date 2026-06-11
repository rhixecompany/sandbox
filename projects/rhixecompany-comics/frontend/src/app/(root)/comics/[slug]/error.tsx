/**
 * Comic Details Page Error Boundary
 * Handles errors that occur during comic details page rendering
 */

"use client";

import { AlertTriangle } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface ComicDetailsErrorProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function ComicDetailsError({ error, reset }: ComicDetailsErrorProps) {
  return (
    <main className="flex min-h-screen items-center justify-center bg-background px-4">
      <div className="max-w-md text-center">
        <div className="mb-4 flex justify-center">
          <div className="rounded-full bg-red-100 p-3">
            <AlertTriangle className="h-8 w-8 text-red-600" />
          </div>
        </div>

        <h1 className="mb-2 text-2xl font-bold">Comic Not Found</h1>
        <p className="mb-6 text-muted-foreground">
          {error.message ||
            "The comic you're looking for couldn't be found. It may have been removed or is temporarily unavailable."}
        </p>

        {error.digest && <p className="mb-4 text-xs text-muted-foreground">Error ID: {error.digest}</p>}

        <div className="flex flex-wrap justify-center gap-3">
          <Button onClick={reset} variant="default">
            Try Again
          </Button>
          <Button asChild variant="outline">
            <Link href="/comics">Back to Comics</Link>
          </Button>
        </div>
      </div>
    </main>
  );
}
