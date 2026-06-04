class OCRQualityService:

    @staticmethod
    def analyze(text):

        score = 100

        suspicious = [
            "http:/I",
            "http:/l",
            "http:/|",
            "www ",
            " .com",
            " .in"
        ]

        for item in suspicious:

            if item in text:

                score -= 15

        return max(
            score,
            0
        )