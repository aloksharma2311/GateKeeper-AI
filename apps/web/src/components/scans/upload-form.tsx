"use client";

import { useState } from "react";

import { uploadScreenshot } from "@/features/scans/actions/upload-scan.action";

export function UploadForm() {
  const [loading, setLoading] =
    useState(false);

  return (
    <form
      action={async (
        formData
      ) => {
        setLoading(true);

        try {
          await uploadScreenshot(
            formData
          );

          alert(
            "Upload successful"
          );
        } catch (
          error
        ) {
          alert(
            error instanceof Error
              ? error.message
              : "Upload failed"
          );
        } finally {
          setLoading(false);
        }
      }}
      className="space-y-4"
    >
      <input
        type="file"
        name="file"
        accept="image/*"
        required
      />

      <button
        type="submit"
        disabled={loading}
        className="rounded-md bg-black px-4 py-2 text-white"
      >
        {loading
          ? "Uploading..."
          : "Upload Screenshot"}
      </button>
    </form>
  );
}