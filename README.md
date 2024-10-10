# nlp-handson

This repo contains starter code for NLP-related job interviews. There are two parts that rely upon one another:

1. a training script (`train.py`) that downloads a dataset from the HuggingFace Hub, trains a simple bag-of-words classifier and saves both the classifier and the feature extractor
2. a streamlit app that creates a simple form and uses the classifier and feature extractor saved previously to classify answers into one of three classes

## Setup

1. Clone your fork.
2. Not strictly relevant, but highly recommended: create a virtual environment for project dependencies, e.g. `python -m venv venv`
3. Install requirements: `pip install -r requirements.txt`
4. Run training script: `python train.py`
5. Run streamlit app: `streamlit run app.py`

Once the above steps are done and things are working, you are ready for the interview :-)
