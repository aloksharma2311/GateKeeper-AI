from urllib.parse import urlparse


class DomainIntelligenceService:

    OFFICIAL_BANK_DOMAINS = {
        "State Bank of India":
            "sbi.co.in",

        "HDFC Bank":
            "hdfcbank.com",

        "ICICI Bank":
            "icicibank.com",

        "Axis Bank":
            "axisbank.com",

        "Kotak Mahindra Bank":
            "kotak.com",

        "Punjab National Bank":
            "pnbindia.in",
    }

    @classmethod
    def analyze(
        cls,
        findings
    ):

        urls = [
            f["value"]
            for f in findings
            if f["type"] == "url"
        ]

        brands = [
            f["value"]
            for f in findings
            if f["type"] == "brand"
        ]

        intelligence = []

        for brand in brands:

            official_domain = (
                cls.OFFICIAL_BANK_DOMAINS.get(
                    brand
                )
            )

            if not official_domain:
                continue

            for url in urls:

                try:

                    parsed = urlparse(url)

                    domain = (
                        parsed.netloc
                        .replace("www.", "")
                        .lower()
                    )

                    if not domain:
                        continue

                    if (
                        official_domain
                        not in domain
                    ):

                        intelligence.append(
                            {
                                "type":
                                    "brand_impersonation",

                                "value":
                                    brand,

                                "domain":
                                    domain,

                                "confidence":
                                    95,
                            }
                        )

                except Exception:
                    continue

        return intelligence