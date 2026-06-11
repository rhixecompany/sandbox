"use server";
import { desc, eq } from "drizzle-orm";
import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { notificationDal } from "@/dal/notification-dal";
import { db } from "@/database/db";
import { notification } from "@/database/schema";
import type { ActionResult } from "@/types/actions-types";

export async function markNotificationReadAction(id: number): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id) return { ok: false, error: "Not authenticated" };
  try {
    await notificationDal.markRead(id);
    revalidatePath("/notifications");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[markNotificationReadAction]", e);
    return { ok: false, error: "Failed to mark notification as read" };
  }
}

export async function markAllNotificationsReadAction(): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id) return { ok: false, error: "Not authenticated" };
  try {
    await notificationDal.markAllRead(session.user.id);
    revalidatePath("/notifications");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[markAllNotificationsReadAction]", e);
    return { ok: false, error: "Failed to mark notifications as read" };
  }
}

export async function getNotificationsAction(): Promise<ActionResult<(typeof notification.$inferSelect)[]>> {
  const session = await auth();
  if (!session?.user?.id) return { ok: false, error: "Not authenticated" };
  try {
    const notifications = await db
      .select()
      .from(notification)
      .where(eq(notification.userId, session.user.id))
      .orderBy(desc(notification.createdAt))
      .limit(50);
    return { ok: true, data: notifications };
  } catch (error) {
    console.error("[getNotificationsAction]", error);
    return { ok: false, error: "Failed to fetch notifications" };
  }
}
