import { redirect } from "next/navigation";

import { auth } from "@/auth";
import { AppSidebar } from "@/components/layout/app-sidebar";
import { SiteHeader } from "@/components/layout/site-header";
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar";

import type { ReactNode } from "react";
export default async function AdminLayout({ children }: { children: ReactNode }) {
  const session = await auth();

  // Require authentication
  if (!session?.user) {
    redirect("/sign-in");
  }

  // Require admin role
  const user = session.user as { role?: unknown };
  if (typeof user?.role !== "string" || user.role !== "admin") {
    redirect("/");
  }

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as React.CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col">
          <div className="@container/main flex flex-1 flex-col gap-2">{children}</div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
}
