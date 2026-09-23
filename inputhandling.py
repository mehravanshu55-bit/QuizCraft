def clean_user_input(text):
    """Remove unnecessary spaces from user-provided study material."""
    if not isinstance(text, str):
        return ""
    return " ".join(text.strip().split())
    
def validate_text_input(text):
    """Check whether study material contains usable text."""
    return isinstance(text, str) and len(text.strip()) > 0
