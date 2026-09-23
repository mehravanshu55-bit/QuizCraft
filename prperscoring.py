def calculate_score(answers, correct_answers):
    """Calculate the number of correct quiz answers."""
    score = 0

    for user_answer, correct_answer in zip(answers, correct_answers):
        if user_answer == correct_answer:
            score += 1

    return score

def calculate_percentage(score, total):
    """Calculate quiz percentage."""
    if total == 0:
        return 0.0

    return (score / total) * 100

def get_result_message(percentage):
    """Return feedback based on quiz performance."""
    if percentage >= 80:
        return "Excellent work!"
    elif percentage >= 50:
        return "Good effort! Keep practicing."
    else:
        return "Keep practicing and try again."
