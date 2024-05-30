import streamlit as st
import pandas as pd
import numpy as np

st.header(
    "Saint or Slut?"
)

st.markdown(
    "You probably know already, but let's answer some questions and make a graph, shall we?"
)

if st.button("Start"):
    st.switch_page("pages/01 Page 1.py")


if 'answers_1' not in st.session_state:
    st.session_state.answers_1 = 0
    st.session_state.answers_2 = 0