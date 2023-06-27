import pickle
import numpy as np
import xgboost as xgb

# Load the depression model and vectorizer
depression_path = '../model/xgboost_for_depression_with_vectorizer.pkl'
with open(depression_path, 'rb') as f:
    depression_objects = pickle.load(f)

depression_vectorizer = depression_objects[0]
depression_model = depression_objects[1]

# Load the anxiety model and vectorizer
anxiety_path = '../model/xgboost_for_anxiety_with_vectorizer.pkl'
with open(anxiety_path, 'rb') as f:
    anxiety_objects = pickle.load(f)

anxiety_vectorizer = anxiety_objects[0]
anxiety_model = anxiety_objects[1]

# Define a function to preprocess the input text using the appropriate vectorizer
def preprocess_text(text, vectorizer):
    # Transform the text data
    text_tfidf = vectorizer.transform([text])

    return text_tfidf

def classify_emotional_state(text):
    # Preprocess the input text
    depression_text_tfidf = preprocess_text(text, depression_vectorizer)
    anxiety_text_tfidf = preprocess_text(text, anxiety_vectorizer)
    anxiety_labels = ["General", "Anxious"]
    depression_labels = ["General", "Depressed"]

    # Use the model to predict the class probabilities
    anxiety_probs = anxiety_model.predict_proba(anxiety_text_tfidf)
    depression_probs = depression_model.predict_proba(depression_text_tfidf)

    # Get the highest probability index for anxiety
    anxiety_highest_prob_index = np.argmax(anxiety_probs)
    anxiety_highest_prob = anxiety_probs[0, anxiety_highest_prob_index]
    anxiety_label = anxiety_labels[anxiety_highest_prob_index]

    # Get the highest probability index for depression
    depression_highest_prob_index = np.argmax(depression_probs)
    depression_highest_prob = depression_probs[0, depression_highest_prob_index]
    depression_label = depression_labels[depression_highest_prob_index]

    # Determine the emotional state label based on probabilities
    if anxiety_highest_prob > depression_highest_prob:
        emotional_state_label = anxiety_label
        emotional_state_prob = anxiety_highest_prob
    elif depression_highest_prob > anxiety_highest_prob:
        emotional_state_label = depression_label
        emotional_state_prob = depression_highest_prob

    # Return the emotional state label and probability
    return {"label": emotional_state_label, "probability": emotional_state_prob}

# Test the model with some example inputs
user_input1 = "Your brain creates problems that don't exist, with anxiety we tend to assume the worst will happen. This makes us very scared to do normal things"
user_input2 = "I like dogs."
user_input3 = "I like to cut myself just to feel something"
user_input4 = "I went to the hospital to have a regular check up"

print(classify_emotional_state(user_input1))
print(classify_emotional_state(user_input2))
print(classify_emotional_state(user_input3))
print(classify_emotional_state(user_input4))