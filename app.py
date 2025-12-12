import streamlit as st

st.set_page_config(page_title="Avengers at Work Survey", page_icon="🦸‍♂️")
st.title("🦸‍♂️ Avengers at Work Survey")
st.write("Answer the following work-style questions and find out which Avenger you channel!")

# Questions and options with Avenger mapping
questions = [
    {
        "q": "Decision-Making & Leadership",
        "options": {
            "Lead with principles, ensure everyone’s on board.": "Captain America",
            "Dive in with bold action and energy.": "Thor",
            "Improvise and adapt on the fly.": "Spider-Man",
            "Strategically plan and innovate with tech/creative solutions.": "Iron Man"
        }
    },
    {
        "q": "Problem-Solving Style",
        "options": {
            "Analyze, gather data, and use resources wisely.": "Black Panther",
            "Smash through obstacles with determination.": "Hulk",
            "Consider multiple dimensions and think outside the box.": "Doctor Strange",
            "Collaborate quietly to navigate challenges efficiently.": "Black Widow"
        }
    },
    {
        "q": "Team Dynamics",
        "options": {
            "Motivator and morale booster.": "Captain America",
            "Creative problem solver and innovator.": "Iron Man",
            "Visionary who brings new perspectives.": "Scarlet Witch",
            "Steady, reliable, ensures deadlines are met.": "Hawkeye"
        }
    },
    {
        "q": "Stress & Crisis Management",
        "options": {
            "Calmly plan multiple contingencies.": "Doctor Strange",
            "Channel stress into productive energy.": "Hulk",
            "Confidently tackle the challenge head-on.": "Thor",
            "Adapt quickly and think on your feet.": "Spider-Man"
        }
    },
    {
        "q": "Innovation & Creativity",
        "options": {
            "Build prototypes and test rapidly.": "Iron Man",
            "Consider unconventional, multidimensional solutions.": "Doctor Strange",
            "Scout broadly for inspiration and trends.": "Falcon",
            "Use a mix of tradition and modern strategy.": "Black Panther"
        }
    },
    {
        "q": "Risk-Taking",
        "options": {
            "Cautious, weighs pros and cons carefully.": "Captain America",
            "Bold and direct, leaps in with confidence.": "Hulk",
            "Analyzes, innovates, and tests before acting.": "Iron Man",
            "Trusts intuition and creative instincts.": "Scarlet Witch"
        }
    },
    {
        "q": "Conflict Resolution",
        "options": {
            "Diplomatic, resolves quietly behind the scenes.": "Black Widow",
            "Addresses the issue head-on, openly and confidently.": "Thor",
            "Mediates, adapts, and finds compromise.": "Spider-Man",
            "Strategically navigates to the best long-term solution.": "Black Panther"
        }
    },
    {
        "q": "Motivation Style",
        "options": {
            "Lead by example, inspire through integrity.": "Captain America",
            "Motivate through innovation and challenge.": "Iron Man",
            "Inspire with vision and creativity.": "Scarlet Witch",
            "Support and encouragement, keeping morale high.": "Hawkeye"
        }
    }
]

# Collect responses
responses = {}
for i, q in enumerate(questions, start=1):
    responses[q['q']] = st.radio(f"{i}. {q['q']}", list(q['options'].keys()))

# Submit button
if st.button("Submit"):
    st.success("✅ Survey Completed! Here’s your Avenger-style profile:")
    for q in questions:
        selected_option = responses[q['q']]
        avenger = q['options'][selected_option]
        st.write(f"**{q['q']}** → *{avenger}* ({selected_option})")
