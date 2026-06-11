"use client";

import { IconDotsVertical, IconLogout, IconSettings, IconUserCircle } from "@tabler/icons-react";
import { useTransition } from "react";

import { signOutAction } from "@/actions/auth.actions";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { SidebarMenu, SidebarMenuButton, SidebarMenuItem, useSidebar } from "@/components/ui/sidebar";

interface NavUserProps {
  user?: { avatar?: null | string; email?: null | string; name?: null | string } | null;
}

export function NavUser({ user }: NavUserProps) {
  const { isMobile } = useSidebar();
  const [, startTransition] = useTransition();

  if (!user) {
    return (
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton asChild size="lg">
            <a href="/sign-in">Sign In</a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    );
  }

  const handleSignOut = () => {
    startTransition(async () => {
      await signOutAction("/");
    });
  };

  return (
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton
              className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
              size="lg"
            >
              <Avatar className="h-8 w-8 rounded-lg grayscale">
                <AvatarImage alt={user.name || ""} src={user.avatar || undefined} />
                <AvatarFallback className="rounded-lg">{user.name?.[0] || "U"}</AvatarFallback>
              </Avatar>
              <div className="grid flex-1 text-start text-sm leading-tight">
                <span className="truncate font-medium">{user.name || "User"}</span>
                <span className="truncate text-xs text-muted-foreground">{user.email}</span>
              </div>
              <IconDotsVertical className="ms-auto size-4" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            align="end"
            className="w-(--radix-dropdown-menu-trigger-width) min-w-56 rounded-lg"
            side={isMobile ? "bottom" : "right"}
            sideOffset={4}
          >
            <DropdownMenuLabel className="p-0 font-normal">
              <div className="flex items-center gap-2 px-1 py-1.5 text-start text-sm">
                <Avatar className="h-8 w-8 rounded-lg">
                  <AvatarImage alt={user.name || ""} src={user.avatar || undefined} />
                  <AvatarFallback className="rounded-lg">{user.name?.[0] || "U"}</AvatarFallback>
                </Avatar>
                <div className="grid flex-1 text-start text-sm leading-tight">
                  <span className="truncate font-medium">{user.name || "User"}</span>
                  <span className="truncate text-xs text-muted-foreground">{user.email}</span>
                </div>
              </div>
            </DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuItem asChild>
              <a href="/profile">
                <IconUserCircle />
                Profile
              </a>
            </DropdownMenuItem>
            <DropdownMenuItem asChild>
              <a href="/profile/settings">
                <IconSettings />
                Settings
              </a>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem onClick={handleSignOut}>
              <IconLogout />
              Log out
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  );
}
