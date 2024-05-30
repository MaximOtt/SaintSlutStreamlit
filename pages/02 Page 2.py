import streamlit as st
import pandas as pd
import utils

st.header("Page 1 of Questionnaire")

dimension = 'theory'
all_questions = pd.read_csv('questions.csv',sep=";")
filtered_questions = all_questions[all_questions['dimension'] == dimension]
page_questions = filtered_questions.to_dict(orient='records')

answers_2 = utils.display_questions(page_questions)

if st.button("Finish"):
    st.session_state.answers_2 = answers_2
    st.switch_page("pages/03 Result.py")