import easyocr


class OCRService:

    _reader = easyocr.Reader(
        ["en"],
        gpu=True
    )

    @classmethod
    def extract_text(
        cls,
        image_path: str
    ) -> str:

        result = cls._reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)