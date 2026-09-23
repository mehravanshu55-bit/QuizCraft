def clean_user_input(text):
    """Remove unnecessary spaces from user-provided study material."""
    if not isinstance(text, str):
        return ""
    return " ".join(text.strip().split())
