"use client";
import { useEffect } from "react";

import { Button } from "@/components/ui/button";

export default function GlobalError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  useEffect(() => {
    console.error("[GlobalError]", error);
  }, [error]);

  return (
    <html lang="en">
      <body>
        <div className="flex min-h-screen flex-col items-center justify-center gap-4">
          <h2 className="text-2xl font-bold">Something went wrong!</h2>
          <p className="text-muted-foreground">{error.message}</p>
          {error.digest && <p className="text-xs text-muted-foreground">Error ID: {error.digest}</p>}
          <Button onClick={reset}>Try again</Button>
        </div>
      </body>
    </html>
  );
}
