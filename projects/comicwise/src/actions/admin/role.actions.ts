"use server";

import { auth } from "@/auth";
import { roleDal } from "@/dal/role-dal";
import type { ActionResult } from "@/types/actions-types";

type RoleType = Awaited<ReturnType<typeof roleDal.list>>[number];

export async function getRolesAction(): Promise<ActionResult<RoleType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const roles = await roleDal.list({ limit: 50 });
    return { ok: true, data: roles };
  } catch (error) {
    console.error("[getRolesAction]", error);
    return { ok: false, error: "Failed to fetch roles" };
  }
}
