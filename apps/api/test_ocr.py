import easyocr

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

result = reader.readtext(
    "downloads/original.png",
    detail=0
)

print(result)