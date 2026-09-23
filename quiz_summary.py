
def create_quiz_summary(topic, score, total):
    """Create a simple quiz result summary."""
    percentage = (score / total * 100) if total else 0

    return {
        "topic": topic,
        "score": score,
        "total": total,
        "percentage": round(percentage, 1)
    }
