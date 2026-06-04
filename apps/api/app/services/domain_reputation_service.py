import socket
import whois

from urllib.parse import urlparse


class DomainReputationService:

    SUSPICIOUS_TLDS = {
        ".xyz",
        ".top",
        ".click",
        ".gq",
        ".tk",
        ".ml",
        ".cf"
    }

    @staticmethod
    def analyze(url: str):

        result = {
            "domain": None,
            "dns_resolves": False,
            "domain_registered": False,
            "domain_age_days": None,
            "suspicious_tld": False,
            "risk_score": 0
        }

        try:

            parsed = urlparse(url)

            domain = parsed.netloc

            domain = domain.replace(
                "www.",
                ""
            )

            result["domain"] = domain

            # DNS Check

            try:

                socket.gethostbyname(
                    domain
                )

                result[
                    "dns_resolves"
                ] = True

            except:

                result[
                    "dns_resolves"
                ] = False

                result[
                    "risk_score"
                ] += 30

            # Suspicious TLD

            for tld in (
                DomainReputationService
                .SUSPICIOUS_TLDS
            ):

                if domain.endswith(tld):

                    result[
                        "suspicious_tld"
                    ] = True

                    result[
                        "risk_score"
                    ] += 20

            # WHOIS

            try:

                info = whois.whois(
                    domain
                )

                if info.domain_name:

                    result[
                        "domain_registered"
                    ] = True

                creation_date = (
                    info.creation_date
                )

                if isinstance(
                    creation_date,
                    list
                ):
                    creation_date = (
                        creation_date[0]
                    )

                if creation_date:

                    from datetime import (
                        datetime
                    )

                    age_days = (
                        datetime.now()
                        - creation_date
                    ).days

                    result[
                        "domain_age_days"
                    ] = age_days

                    if age_days < 30:

                        result[
                            "risk_score"
                        ] += 25

            except:

                result[
                    "risk_score"
                ] += 25

        except Exception as e:

            print(
                "Domain Reputation Error:",
                e
            )

        return result