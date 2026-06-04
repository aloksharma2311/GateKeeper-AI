from collections import Counter

from app.repositories.dashboard_repository import (
    DashboardRepository,
)


class DashboardService:

    @staticmethod
    def get_summary(
        organization_id: str
    ):

        scans = (
            DashboardRepository
            .get_all_scans(
                organization_id
            )
        )

        classifications = (
            DashboardRepository
            .get_all_classifications(
                organization_id
            )
        )

        findings = (
            DashboardRepository
            .get_all_findings(
                organization_id
            )
        )

        total_scans = len(scans)

        critical = len([
            s for s in scans
            if (
                s.get(
                    "threat_score",
                    0
                ) >= 75
            )
        ])

        high = len([
            s for s in scans
            if (
                50 <=
                s.get(
                    "threat_score",
                    0
                ) < 75
            )
        ])

        medium = len([
            s for s in scans
            if (
                25 <=
                s.get(
                    "threat_score",
                    0
                ) < 50
            )
        ])

        low = len([
            s for s in scans
            if (
                s.get(
                    "threat_score",
                    0
                ) < 25
            )
        ])

        scam_types = Counter()

        for item in classifications:

            scam_types[
                item["scam_type"]
            ] += 1

        brand_counter = Counter()

        indicator_counter = Counter()

        for item in findings:

            finding_type = (
                item[
                    "finding_type"
                ]
            )

            finding_value = (
                item[
                    "finding_value"
                ]
            )

            indicator_counter[
                finding_type
            ] += 1

            if (
                finding_type
                == "brand"
            ):
                brand_counter[
                    finding_value
                ] += 1

        recent_scans = sorted(
            scans,
            key=lambda x:
                x["created_at"],
            reverse=True
        )[:10]

        return {

            "summary": {
                "total_scans":
                    total_scans,
                "critical":
                    critical,
                "high":
                    high,
                "medium":
                    medium,
                "low":
                    low,
            },

            "scam_types":
                dict(
                    scam_types
                ),

            "top_brands": [
                {
                    "brand": brand,
                    "count": count
                }
                for brand, count
                in brand_counter.most_common(
                    5
                )
            ],

            "top_indicators": [
                {
                    "indicator":
                        indicator,
                    "count":
                        count
                }
                for indicator, count
                in indicator_counter.most_common(
                    10
                )
            ],

            "recent_scans":
                recent_scans,
        }