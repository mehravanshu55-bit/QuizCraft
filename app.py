import streamlit as st
from database import (
    create_users_table, create_history_table, add_user,
    check_login, save_quiz_history, get_quiz_history
)
from text_processor import extract_text_from_pdf, clean_text
from quiz_generator import generate_quiz

create_users_table()
create_history_table()

st.set_page_config(page_title="QuizCraft", page_icon="🧠", layout="wide")

st.markdown("""
<style>
.stApp{background:#0B1F3A;color:white}

.block-container{max-width:1100px;padding:3rem 4rem 4rem}

h1{color:white!important;text-align:center;margin-bottom:30px}

h2{color:#DCE7FF!important;margin:30px 0 20px}

h3{color:#9DBBFF!important;margin:25px 0 18px}

p{color:#D7E2F5;line-height:1.7}

.stButton{margin:12px 0 18px}

.stButton>button{width:100%;min-height:46px;background:#2563EB;color:white;border-radius:10px;border:1px solid #5D8DFF;font-weight:600}

.stButton>button:hover{background:#1D4ED8;color:white}

.stTextInput,.stTextArea,.stSelectbox,.stRadio,.stFileUploader{margin-bottom:22px}

.stTextInput input,.stTextArea textarea{background:#162E52;color:white;border:1px solid #4169A1;border-radius:10px}

[data-testid="stSidebar"]{background:#08172C}

[data-testid="stVerticalBlockBorderWrapper"]{background:#12294A;border:1px solid #294A7A;border-radius:15px;padding:25px;margin:15px 0 25px}

</style>
""", unsafe_allow_html=True)

defaults = {
    "page": "home",
    "logged_in": False,
    "username": "",
    "quiz": None,
    "current_question": 0,
    "answers": {},
    "quiz_submitted": False,
    "history_saved": False,
    "quiz_topic": "",
    "quiz_difficulty": "",
    "quiz_question_count": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def reset_quiz():
    st.session_state.quiz = None
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.history_saved = False
    st.session_state.quiz_topic = ""
    st.session_state.quiz_difficulty = ""
    st.session_state.quiz_question_count = 0


def go_to(page):
    st.session_state.page = page
    st.rerun()


if st.session_state.page == "home":

    st.title("🧠 QuizCraft")
    st.subheader("Smart Quiz Generator")
    st.write("Turn your study material into an interactive quiz.")
    st.divider()
    st.subheader("Why QuizCraft?")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("📄 PDF & Text")
            st.write("Enter your notes or upload a PDF as study material.")

    with col2:
        with st.container(border=True):
            st.subheader("🎯 Smart Quiz")
            st.write("Generate questions according to topic and difficulty.")

    with col3:
        with st.container(border=True):
            st.subheader("📊 Results")
            st.write("Complete the quiz and check your performance.")

    st.divider()
    st.subheader("Get Started")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Login"):
            go_to("login")

    with col2:
        if st.button("✨ Sign Up"):
            go_to("signup")


elif st.session_state.page == "login":

    st.title("🔐 Login")

    col1, col2, col3 = st.columns([1, 1.4, 1])

    with col2:
        with st.container(border=True):

            st.subheader("Welcome Back")

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            if st.button("Login →"):

                if not username or not password:
                    st.error("Please enter username and password.")

                elif check_login(username, password):

                    st.session_state.username = username
                    st.session_state.logged_in = True
                    reset_quiz()
                    go_to("dashboard")

                else:
                    st.error("Invalid username or password.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back to Home"):
            go_to("home")

    with col2:
        if st.button("Create Account"):
            go_to("signup")


elif st.session_state.page == "signup":

    st.title("✨ Create Account")

    col1, col2, col3 = st.columns([1, 1.4, 1])

    with col2:
        with st.container(border=True):

            st.subheader("Join QuizCraft")

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            username = st.text_input(
                "Username",
                placeholder="Choose a username"
            )

            email = st.text_input(
                "Email",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Create a password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Confirm your password"
            )

            if st.button("Create Account →"):

                if not all([name, username, email, password]):
                    st.error("Please fill all fields.")

                elif password != confirm_password:
                    st.error("Passwords do not match.")

                elif add_user(name, username, email, password):

                    st.success("Account created successfully! 🎉")

                    st.session_state.username = username
                    st.session_state.logged_in = True
                    reset_quiz()
                    go_to("dashboard")

                else:
                    st.error("Username or email already exists.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back to Home"):
            go_to("home")

    with col2:
        if st.button("Already have an account? Login"):
            go_to("login")


elif st.session_state.page in ["dashboard", "history"]:

    with st.sidebar:

        st.title("🧠 QuizCraft")
        st.write(f"Welcome, {st.session_state.username} 👋")
        st.divider()

        if st.button("🏠 Home"):
            go_to("home")

        if st.button("📝 Create Quiz"):
            reset_quiz()
            go_to("dashboard")

        if st.button("📊 Quiz History"):
            go_to("history")

        st.divider()

        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            reset_quiz()
            go_to("home")


    if st.session_state.page == "history":

        st.title("📊 Quiz History")

        history = get_quiz_history(
            st.session_state.username
        )

        if history:

            st.subheader("Your Previous Quizzes")

            for record in history:

                topic, difficulty, total, score, percentage, date = record

                with st.container(border=True):

                    st.subheader(f"📝 {topic}")

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.write(f"**Difficulty**\n\n{difficulty}")

                    with col2:
                        st.write(f"**Score**\n\n{score}/{total}")

                    with col3:
                        st.write(f"**Percentage**\n\n{percentage:.1f}%")

                    with col4:
                        st.write(f"**Date**\n\n{date}")

        else:

            st.info(
                "No quiz history available yet. "
                "Complete a quiz to see it here."
            )


    else:

        st.title("Welcome to QuizCraft 🧠")
        st.write("Create a personalized quiz from your study material.")
        st.divider()
        st.subheader("📝 Create Your Quiz")

        input_type = st.radio(
            "Choose Study Material",
            ["Enter Text", "Upload PDF"],
            horizontal=True
        )

        text = ""

        if input_type == "Enter Text":

            text = st.text_area(
                "Enter your study material",
                height=220,
                placeholder="Paste your notes here..."
            )

        else:

            pdf_file = st.file_uploader(
                "Upload your PDF",
                type=["pdf"]
            )

            if pdf_file:
                text = extract_text_from_pdf(pdf_file)

        topic = st.text_input(
            "Topic",
            placeholder="Example: Information Systems"
        )

        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

        question_count = st.selectbox(
            "Number of Questions",
            [5, 10, 15]
        )

        if st.button("🎯 Generate Quiz"):

            if not text.strip():
                st.error("Please enter text or upload a PDF.")

            elif not topic.strip():
                st.error("Please enter a topic.")

            else:

                try:

                    cleaned_text = clean_text(text)

                    quiz = generate_quiz(
                        cleaned_text,
                        topic,
                        difficulty,
                        question_count
                    )

                    if quiz:

                        st.session_state.quiz = quiz
                        st.session_state.current_question = 0
                        st.session_state.answers = {}
                        st.session_state.quiz_submitted = False
                        st.session_state.history_saved = False
                        st.session_state.quiz_topic = topic
                        st.session_state.quiz_difficulty = difficulty
                        st.session_state.quiz_question_count = len(quiz)

                        st.success("Quiz generated successfully! 🎉")

                    else:
                        st.error(
                            "Quiz could not be generated. "
                            "Please provide more study material."
                        )

                except Exception as e:
                    st.error(f"Quiz generation error: {e}")


        if st.session_state.quiz and not st.session_state.quiz_submitted:

            quiz = st.session_state.quiz
            current = st.session_state.current_question

            st.divider()
            st.subheader("🎯 Your Quiz")

            if current < len(quiz):

                question = quiz[current]

                st.write(
                    f"### Question {current + 1} of {len(quiz)}"
                )

                st.write(question["question"])

                answer = st.radio(
                    "Choose your answer:",
                    question["options"],
                    key=f"answer_{current}"
                )

                st.session_state.answers[current] = answer

                if current < len(quiz) - 1:

                    if st.button("Next →"):
                        st.session_state.current_question += 1
                        st.rerun()

                else:

                    if st.button("Submit Quiz 🎉"):
                        st.session_state.quiz_submitted = True
                        st.rerun()


        if st.session_state.quiz and st.session_state.quiz_submitted:

            quiz = st.session_state.quiz
            score = 0

            for i, question in enumerate(quiz):

                user_answer = st.session_state.answers.get(i)

                if user_answer == question.get("answer"):
                    score += 1

            total = len(quiz)
            wrong = total - score
            percentage = (score / total) * 100

            if not st.session_state.history_saved:

                save_quiz_history(
                    st.session_state.username,
                    st.session_state.quiz_topic,
                    st.session_state.quiz_difficulty,
                    total,
                    score,
                    percentage
                )

                st.session_state.history_saved = True

            st.divider()
            st.title("🏆 Quiz Result")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Score", f"{score}/{total}")

            with col2:
                st.metric("Correct", score)

            with col3:
                st.metric("Wrong", wrong)

            st.metric("Percentage", f"{percentage:.1f}%")

            if percentage >= 80:
                st.success("Excellent work! 🌟")

            elif percentage >= 50:
                st.info("Good effort! Keep practicing. 👍")

            else:
                st.warning("Keep practicing and try again. 💪")

            st.divider()
            st.subheader("📋 Question Review")

            for i, question in enumerate(quiz):

                user_answer = st.session_state.answers.get(i)
                correct_answer = question.get("answer")

                st.write(f"### Question {i + 1}")
                st.write(question["question"])
                st.write(f"**Your Answer:** {user_answer}")
                st.write(f"**Correct Answer:** {correct_answer}")

                if user_answer == correct_answer:
                    st.success("✅ Correct")
                else:
                    st.error("❌ Wrong")

                st.divider()

            if st.button("🔄 Create New Quiz"):
                reset_quiz()
                st.rerun()
