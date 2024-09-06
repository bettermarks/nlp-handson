from difflib import SequenceMatcher
from enum import Enum
import joblib


class FeedbackLabel(Enum):
    INCORRECT = "Incorrect"
    PARTIALLY_CORRECT = "Partially correct"
    CORRECT = "Correct"
    UNKNOWN = "Unknown"


def _dummy_evaluate(answer, reference, question):
    reference_sim = SequenceMatcher(a=answer, b=reference).ratio()
    question_sim = SequenceMatcher(a=answer, b=question).ratio()
    print(reference_sim, question_sim)
    match (2 * reference_sim + question_sim) / 2:
        case num if num < 0.5:
            return FeedbackLabel.INCORRECT
        case num if num >= 0.5 and num < 0.9:
            return FeedbackLabel.PARTIALLY_CORRECT
        case num if num >= 0.9:
            return FeedbackLabel.CORRECT
        case _:
            return FeedbackLabel.UNKNOWN


_CLASSIFIER = joblib.load("classifier.pkl")
_VECTORIZER = joblib.load("vectorizer.pkl")


def _classify(answer, reference, question):
    features = _VECTORIZER.transform([answer])
    label_str = _CLASSIFIER.predict(features)[0]
    return FeedbackLabel(label_str)


def evaluate_answer(answer, reference, question):
    if not answer or not reference or not question:
        return FeedbackLabel.UNKNOWN
    return _classify(answer, reference, question)
