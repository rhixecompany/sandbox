"use client";

import { IconChartBar, IconLayoutDashboard, IconSearch, IconSettings, IconStar, IconUsers } from "@tabler/icons-react";
import { useSession } from "next-auth/react";
import Link from "next/link";

import { NavMain } from "@/components/layout/nav-main";
import { NavSecondary } from "@/components/layout/nav-secondary";
import { NavUser } from "@/components/layout/nav-user";
import { NotificationBell } from "@/components/notifications/notification-bell";
import { ThemeToggle } from "@/components/theme/theme-toggle";
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar";

const adminNavItems = [
  {
    title: "Dashboard",
    url: "/admin",
    icon: IconLayoutDashboard,
  },
  {
    title: "Manage Comics",
    url: "/admin/comics",
    icon: IconChartBar,
  },
  {
    title: "Manage Users",
    url: "/admin/users",
    icon: IconUsers,
  },
  {
    title: "Analytics",
    url: "/admin/analytics",
    icon: IconChartBar,
  },
];

const userNavItems = [
  {
    title: "My Bookmarks",
    url: "/bookmarks",
    icon: IconStar,
  },
  {
    title: "My Ratings",
    url: "/ratings",
    icon: IconStar,
  },
];

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  const { data: session } = useSession();
  const user = session?.user as
    | { email?: null | string; image?: null | string; name?: null | string; role?: string }
    | null
    | undefined;
  const isAdmin = user?.role === "admin";

  return (
    <Sidebar collapsible="offcanvas" {...props}>
      <SidebarHeader>
        <div className="flex items-center justify-between gap-2 px-2">
          <SidebarMenu>
            <SidebarMenuItem>
              <SidebarMenuButton asChild className="data-[slot=sidebar-menu-button]:p-1.5!">
                <Link href="/">
                  <span className="text-base font-semibold">Comicwise.</span>
                </Link>
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
          <div className="flex items-center gap-2">
            <ThemeToggle />
            {user && <NotificationBell />}
          </div>
        </div>
      </SidebarHeader>
      <SidebarContent>
        {user && isAdmin && <NavMain items={adminNavItems} />}
        {user && <NavMain items={userNavItems} />}
        <NavSecondary
          className="mt-auto"
          items={[
            { title: "Search", url: "/search", icon: IconSearch },
            { title: "Settings", url: "/settings", icon: IconSettings },
          ]}
        />
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={user} />
      </SidebarFooter>
    </Sidebar>
  );
}
