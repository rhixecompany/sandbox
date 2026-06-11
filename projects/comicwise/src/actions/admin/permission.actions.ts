"use server";

import { auth } from "@/auth";
import { permissionDal } from "@/dal/permission-dal";
import type { ActionResult } from "@/types/actions-types";

type PermissionType = Awaited<ReturnType<typeof permissionDal.list>>[number];

export async function getPermissionsAction(): Promise<ActionResult<PermissionType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const permissions = await permissionDal.list({ limit: 100 });
    return { ok: true, data: permissions };
  } catch (error) {
    console.error("[getPermissionsAction]", error);
    return { ok: false, error: "Failed to fetch permissions" };
  }
}
