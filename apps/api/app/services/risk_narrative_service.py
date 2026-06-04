class RiskNarrativeService:

    @staticmethod
    def generate(
        scam_type,
        findings
    ):

        if scam_type == "Banking Phishing":

            return (
                "This screenshot appears to "
                "impersonate a financial institution "
                "and attempts to redirect users "
                "to a suspicious website."
            )

        if scam_type == "Bank Reward Scam":

            return (
                "This screenshot claims the user "
                "has reward points waiting to be claimed "
                "and uses deceptive branding."
            )

        if scam_type == "Phishing Attempt":

            return (
                "This screenshot contains indicators "
                "commonly used in phishing attacks "
                "to steal credentials."
            )

        return (
            "Suspicious content detected."
        )