# nlp-handson

This repo contains starter code for the NLP Engineer job interviews. There are two parts that rely upon one another:

1. a training script (`train.py`) that downloads a dataset from the HuggingFace Hub, trains a simple bag-of-words classifier and saves both the classifier and the feature extractor
2. a streamlit app that creates a simple form and uses the classifier and feature extractor saved previously to classify answers into one of three classes

## Setup

1. Fork this repository so we have the option to create pull requests later.
2. Clone your fork.
3. Not strictly relevant, but highly recommended: create a virtual environment for project dependencies, e.g. `python -m venv venv`
4. Install requirements: `pip install -r requirements.txt`
5. Run training script: `python train.py`
6. Run streamlit app: `streamlit run app.py`

Once the above steps are done and things are working, you are ready for the interview :-)
