class ReportGeneratorService:

    @staticmethod
    def generate(
        findings,
        classification,
        threat_score
    ):

        types = {
            finding["type"]
            for finding in findings
        }

        # =====================
        # Risk Level
        # =====================

        if threat_score >= 75:
            risk_level = "CRITICAL"

        elif threat_score >= 50:
            risk_level = "HIGH"

        elif threat_score >= 25:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        # =====================
        # Attack Vectors
        # =====================

        attack_vectors = []

        if "brand_impersonation" in types:
            attack_vectors.append(
                "Brand Impersonation"
            )

        if "url" in types:
            attack_vectors.append(
                "Malicious URL"
            )

        if "url_shortener" in types:
            attack_vectors.append(
                "URL Shortener Abuse"
            )

        if "unresolvable_domain" in types:
            attack_vectors.append(
                "Suspicious Domain"
            )

        if "ip_url" in types:
            attack_vectors.append(
                "IP-Based URL"
            )

        if "email" in types:
            attack_vectors.append(
                "Email Phishing"
            )

        if "telegram" in types:
            attack_vectors.append(
                "Telegram Social Engineering"
            )

        if "phone" in types:
            attack_vectors.append(
                "Phone-Based Fraud"
            )

        if "upi" in types:
            attack_vectors.append(
                "Financial Fraud"
            )

        if "aadhaar" in types:
            attack_vectors.append(
                "Identity Theft"
            )

        if "pan" in types:
            attack_vectors.append(
                "Identity Theft"
            )

        # =====================
        # Executive Summary
        # =====================

        scam_type = classification.get(
            "scam_type",
            "Unknown"
        )

        confidence = classification.get(
            "confidence",
            0
        )

        summary = (
            f"This content was classified as "
            f"{scam_type} with a confidence "
            f"score of {confidence}%."
        )

        if "brand_impersonation" in types:
            summary += (
                " The content appears to "
                "impersonate a trusted brand."
            )

        if "url" in types:
            summary += (
                " A potentially malicious "
                "website was detected."
            )

        if "url_shortener" in types:
            summary += (
                " A URL shortener was used "
                "to hide the destination."
            )

        if "unresolvable_domain" in types:
            summary += (
                " The detected domain could "
                "not be resolved."
            )

        if "ip_url" in types:
            summary += (
                " An IP-based URL was used "
                "instead of a normal domain."
            )

        if "aadhaar" in types:
            summary += (
                " Sensitive identity data "
                "was detected."
            )

        # =====================
        # Recommendations
        # =====================

        recommendations = [
            "Do not interact with the sender",
            "Do not share personal information",
            "Report the incident"
        ]

        if "url" in types:
            recommendations.append(
                "Do not visit the detected URL"
            )

        if "upi" in types:
            recommendations.append(
                "Do not transfer money"
            )

        if "brand_impersonation" in types:
            recommendations.append(
                "Verify through official channels"
            )

        if "aadhaar" in types:
            recommendations.append(
                "Monitor for identity misuse"
            )

        # Remove duplicates

        recommendations = list(
            dict.fromkeys(
                recommendations
            )
        )

        attack_vectors = list(
            dict.fromkeys(
                attack_vectors
            )
        )

        return {
            "risk_level":
                risk_level,

            "summary":
                summary,

            "attack_vectors":
                attack_vectors,

            "recommended_actions":
                recommendations
        }