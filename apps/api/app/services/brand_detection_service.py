import re


class BrandDetectionService:

    BANK_BRANDS = {
        "sbi": "State Bank of India",
        "hdfc": "HDFC Bank",
        "icici": "ICICI Bank",
        "axis": "Axis Bank",
        "kotak": "Kotak Mahindra Bank",
        "pnb": "Punjab National Bank",
        "bob": "Bank of Baroda",
        "canara": "Canara Bank",
        "union": "Union Bank",
    }

    @classmethod
    def detect(cls, text: str):

        text = text.lower()

        matches = []

        for keyword, bank in cls.BANK_BRANDS.items():

            if keyword in text:

                matches.append(
                    {
                        "brand": bank,
                        "keyword": keyword,
                        "confidence": 90,
                    }
                )

        return matches