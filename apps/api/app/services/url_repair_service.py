import re


class UrlRepairService:

    @staticmethod
    def repair(text: str):

        if not text:
            return text

        # -----------------------------
        # Common OCR URL mistakes
        # -----------------------------

        replacements = {

            "http:/ ": "http://",
            "https:/ ": "https://",

            "http:/I": "http://",
            "https:/I": "https://",

            "http:/l": "http://",
            "https:/l": "https://",

            "http:/|": "http://",
            "https:/|": "https://",

            "http ://": "http://",
            "https ://": "https://",

            "hxxp://": "http://",
            "hxxps://": "https://",

            "[.]": ".",
            "(.)": ".",

        }

        for bad, good in replacements.items():

            text = text.replace(
                bad,
                good
            )

        # -----------------------------
        # Remove spaces inside URLs
        # -----------------------------

        text = re.sub(
            r"(https?://)\s+",
            r"\1",
            text
        )

        # -----------------------------
        # OCR sometimes inserts spaces
        # in domains
        #
        # Example:
        # sbi security-check.xyz
        # becomes
        # sbi-security-check.xyz
        # -----------------------------

        domain_fix_pattern = (
            r"([a-zA-Z0-9]+)\s+([a-zA-Z0-9\-]+\.(?:com|org|net|xyz|in|co))"
        )

        text = re.sub(
            domain_fix_pattern,
            r"\1-\2",
            text
        )

        # -----------------------------
        # Remove double slashes
        # -----------------------------

        text = text.replace(
            "http:////",
            "http://"
        )

        text = text.replace(
            "https:////",
            "https://"
        )
        
        text = text.replace(
            "https:///",
            "https://"
        )

        text = text.replace(
            "http:///",
            "http://"
        )

        return text