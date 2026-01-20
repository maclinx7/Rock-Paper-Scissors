import streamlit as st
import random

# Page Config
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✂️",
    layout="centered"
)

st.title("🪨📄✂️ Rock Paper Scissors")

# Initialize Session State
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "rounds" not in st.session_state:
    st.session_state.rounds = 0

choices = ["Rock", "Paper", "Scissors"]

# Game Logic
def get_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        return "User"
    else:
        return "Computer"

# UI
user_choice = st.radio("Choose your move 👇", choices, horizontal=True)

if st.button("Play 🎮"):
    computer_choice = random.choice(choices)
    result = get_winner(user_choice, computer_choice)

    st.session_state.rounds += 1

    st.subheader("Result")
    st.write(f"🧑 You chose: **{user_choice}**")
    st.write(f"💻 Computer chose: **{computer_choice}**")

    if result == "User":
        st.success("🎉 You Win!")
        st.session_state.user_score += 1
    elif result == "Computer":
        st.error("😢 Computer Wins!")
        st.session_state.computer_score += 1
    else:
        st.info("🤝 It's a Draw!")

# Scoreboard
st.divider()
st.subheader("📊 Score Board")

col1, col2, col3 = st.columns(3)
col1.metric("👤 Your Score", st.session_state.user_score)
col2.metric("💻 Computer Score", st.session_state.computer_score)
col3.metric("🔁 Rounds", st.session_state.rounds)

# Play Again / Reset
st.divider()
if st.button("🔄 Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.rounds = 0
    st.success("Game reset successfully!")
