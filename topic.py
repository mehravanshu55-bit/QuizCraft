
def format_quiz_topic(topic):
    """Format a quiz topic for display."""
    if not topic:
        return "General"

    return topic.strip().title()
