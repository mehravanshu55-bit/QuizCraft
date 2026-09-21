def extract_concepts(text):
    sentences = re.split(r"[.!?]", text)
    concepts = []

    patterns = [
        ("definition", r"^(.+?)\s+is\s+(?:a|an|the)\s+(.+)$"),
        ("definition", r"^(.+?)\s+is\s+(.+)$"),
        ("definition", r"^(.+?)\s+are\s+(.+)$"),
    ]
