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
            "B) The entire DSM-5, but either emotionally or intellectually, never both",
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

scoring = {
    "q1": {
        "A": ["Green Dot", "The True Deceiver"],
        "B": ["Crying in H Mart", "Ask Helen about Fanfic"],
        "C": ["The Darkness Outside Us", "The Work"],
        "D": ["Disorientation", "Jack Charles: Born Again Blakfella"],
        "E": ["Interior Chinatown", "The Book of Elsewhere"]
    },
    "q2": {
        "A": ["The Book of Elsewhere", "Greta and Valdin"],
        "B": ["Unmasking Autism", "Crying in H Mart"],
        "C": ["The Work", "Ask Helen about Fanfic"],
        "D": ["The Darkness Outside Us", "Everything is Tuberculosis"],
        "E": ["Disorientation", "Interior Chinatown"]
    },
    "q3": {
        "A": ["The True Deceiver", "The Book of Elsewhere"],
        "B": ["Jack Charles: Born Again Blakfella", "Crying in H Mart"],
        "C": ["Greta and Valdin", "Ask Helen about Fanfic"],
        "D": ["The Work", "Disorientation"],
        "E": ["Unmasking Autism", "Interior Chinatown"]
    },
    "q4": {
        "A": ["Interior Chinatown", "The Book of Elsewhere"],
        "B": ["Unmasking Autism", "Everything is Tuberculosis"],
        "C": ["Ask Helen about Fanfic", "Greta and Valdin"],
        "D": ["Disorientation", "Green Dot"],
        "E": ["The True Deceiver", "The Darkness Outside Us"]
    },
    "q5": {
        "A": ["Crying in H Mart", "Jack Charles: Born Again Blakfella"],
        "B": ["The Work", "Unmasking Autism"],
        "C": ["The True Deceiver", "The Book of Elsewhere"],
        "D": ["Green Dot", "Greta and Valdin"],
        "E": ["Ask Helen about Fanfic", "Disorientation"]
    },
    "q6": {
        "A": ["The Work", "Green Dot"],
        "B": ["Greta and Valdin", "Everything is Tuberculosis"],
        "C": ["The True Deceiver", "Crying in H Mart"],
        "D": ["Ask Helen about Fanfic", "The Darkness Outside Us"],
        "E": ["Interior Chinatown", "Disorientation"]
    },
    "q7": {
        "A": ["The True Deceiver", "Jack Charles: Born Again Blakfella"],
        "B": ["Greta and Valdin", "The Work"],
        "C": ["Interior Chinatown", "Unmasking Autism"],
        "D": ["The Darkness Outside Us", "Ask Helen about Fanfic"],
        "E": ["Disorientation", "Green Dot"]
    },
    "q8": {
        "A": ["Green Dot", "Greta and Valdin"],
        "B": ["Ask Helen about Fanfic", "Disorientation"],
        "C": ["Interior Chinatown", "The Work"],
        "D": ["The Book of Elsewhere", "Everything is Tuberculosis"],
        "E": ["The True Deceiver", "Unmasking Autism"]
    },
    "q9": {
        "A": ["Unmasking Autism", "Green Dot"],
        "B": ["Disorientation", "Ask Helen about Fanfic"],
        "C": ["The Darkness Outside Us", "The Book of Elsewhere"],
        "D": ["Everything is Tuberculosis", "Interior Chinatown"],
        "E": ["Greta and Valdin", "Crying in H Mart"]
    },
    "q10": {
        "A": ["The Book of Elsewhere", "The True Deceiver"],
        "B": ["Disorientation", "Ask Helen about Fanfic"],
        "C": ["Unmasking Autism", "Jack Charles: Born Again Blakfella"],
        "D": ["The Darkness Outside Us", "Greta and Valdin"],
        "E": ["Crying in H Mart", "Everything is Tuberculosis"]
    }
}

book_info = {
    "Green Dot": """**Green Dot**  
*Emotional, funny, contemporary fiction.*

A darkly humorous and emotionally raw story of young adulthood, complicated relationships, and self-discovery.

PLACEHOLDER""",

    "Harriet Tubman: Live in Concert": """**Harriet Tubman: Live in Concert**  
*Fantasy, historical, funny, fast-paced fiction.*

A blend of history and fantasy with humor, celebrating Black resilience and queer identity.

PLACEHOLDER""",

    "The Work": """**The Work**  
*Emotional, reflective, contemporary fiction.*

A sharp, introspective story of ambition, art, and love in modern relationships.

PLACEHOLDER""",

    "Disorientation": """**Disorientation**  
*Funny, reflective, satirical fiction.*

An academic satire that dives deep into cultural identity, racism, and belonging.

PLACEHOLDER""",

    "Interior Chinatown": """**Interior Chinatown**  
*Funny, genre-bending fiction.*

A witty critique of race and representation told through the lens of a screenplay format.

PLACEHOLDER""",

    "The Book of Elsewhere": """**The Book of Elsewhere**  
*Dark, genre-blurring fantasy.*

Immortal warriors, mysterious forces, and gritty adventure collide in this mythic epic.

PLACEHOLDER""",

    "Jack Charles: Born Again Blakfella": """**Jack Charles: Born Again Blakfella**  
*Emotional, challenging memoir.*

A powerful story of survival, culture, addiction, and redemption by a legendary performer and activist.

PLACEHOLDER""",

    "The True Deceiver": """**The True Deceiver**  
*Mysterious, literary fiction.*

A slow-burning psychological tale of deception, loneliness, and shifting power.

PLACEHOLDER""",

    "Unmasking Autism": """**Unmasking Autism**  
*Reflective, informative non-fiction.*

A compassionate guide to understanding and embracing neurodivergence and authenticity.

PLACEHOLDER""",

    "Everything is Tuberculosis": """**Everything is Tuberculosis**  
*Science, history, equity.*

John Green explores global health, human stories, and the weird corners of illness with wit and compassion.

PLACEHOLDER""",

    "The Darkness Outside Us": """**The Darkness Outside Us**  
*Emotional YA sci-fi.*

Enemies-turned-allies must survive alone in deep space, with queer romance and mind-bending mysteries.

PLACEHOLDER""",

    "Crying in H Mart": """**Crying in H Mart**  
    
*An emotional, reflective memoir.*

Michelle Zauner’s bestselling story of grief, culture, food, and the bond between mother and daughter.

PLACEHOLDER""",

    "Greta and Valdin": """**Greta and Valdin**  
*Light-hearted, queer literary fiction.*

A hilarious, touching sibling story about culture, crushes, and growing up in Auckland.

PLACEHOLDER""",

    "Ask Helen about Fanfic": """**Ask Helen about Fanfic**  
*A genre recommendation via Helen.*

Chaotic queer romance meets anime energy and moral depth. Ask Helen — she has recs.

PLACEHOLDER"""
}


personality_matches = {
    "Green Dot": """**"The overthinker in a spiral, but still making jokes."**

Loves a bit of heartbreak with a slice of chaotic romance. You’re smart, self-aware, and deeply committed to bad decisions — but with taste. You flirt via existential memes and keep a well-thumbed copy of something sad in your tote bag.""",

    "The Work": """**"Emotionally sincere but academically intense."**

Probably falling in love with someone at a gallery opening or during a philosophical argument. You drink long blacks and think capitalism should be more ethical (but hotter). Your red flags are well-curated and you think about them during pilates.""",

    "Disorientation": """**"The burnout academic with a meme folder and a grudge."**

You’ve been in a department meeting that became a class war. You survive by deploying humour, calling out nonsense, and getting a little unhinged in the group chat. You use footnotes *and* chaos to make a point.""",

    "The True Deceiver": """**"Mysterious girl autumn."**

You’ve been described as ‘quietly intimidating.’ You bake sourdough as a power move. You trust no one, love sparingly, and probably live near a forest (or wish you did).""",

    "The Darkness Outside Us": """**"The queer disaster astronaut with too many feelings."**

You're trapped in a space mission *and* your own emotional growth arc. You want to scream “what is happening??” — but only after making out with your nemesis. You believe in love, even if it’s encrypted.""",

    "Interior Chinatown": """**"Satirical, stylish, and silently keeping score."**

You see the system. You’ve memorized the script. And now? You’re flipping the narrative. You hold contradictions like a pro and weaponise awkward silence for justice.""",

    "Harriet Tubman: Live in Concert": """**"The history nerd who slays."**

You love a mash-up of revolution, glitter, and liberation. You’re here for Black excellence, queer joy, and the audacity to reimagine the past with power and play. Time travel is real and it’s called drag.""",

    "Crying in H Mart": """**"Tender soul with a memory for smells."**

You hold grief in one hand and a spoon in the other. You feel things hard, love deeply, and know that recipes are rituals. You’ve cried in public and made it poetic.""",

    "Greta and Valdin": """**"Chaos with charisma."**

You're juggling dating apps, family group chats, and a too-intense crush, all with stunning outfits and solid jokes. Your mess is lovable, and you know it. People fall in love with you at brunch.""",

    "Unmasking Autism": """**"Self-aware, boundary-setting, and done with masking."**

You're learning how to exist in a world that doesn't always get it — and doing it with clarity, courage, and maybe a new spreadsheet system for your special interests. You’re tired of pretending, and that’s your power.""",

    "The Book of Elsewhere": """**"Ancient soul in a modern timeline."**

You’ve lived a thousand lives, each with a sword and a tragic backstory. You’re not afraid of darkness — you *are* the darkness. You’re collecting scars like souvenirs and still look great in leather.""",

    "Everything is Tuberculosis": """**"The earnest explainer friend."**

You read footnotes and cry about access to medication. You bring the big picture *and* the fun facts. You’ve made three spreadsheets and one infographic about injustice today.""",

    "Ask Helen about Fanfic": """**"Queer-coded, deeply online, and suspiciously emotionally literate."**

You read character studies like scripture, love a redemption arc, and are somehow both trash and art. You’ve never finished a fic without analyzing it. Also you have *takes*."""
}


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

# tally function
from collections import Counter

def tally_results(answers, scoring):
    tally = Counter()
    for q_key, answer_letter in answers.items():
        matched_books = scoring.get(q_key, {}).get(answer_letter, [])
        tally.update(matched_books)
    return tally

#define how to explain matches
def explain_matches(answers, quiz_data, scoring):
    st.markdown("---")
    st.subheader("📖 Here's how your answers matched your book:")
    for i, q in enumerate(quiz_data):
        q_key = f"q{i+1}"
        user_answer_letter = answers.get(q_key)
        user_answer_text = next((opt for opt in q["options"] if opt.startswith(user_answer_letter)), "N/A")
        matched_books = scoring.get(q_key, {}).get(user_answer_letter, [])

        st.markdown(f"**Q{i+1}. {q['question']}**")
        st.markdown(f"Your answer: *{user_answer_text}*")
        st.markdown(f"→ Matched books: {', '.join(matched_books) if matched_books else 'None'}")
        st.markdown("---")

# Submit button
if st.button("Submit"):
    if len(st.session_state.answers) < len(quiz_data):
        st.warning("Please answer all questions before submitting!")
    else:
        st.success("🎉 You've completed the quiz!")

        # Tally results
        results = tally_results(st.session_state.answers, scoring)
        top_books = results.most_common(3)

        # Display top match with full detail
        top_book = top_books[0][0]

        st.markdown("📚 Your top recommended read:")
        st.markdown(f"### 🥇 **{top_book}**")

        # Display personality match
        st.markdown(personality_matches.get(top_book, ""))

        # Display book synopsis
        st.markdown(book_info.get(top_book, "No synopsis available."))

        st.markdown("---")

        if len(top_books) > 1:
            st.write("Other strong matches:")
            for book, score in top_books[1:]:
                st.markdown(f"**{book}** (matched {score} times)")
                st.markdown(f"_{book_info.get(book, 'No description available.')}_")


        #Show how answers contributed to matches
        explain_matches(st.session_state.answers, quiz_data, scoring)

