"use client";

import { AlertTriangle } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface ComicsErrorProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function ComicsError({ error, reset }: ComicsErrorProps) {
  return (
    <main className="flex min-h-screen items-center justify-center bg-background px-4">
      <div className="max-w-md text-center">
        <div className="mb-4 flex justify-center">
          <div className="rounded-full bg-red-100 p-3">
            <AlertTriangle className="h-8 w-8 text-red-600" />
          </div>
        </div>

        <h1 className="mb-2 text-2xl font-bold">Unable to Load Comics</h1>
        <p className="mb-6 text-muted-foreground">
          {error.message || "An error occurred while trying to load the comics. Please try again."}
        </p>

        {error.digest && <p className="mb-4 text-xs text-muted-foreground">Error ID: {error.digest}</p>}

        <div className="flex flex-wrap justify-center gap-3">
          <Button onClick={reset} variant="default">
            Try Again
          </Button>
          <Button asChild variant="outline">
            <Link href="/">Go Home</Link>
          </Button>
        </div>
      </div>
    </main>
  );
}
