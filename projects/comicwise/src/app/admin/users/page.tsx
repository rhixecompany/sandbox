import { getUsersAction } from "@/actions/admin/user.actions";
import { AdminUsersWrapper } from "@/components/admin/admin-users-wrapper";

export const metadata = {
  title: "Admin - Users",
};

export default async function AdminUsersPage() {
  const result = await getUsersAction();
  const users = result.ok ? result.data : [];
  return <AdminUsersWrapper users={users} />;
}
