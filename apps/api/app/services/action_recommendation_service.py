class ActionRecommendationService:

    @staticmethod
    def generate(
        scam_type
    ):

        common = [
            "Do not click suspicious links",
            "Do not share personal information",
            "Report the sender",
            "Block the contact"
        ]

        if scam_type == "Banking Phishing":

            common.extend(
                [
                    "Contact your bank directly",
                    "Change banking passwords"
                ]
            )

        if scam_type == "Identity Theft Scam":

            common.extend(
                [
                    "Monitor identity documents",
                    "Notify financial institutions"
                ]
            )

        return common