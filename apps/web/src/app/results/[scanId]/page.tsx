import { ResultsService } from "@/features/scans/services/results.service";

type Props = {
  params: Promise<{
    scanId: string;
  }>;
};

export default async function ResultPage({
  params,
}: Props) {
  const { scanId } = await params;

  const result =
    await ResultsService.getResult(
      scanId
    );

  const scan =
    result.scan;

  const findings =
    result.findings ?? [];

  const ocr =
    result.ocr;

  const classification =
    result.classification;

  const score =
    scan.threat_score;

  let riskLevel =
    "LOW";

  let riskColor =
    "bg-green-500";

  if (score >= 75) {
    riskLevel =
      "CRITICAL";

    riskColor =
      "bg-red-600";
  } else if (
    score >= 50
  ) {
    riskLevel =
      "HIGH";

    riskColor =
      "bg-orange-500";
  } else if (
    score >= 25
  ) {
    riskLevel =
      "MEDIUM";

    riskColor =
      "bg-yellow-500";
  }

  return (
    <main className="max-w-5xl mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">
        Scan Result
      </h1>

      {/* Summary */}

      <div className="border rounded p-6 mb-6">
        <h2 className="font-bold text-xl mb-4">
          Summary
        </h2>

        <div className="space-y-2">
          <p>
            <strong>Status:</strong>{" "}
            {scan.status}
          </p>

          <p>
            <strong>
              Threat Score:
            </strong>{" "}
            {scan.threat_score}
            /100
          </p>

          <div className="flex items-center gap-2">
            <strong>
              Risk Level:
            </strong>

            <span
              className={`
                ${riskColor}
                text-white
                px-3
                py-1
                rounded-full
                text-sm
                font-semibold
              `}
            >
              {riskLevel}
            </span>
          </div>

          <p>
            <strong>File:</strong>{" "}
            {scan.file_name}
          </p>
        </div>
      </div>

      {/* Intelligence Report */}

      <div className="border rounded p-6 mb-6">
        <h2 className="font-bold text-xl mb-4">
          AI Scam Classification
        </h2>

        {classification ? (
          <div className="space-y-4">

            <div>
              <p className="text-sm text-gray-500">
                Scam Type
              </p>

              <h3 className="text-2xl font-bold text-red-600">
                {
                  classification.scam_type
                }
              </h3>
            </div>

            <div>
              <p className="text-sm text-gray-500 mb-2">
                Confidence
              </p>

              <div className="w-full bg-gray-200 rounded-full h-4">
                <div
                  className="
                    bg-red-600
                    h-4
                    rounded-full
                  "
                  style={{
                    width: `${classification.confidence}%`,
                  }}
                />
              </div>

              <p className="mt-2 font-medium">
                {
                  classification.confidence
                }
                %
              </p>
            </div>

            <div>
              <p className="text-sm text-gray-500 mb-2">
                Indicators
              </p>

              <ul className="list-disc pl-6 space-y-1">

                {Array.isArray(
                  classification.explanation
                ) ? (
                  classification.explanation.map(
                    (
                      item: string,
                      index: number
                    ) => (
                      <li key={index}>
                        {item}
                      </li>
                    )
                  )
                ) : (
                  <li>
                    {
                      classification.explanation
                    }
                  </li>
                )}

              </ul>
            </div>

          </div>
        ) : (
          <p className="text-gray-500">
            No classification available.
          </p>
        )}
      </div>

      {/* Threat Findings */}

      <div className="border rounded p-6 mb-6">
        <h2 className="font-bold text-xl mb-4">
          Detected Threats
        </h2>

        {findings.length === 0 ? (
          <div className="text-green-600 font-medium">
            No threats detected.
          </div>
        ) : (
          <div className="space-y-3">

            {findings.map(
              (finding: any) => (
                <div
                  key={finding.id}
                  className="
                    border
                    rounded
                    p-4
                    bg-gray-50
                  "
                >
                  <div className="font-semibold text-red-600 capitalize">
                    {
                      finding.finding_type
                    }
                  </div>

                  <div className="mt-1">
                    {
                      finding.finding_value
                    }
                  </div>

                  <div className="text-sm text-gray-500 mt-1">
                    Confidence:{" "}
                    {
                      finding.confidence
                    }
                    %
                  </div>
                </div>
              )
            )}

          </div>
        )}
      </div>

      {/* OCR Output */}

      <div className="border rounded p-6">
        <h2 className="font-bold text-xl mb-4">
          OCR Extracted Text
        </h2>

        <pre
          className="
            whitespace-pre-wrap
            text-sm
            bg-gray-50
            p-4
            rounded
            overflow-auto
          "
        >
          {ocr?.extracted_text ??
            "No OCR text available"}
        </pre>
      </div>
    </main>
  );
}