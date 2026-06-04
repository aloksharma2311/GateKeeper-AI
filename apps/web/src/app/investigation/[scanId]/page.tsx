import {
  InvestigationService
} from "@/features/investigation/services/investigation.service";

export default async function InvestigationPage({
  params,
}: {
  params: Promise<{
    scanId: string;
  }>;
}) {

  const { scanId } =
    await params;

  const data =
    await InvestigationService.getInvestigation(
      scanId
    );

  const threatScore =
    data.scan?.threat_score || 0;

  const riskLevel =
    data.report?.risk_level || "UNKNOWN";

  return (

    <main className="min-h-screen bg-zinc-950 text-white p-8">

      {/* Header */}

      <div className="mb-8">

        <h1 className="text-4xl font-bold">
          Investigation Report
        </h1>

        <p className="text-zinc-400 mt-2">
          Scan ID: {scanId}
        </p>

      </div>

      {/* Summary Cards */}

      <div className="grid grid-cols-3 gap-6 mb-8">

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <p className="text-zinc-400">
            Threat Score
          </p>

          <h2 className="text-5xl font-bold mt-2">
            {threatScore}
          </h2>

        </div>

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <p className="text-zinc-400">
            Risk Level
          </p>

          <h2
            className={
              riskLevel === "CRITICAL"
                ? "text-red-500 text-4xl font-bold mt-2"
                : riskLevel === "HIGH"
                ? "text-orange-500 text-4xl font-bold mt-2"
                : riskLevel === "MEDIUM"
                ? "text-yellow-500 text-4xl font-bold mt-2"
                : "text-green-500 text-4xl font-bold mt-2"
            }
          >
            {riskLevel}
          </h2>

        </div>

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <p className="text-zinc-400">
            Scam Type
          </p>

          <h2 className="text-2xl font-bold mt-2">
            {data.classification?.scam_type}
          </h2>

        </div>

      </div>

      {/* Executive Summary */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
        mb-8
      ">

        <h2 className="text-2xl font-bold mb-4">
          Executive Summary
        </h2>

        <p className="text-zinc-300">
          {data.report?.summary}
        </p>

      </div>

      {/* Attack Vectors */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
        mb-8
      ">

        <h2 className="text-2xl font-bold mb-4">
          Attack Vectors
        </h2>

        <div className="flex flex-wrap gap-3">

          {data.report?.attack_vectors?.map(
            (
              vector: string,
              index: number
            ) => (

              <span
                key={index}
                className="
                  px-4
                  py-2
                  rounded-full
                  bg-red-900
                  text-red-300
                "
              >
                {vector}
              </span>

            )
          )}

        </div>

      </div>

      {/* Recommendations */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
        mb-8
      ">

        <h2 className="text-2xl font-bold mb-4">
          Recommended Actions
        </h2>

        <ul className="space-y-3">

          {data.report?.recommended_actions?.map(
            (
              action: string,
              index: number
            ) => (

              <li
                key={index}
                className="
                  border
                  border-zinc-800
                  rounded-lg
                  p-3
                "
              >
                {action}
              </li>

            )
          )}

        </ul>

      </div>

      {/* Findings */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
        mb-8
      ">

        <h2 className="text-2xl font-bold mb-4">
          Findings
        </h2>

        <div className="space-y-3">

          {data.findings?.map(
            (finding: any) => (

              <div
                key={finding.id}
                className="
                  border
                  border-zinc-800
                  rounded-lg
                  p-3
                "
              >

                <div className="font-bold">
                  {finding.finding_type}
                </div>

                <div className="text-zinc-400">
                  {finding.finding_value}
                </div>

              </div>

            )
          )}

        </div>

      </div>

      {/* IOC Table */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
        mb-8
      ">

        <h2 className="text-2xl font-bold mb-4">
          Indicators of Compromise
        </h2>

        <table className="w-full">

          <thead>

            <tr className="border-b border-zinc-800">

              <th className="text-left p-3">
                Type
              </th>

              <th className="text-left p-3">
                Value
              </th>

            </tr>

          </thead>

          <tbody>

            {data.iocs?.map(
              (ioc: any) => (

                <tr
                  key={ioc.id}
                  className="border-b border-zinc-800"
                >

                  <td className="p-3">
                    {ioc.indicator_type}
                  </td>

                  <td className="p-3">
                    {ioc.indicator_value}
                  </td>

                </tr>

              )
            )}

          </tbody>

        </table>

      </div>

      {/* MITRE */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
      ">

        <h2 className="text-2xl font-bold mb-4">
          MITRE ATT&CK Mapping
        </h2>

        <div className="grid grid-cols-2 gap-4">

          {data.mitre?.map(
            (technique: any) => (

              <div
                key={technique.id}
                className="
                  border
                  border-zinc-800
                  rounded-lg
                  p-4
                "
              >

                <div className="text-red-400 font-bold">
                  {technique.technique_id}
                </div>

                <div className="text-zinc-300">
                  {technique.technique_name}
                </div>

              </div>

            )
          )}

        </div>

      </div>

    </main>
  );
}