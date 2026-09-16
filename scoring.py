import streamlit as st
from text_processor import extract_text_from_pdf, clean_text
from quiz_generator import generate_quiz

st.set_page_config(
    page_title= "QuizCraft",
    page_icon= "🧠"
)
st.markdown("""
<style>

    /* App background and font */
    .stApp {
        font-family: Arial, sans-serif;
        background-color: #f3efff;
        color: #222222;
    }

    .stMarkdown {
        color: #222222 !important;
        }

    h1 { 
        text-align :center;
        color: #222222 !important;
        font-size: 45px;
        font-weight: bold;}

    /* Main title and all headings */
    h1, h2, h3, h4 {
        color: #222222;
        }

    /*normal text*/
    p, span, label {
        color: #222222;
        }   
  
    /* Radio button options */
    .stRadio label {
        color: #222222 !important;
    }  

    /* pdf upload */
    .stFileUploader label {
    color: #222222
    }
    
    .stFileUploader button {
    color: #222222 !important;
    background-color : white !important;
    }


    /* Button styling */
    .stButton > button {
        background-color: white !important;
        color: #222222 !important;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px 20px;
        width: 100%;
        font-size: 16px;
    }

    /* Input boxes */
    .stTextInput > div > div,
    .stTextArea > div > div,
    .stSelectbox > div > div {
        border-radius: 10px;
    }

    /* Text area */
    .stTextArea textarea {
        min-height: 180px;
        background-color: white !important;
        color: #222222 !important;
    }

    /* Section headings */
    h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #222222;
    }

    /* Subheading */
    h2 {
        margin-top: 10px;
        margin-bottom: 15px;
        color: #222222;
    }

    /* Input labels */
    label {
        font-weight: bold;
        color: #222222;
    }

</style>
""", unsafe_allow_html=True)


st.title("QuizCraft")

st.subheader("Smart quiz generator")
st.write("Generate quiz from your study material")

st.markdown("### Choose your input.")

input_type = st.radio(
    "How do you want to provide your study material?",
    ["upload PDF", "Enter text"],
    key= "input_type"
)

if "last_input_type" not in st.session_state:
    st.session_state.last_input_type = input_type

if st.session_state.last_input_type != input_type:
    st.session_state.quiz = None
    st.session_state.last_input_type = input_type
    
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
cleaned_text = ""
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
if "quiz" not in st.session_state:
   st.session_state.quiz = None

if st.button("Generate quiz"):
     st.session_state.quiz = generate_quiz(
      cleaned_text,
      Topic,
      Difficulty,
      number_of_questions
   )
     st.success("Quiz generated successfully")

if st.session_state.quiz:
   for i, q in enumerate(st.session_state.quiz):
      st.write(q["question"])

      answer = st.radio(
         "choose your answer:",
         q["options"],
         index=None,
         key = f"question_{i}"
      )
      
      
if st.button("Submit Quiz"):
    score = 0 
    for i, q in enumerate(st.session_state.quiz):
      user_answer = st.session_state.get(f"question_{i}")      

      if user_answer == q["answer"]:
         score += 1
    st.success(f"Your Score: {score}/{len(st.session_state.quiz)}")

  

       


