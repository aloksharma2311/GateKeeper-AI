import whois
from datetime import datetime


class WhoisService:

    @staticmethod
    def analyze(domain):

        try:

            result = whois.whois(domain)

            creation_date = result.creation_date

            if isinstance(
                creation_date,
                list
            ):
                creation_date = creation_date[0]

            if not creation_date:
                return None

            age_days = (
                datetime.now()
                - creation_date
            ).days

            return {
                "domain": domain,
                "age_days": age_days
            }

        except Exception:

            return None