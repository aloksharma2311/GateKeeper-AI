from app.core.supabase import supabase


class ScanRepository:

    @staticmethod
    def get_by_id(scan_id: str):
        response = (
            supabase
            .table("scans")
            .select("*")
            .eq("id", scan_id)
            .single()
            .execute()
        )

        return response.data

    @staticmethod
    def update_status(
        scan_id: str,
        status: str
    ):
        response = (
            supabase
            .table("scans")
            .update({
                "status": status
            })
            .eq("id", scan_id)
            .execute()
        )

        return response.data

    @staticmethod
    def update_threat_score(
        scan_id: str,
        threat_score: int
    ):
        response = (
            supabase
            .table("scans")
            .update({
                "threat_score": threat_score
            })
            .eq("id", scan_id)
            .execute()
        )

        return response.data

    @staticmethod
    def get_full_scan(
        scan_id: str
):

        scan = (
        supabase
        .table("scans")
        .select("*")
        .eq("id", scan_id)
        .single()
        .execute()
    )

        findings = (
        supabase
        .table("threat_findings")
        .select("*")
        .eq("scan_id", scan_id)
        .execute()
    )

        ocr = (
        supabase
        .table("ocr_results")
        .select("*")
        .eq("scan_id", scan_id)
        .order(
            "created_at",
            desc=True
        )
        .limit(1)
        .execute()
    )

        classification = (
        supabase
        .table("scan_classifications")
        .select("*")
        .eq("scan_id", scan_id)
        .order(
            "created_at",
            desc=True
        )
        .limit(1)
        .execute()
    )

        report = (
        supabase
        .table("reports")
        .select("*")
        .eq("scan_id", scan_id)
        .order(
            "created_at",
            desc=True
        )
        .limit(1)
        .execute()
    )

        iocs = (
        supabase
        .table(
            "indicators_of_compromise"
        )
        .select("*")
        .eq(
            "scan_id",
            scan_id
        )
        .execute()
    )

        mitre = (
        supabase
        .table(
            "mitre_techniques"
        )
        .select("*")
        .eq(
            "scan_id",
            scan_id
        )
        .execute()
    )

        return {

        "scan":
            scan.data,

        "ocr":
            ocr.data[0]
            if ocr.data
            else None,

        "findings":
            findings.data or [],

        "classification":
            classification.data[0]
            if classification.data
            else None,

        "report":
            report.data[0]
            if report.data
            else None,

        "iocs":
            iocs.data or [],

        "mitre":
            mitre.data or []
    }