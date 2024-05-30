import streamlit as st
import pandas as pd
import utils

st.header("Page 1 of Questionnaire")

dimension = 'reality'
all_questions = pd.read_csv('questions.csv',sep=";")
filtered_questions = all_questions[all_questions['dimension'] == dimension]
page_questions = filtered_questions.to_dict(orient='records')

answers_1 = utils.display_questions(page_questions)

if st.button("Next"):
    st.session_state.answers_1 = answers_1
    st.switch_page("pages/02 Page 2.py")