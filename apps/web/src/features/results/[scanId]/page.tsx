import { ResultsService } from "@/features/results/services/results.service";

export default async function ResultsPage({
  params,
}: {
  params: Promise<{
    scanId: string;
  }>;
}) {

  const { scanId } =
    await params;

  const result =
    await ResultsService.getScanResult(
      scanId
    );

  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold">
        Analysis Result
      </h1>

      <pre>
        {JSON.stringify(
          result,
          null,
          2
        )}
      </pre>
    </main>
  );
}