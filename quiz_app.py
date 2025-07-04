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
            "B) All your timelines converge in the noodle aisle.",
            "C) Your story wasn’t about love—it was about fajitas and survival.",
            "D) Let them think you’re from Liverpool. It’s safer that way.",
            "E) The archive knows. The archive always knows."
        ]
    },
    {
        "question": "You gain the power to instantly understand one subject. What do you pick?",
        "options": [
            "A) How dragon mythology has influenced 90s boy band choreography",
            "B) The entire DSM-5, but emotionally, not intellectually",
            "C) How to ghostwrite your own autobiography",
            "D) Quantum physics as it relates to that cool shiny paint you see on cars sometimes",
            "E) How to take a bangin selfie and dismantle capitalism at the same time"
        ]
    },
    {
        "question": "You’re at a dinner party where everyone is a fictional character. You sit next to…",
        "options": [
            "A) A morally gray swordsman who writes gay poetry",
            "B) A queer cousin who wants gossip but ends up trauma-dumping",
            "C) A ghost who makes artisanal jams and breads",
            "D) A therapist with an identity crisis and bottomless bellinis",
            "E) A raccoon with a PowerPoint on systemic oppression"
        ]
    },
    {
        "question": "Pick your side hustle:",
        "options": [
            "A) Selling personalised AI-generated memes to Boomers",
            "B) Recording a podcast called “Intergenerational Baggage”, featuring guests and their parents",
            "C) Reading personalised fanfic out loud at weddings",
            "D) An undercover K-pop lyricist and producer",
            "E) Coaching villains through their redemption arcs"
        ]
    },
    {
        "question": "A strange smell wafts into your room. It reminds you of…",
        "options": [
            "A) Grief and garlic",
            "B) Ozone, regret, and printer ink",
            "C) Grandma’s house—but post-apocalyptic",
            "D) Spicy noodles and unspoken feelings",
            "E) That one tumblr post that lives in your head rent-free"
        ]
    },
    {
        "question": "A haunted vending machine gives you one free item. It is:",
        "options": [
            "A) A USB containing your childhood memories, redacted",
            "B) A ticket to a concert that never happened",
            "C) A book you didn’t write but that’s about you",
            "D) A fan-made K-drama starring you and your nemesis",
            "E) A jar of water labelled “Unsent Tears”"
        ]
    },
    {
        "question": "You must choose a familiar to guide you. Who do you pick?",
        "options": [
            "A) A turtle with a dark, mysterious past",
            "B) A talking bonsai that calls you “champ”",
            "C) A cloud of bees that quotes Virginia Woolf",
            "D) A glow-in-the-dark axolotl that goes dark when it senses at injustice",
            "E) A possum with a PhD in gender studies"
        ]
    },
    {
        "question": "You’re invited to a secret society. Their motto is:",
        "options": [
            "A) “We cry in the club.”",
            "B) “No gods, no managers, just deeply cursed crafts.”",
            "C) “This is not a phase. It’s an aesthetic.”",
            "D) “Meeting adjourned. We ride at dusk.”",
            "E) “The prophecy was a vibe check.”"
        ]
    },
    {
        "question": "Your theme song right now is:",
        "options": [
            "A) A lo-fi remix of a dog training video",
            "B) A kazoo rendition of a breakup text",
            "C) A dissonant cello piece titled “Capitalism Was a Mistake”",
            "D) Synthy space pop with Latin choir vocals",
            "E) An anime opening with violin and yelling"
        ]
    },
    {
        "question": "You unlock a superpower, but it only works when you're emotional. It is:",
        "options": [
            "A) Summoning extinct animals that judge your decision making then disappear",
            "B) Channeling sarcasm into protective force fields",
            "C) Telepathy, but only for feelings you haven't processed",
            "D) Causing the closest speaker to play your internal monologue, but as ASMR",
            "E) You're amazing at a Morse code that only birds understand."
        ]
    }
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

