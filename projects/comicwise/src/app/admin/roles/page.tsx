/**
 * Roles Admin Page
 * Route: /admin/roles
 */

import { getRolesAction } from "@/actions/rbac.actions";
import { AdminRolesWrapper } from "@/components/admin/admin-roles-wrapper";

export const metadata = {
  title: "Admin - Roles Management",
};

export default async function RolesPage() {
  const result = await getRolesAction();
  const roles = result.ok ? result.data : [];

  return <AdminRolesWrapper roles={roles} />;
}
