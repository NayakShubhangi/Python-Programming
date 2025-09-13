import streamlit as st
from datetime import datetime
import time


def clockDigital():
    clockPlaceholder = st.empty()
    while True:
        currentTime = datetime.now().strftime("%H:%M:%S")
        clockPlaceholder.markdown(f"<h1 style='text-align: center; color: green;'>{currentTime}</h1>", unsafe_allow_html=True)
        time.sleep(1)