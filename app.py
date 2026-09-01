import streamlit as st

st.set_page_config(
    page_title= "QuizCraft",
    page_icon= "🧠"
)
st.title("QuizCraft")
st.divider()
st.subheader("Smart quiz generator")
st.write("Generate quiz from your study material")

st.markdown("### Choose your input.")
input_type = st.radio(
    "How do you want to provide your study material?",
    ["upload PDF", "Enter text"]
)
number_of_questions = st.number_input(
    "Number of questions",
    min_value = 5,
    max_value = 30,
    value = 10,
    step = 1
)
Topic = st.selectbox(
    "select your topic",
    [
        "Python",
        "C programming",
        "Digital electronics",
        "Computer Networks",
        "Database",
        "Other"
    ]
)
st.markdown("### Select Difficulty.")
Difficulty = st.radio(
    "Choose your difficulty level",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)
st.markdown("### Study material")
if input_type == "upload PDF":
    pdf_file = st.file_uploader(
        "Upload your PDF",
        type = ["pdf"]
    )
else:
    text = st.text_area(
        "Enter your study material",
        height = 200
    )


