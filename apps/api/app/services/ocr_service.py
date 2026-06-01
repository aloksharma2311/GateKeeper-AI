from paddleocr import PaddleOCR


class OCRService:

    _ocr = PaddleOCR(
        use_angle_cls=True,
        lang="en"
    )

    @classmethod
    def extract_text(
        cls,
        image_path: str
    ) -> str:

        result = cls._ocr.ocr(
            image_path,
            cls=True
        )

        extracted = []

        for block in result:
            if not block:
                continue

            for line in block:
                extracted.append(
                    line[1][0]
                )

        return "\n".join(
            extracted
        )