class RecommendationService:

    @staticmethod
    def generate(
        scam_type: str
    ):

        recommendations = {

            "Banking Phishing": [
                "Never share OTP",
                "Verify the website domain",
                "Contact the bank using official channels",
                "Do not click suspicious links",
            ],

            "UPI Fraud": [
                "Do not send money",
                "Verify UPI owner identity",
                "Report suspicious payment requests",
            ],

            "Social Engineering Scam": [
                "Do not engage with unknown contacts",
                "Verify identity independently",
                "Block suspicious accounts",
            ],

            "Telegram Payment Scam": [
                "Avoid direct payments through Telegram",
                "Verify seller identity",
                "Use trusted payment channels",
            ],

            "Identity Theft Scam": [
                "Do not share Aadhaar or PAN",
                "Report leaked identity documents",
                "Monitor financial accounts",
            ],

            "Phishing Campaign": [
                "Do not click suspicious links",
                "Verify sender authenticity",
                "Report phishing emails",
            ],

            "Unknown": [
                "Review manually",
                "Verify all contact information",
            ],
        }

        return recommendations.get(
            scam_type,
            ["Review manually"]
        )