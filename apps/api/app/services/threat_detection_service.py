import re


class ThreatDetectionService:

    PHONE_REGEX = (
        r"(?:\+91[\-\s]?)?[6-9]\d{9}"
    )

    EMAIL_REGEX = (
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    )

    EMAIL_FUZZY_REGEX = (
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+com"
    )

    URL_REGEX = (
        r"(https?://[^\s\]\)\},;]+|www\.[^\s\]\)\},;]+)"
        )

    UPI_REGEX = (
        r"\b[a-zA-Z0-9._-]{2,256}"
        r"@(paytm|ybl|ibl|oksbi|okicici|axl|upi)\b"
    )

    TELEGRAM_REGEX = (
        r"(?<!\w)@[a-zA-Z0-9_]{5,32}"
    )

    INSTAGRAM_REGEX = (
        r"instagram\.com\/([a-zA-Z0-9_.]+)"
    )

    DISCORD_REGEX = (
        r"[a-zA-Z0-9_]{2,32}#[0-9]{4}"
    )

    WHATSAPP_REGEX = (
        r"(?:\+91[\-\s]?)?[6-9]\d{9}"
    )

    OTP_REGEX = (
        r"\b(?:otp|verification code|one time password)\b"
    )

    AADHAAR_REGEX = (
        r"\b\d{4}\s?\d{4}\s?\d{4}\b"
    )

    PAN_REGEX = (
        r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
    )

    CREDIT_CARD_REGEX = (
        r"\b(?:\d[ -]*?){13,16}\b"
    )

    @classmethod
    def detect(
        cls,
        text: str
    ):

        findings = []

        seen = set()

        def add_finding(
            finding_type,
            value
        ):

            key = (
                finding_type,
                value
            )

            if key not in seen:

                findings.append(
                    {
                        "type":
                            finding_type,
                        "value":
                            value,
                    }
                )

                seen.add(key)

        # Phones
        for phone in re.findall(
            cls.PHONE_REGEX,
            text
        ):
            add_finding(
                "phone",
                phone
            )

        # Emails
        for email in re.findall(
            cls.EMAIL_REGEX,
            text
        ):
            add_finding(
                "email",
                email
            )

        # OCR-damaged emails
        for email in re.findall(
            cls.EMAIL_FUZZY_REGEX,
            text
        ):

            fixed_email = (
                email
                .replace(
                    "gmailcom",
                    "gmail.com"
                )
                .replace(
                    "yahoocom",
                    "yahoo.com"
                )
            )

            add_finding(
                "email",
                fixed_email
            )

        # URLs
        for url in re.findall(
            cls.URL_REGEX,
            text
        ):

            url = url.rstrip(
                "])},.;"
            )

            add_finding(
                "url",
                url
            )

        # UPI IDs
        for match in re.findall(
            cls.UPI_REGEX,
            text,
            flags=re.IGNORECASE
        ):

            if isinstance(
                match,
                tuple
            ):
                continue

        upi_matches = re.finditer(
            cls.UPI_REGEX,
            text,
            flags=re.IGNORECASE
        )

        for match in upi_matches:

            add_finding(
                "upi",
                match.group()
            )

        # Telegram
        for telegram in re.findall(
            cls.TELEGRAM_REGEX,
            text
        ):
            add_finding(
                "telegram",
                telegram
            )

        # Instagram
        for insta in re.findall(
            cls.INSTAGRAM_REGEX,
            text
        ):
            add_finding(
                "instagram",
                insta
            )

        # Discord
        for discord in re.findall(
            cls.DISCORD_REGEX,
            text
        ):
            add_finding(
                "discord",
                discord
            )

        # OTP
        for otp in re.findall(
            cls.OTP_REGEX,
            text,
            flags=re.IGNORECASE
        ):
            add_finding(
                "otp",
                otp
            )

        # Aadhaar
        for aadhaar in re.findall(
            cls.AADHAAR_REGEX,
            text
        ):
            add_finding(
                "aadhaar",
                aadhaar
            )

        # PAN
        for pan in re.findall(
            cls.PAN_REGEX,
            text
        ):
            add_finding(
                "pan",
                pan
            )

        # Credit Cards
        for card in re.findall(
            cls.CREDIT_CARD_REGEX,
            text
        ):
            add_finding(
                "credit_card",
                card
            )

        return findings