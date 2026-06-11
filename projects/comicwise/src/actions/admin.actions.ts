"use server";
import { revalidatePath } from "next/cache.js";
import { z } from "zod";

import { auth } from "@/auth";
import { userDal } from "@/dal/user-dal";
import type { ActionResult } from "@/types/actions-types";

async function requireAdmin() {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    throw new Error("Forbidden");
  }
  return session!;
}

const UpdateRoleSchema = z.object({
  userId: z.string().min(1),
  role: z.enum(["user", "admin", "moderator"]),
});

export async function updateUserRoleAction(input: unknown): Promise<ActionResult<void>> {
  try {
    await requireAdmin();
  } catch {
    return { ok: false, error: "Forbidden" };
  }
  const parsed = UpdateRoleSchema.safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    await userDal.updateRole(parsed.data.userId, parsed.data.role);
    revalidatePath("/admin/users");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[updateUserRoleAction]", e);
    return { ok: false, error: "Failed to update user role" };
  }
}

export async function deleteUserAction(userId: string): Promise<ActionResult<void>> {
  try {
    await requireAdmin();
  } catch {
    return { ok: false, error: "Forbidden" };
  }
  try {
    await userDal.delete(userId);
    revalidatePath("/admin/users");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteUserAction]", e);
    return { ok: false, error: "Failed to delete user" };
  }
}
