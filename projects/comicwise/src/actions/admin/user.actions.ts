"use server";

import { auth } from "@/auth";
import { userDal } from "@/dal/user-dal";
import type { ActionResult } from "@/types/actions-types";

type UserType = Awaited<ReturnType<typeof userDal.list>>[number];

export async function getUsersAction(): Promise<ActionResult<UserType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const users = await userDal.list({ limit: 50 });
    return { ok: true, data: users };
  } catch (error) {
    console.error("[getUsersAction]", error);
    return { ok: false, error: "Failed to fetch users" };
  }
}
