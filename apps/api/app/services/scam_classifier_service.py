class ScamClassifierService:

    @staticmethod
    def classify(findings):

        types = {
            finding["type"]
            for finding in findings
        }

        explanation = []
        explanation_seen = set()

        score = 0

        def add_explanation(text):

            if text not in explanation_seen:

                explanation.append(text)
                explanation_seen.add(text)

        # =====================
        # Threat Intelligence
        # =====================

        if "unresolvable_domain" in types:

            score += 20

            add_explanation(
                "Domain could not be resolved"
            )

        if "suspicious_tld" in types:

            score += 15

            add_explanation(
                "Suspicious domain extension detected"
            )

        if "url_shortener" in types:

            score += 15

            add_explanation(
                "URL shortener detected"
            )

        if "ip_url" in types:

            score += 25

            add_explanation(
                "IP address based URL detected"
            )

        if "resolved_ip" in types:

            score += 5

            add_explanation(
                "Domain successfully resolved"
            )
            
        if "new_domain" in types:

            score += 15

            add_explanation(
                "Recently registered domain"
            )    

        # =====================
        # Base Indicators
        # =====================

        if "phone" in types:

            score += 10

            add_explanation(
                "Phone number detected"
            )

        if "email" in types:

            score += 10

            add_explanation(
                "Email address detected"
            )

        if "url" in types:

            score += 15

            add_explanation(
                "Website detected"
            )

        if "telegram" in types:

            score += 15

            add_explanation(
                "Telegram contact detected"
            )

        if "upi" in types:

            score += 20

            add_explanation(
                "UPI identifier detected"
            )

        if "aadhaar" in types:

            score += 20

            add_explanation(
                "Aadhaar number detected"
            )

        if "pan" in types:

            score += 20

            add_explanation(
                "PAN card detected"
            )

        if "credit_card" in types:

            score += 30

            add_explanation(
                "Credit card detected"
            )

        if "otp" in types:

            score += 15

            add_explanation(
                "OTP request detected"
            )

        # =====================
        # Brand Intelligence
        # =====================

        if "brand" in types:

            score += 10

            add_explanation(
                "Financial institution detected"
            )

        if "brand_impersonation" in types:

            score += 40

            add_explanation(
                "Possible brand impersonation detected"
            )

        # =====================
        # Context Intelligence
        # =====================

        context_categories = []

        for finding in findings:

            if finding["type"] == "context":

                category = finding.get(
                    "category"
                )

                if category:

                    context_categories.append(
                        category
                    )

        if "phishing" in context_categories:

            score += 25

            add_explanation(
                "Phishing language detected"
            )

        if "urgency" in context_categories:

            score += 15

            add_explanation(
                "Urgency tactics detected"
            )

        if "lottery_scam" in context_categories:

            score += 30

            add_explanation(
                "Lottery scam indicators detected"
            )

        if "reward_scam" in context_categories:

            score += 25

            add_explanation(
                "Reward scam indicators detected"
            )

        if "support_scam" in context_categories:

            score += 25

            add_explanation(
                "Fake support indicators detected"
            )

        if "refund_scam" in context_categories:

            score += 25

            add_explanation(
                "Refund scam indicators detected"
            )

        # =====================
        # Scam Classification
        # =====================

        scam_type = "Unknown"

        # Bank Reward Scam

        if (
            "brand_impersonation" in types
            and "reward_scam" in context_categories
        ):

            scam_type = (
                "Bank Reward Scam"
            )

            score += 25

        # Banking Phishing

        elif (
            "brand_impersonation" in types
        ):

            scam_type = (
                "Banking Phishing"
            )

            score += 20

        elif (
            "brand" in types
            and "url" in types
            and (
                "suspicious_tld" in types
                or "unresolvable_domain" in types
                or "new_domain" in types
            )
        ):

            scam_type = (
                "Banking Phishing"
            )

            score += 20

        elif (
            "brand" in types
            and "url" in types
            and "aadhaar" in types
        ):

            scam_type = (
                "Banking Phishing"
            )

            score += 15

        # Suspicious Website

        elif (
            "new_domain" in types
            and "url" in types
        ):

            scam_type = (
                "Suspicious Website"
            )

            score += 15

        # UPI Fraud

        elif (
            "upi" in types
            and "phone" in types
        ):

            scam_type = (
                "UPI Fraud"
            )

            score += 15

        # Telegram Payment Scam

        elif (
            "telegram" in types
            and "upi" in types
        ):

            scam_type = (
                "Telegram Payment Scam"
            )

            score += 20

        # Social Engineering

        elif (
            "telegram" in types
            and "phone" in types
        ):

            scam_type = (
                "Social Engineering Scam"
            )

            score += 15

        # Identity Theft

        elif (
            "aadhaar" in types
            and "pan" in types
        ):

            scam_type = (
                "Identity Theft Scam"
            )

            score += 20

        # Generic Phishing

        elif (
            "email" in types
            and "url" in types
        ):

            scam_type = (
                "Phishing Campaign"
            )

            score += 15

        # Context-only Scams

        elif (
            "phishing"
            in context_categories
        ):

            scam_type = (
                "Phishing Attempt"
            )

        elif (
            "lottery_scam"
            in context_categories
        ):

            scam_type = (
                "Lottery Scam"
            )

        elif (
            "reward_scam"
            in context_categories
        ):

            scam_type = (
                "Reward Scam"
            )

        elif (
            "support_scam"
            in context_categories
        ):

            scam_type = (
                "Tech Support Scam"
            )

        elif (
            "refund_scam"
            in context_categories
        ):

            scam_type = (
                "Refund Scam"
            )

        # =====================
        # Confidence
        # =====================

        confidence = min(
            score,
            100
        )

        if not explanation:

            add_explanation(
                "Insufficient indicators"
            )

        return {
            "scam_type": scam_type,
            "confidence": confidence,
            "explanation": explanation,
        }