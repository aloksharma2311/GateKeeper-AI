"use server";

import { redirect } from "next/navigation";

export async function analyzeScan(
  scanId: string
) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/api/v1/scans/process/${scanId}`,
    {
      method: "POST",
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error(
      "Analysis failed"
    );
  }

  redirect(
    `/results/${scanId}`
  );
}