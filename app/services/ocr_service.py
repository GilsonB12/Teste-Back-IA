import io
from PIL import Image
from pdf2image import convert_from_bytes
import pytesseract

def extract_text(file_storage):
    filename = file_storage.filename.lower()
    file_bytes = file_storage.read()
    file_storage.seek(0)

    if filename.endswith(".pdf"):
        pages = convert_from_bytes(file_bytes)
        return "\n".join(pytesseract.image_to_string(p) for p in pages)
    elif filename.endswith((".png", ".jpeg", ".jpg")):
        img = Image.open(io.BytesIO(file_bytes))
        return pytesseract.image_to_string(img)
    else:
        raise ValueError(f"não suporta: {filename}")
