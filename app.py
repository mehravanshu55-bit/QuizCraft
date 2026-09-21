import streamlit as st
from database import (
    create_users_table, create_history_table, add_user,
    check_login, save_quiz_history, get_quiz_history
)
from text_processor import extract_text_from_pdf, clean_text
from quiz_generator import generate_quiz

create_users_table()
create_history_table()

st.set_page_config(
    page_title="QuizCraft",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp{background:#0B1F3A;color:white}
.block-container{max-width:1100px;padding:3rem 4rem 4rem}
h1{color:white!important;text-align:center;margin-bottom:30px}
h2{color:#DCE7FF!important;margin:30px 0 20px}
h3{color:#9DBBFF!important;margin:25px 0 18px}
p{color:#D7E2F5;line-height:1.7}
.stButton{margin:12px 0 18px}
.stButton>button{
    width:100%;
    min-height:46px;
    background:#2563EB;
    color:white;
    border-radius:10px;
    border:1px solid #5D8DFF;
    font-weight:600
}
.stButton>button:hover{
    background:#1D4ED8;
    color:white
}
.stTextInput,.stTextArea,.stSelectbox,
.stRadio,.stFileUploader{
    margin-bottom:22px
}
.stTextInput input,
.stTextArea textarea{
    background:#162E52;
    color:white;
    border:1px solid #4169A1;
    border-radius:10px
}
[data-testid="stSidebar"]{
    background:#08172C
}
[data-testid="stVerticalBlockBorderWrapper"]{
    background:#12294A;
    border:1px solid #294A7A;
    border-radius:15px;
    padding:25px;
    margin:15px 0 25px
}
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
