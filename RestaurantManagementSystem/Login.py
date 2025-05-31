import streamlit as st
import sys
from Model import session, admin, credentials


def authentication():
    db = session
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if not st.session_state.authenticated:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = db.query(credentials).join(admin, credentials.identityNumber == admin.identityNumber).filter(credentials.username == username).first()
            if user and user.password == password:
                st.session_state.authenticated = True
                st.success("Login Successful")
            else:
                st.error("Invalid Username or Password")
                return False
    if st.session_state.authenticated:
        st.success("You are logged in . . .")
        return True
