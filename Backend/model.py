import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# ------------------ Step 1: Load Synthetic Data ------------------

df = pd.read_csv("synthetic_training_data_updated.csv")

# ------------------ Step 2: Clean Sentences ------------------

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df["cleaned_sentence"] = df["sentence"].apply(clean_text)

# ------------------ Step 3: Train-Test Split ------------------

X = df["cleaned_sentence"]
y = df["disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# ------------------ Step 4: Build NLP Classifier Pipeline ------------------

model = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=1500, ngram_range=(1,2))),
    ('clf', MultinomialNB())
])

model.fit(X_train, y_train)

# ------------------ Step 5: Evaluate Model ------------------

y_pred = model.predict(X_test)

print("\n Model Evaluation")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ------------------ Step 6: Predict from Natural Input ------------------

def predict_disease(user_input):
    cleaned_input = clean_text(user_input)
    probs = model.predict_proba([cleaned_input])[0]
    top_indices = probs.argsort()[::-1]  # sorted high to low

    print("\n============================")
    print("Top Predicted Diseases (≥ 10% confidence):")

    shown = 0
    for idx in top_indices:
        confidence = probs[idx] * 100
        if confidence < 10:
            continue  # skip low confidence predictions
        disease = model.classes_[idx]
        print(f"→ {disease} ({confidence:.2f}%)")
        shown += 1
        if shown >= 3:  # max top 3 diseases
            break

    if shown == 0:
        print(" No strong prediction could be made. Please try rephrasing your symptoms.")

    print("============================\n")

# ------------------ Step 7: CLI for User Input ------------------

while True:
    user_input = input("\n Enter your symptoms (or type 'exit' to quit):\n→ ")
    if user_input.lower() == 'exit':
        break
    predict_disease(user_input)

# ------------------ Step 8: Save the Model ------------------
# Save the trained model
with open("disease_classifier.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
