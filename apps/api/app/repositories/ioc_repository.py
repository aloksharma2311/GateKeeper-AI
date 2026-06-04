from app.core.supabase import supabase


class IOCRepository:

    @staticmethod
    def create(
        scan_id: str,
        ioc_type: str,
        ioc_value: str
    ):

        return (
            supabase
            .table(
                "indicators_of_compromise"
            )
            .insert(
                {
                    "scan_id": scan_id,
                    "indicator_type": ioc_type,
                    "indicator_value": ioc_value,
                    "confidence": 100
                }
            )
            .execute()
        )

    @staticmethod
    def get_by_scan_id(
        scan_id: str
    ):

        result = (
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

        return result.data or []