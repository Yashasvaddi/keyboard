import streamlit as st

# Single-line text input
user_input = st.text_input("Type your secret message:")
st.write(f"{user_input}")
