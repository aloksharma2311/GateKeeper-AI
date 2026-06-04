class DomainAgeService:

    @staticmethod
    def analyze(whois_data):

        findings = []

        if not whois_data:
            return findings

        age = whois_data["age_days"]

        if age < 30:

            findings.append(
                {
                    "type": "new_domain",
                    "value": str(age),
                    "confidence": 100
                }
            )

        elif age < 180:

            findings.append(
                {
                    "type": "young_domain",
                    "value": str(age),
                    "confidence": 80
                }
            )

        return findings