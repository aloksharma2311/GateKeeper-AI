# app/services/mitre_mapper_service.py

class MitreMapperService:

    MITRE_MAPPING = {

        "brand_impersonation": {
            "id": "T1585",
            "name": "Establish Accounts"
        },

        "url": {
            "id": "T1583",
            "name": "Acquire Infrastructure"
        },

        "email": {
            "id": "T1566.001",
            "name": "Spearphishing Attachment"
        },

        "telegram": {
            "id": "T1105",
            "name": "Ingress Tool Transfer"
        },

        "ip_url": {
            "id": "T1583",
            "name": "Acquire Infrastructure"
        }
    }

    @staticmethod
    def map(findings):

        techniques = []
        seen = set()

        for finding in findings:

            technique = (
                MitreMapperService
                .MITRE_MAPPING
                .get(
                    finding["type"]
                )
            )

            if not technique:
                continue

            if technique["id"] in seen:
                continue

            seen.add(
                technique["id"]
            )

            techniques.append(
                technique
            )

        return techniques