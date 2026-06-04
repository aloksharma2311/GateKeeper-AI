import { createClient } from "@/lib/supabase/server";

export class OrganizationRepository {
  static async findByOwner(userId: string) {
    const supabase = await createClient();

    const { data, error } = await supabase
      .from("organizations")
      .select("*")
      .eq("owner_id", userId)
      .maybeSingle();

    return data;
  }

  static async create(name: string, slug: string, ownerId: string) {
    const supabase = await createClient();

    const { data, error } = await supabase
      .from("organizations")
      .insert({
        name,
        slug,
        owner_id: ownerId,
      })
      .select()
      .single();

    if (error) {
      throw error;
    }

    return data;
  }
}
