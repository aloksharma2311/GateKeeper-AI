import { createClient } from "@/lib/supabase/server";

export class MembershipRepository {
  static async findMembership(
    organizationId: string,
    userId: string
  ) {
    const supabase = await createClient();

    const { data, error } = await supabase
      .from("organization_members")
      .select("*")
      .eq("organization_id", organizationId)
      .eq("user_id", userId)
      .maybeSingle();

    if (error) {
      throw error;
    }

    return data;
  }

  static async createOwnerMembership(
    organizationId: string,
    userId: string
  ) {
    const supabase = await createClient();

    const { data, error } = await supabase
      .from("organization_members")
      .insert({
        organization_id: organizationId,
        user_id: userId,
        role: "owner",
      })
      .select()
      .single();

    if (error) {
      throw error;
    }

    return data;
  }
}