/**
 * Permissions Admin Page
 * Route: /admin/permissions
 */

import { getPermissionsAction } from "@/actions/rbac.actions";
import { AdminPermissionsWrapper } from "@/components/admin/admin-permissions-wrapper";

export const metadata = {
  title: "Admin - Permissions Management",
};

export default async function PermissionsPage() {
  const result = await getPermissionsAction();
  const permissions = result.ok ? result.data : [];

  return <AdminPermissionsWrapper permissions={permissions} />;
}
