# app/services/ioc_service.py

class IOCService:

    IOC_TYPES = {
        "phone",
        "email",
        "url",
        "telegram",
        "upi",
        "aadhaar",
        "pan",
        "credit_card",
        "ip_url",
    }

    @staticmethod
    def extract(findings):

        iocs = []
        seen = set()

        for finding in findings:

            if finding["type"] not in IOCService.IOC_TYPES:
                continue

            key = (
                finding["type"],
                finding["value"]
            )

            if key in seen:
                continue

            seen.add(key)

            iocs.append(
                {
                    "ioc_type": finding["type"],
                    "ioc_value": finding["value"],
                }
            )

        return iocs