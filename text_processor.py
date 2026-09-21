import re
from PyPDF2 import PdfReader


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()
