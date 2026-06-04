import socket
import re
from urllib.parse import urlparse


class ThreatIntelligenceService:

    SUSPICIOUS_TLDS = {
        "xyz",
        "top",
        "click",
        "monster",
        "shop",
        "cc",
        "tk",
        "ml",
        "ga",
        "gq",
    }

    SHORTENER_KEYWORDS = [
    "bit.ly",
    "bitly",
    "bit-ly",
    "tinyurl",
    "t.co",
    "goo.gl",
    ]
    
    

    @classmethod
    def analyze(cls, findings):

        intelligence = []

        urls = [
            f["value"]
            for f in findings
            if f["type"] == "url"
        ]

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

                # --------------------------------
                # URL Shorteners
                # --------------------------------

                if any(
                    keyword in domain
                    for keyword in cls.SHORTENER_KEYWORDS
                ):

                    intelligence.append(
                    {
                        "type": "url_shortener",
                        "value": domain,
                        "confidence": 90,
                    }
                    )

                # --------------------------------
                # Suspicious TLDs
                # --------------------------------

                parts = domain.split(".")

                if len(parts) > 1:

                    tld = parts[-1]

                    if (
                        tld
                        in cls.SUSPICIOUS_TLDS
                    ):

                        intelligence.append(
                            {
                                "type":
                                    "suspicious_tld",

                                "value":
                                    domain,

                                "confidence":
                                    90,
                            }
                        )

                # --------------------------------
                # IP URLs
                # --------------------------------

                if re.match(
                    r"^\d+\.\d+\.\d+\.\d+$",
                    domain
                ):

                    intelligence.append(
                        {
                            "type":
                                "ip_url",

                            "value":
                                domain,

                            "confidence":
                                95,
                        }
                    )

                # --------------------------------
                # DNS Resolution
                # --------------------------------

                try:

                    socket.gethostbyname(
                        domain
                    )

                except Exception:

                    intelligence.append(
                        {
                            "type":
                                "unresolvable_domain",

                            "value":
                                domain,

                            "confidence":
                                95,
                        }
                    )

            except Exception:
                pass

        return intelligence