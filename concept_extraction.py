def extract_concepts(text):
    sentences = re.split(r"[.!?]", text)
    concepts = []

    patterns = [
        ("definition", r"^(.+?)\s+is\s+(?:a|an|the)\s+(.+)$"),
        ("definition", r"^(.+?)\s+is\s+(.+)$"),
        ("definition", r"^(.+?)\s+are\s+(.+)$"),
        ("use", r"^(.+?)\s+is\s+used\s+for\s+(.+)$"),
        ("use", r"^(.+?)\s+uses\s+(.+)$"),
        ("support", r"^(.+?)\s+supports\s+(.+)$"),
        ("provide", r"^(.+?)\s+provides\s+(.+)$"),
        ("allow", r"^(.+?)\s+allows\s+(.+)$"),
        ("help", r"^(.+?)\s+helps\s+(.+)$")
    ]
