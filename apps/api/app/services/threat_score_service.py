class ThreatScoreService:

    WEIGHTS = {

    "phone": 5,
    "email": 5,
    "upi": 15,
    "url": 15,
    "telegram": 10,
    "instagram": 5,
    "discord": 5,
    "aadhaar": 15,
    "pan": 15,
    "credit_card": 35,

    "brand": 10,
    "brand_impersonation": 30,
    "context": 15,

    "resolved_ip": 5,
    "unresolvable_domain": 20,
    "suspicious_tld": 15,
    "url_shortener": 15,
    "ip_url": 25,
    
    "new_domain": 20,
    "suspicious_tld": 20,
    "unresolvable_domain": 25,
    }

    @classmethod
    def calculate(
        cls,
        findings
    ):

        score = 0

        seen = set()

        for finding in findings:

            finding_type = (
                finding["type"]
            )

            if finding_type in seen:
                continue

            seen.add(
                finding_type
            )

            score += cls.WEIGHTS.get(
                finding_type,
                0
            )

        return min(
            score,
            100
        )