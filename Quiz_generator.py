import random
import re


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

    for sentence in sentences:
        sentence = re.sub(r"\s+", " ", sentence.strip())

        if len(sentence.split()) < 4:
            continue

        for relation, pattern in patterns:
            match = re.match(pattern, sentence, re.IGNORECASE)

            if match:
                subject = match.group(1).strip()
                answer = match.group(2).strip()

                if len(subject.split()) <= 8 and len(answer.split()) >= 2:
                    concepts.append({
                        "subject": subject,
                        "answer": answer,
                        "relation": relation
                    })
                    break

    return concepts


def get_category(text):
    text = text.lower()

    categories = {
        "programming_language": [
            "programming language",
            "high-level language",
            "low-level language",
            "programming language"
        ],
        "programming": [
            "programming",
            "object-oriented",
            "procedural",
            "functional"
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
        ],
        "data_structure": [
            "stack",
            "queue",
            "linked list",
            "tree",
            "graph"
        ],
        "digital": [
            "logic gate",
            "and gate",
            "or gate",
            "not gate",
            "flip-flop",
            "counter",
            "register"
        ],
        "hardware": [
            "processor",
            "memory",
            "hardware",
            "storage",
            "keyboard",
            "mouse"
        ],
        "software": [
            "software",
            "operating system",
            "compiler",
            "interpreter",
            "application"
        ]
    }

    for category, words in categories.items():
        for word in words:
            if word in text:
                return category

    return "general"


def get_distractors(correct_answer, concepts):
    correct_category = get_category(correct_answer)
    candidates = []

    for concept in concepts:
        answer = concept["answer"].strip()

        if answer.lower() == correct_answer.lower():
            continue

        if get_category(answer) == correct_category:
            candidates.append(answer)

    random.shuffle(candidates)

    if len(candidates) < 3:
        for concept in concepts:
            answer = concept["answer"].strip()

            if answer.lower() == correct_answer.lower():
                continue

            if answer not in candidates:
                candidates.append(answer)

            if len(candidates) == 3:
                break

    result = []

    for answer in candidates:
        if answer.lower() != correct_answer.lower():
            if answer not in result:
                result.append(answer)

        if len(result) == 3:
            break

    return result


def make_question(subject, answer, relation, difficulty):
    if difficulty == "Easy":

        if relation == "definition":
            return f"What is {subject}?"

        if relation == "use":
            return f"What is {subject} used for?"

        if relation == "support":
            return f"What does {subject} support?"

        if relation == "provide":
            return f"What does {subject} provide?"

        if relation == "allow":
            return f"What does {subject} allow?"

        if relation == "help":
            return f"What does {subject} help with?"

    elif difficulty == "Medium":

        if relation == "definition":
            return f"Which of the following correctly describes {subject}?"

        if relation == "use":
            return f"Which of the following is a use of {subject}?"

        if relation == "support":
            return f"Which of the following is supported by {subject}?"

        if relation == "provide":
            return f"Which of the following is provided by {subject}?"

        if relation == "allow":
            return f"Which of the following is enabled by {subject}?"

        if relation == "help":
            return f"Which of the following does {subject} help with?"

    else:

        if relation == "definition":
            return f"Which statement best identifies the nature of {subject}?"

        if relation == "use":
            return f"Which option best identifies the purpose of {subject}?"

        if relation == "support":
            return f"Which option best identifies what {subject} supports?"

        if relation == "provide":
            return f"Which option best identifies what {subject} provides?"

        if relation == "allow":
            return f"Which option best identifies what {subject} enables?"

        if relation == "help":
            return f"Which option best identifies the function of {subject}?"

    return f"Which statement correctly describes {subject}?"


def generate_quiz(text, topic, difficulty, number_of_questions):
    concepts = extract_concepts(text)

    if not concepts:
        return []

    random.shuffle(concepts)

    questions = []
    used_questions = set()
    used_subjects = set()

    for concept in concepts:
        if len(questions) >= number_of_questions:
            break

        subject = concept["subject"]
        answer = concept["answer"]
        relation = concept["relation"]

        subject_key = subject.lower().strip()

        if subject_key in used_subjects:
            continue

        distractors = get_distractors(answer, concepts)

        if len(distractors) < 3:
            continue

        question_text = make_question(
            subject,
            answer,
            relation,
            difficulty
        )

        question_key = question_text.lower().strip()

        if question_key in used_questions:
            continue

        options = [answer] + distractors
        random.shuffle(options)

        questions.append({
            "question": question_text,
            "options": options,
            "answer": answer
        })

        used_questions.add(question_key)
        used_subjects.add(subject_key)

    return questions
