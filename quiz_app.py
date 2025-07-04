import streamlit as st

st.set_page_config(page_title="Paperbacks & Snacks Quiz", page_icon="📚")

st.title("📚 Paperbacks and Snacks 6 Month Recs Quiz")
st.write("Welcome to the highlights reel! Answer the following 10 very normal, very serious questions to find your next perfect read, based on the FB group thread of our half-way-highlights!")

# Store answers using Streamlit's session state
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Question 1
st.subheader("Question 1")

q1 = st.radio(
    "You meet your future self in a dream. They offer one cryptic sentence. What is it?:",
    options=[
        "A) You were right to eat the forbidden cheese.",
        "B) All your timelines converge in noodle aisle.",
        "C) Your story wasn’t about love — it was about survival.",
        "D) Let them think you’re from Birmingham. It’s safer that way.",
        "E) The archive knows. The archive always knows."
    ]
)

# Store the selected answer
st.session_state.answers["q1"] = q1[0]  # stores just the letter (A, B, etc.)

# temporary checking
st.write("Current answers:", st.session_state.answers)

