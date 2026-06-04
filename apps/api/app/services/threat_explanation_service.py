class ThreatExplanationService:

    @staticmethod
    def generate(
        findings,
        scam_type,
        risk_level
    ):

        risks = []

        if any(
            f["type"] == "brand_impersonation"
            for f in findings
        ):
            risks.append(
                "Brand impersonation detected"
            )

        if any(
            f["type"] == "unresolvable_domain"
            for f in findings
        ):
            risks.append(
                "Website domain cannot be verified"
            )

        if any(
            f["type"] == "suspicious_tld"
            for f in findings
        ):
            risks.append(
                "Suspicious website domain detected"
            )

        if any(
            f["type"] == "ip_url"
            for f in findings
        ):
            risks.append(
                "Website uses raw IP address"
            )

        if any(
            f["type"] == "aadhaar"
            for f in findings
        ):
            risks.append(
                "Identity information detected"
            )

        summary = (
            f"This content was classified as "
            f"{scam_type} with a "
            f"{risk_level} risk rating."
        )

        return {
            "summary": summary,
            "key_risks": risks
        }