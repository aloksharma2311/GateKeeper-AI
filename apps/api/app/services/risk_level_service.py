class RiskLevelService:

    @staticmethod
    def get_level(
        score: int
    ):

        if score <= 20:
            return "SAFE"

        if score <= 40:
            return "LOW"

        if score <= 60:
            return "MEDIUM"

        if score <= 80:
            return "HIGH"

        return "CRITICAL"