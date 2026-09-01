import re

def clean_text(text):
    text = re.sub(r"\s+"," ", text)
    return text.strip()
# testing
sample_text = """
Python    is a programming language.

it is easy    to learn.
"""
cleaned_text = clean_text(sample_text)
print(cleaned_text)
