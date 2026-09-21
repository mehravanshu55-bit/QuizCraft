def get_category(text):
    text = text.lower()

    categories = {
        "programming_language": [
            "programming language",
            "high-level language",
            "low-level language"
        ],
        "database": [
            "database",
            "dbms",
            "sql",
            "query"
        ],
        "network": [
            "network",
            "protocol",
            "tcp",
            "http",
            "ftp",
            "ip"
        ]
    }

    for category, words in categories.items():
        for word in words:
            if word in text:
                return category

    return "general"
