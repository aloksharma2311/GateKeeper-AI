from app.core.supabase import supabase


class DashboardRepository:

    @staticmethod
    def get_all_scans(
        organization_id: str
    ):
        result = (
            supabase
            .table("scans")
            .select("*")
            .eq(
                "organization_id",
                organization_id
            )
            .execute()
        )

        return result.data or []

    @staticmethod
    def get_all_classifications(
        organization_id: str
    ):

        scans = (
            supabase
            .table("scans")
            .select("id")
            .eq(
                "organization_id",
                organization_id
            )
            .execute()
        )

        scan_ids = [
            scan["id"]
            for scan in (scans.data or [])
        ]

        if not scan_ids:
            return []

        result = (
            supabase
            .table(
                "scan_classifications"
            )
            .select(
                "scam_type, scan_id"
            )
            .in_(
                "scan_id",
                scan_ids
            )
            .execute()
        )

        return result.data or []

    @staticmethod
    def get_all_findings(
        organization_id: str
    ):

        scans = (
            supabase
            .table("scans")
            .select("id")
            .eq(
                "organization_id",
                organization_id
            )
            .execute()
        )

        scan_ids = [
            scan["id"]
            for scan in (scans.data or [])
        ]

        if not scan_ids:
            return []

        result = (
            supabase
            .table(
                "threat_findings"
            )
            .select(
                "finding_type, finding_value"
            )
            .in_(
                "scan_id",
                scan_ids
            )
            .execute()
        )

        return result.data or []