"use client";

interface AdminChaptersWrapperProps {
  children?: React.ReactNode;
}

export function AdminChaptersWrapper({ children }: AdminChaptersWrapperProps) {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Admin - Chapters Management</h1>
      <p className="mt-2 text-muted-foreground">Coming soon...</p>
      {children}
    </div>
  );
}
