import streamlit as st

# Single-line text input
user_input = st.text_input("Enter your name:")
st.write(f"Hello, {user_input}!")
