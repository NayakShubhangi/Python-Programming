import streamlit as st

st.title("My First Streamlit App")
name = st.text_input("What is your name?: ")
button1 = st.button("Greet")
if button1:
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("No name is provided. . .")
