from app.services.domain_reputation_service import (
    DomainReputationService
)


class DomainReputationFindingService:

    @staticmethod
    def analyze(findings):

        new_findings = []

        urls = [
            f
            for f in findings
            if f["type"] == "url"
        ]

        for item in urls:

            result = (
                DomainReputationService
                .analyze(
                    item["value"]
                )
            )

            if not result[
                "dns_resolves"
            ]:

                new_findings.append(
                    {
                        "type":
                            "unresolvable_domain",
                        "value":
                            result["domain"]
                    }
                )

            if result[
                "suspicious_tld"
            ]:

                new_findings.append(
                    {
                        "type":
                            "suspicious_tld",
                        "value":
                            result["domain"]
                    }
                )

            age = result.get(
                "domain_age_days"
            )

            if (
                age is not None
                and age < 30
            ):

                new_findings.append(
                    {
                        "type":
                            "new_domain",
                        "value":
                            result["domain"]
                    }
                )

        return new_findings