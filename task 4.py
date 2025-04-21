import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game")

st.title("🎯 Guess the Number Game")

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.message = "I'm thinking of a number between 1 and 100..."

st.write(st.session_state.message)

guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    st.session_state.guesses += 1
    if guess < st.session_state.number:
        st.session_state.message = "Too low! Try again."
    elif guess > st.session_state.number:
        st.session_state.message = "Too high! Try again."
    else:
        st.success(f"Correct! The number was {st.session_state.number}.")
        st.balloons()
        st.session_state.message = f"You guessed it in {st.session_state.guesses} tries!"
        # Reset the game
        st.session_state.number = random.randint(1, 100)
        st.session_state.guesses = 0

if st.button("Reset Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.message = "Game reset. I'm thinking of a new number..."
    st.rerun()