import re


class TextNormalizerService:

    @staticmethod
    def normalize(text: str):

        text = re.sub(
            r"\n+",
            " ",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()