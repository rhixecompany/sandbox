/**
 * RBAC Server Actions
 * Handle role and permission management
 */

"use server";

import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { auditLogDal } from "@/dal/audit-log-dal";
import { permissionDal } from "@/dal/permission-dal";
import { roleDal } from "@/dal/role-dal";
import { userRoleDal } from "@/dal/user-role-dal";
import {
  assignRoleSchema,
  createPermissionSchema,
  createRoleSchema,
  removeRoleSchema,
  updateRoleSchema,
} from "@/schemas/rbac.schema";

import type { ActionResult } from "@/types/actions-types";

export async function createRoleAction(input: unknown): Promise<ActionResult<{ roleId: number }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = createRoleSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const role = await roleDal.create(parsed.data);

    await auditLogDal.create({
      userId: session.user.id,
      action: "create",
      resource: "role",
      resourceId: String(role.id),
      details: { name: role.name },
    });

    revalidatePath("/admin/roles");

    return { ok: true, data: { roleId: role.id } };
  } catch {
    return { ok: false, error: "Failed to create role" };
  }
}

export async function updateRoleAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = updateRoleSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const { id, ...data } = parsed.data;
    await roleDal.update(id, data);

    await auditLogDal.create({
      userId: session.user.id,
      action: "update",
      resource: "role",
      resourceId: String(id),
      details: data,
    });

    revalidatePath("/admin/roles");

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to update role" };
  }
}

export async function deleteRoleAction(id: number): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    await roleDal.delete(id);

    await auditLogDal.create({
      userId: session.user.id,
      action: "delete",
      resource: "role",
      resourceId: String(id),
    });

    revalidatePath("/admin/roles");

    return { ok: true, data: { success: true } };
  } catch (error) {
    if (error instanceof Error && error.message.includes("system role")) {
      return { ok: false, error: "Cannot delete system role" };
    }
    return { ok: false, error: "Failed to delete role" };
  }
}

export async function createPermissionAction(input: unknown): Promise<ActionResult<{ permissionId: number }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = createPermissionSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const permission = await permissionDal.create(parsed.data);

    await auditLogDal.create({
      userId: session.user.id,
      action: "create",
      resource: "permission",
      resourceId: String(permission.id),
      details: { name: permission.name },
    });

    revalidatePath("/admin/permissions");

    return { ok: true, data: { permissionId: permission.id } };
  } catch {
    return { ok: false, error: "Failed to create permission" };
  }
}

export async function assignRoleAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = assignRoleSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    await userRoleDal.create({
      ...parsed.data,
      assignedBy: session.user.id,
    });

    await auditLogDal.create({
      userId: session.user.id,
      action: "assign_role",
      resource: "user",
      resourceId: parsed.data.userId,
      details: { roleId: parsed.data.roleId },
    });

    revalidatePath("/admin/users");

    return { ok: true, data: { success: true } };
  } catch (error) {
    if (error instanceof Error && error.message.includes("already has")) {
      return { ok: false, error: "User already has this role" };
    }
    return { ok: false, error: "Failed to assign role" };
  }
}

export async function removeRoleAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = removeRoleSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    await userRoleDal.removeRole(parsed.data.userId, parsed.data.roleId);

    await auditLogDal.create({
      userId: session.user.id,
      action: "remove_role",
      resource: "user",
      resourceId: parsed.data.userId,
      details: { roleId: parsed.data.roleId },
    });

    revalidatePath("/admin/users");

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to remove role" };
  }
}

interface RoleType {
  description: null | string;
  id: number;
  isSystem: boolean;
  name: string;
}

export async function getRolesAction(): Promise<ActionResult<RoleType[]>> {
  try {
    const roles = await roleDal.list();
    return { ok: true, data: roles };
  } catch {
    return { ok: false, error: "Failed to get roles" };
  }
}

interface PermissionType {
  action: string;
  description: null | string;
  id: number;
  name: string;
  resource: string;
}

export async function getPermissionsAction(): Promise<ActionResult<PermissionType[]>> {
  try {
    const permissions = await permissionDal.list();
    return { ok: true, data: permissions };
  } catch {
    return { ok: false, error: "Failed to get permissions" };
  }
}
