import easyocr


class OCRService:

    _reader = None

    @classmethod
    def get_reader(cls):

        if cls._reader is None:

            cls._reader = easyocr.Reader(
                ["en"],
                gpu=False
            )

        return cls._reader

    @classmethod
    def extract_text(
        cls,
        image_path: str
    ) -> str:

        reader = cls.get_reader()

        result = reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)