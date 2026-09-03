import streamlit as st
from text_processor import extract_text_from_pdf, clean_text

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
st.markdown("### Number of Questions")
number_of_questions = st.number_input(
    "How many Questions do you want?",
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
    if pdf_file:
        extracted_text = extract_text_from_pdf(pdf_file)
        cleaned_text = clean_text(extracted_text)

        st.success("PDF uploaded successfully")

        st.write("processed Text:")
        st.write(cleaned_text)
else:
    text = st.text_area(
        "Enter your study material",
        height = 200
    )
if st.button("process text"):
    if text:
        cleaned_text = clean_text(text) 



        st.success("Text processed successfully")
        st.write("processed text:")
        st.write(cleaned_text)
    else:
        st.error("please enter some text first")

st.markdown("### Generate quiz")
if st.button("Generate quiz"):
    st.success("Quiz generated started!")        
       


