def validate_signup(name, username, email, password):
    """Validate required signup fields."""
    if not name or not username or not email or not password:
        return False

    return True

def validate_password_confirmation(password, confirm_password):
    """Check whether both passwords match."""
    return password == confirm_password
