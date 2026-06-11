"use client";

import Link from "next/link";

export default function NotFoundPage() {
  return (
    <main className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <h1 className="text-2xl font-bold">Page not found</h1>
        <p className="mt-2">The requested page could not be found.</p>
        <p className="mt-4">
          <Link href="/">Go back home</Link>
        </p>
      </div>
    </main>
  );
}
