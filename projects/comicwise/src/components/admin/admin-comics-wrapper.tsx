"use client";

interface AdminComicsWrapperProps {
  children?: React.ReactNode;
}

export function AdminComicsWrapper({ children }: AdminComicsWrapperProps) {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Admin - Comics Management</h1>
      <p className="mt-2 text-muted-foreground">Coming soon...</p>
      {children}
    </div>
  );
}
