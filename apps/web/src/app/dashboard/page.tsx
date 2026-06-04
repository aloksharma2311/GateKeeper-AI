import Link from "next/link";

import {
  DashboardService
} from "@/features/dashboard/services/dashboard.service";

export default async function DashboardPage() {

  const stats =
    await DashboardService.getStats();

  return (

    <main className="min-h-screen bg-zinc-950 text-white p-8">

      {/* Header */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold">
          🛡️ GateKeeper AI
        </h1>

        <p className="text-zinc-400 mt-2">
          Cybercrime Detection & Investigation Platform
        </p>

      </div>

      {/* KPI Cards */}

      <div className="grid grid-cols-4 gap-6 mb-8">

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <p className="text-zinc-400">
            Total Scans
          </p>

          <h2 className="text-5xl font-bold mt-2">
            {stats.summary.total_scans}
          </h2>

        </div>

        <div className="
          bg-red-950
          border border-red-800
          rounded-xl
          p-6
        ">

          <p className="text-red-400">
            Critical
          </p>

          <h2 className="text-5xl font-bold text-red-500 mt-2">
            {stats.summary.critical}
          </h2>

        </div>

        <div className="
          bg-orange-950
          border border-orange-800
          rounded-xl
          p-6
        ">

          <p className="text-orange-400">
            High
          </p>

          <h2 className="text-5xl font-bold text-orange-500 mt-2">
            {stats.summary.high}
          </h2>

        </div>

        <div className="
          bg-yellow-950
          border border-yellow-800
          rounded-xl
          p-6
        ">

          <p className="text-yellow-400">
            Medium
          </p>

          <h2 className="text-5xl font-bold text-yellow-500 mt-2">
            {stats.summary.medium}
          </h2>

        </div>

      </div>

      {/* Analytics */}

      <div className="grid grid-cols-3 gap-6 mb-8">

        {/* Scam Types */}

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <h2 className="text-xl font-bold mb-4">
            Scam Types
          </h2>

          <div className="space-y-3">

            {Object.entries(
              stats.scam_types
            ).map(
              ([type, count]) => (

                <div
                  key={type}
                  className="
                    flex
                    justify-between
                  "
                >

                  <span>
                    {type}
                  </span>

                  <span className="font-bold">
                    {count as number}
                  </span>

                </div>

              )
            )}

          </div>

        </div>

        {/* Brands */}

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <h2 className="text-xl font-bold mb-4">
            Top Targeted Brands
          </h2>

          <div className="space-y-3">

            {stats.top_brands.map(
              (
                item: any,
                index: number
              ) => (

                <div
                  key={index}
                  className="
                    flex
                    justify-between
                  "
                >

                  <span>
                    {item.brand}
                  </span>

                  <span className="font-bold">
                    {item.count}
                  </span>

                </div>

              )
            )}

          </div>

        </div>

        {/* Indicators */}

        <div className="
          bg-zinc-900
          border border-zinc-800
          rounded-xl
          p-6
        ">

          <h2 className="text-xl font-bold mb-4">
            Top Indicators
          </h2>

          <div className="space-y-3">

            {stats.top_indicators.map(
              (
                item: any,
                index: number
              ) => (

                <div
                  key={index}
                  className="
                    flex
                    justify-between
                  "
                >

                  <span>
                    {item.indicator}
                  </span>

                  <span className="font-bold">
                    {item.count}
                  </span>

                </div>

              )
            )}

          </div>

        </div>

      </div>

      {/* Recent Investigations */}

      <div className="
        bg-zinc-900
        border border-zinc-800
        rounded-xl
        p-6
      ">

        <h2 className="text-2xl font-bold mb-6">
          Recent Investigations
        </h2>

        <table className="w-full">

          <thead>

            <tr className="border-b border-zinc-700">

              <th className="text-left p-3">
                File
              </th>

              <th className="text-left p-3">
                Threat Score
              </th>

              <th className="text-left p-3">
                Status
              </th>

              <th className="text-left p-3">
                Action
              </th>

            </tr>

          </thead>

          <tbody>

            {stats.recent_scans.map(
              (scan: any) => (

                <tr
                  key={scan.id}
                  className="
                    border-b
                    border-zinc-800
                  "
                >

                  <td className="p-3">
                    {scan.file_name}
                  </td>

                  {/* Threat Score */}

                  <td className="p-3">

                    <span
                      className={
                        scan.threat_score >= 75
                          ? "text-red-500 font-bold"
                          : scan.threat_score >= 50
                          ? "text-orange-500 font-bold"
                          : scan.threat_score >= 25
                          ? "text-yellow-500 font-bold"
                          : "text-green-500 font-bold"
                      }
                    >
                      {scan.threat_score}
                    </span>

                  </td>

                  {/* Status */}

                  <td className="p-3">

                    <span
                      className={
                        scan.status === "completed"
                          ? `
                            px-3
                            py-1
                            rounded-full
                            bg-green-900
                            text-green-300
                            text-sm
                          `
                          : `
                            px-3
                            py-1
                            rounded-full
                            bg-yellow-900
                            text-yellow-300
                            text-sm
                          `
                      }
                    >
                      {scan.status}
                    </span>

                  </td>

                  <td className="p-3">

                    <Link
                      href={`/investigation/${scan.id}`}
                      className="
                        bg-blue-600
                        hover:bg-blue-700
                        px-4
                        py-2
                        rounded-lg
                        text-white
                        font-medium
                      "
                    >
                      Investigate
                    </Link>

                  </td>

                </tr>

              )
            )}

          </tbody>

        </table>

      </div>

    </main>
  );
}