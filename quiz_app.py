import streamlit as st

st.set_page_config(page_title="Paperbacks & Snacks Quiz", page_icon="📚")

# markdown
st.markdown(
    "<h2 style='color:#FF69B4; font-family:Comic Sans MS;'>✨ Paperbacks and Snacks: The Half-Way-Highlights Quiz!</h2>",
    unsafe_allow_html=True
)

#st.title("📚 Paperbacks and Snacks 6 Month Recs Quiz!")
st.write("Welcome to the highlights reel! Answer the following 10 very normal, very serious questions to find your next perfect read, based on the FB group thread of our half-way-highlights!")

# Store answers using Streamlit's session state
if "answers" not in st.session_state:
    st.session_state.answers = {}

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

