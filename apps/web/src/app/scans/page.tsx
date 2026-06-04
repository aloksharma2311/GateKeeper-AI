import Link from "next/link";

import { ScansService } from "@/features/scans/services/scans.service";
import { uploadScreenshot } from "@/features/scans/actions/upload-scan.action";

export default async function ScansPage() {
  const scans = await ScansService.getScans();

  return (
    <main className="p-8">
      <h1 className="mb-6 text-3xl font-bold">Scans</h1>

      <form action={uploadScreenshot} className="mb-8">
        <input type="file" name="file" required />

        <button
          className="
            ml-2
            rounded
            bg-black
            px-4
            py-2
            text-white
          "
        >
          Upload
        </button>
      </form>

      <div className="space-y-4">
        {scans.map((scan: any) => (
          <div
            key={scan.id}
            className="
                rounded
                border
                p-4
              "
          >
            <p className="font-medium">{scan.file_name}</p>

            <p>Status: {scan.status}</p>

            <p>Threat: {scan.threat_score}</p>

            <div
              className="
                  mt-3
                  flex
                  gap-2
                "
            >
              <Link
                href={`/results/${scan.id}`}
                className="
                    rounded
                    bg-green-600
                    px-3
                    py-2
                    text-white
                  "
              >
                Results
              </Link>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
