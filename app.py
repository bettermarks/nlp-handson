import streamlit as st

from feedback import FeedbackLabel, evaluate_answer

FEEDBACK_COMPONENTS = {
    FeedbackLabel.INCORRECT: st.error,
    FeedbackLabel.PARTIALLY_CORRECT: st.warning,
    FeedbackLabel.CORRECT: st.success,
    FeedbackLabel.UNKNOWN: st.info,
}

FEEDBACK_MESSAGES = {
    FeedbackLabel.INCORRECT: "Das ist leider nicht richtig.",
    FeedbackLabel.PARTIALLY_CORRECT: "Du bist auf dem richtigen Weg, aber es fehlt noch etwas.",
    FeedbackLabel.CORRECT: "Das ist richtig! Weiter so!",
    FeedbackLabel.UNKNOWN: "Die Antwort konnte nicht überprüft werden.",
}

st.title("Evaluating German short answers")

question = st.text_input("Frage:")
reference = st.text_input("Musterantwort:")
learner_answer = st.text_input("Lernerantwort:")

label = evaluate_answer(learner_answer, reference, question)

FEEDBACK_COMPONENTS[label](FEEDBACK_MESSAGES[label])
