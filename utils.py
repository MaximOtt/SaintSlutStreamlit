# Function to display numeric values as text for Likert scale
def display_value_as_text(value):
    match value:
        case -2:
            return "Strongly Disagree"
        case -1:
            return "Disgree"
        case 0:
            return "Undecided"
        case 1:
            return "Agree"
        case 2:
            return "Strongly agree"
        case _:
            return "Something is wrong"

# Function to display questions and collect answers
def display_questions(questions):
    import streamlit as st # Only works if imported inside function

    slider_values = [-2, -1, 0, 1, 2]

    answers = []
    for q in questions:
        answer = st.select_slider(
            r"$\textsf{\Large %s}$" %q['question'],
            key=q,
            options=slider_values,
            format_func=display_value_as_text,
            value=0
        )
        st.write('')
        answers.append({"question": q["question"], "dimension": q["dimension"], "answer": answer * q['reverse']})
    return answers

