class ContextAnalysisService:

    KEYWORDS = {
        "verify account":
            "phishing",

        "update kyc":
            "phishing",

        "account blocked":
            "phishing",

        "customer support":
            "support_scam",

        "refund":
            "refund_scam",

        "reward points":
            "reward_scam",

        "click here":
            "phishing",

        "urgent":
            "urgency",

        "limited time":
            "urgency",

        "lottery":
            "lottery_scam",

        "winner":
            "lottery_scam",
    }

    @classmethod
    def detect(cls, text: str):

        text = text.lower()

        findings = []

        for keyword, category in (
            cls.KEYWORDS.items()
        ):

            if keyword in text:

                findings.append(
                    {
                        "type":
                            "context",

                        "value":
                            keyword,

                        "category":
                            category,

                        "confidence":
                            90,
                    }
                )

        return findings