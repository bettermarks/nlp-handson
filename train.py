from datasets import load_dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

micro_job_dataset = load_dataset("Short-Answer-Feedback/saf_micro_job_german")

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(micro_job_dataset["train"]["provided_answer"])
joblib.dump(vectorizer, "vectorizer.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X, micro_job_dataset["train"]["verification_feedback"]
)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

joblib.dump(classifier, "classifier.pkl")

predictions = classifier.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))
