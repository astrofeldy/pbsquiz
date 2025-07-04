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

At 24, Hera is a violently unsatisfied disaster. To her, the future is nothing but an exhausting thought exercise, one depressing hypothetical after another. She's a mean little thing, adrift in her own smug malaise, until her new job as an "online community moderator" of a news outlet's online comment section-a job even more mind-numbing than it sounds-introduces her to Arthur, a middle-aged journalist. Though she's preferred women to men for years now, she relishes becoming a cliché as their mutual infatuation quickly festers into affair. She is coming apart with want and loving every second of it! Well, except for the tiny hiccup of Arthur's wife - and that said wife has no idea Hera exists.

With her daringly specific and intimate voice, Gray has created an irresistible and messy love story about the terrible allure of wanting something that promises nothing; about the joys and indignities of coming into adulthood against the pitfalls of the 21st century; and the winding, torturous, and often very funny journey we take in deciding who we are and who we want to be.""",

    "Harriet Tubman: Live in Concert": """**Harriet Tubman: Live in Concert**  
*Fantasy, historical, funny, fast-paced fiction.*

A blend of history and fantasy with humor, celebrating Black resilience and queer identity.

She calls upon Darnell Williams, a once successful hip-hop producer who was topping the charts before being outed by a rival at the BET Awards. Darnell has no idea what to expect when he steps into the studio with Harriet, only that they have one week to write a Broadway caliber musical she can take on the road. Over the course of their time together, they not only mount a show that will take the country by storm, but confront the horrors of both their pasts, and learn to find a way to a better future.
Harriet Tubman and four of the enslaved persons she led to freedom want to tell their story in a unique way—by following in the footsteps of Lin-Manuel Miranda’s Hamilton. Harriet wants to put on a show about her life, and she needs a songwriter to help her.
In an age of miracles where our greatest heroes from history have magically, unexplainably returned to shake us out of our confusion and hate, Harriet Tubman is back, and she has a lot to say.
Original, evocative, and historic, Harriet Tubman: Live in Concert is a landmark achievement that will burrow deep into our hearts (and ears).""",

    "The Work": """**The Work**  
*Emotional, reflective, contemporary fiction.*

A sharp, introspective story of ambition, art, and love in modern relationships.

Lally has invested everything into her gallery in Manhattan and the sacrifices are finally paying off. Pat is a scholarship boy desperate to establish himself in Sydney's antiquities scene. When they meet at New York's Armory Show their chemistry is instant - fighting about art and politics is just foreplay. 

With an ocean between them they try to get back to work, but they're each struggling to balance money and ambition with the love of art that first drew them to their strange industry. Lally is a kingmaker, bringing exciting new talent to the world, so what's the problem if it's also making her rich? Pat can barely make his rent and he isn't sure if he's taking advantage of his clients or if they are taking advantage of him, and which would be worse? Their international affair ebbs and flows like the market, while their aspirations and insecurities are driving them both towards career-ending mistakes.

If love costs and art takes, what price do we pay for wanting it all? The Work is about the biggest intersections of life: of art and commerce, of intimacy and distance, of talent and entitlement, and of labour and privilege. Dazzling, funny and unforgettable, it is an epic and forensic exploration of modern love and passion, politics and power. The Work announces a brilliant new voice in Australian fiction.""",

    "Disorientation": """**Disorientation**  
*Funny, reflective, satirical fiction.*

An academic satire that dives deep into cultural identity, racism, and belonging.

Twenty-nine-year-old PhD student Ingrid Yang is desperate to finish her dissertation on the late canonical poet Xiao-Wen Chou and never read about “Chinese-y” things again. But after years of grueling research, all she has to show for her efforts are junk food addiction and stomach pain. When she accidentally stumbles upon a curious note in the Chou archives one afternoon, she convinces herself it’s her ticket out of academic hell.
But Ingrid’s in much deeper than she thinks. Her clumsy exploits to unravel the note’s message lead to an explosive discovery, upending not only her sheltered life within academia but her entire world beyond it. With her trusty friend Eunice Kim by her side and her rival Vivian Vo hot on her tail, together they set off a roller coaster of mishaps and misadventures, from book burnings and OTC drug hallucinations, to hot-button protests and Yellow Peril 2.0 propaganda. 
In the aftermath, nothing looks the same to Ingrid—including her gentle and doting fiancé, Stephen Greene. When he embarks on a book tour with the super kawaii Japanese author he’s translated, doubts and insecurities creep in for the first time… As the events Ingrid instigated keep spiraling, she’ll have to confront her sticky relationship to white men and white institutions—and, most of all, herself.""",

    "Interior Chinatown": """**Interior Chinatown**  
*Funny, genre-bending fiction.*

A witty critique of race and representation told through the lens of a screenplay format.

Willis Wu doesn’t perceive himself as the protagonist in his own life: he’s merely Generic Asian Man. Sometimes he gets to be Background Oriental Making a Weird Face or even Disgraced Son, but always he is relegated to a prop. Yet every day, he leaves his tiny room in a Chinatown SRO and enters the Golden Palace restaurant, where Black and White, a procedural cop show, is in perpetual production. He’s a bit player here, too, but he dreams of being Kung Fu Guy—the most respected role that anyone who looks like him can attain. Or is it?

After stumbling into the spotlight, Willis finds himself launched into a wider world than he’s ever known, discovering not only the secret history of Chinatown, but the buried legacy of his own family. Infinitely inventive and deeply personal, exploring the themes of pop culture, assimilation, and immigration—Interior Chinatown is Charles Yu’s most moving, daring, and masterful novel yet.""",

    "The Book of Elsewhere": """**The Book of Elsewhere**  
*Dark, genre-blurring fantasy.*

Immortal warriors, mysterious forces, and gritty adventure collide in this mythic epic.

There have always been whispers. Legends. The warrior who cannot be killed. Who’s seen a thousand civilizations rise and fall. He has had many names: Unute, Child of Lightning, Death himself. These days, he’s known simply as “B.”

And he wants to be able to die.

In the present day, a U.S. black-ops group has promised him they can help with that. And all he needs to do is help them in return. But when an all-too-mortal soldier comes back to life, the impossible event ultimately points toward a force even more mysterious than B himself. One at least as strong. And one with a plan all its own.

In a collaboration that combines Miéville’s singular style and creativity with Reeves’s haunting and soul-stirring narrative, these two inimitable artists have created something utterly unique, sure to delight existing fans and to create scores of new ones.""",

    "Jack Charles: Born Again Blakfella": """**Jack Charles: Born Again Blakfella**  
*Emotional, challenging memoir.*

A powerful story of survival, culture, addiction, and redemption by a legendary performer and activist.

Jack Charles has worn many hats throughout his life: actor, cat burglar, musician, heroin addict, activist, even Senior Victorian Australian of the Year. But the title he’s most proud to claim is that of Aboriginal Elder.

Stolen from his mother and placed into institutional care when he was only a few months old, Uncle Jack was raised under the government’s White Australia Policy. The loneliness and isolation he experienced during those years had a devastating impact on him that endured long after he reconnected with his Aboriginal roots and discovered his stolen identity. Even today he feels like an outsider; a loner; a fringe dweller.

In this honest and no-holds-barred memoir, Uncle Jack reveals the ‘ups and downs of this crazy, drugged up, locked up, fucked up, and at times unbelievable, life’. From his sideline as a cat burglar, battles with drug addiction and stints in prison, to gracing the nation’s stages and screens as he dazzled audiences with his big personality and acting prowess, he takes us through the most formative moments of his life.

By turns heartbreaking and hilarious, Jack Charles: Born-again Blakfella is a candid and uplifting memoir from one of Australia’s finest and most beloved actors.""",

    "The True Deceiver": """**The True Deceiver**  
*Mysterious, literary fiction.*

A slow-burning psychological tale of deception, loneliness, and shifting power.

In the deep winter snows of a Swedish hamlet, a strange young woman fakes a break-in at the house of an elderly artist in order to persuade her that she needs companionship. But what does she hope to gain by doing this? And who ultimately is deceiving whom? In this portrayal of two women grappling with truth and lies, nothing can be taken for granted. By the time the snow thaws, both their lives will have changed irrevocably.""",

    "Unmasking Autism": """**Unmasking Autism**  
*Reflective, informative non-fiction.*

A compassionate guide to understanding and embracing neurodivergence and authenticity.

For every visibly Autistic person you meet, there are countless “masked” Autistic people who pass as neurotypical. Masking is a common coping mechanism in which Autistic people hide their identifiably Autistic traits in order to fit in with societal norms, adopting a superficial personality at the expense of their mental health. This can include suppressing harmless stims, papering over communication challenges by presenting as unassuming and mild-mannered, and forcing themselves into situations that cause severe anxiety, all so they aren’t seen as needy or “odd.” 

In Unmasking Autism, Dr. Devon Price shares his personal experience with masking and blends history, social science research, prescriptions, and personal profiles to tell a story of neurodivergence that has thus far been dominated by those on the outside looking in. For Dr. Price and many others, Autism is a deep source of uniqueness and beauty. Unfortunately, living in a neurotypical world means it can also be a source of incredible alienation and pain. Most masked Autistic individuals struggle for decades before discovering who they truly are. They are also more likely to be marginalized in terms of race, gender, sexual orientation, class, and other factors, which contributes to their suffering and invisibility. Dr. Price lays the groundwork for unmasking and offers exercises that encourage self-expression.""",

    "Everything is Tuberculosis": """**Everything is Tuberculosis**  
*Science, history, equity.*

John Green explores global health, human stories, and the weird corners of illness with wit and compassion.

Tuberculosis has been entwined with humanity for millennia. Once romanticized as a malady of poets, today tuberculosis is a disease of poverty that walks the trails of injustice and inequity we blazed for it.
 
In 2019, John Green met Henry, a young tuberculosis patient at Lakka Government Hospital in Sierra Leone while traveling with Partners in Health. John became fast friends with Henry, a boy with spindly legs and a big, goofy smile. In the years since that first visit to Lakka, Green has become a vocal and dynamic advocate for increased access to treatment and wider awareness of the healthcare inequities that allow this curable, treatable infectious disease to also be the deadliest, killing 1.5 million people every year.
 
In Everything is Tuberculosis, John tells Henry’s story, woven through with the scientific and social histories of how tuberculosis has shaped our world and how our choices will shape the future of tuberculosis.""",

    "The Darkness Outside Us": """**The Darkness Outside Us**  
*Emotional YA sci-fi.*

Enemies-turned-allies must survive alone in deep space, with queer romance and mind-bending mysteries.

Two boys, alone in space. Sworn enemies sent on the same rescue mission.
Ambrose wakes up on the Coordinated Endeavor with no memory of a launch. There’s more that doesn’t add up: evidence indicates strangers have been on board, the ship’s operating system is voiced by his mother, and his handsome, brooding shipmate has barricaded himself away. But nothing will stop Ambrose from making his mission succeed—not when he’s rescuing his own sister.
In order to survive the ship’s secrets, Ambrose and Kodiak will need to work together and learn to trust each other . . . especially once they discover what they are truly up against. Love might be the only way to survive.""",

    "Crying in H Mart": """**Crying in H Mart by SOMEONE**  
    
*An emotional, reflective memoir.*

Michelle Zauner’s bestselling story of grief, culture, food, and the bond between mother and daughter.

In this exquisite story of family, food, grief, and endurance, Michelle Zauner proves herself far more than a dazzling singer, songwriter, and guitarist. With humor and heart, she tells of growing up one of the few Asian American kids at her school in Eugene, Oregon; of struggling with her mother’s particular, high expectations of her; of a painful adolescence; of treasured months spent in her grandmother’s tiny apartment in Seoul, where she and her mother would bond, late at night, over heaping plates of food.
As she grew up, moving to the East Coast for college, finding work in the restaurant industry, and performing gigs with her fledgling band–and meeting the man who would become her husband–her Koreanness began to feel ever more distant, even as she found the life she wanted to live. It was her mother’s diagnosis of terminal cancer, when Michelle was twenty-five, that forced a reckoning with her identity and brought her to reclaim the gifts of taste, language, and history her mother had given her.
Vivacious and plainspoken, lyrical and honest, Zauner’s voice is as radiantly alive on the page as it is onstage. Rich with intimate anecdotes that will resonate widely, and complete with family photos, Crying in H Mart is a book to cherish, share, and reread.""",

    "Greta and Valdin": """**Greta and Valdin**  
*Light-hearted, queer literary fiction.*

A hilarious, touching sibling story about culture, crushes, and growing up in Auckland.

Valdin is still in love with his ex-boyfriend Xabi, who used to drive around Auckland in a ute but now drives around Buenos Aires in one. Greta is in love with her fellow English tutor Holly, who doesn’t know how to pronounce Greta’s surname, Vladisavljevic, properly.

From their Auckland apartment, brother and sister must navigate the intricate paths of modern romance as well as weather the small storms of their eccentric Māori–Russian–Catalonian family. This beguiling and hilarious novel by Adam Foundation Prize winner Rebecca K Reilly owes as much to Shakespeare as it does to Tinder. Set in a world that is deeply familiar (but also a bit sexier and more stylish than the real one), Greta and Valdin will speak to anyone who has had their heart broken, or has decided that they don’t want to be a physicist anymore, or has wondered about all of the things they don’t know about their family.""",

    "Ask Helen about Fanfic": """**Ask Helen about Fanfic**  
*A genre recommendation via Helen.*

Chaotic queer romance meets anime energy and moral depth. This isn't a single book, but instead a reminder to ask Helen about fanfic — they have recs. Many.
"""
}


personality_matches = {
    "Green Dot": """**the overthinker in a spiral, but you're still making jokes.**

Loves a bit of heartbreak with a slice of chaotic romance. You’re smart, self-aware, and deeply committed to bad decisions — but with taste. You flirt via existential memes and keep a well-thumbed copy of something sad in your tote bag.""",

    "The Work": """**"emotionally sincere but academically intense."**

Probably falling in love with someone at a gallery opening or during a philosophical argument. You drink long blacks and think capitalism should be more ethical (but hotter). Your red flags are well-curated and you think about them during pilates.""",

    "Disorientation": """**"the burnout academic with a meme folder and a grudge."**

You’ve been in a department meeting that became a class war. You survive by deploying humour, calling out nonsense, and getting a little unhinged in the group chat. You use footnotes *and* chaos to make a point.""",

    "The True Deceiver": """**giving "mysterious girl autumn."**

You’ve been described as ‘quietly intimidating.’ You bake sourdough as a power move. You trust no one, love sparingly, and probably live near a forest (or wish you did).""",

    "The Darkness Outside Us": """**the queer disaster with too many feelings.**

You're trapped in a space mission *and* your own emotional growth arc. You want to scream “what is happening??” — but only after making out with your nemesis. You believe in love, even if it’s encrypted.""",

    "Interior Chinatown": """**satirical, stylish, and silently keeping score.**

You see the system. You’ve memorized the script. And now? You’re flipping the narrative. You hold contradictions like a pro and weaponise awkward silence for justice.""",

    "Harriet Tubman: Live in Concert": """**the history nerd who straight up slays.**

You love a mash-up of revolution, glitter, and liberation. You’re here for Black excellence, queer joy, and the audacity to reimagine the past with power and play. Time travel is real and it’s called drag.""",

    "Crying in H Mart": """**a tender soul with a memory for smells.**

You hold grief in one hand and a spoon in the other. You feel things hard, love deeply, and know that recipes are rituals. You’ve cried in public and made it poetic.""",

    "Greta and Valdin": """**bringing the chaos, but also the charisma.**

You're juggling dating apps, family group chats, and a too-intense crush, all with stunning outfits and solid jokes. Your mess is lovable, and you know it. People fall in love with you at brunch.""",

    "Unmasking Autism": """**self-aware, boundary-setting, and done with masking. And if that doesn't immediately resonate, we may have some news for you.**

You're learning how to exist in a world that doesn't always get it — and doing it with clarity, courage, and maybe a new spreadsheet system for your special interests. You’re tired of pretending, and that’s your power.""",

    "The Book of Elsewhere": """**an ancient soul in a modern timeline.**

You’ve lived a thousand lives, each with a sword and a tragic backstory. You’re not afraid of darkness — you *are* the darkness. You’re collecting scars like souvenirs and still look great in leather.""",

    "Everything is Tuberculosis": """**the earnest explainer friend, and we love you for it.**

You read footnotes and cry about access to medication. You bring the big picture *and* the fun facts. You’ve made three spreadsheets and one infographic about injustice today.""",

    "Ask Helen about Fanfic": """**queer-coded, deeply online, and suspiciously emotionally literate.**

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

#        st.markdown("📚 Your top recommended read:")


        # Display personality match
        st.markdown(f"### You're {personality_matches.get(top_book)}")
        st.markdown(f"### 🥇 Your half-way-hero book match is: **{top_book}**")
        
        # Display header before book description
        # st.markdown(f"**More about your half-way-hero book match:**")

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

