import streamlit as st
# Title & text
st.title("Hello Streamlit 👋")
st.write("This is your first Streamlit app!")
# Input from user
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello {name}, welcome to Streamlit!")
    