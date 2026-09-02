import re
from pyPDF2 import pdfReader

def clean_text(text):
    text = re.sub(r"\s+"," ", text)
    return text.strip()
def extract_text_from_pdf(pdf_file):
    reader = pdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
    
# testing
sample_text = """
Python    is a programming language.

it is easy    to learn.
"""
cleaned_text = clean_text(sample_text)
print(cleaned_text)
