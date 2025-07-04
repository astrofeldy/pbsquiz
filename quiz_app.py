import streamlit as st

st.set_page_config(page_title="Paperbacks & Snacks Quiz", page_icon="📚")

# markdown
st.markdown(
    "<h2 style='color:#FF69B4; font-family:Comic Sans MS;'>✨ Paperbacks and Snacks: The Half-Way-Highlights Quiz!</h2>",
    unsafe_allow_html=True
)

#st.title("📚 Paperbacks and Snacks 6 Month Recs Quiz!")
st.write("Welcome to the highlights reel! Answer the following 10 very normal, very serious questions to find your next perfect read, based on the FB group thread of our half-way-highlights!")

# Store answers in session state
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Quiz questions
quiz_data = [
    {
        "question": "You meet your future self in a dream. They offer one cryptic sentence. What is it?",
        "options": [
            "A) You were right to eat the forbidden cheese.",
            "B) All your timelines converge in aisle seven of the Asian grocery.",
            "C) Your story wasn’t about love—it was about survival.",
            "D) Let them think you’re unhinged. It’s safer that way.",
            "E) The archive knows. The archive always knows."
        ]
    },
    {
        "question": "You gain the power to instantly understand one subject. What do you pick?",
        "options": [
            "A) Dragon lore and 90s boy band choreography",
            "B) The entire DSM-5, but emotionally",
            "C) How to ghostwrite your own autobiography",
            "D) Time travel physics for idiots",
            "E) How to take a good selfie and dismantle capitalism at the same time"
        ]
    },
    # Add remaining 8 questions...
]

# Display all questions at once
for i, q in enumerate(quiz_data):
    st.subheader(f"{i + 1}. {q['question']}")
    selected = st.radio(
        "Choose one:",
        options=q["options"],
        key=f"q{i}_radio",
        index=None
    )
    if selected:
        st.session_state.answers[f"q{i+1}"] = selected[0]  # store only the letter A/B/C/etc.

# Submit button
if st.button("Submit"):
    if len(st.session_state.answers) < len(quiz_data):
        st.warning("Please answer all questions before submitting!")
    else:
        st.success("🎉 You've completed the quiz!")
        # Add scoring logic here and show book recommendation
        st.write("📚 Your perfect book match is... [placeholder]")

# Store answers using Streamlit's session state
# if "answers" not in st.session_state:
  #  st.session_state.answers = {}

# Question 1
# st.subheader("Question 1: You meet your future self in a dream. They offer one cryptic sentence. What is it?")

# q1 = st.radio(
 #    "Select your sentence",
   # options=[
    #    "A) You were right to eat the forbidden cheese.",
     #   "B) All your timelines converge in noodle aisle.",
      #  "C) Your story wasn’t about love — it was about survival.",
       # "D) Let them think you’re from Birmingham. It’s safer that way.",
        #"E) The archive knows. The archive always knows."
  #  ],
   # index=None
#)

# next button
# if q1 is not None:
  #  if st.button("Next"):
   #     # Logic to move to the next question
    #    st.session_state.current_question = 2
# else:
  #  st.button("Next", disabled=True)
   # st.warning("Please select an answer to continue.")

# temporary checking
st.write("Current answers:", st.session_state.answers)

