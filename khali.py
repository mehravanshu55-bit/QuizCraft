def calculate_score(answers, correct_answers):
    """Calculate the number of correct quiz answers."""
    score = 0

    for user_answer, correct_answer in zip(answers, correct_answers):
        if user_answer == correct_answer:
            score += 1

    return score
