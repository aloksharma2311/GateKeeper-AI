"use server";

import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export async function signIn(
  email: string,
  password: string
) {
  const supabase = await createClient();

  const { error } =
    await supabase.auth.signInWithPassword({
      email,
      password,
    });

  if (error) {
    return {
      success: false,
      message: error.message,
    };
  }

  redirect("/dashboard");
}

export async function signUp(
  email: string,
  password: string
) {
  const supabase = await createClient();

  const { data, error } =
    await supabase.auth.signUp({
      email,
      password,
    });

  if (error) {
    return {
      success: false,
      message: error.message,
    };
  }

  redirect("/auth/login");
}

export async function signOut() {
  const supabase = await createClient();

  await supabase.auth.signOut();

  redirect("/auth/login");
}